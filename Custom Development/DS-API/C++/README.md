# DS-API C / C++ SDK

> [!IMPORTANT]
> **End-User License Notice:** `DS-API` C/C++ libraries and APEX file/data formats are licensed strictly for internal end-user use and cannot be used for commercial means without formal written authorization from APEX ([Software License Agreement](../../../Release%20Policies/software-license-agreement.md)). Legacy FLEXlm (`lmgrd`) licensing is discontinued in **October 2027**; all product versions going forward use **[APEX License Manager](../../../License%20Manager/README.md)**.

The **C / C++ SDK** is the most complete interface in DS-API, supporting offline file reading and creation (`.rwx`, `.pkx`, `.datx`, `.raw`, `.pks`, `.cats_index`), live DS 3.x network packet streaming, remote manager and synchronized `N:M` cluster automation, and custom C/C++ hardware driver and DSP statistics plugins.

## Headers and Shared Libraries

Include the main umbrella header for both C and C++ callers, or add the C++ header for C++-specific helpers:

```c
#include "dsapi.h"   /* Works in both C and C++ */
```

```cpp
#include "dsapi.h"
#include "dsapi.hpp" /* C++ convenience definitions */
```

`dsapi.h` automatically defines the shared linkage preprocessor flags before importing core headers:
- `CORE_API_SHARED`
- `CORE_DSP_SHARED`
- `CORE_IPC_SHARED`
- `DSAPI` (`extern "C" CORE_API_IMPORT` for consumers, `CORE_API_EXPORT` when building the SDK)

Link against the **`dsapi`** shared library (`dsapi.dll` + import library on Windows, `libdsapi.so` on Linux). At runtime, the dynamic loader also requires DS-API's companion core libraries (installed under `bin/` in CMake installs or `lib/` / `lib64/` in SDK archives):
- `ApexDsp*`, `ApexFile`, `ApexIpc`, `ApexLicenser`, `ApexUtils`
- Legacy FlexNet runtime libraries `libfnp64` / `libfnpts64` when built with `-DAPEX_USE_LEGACY_LICENSING` (or ApexLM runtime when built with `-DAPEX_ALM_LICENSING`)

## Building with CMake or Make

### CMake Example

```cmake
cmake_minimum_required(VERSION 3.16)
project(dsapi_client LANGUAGES C CXX)

find_path(DSAPI_INCLUDE_DIR dsapi.h PATHS "${DSAPI_ROOT}/include" REQUIRED)
find_library(DSAPI_LIBRARY NAMES dsapi PATHS "${DSAPI_ROOT}/lib64" "${DSAPI_ROOT}/lib" "${DSAPI_ROOT}/bin" REQUIRED)

add_executable(my_client main.cxx)
target_include_directories(my_client PRIVATE "${DSAPI_INCLUDE_DIR}")
target_link_libraries(my_client PRIVATE "${DSAPI_LIBRARY}")
```

### Toolchain Notes
- **MSVC (Windows)**: If distributing without an MSVC `.lib` import library, generate one from the DLL export `.def` file using `LIB /DEF:...` (`doc/apipackage.dox`). Ensure architecture (64-bit vs 32-bit) matches `lib64/` vs `lib/`.
- **MinGW-w64 (Windows)**: SDK documentation (`doc/apipackage.dox`) notes compatibility with MinGW-w64 `sjlj` / `win32` builds.
- **Linux**: Built for glibc compatibility (historically CentOS 6+ toolchain baselines); add the SDK `lib64/` directory to `LD_LIBRARY_PATH` or set `RPATH`.

## C Lifecycle Macros vs. C++ RAII Wrappers

Many core structures (`UtilString`, `DspSetup`, `FileDataPoint`, `DspSetupStrList`) contain internal heap allocations managed automatically in C++ via constructors and destructors. When compiling pure **C**, you **must** initialize and dispose these structs explicitly:

