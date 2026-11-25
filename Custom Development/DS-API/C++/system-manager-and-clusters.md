# DS-API C / C++ System Manager and Clusters

Acquire **Manager** privileges on one or more DS 3.x servers to upload configurations, run hardware calibration, synchronize multi-chassis **`N:M` clusters**, and remotely control monitoring and recording.

> [!IMPORTANT]
> Only one high-priority client may hold active manager ownership (`DSAPI_net_manage`) of a DS server at a time. Check connection rejection (`NET_ERR_CONN_REJECT = -2`) and inspect `DSAPI_net_last_error(net, id)` if another controller is attached.

## Manager Ownership Lifecycle

| Function | Description |
| --- | --- |
| `DSAPI_net_manage(net, id, ...)` | Claim remote manager control over connected host `id` |
| `DSAPI_net_is_manager(net, id)` | Return whether this session currently holds manager control on host `id` |
| `DSAPI_net_release(net, id)` | Release manager control cleanly without shutting down the entire session |
| `DSAPI_net_last_error(net, id)` | Return the most recent manager/control error string reported by host `id` |

## Synchronized `N:M` Multi-Chassis Clusters (`DSAPI_net_cluster`)

To coordinate multiple DS acquisition chassis as a single synchronized logical system, first connect and acquire **manager** privileges on every chassis, then group their connection IDs into a cluster:

```c
/* Example: bind 2 or more managed DS chassis into a synchronized cluster */
int host_ids[2] = { id_chassis_1, id_chassis_2 };
int cluster_id = DSAPI_net_cluster(net, 2, host_ids);
```

Verified cluster rules (`dsapinet.cxx`):
- **Minimum members**: Requires **`>= 2`** active manager connections (`count >= 2`).
- **Cluster ID range**: Allocates and returns a valid cluster ID between **`0` and `31`** (up to 32 active clusters).
- Once grouped, configuration updates, monitor start/stop/idle, and recording transitions apply across the synchronized cluster.

## Remote Setup, Calibration, Monitoring, and Recording

| Function | Purpose | Notes |
| --- | --- | --- |
| `DSAPI_net_configure(net, id, setup)` | Upload and apply a `DspSetup` configuration | Targets individual managed host or cluster |
| `DSAPI_net_calibrate(net, id, ...)` | Execute hardware calibration routine | Inspect `DSAPI_net_last_error` on failure |
| `DSAPI_net_monitor_start(net, dpoint, toutms)` | Arm / start monitoring with `FileDataPoint *dpoint` | Times out after `toutms` milliseconds |
| `DSAPI_net_monitor_idle(net, ...)` | Transition acquisition to idle/standby state | Keeps server ready without active streaming |
| `DSAPI_net_monitor_stop(net, ...)` | Stop monitoring | Halts acquisition pipeline |
| `DSAPI_net_record_exists(net, id, ...)` | Check if target recording name/datapoint already exists | Avoids accidental overwrite |
| `DSAPI_net_record_start(net, ...)` | Start saving data to disk on the DS host(s) | Transitions state to recording |
| `DSAPI_net_record_event(net, ...)` | Inject a timestamped manual/automated test event marker | Embedded into recording event log |
| `DSAPI_net_record_stop(net, ...)` | Stop recording and finalize output files | Closes `.rwx` / `.pkx` / `.datx` files on server |
| `DSAPI_net_record_state(net, id)` | Query recording status | Docstring states `0=Off, 1=MON, 2=RECMON, 3=REC` (see `dsapinet.cxx` `0, 1, 2` mapping) |
| `DSAPI_net_record_space(net, id, double space[6])` | Query disk capacity & free-space metrics | Populates 6 `double` values for recording storage |
| `DSAPI_net_reply_record_state(reply)` | Extract recording state from `DspNetReply` | Used with asynchronous reply handling |

## Automated Control Loop (`examples/dscontrolapp.cxx`)

`dscontrolapp.cxx` demonstrates the full remote automation sequence for automated test stands:

1. **Startup & Connect**: Call `DSAPI_net_startup(16, 16)`, discover hosts (`DSAPI_net_discover_tout`), and connect (`DSAPI_net_connect`).
2. **Manage (and Optional Cluster)**: Claim control with `DSAPI_net_manage` (and bind `>= 2` hosts with `DSAPI_net_cluster` when operating synchronized chassis).
3. **Configure**: Push updated channel rates, ranges, and parameters via `DSAPI_net_configure`.
4. **Verify Storage & Datapoint Uniqueness**: Check available disk space via `DSAPI_net_record_space` and check name collisions via `DSAPI_net_record_exists`.
5. **Run Test Sequence**:
   - Call `DSAPI_net_monitor_start(net, &dpoint, toutms)` to verify live levels/health.
   - Transition to recording with `DSAPI_net_record_start` and poll `DSAPI_net_record_state`.
   - Annotate milestones during the test with `DSAPI_net_record_event`.
   - Finish cleanly with `DSAPI_net_record_stop`, then `DSAPI_net_monitor_stop`.
6. **Release & Shutdown**: Relinquish manager lock with `DSAPI_net_release` before calling `DSAPI_net_shutdown`.
