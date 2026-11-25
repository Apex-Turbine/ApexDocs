# Custom Development

> [!IMPORTANT]
> **Strict Non-Commercial End-User API & Format License:** All APEX APIs, SDKs, headers, client bindings (`DS-API`, `Phoenix API`), and APEX file, database, and streaming formats are provided strictly for **internal end-user use** by licensed customers with authorized APEX software. They **cannot be used for commercial means** (including commercial SaaS, resale, or third-party commercial adapters/translators) unless explicitly authorized by APEX through formal written agreement. See the complete **[Software License Agreement](../Release%20Policies/software-license-agreement.md)** and **[Software Release Policies](../Release%20Policies/README.md)**.

Build custom acquisition, streaming, post-processing, and automation software on top of the **APEX DS** and **APEX Phoenix** platforms.

> [!TIP]
> New to the SDKs? Follow the **[Custom Development Quick Start Guide](quick-start.md)** for minimal working examples in C++, Python, and MATLAB.

> [!IMPORTANT]
> Choose **DS-API** when integrating with existing **APEX DS (DS 3.x)** servers, DS acquisition clusters, or legacy `.rwx` / `.pkx` / `.raw` / `.pks` / `.datx` / `.cats` workflows. Choose **Phoenix API** for modern **C++20 / Python (`phoenixpy`)** composable DAG pipelines (`Component` / `GraphJson`), direct hardware device drivers (`DeviceLibrary`), ZeroMQ streaming (`DXPNet`), and **SQLite / PostgreSQL** storage.

## Platform Comparison

| Capability | [DS-API](DS-API/README.md) | [Phoenix API](Phoenix%20API/README.md) |
| --- | --- | --- |
| **Target Ecosystem** | APEX DS (DS 3.x) servers & standalone files | APEX Phoenix / DX+ modular pipeline runtime |
| **C / C++ SDK** | C & C++ shared library (`dsapi.h` / `dsapi.hpp`, `dsapi`) | C++20 (`PhoenixCore`, `PhoenixLic`, modular plugin libs) |
| **Python Bindings** | `dsapi.py` (`ctypes` over `dsapiscript.dll` / `libdsapiscript.so`) | `phoenixpy` SWIG (`abi3`, Python `>=3.12`, strict `bytes`/`str`) |
| **MATLAB Bindings** | 64-bit MATLAB (`loadlibrary`/`calllib` via `mxapi.h` & `mxapi`) | Not provided |
| **Live Streaming** | DS 3.x UDP discovery & TCP packet streaming (base port `10995`, 10 ports) | ZeroMQ (`DXPNetReceiver` / `DXPNetTransmitter`) + DS 3.x bridge (`DSNetReceiver`) |
| **Remote System Control** | Single-host `DSAPI_net_manage` & synchronized `N:M` clusters (`DSAPI_net_cluster`) | `ComponentManager` / `OnlineComponentManager`, `Apps/` (`PhoenixEngine`, `PhoenixFoundry`, `PhoenixOPCUA`, `PhoenixPLC`) |
| **File Reading** | `.rwx`, `.rwz`, `.pkx`, `.raw`, `.pks`, `.datx`, `.cats_index` (all languages) | `.rwx`, `.datx` (`FileLibrary`), plus offline `OfflineQueryComponentManager` |
| **File Writing** | `.rwx`, `.pkx`, `.datx` (`DSAPI_file_create_*` in C/C++) | `.rwx`, `.datx` (`FileLibrary`), plus `APEX-H5` output components |
| **Database I/O** | None built in | `SQLite` & `PostgreSQL` (`PhoenixDBConnection`, `PhoenixDBReader`, `PhoenixDBWriter`, `DBQuery`) |
| **Custom Plugins** | C/C++ Device Driver (`EDASpluginTable`/`PluginDev`) & DSP Stat (`DspPlugin`) | C++20 `Component` (`ComponentLibrary`) & `Device` (`DeviceLibrary`) shared libraries |
| **External Telemetry Ingest** | TCP Parameter Server (`MAGIC_NOTIME=0x15260826`, `MAGIC_TIME=0x18480315`) | `StreamReceiver`, OPC UA (`PhoenixOPCUA`), PLC (`PhoenixPLC`), virtual sensors |

## Choosing an API by Workflow

### 1. Offline Data Extraction & Conversion
- **DS-API**: Ideal for sequential or random-block extraction from DS/EDAS files in [C/C++](DS-API/C++/file-io.md), [MATLAB](DS-API/MatLab/file-reader.md), or [Python](DS-API/Python/file-and-network-api.md). Calling `DSAPI_file_*` functions does not consume network licenses.
- **Phoenix API**: Use [File & Database I/O (C++)](Phoenix%20API/C++/devices-streams-and-io.md) or [Python Data I/O](Phoenix%20API/Python/data-io-and-databases.md) when combining `.rwx` / `.datx` files with SQLite/PostgreSQL storage, virtual channels (`VirtualSensorManager`), or offline DAG processing (`OfflineQueryComponentManager`).

### 2. Real-Time Monitoring & Automated Test Control
- **DS-API**: Use [Streaming Client](DS-API/C++/streaming-client.md) and [System Manager & Clusters](DS-API/C++/system-manager-and-clusters.md) (or MATLAB `mxapi_net_*` / Python `dsapi.py`) to discover DS 3.x chassis, push `.dspro` setups, arm calibration, synchronize `N:M` clusters, and trigger recording.
- **Phoenix API**: Build or load `GraphJson` topologies with [Pipelines & Components (C++)](Phoenix%20API/C++/pipeline-and-components.md) or [Python Pipelines](Phoenix%20API/Python/pipelines-and-graphs.md) to process live hardware/ZMQ streams directly inside your own process or via [Phoenix Apps](Phoenix%20API/Apps/README.md).

