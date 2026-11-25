# Software Licensing

After **APEX DS** software components are installed, operational entitlements must be available from either the modern **APEX License Manager (ApexLM)** service or (for legacy deployments) Flexera Software's **FlexNet** license manager.

## Suite Licensing Rules

The following application-specific rules apply across **APEX DS** and companion suite tools:

- **Simulator Evaluation Mode (`APEX DS`):** Running **APEX DS** in simulated input mode (`simul`) acts as an uncounted evaluation mode—hardware channel, plot display (`AEROPLOTS`), and optional DS feature flags (`PARAMETER_SERVER`, `RWX_COMPRESSION`, `DS_MANAGER`) are not consumed. Note that pre-release builds (Alpha `14`-day, Beta `60`/`62`-day, RC `21`-day) still enforce build-date expiration checks.
- **Hardware Acquisition (`APEX DS`):** When acquiring from real hardware (`INPUT_ADCDEVICE`), the following rules apply:
  - **Counted Channel Pools (`<VENDOR>_CHANNELS` and `ANY_CHANNELS`):** Each active hardware input channel checks out one channel license. DS attempts to allocate from the matching vendor pool first (for example `NI_CHANNELS`, `VTI_CHANNELS`, `GS_CHANNELS`, `MECALC_CHANNELS`, `SCANI_CHANNELS`) and falls back to the generic `ANY_CHANNELS` pool if vendor-specific seats are exhausted. (Legacy FlexNet maps these to `APEXDS_CHANNELS_<vendor>` and `APEXDS_CHANNELS_ANY`.)
  - **Shared Plot Display Token (`AEROPLOTS`):** Opening the full Engineering Plots interface during real hardware acquisition checks out one `AEROPLOTS` license (known as **DR Plot Interface** / `APEXDS_AEROPLOTS` in legacy FlexNet). These seats are pooled across all running **APEX DS** and **APEX DR** instances.
  - **Boolean Feature Flags:** Non-counted feature flags enable or disable DS subsystems globally:
    - **`PARAMETER_SERVER`** *(legacy `PARAMETER`)* — Enables derived/computed parameters and external parameter sources.
    - **`RWX_COMPRESSION`** *(legacy `COMPRESSION`)* — Enables compressed `.rwz` raw data recording.
    - **`DS_MANAGER`** *(legacy `MANAGER`)* — Allows DS to accept remote manager control connections from **APEX DM (`DM-cmd` / `DM-api`)** and **`DSAPI`** tools.
- **Remote Display (`APEX DR`):** **APEX DR** (`DR`) always requires one **`AEROPLOTS`** license on startup, drawn from the same shared pool used by **APEX DS**.
- **Data Manager & `DSAPI` (`DM`, `DSAPI`):** Remote manager automation requires `DS_MANAGER` on non-simulator **DS** targets. Standalone **`DSAPI`** tools check out `APEXAPI_NET_STREAM`, `APEXAPI_NET_RECORD`, and `APEXAPI_NET_CONFIG` (`DM` is registered under application ID `DM`; embedded `DS`/`DX+` clients operate in passthrough mode).
- **Data Viewer (`APEX DV`) & Post-Processing (`APEX DX` / `DX+`):** **APEX DV** (`DV`) can run unlicensed in basic mode, while optional features (`DVFILE`, `DVBANNER`, `DVPROJECT`, `DVSCREEN2`–`DVSCREEN4`) consume `ANALYSIS` tokens (`5` tokens each), shared with **APEX DX**, **GageMap**, and **BT**.
- **Device Drivers:** Individual `drv-*` acquisition and DSP plugins are not licensed standalone; channel entitlements are enforced by the host **APEX DS** process loading them (with optional ApexLM `licenses[].hardware` vendor serial validation via `ApexLmLic`).

---

## Modern Licensing: APEX License Manager (`ApexLM` / `ALM`)

Current and future **APEX DS** releases connect to **[APEX License Manager (`ApexLM`)](../../../License%20Manager/README.md)** (**APEX LM Daemon** & **APEX LM Server Daemon**).

> [!WARNING]
> **Legacy FLEXlm / `lmgrd` Discontinuation Notice (October 2027)**
>
> The previous licensing method using **FLEXlm / FlexNet Publisher (`lmgrd` license server, `lmtools`, `lmutil`, `.lic` files, `27000@host`, and OpenCode Trusted Storage)** will be **discontinued as of October 2027**. All product versions going forward exclusively use **APEX License Manager (`ApexLM`)** (**APEX LM Daemon** & **APEX LM Server Daemon**).

### Architecture, Transport & Network Ports

