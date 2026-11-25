# Index

Complete navigation index for all **APEX** user documentation, Quick Start guides, and developer API SDKs.

---

## 1. DS — Data Acquisition & Telemetry Suite

High-speed synchronized hardware acquisition (`DS`), networked engineering display stations (`DR`), multi-chassis `N:M` cluster automation (`DM`), live/file analog waveform output (`DO`), and vendor hardware drivers (`Drivers`).

- **Primary Links**: **[DS Quick Start Guide](DS/quick-start.md)** · **[DS Master Documentation](DS/README.md)**

### Sub-Manuals

- **DS — APEX Data System ([`DS/DS/`](DS/DS/README.md))**
  - [Overview](DS/DS/overview/README.md): [Hardware](DS/DS/overview/hardware.md) · [Software](DS/DS/overview/software.md) · [Data Processing](DS/DS/overview/dataproc.md) · [Data Storage](DS/DS/overview/datastore.md)
  - [Installation](DS/DS/installation/README.md): [Hardware Requirements](DS/DS/installation/hwrequired.md) · [Software Requirements](DS/DS/installation/swrequired.md) · [Installation](DS/DS/installation/installation.md) · [Licensing (`ApexLM` & FlexNet)](DS/DS/installation/licensing.md)
  - [User Interface](DS/DS/interface/README.md): [Menu Bar](DS/DS/interface/menubar.md) · [Record Bar](DS/DS/interface/recordbar.md) · [Status Bar](DS/DS/interface/statusbar.md) · [Plot Area](DS/DS/interface/plotarea.md) · [Test Ops](DS/DS/interface/testops.md) · [Calibration](DS/DS/interface/calibration.md) · [Simulator](DS/DS/interface/simulator.md) · [Preferences](DS/DS/interface/preferences.md) · [Data Point](DS/DS/interface/datapoint.md) · [Alarm View](DS/DS/interface/alarmview.md) · [Licensing Dialog](DS/DS/interface/licensing.md)
  - [Plots](DS/DS/plots/README.md): [Plot Area](DS/DS/plots/plotarea.md) · [Plot Creation](DS/DS/plots/plotcreate.md) · [Plot Setup](DS/DS/plots/plotsetup.md) · [Plot Matrix](DS/DS/plots/plotmatrix.md) · [Plot Export](DS/DS/plots/plotexport.md)
  - [Acquisition Setup](DS/DS/setup/README.md): [Common](DS/DS/setup/common.md) · [Devices](DS/DS/setup/devices.md) · [Channels](DS/DS/setup/channels.md) · [Duplicated Channels](DS/DS/setup/duplicated.md) · [Amplifiers](DS/DS/setup/amplifiers.md) · [Processing](DS/DS/setup/processing.md) · [Computed Channels](DS/DS/setup/computed.md) · [Parameters](DS/DS/setup/parameters.md) · [Storage](DS/DS/setup/storage.md) · [Networking](DS/DS/setup/networking.md) · [Plugins](DS/DS/setup/plugins.md) · [Advanced](DS/DS/setup/advanced.md)
  - [Appendix](DS/DS/appendix/README.md) · [FAQ](DS/DS/faq/README.md)
- **DR — APEX Data Remote ([`DS/DR/`](DS/DR/README.md))**
  - [Overview](DS/DR/overview/README.md) · [Installation & Licensing](DS/DR/installation/licensing.md) · [User Interface](DS/DR/interface/README.md) · [Server Connections](DS/DR/interface/servers.md) · [Plots](DS/DR/plots/README.md) · [Setup](DS/DR/setup/README.md)
- **DM — APEX Data Manager ([`DS/DM/`](DS/DM/README.md))**
  - [DM Overview, Clusters & Licensing](DS/DM/README.md) · [`DM-cmd` Interactive & Batch Reference](DS/DM/dm-cmd-reference.md) · [Automation CLI Utilities](DS/DM/automation-utilities.md)
- **DO — APEX Data Output ([`DS/DO/`](DS/DO/README.md))**
  - [APEX Data Output Utility & D2A Hardware Reference](DS/DO/README.md)
- **Drivers — DS Hardware Drivers ([`DS/Drivers/`](DS/Drivers/README.md))**
  - [Master Hardware Driver Matrix](DS/Drivers/README.md) · [Plugin Architecture & Licensing](DS/Drivers/architecture-and-licensing.md) · [National Instruments](DS/Drivers/national-instruments.md) · [VTI Instruments](DS/Drivers/vti-instruments.md) · [General Standards & PCI](DS/Drivers/general-standards-and-pci.md) · [Telemetry & High-Speed](DS/Drivers/telemetry-and-high-speed.md) · [Pressure & Auxiliary](DS/Drivers/pressure-and-auxiliary.md)