### 3. Hardware & Custom Processing Extensions
- **DS-API**: Implement [Driver Plugins & Parameter Server](DS-API/C++/driver-plugins-and-param-server.md) to add custom hardware drivers (`PluginDev`) or custom DSP statistics (`DspPlugin`) to DS 3.x, or stream external scalar telemetry over the TCP Parameter Server protocol.
- **Phoenix API**: Implement [Custom C++ Plugins](Phoenix%20API/C++/custom-plugins.md) loaded dynamically by `ComponentLibrary` and `DeviceLibrary`.

## Developer Licensing Matrix

> [!WARNING]
> **Legacy FLEXlm / FlexNet Discontinuation — October 2027**
> Legacy **FLEXlm / FlexNet** (`lmgrd`, `lmtools`, `.lic` files, `27000@host`) licensing will be **discontinued as of October 2027**. All custom applications and product versions going forward exclusively use **[APEX License Manager](../License%20Manager/README.md)** (`ApexLM`), the **APEX LM Daemon (`ApexLM_Service`)**, and the **APEX LM Server Daemon (`ApexLM_Server_Service`)**.

Both APIs distinguish between **local/offline API calls** and **network/runtime features** enforced via **[APEX License Manager (ApexLM)](../License%20Manager/README.md)** or legacy **FlexNet Publisher (FNP)** *(discontinued October 2027)*:

| API | Application ID (`ApexApps`) | License Features Checked Out | Licensing Backend & Ports | Offline File I/O License Required? |
| --- | --- | --- | --- | --- |
| **DS-API (C/C++, MATLAB, Python)** | `DSAPI` | `APEXAPI_NET_STREAM`, `APEXAPI_NET_RECORD`, `APEXAPI_NET_CONFIG` (`COUNTED`) | FlexNet *(legacy, ends Oct 2027)* or ApexLM (`-DAPEX_ALM_LICENSING`, CurveZMQ `27884`, loopback Web UI `27887`) | **No** (`DSAPI_file_*` does not check out network seats; still bound by [End-User SLA](../Release%20Policies/software-license-agreement.md)) |
| **Phoenix API (`PhoenixLic` / `ApexLmClient`)** | `PHOENIX`, `DXPLUS`, `DX+DAQ`, `DX+ONLINEANALYSIS`, `DX+OFFLINEANALYSIS`, `DX+REMOTEVIEWER`, `DX+DATAVIEWER`, `OPCUA`, `DBMANAGE` | Feature & channel/token checkouts + hardware serial verification per workflow/component | **ApexLM** (`27884` local client, `27885`/`27886` server, `http://127.0.0.1:27887/` local UI, `http://127.0.0.1:27888/` server loopback UI; signed v2 JSON; `LOCAL`/`PASSTHROUGH`/`SERVER`; 30-day offline reservation via **Reserve** tab) | Required when initializing licensed `PhoenixLic` components/pipelines |

See [DS-API Licensing](DS-API/README.md#developer-licensing-guide), [Phoenix C++ Licensing](Phoenix%20API/C++/licensing.md), and the **[APEX License Manager Documentation](../License%20Manager/README.md)** for exact initialization sequences and error handling.

## Documentation Map

- **[DS-API Documentation](DS-API/README.md)**
  - [C / C++ SDK](DS-API/C++/README.md): [Data Types](DS-API/C++/data-types.md) · [File I/O](DS-API/C++/file-io.md) · [Streaming Client](DS-API/C++/streaming-client.md) · [System Manager & Clusters](DS-API/C++/system-manager-and-clusters.md) · [Driver Plugins & Parameter Server](DS-API/C++/driver-plugins-and-param-server.md)
  - [MATLAB Interface](DS-API/MatLab/README.md): [File Reader](DS-API/MatLab/file-reader.md) · [Network Streaming & Manager](DS-API/MatLab/network-streaming-and-manager.md)
  - [Python Bindings](DS-API/Python/README.md): [Setup & Configuration](DS-API/Python/setup-and-configuration.md) · [File & Network API](DS-API/Python/file-and-network-api.md)
- **[Phoenix API Documentation](Phoenix%20API/README.md)**
  - [C++20 SDK](Phoenix%20API/C++/README.md): [Licensing](Phoenix%20API/C++/licensing.md) · [Pipelines & Components](Phoenix%20API/C++/pipeline-and-components.md) · [Devices, Streams & I/O](Phoenix%20API/C++/devices-streams-and-io.md) · [Data Types & Utilities](Phoenix%20API/C++/data-types-and-utilities.md) · [Custom Plugins](Phoenix%20API/C++/custom-plugins.md)
  - [Python (`phoenixpy`)](Phoenix%20API/Python/README.md): [Licensing](Phoenix%20API/Python/licensing.md) · [Pipelines & Graphs](Phoenix%20API/Python/pipelines-and-graphs.md) · [Data I/O & Databases](Phoenix%20API/Python/data-io-and-databases.md) · [Module Reference](Phoenix%20API/Python/module-reference.md)
  - [PhoenixCore Modules](Phoenix%20API/PhoenixCore/PhoenixCore.md) · [Ports & Endpoints](Phoenix%20API/PhoenixCore/ports.md) · [Components Catalog](Phoenix%20API/Components/Inputs/README.md) · [Phoenix Applications](Phoenix%20API/Apps/README.md) ([PhoenixFoundry](Phoenix%20API/Apps/PhoenixFoundry.md) · [PhoenixOPCUA](Phoenix%20API/Apps/PhoenixOPCUA.md) · [PhoenixPLC](Phoenix%20API/Apps/PhoenixPLC.md) · [PhoenixEngine](Phoenix%20API/Apps/PhoenixEngine.md))
