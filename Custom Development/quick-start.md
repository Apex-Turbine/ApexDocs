# APEX Custom Development Quick Start Guide

> [!IMPORTANT]
> **Non-Commercial End-User API & Format License:** APEX SDKs, APIs, and data formats are licensed strictly for **internal end-user use** and cannot be used for commercial means without formal written authorization from APEX ([Software License Agreement](../Release%20Policies/software-license-agreement.md)).
>
> **Legacy FLEXlm / FlexNet Discontinuation (October 2027):** Legacy **FLEXlm / FlexNet (`lmgrd`)** licensing will be discontinued as of **October 2027**. Target **[APEX License Manager](../License%20Manager/README.md)** (`ApexLM`, **APEX LM Daemon**, and **APEX LM Server Daemon**) for all new development.

This guide helps developers choose between **DS-API** and **Phoenix API**, verify developer licensing, and build their first working integration in **C++**, **Python**, or **MATLAB**.

---

## Step 1: Choose Your SDK & Check Licensing

| Need | Recommended SDK | Developer License Features |
| :--- | :--- | :--- |
| Read/write `.rwx` / `.pkx` / `.datx` files or control **APEX DS (DS 3.x)** servers & `N:M` clusters | **[DS-API](DS-API/README.md)** | Offline file reading requires **no network license** (still subject to the [End-User SLA](../Release%20Policies/software-license-agreement.md)); live streaming/control checks out `APEXAPI_NET_STREAM`, `APEXAPI_NET_RECORD`, `APEXAPI_NET_CONFIG` under app `DSAPI`. |
| Build **C++20** or **Python (`phoenixpy`)** streaming DAG pipelines, database readers/writers, or custom DX+ components/devices | **[Phoenix API](Phoenix%20API/README.md)** | Enforced via `PhoenixLic` / `ApexLmClient` against **[APEX License Manager (`ApexLM`)](../License%20Manager/README.md)** on port `27884` (`http://127.0.0.1:27887/`). |

See the complete comparison in [Custom Development Overview](README.md).

---

## Step 2: DS-API Quick Start

### Python (`dsapi.py`) — Read an Offline File

Ensure `dsapiscript.dll` (`libdsapiscript.so` on Linux) and `dsapi.py` are on your library/module path ([DS-API Python Guide](DS-API/Python/README.md)):

```python
import dsapi

handle = dsapi.dsapi_file_open(r"C:\data\run01.rwx")
n_chan = dsapi.dsapi_file_channel_count(handle)
print(f"Opened RWX file with {n_chan} channels")
dsapi.dsapi_file_close(handle)
```

For live DS server discovery, streaming, and manager control in Python, see [File & Network API](DS-API/Python/file-and-network-api.md).

### C / C++ — Discover Live DS Servers & Stream

Link against `dsapi` and include `dsapi.h` ([DS-API C++ Guide](DS-API/C++/README.md)):

```c
#include "dsapi.h"
#include <stdio.h>

int main(void) {
    DSAPI_session net = DSAPI_net_startup(16, 16);
    if (!net) return 1;

    DspNetHost hosts[8];
    int count = DSAPI_net_discover_tout(net, hosts, 8, 2000);
    printf("Discovered %d DS servers\n", count);

    DSAPI_net_shutdown(net);
    return 0;
}
```

### 64-Bit MATLAB (`mxapi`)

Load `mxapi.dll` / `libmxapi.so` with `mxapi.h` ([DS-API MATLAB Guide](DS-API/MatLab/README.md)):

```matlab
loadlibrary('mxapi', 'mxapi.h');
fh = calllib('mxapi', 'mxapi_file_open', 'C:\data\run01.rwx');
nchan = calllib('mxapi', 'mxapi_setup_channel_count', fh);
calllib('mxapi', 'mxapi_file_close', fh);
unloadlibrary('mxapi');
```

---

## Step 3: Phoenix API Quick Start

### Python (`phoenixpy` SWIG Package)

Install the `phoenixpy` wheel (Python `>= 3.12`) and verify runtime libraries ([Phoenix Python Guide](Phoenix%20API/Python/README.md)):

```python
import phoenixpy as px

# Initialize developer licensing (ApexLM daemon on TCP 27884)
px.PhoenixLic.init("PHOENIX")

# Inspect built-in component catalog
mgr = px.ComponentManager()
print("Loaded Phoenix ComponentManager")
```

For full `GraphJson` pipeline examples, database queries (`PhoenixDBReader` / `DBQuery`), and live ZeroMQ streams (`StreamReceiver`), see:

- [Licensing from Python](Phoenix%20API/Python/licensing.md)
- [Building & Running Pipelines](Phoenix%20API/Python/pipelines-and-graphs.md)
- [File, Database & Stream I/O in Python](Phoenix%20API/Python/data-io-and-databases.md)

### C++20 SDK

Link against `PhoenixCore` and `PhoenixLic` targets via CMake and initialize `PhoenixLic` before instantiating `ComponentLibraryManager`, `DeviceLibraryManager`, or `OnlineComponentManager` ([Phoenix C++ Guide](Phoenix%20API/C++/README.md) · [C++ Licensing](Phoenix%20API/C++/licensing.md)).
