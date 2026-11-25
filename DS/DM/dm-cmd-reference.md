# `DM-cmd` Interactive & Batch Command Reference

`DM-cmd` is the interactive shell and batch script interpreter for **APEX Data Manager (`DM`)**. It connects over TCP/UDP (`10995`–`11004`) to one or more **APEX DS** servers in manager mode to push configurations, start/stop acquisition, record Data Points (`DP`), and verify automation state.

## Invocation & Execution Model

```text
DM-cmd
```

- **Interactive Prompt & Batch Scripts:** Commands can be typed interactively at the `DM-cmd` prompt or read sequentially from batch files via the `load` (`l`) command (supports recursive batch script nesting up to **20 levels** deep).
- **Command Abbreviations (`*`):** In the full `DM-cmd` batch grammar (`DM-api.info`), an asterisk `*` in the command specification denotes the shortest accepted prefix (for example `fa*tal` matches `fa`, `fat`, `fata`, or `fatal`).
- **Dual Build Profiles:** Standard cluster/batch automation builds expose the full command set documented below (`DM-api.info` specification), while minimal interactive builds (`DM-cmd.cxx`) expose a compact single-letter subset (`?`, `q`, `h`, `c host config`, `d`, `i`, `m`, `s`, `r dpnum dpflags`, `e`, `l filename`, `w seconds`, with a `60 s` server handshake timeout). Both forms are noted below where applicable.

## Exit Status

| Exit Code | Meaning |
| :--- | :--- |
| **`0`** | Clean termination via `quit` (`q`) or end-of-input (EOF) on standard input / batch script completion. |
| **Non-zero** | Initialization failure (for example missing/denied `DSAPI` or `DS_MANAGER` license, connection handshake failure exceeding `60 s` in compact `DM-cmd`, or `fatal ON` abort upon command error). |

---

## General & Script Control Commands

| Command | Compact Alias | Arguments | Description |
| :--- | :--- | :--- | :--- |
| `# ...` | `#` | Arbitrary text | Comment line; ignored by the command parser. |
| `fa*tal` | — | `ON` \| `OFF` | Enables (`ON`) or disables (`OFF`) immediate abort on command or server errors. |
| `ech*o` | — | `ON` \| `OFF` | Controls echoing of executed batch script lines to console output. |
| `l*oad` | `l` | `FILE ...` | Executes one or more batch script files sequentially (max include depth `20`). |
| `p*ause` | `w` | `SECONDS` | Pauses script execution for the specified integer number of seconds. |
| `comp*are` | — | `FILE1 FILE2` | Compares two output/configuration files and reports differences (triggers failure under `fatal ON` on mismatch). |
| `sh*ow` | — | `FILENAME` | Displays the contents of `FILENAME` on standard output. |
| `m*essage` | — | `TEXT ...` | Prints a formatted informational message to console/log output. |
| `v*erify` | — | `EXPR ...` | Verifies expected system/cluster status conditions for automated test validation. |
| `q*uit` | `q` | None | Cleanly disconnects active sessions and exits `DM-cmd` with status `0`. |
| `h*elp` / `?` | `?` | None | Prints interactive command usage summary. |

---

## Connection & Configuration Commands

| Command | Compact Alias | Arguments | Description |
| :--- | :--- | :--- | :--- |
| `c*onnect` | `c host config` | `[HOST ...]` | Connects to one or more DS servers in manager mode. Supports multiple target forms:<br>- **Omitted:** lists discovered hosts/configs (`h` in compact CLI).<br>- **Numeric node index:** `1`, `2`, ...<br>- **`N:M` cluster coordinate:** `1:1`, `1:2` (targets member `M` in cluster `N`).<br>- **Hostname / IP:** `hostname` (defaults host to `localhost` when omitted), `hostname:port`, or `hostname:configurationname`.<br>Passing multiple hosts groups them into a synchronized cluster session. |
| `d*isconnect` | `d` | None | Terminates the active DS server / cluster manager connection. |
| `res*tore` | — | None | Restores previously saved connection and acquisition state. |
| `i*nspect` | `i` | `ID [FILENAME]` | Queries live status, configuration metadata, and channel tables for node `ID` (or writes inspected configuration to `FILENAME`). In compact CLI, `i` prints active host info/state. |
| `conf*igure` | — | `ID [FILENAME]` | Pushes a `.dspro` / project configuration file (`FILENAME`) to DS node `ID` (or applies default node configuration). |
| — *(compact)* | `h` | None | Compact CLI discovery command: probes the LAN (`DSAPI_net_discover`) and lists visible DS servers and configuration names. |

