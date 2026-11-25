#!/usr/bin/env python3
"""
APEX Documentation Builder (build_docs.py)

Compiles the unified Azure Static Web App documentation portal (`dist/site`)
and individual main-folder deliverables (`DS`, `DX`, `GageMap`, `DX+`,
`Custom Development`, `License Manager`, `Release Policies`) into standalone
HTML bundles (`dist/html/`) and formatted PDF manuals (`dist/pdf/`).

Examples:
    py -3.13 build_docs.py --target site --format html --strict
    py -3.13 build_docs.py --target all --format both
    py -3.13 build_docs.py --target DS --target DX --format pdf
"""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import html
import os
import posixpath
import re
import shutil
import subprocess
import sys
import urllib.parse
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import markdown
import yaml


ROOT_DIR = Path(__file__).resolve().parent


@dataclass(frozen=True)
class TargetSpec:
    key: str
    folder: str
    slug: str
    title: str
    subtitle: str


TARGETS: Dict[str, TargetSpec] = {
    "DS": TargetSpec(
        key="DS",
        folder="DS",
        slug="DS",
        title="APEX Data System (DS) Documentation",
        subtitle="DS Acquisition, DR Remote, DM Automation, DO Output & Hardware Drivers",
    ),
    "DX": TargetSpec(
        key="DX",
        folder="DX",
        slug="DX",
        title="APEX Data Explorer (DX) Documentation",
        subtitle="Post-Test Data Visualization, Processing, Filtering & Limits Analysis",
    ),
    "GageMap": TargetSpec(
        key="GageMap",
        folder="GageMap",
        slug="GageMap",
        title="APEX GageMap Suite Documentation",
        subtitle="GageMap Classic (GM), GMx, GmScript, GM Theory, SDRFM & SDR Converter",
    ),
    "DX+": TargetSpec(
        key="DX+",
        folder="DX+",
        slug="DX-Plus",
        title="APEX DX+ Platform Documentation",
        subtitle="DX+DAQ, Online & Offline Analysis, Viewers, DB Manager & DXNet Bridges",
    ),
    "Custom Development": TargetSpec(
        key="Custom Development",
        folder="Custom Development",
        slug="Custom-Development",
        title="APEX Custom Development & API Documentation",
        subtitle="DS-API (C++, MATLAB, Python) & Phoenix API (C++, Python) Developer Guide",
    ),
    "License Manager": TargetSpec(
        key="License Manager",
        folder="License Manager",
        slug="License-Manager",
        title="APEX License Manager (ApexLM) Documentation",
        subtitle="Workstation & Floating Server Daemons, CLI Tools, Web Admin UI & Offline Reservations",
    ),
    "Release Policies": TargetSpec(
        key="Release Policies",
        folder="Release Policies",
        slug="Release-Policies",
        title="APEX Software Release Policies & License Agreement",
        subtitle="Distribution, 18-Month Version Lifecycle, System Requirements, Maintenance & End-User SLA",
    ),
}

SITE_BASE_URL = "https://apexdocs.apexturbine.com"


def _resolved_path_to_site_url(resolved: Path, frag: str = "") -> str | None:
    """Map a resolved file or directory inside ROOT_DIR to its published ApexDocs HTML URL."""
    try:
        rel_path = resolved.resolve().relative_to(ROOT_DIR.resolve())
    except ValueError:
        return None
    if resolved.is_dir():
        readme = resolved / "README.md"
        if not readme.exists():
            return None
        rel_path = readme.relative_to(ROOT_DIR)
    posix_rel = rel_path.as_posix()
    if posix_rel.lower().endswith("/readme.md"):
        html_rel = posix_rel[: -len("README.md")] + "index.html"
    elif posix_rel.lower() == "readme.md":
        html_rel = "index.html"
    elif rel_path.suffix.lower() == ".md":
        html_rel = posix_rel[:-3] + ".html"
    else:
        html_rel = posix_rel
    quoted = "/".join(urllib.parse.quote(part) for part in html_rel.split("/") if part)
    return f"{SITE_BASE_URL}/{quoted}{frag}"


