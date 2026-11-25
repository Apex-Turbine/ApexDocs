# Python File Reading & Live Network API (`dsapi.py`)

Extract time waveforms, spectra, statistics, peaks, triggers, timestamps, and scalar parameters from DS/EDAS recordings or live DS 3.x network streams using `dsapi.py`.

## Data Block & Packet Extractors (`dsapi.py`)

Once a `DspBlockData` block is obtained either from an offline recording (`dsapi_file_*`) or a live network session (`get_network_session()`), `dsapi.py` exposes packet-type helpers covering all DS stream types:

| Data Category | Supported Stream / Helper Coverage in `dsapi.py` | Payload Description |
| --- | --- | --- |
| **Raw ADC** | `raw16i`, `raw32i`, `raw32f` | Unscaled 16-bit integer, 32-bit integer, and 32-bit float samples |
| **Calibrated Time** | `time` | Engineering-unit scaled time-domain samples |
| **Complex FFT** | `fft` | Complex frequency spectrum |
| **Magnitude & Envelope** | `mag`, `env` | Spectral magnitude bins and spectral envelope bins |
| **Block Statistics** | `stat` | Per-channel scalar statistical metrics (`RMS`, `Mean`, etc.) |
| **Spectral Peaks** | `peak` | Detected peak frequency, magnitude, phase, and validity flags |
| **Speed / Tach Triggers** | `trigger` | Fractional trigger offsets within block (`val / (1 << 30)`) and speed |
| **Parameters** | `param` | Block-aligned scalar parameter vector |
| **Timestamps** | `timecode`, `timezone` | Block acquisition timestamp and timezone metadata |

## Offline File Reading (`dsapi_file_*`)

Reading files via `dsapi_file_*` supports `.rwx`, `.rwz`, `.pkx`, `.raw`, `.pks`, `.datx` (`.datx_index*`), and `.cats_index` recordings and **does not consume a network license**.

Typical flow in Python:
1. Ensure SDK shared libraries (`dsapiscript`, `dsapi`, `Apex*`) are loadable (`os.add_dll_directory` on Windows, `LD_LIBRARY_PATH` on Linux) and `import dsapi`.
2. Open the target file through the `dsapi_file_*` wrappers exposed on `dsapi`.
3. Inspect setup metadata via `dsapi_setup_*`, `dsapi_chan_*`, `dsapi_param_*`, and `dsapi_stat_*`.
4. Step or seek through blocks using `dsapi_file_*`, checking `timecode` / `timezone` and extracting `raw16i`/`raw32i`/`raw32f`, `time`, `fft`, `mag`, `env`, `stat`, `peak`, `trigger`, and `param` arrays per channel.
5. Close the file handle cleanly when finished.

> [!NOTE]
> File creation and writing (`DSAPI_file_create_raw`, `DSAPI_file_create_peak`, `DSAPI_file_create_datx`, `DSAPI_file_write`) are available only in the [C/C++ File I/O API](../C++/file-io.md).

## Live Network Streaming & Remote Manager Automation

To discover DS 3.x servers, stream live packets, or automate monitoring/recording on a single host from Python:

1. **Acquire Network Session**: Call `dsapi.get_network_session()` (which wraps `dsapi_net_startup` and checks out `APEXAPI_NET_STREAM`, `APEXAPI_NET_RECORD`, and `APEXAPI_NET_CONFIG` under app `DSAPI`).
2. **Discover & Connect**: Query online DS hosts and connect to the target chassis on port `10995+` (`NET_DSP_BASE_PORT`).
3. **Stream Packets**: Subscribe to desired channels and packet types (`raw`, `time`, `mag`, `peak`/`param`), enable decompression if needed, and poll incoming blocks to read `timecode`, `timezone`, waveforms, spectra, statistics, and parameters.
4. **Remote Manager Control**: Claim manager rights to push setups built/modified with `dsapi_setup_*`, run calibration, start/stop monitoring, check recording status/space, and start/stop/annotate recordings.
5. **Teardown**: Release manager lock and shut down the network session cleanly when exiting.

For multi-chassis synchronized clusters (`DSAPI_net_cluster`), DS GUI workspace switching (`DSAPI_net_gui_view*`), or custom App ID overrides (`DSAPI_net_set_appid`), use the [C/C++ System Manager & Clusters API](../C++/system-manager-and-clusters.md).