---

## 2. DX — Data Explorer

Post-test engineering signal processing, visual DAG workflows, order-domain tracking, parameter merging, scope limits evaluation, and multi-format data viewing across `.rwx`, `.pkx`, `.datx`, `.raw`, and `.pks` runs.

- **Primary Links**: **[DX Quick Start Guide](DX/quickstart.md)** · **[DX Master Documentation](DX/README.md)**

### Sections

- **Getting Started**: [Overview](DX/overview.md) · [Requirements](DX/require.md) · [Installation](DX/install.md) · [Licensing (`ApexLM` & FlexNet)](DX/licensing.md) · [FlexNet Details](DX/flex.md)
- **Workspace & Workflows**: [DX Designer](DX/design.md) · [DX Viewer](DX/view.md) · [Connections Guide](DX/connect.md) · [Preferences](DX/prefs.md) · [Reporting](DX/report.md)
- **Analysis & Reference**: [Order Domain Processing](DX/order.md) · [Parameter Merge](DX/parametermerge.md) · [Supported Data Formats](DX/formats.md) · [Scope Limits Format](DX/limits.md) · [Regular Expressions](DX/regexp.md) · [FAQ](DX/faq.md) · [Issues & Limitations](DX/issues.md) · [Version History](DX/versions.md) · [Attribution](DX/attr.md) · [About](DX/about.md) · [SLA](DX/sla.md)

---

## 3. GageMap — FE Sensor Optimization & Fatigue Suite

Finite-element model conversion from ANSYS, ABAQUS, and NASTRAN (`SDR Converter`), reduced-model inspection and manipulation (`SDRFM`), interactive desktop sensor placement & HCF fatigue (`GM` / `GMx`), Lua scripting (`GmScript`), and mathematical theory (`GM Theory`).

- **Primary Links**: **[GageMap Quick Start Guide](GageMap/quick-start.md)** · **[GageMap Master Documentation](GageMap/README.md)**

### Suite Components

- **GM — GageMap Classic ([`GageMap/GM/`](GageMap/GM/README.md))**
  - [Intro](GageMap/GM/intro.md) · [Installation](GageMap/GM/install.md) · [Licensing (`ApexLM` & FlexNet)](GageMap/GM/flex.md) · [Using SDR Models](GageMap/GM/usingSDR.md) · [SGA Format](GageMap/GM/SGA_File_Formats.md)
  - Tasks: [Animation](GageMap/GM/task_modelAnim.md) · [Grouping](GageMap/GM/task_group.md) · [Sensors](GageMap/GM/task_sensors.md) · [Tip Timing](GageMap/GM/tiptiming.md) · [Optimization](GageMap/GM/task_optimize.md) · [CSS Phase Search](GageMap/GM/task_cssPhaseSearch.md) · [Mean Stress](GageMap/GM/task_meanStress.md) · [Fatigue](GageMap/GM/task_fatigue.md) · [Model Validation](GageMap/GM/task_modelValid.md)
- **GMx — GageMap Next Gen ([`GageMap/GMx/`](GageMap/GMx/README.md))**
  - [Overview](GageMap/GMx/overview.md) · [Project File Formats (`.gmp`)](GageMap/GMx/files.md) · [Installation](GageMap/GMx/install.md) · [Licensing (`ApexLM` & FlexNet)](GageMap/GMx/flex.md) · [Model Connections](GageMap/GMx/modelcon.md) · [Custom Fatigue Libraries](GageMap/GMx/custom_fatigue_library_support.md)
- **GmScript — Lua Batch Engine ([`GageMap/GmScript/`](GageMap/GmScript/README.md))**
  - [Intro & Scripting Guide](GageMap/GmScript/intro.md) · [Installation & Licensing](GageMap/GmScript/install.md) · [Scripting Basics](GageMap/GmScript/script_basics.md) · [Main Module](GageMap/GmScript/script_main.md) · [SDRFM Module](GageMap/GmScript/script_sdrfm.md)