def _rewrite_cross_folder_md_links(md_text: str, src_md: Path, folder_root: Path) -> str:
    """Rewrite Markdown links pointing outside a standalone target folder to the published portal URL."""
    folder_resolved = folder_root.resolve()
    root_resolved = ROOT_DIR.resolve()
    link_re = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)]+)\)")

    def _replace_line_outside_inline_code(segment: str) -> str:
        code_spans = [(cm.start(), cm.end()) for cm in re.finditer(r"`+[^`]*`+", segment)]

        def _repl(m: re.Match) -> str:
            if any(s <= m.start() < e or s < m.end() <= e for s, e in code_spans):
                return m.group(0)
            label, inner = m.group(1), m.group(2).strip()
            if inner.startswith("<"):
                end = inner.find(">")
                if end == -1:
                    return m.group(0)
                href, rest = inner[1:end], inner[end + 1 :]
            else:
                parts = inner.split(None, 1)
                href = parts[0]
                rest = f" {parts[1]}" if len(parts) > 1 else ""
            if not href or href.startswith(("http://", "https://", "mailto:", "#", "data:")):
                return m.group(0)
            frag = ""
            raw_path = href
            if "#" in href:
                raw_path, f = href.split("#", 1)
                frag = f"#{f}"
            path_part = urllib.parse.unquote(raw_path.strip())
            resolved = (src_md.parent / path_part).resolve()
            if not resolved.exists():
                return m.group(0)
            try:
                resolved.relative_to(folder_resolved)
                return m.group(0)
            except ValueError:
                pass
            try:
                resolved.relative_to(root_resolved)
            except ValueError:
                return m.group(0)
            site_url = _resolved_path_to_site_url(resolved, frag)
            if not site_url:
                return m.group(0)
            return f"[{label}]({site_url}{rest})"

        return link_re.sub(_repl, segment)

    out_lines: list[str] = []
    in_fence = False
    fence_char = ""
    fence_len = 0
    for line in md_text.splitlines(keepends=True):
        stripped = line.lstrip()
        if not in_fence:
            m_fence = re.match(r"^(`{3,}|~{3,})", stripped)
            if m_fence:
                in_fence = True
                fence_char = m_fence.group(1)[0]
                fence_len = len(m_fence.group(1))
                out_lines.append(line)
                continue
        else:
            m_close = re.match(rf"^({re.escape(fence_char)}{{{fence_len},}})\s*$", stripped)
            if m_close:
                in_fence = False
                out_lines.append(line)
                continue
            out_lines.append(line)
            continue

        out_lines.append(_replace_line_outside_inline_code(line))

    return "".join(out_lines)

ALERT_MAP = {
    "NOTE": "note",
    "TIP": "tip",
    "IMPORTANT": "info",
    "WARNING": "warning",
    "CAUTION": "danger",
}

ALERT_LABELS = {
    "NOTE": "Note",
    "TIP": "Tip",
    "IMPORTANT": "Important",
    "WARNING": "Warning",
    "CAUTION": "Caution",
}


# ---------------------------------------------------------------------------
# Markdown pre-processing helpers
# ---------------------------------------------------------------------------

def convert_github_alerts_for_mkdocs(md_text: str) -> str:
    """Convert GitHub `> [!NOTE]` callouts into MkDocs Material `!!! note` blocks."""
    lines = md_text.splitlines()
    out: List[str] = []
    in_fence = False
    fence_marker = ""
    i = 0
    while i < len(lines):
        line = lines[i]
        fence_m = re.match(r"^\s*(```+|~~~+)", line)
        if fence_m:
            marker = fence_m.group(1)[0]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
            out.append(line)
            i += 1
            continue

        if not in_fence:
            alert_m = re.match(r"^\s*>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*(.*)$", line, re.I)
            if alert_m:
                kind = alert_m.group(1).upper()
                mk_kind = ALERT_MAP[kind]
                extra_title = alert_m.group(2).strip()
                header = f'!!! {mk_kind} "{extra_title}"' if extra_title else f"!!! {mk_kind}"
                out.append(header)
                i += 1
                while i < len(lines) and re.match(r"^\s*>", lines[i]):
                    body_line = re.sub(r"^\s*>\s?", "", lines[i])
                    out.append(f"    {body_line}" if body_line else "")
                    i += 1
                continue

        out.append(line)
        i += 1
    return "\n".join(out) + ("\n" if md_text.endswith("\n") else "")


def convert_github_alerts_for_html(md_text: str) -> str:
    """Convert GitHub `> [!NOTE]` callouts into clean HTML div callout blocks for PDF."""
    lines = md_text.splitlines()
    out: List[str] = []
    in_fence = False
    fence_marker = ""
    i = 0
    while i < len(lines):
        line = lines[i]
        fence_m = re.match(r"^\s*(```+|~~~+)", line)
        if fence_m:
            marker = fence_m.group(1)[0]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
            out.append(line)
            i += 1
            continue

        if not in_fence:
            alert_m = re.match(r"^\s*>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*(.*)$", line, re.I)
            if alert_m:
                kind = alert_m.group(1).upper()
                label = alert_m.group(2).strip() or ALERT_LABELS[kind]
                body_lines: List[str] = []
                i += 1
                while i < len(lines) and re.match(r"^\s*>", lines[i]):
                    body_lines.append(re.sub(r"^\s*>\s?", "", lines[i]))
                    i += 1
                body_html = markdown.markdown(
                    "\n".join(body_lines),
                    extensions=["tables", "fenced_code", "sane_lists"],
                )
                out.append(
                    f'<div class="apex-callout apex-callout-{kind.lower()}">'
                    f'<div class="apex-callout-title">{html.escape(label)}</div>'
                    f'<div class="apex-callout-body">{body_html}</div>'
                    f"</div>"
                )
                out.append("")
                continue

        out.append(line)
        i += 1
    return "\n".join(out) + "\n"


