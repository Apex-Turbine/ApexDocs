# `DM-api` & Standalone `DSAPI` Automation Utilities

In addition to **`DM-cmd`**, the APEX DS suite ships **`DM-api`** and lightweight single-purpose C++ command-line utilities built against **`DSAPI`** (`libdsapi` / `dsapi.dll`) for integrating DS discovery, calibration, timed recording, and threshold-driven acquisition into external scripts and test-cell controllers.

---

## `DM-api`

`DM-api` is a `DSAPI`-linked script runner (`DS/app/dm/DM-api.cxx`) implementing the `DM-cmd` script loader pattern directly on top of the `DSAPI` C++ network interface.

### Capabilities & Workflow
- Runs interactively from standard input or executes batch files via:
  - `h` — run `DSAPI` LAN discovery and list active DS servers
  - `l <filename>` — load and execute nested batch command scripts
  - `w <seconds>` — sleep for `seconds` between control transitions
  - `# <comment>` — ignored comment lines
  - `?` — display supported commands
  - `q` — exit cleanly (`0`)
- Suitable as a minimal template or scripted wrapper when integrating custom `DSAPI` builds alongside `DM-cmd`.

---

## `dsdiscoverapp`

`dsdiscoverapp` continuously probes the network (or a specific unicast host) to discover live **APEX DS** servers and report their hostnames, control ports, operational states, and loaded configurations.

### Usage
```text
dsdiscoverapp [host_or_ip]
```
- **`host_or_ip`** *(optional)*: Target IP address or hostname to probe directly. When omitted, defaults to `"localhost"` and broadcasts LAN discovery over UDP port `10995`.

### Behavior & Output Format
- Polls every **5 seconds** using a **`1000 ms`** discovery timeout (`DSAPI_net_discover_tout`).
- Prints each discovered DS server to standard output in the format:
  ```text
  DS host <index>, port <port>, state <state>: '<hostname>' -- '<ip>' -- '<configuration>'
  ```
- **Typical Use Cases:**
  - Verifying firewall/subnet reachability (UDP `10995` / TCP `10995`–`11004`) before running `DM-cmd` scripts.
  - Identifying exact `<hostname>` and `<configuration>` names required by `DM-cmd connect`, `dscalapp`, or `dsrecordapp`.

---

## `dscalapp`

`dscalapp` connects to a running **APEX DS** server in manager mode and programmatically updates the ADC calibration scale (`adcCalScale`) across all active input channels before committing calibration back to the peer server.

### Usage
```text
dscalapp <DShost> <DSconfigname> <calscale>
```

| Argument | Description |
| :--- | :--- |
| **`DShost`** | Hostname or IP address of the running APEX DS server. |
| **`DSconfigname`** | Configuration name active on the DS server (case-sensitive match as reported by `dsdiscoverapp`). |
| **`calscale`** | Floating-point calibration scale factor (`adcCalScale`) applied to every input channel in the peer setup. |

### Exit Status & Workflow
1. Discovers `<DShost>` and requests an exclusive manager connection (`DSAPI_net_connect(..., DS_MANAGER)`).
2. Copies the server's active `Setup` (`DSAPI_net_peer_setup`), updates `adcCalScale(calscale)` on every channel (`0 .. channelCount - 1`), and invokes `DSAPI_net_calibrate`.
3. Disconnects and returns **`0`** on success or **`-1`** on discovery, manager lock, or calibration failure.

### Example
```bash
# Apply a 1.025 calibration scale factor to DS node 192.168.10.20 running RigTest
dscalapp 192.168.10.20 RigTest 1.025
```

---

## `dsrecordapp`

`dsrecordapp` executes a deterministic sequence of **Off**, **Raw (`.rwx`)**, and **Peak (`.pkx`)** recording intervals on an **already running** APEX DS acquisition server while monitoring telemetry stream continuity.

### Usage
```text
dsrecordapp <DShost> <DSconfigname> <Command>...
```

| Argument | Description |
| :--- | :--- |
| **`DShost`** | Hostname or IP address of the target APEX DS server. |
| **`DSconfigname`** | Active configuration name on the target server. |
| **`Command...`** | One or more timed state directives executed left to right: <br>- **`O<seconds>`**: Off — pauses recording (server stays `RUNNING`, no file written) for `<seconds>`.<br>- **`R<seconds>`**: Raw — records `.rwx` raw data (`record-%04d.rwx`) for `<seconds>`.<br>- **`P<seconds>`**: Peak — records `.pkx` processed peak/FFT data (`record-%04d.pkx`) for `<seconds>`. |

### Requirements & Telemetry Reporting
- **Precondition:** The target DS server must already be in `RUNNING` acquisition state (`NET_DSP_STATE_RUNNING`); otherwise `dsrecordapp` reports an error and exits.
- Subscribes to `"PR"` (Peak + Raw) network streams during execution and reports any missed data blocks or raw packets encountered during recording intervals.

### Example
```bash
# Wait 2s off, record 10s raw (.rwx), pause 5s, then record 15s peak (.pkx)
dsrecordapp daq-node1 TurbineRig O2 R10 O5 P15
```

---

## `dscontrolapp`

`dscontrolapp` (`DS/api/examples/dscontrolapp.cxx`) connects as a `DSAPI` manager client to automate closed-loop Data Point (`DP`) recording triggered by live channel statistics or derived parameter thresholds with hysteresis.

### Usage
```text
dscontrolapp <DShost> <DSconfigname> <DPtrigger> <ONlevel> <OFFlevel> [DPlength]
```

| Argument | Description |
| :--- | :--- |
| **`DShost`** | Hostname or IP address of the target APEX DS server. |
| **`DSconfigname`** | Active DS configuration name. |
| **`DPtrigger`** | Trigger signal specifier: either a parameter name or `<ChannelName>:<Stat>` (channel statistic). |
| **`ONlevel`** | Threshold that initiates `DP` recording when crossed. |
| **`OFFlevel`** | Hysteresis release threshold that stops `DP` recording. |
| **`DPlength`** *(optional)* | Maximum `DP` duration in seconds (forces `DP` close even if `OFFlevel` has not been reached). |

### Example Workflow
```bash
# Start DP recording automatically when Speed_RPM >= 12000, stop when < 11500, max 60s per DP
dscontrolapp 10.1.0.50 Cell2 Speed_RPM 12000 11500 60
```

See also: [APEX DM Overview](README.md) · [DM-cmd Reference](dm-cmd-reference.md) · [APEX DS Suite Overview](../README.md)
