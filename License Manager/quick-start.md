# APEX License Manager Quick Start Guide

Follow one of the two deployment tracks below to activate a single-workstation node-locked license (`LOCAL`) or connect your workstation to a central floating **APEX LM Server Daemon** (`SERVER` + `PASSTHROUGH`).

> [!IMPORTANT]
> **Transitioning from FLEXlm / `lmgrd`?** Legacy FLEXlm licensing (`27000@host`, `.lic` files, `lmtools`) will be **discontinued in October 2027**. All current and future **APEX** software versions use **APEX License Manager (`ApexLM`)** (`ApexLM_Service` and `ApexLM_Server_Service`).

---

## Track A: Single Workstation (`LOCAL` Mode)

### 1. Start the Local APEX LM Daemon

- **Windows**: Confirm `ApexLMService` is running in **Services** (`services.msc`) or install/start it from an **elevated** PowerShell prompt:
  ```powershell
  ApexLM_Service.exe --install-service
  ApexLM_Service.exe --start-service
  ```
- **Linux**: Install and start `apexlm.service`:
  ```bash
  sudo ./ApexLM_Service --install-service
  sudo ./ApexLM_Service --start-service
  ```

### 2. Retrieve Your Host ID / License Request File

1. Launch **ApexLM Tray** (`ApexLM_Tray`), right-click the **A** tray icon, and choose **Open Configuration** — or open **`http://127.0.0.1:27887/`** directly in your browser.
2. On the **Overview** tab in the **Host** card, click **Download license request** to save `license-request.json` (or copy the workstation MAC address).
3. Submit the license request through the [APEX User Portal](https://users.apexturbine.com/) to obtain your Ed25519-signed **Format Version 2** license file.

### 3. Install Your License

Either use the **Web Admin UI** or the **CLI**:

=== "Web Admin UI (Browser)"

    1. Open `http://127.0.0.1:27887/` and switch to the **Configuration** tab (`#config`).
    2. Ensure **Service mode** is set to **Local**.
    3. Under **Install license**, click **Browse license file...** (or drag and drop your `.json` license text) and click **Install**.
    4. Switch to **Overview** and **Records** to verify green **`LOCAL`** status and licensed applications/features.

=== "ApexLM_CLI (Terminal)"

    ```powershell
    ApexLM_CLI.exe setsrvmode LOCAL
    ApexLM_CLI.exe loadlic "C:\path\to\workstation-license.json"
    ApexLM_CLI.exe status
    ApexLM_CLI.exe counts
    ```

---

## Track B: Central Floating License Server (`SERVER` + `PASSTHROUGH`)

Floating pools require **APEX LM Server Daemon (`ApexLM_Server_Service`)** on a central host and local **APEX LM Daemons (`ApexLM_Service`)** configured in **`PASSTHROUGH`** mode on each client workstation. Client applications never connect directly across the network to port `27885`; they always talk locally to `127.0.0.1:27884`.

### 1. Prepare and Start the Central License Server

1. Obtain a server-authorized Format Version 2 license (`"server": true`, bound to the server host MAC address) from **APEX**.
2. On the license server host (elevated shell / `sudo`):
   ```powershell
   # Validate signature & server flag, and stage license for server startup
   ApexLM_Server_Service.exe install-license "C:\path\to\server-license.json"

   # Install and start the central OS service (binds TCP 27885)
   ApexLM_Server_Service.exe install
   ApexLM_Server_Service.exe start-service
   ApexLM_Server_Service.exe status
   ```
   *(On Linux, run `sudo ./ApexLM_Server_Service install-license ...`, `sudo ./ApexLM_Server_Service install`, and `sudo ./ApexLM_Server_Service start-service`.)*
3. Ensure the server firewall permits inbound TCP traffic on **`27885`** (`APEXLM_SERVER_PORT`, and `27886` if using `APEXLM_SERVER_LISTEN`) from authorized workstation subnets.
4. Optionally open **`http://127.0.0.1:27888/`** on the server host (or via SSH local port forward) to inspect active **Records**, **Usage**, and **Clients**.

### 2. Point Each Workstation Daemon to the License Server

1. On the client workstation, open **`http://127.0.0.1:27887/#config`** (via **ApexLM Tray -> Open Configuration**).
2. Under **Settings**:
   - **Service mode** (`SERVER_MODE`): Select **Passthrough**.
   - **License server host** (`PT_HOST`): Enter the server's hostname or IP address (for example `licserver.corp.local`).
   - **License server port** (`PT_PORT`): Keep **`27885`** (unless customized via `APEXLM_SERVER_PORT`).
   - *(Optional)* **Proxy address / port** (`PROXY_IP`, `PROXY_PORT`): Complete only if traffic routes through an outbound proxy.
3. Click **Save changes**, then in the **Control** card click **Restart service**.
4. Confirm the status bar at the top reads **`Connected to License Server`** with a green **`PASSTHROUGH`** pill.

### 3. Reserve Licenses for Offline / Field Use (Optional)

If taking a laptop or acquisition rig offline away from the corporate network:

1. Open **`http://127.0.0.1:27887/#borrow`** (the **Reserve** tab) while connected to the server.
2. Check the needed features/token counts and hardware vendors, select a **Return by** date (up to **30 days**), and click **Reserve selected**.
3. Your workstation will automatically transition into **Offline Reservation** mode whenever the server is unreachable.

See [Workstation Daemon & Floating License Server Setup](setup-and-server.md), [CLI Tools Reference](cli-reference.md), and [Web Admin UI & Reservation System](web-ui-and-reservations.md) for complete operational details.
