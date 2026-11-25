# Licensing Dialogs

When launched, one of the first initialization steps the **APEX DS** application performs is displaying the **Splash Dialog** window shown below. This window disappears automatically after a short timeout, or can be dismissed immediately when there are no licensing issues.

The Splash Dialog displays a summary of the application's version, build, and current licensing status. It can also be reopened at any time by selecting **About** under the **Help** menu.

![Example Splash Dialog (DV shown, others similar)](../images/interface/images/licensing-883f794f.png)

*Example Splash Dialog (DV shown, others similar)*

## Modern ApexLM Configuration (`http://127.0.0.1:27887/`)

On builds using **APEX License Manager (ApexLM / ALM)**:

- Clicking **Configure** on the Splash/About dialog launches the **ApexLM Web Administration UI** at **`http://127.0.0.1:27887/`** in your system web browser (communicating with the local ALM client daemon on TCP port `27884`).
- Within the Web UI you can:
  - View **Overview** (host MAC Host ID, active operating mode `LOCAL` / `PASSTHROUGH` / `SERVER`, and installed entitlements).
  - Install a new Format v2 JSON license file or inspect version ceilings, channel pools (`<VENDOR>_CHANNELS` / `ANY_CHANNELS`), `AEROPLOTS`, and boolean flags (`PARAMETER_SERVER`, `RWX_COMPRESSION`, `DS_MANAGER`).
  - Monitor **Usage**, active **Clients** (heartbeats), **Records**, **Logs**, and **Audit** trails.
  - Configure upstream floating server connection (`TCP 27885`/`27886`) under **Config** and request offline **Borrow** leases (up to **30 days**) under **Borrow**.
- Running **APEX DS** in simulated input mode (`simul`) permits evaluation without checking out hardware channel or DS feature licenses.

---

## Legacy FlexNet License Configuration Dialogs

In legacy FlexNet (`27000@host`) builds, clicking **Configure** opens the FlexNet License Configuration dialog shown below. This dialog configures the active licensing mode and mode-specific options.

Administrators can protect changes with a password via the **Password** button (requiring the stored password before modifying settings). Selecting **Unlicensed** mode still allows many APEX DS suite applications to execute with reduced or simulator-only functionality.

### Node Locked Licensing

In this mode, the APEX DS application is licensed using an APEX-provided Flexera FlexNET format license file:

> - Install the software if not already installed.
> - Run the software and invoke the license configuration dialog from the initial splash screen.
> - Record the Host ID from the registration window and provide it to APEX, Inc.
> - APEX returns a `.lic` license file. Install the file according to the method selected on the license configuration panel (shown below).

![Example License Configuration Dialog: Custom mode](../images/interface/images/licensing-f6d12fcf.png)

*Example License Configuration Dialog: Custom mode*

Node-locked license files can be installed using one of two methods:

> - **Default**: The file must be copied to the `../licenses` directory relative to the main application executable. Keep only the active license file in this folder and remove expired files when updating.
> - **Custom**: The file can be placed in an arbitrary directory on the host OS file system. Its path must be entered in the license configuration dialog.
>
>   > [!NOTE]
>   > The two methods above may behave differently when multiple users share a workstation. **Default** generally works best across user accounts; when using **Custom**, select a directory accessible to all intended users.

### Server Based Licensing

When using FlexNet server-based licensing (`27000@host`), only the license server's IP address or hostname needs to be entered on client workstations (managing `lmgrd` on the server host is covered separately):

![Example License Configuration Dialog: Server mode](../images/interface/images/licensing-74f01761.png)

*Example License Configuration Dialog: Server mode*

APEX DS suite applications support borrowing licenses from configured FlexNet servers. Borrowed licenses behave as temporary node-locked licenses checked out against the server's pool for up to one year, allowing disconnected operation and early return upon reconnecting.

> [!NOTE]
> Always configure the APEX application as intended for disconnected use before performing the borrow operation so all required channel and feature counts are checked out.

### OpenCode Licensing

OpenCode is a node-locked mode using Flexera **Trusted Storage** with alphanumeric code groups (`6` to `10` groups of six characters) instead of `.lic` files:

![Example License Configuration Dialog: OpenCode mode](../images/interface/images/licensing-08abb04a.png)

*Example License Configuration Dialog: OpenCode mode*

APEX, Inc. maintains an OpenCode activation server supporting:

> - **Request Open Code Activation**: Generates an activation request code to enter on the activation server, creating a *pending request*.
> - **Process Response**: Applies the response code from the activation server to complete activation.
> - **Cancel Open Code Activation**: Clears a pending request locally without completing the transaction.
> - **Return Open Code**: Deactivates local APEX DS licenses and outputs a return code to reclaim credit on the activation server.

The **Manage Trusted Storage** button switches to administrative Trusted Storage actions:

> - **Install Trusted Storage**: Installs FlexNET Trusted Storage components on the host (performed only once).
> - **Trusted Storage Contents**: Lists all OpenCode licenses stored on the host.
> - **Reset Trusted Storage**: Removes all stored OpenCode licenses.
> - **Remove Open Code**: Deletes a license without generating a return transaction.
>
> > [!WARNING]
> > Except for initial Trusted Storage installation (when needed and **only once**) and listing contents, **do not** invoke Trusted Storage reset/removal actions unless explicitly instructed by APEX support.

---

## License Agreement

The License Agreement dialog is displayed when a new software release is first run and can also be opened manually from the Splash Dialog window. Users must accept the agreement text to continue using **APEX DS**.

![Example License Agreement Dialog](../images/interface/images/licensing-8bde7052.png)

*Example License Agreement Dialog*
