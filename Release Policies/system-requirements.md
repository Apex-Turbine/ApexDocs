# System Requirements, CPU Architectures & OS Support

Before installing **APEX** desktop suites, data acquisition servers, finite-element tools, developer SDKs, or **APEX License Manager (`ApexLM`)**, verify that target hardware and operating systems meet the requirements below.

---

## 1. CPU Architecture & Mandatory `AVX2` Instruction Set

- **64-Bit `x86-64` Architecture Only**: All current **APEX** applications, processing pipelines, acquisition daemons, and SDK binaries require a **64-bit `x86-64` (`AMD64` / Intel 64)** processor.
  - Native 32-bit operating systems (`x86`) and non-`x86-64` processors (including ARM64 CPUs lacking hardware `AVX2`) are **not supported**.
  - *(Note: On 64-bit **APEX DS** acquisition workstations using legacy 32-bit hardware vendor DLLs, 64-bit DS communicates out-of-process with helper `ProxyDev` servers rather than running the main suite in 32-bit mode.)*
- **Mandatory `AVX2` (Advanced Vector Extensions 2) & FMA3**:
  - Modern **APEX** signal processing, FFT/order-domain resampling, vectorized math, 32,768-bin waveform envelope decimation, and GageMap FEA solver kernels are compiled for **`AVX2`** execution.
  - Compatible processors include **Intel 4th Generation Core (Haswell) / Xeon E5 v3 (2016+ recommended)** or newer, and **AMD Ryzen / Threadripper / EPYC (Zen architecture)** or newer.
  - Executing APEX software on CPUs lacking `AVX2` — or inside virtual machines (VMware, Hyper-V, KVM/QEMU) whose vCPU profile masks `AVX2` flags — is unsupported and causes application termination (`STATUS_ILLEGAL_INSTRUCTION` / `SIGILL`).
- **Graphics Requirement (OpenGL)**: Interactive visualization applications (`DX+`, `GMx`, `GM`, `SDRFM`, `SdrConverter`, `DX`) require a hardware-accelerated OpenGL-capable GPU (discrete **NVIDIA** / **AMD** workstation graphics strongly recommended for 3D FE models and 60 Hz spectral waterfalls). Virtualized remote desktop sessions must pass through hardware OpenGL acceleration.

### Verifying `AVX2` Support Before Deployment

=== "Windows (PowerShell)"

    ```powershell
    # Check CPU model and confirm .NET/OS reports hardware AVX2 support
    Get-CimInstance Win32_Processor | Select-Object Name, NumberOfCores, NumberOfLogicalProcessors, AddressWidth
    [System.Runtime.Intrinsics.X86.Avx2]::IsSupported
    ```
    *`[System.Runtime.Intrinsics.X86.Avx2]::IsSupported` must evaluate to **`True`**.*

=== "Linux (Bash)"

    ```bash
    uname -m                           # Must print: x86_64
    grep -o -m 1 '\bavx2\b' /proc/cpuinfo || echo "AVX2 NOT SUPPORTED"
    ```

> [!TIP]
> **Virtual Machine Deployment**: In VMware ESXi, KVM/QEMU, or Proxmox environments, configure the virtual CPU type to **`host-passthrough`** (or enable `EVC Mode: Haswell` or newer) so the guest OS exposes native `AVX2` instructions.

---

## 2. Workload-Based Hardware & RAM Recommendations

Select hardware matching your highest-demand operational tier:

| Workload Tier | Representative Applications | CPU Recommendation (`x86-64` + `AVX2`) | RAM Minimum / Recommended | Storage & Graphics |
| :--- | :--- | :--- | :--- | :--- |
| **1. License Server & Remote Viewer** | `ApexLM_Server_Service`, `APEX DR`, `DX+ Remote Viewer` | **4+ cores** (`>= 2.5 GHz`) | **4 GB min** / **8–16 GB recommended** | `120+ GB` SSD · `1280 x 1024` min (`1920 x 1080` recommended) |
| **2. Standard Acquisition, Analysis & Bridges** | `APEX DX`, `DX+ DAQ` (`<= 32` ch), `DX+ Online/Offline Analysis`, `DX+ Data Viewer`, `DB Manager`, `DXNet Bridges` | **6–8+ cores** (`>= 3.0 GHz`) | **8 GB min** / **16–32 GB recommended** | `500 GB–1 TB` NVMe SSD · Hardware OpenGL (`1920 x 1080`+) |
| **3. High-Channel-Count DAQ & Live DSP** | `APEX DS`, `DX+ DAQ`, `DX+ Online Analysis` (`64–256+` channels @ `100–200+ kHz`, live FFT/Order/Campbell, DB recording) | **12–24+ high-clock cores** (`>= 3.5 GHz` sustained) | **32–64+ GB multi-channel DDR4/DDR5** *(budget `>= 1–2 GB` per 16 ch @ 200 kHz + ring buffers)* | Dedicated high-endurance NVMe SSD / RAID sustaining **`>= 3x` aggregate write bandwidth** (`>= 500 MB/s`–`2+ GB/s`) · Discrete GPU |
| **4. Large FEA Optimization & Fatigue (`GageMap`)** | `GMx`, `GM`, `SDR Converter`, `SDRFM`, `GmScript` (ANSYS `.rst` / ABAQUS `.odb` / NASTRAN `.op2` conversion & optimization) | **8–32+ cores** (`>= 3.0 GHz`) | **32 GB min** / **64–128+ GB recommended** for large multi-million-DOF cyclic/modal `.sdr` models | `1–4 TB` fast NVMe scratch SSD · Discrete OpenGL GPU (`8+ GB` VRAM) |