| Struct | C Initialization | C Cleanup | C++ Behavior |
| --- | --- | --- | --- |
| `UtilString` | `DSAPI_string_init(&str)` | `DSAPI_string_dispose(&str)` | Constructor / Destructor (macros are no-ops) |
| String list | `DSAPI_strlist_init(&list)` | `DSAPI_strlist_dispose(&list)` | Constructor / Destructor (macros are no-ops) |
| `DspSetup` | `DSAPI_setup_init(&setup)` | `DSAPI_setup_dispose(&setup)` | Constructor / Destructor (macros are no-ops) |
| `FileDataPoint` | `DSAPI_datapoint_init(&dp)` | `DSAPI_datapoint_dispose(&dp)` | Constructor / Destructor (macros are no-ops) |

Additional cross-language C helper utilities in `dsapi.h`:
- `DSAPI_info()` — returns SDK version/build info string
- `DSAPI_setup_copy(...)`, `DSAPI_setup_size(...)`, `DSAPI_setup_stats(...)`
- `DSAPI_datapoint_copy(...)`
- `DSAPI_strlist_size(...)`
- `DSAPI_string_copy(...)`, `DSAPI_string_printf(...)`

### Side-by-Side Idiom (`packetcount.c` vs. `packetcount.cxx`)

**C (`samples/packetcount.c`)** explicitly calls `DSAPI_string_init` / `DSAPI_string_dispose` and accesses struct arrays (`data->channels`, `data->channel[ch].raw`):

```c
UtilString errors;
DSAPI_file file;
DSAPI_string_init(&errors);
if ((file = DSAPI_file_open(name, &errors))) {
  const DspBlockData *data;
  int result;
  while ((data = DSAPI_file_read(file, &result, &errors))) {
    const DspBlockChannel *chan = data->channel;
    for (index_t ch = 0; ch < data->channels; ch++) {
      if (chan[ch].raw) { /* ... */ }
    }
  }
  DSAPI_file_close(file);
}
DSAPI_string_dispose(&errors);
```

**C++ (`samples++/packetcount.cxx`)** omits the init/dispose macros and calls inline member accessors (`data->channels()`, `data->raw(ch)`):

```cpp
UtilString errors;
DSAPI_file file;
if ((file = DSAPI_file_open(name, &errors))) {
  const DspBlockData *data;
  int result;
  while ((data = DSAPI_file_read(file, &result, &errors))) {
    for (index_t ch = 0; ch < data->channels(); ch++) {
      if (data->raw(ch)) { /* ... */ }
    }
  }
  DSAPI_file_close(file);
}
```

## Error Handling and Status Codes

- **File & Setup Functions**: Pass `&errors` (`UtilString *`) to receive human-readable diagnostic messages when calls return `NULL`, false, or a non-zero error status (`int *result`).
- **Asynchronous Network & Manager Replies**: Query host-specific failure strings with `DSAPI_net_last_error(net, id)`.
- **Network Status Codes (`DspNetwork.h`)**:

| Constant | Value | Meaning |
| --- | --- | --- |
| `NET_ERR_SUCCESS` | `0` | Operation succeeded |
| `NET_ERR_CANT_CONNECT` | `-1` | TCP connection to DS server failed |
| `NET_ERR_CONN_REJECT` | `-2` | Server rejected connection (priority, password, or state) |
| `NET_ERR_PROTOCOL` | `-3` | Wire protocol error |
| `NET_ERR_TIMEOUT` | `-4` | Request or handshake timed out |

- **Node Roles & Connection States (`DspNetwork.h`)**:
  - Port range: `NET_DSP_BASE_PORT = 10995`, `NET_DSP_MAX_PORTS = 10`
  - Roles: `NET_DSP_ROLE_SERVER = 70`, `NET_DSP_ROLE_CLIENT = 71`
  - States: `NET_DSP_STATE_IDLE = 60`, `NET_DSP_STATE_RUNNING = 61`, `NET_DSP_STATE_FAILED = 62`, `NET_DSP_STATE_STOPPED = 63`

## Next Steps

- [Data Types & Packet Formats](data-types.md)
- [Offline File I/O](file-io.md)
- [Live Streaming Client](streaming-client.md)
- [System Manager & Multi-Chassis Clusters](system-manager-and-clusters.md)
- [Device Driver Plugins, DSP Stat Plugins & Parameter Server](driver-plugins-and-param-server.md)