---

## Acquisition, Recording & Tabulation Commands

| Command | Compact Alias | Arguments | Description |
| :--- | :--- | :--- | :--- |
| `bu*fdisable` | — | None | Disables rolling pre-trigger memory buffering on connected DS servers. |
| `sta*rt` | `m` | None | Arms/starts live hardware acquisition on all connected DS hosts (`m` = start monitoring in compact CLI). DS enters `RUNNING` state and begins streaming telemetry without yet writing Data Points (`DP`). |
| `sto*p` | `s` | None | Halts hardware acquisition and transitions DS back to idle (`s` = stop monitoring in compact CLI). |
| `r*ecord` | `r dpnum dpflags` | `[NUMBER [FLAGS [TESTID [FILENAME]]]]` | Starts recording a synchronized Data Point (`DP`) across the connected server or cluster.<br>- `NUMBER`: Integer DP index.<br>- `FLAGS`: Recording mode bitmask/flags (raw `.rwx`, peak `.pkx`, or both).<br>- `TESTID`: Optional test/run identifier string.<br>- `FILENAME`: Optional explicit base output path. |
| `fi*nish` | `e` | None | Terminates the active Data Point (`DP`) recording (`e` = end DP in compact CLI). |
| `br*ecord` | — | `BLOCK [NUMBER [FLAGS [TESTID [FILENAME]]]]` | Starts a block-indexed Data Point recording scoped to specific block number `BLOCK` on clustered servers. |
| `bf*inish` | — | `BLOCK` | Stops block-indexed Data Point recording for block `BLOCK`. |
| `t*abulate` | — | `PAGE ROW COLUMN FILENAME` | Extracts and tabulates live cluster/server parameter or display matrix cell `(PAGE, ROW, COLUMN)` to `FILENAME`. |

---

## Annotated Automation Script Examples

### 1. Single-Server Unattended Test Run (Full Batch Grammar)

```text
# Enable strict error checking and trace output
fatal ON
echo ON

# Connect to acquisition host localhost running setup "RigA"
connect localhost:RigA

# Inspect node 1 and load project setup
inspect 1 baseline_status.txt
configure 1 C:\ApexProjects\RigA\baseline.dspro

# Start hardware acquisition and wait 3 seconds for sensor settling
start
pause 3

# Record Data Point 101 for 30 seconds, then close DP
message Recording DP 101 (steady-state point)
record 101 1 RIG_A_RUN01 C:\ApexData\rig_a_101
pause 30
finish

# Stop acquisition and exit cleanly
stop
disconnect
quit
```

### 2. Multi-Node `N:M` Synchronized Cluster Acquisition

```text
# Coordinate two common-clock DS chassis (node 1:1 and node 1:2)
fatal ON
connect 10.20.1.11:ChassisA 10.20.1.12:ChassisB

# Push node-specific configurations and disable ring buffering
configure 1:1 /opt/apex/configs/chassis_a.dspro
configure 1:2 /opt/apex/configs/chassis_b.dspro
bufdisable

# Start synchronized acquisition across both nodes
start
pause 2

# Record synchronized DP 1 and verify / tabulate output
record 1 3 CLUSTER_TEST_01 /data/cluster_dp1
pause 15
finish

tabulate 1 1 1 /data/summary_cell.txt
stop
disconnect
quit
```

### 3. Compact Interactive `DM-cmd` Session (`DM-cmd.cxx` Profile)

```text
h
c localhost RigA
i
m
w 5
r 1 1
w 10
e
s
d
q
```

- `h` discovers LAN servers -> `c localhost RigA` connects as manager -> `m` starts acquisition -> `w 5` waits 5 s -> `r 1 1` begins DP 1 -> `w 10` records 10 s -> `e` ends DP -> `s` stops acquisition -> `d` disconnects -> `q` exits `0`.

See also: [APEX DM Overview](README.md) · [Automation & CLI Utilities](automation-utilities.md)
