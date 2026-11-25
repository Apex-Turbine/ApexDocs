# MATLAB Network Streaming and Acquisition Manager

Modern builds of `mxapi` support **both** live TCP packet streaming from DS 3.x servers **and** remote acquisition manager automation (`mxapi_net_*` functions exported in `mxapi.h`).

> [!NOTE]
> Calling `mxapi_net_startup` creates a licensed DS-API network session under app `DSAPI` (`APEXAPI_NET_STREAM`, `APEXAPI_NET_RECORD`, `APEXAPI_NET_CONFIG`). See [Developer Licensing Guide](../README.md#developer-licensing-guide).

## Capabilities Overview (`mxapi_net_*`)

Using `mxapi.h` with MATLAB `calllib`, scripts can:
1. Initialize and tear down a network session (`mxapi_net_startup`, shutdown/cleanup)
2. Discover and connect to DS 3.x servers on the network (1-based host indices)
3. Inspect live remote `DspSetup` channels, parameters, and statistics
4. Subscribe to packet types (`raw`, `time`, `mag`/`env`, `peak`/`stat`, `param`) and dequeue incoming live blocks into MATLAB arrays
5. Acquire **Manager** control (`mxapi_net_manage`) to remotely arm/start/idle/stop monitoring and recording

## Critical Handle Rule: `hsession` vs. `hmanager`

> [!WARNING]
> Pay close attention to which handle each `mxapi_net_*` control function validates in `mxapi.cpp`! Several monitor and recording commands validate `SESSION_HANDLE` (`hsession` from `mxapi_net_startup`) rather than `MANAGER_HANDLE` (`hmanager` from `mxapi_net_manage`), even though inline docstrings mention `hmanager`.

Check the handle requirement table verified against `mxapi.cpp`:

| Function | Expected Handle Argument | Notes |
| --- | --- | --- |
| `mxapi_net_startup` | *(returns `hsession`)* | Initializes DS-API networking and checks out network license features |
| `mxapi_net_manage` | `hsession` *(returns `hmanager`)* | Acquires manager ownership on target host |
| `mxapi_net_monitor_start` | **`SESSION_HANDLE` (`hsession`)** | Validates `hsession` in `mxapi.cpp` |
| `mxapi_net_monitor_start_dp` | **`SESSION_HANDLE` (`hsession`)** | Validates `hsession` in `mxapi.cpp` (starts with datapoint metadata) |
| `mxapi_net_monitor_stop` | **`SESSION_HANDLE` (`hsession`)** | Validates `hsession` in `mxapi.cpp` |
| `mxapi_net_monitor_idle` | **`SESSION_HANDLE` (`hsession`)** | Validates `hsession` in `mxapi.cpp` |
| `mxapi_net_record_start` | **`SESSION_HANDLE` (`hsession`)** | Validates `hsession` in `mxapi.cpp` |
| `mxapi_net_record_start_dp` | **`SESSION_HANDLE` (`hsession`)** | Validates `hsession` in `mxapi.cpp` (records with datapoint metadata) |
| `mxapi_net_record_stop` | **`SESSION_HANDLE` (`hsession`)** | Validates `hsession` in `mxapi.cpp` |
| `mxapi_net_release` | **`MANAGER_HANDLE` (`hmanager`)** | Releases manager ownership; requires `hmanager` |
| `mxapi_net_record_state` | **`MANAGER_HANDLE` (`hmanager`)** | Queries host recording state; requires `hmanager` |
| `mxapi_net_record_header` | **`MANAGER_HANDLE` (`hmanager`)** | Updates/queries recording header metadata; requires `hmanager` |
| `mxapi_net_last_error` | **`MANAGER_HANDLE` (`hmanager`)** | Returns last remote manager error message; requires `hmanager` |

Multi-chassis cluster synchronization (`DSAPI_net_cluster`) and GUI perspective switching (`DSAPI_net_gui_view*`) are available only in the [C/C++ SDK](../C++/system-manager-and-clusters.md).

## Walkthrough: `examples/matdataclient.m`

The SDK's `examples/matdataclient.m` demonstrates real-time DS streaming inside MATLAB:

1. **Load `mxapi`**: Call `loadlibrary` on `mxapi` + `mxapi.h` and verify `mxapi_version`.
2. **Start Network Session**: Call `mxapi_net_startup` to obtain `hsession`.
3. **Discover & Connect**: Run DS host discovery, choose the 1-based target host index, and connect as client (optionally also calling `mxapi_net_manage` if remote start/stop automation is required).
4. **Query Live Setup & Subscribe**: Call `mxapi_setup_info`, `mxapi_setup_channel`, and `mxapi_setup_param` on the remote setup, then enable packet subscriptions for target channels and packet streams.
5. **Stream & Visualize**: Poll incoming packets in a loop, extracting vectors via `mxapi_time_data`, `mxapi_mag_data`, `mxapi_peak_*`, and `mxapi_param_*` for live plotting or analysis.
6. **Cleanup**: Release manager ownership (`mxapi_net_release(hmanager)` if acquired), disconnect/shut down the network session, and call `unloadlibrary('mxapi')`.
