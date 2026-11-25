# CLI Tools Reference

**APEX License Manager (`ApexLM`)** provides dedicated command-line utilities for workstation administration, central floating license servers, OS service registration, and tray control. Administrative CLIs discover the live daemon via `management.endpoint` and communicate strictly over the local loopback HTTP management API (`127.0.0.1`).

> [!WARNING]
> Legacy FlexNet CLI utilities (`lmutil`, `lmstat`, `lmdiag`, `lmborrow`, `lmgrd`) apply only to legacy releases and will be **discontinued as of October 2027**. Use `ApexLM_CLI`, `ApexLM_Server_CLI`, `ApexLM_Service`, and `ApexLM_Server_Service` for all current and future APEX deployments.

---

## 1. Workstation Manager CLI (`ApexLM_CLI`)

Manage the local **APEX LM Daemon** (`ApexLM_Service`, prompt `ApexLM> `, default admin endpoint `http://127.0.0.1:27887/`). Note that `ApexLM_CLI` automatically refuses connections to a `SERVER`-mode daemon — use `ApexLM_Server_CLI` on central license server hosts.

### Execution Modes

- **Interactive Shell**: Run with no arguments to enter the `ApexLM> ` prompt *(single-instance guarded across workstation managers)*:
  ```powershell
  ApexLM_CLI.exe
  ```
- **Non-Interactive One-Shot Execution**: Pass any CLI command directly on the command line for batch scripts and Ansible/PowerShell automation:
  ```powershell
  ApexLM_CLI.exe status
  ApexLM_CLI.exe counts
  ApexLM_CLI.exe setsrvmode PASSTHROUGH
  ApexLM_CLI.exe loadlic "C:\Licenses\workstation.json"
  ```

### Command Reference

| Command | Arguments | Description |
| :--- | :--- | :--- |
| `connect` | — | Discover `management.endpoint` and connect to the local workstation daemon. |
| `disconnect` | — | Close the active management CLI session. |
| `status` | — | Display running state, `LIC_TYPE`, `SERVER_MODE`, bind address, port, passthrough online status, active offline reservation state, and any detected crash dump. |
| `features` | — | List all available, used, and total feature counts per licensed application, plus active **Reserved / Borrowed Entitlements** when in `PASSTHROUGH` mode. |
| `counts` | — | Render the consolidated tabular **Feature Counts** summary across all applications. |
| `clients` | — | List connected client applications, connection IDs, and source IPs. |
| `licenses` | — | Show licensee metadata (username, company, license date, expiration), licensed applications, feature counts, **Token Pools** (with per-feature token cost & accrual policy), and **Hardware** entries. |
| `records` | — | Display full **Checkout Records** (application entitlements, max allowed `YYYY.MM` versions, included features), **Licensed Hardware** (vendor, type, serials, used/available/max), and **Token Pools**. |
| `config` | — | Print current configuration settings (`SERVER_MODE`, `LIC_TYPE`, `PT_HOST`, `PT_PORT`, `PROXY_IP`, `PROXY_PORT`, ports). |
| `display` | `<target>` | Subcommand alias for `mode`, `status`, `features`, `counts`, `clients`, `licenses`, `records`, or `crash-dump`. |
| `setmode` | `<NL\|LS\|PT>` | Set legacy license type flag (`NL` Node-Locked, `LS` License Server, `PT` Passthrough). Prefer `setsrvmode` on modern builds. |
| `setsrvmode` | `<LOCAL\|PASSTHROUGH>` | Switch daemon mode between `LOCAL` and `PASSTHROUGH` *(requires daemon restart to apply)*. |
| `setport` | `<port>` | Update `APEXLM_PORT` in environment configuration *(requires daemon restart to apply)*. |
| `loadlic` | `<filepath>` | Read a Format Version 2 license JSON file from disk, validate its Ed25519 signature, install it into the daemon SQLite database, and display updated entitlements. |
| `service` | `<cmd>` | Manage the OS system service (`install`, `uninstall`, `start`, `stop`, `restart`, `status`) from an **elevated** shell (`ApexLMService` / `apexlm.service`). |
| `monitor` | `<on\|off>` | Toggle continuous auto-refresh dashboard output (status + feature counts; press `Enter` to stop). |
| `refresh` | `<seconds>` | Set the auto-refresh interval for `monitor on` (minimum `1` second, default `5`). |
| `crash-dump` | — | Query crash diagnostics from the running daemon, or fall back automatically to reading `apexlm.crash.dmp` from disk if the daemon is offline (`crash`, `crashdump` aliases). |
| `clear` | — | Clear the terminal screen. |
| `help` | — | Print available commands. |
| `quit`, `exit` | — | Exit the interactive shell. |

---

## 2. Floating Server CLI (`ApexLM_Server_CLI`)

