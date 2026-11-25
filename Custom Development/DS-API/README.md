# DS-API Developer Guide

**DS-API** is the official C, C++, 64-bit MATLAB, and Python SDK for reading and writing **APEX DS (DS 3.x)** / EDAS data files, streaming live processed and raw acquisition packets over TCP/IP, automating single-host and synchronized `N:M` multi-chassis test stands, and extending DS with custom driver and DSP statistics plugins.

## Language & Capability Matrix

| Interface | Headers / Bindings | Native Libraries | Offline Read | Offline Write | Live Stream | System Manager | Clusters (`N:M`) | Custom Plugins |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **[C / C++](C++/README.md)** | `dsapi.h`, `dsapi.hpp` | `dsapi` (`dsapi.dll` / `libdsapi.so`) | Yes | `.rwx`, `.pkx`, `.datx` | Yes | Yes | Yes (`DSAPI_net_cluster`) | Device driver & DSP stat |
| **[MATLAB (64-bit)](MatLab/README.md)** | `mxapi.h` | `mxapi` (`mxapi.dll` / `libmxapi.so`) | Yes | No | Yes | Yes | No | No |
| **[Python 3](Python/README.md)** | `dsapi.py` (`ctypes`) | `dsapiscript` (`dsapiscript.dll` / `libdsapiscript.so`) | Yes | No | Yes | Yes | No | No |

## SDK Directory Layout

Depending on whether you consume an SDK package (`Makefile` archive) or a CMake build/install tree (`DS/API/CMakeLists.txt`), directories are laid out as follows:

| Directory | CMake Install Layout | Standalone Package Layout | Contents |
| --- | --- | --- | --- |
| Headers | `include/` | `include/` | `dsapi.h`, `dsapi.hpp`, `mxapi.h`, `dsapiscript.h`, `core/...` headers |
| Shared / Import Libs | `bin/` | `lib/` (32-bit), `lib64/` (64-bit) | `dsapi`, `dsapiscript`, `mxapi`, `ApexDsp*`, `ApexFile`, `ApexIpc`, `ApexLicenser`, `ApexUtils`, FlexNet `libfnp64`/`libfnpts64` |
| Python | `DS/API/dsapi.py` (or `python/`) | `python/` or `samples/` | `dsapi.py` ctypes wrapper, `tdf/tdf2dspro.py` template inspector |
| Documentation | `doc/` | `doc/` | Doxygen sources (`doc/*.dox`) |
| Examples | `examples/` | `examples/`, `examples++/` | `showfile.c`, `showfile.cxx`, `discover.cxx`, `dscontrolapp.cxx`, `paramserver.c`, `matdataviewer.m`, `matdataclient.m` |
| Samples | `samples/`, `samples++/` | `samples/`, `samples++/` | Minimal C & C++ samples (`buildsetup`, `clientconnect`, `controlclient`, `dataclient`, `packetcount`, `show*`) |
| Plugins | `plugins/` | `plugins/` (or `drivers/`) | DSP stat example `dbstat.c` |

## Supported File Formats & Network Protocol

### File Formats (`DSAPI_file_open`)
DS-API automatically detects format and optional compression from the filename or index extension:

| Format | Extensions | Read | Write (`DSAPI_file_create_*`) | Notes |
| --- | --- | --- | --- | --- |
| **EDAS / DS Extended Raw** | `.rwx`, `.rwz` | Yes | Yes (`DSAPI_file_create_raw`) | `FileDspEdas`; optional zlib packet decompression (`DSAPI_file_uncompress`) |
| **EDAS / DS Extended Peak** | `.pkx` | Yes | Yes (`DSAPI_file_create_peak`) | `FileDspEdas`; per-block stats, FFT peaks, and speed triggers |
| **Legacy EDAS Raw & Peak** | `.raw`, `.pks` | Yes | No | `FileDspEdasLegacy` read-only compatibility |
| **Indexed Block Format** | `.datx`, `.datx_index*`, `.datx_[0-9]*` | Yes | Yes (`DSAPI_file_create_datx`) | `FileDspCustomDatx*` fast indexed access & multi-part storage |
| **CATS Format** | `.cats_index`, `*.[Cc][0-9]*` | Yes | No | `FileDspCustomCats*` read-only access |