def extract_title(md_path: Path) -> str:
    text = md_path.read_text(encoding="utf-8", errors="replace")
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("# "):
            return s[2:].strip()
    return md_path.stem.replace("-", " ").replace("_", " ").title()


# ---------------------------------------------------------------------------
# Staging for MkDocs HTML compilation
# ---------------------------------------------------------------------------

SKIP_COPY_DIRS = {
    ".git",
    "build",
    "dist",
    "site",
    ".venv",
    "venv",
    "__pycache__",
    "legacy-redirect-swa",
    "config",
    "deployment",
}

SKIP_EXTS = {".dpd", ".xlsx", ".rst", ".dox", ".odt"}


def stage_tree(src_dirs: Sequence[Path], dst_docs_dir: Path, strip_prefix: Optional[Path] = None):
    if dst_docs_dir.exists():
        shutil.rmtree(dst_docs_dir)
    dst_docs_dir.mkdir(parents=True, exist_ok=True)

    # Always copy shared stylesheets/js assets into staged docs root
    assets_src = ROOT_DIR / "assets"
    if assets_src.exists():
        shutil.copytree(assets_src, dst_docs_dir / "assets", dirs_exist_ok=True)

    def copy_item(src: Path, rel: Path):
        dst = dst_docs_dir / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.suffix.lower() == ".md":
            raw = src.read_text(encoding="utf-8", errors="replace")
            if strip_prefix is not None and strip_prefix != ROOT_DIR:
                raw = _rewrite_cross_folder_md_links(raw, src, strip_prefix)
            dst.write_text(convert_github_alerts_for_mkdocs(raw), encoding="utf-8")
        else:
            shutil.copy2(src, dst)

    for sdir in src_dirs:
        if sdir.is_file():
            rel = sdir.relative_to(ROOT_DIR) if strip_prefix is None else sdir.relative_to(strip_prefix)
            copy_item(sdir, rel)
            continue
        for root, dirs, files in os.walk(sdir):
            root_p = Path(root)
            dirs[:] = [d for d in sorted(dirs) if d not in SKIP_COPY_DIRS and not d.startswith(".")]
            for fn in sorted(files):
                if fn.startswith(("~$", ".")) or fn in {"CMakeLists.txt", "azure-pipelines.yml", "staticwebapp.config.json", "requirements.txt", "build_docs.py", "build.ps1", "build.sh"}:
                    continue
                fp = root_p / fn
                if fp.suffix.lower() in SKIP_EXTS:
                    continue
                if root_p == ROOT_DIR and fn not in {"README.md", "DOC_INDEX.md"}:
                    continue
                rel = fp.relative_to(strip_prefix or ROOT_DIR)
                copy_item(fp, rel)


def make_mkdocs_config(
    cfg_path: Path,
    docs_dir: Path,
    site_dir: Path,
    site_name: str,
    nav: Optional[List] = None,
    use_directory_urls: bool = True,
):
    base_cfg = yaml.unsafe_load((ROOT_DIR / "config" / "mkdocs.yml").read_text(encoding="utf-8"))
    base_cfg["site_name"] = site_name
    base_cfg["docs_dir"] = str(docs_dir.resolve())
    base_cfg["site_dir"] = str(site_dir.resolve())
    base_cfg["use_directory_urls"] = use_directory_urls
    base_cfg.pop("exclude_docs", None)
    if not use_directory_urls:
        # Offline bundles must not emit canonical remote site_url tags
        base_cfg.pop("site_url", None)
    if nav is not None:
        base_cfg["nav"] = nav
    else:
        base_cfg.pop("nav", None)
    cfg_path.parent.mkdir(parents=True, exist_ok=True)
    cfg_path.write_text(yaml.dump(base_cfg, sort_keys=False, allow_unicode=True), encoding="utf-8")