- **GM Theory — Engineering Reference ([`GageMap/GM Theory/`](GageMap/GM%20Theory/README.md))**
  - [Introduction](GageMap/GM%20Theory/intro.md) · [Strain & Stress](GageMap/GM%20Theory/strainStress.md) · [Sensor Mapping](GageMap/GM%20Theory/MappingSensors.md) · [Tip Timing](GageMap/GM%20Theory/TipTimingSensors.md) · [Pre-Test Optimization](GageMap/GM%20Theory/PreTestOpt.md) · [Cyclic Symmetry](GageMap/GM%20Theory/css.md) · [Anisotropic Materials](GageMap/GM%20Theory/anisthropicMat.md) · [Mean Stress](GageMap/GM%20Theory/meanStress.md) · [Fatigue Assessment](GageMap/GM%20Theory/fatigueassessment.md)
- **SDRFM — SDR File Manager ([`GageMap/SDRFM/`](GageMap/SDRFM/README.md))**
  - [SDRFM Overview & Licensing](GageMap/SDRFM/README.md) · [Browsers & Operations](GageMap/SDRFM/browsers-and-operations.md) · [`.sdr` Format & Batch CLI](GageMap/SDRFM/file-format-and-batch.md)
- **SDR Converter ([`GageMap/SDR Converter/`](GageMap/SDR%20Converter/README.md))**
  - [Unified `SdrConverter` Overview](GageMap/SDR%20Converter/README.md) · [ANSYS](GageMap/SDR%20Converter/ansys.md) · [ABAQUS](GageMap/SDR%20Converter/abaqus.md) · [NASTRAN](GageMap/SDR%20Converter/nastran.md)

---

## 4. DX+ — Acquisition, Streaming & Analytics Platform

*(Maintained via the `dxplus-doc` Git submodule)*

Modern Phoenix-powered desktop and service ecosystem providing hardware DAQ (`DX+DAQ`), real-time streaming pipelines (`DX+OnlineAnalysis`), post-test querying (`DX+OfflineAnalysis`), live monitoring (`DX+RemoteViewer`), recorded visualization (`DX+DataViewer`), database tooling (`DB Manager`), and industrial OPC-UA / PLC bridges (`DXNet`).

- **Primary Links**: **[DX+ Quick Start Guide](DX+/quick-start.md)** · **[DX+ Master Documentation](DX+/README.md)**

### Applications, Tools & Services

- **Getting Started ([`DX+/introduction/`](DX+/introduction/README.md))**: [Introduction](DX+/introduction/introduction.md) · [Features](DX+/introduction/features-overview.md) · [System Requirements](DX+/introduction/system-requirements.md) · [Installation & `ApexLM` Licensing](DX+/introduction/installing-and-licensing.md) · [Quick Start: Datatel](DX+/introduction/quick-start-datatel.md) · [Quick Start: VTI](DX+/introduction/quick-start-vti.md) · [Data Formats & DB Schema](DX+/introduction/data-formats.md)
- **DX+DAQ ([`DX+/DX+DAQ/`](DX+/DX+DAQ/README.md))**: [General](DX+/DX+DAQ/general/README.md) · [Devices](DX+/DX+DAQ/devices/README.md) · [Processors](DX+/DX+DAQ/processors/README.md) · [Outputs](DX+/DX+DAQ/outputs/README.md)
- **DX+OnlineAnalysis ([`DX+/DX+OnlineAnalysis/`](DX+/DX+OnlineAnalysis/README.md))**: [Designer Workspace](DX+/DX+OnlineAnalysis/designer-workspace.md) · [Inputs & Streams](DX+/DX+OnlineAnalysis/inputs-and-streams.md) · [Processors](DX+/DX+OnlineAnalysis/processors.md) · [Outputs](DX+/DX+OnlineAnalysis/outputs.md) · [Live Monitoring](DX+/DX+OnlineAnalysis/live-monitoring.md)
- **DX+OfflineAnalysis ([`DX+/DX+OfflineAnalysis/`](DX+/DX+OfflineAnalysis/README.md))**: [Designer & Stream Select](DX+/DX+OfflineAnalysis/designer-and-stream-select.md) · [Record Selection](DX+/DX+OfflineAnalysis/record-selection-and-disambiguation.md) · [Processors & Outputs](DX+/DX+OfflineAnalysis/processors-and-outputs.md) · [`DX+OfflineQueryCli`](DX+/DX+OfflineAnalysis/offline-query-cli.md)
- **DX+RemoteViewer ([`DX+/DX+RemoteViewer/`](DX+/DX+RemoteViewer/README.md))**: [Connecting & Streams (`DXNet-Rx`)](DX+/DX+RemoteViewer/connecting-and-streams.md) · [Workspace](DX+/DX+RemoteViewer/viewer-workspace.md) · [DAQ Control & Limits](DX+/DX+RemoteViewer/daq-control-and-limits.md) · [Live Plots](DX+/DX+RemoteViewer/live-plots.md)
- **DX+DataViewer ([`DX+/DX+DataViewer/`](DX+/DX+DataViewer/README.md))**: [Loading & Playback](DX+/DX+DataViewer/loading-and-playback.md) · [Ribbon & Options](DX+/DX+DataViewer/ribbon-and-options.md) · [Time-Based Plots](DX+/DX+DataViewer/time-based-plots.md) · [Frequency-Based Plots](DX+/DX+DataViewer/frequency-based-plots.md)
- **Tools**: [DX+ DB Manager (`dx+dbmanager.exe`)](DX+/Tools/DB%20Manager/README.md)
- **Services**: [DXNet Bridge (OPC UA)](DX+/Services/DXNet%20Bridge%20%28OPCUA%29/README.md) · [DXNet Bridge (PLC)](DX+/Services/DXNet%20Bridge%20%28PLC%29/README.md)
- **Release & Legal**: [Release Notes](DX+/release-notes/README.md) · [Legal & SLA](DX+/legal/README.md)

