# Licensing: Apex License Manager (ApexLM) & Legacy FlexNet

GageMap Next Gen (`GMx`) supports both the modern **Apex License Manager (ApexLM)** service and **Legacy FlexNet Publisher** license servers.

---

## Apex License Manager (ApexLM)

`GMx` connects to the ApexLM service over encrypted ZeroMQ (`CurveZMQ` via `CoreApexLm` / `ApexLmLic`) and registers with application name `gmx`, version (`YYYY.MM`), and license category `ANALYSIS`.

### Operating Modes

| Mode | Description |
| --- | --- |
| **LOCAL** | Connects exclusively to `127.0.0.1:27884` using a local Ed25519-signed JSON license bound to host MAC addresses. |
| **PASSTHROUGH** | Connects locally on `127.0.0.1:27884` and proxies checkouts/checkins to a central `SERVER`. Supports **offline borrowing for up to 30 days** across restarts. |
| **SERVER** | Hosts floating entitlements on `APEXLM_SERVER_LISTEN` (`27886`) for remote `PASSTHROUGH` workstations. Direct client application connections to `SERVER` are rejected. |

### Network Ports & Local Web Management Portal

Ports can be configured via environment variables or a local `.env` / `.env.apexlm` file next to the application executable:

| Port / URL | Environment Variable | Purpose |
| --- | --- | --- |
| `http://127.0.0.1:27887/` | `APEXLM_MANAGEMENT_PORT` / `APEXLM_ADMIN_PORT` | **Local Web Admin UI** (Overview, Usage, Clients, Borrow, Config, Records, Logs, Audit). |
| `http://127.0.0.1:27888/` | `APEXLM_SERVER_MANAGEMENT_PORT` / `APEXLM_SERVER_ADMIN_PORT` | **Server Web Admin UI** for central license server administration. |
| `27884` | `APEXLM_PORT` | Local ApexLM ZeroMQ service port. |
| `27885` | `APEXLM_SERVER_PORT` | Server service ZeroMQ port. |
| `27886` | `APEXLM_SERVER_LISTEN` | Server external listen port for `PASSTHROUGH` services. |

Configuration and audit records are persisted in SQLite (`C:\ProgramData\APEX\APEXLM\apexlm.db` on Windows; `/var/lib/apexlm/apexlm.db` on Linux).

### GMx Features, Optimizer & Custom Fatigue Licensing

| Application / Feature | Type / Token Cost | Capabilities Covered |
| --- | --- | --- |
| `GMx` (App) / `VIRTUAL-MODELS` | Counted (`ANALYSIS`, 10 tokens) | Required base feature (`GageMap Base` / `GM_BASE`) enabling `GMx` startup, `.gmp`/`.sdr` project loading, 3D visualization, grouping, and animation. |
| `GM_OPTIMIZER` | Module / Umbrella Feature | **Sensors Tab Optimization**: Quantity optimizer (`.gmo`) and genetic sensor placement optimization ([task_optimize.md](task_optimize.md)). |
| `GM_FATIGUE` | Module / Umbrella Feature | **Fatigue Tab Assessments**: Goodman/Haigh constant-life diagrams, group assignments (`.gml`/`.gmm`), modal scale factor limits, and sensor limit/ratio reports ([task_fatigue.md](task_fatigue.md)). |
| `GM_CSS` | Module / Umbrella Feature | Cyclic symmetry mode handling and phase search ([task_cssPhaseSearch.md](task_cssPhaseSearch.md)). |
| `GM_TIP_TIMING` | Module / Umbrella Feature | Tip-timing / NSMS spot-probe sensor modeling ([tiptiming.md](tiptiming.md)). |
| `ANSYS_CONVERTER`, `ABAQUS_CONVERTER`, `NASTRAN_CONVERTER` | Converter Entitlements | FE-to-SDR conversion via `SdrConverter` ([SDR Converter](../SDR%20Converter/README.md)). |

#### Custom Fatigue Library Support & Licensing

`GMx` supports user-compiled **Custom Fatigue Assessment Libraries** (`.dll` on Windows, `.so` on Linux) for custom temperature interpolation and limit-curve calculations:

- Custom fatigue libraries are configured under **File > Preferences > Fatigue** and enabled on a per-session basis in the **Fatigue** tab via **Use Custom Fatigue Library** (see [Custom Fatigue Library Support](custom_fatigue_library_support.md)).
- No separate ApexLM feature seat is required to load a custom `.dll`/`.so` plugin beyond your active `GMx` / fatigue license (`VIRTUAL-MODELS` / `GM_FATIGUE`). Upon selection, `GMx` automatically validates library loading and required C-interface symbols before enabling custom fatigue calculations.

> [!NOTE]
> When an umbrella seat (such as `GM_PRO`) is checked out, `ApexLmLic` caches all bundled child features locally (`m_includedFeatures`) so subsequent module checks succeed immediately with zero network round-trips.

---

## Legacy FlexNet Publisher

For legacy FlexNet deployments (`FLEXnet` version 11.4), `GMx` uses:

- **GUI Configuration**: **File > License Product** (`License File` or `License Server`, which also displays the system Host ID).
- **Environment Variables**: `GM_FLEX_SERVER` (or `LM_LICENSE_FILE`), typically set to `27000@host` or the full path to a `.lic` file.

### LMUtils Reference

The *FLEXnet Licensing End User Guide* is available via `Start > All Programs > APEX > LMUtils > PDF Documentation` (Windows) or `/opt/APEX/doc/LicensingEndUserGuide.pdf` (Linux). Standard utilities include:

- `lmborrow` — Supports license borrowing.
- `lmdiag` — Diagnoses license checkout problems.
- `lmdown` — Shuts down the license server.
- `lmgrd` — Starts the FlexNet license server.
- `lmhostid` — Reports the system Host ID.
- `lminstall` — Converts license files between formats.
- `lmpath` — Controls license file path settings.
- `lmremove` — Releases a hung license to the pool of free licenses.
- `lmreread` — Causes the license daemon to reread the license file and start new vendor daemons.
- `lmstat` — Displays license server and checkout status.
- `lmswitch` *(Linux only)* — Controls debug log location and size.
- `lmswitchr` — Switches the report log to a new file name.
- `lmtools` *(Windows only)* — Graphical license server manager (including Windows Service setup).
- `lmutil` — Combined CLI wrapper for all FLEXnet utilities.
- `lmver` — Reports the FLEXnet version of a library or binary file.

> [!NOTE]
> APEX products use **FLEXnet version 11.4**. Sites running older FlexNet servers may need to update `lmgrd` (found in the application's `licenses` directory) to serve the APEX vendor daemon alongside existing daemons of version 11.4 or lower.
