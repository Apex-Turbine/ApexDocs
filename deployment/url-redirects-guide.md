# Redirecting Legacy Documentation URLs (`ds-doc.apexturbine.com` -> `apexdocs.apexturbine.com`)

## Current DNS & Hosting Inventory

DNS inspection of `*.apexturbine.com` (authoritative nameservers: `ns1.bluehost.com`, `ns2.bluehost.com`) shows the following legacy documentation records:

| Subdomain | Current DNS Record | Current Hosting Target | Target Path in `ApexDocs` |
| :--- | :--- | :--- | :--- |
| `ds-doc.apexturbine.com` | **None (`NXDOMAIN`)** | *Not currently configured in DNS* | `https://apexdocs.apexturbine.com/DS/` |
| `dsdoc.apexturbine.com` | `CNAME` -> `icy-beach-0994ed410.5.azurestaticapps.net` | Azure Static Web Apps | `https://apexdocs.apexturbine.com/DS/` |
| `dxdoc.apexturbine.com` | `CNAME` -> `blue-cliff-0dedb3110.1.azurestaticapps.net` | Azure Static Web Apps | `https://apexdocs.apexturbine.com/DX/` |
| `gmdoc.apexturbine.com` | `CNAME` -> `thankful-ground-004e06d10.1.azurestaticapps.net` | Azure Static Web Apps | `https://apexdocs.apexturbine.com/GageMap/GM/` |
| `gmxdoc.apexturbine.com` | `CNAME` -> `blue-glacier-008213b10.1.azurestaticapps.net` | Azure Static Web Apps | `https://apexdocs.apexturbine.com/GageMap/GMx/` |
| `gmscriptdoc.apexturbine.com` | `CNAME` -> `black-island-00980af10.1.azurestaticapps.net` | Azure Static Web Apps | `https://apexdocs.apexturbine.com/GageMap/GmScript/` |
| `gmtheory.apexturbine.com` | `CNAME` -> `red-bush-0459bfc10.1.azurestaticapps.net` | Azure Static Web Apps | `https://apexdocs.apexturbine.com/GageMap/GM%20Theory/` |
| `dxplusdoc.apexturbine.com` | `CNAME` -> `9847366aec-hosting.gitbook.io` | GitBook Hosting | `https://apexdocs.apexturbine.com/DX+/` |
| `apexdocs.apexturbine.com` | **None yet** | *New Azure Static Web App* | `https://apexdocs.apexturbine.com/` |

> [!NOTE]
> Notice both **`ds-doc.apexturbine.com`** (requested hyphenated hostname, currently missing from DNS) and **`dsdoc.apexturbine.com`** (currently live on Azure Static Web Apps). The recommended approach below covers **both** hostnames cleanly.

---

## Option Comparison

### Option A — Recommended: Path-Preserving 301 Redirects via Azure Static Web Apps

**Why this is best:**
- **True HTTPS with Managed TLS**: Unlike registrar/cPanel URL forwarders (which frequently fail on HTTPS bookmarks or show certificate mismatch warnings), Azure Static Web Apps automatically issues and renews valid HTTPS certificates for every custom domain bound to it.
- **Preserves Deep Links**: Existing bookmarks, Sphinx chapter URLs (`/apex-ds/...`, `/apex-dr/...`), and search-engine links receive an HTTP **301 Permanent Redirect** straight to their new destination on `apexdocs.apexturbine.com`.
- **Zero Extra Cost / Minimal Infrastructure**: Runs directly inside your existing legacy Azure Static Web App(s) (or a single consolidated Free-tier redirect SWA).

**Limitations**: An Azure Static Web App custom domain allows at most 2 custom domains on the Free tier (up to 5 on Standard tier, or use existing individual legacy SWAs in place with a redirect-only `staticwebapp.config.json`). Keeping each existing SWA temporarily with a minimal redirect config—or consolidating pairs—costs zero additional Azure spend if staying within existing SWA allocations.

### Option B — Azure Front Door (Standard/Premium) Custom Rule Engine

**When to choose**: If you want a **single** edge resource handling 10+ legacy hostnames (`ds-doc`, `dsdoc`, `dxdoc`, `gmdoc`, `gmxdoc`, `gmscriptdoc`, `gmtheory`, `dxplusdoc`) with host-header regex matching in one place.

- Bind all legacy hostnames via Bluehost `CNAME` to the Front Door endpoint (`*.azurefd.net`).
- Add one **Rule Set** inspecting `Request Header -> Host` and issuing `301` redirects to the corresponding `/DS/`, `/DX/`, `/GageMap/...`, or `/DX+/` prefix on `https://apexdocs.apexturbine.com`.
- **Tradeoff**: Costs ~$35/month minimum for Azure Front Door Standard plus per-domain/traffic fees, whereas Option A uses already-provisioned Free/Standard SWAs.

### Option C — Why NOT Bluehost / Registrar Domain Forwarding Alone

- Bluehost DNS/cPanel domain redirects operate over **plain HTTP** without automated Azure-backed TLS certificates for `https://ds-doc.apexturbine.com` or `https://dsdoc.apexturbine.com`.
- Modern browsers block or warn on `https://` requests when no matching TLS certificate exists for the redirected hostname.
- **Verdict**: Never rely on registrar HTTP forwarding for HTTPS documentation links. Always terminate TLS at Azure Static Web Apps (Option A) or Azure Front Door (Option B).

---

## Step-by-Step Implementation (Option A: Azure Static Web Apps)

