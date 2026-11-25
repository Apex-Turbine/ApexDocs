# GitHub Repository Structure & Submodules

The unified documentation portal lives on GitHub under the **`Apex-Turbine`** organization and combines standalone product manuals with two Git submodules.

## Repository Inventory

| Path in `ApexDocs` | Hosting Model | GitHub Repository | Active Migration Branch |
| :--- | :--- | :--- | :--- |
| Root, `DS/`, `DX/`, `GageMap/`, `Custom Development/DS-API/`, `deployment/` | Direct files in `ApexDocs` | `https://github.com/Apex-Turbine/ApexDocs` | `main` |
| `DX+/` | Git Submodule | `https://github.com/Apex-Turbine/dxplus-doc` | `apexdocs-migration` |
| `Custom Development/Phoenix API/` | Git Submodule | `https://github.com/Apex-Turbine/phoenix-doc` | `apexdocs-migration` |

> [!IMPORTANT]
> Why are the two submodules pinned to `apexdocs-migration` initially? Both `Apex-Turbine/dxplus-doc` and `Apex-Turbine/phoenix-doc` previously hosted GitBook repositories on `main`. Restructured, GitBook-free documentation is staged on **`apexdocs-migration`** so maintainers can review and merge into `main` cleanly without overwriting history unexpectedly.

## Cloning `ApexDocs` with Submodules

Always pass `--recurse-submodules` when cloning:

```bash
git clone --recurse-submodules https://github.com/Apex-Turbine/ApexDocs.git
cd ApexDocs
```

If the repository was already cloned without submodules, initialize them with:

```bash
git submodule update --init --recursive
```

To fast-forward both submodules to the latest commits on their configured `.gitmodules` tracking branch (`apexdocs-migration`):

```bash
git submodule update --remote --merge
```

## Editing Inside a Submodule

1. Enter the submodule and confirm you are on the tracking branch (not detached `HEAD`):

   ```bash
   cd DX+   # or "Custom Development/Phoenix API"
   git checkout apexdocs-migration
   git pull origin apexdocs-migration
   ```

2. Commit and push changes inside the submodule first:

   ```bash
   git add -A
   git commit -m "docs: update DX+ documentation"
   git push origin apexdocs-migration
   ```

3. Return to the `ApexDocs` root repository and commit the updated submodule pointer:

   ```bash
   cd ..
   git add DX+
   git commit -m "chore: bump DX+ submodule pointer"
   git push origin main
   ```

## Promoting Submodules from `apexdocs-migration` to `main`

Once your team has reviewed and approved the cleaned Markdown layout on both submodules:

1. Merge `apexdocs-migration` into `main` (via Pull Request or fast-forward merge) on **`Apex-Turbine/dxplus-doc`** and **`Apex-Turbine/phoenix-doc`**.
2. Update `branch = main` inside `.gitmodules` at the root of `ApexDocs`.
3. Run `git submodule sync && git submodule update --remote` and push the updated `.gitmodules` and submodule commits to `ApexDocs/main`.

## Content & Asset Conventions

- **Zero GitBook artifacts**: Do not re-introduce `.gitbook/`, `SUMMARY.md` GitBook sidebars, YAML `cover:` frontmatter, `{% hint %}` / `{% embed %}` Liquid tags, or `<table data-view="cards">` blocks.
- **Directory index files**: Use **`README.md`** as the landing page in every folder so browsing natively on GitHub and building with MkDocs Material behave identically.
- **Case-exact relative links**: Although Windows filesystems are case-insensitive, Azure Static Web Apps, Linux CI agents, and Git are case-sensitive. Always match exact on-disk casing in Markdown links and image paths.
- **Spaces in paths**: URL-encode spaces as `%20` in Markdown links (for example `[Phoenix API](Phoenix%20API/README.md)`, `[DB Manager](Tools/DB%20Manager/README.md)`).