### Live DS 3.x Network Protocol
- **Discovery**: UDP broadcast discovery on DS ports (`DSAPI_net_discover` / `DSAPI_net_discover_tout`).
- **Session Transport**: TCP client connections starting at `NET_DSP_BASE_PORT` (`10995`, spanning `NET_DSP_MAX_PORTS = 10` ports).
- **Packet Types**: Raw ADC (`raw16i`, `raw32i`, `raw32f`), Scaled Time (`time`), Complex FFT (`fft`), Magnitude & Envelope (`mag`, `env`), Peak/Stats/Speed Triggers (`peak`), Parameter vectors (`param`), and compressed variants (`ZRAW`, `ZTIME`, `ZMAG`, `ZFFT`).

## Developer Licensing Guide

DS-API separates offline file processing from licensed network acquisition operations.

### 1. What Requires a License?
- **No Network License Required**: Opening, seeking, inspecting, and reading offline files (`DSAPI_file_open`, `DSAPI_file_read`, `mxapi_file_*`, `dsapi_file_*`) does **not** initialize `DSAPI_session_handle` and does **not** check out any network license features.
- **License Required**: Calling `DSAPI_net_startup` (or `mxapi_net_startup`, `dsapi.dsapi_net_startup`, `get_network_session`) allocates a `DSAPI_session_handle`, which configures licensing under application `"DSAPI"` and immediately checks out `1` count of each network feature:

| C Macro (`Licenser.h`) | Feature String (`ApexFeatures.csv`) | License Type | Controls |
| --- | --- | --- | --- |
| `LIC_API_NET_STREAM` | `APEXAPI_NET_STREAM` | `COUNTED` | Live streaming data subscription & packet reception |
| `LIC_API_NET_RECORD` | `APEXAPI_NET_RECORD` | `COUNTED` | Remote monitor & recording start/stop/event commands |
| `LIC_API_NET_CONFIG` | `APEXAPI_NET_CONFIG` | `COUNTED` | Remote setup configuration, calibration, and cluster management |

When the session shuts down, the static `Licenser` instance is released (`license(0)`).

### 2. License Lookup Order: FlexNet vs ApexLM
Depending on how the native libraries were built (`-DAPEX_USE_LEGACY_LICENSING` vs `-DAPEX_ALM_LICENSING`):

- **FlexNet Publisher (legacy `ApexLicenser`, default in `DS/API/dsapinet.cxx`)**:
  On session creation, `dsapinet.cxx` configures `"DSAPI"` and searches for a license file via `LIC_USERPATH` in this exact order:
  1. `<executable_dir>/<executable_stem>.lic`
  2. `<dsapi_lib_dir>/<dsapi_stem>.lic` (checking `dsapi` and `libdsapi`)
  3. Empty user path `""`, falling back to standard FlexNet resolution such as the `LM_LICENSE_FILE` environment variable and default vendor paths (runtime depends on `libfnp64` / `libfnpts64`).
- **APEX License Manager (`ApexLM` / `CoreApexLm`, modern builds)**:
  When DS core is built with `-DAPEX_ALM_LICENSING`, licenses are served as Ed25519-signed JSON under application `DSAPI` in `ApexApps.csv` / `ApexFeatures.csv` (`Token Types=NULL`, `Token Cost=NULL`). Clients connect over ZeroMQ CurveZMQ to port `27884` (`APEXLM_PORT`) or a floating license server (`27885` `APEXLM_SERVER_PORT` / `27886` `APEXLM_SERVER_LISTEN`), and local license status can be inspected at `http://127.0.0.1:27887/` (`APEXLM_MANAGEMENT_PORT`).

## Language Guides

- **[C / C++ SDK](C++/README.md)**: Building, RAII vs C lifecycle, data model, file R/W, streaming client, remote/cluster control, and plugins.
- **[MATLAB Interface](MatLab/README.md)**: `mxapi` shared library setup, offline file analysis, and live streaming/manager control.
- **[Python Bindings](Python/README.md)**: `dsapi.py` setup inspection, file reading, and live DS network automation.