### Case 1: Redirecting `ds-doc.apexturbine.com` and `dsdoc.apexturbine.com` -> `apexdocs.apexturbine.com/DS/`

Because `icy-beach-0994ed410.5.azurestaticapps.net` (`dsdoc.apexturbine.com`) is already live in Azure:

1. **Bind `ds-doc.apexturbine.com` as a second custom domain on `icy-beach-0994ed410.5.azurestaticapps.net`** (or on a dedicated lightweight SWA deployed from [`deployment/legacy-redirect-swa/`](https://github.com/Apex-Turbine/ApexDocs/tree/main/deployment/legacy-redirect-swa)):
   - In **Bluehost Zone Editor**, create a `CNAME` record:
     - **Host**: `ds-doc`
     - **Points to**: `icy-beach-0994ed410.5.azurestaticapps.net`
     - **TTL**: `300`
   - Wait for Azure Portal -> Custom Domains -> `ds-doc.apexturbine.com` TLS certificate status = **Validated / Ready**.
2. **Deploy the redirect-only artifact** to that legacy SWA using the files in `deployment/legacy-redirect-swa/`:
   - [`legacy-redirect-swa/staticwebapp.config.json`](https://github.com/Apex-Turbine/ApexDocs/blob/main/deployment/legacy-redirect-swa/staticwebapp.config.json) defines `301` permanent redirects preserving common Sphinx subpaths:
     - `/apex-ds/*` -> `https://apexdocs.apexturbine.com/DS/DS/`
     - `/apex-dr/*` -> `https://apexdocs.apexturbine.com/DS/DR/`
     - `/*` -> `https://apexdocs.apexturbine.com/DS/`
   - [`legacy-redirect-swa/index.html`](https://github.com/Apex-Turbine/ApexDocs/blob/main/deployment/legacy-redirect-swa/index.html) provides an instant `<meta http-equiv="refresh">` + canonical link fallback if any edge path bypasses route rules.

```json
{
  "routes": [
    {
      "route": "/apex-ds/*",
      "redirect": "https://apexdocs.apexturbine.com/DS/DS/",
      "statusCode": 301
    },
    {
      "route": "/apex-dr/*",
      "redirect": "https://apexdocs.apexturbine.com/DS/DR/",
      "statusCode": 301
    },
    {
      "route": "/*",
      "redirect": "https://apexdocs.apexturbine.com/DS/",
      "statusCode": 301
    }
  ]
}
```

### Case 2: Updating the Other Legacy Product SWAs & GitBook Hostname

For each remaining SWA already bound in Bluehost DNS, deploy the exact same two-file redirect folder with its product target URL substituted:

| Legacy SWA Hostname | Replace Target Base URL in Redirect Config |
| :--- | :--- |
| `dxdoc.apexturbine.com` (`blue-cliff-0dedb3110.1.azurestaticapps.net`) | `https://apexdocs.apexturbine.com/DX/` |
| `gmdoc.apexturbine.com` (`thankful-ground-004e06d10.1.azurestaticapps.net`) | `https://apexdocs.apexturbine.com/GageMap/GM/` |
| `gmxdoc.apexturbine.com` (`blue-glacier-008213b10.1.azurestaticapps.net`) | `https://apexdocs.apexturbine.com/GageMap/GMx/` |
| `gmscriptdoc.apexturbine.com` (`black-island-00980af10.1.azurestaticapps.net`) | `https://apexdocs.apexturbine.com/GageMap/GmScript/` |
| `gmtheory.apexturbine.com` (`red-bush-0459bfc10.1.azurestaticapps.net`) | `https://apexdocs.apexturbine.com/GageMap/GM%20Theory/` |
| `dxplusdoc.apexturbine.com` (currently `9847366aec-hosting.gitbook.io`) | Point Bluehost `CNAME` away from GitBook to a redirect SWA -> `https://apexdocs.apexturbine.com/DX+/` |

> [!WARNING]
> **Wait before cutting DNS for `dxplusdoc.apexturbine.com`**: Verify the new Azure Static Web App custom domain and TLS certificate first using Azure's TXT validation (`_dnsauth.dxplusdoc`), or schedule a brief cutover window, before switching the `CNAME` away from `9847366aec-hosting.gitbook.io`.

### Case 3: Why NOT Point `ds-doc.apexturbine.com` Directly to `apexdocs.apexturbine.com`?

If you point `ds-doc.apexturbine.com` directly to the main `apexdocs-swa` resource without a host-based redirect layer, visiting `https://ds-doc.apexturbine.com/` will land on the **`ApexDocs` root landing page** instead of **`/DS/`**, because Azure Static Web Apps `staticwebapp.config.json` routes match path only (not HTTP `Host` header). Using either the dedicated DS legacy SWA (`icy-beach-0994ed410.5.azurestaticapps.net`) or Azure Front Door guarantees users hit `/DS/` directly.

---

## Verification Commands After Cutover

After DNS propagation and redirect deployment, verify TLS + 301 status codes with `curl`:

```bash
curl -I https://ds-doc.apexturbine.com/
# Expect: HTTP/2 301
#         location: https://apexdocs.apexturbine.com/DS/

curl -I https://dsdoc.apexturbine.com/apex-ds/
# Expect: HTTP/2 301
#         location: https://apexdocs.apexturbine.com/DS/DS/

curl -I https://apexdocs.apexturbine.com/
# Expect: HTTP/2 200
```
