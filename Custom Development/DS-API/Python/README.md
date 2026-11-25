# DS-API Python Bindings (`dsapi.py`)

DS-API provides Python 3 bindings in **`dsapi.py`**, implemented using Python's built-in **`ctypes` (`ctypes.CDLL`)** FFI over the **`dsapiscript`** C wrapper library (`dsapiscript.dll` on Windows, `libdsapiscript.so` on Linux, declared in `dsapiscript.h`).

> [!NOTE]
> Unlike the Phoenix API (`phoenixpy`), DS-API Python bindings use `ctypes` (`dsapi.py`) rather than SWIG wrappers. Offline file reading does not require a network license; calling `get_network_session()` / `dsapi_net_startup` initializes licensing under app `DSAPI`.

## Architecture & Module Discovery

`dsapi.py` wraps C entry points exported by `dsapiscript`, binding explicit `argtypes` and `restype` declarations plus convenience helpers such as `get_network_session()`.

### 1. Native Library Search Paths

Make sure both `dsapiscript` and its companion core shared libraries (`dsapi`, `ApexDsp*`, `ApexFile`, `ApexIpc`, `ApexLicenser`, `ApexUtils`, and FlexNet libraries if using legacy licensing) can be loaded by the dynamic linker:

**Windows (Python 3.8+)**:
Because modern Windows Python ignores `PATH` for `ctypes` extension dependencies in many configurations, register the SDK `bin/` (or `lib64/`) directory explicitly before importing `dsapi`:

```python
import os
import sys

sdk_bin = r"C:\path\to\DS-API\bin"      # Contains dsapiscript.dll, dsapi.dll, Apex*.dll
sdk_py  = r"C:\path\to\DS-API\python"   # Contains dsapi.py

os.add_dll_directory(sdk_bin)
sys.path.insert(0, sdk_py)

import dsapi
```

**Linux**:
Set `LD_LIBRARY_PATH` and `PYTHONPATH` (match architecture — 64-bit Python requires 64-bit libraries):

```bash
export LD_LIBRARY_PATH=/path/to/ds-api/lib64:$LD_LIBRARY_PATH
export PYTHONPATH=/path/to/ds-api/python:$PYTHONPATH
python3 your_script.py
```

## Supported Capabilities & Boundaries

| Area | Available in `dsapi.py` | Notes |
| --- | --- | --- |
| **Setup & Configuration** | Yes (`dsapi_setup_*`, `dsapi_rsrc_*`, `dsapi_param_*`, `dsapi_chan_*`, `dsapi_stat_*`) | Inspect and construct setups, channels, parameters, hardware resources, stats |
| **Offline File Reading** | Yes (`dsapi_file_*`) | Read `.rwx`, `.rwz`, `.pkx`, `.raw`, `.pks`, `.datx`, `.cats_index` |
| **Offline File Writing** | **No** | `DSAPI_file_create_*` / `DSAPI_file_write` are C/C++-only (`dsapi.h`) |
| **Live Streaming & Packets** | Yes | Extract `raw16i`, `raw32i`, `raw32f`, `fft`, `mag`, `env`, `time`, `stat`, `peak`, `param`, `trigger`, `timecode`, `timezone` |
| **Single-Host Manager Control** | Yes | Remote configure, calibrate, monitor/record start & stop via `dsapi.py` / `get_network_session()` |
| **Multi-Chassis Clusters / GUI Views** | **No** | `DSAPI_net_cluster` and `DSAPI_net_gui_view*` are C/C++-only (`dsapi.h`, not wrapped in `dsapiscript.h`) |

## Licensing Behavior

- **Offline File Reading & Setup Inspection**: Calling `dsapi_file_*` or local `dsapi_setup_*` does **not** check out network license features.
- **Network Streaming & Control**: Obtaining a session via `get_network_session()` initializes `DSAPI_session_handle` under app `DSAPI` (`APEXAPI_NET_STREAM`, `APEXAPI_NET_RECORD`, `APEXAPI_NET_CONFIG`). See [Developer Licensing Guide](../README.md#developer-licensing-guide).

## Guides

- [Setup Inspection, Creation & TDF Template Notes](setup-and-configuration.md)
- [Offline File Reading & Live Network API](file-and-network-api.md)