def run_mkdocs_build(cfg_path: Path, strict: bool) -> None:
    cmd = [sys.executable, "-m", "mkdocs", "build", "-f", str(cfg_path), "--clean"]
    if strict:
        cmd.append("--strict")
    proc = subprocess.run(cmd, cwd=str(ROOT_DIR))
    if proc.returncode != 0:
        raise RuntimeError(f"MkDocs build failed ({proc.returncode}) for config {cfg_path}")


def ensure_offline_index(out_dir: Path):
    """When use_directory_urls=False, MkDocs emits README.html; add index.html redirect if absent."""
    idx = out_dir / "index.html"
    readme_html = out_dir / "README.html"
    if not idx.exists() and readme_html.exists():
        idx.write_text(
            '<!DOCTYPE html><html><head><meta charset="utf-8">'
            '<meta http-equiv="refresh" content="0; url=README.html">'
            '<title>APEX Documentation</title></head>'
            '<body><p>Redirecting to <a href="README.html">README.html</a>...</p></body></html>\n',
            encoding="utf-8",
        )


def build_unified_site(output_dir: Path, strict: bool) -> Path:
    print("\n=== Building unified static site -> dist/site ===")
    stage_root = ROOT_DIR / "build" / ".staging" / "site"
    docs_dir = stage_root / "docs"
    site_dir = output_dir / "site"

    top_sources = [
        ROOT_DIR / "README.md",
        ROOT_DIR / "DOC_INDEX.md",
        ROOT_DIR / "DS",
        ROOT_DIR / "DX",
        ROOT_DIR / "GageMap",
        ROOT_DIR / "DX+",
        ROOT_DIR / "Custom Development",
        ROOT_DIR / "License Manager",
        ROOT_DIR / "Release Policies",
    ]
    stage_tree(top_sources, docs_dir, strip_prefix=ROOT_DIR)

    base_cfg = yaml.unsafe_load((ROOT_DIR / "config" / "mkdocs.yml").read_text(encoding="utf-8"))
    nav = base_cfg.get("nav")
    cfg_path = stage_root / "mkdocs.yml"
    make_mkdocs_config(cfg_path, docs_dir, site_dir, "APEX Documentation", nav=nav, use_directory_urls=False)
    run_mkdocs_build(cfg_path, strict=strict)
    swa_cfg = ROOT_DIR / "staticwebapp.config.json"
    if swa_cfg.exists():
        shutil.copy2(swa_cfg, site_dir / "staticwebapp.config.json")
    print(f"  [OK] Built static site at {site_dir}")
    return site_dir


def build_folder_html(spec: TargetSpec, output_dir: Path, strict: bool) -> Path:
    print(f"\n=== Building standalone HTML for {spec.key} -> dist/html/{spec.slug} ===")
    src_folder = ROOT_DIR / spec.folder
    if not src_folder.exists():
        raise FileNotFoundError(f"Source folder does not exist: {src_folder}")

    stage_root = ROOT_DIR / "build" / ".staging" / f"html-{spec.slug}"
    docs_dir = stage_root / "docs"
    html_dir = output_dir / "html" / spec.slug
    stage_tree([src_folder], docs_dir, strip_prefix=src_folder)

    cfg_path = stage_root / "mkdocs.yml"
    make_mkdocs_config(cfg_path, docs_dir, html_dir, spec.title, nav=None, use_directory_urls=False)
    run_mkdocs_build(cfg_path, strict=strict)
    ensure_offline_index(html_dir)
    print(f"  [OK] Built standalone HTML at {html_dir}")
    return html_dir


# ---------------------------------------------------------------------------
# PDF compilation via Playwright Chromium / Microsoft Edge
# ---------------------------------------------------------------------------

LINK_PRIORITY_HINTS = [
    "README.md",
    "overview",
    "introduction",
    "installation",
    "licensing",
    "interface",
    "setup",
    "plots",
    "general",
    "devices",
    "processors",
    "outputs",
]


def discover_ordered_markdown(folder: Path) -> List[Path]:
    """Order README.md first, then follow README link order, then remaining files naturally."""
    all_mds = sorted(
        (p.resolve() for p in folder.rglob("*.md") if not any(part in SKIP_COPY_DIRS for part in p.parts)),
        key=lambda p: (len(p.relative_to(folder).parts), str(p).lower()),
    )
    all_set = set(all_mds)
    ordered: List[Path] = []
    visited: set[Path] = set()

    def walk_links(md_path: Path):
        if md_path in visited or md_path not in all_set:
            return
        visited.add(md_path)
        ordered.append(md_path)
        txt = md_path.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", txt):
            raw_t = urllib.parse.unquote(m.group(1).split("#")[0].strip())
            if not raw_t or raw_t.startswith(("http://", "https://", "mailto:", "#")):
                continue
            cand = (md_path.parent / raw_t).resolve()
            if cand.is_dir():
                cand = (cand / "README.md").resolve()
            if cand in all_set and cand not in visited:
                walk_links(cand)

    root_readme = (folder / "README.md").resolve()
    if root_readme in all_set:
        walk_links(root_readme)

    for p in all_mds:
        if p not in visited:
            walk_links(p)
    return ordered