### Storage Bandwidth Rule of Thumb for Live Acquisition

Always size sustained sequential disk write throughput at **at least `3x`** your aggregate peak telemetry rate to absorb OS filesystem flushes and SQLite/RWX chunk commits without FIFO overruns. For example, `32` simultaneous channels at `200 kHz` (`~13 MB/s` raw + peak) require **`>= 39 MB/s`** sustained sequential write bandwidth; `256` channels require **`>= 315+ MB/s`**, making NVMe SSDs mandatory for modern high-channel-count rigs.

---

## 3. Operating System Support Policy

### Windows is the Primary Supported Operating System

**Microsoft Windows (64-bit)** is **APEX's** primary supported and full-QA operating system across the entire software portfolio:

- **Desktop Workstations**: **Windows 11 (64-bit)** and **Windows 10 (64-bit, supported LTSC / current servicing channels)**.
- **License Server & Headless Hosts**: **Windows Server 2022 (64-bit)**, **Windows Server 2019 (64-bit)**, Windows 11, or Windows 10.
- Unsupported / Legacy Windows versions (Windows 7, 8/8.1, Vista, XP) have reached Microsoft end-of-life and are **not supported** on current **APEX** releases.

### Linux Support Scope (Selected Applications & Services)

Selected **APEX** products, acquisition daemons, licensing services, FE converters, and developer SDKs provide native **64-bit Linux** builds alongside Windows. Unless explicitly listed as Linux-supported below, assume **Windows 64-bit** is required.

| Product Suite / Component | Windows 10/11 (64-bit) | 64-bit Linux Support | Platform Notes & Constraints |
| :--- | :--- | :--- | :--- |
| **APEX License Manager (`ApexLM`)**<br>(`ApexLM_Service`, `ApexLM_Tray`, `ApexLM_CLI`, `ApexLM_Server_Service`, `ApexLM_Server_CLI`) | **Primary (Full Support)**<br>+ Windows Server 2019/2022 | **Supported** (`systemd` services & CLI/Tray) | Hardened auto-generated `systemd` units (`apexlm.service`, `apexlm-server.service`); SQLite state in `/var/lib/apexlm*`. |
| **APEX DS Suite**<br>(`DS`, `DR`, `DM`, `DO`, `Drivers`) | **Primary (Full Support)** | **Supported** (selected distros/drivers) | On Linux, device driver kernel modules (typically `/opt/apex/ds/modules`) must match LTS kernels and be recompiled after kernel upgrades; verify specific hardware driver availability. |
| **APEX DX** | **Primary (Full Support)** | **Supported** | Requires X11 / XCB / Fontconfig / FreeType shared libraries on 64-bit `x86-64` hosts; Slackware / RHEL-compatible runtime packaging. |
| **APEX GageMap Suite**<br>(`GM`, `GMx`, `GmScript`, `SDRFM`, `SDR Converter`) | **Primary (Full Support)** | **Supported** | On Linux, `GmScript` and Qt visualization tools require an X11 `DISPLAY` (use `xvfb-run` on headless batch nodes). Solver runtimes (ANSYS / ABAQUS / MATLAB `libmat`) must be on `PATH` / `LD_LIBRARY_PATH`. |
| **APEX DX+ Suite, Tools & Services**<br>(`DX+DAQ`, `OnlineAnalysis`, `OfflineAnalysis`, `RemoteViewer`, `DataViewer`, `DB Manager`, `DXNet OPCUA & PLC`) | **Primary (Full Support)** | **Limited / Headless Core Components** | Desktop Qt 6 suite and `DXNet` bridges target **Windows 10/11 64-bit** as primary platform; cross-platform Phoenix components and CLI/Python utilities run on 64-bit Linux where packaged. |
| **Custom Development SDKs**<br>(`DS-API` & `Phoenix API`) | **Primary (Full Support)** | **Supported** | `DS-API` (`libdsapi.so`, `dsapi.py`, 64-bit MATLAB `mxapi`), `PhoenixCore` C++20, and `phoenixpy` SWIG wheels (`Python >= 3.12`) support 64-bit Linux and Windows 10/11. |

---

## 4. Network & Firewall Prerequisites

Refer to your deployment suite for full port tables:
- **APEX License Manager**: TCP **`27884`** (local loopback), TCP **`27885`** / **`27886`** (`SERVER` incoming from `PASSTHROUGH` hosts), HTTP **`27887`** / **`27888`** (loopback admin UIs only). See [License Manager Ports](../License%20Manager/README.md#network-ports-environment-variables-state-paths).
- **APEX DS / DR / DM**: UDP/TCP **`10995`–`11004`** (discovery & streaming), TCP **`18400`** (`ProxyDev` `daqproxy`).
- **APEX DX+ & Bridges**: TCP **`27026`** / **`27100`–`27176`** (ZeroMQ telemetry & remote management), UDP **`5353`** (`_dxnet._tcp.local` mDNS), TCP **`4840`/`4850`** (`OPC UA`), TCP/UDP **`44818`** (`EtherNet/IP CIP`), TCP **`5432`** (`PostgreSQL`).

See also: [18-Month Release Lifecycle Policy](README.md) · [Software Maintenance & Support](maintenance-and-support.md)
