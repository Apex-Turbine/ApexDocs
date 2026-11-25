# Azure Pipelines & Azure Static Web Apps Deployment

`ApexDocs` uses **Azure Pipelines** ([`azure-pipelines.yml`](https://github.com/Apex-Turbine/ApexDocs/blob/main/azure-pipelines.yml)) to validate Markdown, compile standalone HTML and PDF manuals, and deploy the unified documentation site to **Azure Static Web Apps** (`apexdocs.apexturbine.com`).

## Pipeline Workflow (`azure-pipelines.yml`)

### Triggers & Checkout

- Triggers automatically on pushes and Pull Requests targeting `main` in `Apex-Turbine/ApexDocs`.
- Uses `ubuntu-latest` with:

```yaml
- checkout: self
  submodules: recursive
  fetchDepth: 1
  clean: true
```

### Stage 1: `BuildDocs`

1. Configures Python **3.12** via `UsePythonVersion@0`.
2. Installs `requirements.txt` (`mkdocs`, `mkdocs-material`, `pymdown-extensions`, `playwright`).
3. Installs Playwright Chromium and Linux system packages (`python -m playwright install --with-deps chromium`).
4. Builds and strictly validates the unified static site:
   `python build_docs.py --target site --format html --strict --output "$(Build.SourcesDirectory)/dist"`
5. Builds standalone offline HTML bundles and PDF manuals for every main folder:
   `python build_docs.py --target all --format both --output "$(Build.SourcesDirectory)/dist"`
6. Copies [`staticwebapp.config.json`](https://github.com/Apex-Turbine/ApexDocs/blob/main/staticwebapp.config.json) into `dist/site/`.
7. Publishes three downloadable pipeline artifacts:
   - `ApexDocs-PDFs` (`DS.pdf`, `DX.pdf`, `GageMap.pdf`, `DX-Plus.pdf`, `Custom-Development.pdf`)
   - `ApexDocs-Standalone-HTML` (self-contained HTML folders per product)
   - `ApexDocs-StaticSite` (production web root)

### Stage 2: `DeployStaticWebApp`

Runs automatically after `BuildDocs` succeeds on `refs/heads/main`:

- Downloads `ApexDocs-StaticSite`.
- Deploys pre-built files using `AzureStaticWebApp@0` with `skip_app_build: true` and deployment token `$(AZURE_STATIC_WEB_APPS_API_TOKEN)`.

## One-Time Setup Checklist

### 1. Create the Azure Static Web App Resource

1. In the Azure Portal, create an **Azure Static Web App** (for example `apexdocs-swa`) under the **Free** or **Standard** plan.
   - Choose **Deployment source: Other** (since Azure Pipelines performs the build and push via `AzureStaticWebApp@0`).
2. Open **Settings -> Manage deployment token** and copy the token.

### 2. Configure Azure DevOps Pipeline & Service Connection

1. In Azure DevOps, go to **Pipelines -> New pipeline -> GitHub** and authorize access to `Apex-Turbine/ApexDocs`.
   - Ensure the GitHub OAuth/App authorization can read both public/org submodules (`dxplus-doc` and `phoenix-doc`). If either submodule becomes private in the future, configure a GitHub service connection or PAT with `repo` read scope on all three repositories.
2. Select **Existing Azure Pipelines YAML file** and choose `/azure-pipelines.yml`.
3. Under **Variables**, add:
   - Name: `AZURE_STATIC_WEB_APPS_API_TOKEN`
   - Check **Keep this value secret**.

### 3. Bind Custom Domain (`apexdocs.apexturbine.com`)

Authoritative DNS for `apexturbine.com` is hosted on **Bluehost** (`ns1.bluehost.com`, `ns2.bluehost.com`).

1. In Azure Portal -> `apexdocs-swa` -> **Settings -> Custom domains -> + Add -> Custom domain on other DNS**.
2. Enter `apexdocs.apexturbine.com`. Azure provides:
   - A `CNAME` hostname (for example `<generated-id>.azurestaticapps.net`), and/or
   - A TXT ownership validation record (`_dnsauth.apexdocs`).
3. Log in to **Bluehost Domains -> Zone Editor (`apexturbine.com`)** and add the `CNAME` record:
   - **Host Record**: `apexdocs`
   - **Points to**: `<your-swa-default-hostname>.azurestaticapps.net`
   - **TTL**: `300` (5 minutes during initial verification; raise later if desired)
4. Wait for Azure validation and automatic free **Managed TLS/SSL certificate** provisioning.
5. Verify HTTPS access: `https://apexdocs.apexturbine.com/` should serve `ApexDocs` with a valid Microsoft-issued certificate.
