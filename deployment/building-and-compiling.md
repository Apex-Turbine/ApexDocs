# Compiling Documentation Locally (HTML & PDF)

All APEX documentation is authored in pure **GitHub-Flavored / MkDocs Material Markdown (`.md`)** and compiled using the cross-platform script [`build_docs.py`](https://github.com/Apex-Turbine/ApexDocs/blob/main/build_docs.py) at the repository root.

## Prerequisites

### Python & Packages

Python **3.11 or newer** is required. Install build dependencies from [`requirements.txt`](https://github.com/Apex-Turbine/ApexDocs/blob/main/requirements.txt):

=== "Windows (PowerShell)"

    ```powershell
    py -3.13 -m pip install --upgrade pip
    py -3.13 -m pip install -r requirements.txt
    ```

=== "Linux / macOS / CI"

    ```bash
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    ```

> [!TIP]
> On Windows systems where the `python` command opens the Microsoft Store stub, always invoke **`py -3.13`** (or use [`build.ps1`](https://github.com/Apex-Turbine/ApexDocs/blob/main/build.ps1), which selects `py -3.13` automatically).

### Browser Engine for PDF Compilation

PDF generation uses headless Chromium via **Playwright**:

- **Windows**: `build_docs.py` tries Playwright's bundled Chromium first and automatically falls back to **Microsoft Edge** (`msedge.exe`) if bundled Chromium has not been downloaded.
- **Linux / CI**: Install Playwright's headless Chromium binary and OS system libraries once:

```bash
python3 -m playwright install --with-deps chromium
```

## Build Script Usage (`build_docs.py`)

```text
build_docs.py [--target TARGET] [--format {html,pdf,both}] [--output DIR] [--strict] [--clean]
```

### Supported Targets

| `--target` Value | Source Folder | Standalone HTML Output | PDF Manual Output |
| :--- | :--- | :--- | :--- |
| `site` | Entire user-facing repository (excl. `deployment/`, CI/temp artifacts) | `dist/site/` | *N/A* (use `all` for PDFs) |
| `all` | All 7 user-facing documentation folders | `dist/html/*/` | `dist/pdf/*.pdf` |
| `DS` | `DS/` | `dist/html/DS/` | `dist/pdf/DS.pdf` |
| `DX` | `DX/` | `dist/html/DX/` | `dist/pdf/DX.pdf` |
| `GageMap` | `GageMap/` | `dist/html/GageMap/` | `dist/pdf/GageMap.pdf` |
| `DX+` | `DX+/` | `dist/html/DX-Plus/` | `dist/pdf/DX-Plus.pdf` |
| `Custom Development` | `Custom Development/` | `dist/html/Custom-Development/` | `dist/pdf/Custom-Development.pdf` |
| `License Manager` | `License Manager/` | `dist/html/License-Manager/` | `dist/pdf/License-Manager.pdf` |
| `Release Policies` | `Release Policies/` | `dist/html/Release-Policies/` | `dist/pdf/Release-Policies.pdf` |

The maintainer-only `deployment/` folder is intentionally excluded from `site` and `all` user-facing builds. Multiple `--target` flags or comma-separated values may be supplied in one command (for example `--target DS,DX`).

## Common Commands

### 1. Build the Full Azure Static Web App Site (Strict Validation)

```powershell
py -3.13 build_docs.py --target site --format html --strict
```

Staging happens inside `build/.staging/` so GitHub-style alerts (`> [!NOTE]`, `> [!WARNING]`, etc.) render as MkDocs Material admonitions in HTML while keeping the source `.md` files clean on GitHub.

### 2. Build Standalone HTML and PDF Manuals for All Main Folders

```powershell
py -3.13 build_docs.py --target all --format both
```

Wrapper scripts are also provided at the repository root:

- **Windows PowerShell**: `.\build.ps1 -Target all -Format both`
- **Linux / macOS**: `./build.sh all both`

### 3. Build a Single Product Manual (HTML Only or PDF Only)

```powershell
# Compile only DX PDF
py -3.13 build_docs.py --target DX --format pdf

# Compile only Custom Development standalone HTML
py -3.13 build_docs.py --target "Custom Development" --format html
```

## How HTML & PDF Outputs Differ

- **Unified Site (`dist/site/`)**: Built with `use_directory_urls: false` and the MkDocs Material `offline` plugin so both Azure Static Web Apps (`index.html` opening directly to **Overview**, `DOC_INDEX.html` opening to **Index**) and local `file://` disk browsing work identically without directory listings, featuring full cross-product client-side search and sticky navigation tabs (`deployment/` excluded).
- **Standalone Folder HTML (`dist/html/<product>/`)**: Built with `use_directory_urls: false` and an automatic root `index.html` -> `README.html` redirect so engineers can archive, distribute, or open offline HTML bundles directly from disk (`file://`) without a local HTTP server.
- **Standalone PDF Manuals (`dist/pdf/<product>.pdf`)**: Assembles ordered chapters (starting with `README.md`, following manual hierarchy links, then remaining pages) into a styled print document with a cover page, interactive Table of Contents, page headers/footers, page numbers, local image embedding, and callout boxes.