def _md_anchor_id(src_folder: Path, md_path: Path) -> str:
    rel = md_path.relative_to(src_folder).as_posix()
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", rel[:-3]).strip("-").lower()
    return f"doc-{slug}"


def rewrite_links_and_images_for_pdf(
    html_body: str,
    md_path: Path,
    src_folder: Path,
    doc_id_map: Dict[Path, str],
) -> str:
    def repl_img(m: re.Match) -> str:
        pre, src_val, post = m.group(1), m.group(2), m.group(3)
        raw = urllib.parse.unquote(src_val.split("#")[0].strip())
        if raw.startswith(("http://", "https://", "data:", "file://")):
            return m.group(0)
        resolved = (md_path.parent / raw).resolve()
        if resolved.exists():
            return f'{pre}{resolved.as_uri()}{post}'
        return m.group(0)

    def repl_href(m: re.Match) -> str:
        pre, href_val, post = m.group(1), m.group(2), m.group(3)
        if href_val.startswith(("http://", "https://", "mailto:", "#")):
            return m.group(0)
        frag = ""
        raw_path = href_val
        if "#" in href_val:
            raw_path, f = href_val.split("#", 1)
            frag = f"#{f}"
        path_part = urllib.parse.unquote(raw_path.strip())
        resolved = (md_path.parent / path_part).resolve()
        if resolved.is_dir():
            resolved = (resolved / "README.md").resolve()
        if resolved in doc_id_map:
            return f'{pre}#{doc_id_map[resolved]}{post}'
        site_url = _resolved_path_to_site_url(resolved, frag)
        if site_url:
            return f'{pre}{site_url}{post}'
        return m.group(0)

    html_body = re.sub(r'(<img\b[^>]*\bsrc=")([^"]+)(")', repl_img, html_body, flags=re.I)
    html_body = re.sub(r'(<a\b[^>]*\bhref=")([^"]+)(")', repl_href, html_body, flags=re.I)
    return html_body


def svg_data_uri(svg_path: Path) -> str:
    if not svg_path.exists():
        return ""
    encoded = base64.b64encode(svg_path.read_bytes()).decode("ascii")
    return f"data:image/svg+xml;base64,{encoded}"


def promote_mermaid_blocks_for_pdf(html_body: str) -> str:
    return re.sub(
        r'<pre><code class="language-mermaid">(.*?)</code></pre>',
        r'<div class="mermaid-diagram"><pre class="mermaid">\1</pre></div>',
        html_body,
        flags=re.S,
    )


def assemble_book_html(spec: TargetSpec, src_folder: Path, work_dir: Path) -> Path:
    ordered_mds = discover_ordered_markdown(src_folder)
    doc_id_map = {p: _md_anchor_id(src_folder, p) for p in ordered_mds}

    toc_entries: List[str] = []
    sections_html: List[str] = []

    md_converter = markdown.Markdown(
        extensions=[
            "tables",
            "fenced_code",
            "def_list",
            "footnotes",
            "attr_list",
            "sane_lists",
            "pymdownx.arithmatex",
        ],
        extension_configs={"pymdownx.arithmatex": {"generic": True}},
    )

    for idx, md_path in enumerate(ordered_mds):
        rel_posix = md_path.relative_to(src_folder).as_posix()
        doc_title = extract_title(md_path)
        anchor_id = doc_id_map[md_path]
        depth = len(md_path.relative_to(src_folder).parts) - 1
        toc_cls = "toc-top" if depth == 0 else "toc-sub"
        toc_entries.append(
            f'<li class="{toc_cls}"><a href="#{anchor_id}">{html.escape(doc_title)}</a> '
            f'<span class="toc-path">{html.escape(rel_posix)}</span></li>'
        )

        raw_md = md_path.read_text(encoding="utf-8", errors="replace")
        prep_md = convert_github_alerts_for_html(raw_md)
        md_converter.reset()
        rendered = md_converter.convert(prep_md)
        rendered = promote_mermaid_blocks_for_pdf(rendered)
        rendered = rewrite_links_and_images_for_pdf(rendered, md_path, src_folder, doc_id_map)

        page_break = "page-break-before: always;" if idx > 0 else ""
        sections_html.append(
            f'<section id="{anchor_id}" class="doc-section" style="{page_break}">'
            f'<div class="doc-breadcrumb">{html.escape(spec.key)} / {html.escape(rel_posix)}</div>'
            f'{rendered}'
            f'</section>'
        )

    today = dt.date.today().isoformat()
    mermaid_js_uri = (ROOT_DIR / "assets" / "javascripts" / "mermaid.min.js").resolve().as_uri()
    logo_dark_uri = svg_data_uri(ROOT_DIR / "assets" / "images" / "apex-logo-dark.svg")
    logo_img_html = f'<img class="cover-logo" src="{logo_dark_uri}" alt="APEX">' if logo_dark_uri else ""

    book_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{html.escape(spec.title)}</title>
