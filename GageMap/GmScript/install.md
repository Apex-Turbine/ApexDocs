# Install & License GmScript

## Installation

### Linux Installation

Download the main `GmScript` (`.tgz` file). Packages are installed by extracting them with the `tar` utility into the root (`/`) directory. If the package contains an installer script, it will be located under `/install/doinst.sh` and should be executed with the current directory being root (`/`).

> [!NOTE]
> The packages are built using the Slackware Linux distribution's package format because it installs cleanly across Linux distributions. Under native Slackware systems, package management utilities (`installpkg`, `removepkg`, `upgradepkg`, etc.) can be used directly. On non-Slackware distributions, installing Slackware `pkgtools` (from the `a` package series) enables clean installation, upgrades, and removal.

### Windows Installation

Download the main `GmScript` package (`.exe` or `.zip` file):

- **Installer (`.exe`)**: Recommended for standard workstations; configures Start Menu shortcuts, system files, and runtime dependencies.
- **Portable Archive (`.zip`)**: Provided for corporate environments where users do not have administrator permissions to run an installer. Extract all files into a writable directory.

---

## Licensing (`GMSCRIPT`)

> [!WARNING]
> **Legacy FLEXlm / FlexNet Discontinuation — October 2027**
> Legacy licensing using **FLEXlm / FlexNet** (`lmgrd`, `lmstat`, `lmdiag`, `lmtools`, `.lic` files, and `27000@host` servers) will be **discontinued as of October 2027**. All product versions going forward will exclusively use **[APEX License Manager](../../License%20Manager/README.md)** (`ApexLM`), the **APEX LM Daemon (`ApexLM_Service`)**, and the **APEX LM Server Daemon (`ApexLM_Server_Service`)**.

`GmScript` supports both **[APEX License Manager (ApexLM)](../../License%20Manager/README.md)** and **Legacy FlexNet Publisher** *(discontinued October 2027)*. At startup, `GmScript` checks out its license and logs licensing status and maintenance expiration dates to both console output and the script log file. If no valid license can be obtained, `GmScript` exits immediately with a non-zero exit code.

### APEX License Manager (ApexLM)

See [APEX License Manager](../../License%20Manager/README.md), [Workstation & Server Setup](../../License%20Manager/setup-and-server.md), [CLI Reference](../../License%20Manager/cli-reference.md), and [Web UI & Offline Reservations](../../License%20Manager/web-ui-and-reservations.md) for full details.

- **Registered Application**: `GMSCRIPT` (`gmscript`), license category `GMSCRIPT`.
- **Required Feature**: `GMSCRIPT` (counted feature in `ApexFeatures.csv` — *GM Scripting feature*).
- **Operating Modes**: `LOCAL`, `PASSTHROUGH` (with offline **Reserve** tab leases up to 30 days), and `SERVER`.
- **Default Ports & Admin UI**:
  - `27884` (`APEXLM_PORT`): Local ApexLM ZeroMQ service port.
  - `27885` (`APEXLM_SERVER_PORT`): Server service ZeroMQ port.
  - `27886` (`APEXLM_SERVER_LISTEN`): External listen port for `PASSTHROUGH` services.
  - `http://127.0.0.1:27887/` (`APEXLM_MANAGEMENT_PORT`): Local loopback Web Admin UI for loading licenses, inspecting active seats, and configuring `PASSTHROUGH` / `LOCAL` modes (`http://127.0.0.1:27888/` on loopback for `SERVER` admin UI).
- **Version Enforcement**: The `GmScript` software version must not exceed the `YYYY.MM` version authorized in the ApexLM license file.

### Legacy FlexNet Publisher *(Discontinued October 2027)*

- **Environment Variable**: Set `GMSCRIPT_FLEX_SERVER` (or `LM_LICENSE_FILE`) to `27000@host` or the path to a FlexNet `.lic` file.
- **Token Cost / Feature**: `GMSCRIPT` (40 `ANALYSIS` tokens in legacy token-based FlexNet licensing, or standalone `GMSCRIPT` feature).
- **Server Utilities**: Managed with `lmgrd`, `lmstat`, `lmdiag`, and `lmtools` (Windows). See [GM Licensing](../GM/flex.md) for the full `LMUtils` command reference.

---

## Runtime Requirements & Command-Line Usage

### Command-Line Syntax

```text
GmScript [-h] [--help] [-?] [--doc] [-v] [--version] [--affinity <n>] <filename.lua>
```

| Option / Argument | Description |
| --- | --- |
| `-h`, `--help`, `-?` | Print command-line usage and exit. |
| `--doc` | Launch the GmScript documentation assistant. |
| `-v`, `--version` | Print the `GmScript` version string and exit. |
| `--affinity <n>` | Set CPU affinity value for execution. |
| `<filename.lua>` | Path to the Lua script to execute (exactly one script per invocation; script must define a global `main()` function). |

### System & Third-Party Dependencies

- **Linux Display Server**: On Linux systems, `GmScript` initializes Qt GUI/font components and requires an active X11 `DISPLAY` connection (for headless servers, run under `xvfb-run` or export a valid `DISPLAY`).
- **FE Converter Runtimes** (when using `GM.ansys()` or `GM.sdrconverter()`):
  - **ANSYS**: ANSYS 2019 R2 or newer libraries (`CadoeKernel.dll` & `CadoeReader.dll` for 2021 R1+, or `CadoeCore.dll` for 2019 R2–2020 R2) must be present on `PATH` / `LD_LIBRARY_PATH`.
  - **ABAQUS**: Required Abaqus ODB runtime libraries (`2018`–`2021` or `6.14-1`; see [ABAQUS Converter Guide](../SDR%20Converter/abaqus.md)) must be on `PATH` / `LD_LIBRARY_PATH`.
- **MATLAB Exports**: Exporting `.mat` files via `GM.export()` requires MATLAB shared libraries (`libmat.dll` on Windows or `libmat.so` on Linux) on the system library path.
