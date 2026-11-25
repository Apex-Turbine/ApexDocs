# Licensing: Apex License Manager (ApexLM) & Legacy FlexNet

GageMap Classic (`GM`) supports two licensing backends configured at build/deployment time:

1. **Apex License Manager (ApexLM)** — Modern ZeroMQ-based (`CurveZMQ`) licensing service with a loopback Web Admin UI (`http://127.0.0.1:27887/`) and CLI manager.
2. **Legacy FlexNet Publisher** — Traditional FLEXnet (`libfnp64` / `lmgrd`) floating or node-locked licensing (`27000@host`).

---

## Apex License Manager (ApexLM)

Modern GageMap (`GM`) builds communicate with the local ApexLM service via encrypted ZeroMQ (`CoreApexLm` / `ApexLmLic`) and perform client registration using application identity (`gm` / `GM`), software version (`YYYY.MM`), host metadata, and license category (`ANALYSIS`).

### Operating Modes

| Mode | Description |
| --- | --- |
| **LOCAL** | Local service binds strictly to `127.0.0.1` (`27884`) and validates node-locked MAC-bound JSON licenses directly on the workstation. |
| **PASSTHROUGH** | Local service listens on `127.0.0.1` (`27884`) and forwards feature checkouts/checkins to an upstream `SERVER` instance. Supports **offline feature borrowing for up to 30 days**. |
| **SERVER** | Central license server accepting incoming requests from remote `PASSTHROUGH` services on `APEXLM_SERVER_LISTEN` (`27886`). Direct client connections to `SERVER` are rejected; administration remains loopback-only (`127.0.0.1`). |

### Network Ports & Management Web UI

Ports can be customized via system environment variables or a local `.env` / `.env.apexlm` file in the application directory:

| Port / URL | Variable | Purpose |
| --- | --- | --- |
| `http://127.0.0.1:27887/` | `APEXLM_MANAGEMENT_PORT` / `APEXLM_ADMIN_PORT` | **Local Web Admin UI** & loopback HTTP management API (tabs: Overview, Usage, Clients, Borrow, Config, Records, Logs, Audit). |
| `http://127.0.0.1:27888/` | `APEXLM_SERVER_MANAGEMENT_PORT` / `APEXLM_SERVER_ADMIN_PORT` | **Server Web Admin UI** & loopback HTTP management API. |
| `27884` | `APEXLM_PORT` | Local ApexLM ZeroMQ service port. |
| `27885` | `APEXLM_SERVER_PORT` | Server service ZeroMQ port. |
| `27886` | `APEXLM_SERVER_LISTEN` | Server external listen port for remote `PASSTHROUGH` services. |

> [!NOTE]
> The local Web UI binds to loopback (`127.0.0.1`) only and requires no separate login token when accessed locally on the host machine. Configuration, active checkouts, and audit logs are stored in SQLite (`C:\ProgramData\APEX\APEXLM\apexlm.db` on Windows or `/var/lib/apexlm/apexlm.db` on Linux).

### GageMap (`GM`) Apps & Features

Under ApexLM, GageMap Classic and its companion utilities use the following registered application IDs and feature definitions:

| Application / Feature | Type / Token Cost | Scope & Capabilities |
| --- | --- | --- |
| `GM` (App) / `VIRTUAL-MODELS` | Counted (`ANALYSIS`, 10 tokens) | Base GageMap license (`GageMap Base` / `GM_BASE`) covering model loading, visualization, animation, and grouping. |
| `GM_BASE` / `GM_PRO` | Base / Umbrella Seat | Core GageMap seat; umbrella seats automatically unlock bundled module features locally. |
| `GM_OPTIMIZER` (`PRETEST`) | Module Feature | Pre-Test Optimization (quantity and placement optimization). |
| `GM_FATIGUE` (`FATIGUE` / `BASIC_FATIGUE`) | Module Feature | High-Cycle Fatigue (HCF) Assessment, Goodman/Haigh diagrams, and Mean Stress Alignment. |
| `GM_CSS` (`CSS`) | Module Feature | Cyclic Symmetry Solutions (harmonic index mode expansion and phase search). |
| `GM_TIP_TIMING` (`GM_NSMS`) | Module Feature | Non-Intrusive Stress Measurement System (NSMS) / Tip-Timing spot probe modeling and deflection limits. |
| `GM_SCRIPTING` (`GMSCRIPT`) | Companion App / Feature | Batch Lua scripting via [GmScript](../GmScript/install.md). |
| `SDRFM` / `SDRDUMP` | Companion Apps | Standalone [SDR File Manager](../SDRFM/README.md) and SDR Dump utility. |
| `CUST_MODELING` / `VALIDATION` | Legacy Module Gates | User-defined shape import/export and displacement/vibrometry model validation. |

> [!IMPORTANT]
> ApexLM enforces version validation: if the installed application version exceeds the maximum `YYYY.MM` version authorized in the license JSON, registration succeeds as unlicensed and checkouts are declined. A background heartbeat monitors server connectivity (default 30 s interval, 300 s reconnect timeout).

---

## Legacy FlexNet Publisher

For customer environments still running **FlexNet Publisher** (`FLEXnet` version 11.4), GageMap Classic reads the license path or server address from:

- **Application Setting**: Configured via **License Product** dialog (saved in user settings).
- **Environment Variables**: `GAGEMAP_FLEX_SERVER` (primary for `GM`, `SDRFM`, and `SDRDump`) or `LM_LICENSE_FILE`.
- **Standard Server Format**: `27000@host` (e.g., `27000@license-server.company.com`) or a local `.lic` file path.

### LMUtils Command-Line & GUI Utilities

The full *FLEXnet Licensing End User Guide* is installed with the APEX/EDAS `LMUtils` package (`Start > All Programs > APEX > LMUtils > PDF Documentation` on Windows, or `/opt/APEX/doc/LicensingEndUserGuide.pdf` on Linux). Commonly used utilities include:

- `lmborrow` — Supports offline license borrowing.
- `lmdiag` — Diagnoses license checkout problems.
- `lmdown` — Shuts down the license server.
- `lmgrd` — Starts the FlexNet license server daemon.
- `lmhostid` — Reports the Host ID of a system.
- `lminstall` — Converts license files between formats.
- `lmpath` — Controls license file search path settings.
- `lmremove` — Releases a hung license back to the free pool.
- `lmreread` — Causes `lmgrd` to reread the license file and restart vendor daemons.
- `lmstat` — Displays current license server and feature checkout status.
- `lmswitch` *(Linux only)* — Controls debug log location and size.
- `lmswitchr` — Switches the report log to a new file.
- `lmtools` *(Windows only)* — Graphical utility for managing all aspects of the license server, including installing a Windows Service for automatic startup.
- `lmutil` — Unified wrapper for all FLEXnet licensing utilities.
- `lmver` — Reports the FLEXnet library/binary version.

> [!NOTE]
> APEX / EDAS FlexNet deployments use **FLEXnet version 11.4**. Earlier FlexNet servers must upgrade `lmgrd` (included in the application's `licenses` directory) to run the APEX/EDAS vendor daemon alongside older vendor daemons (v11.4 or lower).