| Component | Default Endpoint / Env Var | Transport & Purpose |
| :--- | :--- | :--- |
| **Client Registration & Heartbeat** | `127.0.0.1:27884` (`APEXLM_HOST` / `APEXLM_PORT`) | Local ZeroMQ `REQ/REP` with CurveZMQ encryption (`5000 ms` `APEXLM_TIMEOUT`). DS monitors the connection and requires an active local **APEX LM Daemon**. |
| **Central Floating Server** | `27885` (`APEXLM_SERVER_PORT`), optional `27886` (`APEXLM_SERVER_LISTEN`) | CurveZMQ **APEX LM Server Daemon** listening for remote `PASSTHROUGH` client daemons (`"server": true` in license required). |
| **Local Web Administration UI** | **`http://127.0.0.1:27887/`** (`APEXLM_MANAGEMENT_PORT`) | Loopback browser console opened by **Configure** in DS/DR or `ApexLM_Tray`: install/inspect licenses, view active sessions & usage, edit config, and **Reserve** offline seats. |
| **Server Web Administration UI** | `http://127.0.0.1:27888/` (`APEXLM_SERVER_MANAGEMENT_PORT`) | Loopback browser console on dedicated **APEX LM Server Daemon** hosts (`ApexLMServerService` / `apexlm-server.service`). |

### Operating Modes

1. **`LOCAL` Mode (Node-Locked):** Licenses are stored locally in an Ed25519-signed Format v2 JSON file installed into the ApexLM SQLite database (`C:\ProgramData\APEX\APEXLM\apexlm.db` on Windows, `/var/lib/apexlm/apexlm.db` on Linux) and bound to host MAC address(es) (`host` array, or `"*"` / `"demo"`).
2. **`PASSTHROUGH` Mode (Floating Client & Offline Reservations):** The local `ApexLMService` / `apexlm.service` daemon on `127.0.0.1:27884` forwards requests securely to a central `SERVER` on TCP `27885`/`27886`. Users can reserve entitlements for offline use for up to **30 days** from the **Reserve** tab in **`http://127.0.0.1:27887/`** ([Web UI & Reservations](../../../License%20Manager/web-ui-and-reservations.md)).
3. **`SERVER` Mode (Floating License Server):** Runs `ApexLMServerService` (Windows) or `apexlm-server.service` (Linux) with a central database (`APEXLM_Server\apexlm_server.db` / `/var/lib/apexlm-server/apexlm_server.db`). DS/DR clients never connect directly to port `27885`; instead they connect to their local `PASSTHROUGH` daemon on `27884`.

See also: **[Workstation & Server Setup](../../../License%20Manager/setup-and-server.md)** · **[CLI Tools Reference](../../../License%20Manager/cli-reference.md)** · **[Software License Agreement](../../../Release%20Policies/software-license-agreement.md)**

### Hardware Serial Binding & Version Ceilings

- ApexLM Format v2 licenses enforce per-application version ceilings (`version`, e.g., `"2026.52"`).
- Licenses may restrict hardware acquisition to specific device serial numbers per vendor (`mecalc`, `scanivalve`, `datatel`, `hgl`, `pacific`, `ni`, `dewesoft`, `ps9016`, `vti`, or `"*"` wildcard) via `licenses[].hardware`.

---

## Legacy FlexNet Licensing (`27000@host`) *(Discontinued October 2027)*

Legacy APEX DS builds only used Flexera Software's FlexNet (`lmgrd`) license manager, which is **discontinued as of October 2027**. Plan migration to **[APEX License Manager (`ApexLM`)](../../../License%20Manager/README.md)** before October 2027.

### Node Locked Licensing

The simplest FlexNet method uses a node-locked `.lic` file tied to the computer's FlexNet **Host ID**:

1. Obtain the FlexNet Host ID from the licensing configuration dialog and provide it to APEX, Inc.
2. Copy the returned `.lic` file either to the standard `../licenses` directory relative to the executable or to a custom path specified in the GUI.

Node-locked counts for channels, plot interfaces, or tokens are shared among all local application instances on that host regardless of user account.

### APEX OpenCode Licensing

**APEX OpenCode** is an extension of node-locked licensing built on Flexera **Trusted Storage (TS)**. Users request, install, return, and transfer licenses against an **activation server** hosted by APEX, Inc. using short alphanumeric code sequences (`6`–`10` groups of `6` characters) entered manually when security rules prevent direct internet access.

### Server Based Licensing

Hosting FlexNet licenses on a central server runs Flexera `lmgrd` (typically **`27000@<host>`**) on a dedicated server machine. Client workstations install no `.lic` files and instead point to the server hostname or IP.

Licenses are allocated first-come, first-served until counts are exhausted and reclaimed when an application exits. Both `.lic` files and OpenCode Trusted Storage are supported on the FlexNet server host. Clients running in FlexNet Server mode can also **borrow** licenses for disconnected field operation (for up to one year) and return them early upon reconnecting.