---

## 5. Custom Development — Developer APIs & SDKs

Developer-facing API references, data models, network protocols, plugin SDKs, and **ApexLM / FlexNet** licensing specifications for building custom applications on **DS-API** and **Phoenix API** *(Phoenix API maintained via the `phoenix-doc` Git submodule)*.

- **Primary Links**: **[Custom Development Quick Start Guide](Custom%20Development/quick-start.md)** · **[Custom Development Master Documentation](Custom%20Development/README.md)**

### SDKs & Languages

- **DS-API ([`Custom Development/DS-API/`](Custom%20Development/DS-API/README.md))**
  - [Capabilities, Formats & Developer Licensing](Custom%20Development/DS-API/README.md)
  - [C / C++ SDK](Custom%20Development/DS-API/C++/README.md): [Data Types](Custom%20Development/DS-API/C++/data-types.md) · [File I/O](Custom%20Development/DS-API/C++/file-io.md) · [Streaming Client](Custom%20Development/DS-API/C++/streaming-client.md) · [System Manager & Clusters](Custom%20Development/DS-API/C++/system-manager-and-clusters.md) · [Driver Plugins & Parameter Server](Custom%20Development/DS-API/C++/driver-plugins-and-param-server.md)
  - [MATLAB (64-bit)](Custom%20Development/DS-API/MatLab/README.md): [File Reader](Custom%20Development/DS-API/MatLab/file-reader.md) · [Network Streaming & Manager](Custom%20Development/DS-API/MatLab/network-streaming-and-manager.md)
  - [Python (`dsapi.py`)](Custom%20Development/DS-API/Python/README.md): [Setup & TDF Utilities](Custom%20Development/DS-API/Python/setup-and-configuration.md) · [File & Network API](Custom%20Development/DS-API/Python/file-and-network-api.md)
- **Phoenix API ([`Custom Development/Phoenix API/`](Custom%20Development/Phoenix%20API/README.md))**
  - [Architecture & Developer Portal](Custom%20Development/Phoenix%20API/README.md)
  - [C++20 SDK](Custom%20Development/Phoenix%20API/C++/README.md): [Licensing (`PhoenixLic` / `ApexLmClient`)](Custom%20Development/Phoenix%20API/C++/licensing.md) · [Pipelines & Components](Custom%20Development/Phoenix%20API/C++/pipeline-and-components.md) · [Devices, Streams & I/O](Custom%20Development/Phoenix%20API/C++/devices-streams-and-io.md) · [Data Types & Utilities](Custom%20Development/Phoenix%20API/C++/data-types-and-utilities.md) · [Custom Plugins](Custom%20Development/Phoenix%20API/C++/custom-plugins.md)
  - [Python (`phoenixpy`)](Custom%20Development/Phoenix%20API/Python/README.md): [Licensing](Custom%20Development/Phoenix%20API/Python/licensing.md) · [Pipelines & Graphs](Custom%20Development/Phoenix%20API/Python/pipelines-and-graphs.md) · [Data I/O & Databases](Custom%20Development/Phoenix%20API/Python/data-io-and-databases.md) · [Module Reference](Custom%20Development/Phoenix%20API/Python/module-reference.md)
  - [PhoenixCore](Custom%20Development/Phoenix%20API/PhoenixCore/PhoenixCore.md) · [Component Catalog](Custom%20Development/Phoenix%20API/Components/Inputs/README.md) · [Phoenix Apps](Custom%20Development/Phoenix%20API/Apps/README.md)
