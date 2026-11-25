# Software Licensing

After **APEX DR** software components are installed, operational entitlements must be available from either the modern **APEX License Manager (ApexLM)** service or (for legacy deployments) Flexera Software's **FlexNet** license manager.

## Suite Licensing Rules

The following application-specific rules apply to **APEX DR** and companion DS suite components:

- **Remote Display (`APEX DR`):** Running **APEX DR** (`DR`) always requires one shared **`AEROPLOTS`** display token on startup (known as **DR Plot Interface** / `APEXDS_AEROPLOTS` in legacy FlexNet). If `AEROPLOTS` is unavailable, **APEX DR** cannot initialize display operation and exits. These licenses are pooled across all running **APEX DR** and **APEX DS** instances.
- **Acquisition Server (`APEX DS`):**
  - **Simulator Evaluation Mode:** **APEX DS** in simulated input mode (`simul`) runs without consuming hardware channels, `AEROPLOTS`, or optional feature flags. (Note that **APEX DR** itself still checks out `AEROPLOTS` when launched.)
  - **Live Hardware Mode:** **APEX DS** consumes one counted channel license per active channel (`<VENDOR>_CHANNELS` with fallback to `ANY_CHANNELS`), one shared `AEROPLOTS` token for full local Engineering Plots, and boolean feature flags (`PARAMETER_SERVER`, `RWX_COMPRESSION`, `DS_MANAGER`).
- **Data Manager & `DSAPI` (`DM`, `DSAPI`):** Remote automation requires `DS_MANAGER` on non-simulator **DS** nodes; standalone `DSAPI` clients require `APEXAPI_NET_STREAM`, `APEXAPI_NET_RECORD`, and `APEXAPI_NET_CONFIG`.
- **Data Viewer (`APEX DV`):** Runs in basic mode without tokens; optional capabilities (`DVFILE`, `DVBANNER`, `DVPROJECT`, `DVSCREEN2`–`DVSCREEN4`) consume `ANALYSIS` tokens (`5` tokens each), shared with **APEX DX**, **GageMap**, and **BT**.
- **Device Drivers:** Plugins (`drv-*`) are not licensed standalone; channel entitlements are governed by **APEX DS** (with optional ApexLM hardware serial validation per vendor).

---

## Modern Licensing: APEX License Manager (`ApexLM` / `ALM`)

Current and future **APEX DR** releases connect to **[APEX License Manager (`ApexLM`)](../../../License%20Manager/README.md)** (**APEX LM Daemon** & **APEX LM Server Daemon**).

> [!WARNING]
> **Legacy FLEXlm / `lmgrd` Discontinuation Notice (October 2027)**
>
> The previous licensing method using **FLEXlm / FlexNet Publisher (`lmgrd` license server, `lmtools`, `lmutil`, `.lic` files, `27000@host`, and OpenCode Trusted Storage)** will be **discontinued as of October 2027**. All product versions going forward exclusively use **APEX License Manager (`ApexLM`)** (**APEX LM Daemon** & **APEX LM Server Daemon**).

### Architecture, Transport & Network Ports

| Component | Default Endpoint / Env Var | Transport & Purpose |
| :--- | :--- | :--- |
| **Client Registration & Heartbeat** | `127.0.0.1:27884` (`APEXLM_HOST` / `APEXLM_PORT`) | Local ZeroMQ `REQ/REP` with CurveZMQ encryption (`5000 ms` `APEXLM_TIMEOUT`). DR requires an active local **APEX LM Daemon**. |
| **Central Floating Server** | `27885` (`APEXLM_SERVER_PORT`), optional `27886` (`APEXLM_SERVER_LISTEN`) | CurveZMQ **APEX LM Server Daemon** serving remote `PASSTHROUGH` client daemons. |
| **Local Web Administration UI** | **`http://127.0.0.1:27887/`** (`APEXLM_MANAGEMENT_PORT`) | Loopback browser console opened by **Configure** in DR/DS or `ApexLM_Tray`: install/inspect licenses, view shared `AEROPLOTS` usage & clients, configure upstream server, and **Reserve** offline seats. |
| **Server Web Administration UI** | `http://127.0.0.1:27888/` (`APEXLM_SERVER_MANAGEMENT_PORT`) | Loopback browser console on dedicated **APEX LM Server Daemon** hosts (`ApexLMServerService` / `apexlm-server.service`). |

### Operating Modes

1. **`LOCAL` Mode (Node-Locked):** Ed25519-signed Format v2 JSON license stored in the local ApexLM SQLite database (`C:\ProgramData\APEX\APEXLM\apexlm.db` on Windows, `/var/lib/apexlm/apexlm.db` on Linux) bound to host MAC address(es) (`host` array, or `"*"` / `"demo"`).
2. **`PASSTHROUGH` Mode (Floating Client & Offline Reservations):** Recommended for multi-seat **APEX DR** control rooms. The local `ApexLMService` / `apexlm.service` daemon on `127.0.0.1:27884` checks out shared **`AEROPLOTS`** tokens from a central ApexLM `SERVER` on TCP `27885`/`27886`. Users can reserve licenses for offline use for up to **30 days** from the **Reserve** tab at **`http://127.0.0.1:27887/`** ([Web UI & Reservations](../../../License%20Manager/web-ui-and-reservations.md)).
3. **`SERVER` Mode (Floating License Server):** Runs `ApexLMServerService` (Windows) or `apexlm-server.service` (Linux) with `APEXLM_Server\apexlm_server.db` / `/var/lib/apexlm-server/apexlm_server.db`. Client workstations run in `PASSTHROUGH` mode pointing at the server ([Workstation & Server Setup](../../../License%20Manager/setup-and-server.md)).

### Hardware Serial Binding & Version Ceilings

- ApexLM licenses validate per-application build version ceilings (`version`, e.g., `"2026.52"`). Note pre-release Alpha (`14`-day), Beta (`60`/`62`-day), and RC (`21`-day) builds also enforce build-date expirations ([Release Policies](../../../Release%20Policies/README.md)).
- Server-side DS acquisition entitlements can additionally bind to per-vendor hardware serials (`mecalc`, `scanivalve`, `datatel`, `hgl`, `pacific`, `ni`, `dewesoft`, `ps9016`, `vti`) via `licenses[].hardware`.

---

## Legacy FlexNet Licensing (`27000@host`) *(Discontinued October 2027)*

Legacy APEX DR builds only use Flexera Software's FlexNet (`lmgrd`) license manager, which is **discontinued as of October 2027**. Plan migration to **[APEX License Manager (`ApexLM`)](../../../License%20Manager/README.md)** ahead of October 2027.

### Node Locked Licensing

In node-locked mode, obtain the FlexNet **Host ID** from the licensing dialog, send it to APEX, Inc., and place the resulting `.lic` file either in `../licenses` relative to the executable or in a custom directory configured in the GUI. Counts on the host are shared across local application instances regardless of OS user.

### APEX OpenCode Licensing

**APEX OpenCode** extends node-locked licensing using Flexera **Trusted Storage (TS)**. Operations (request, activation, deactivation, return, and move) exchange `6`–`10` alphanumeric code groups with the APEX activation server, supporting air-gapped environments.

### Server Based Licensing

Running FlexNet `lmgrd` (typically **`27000@<host>`**) on a central license server pools shared **`AEROPLOTS`** / **DR Plot Interface** seats across networked DR and DS workstations. Client workstations enter the server address in the GUI and may borrow seats offline for up to one year (returning them early upon reconnecting).