Manage the central **APEX LM Server Daemon** (`ApexLM_Server_Service`, prompt `ApexLM-Server> `, default admin endpoint `http://127.0.0.1:27888/`). `ApexLM_Server_CLI` connects strictly to `SERVER`-mode daemons on `127.0.0.1`.

### Supported Commands

All inspection, licensing, monitoring, crash-dump, and service lifecycle commands match `ApexLM_CLI`:
- **Interactive or One-Shot**: `connect`, `disconnect`, `status`, `features`, `counts`, `clients`, `licenses`, `records`, `config`, `loadlic <filepath>`, `display <target>`, `setport <port>`, `service <install|uninstall|start|stop|restart|status>`, `monitor <on|off>`, `refresh <seconds>`, `crash-dump`, `clear`, `help`, `quit`/`exit`.
- **Mode Lock Enforcement**: Mode-changing commands (`setmode` and `setsrvmode`) are **disabled** in `ApexLM_Server_CLI` because the central server daemon is locked exclusively to `SERVER` mode.

### Server Administration Examples

```powershell
# Inspect server status, connected workstation proxies, and floating pool usage
ApexLM_Server_CLI.exe status
ApexLM_Server_CLI.exe clients
ApexLM_Server_CLI.exe counts

# Hot-reload an updated server license (succeeds immediately when 0 seats are checked out)
ApexLM_Server_CLI.exe loadlic "C:\Licenses\floating-server-2027.json"

# Inspect full entitlements, hardware serial lists, and token pools
ApexLM_Server_CLI.exe records
```

---

## 3. Workstation Daemon Executable (`ApexLM_Service`)

Run directly to start the local service in foreground mode, query version, or install/control the native OS service (requiring Administrator on Windows or `sudo` on Linux for `install`/`start`/`stop`/`restart`/`uninstall`):

| Flag | Description |
| :--- | :--- |
| *(no flags)* | Run **APEX LM Daemon** in the foreground (single-instance check enforced). |
| `-v`, `--version` | Print the **APEX License Manager** build version and exit. |
| `-r`, `--restart` | Restart helper used during in-place Web UI / daemon restarts. |
| `-s`, `--service [variant]` | Windows SCM service entrypoint *(used internally when started by Windows Services)*. |
| `--install-service` | Install `ApexLMService` (Windows) or `/etc/systemd/system/apexlm.service` (Linux). |
| `--uninstall-service` | Stop, disable, and remove the system service. |
| `--start-service` | Start the installed system service. |
| `--stop-service` | Stop the running system service. |
| `--restart-service` | Restart the installed system service. |
| `--service-status` | Print current OS service status (does not require elevation). |

---

## 4. Floating Server Service Executable (`ApexLM_Server_Service`)

Command-line controller and daemon entrypoint for central floating license servers (`SERVER` mode only):

| Subcommand / Flag | Description |
| :--- | :--- |
| `install-license <license-file>` | Pre-validate JSON schema, Ed25519 signature, and `"server": true` flag, and stage the server license file. |
| `start` | Validate the installed server license and start the **APEX LM Server Daemon** directly. |
| `stop` | Stop the running server process (`taskkill` on Windows / `SIGTERM` -> `SIGKILL` on Linux). |
| `restart` | Stop and restart the running server process cleanly. |
| `status` | Display running PID, user, locked `SERVER` mode, and license validity. |
| `install` | Install native OS service `ApexLMServerService` (Windows) or `/etc/systemd/system/apexlm-server.service` (Linux). |
| `uninstall` | Remove the installed OS system service. |
| `start-service` | Start the installed OS system service. |
| `stop-service` | Stop the installed OS system service. |
| `restart-service` | Restart the installed OS system service. |
| `service-status` | Report installed OS system service state. |
| `-v`, `--version` | Print server daemon version and locked mode status. |
| `-h`, `--help` | Print command help. |

---

## 5. System Tray Companion (`ApexLM_Tray`)

`ApexLM_Tray` runs a lightweight tray icon (**A**) in the desktop notification area and discovers the local daemon's `management.endpoint`:

- **Context Menu Actions**:
  - **Service running (Open Configuration)** / **Open Configuration** — Opens **`http://127.0.0.1:27887/`** in your default browser *(also triggered by double-clicking the tray icon)*.
  - **Start Service** / **Restart Service** — Starts or restarts `ApexLMService` asynchronously and polls health status.
  - **Exit** — Closes the tray icon *(leaves the background `ApexLMService` daemon running)*.
- **Command-Line Flags**:
  - `-b`, `--open-browser` — Immediately open the Web Admin UI in the default browser (launches tray icon if not already running).
  - `-v`, `--version` — Print version and exit.

See also: [Workstation & Server Setup](setup-and-server.md) · [Web Admin UI, Configuration & Reservations](web-ui-and-reservations.md)