<script src="{mermaid_js_uri}"></script>
<style>
  @page {{
    size: Letter;
    margin: 0.78in 0.7in 0.78in 0.7in;
  }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.5;
    color: #1e293b;
    margin: 0;
  }}
  .cover-page {{
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 9.2in;
  }}
  .cover-hero {{
    background: linear-gradient(135deg, #151515 0%, #092c48 100%);
    color: #f5f5f5;
    padding: 0.55in 0.5in 0.6in 0.5in;
    border-radius: 8px;
    border-bottom: 6px solid #4488f7;
  }}
  .cover-logo {{
    max-width: 240px;
    height: auto;
    border: none;
    margin: 0 0 24px 0;
    display: block;
  }}
  .cover-kicker {{
    font-size: 10.5pt;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #4488f7;
    margin-bottom: 10px;
  }}
  .cover-title {{
    font-size: 25pt;
    font-weight: 800;
    color: #f5f5f5;
    border: none;
    padding: 0;
    margin: 0 0 12px 0;
    line-height: 1.18;
  }}
  .cover-subtitle {{
    font-size: 12.5pt;
    color: #cbd5e1;
    margin: 0;
    line-height: 1.45;
  }}
  .cover-meta {{
    border-top: 2px solid #092c48;
    padding-top: 14px;
    font-size: 9.5pt;
    color: #475569;
  }}
  .toc-page {{
    page-break-after: always;
  }}
  .toc-page h2 {{
    color: #092c48;
    border-bottom: 2px solid #4488f7;
    padding-bottom: 6px;
  }}
  .toc-list {{
    list-style: none;
    padding-left: 0;
  }}
  .toc-list li {{
    margin: 5px 0;
    display: flex;
    justify-content: space-between;
    border-bottom: 1px dotted #e2e8f0;
    padding-bottom: 2px;
  }}
  .toc-list li.toc-top {{
    font-weight: 600;
    margin-top: 9px;
  }}
  .toc-list li.toc-sub {{
    padding-left: 16px;
  }}
  .toc-list a {{
    color: #0060ac;
    text-decoration: none;
  }}
  .toc-path {{
    font-family: Consolas, monospace;
    font-size: 8pt;
    color: #64748b;
  }}
  .doc-breadcrumb {{
    font-size: 8pt;
    font-family: Consolas, monospace;
    color: #64748b;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 3px;
    margin-bottom: 10px;
  }}
  h1 {{ font-size: 18pt; color: #092c48; border-bottom: 2px solid #4488f7; padding-bottom: 4px; margin-top: 0; }}
  h2 {{ font-size: 13.5pt; color: #0060ac; margin-top: 1.3em; page-break-after: avoid; }}
  h3 {{ font-size: 11.5pt; color: #092c48; margin-top: 1.1em; page-break-after: avoid; }}
  p, li {{ orphans: 3; widows: 3; }}
  a {{ color: #0060ac; }}
  code {{
    font-family: Consolas, "Courier New", monospace;
    background: #f1f5f9;
    padding: 1px 4px;
    border-radius: 3px;
    font-size: 8.8pt;
  }}
  pre {{
    background: #151515;
    color: #f5f5f5;
    padding: 10px 12px;
    border-radius: 5px;
    font-size: 8.3pt;
    line-height: 1.4;
    white-space: pre-wrap;
    word-break: break-word;
    page-break-inside: avoid;
  }}
  pre code {{
    background: transparent;
    color: inherit;
    padding: 0;
  }}
  pre.mermaid {{
    background: #f8fafc;
    color: #1e293b;
    border: 1px solid #cbd5e1;
    padding: 12px;
    border-radius: 6px;
  }}
  .mermaid-diagram {{
    margin: 14px 0;
    text-align: center;
    page-break-inside: avoid;
  }}
  .mermaid-diagram svg {{
    max-width: 100% !important;
    height: auto !important;
    max-height: 7.2in;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0;
    font-size: 8.5pt;
    page-break-inside: avoid;
  }}
  th, td {{
    border: 1px solid #cbd5e1;
    padding: 5px 7px;
    text-align: left;
    vertical-align: top;
  }}
  th {{
    background: #092c48;
    color: #f5f5f5;
    font-weight: 700;
  }}
  img {{
    max-width: 100%;
    max-height: 7.2in;
    height: auto;
    display: block;
    margin: 10px auto;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    page-break-inside: avoid;
  }}
  .doc-section img[src$="apex-logo-dark.svg"],
  .doc-section img[src$="dxplus-logo-dark.svg"] {{
    background: #151515;
    padding: 10px 16px;
    border: 1px solid #092c48;
    max-width: 280px;
  }}
  blockquote {{
    border-left: 4px solid #94a3b8;
    margin: 10px 0;
    padding: 4px 12px;
    color: #334155;
    background: #f8fafc;
  }}
  .apex-callout {{
    border-left: 4px solid #4488f7;
    background: #f8fafc;
    padding: 8px 12px;
    margin: 12px 0;
    border-radius: 0 4px 4px 0;
    page-break-inside: avoid;
  }}
  .apex-callout-title {{
    font-weight: 700;
    color: #092c48;
    margin-bottom: 4px;
  }}
  .apex-callout-warning, .apex-callout-caution {{
    border-left-color: #d97706;
    background: #fffbeb;
  }}
  .apex-callout-warning .apex-callout-title, .apex-callout-caution .apex-callout-title {{
    color: #92400e;
  }}
  .apex-callout-tip {{
    border-left-color: #059669;
    background: #ecfdf5;
  }}
</style>
</head>
<body>
  <div class="cover-page">
    <div class="cover-hero">
      {logo_img_html}
      <div class="cover-kicker">APEX Testing Technologies</div>
      <h1 class="cover-title">{html.escape(spec.title)}</h1>
      <p class="cover-subtitle">{html.escape(spec.subtitle)}</p>
    </div>
    <div class="cover-meta">
      <strong>Repository:</strong> ApexDocs ({html.escape(spec.folder)}/)<br>
      <strong>Generated:</strong> {today}<br>
      <strong>Sections Compiled:</strong> {len(ordered_mds)} documents
    </div>
  </div>
  <div class="toc-page">
    <h2>Table of Contents</h2>
    <ul class="toc-list">
      {''.join(toc_entries)}
    </ul>
  </div>
  {''.join(sections_html)}
<script>
window.__mermaidErrors = [];
(async () => {{
  try {{
    mermaid.initialize({{
      startOnLoad: false,
      securityLevel: "loose",
      theme: "base",
      themeVariables: {{
        primaryColor: "#e8f1fe",
        primaryTextColor: "#092c48",
        primaryBorderColor: "#4488f7",
        lineColor: "#092c48",
        secondaryColor: "#f1f5f9",
        tertiaryColor: "#ffffff",
        fontFamily: "Segoe UI, Roboto, Arial, sans-serif"
      }}
    }});
    const nodes = document.querySelectorAll("pre.mermaid");
    for (const node of nodes) {{
      try {{
        await mermaid.run({{ nodes: [node] }});
      }} catch (err) {{
        window.__mermaidErrors.push(String(err));
      }}
    }}
  }} catch (err) {{
    window.__mermaidErrors.push(String(err));
  }} finally {{
    window.__mermaidDone = true;
  }}
}})();
</script>
</body>
</html>
"""
    work_dir.mkdir(parents=True, exist_ok=True)
    html_file = work_dir / f"{spec.slug}.print.html"
    html_file.write_text(book_html, encoding="utf-8")
    return html_file


def launch_browser_for_pdf(playwright_obj):
    edge_win = Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
    edge_win64 = Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe")
    try:
        return playwright_obj.chromium.launch(headless=True)
    except Exception:
        for exe in (edge_win, edge_win64):
            if exe.exists():
                return playwright_obj.chromium.launch(executable_path=str(exe), headless=True)
        return playwright_obj.chromium.launch(channel="msedge", headless=True)


def build_pdfs(specs: Sequence[TargetSpec], output_dir: Path) -> List[Path]:
    from playwright.sync_api import sync_playwright

    pdf_dir = output_dir / "pdf"
    pdf_dir.mkdir(parents=True, exist_ok=True)
    work_dir = ROOT_DIR / "build" / ".staging" / "pdf-html"
    produced: List[Path] = []
    logo_light_uri = svg_data_uri(ROOT_DIR / "assets" / "images" / "apex-logo-light.svg")
    hdr_logo = f'<img src="{logo_light_uri}" style="height:14px;width:auto;vertical-align:middle;margin-right:8px;" />' if logo_light_uri else ""

    with sync_playwright() as p:
        browser = launch_browser_for_pdf(p)
        try:
            page = browser.new_page()
            for spec in specs:
                print(f"\n=== Compiling PDF for {spec.key} -> dist/pdf/{spec.slug}.pdf ===")
                src_folder = ROOT_DIR / spec.folder
                book_html = assemble_book_html(spec, src_folder, work_dir)
                out_pdf = pdf_dir / f"{spec.slug}.pdf"
                page.goto(book_html.as_uri(), wait_until="load")
                page.wait_for_function("window.__mermaidDone === true", timeout=60000)
                m_errs = page.evaluate("window.__mermaidErrors")
                if m_errs:
                    raise RuntimeError(f"Mermaid rendering errors in {spec.key} PDF: {m_errs}")
                page.pdf(
                    path=str(out_pdf),
                    format="Letter",
                    print_background=True,
                    display_header_footer=True,
                    header_template=(
                        f'<div style="font-size:7.5pt;color:#64748b;width:100%;padding:0 0.7in;'
                        f'display:flex;justify-content:space-between;align-items:center;">'
                        f'<span style="display:flex;align-items:center;">{hdr_logo}<span>APEX Documentation</span></span>'
                        f'<span>{html.escape(spec.title)}</span></div>'
                    ),
                    footer_template=(
                        '<div style="font-size:7.5pt;color:#64748b;width:100%;padding:0 0.7in;'
                        'display:flex;justify-content:space-between;">'
                        '<span>apexdocs.apexturbine.com</span>'
                        '<span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>'
                    ),
                )
                print(f"  [OK] Built PDF {out_pdf} ({out_pdf.stat().st_size:,} bytes)")
                produced.append(out_pdf)
        finally:
            browser.close()
    return produced


# ---------------------------------------------------------------------------
# CLI Entrypoint
# ---------------------------------------------------------------------------

def resolve_targets(raw_targets: Sequence[str]) -> Tuple[bool, List[TargetSpec]]:
    tokens: List[str] = []
    for item in raw_targets:
        tokens.extend(t.strip() for t in item.split(",") if t.strip())
    if not tokens:
        tokens = ["all"]

    build_site = False
    specs: List[TargetSpec] = []
    lookup = {k.lower(): v for k, v in TARGETS.items()}
    lookup["dx-plus"] = TARGETS["DX+"]
    lookup["custom-development"] = TARGETS["Custom Development"]
    lookup["license-manager"] = TARGETS["License Manager"]
    lookup["release-policies"] = TARGETS["Release Policies"]

    for tok in tokens:
        tl = tok.lower()
        if tl == "site":
            build_site = True
        elif tl == "all":
            specs = list(TARGETS.values())
        elif tl in lookup:
            spec = lookup[tl]
            if spec not in specs:
                specs.append(spec)
        else:
            valid = ", ".join(["site", "all"] + list(TARGETS.keys()))
            raise SystemExit(f"Unknown --target '{tok}'. Valid options: {valid}")
    return build_site, specs


def main() -> int:
    parser = argparse.ArgumentParser(description="Compile APEX documentation to HTML and PDF.")
    parser.add_argument(
        "--target",
        action="append",
        default=[],
        help="Target to build: site, all, DS, DX, GageMap, DX+, Custom Development, License Manager, Release Policies (repeatable or comma-separated).",
    )
    parser.add_argument(
        "--format",
        choices=["html", "pdf", "both"],
        default="both",
        help="Output format for folder targets (default: both). Unified 'site' always builds HTML.",
    )
    parser.add_argument(
        "--output",
        default="dist",
        help="Output root directory relative to repo root or absolute path (default: dist).",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Enable MkDocs --strict mode to fail on warnings or unresolved links.",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove build/staging and target output directories before building.",
    )
    args = parser.parse_args()

    output_dir = Path(args.output)
    if not output_dir.is_absolute():
        output_dir = (ROOT_DIR / output_dir).resolve()

    if args.clean:
        for p in (ROOT_DIR / "build", output_dir):
            if p.exists():
                shutil.rmtree(p)

    build_site, specs = resolve_targets(args.target)

    if build_site:
        build_unified_site(output_dir, strict=args.strict)

    if specs:
        if args.format in ("html", "both"):
            for spec in specs:
                build_folder_html(spec, output_dir, strict=args.strict)
        if args.format in ("pdf", "both"):
            build_pdfs(specs, output_dir)

    print("\nBuild complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
