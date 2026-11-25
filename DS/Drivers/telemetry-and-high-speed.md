# Telemetry & High-Speed Acquisition Drivers

These drivers integrate slip-ring/rotor telemetry, distributed Ethernet/PTP test-cell chassis, real-time data streaming suites, and portable high-speed recorders into **APEX DS**.

---

## Astech DSR Telemetry (`astechdsr`)

- **License Class:** `ASTECH_CHANNELS` (`ANY_CHANNELS` fallback)
- **Architecture:** Connects to a **Linux RS-422 serial-to-TCP proxy** bridging rotor telemetry frames from Astech DSR receivers into Windows or Linux DS servers.
- **Channels & Parameters:** Exposes **`5` base channels** per unit (`4` primary telemetry channels per RS-422 port plus `1` auxiliary channel) alongside extracted telemetry parameters.
- **Sample Rate:** Fixed **`100 kHz`** hardware stream with selectable **`/2^N` integer decimation**.
- **Driver Options:** Supports `datadir=` and `datasave=` options for raw frame capture and offline file replay.

---

## Datatel Telemetry (`datatel`, `datatel++`)

- **License Class:** `DATATEL_CHANNELS` (`ANY_CHANNELS` fallback)
- **OS Support:** Windows 64-bit and Linux 64-bit.
- **Hardware & Protocol:** Interfaces over Ethernet LAN with **Datatel `dt8060`** (WebGUI control via **HTTP port `80`**) and **`dt6090`** Digital Output (DO) receivers.
- **Capabilities:**
  - Up to **`32` dynamic channels** plus **`82` low-speed telemetry parameters**
  - Selectable hardware decimation (`decimate=1..16`)
  - Rack selection (`rack=`) and **IRIG** timing support (`irig`)
  - Supports offline playback of saved telemetry captures via `datadir=`

---

## HGL Dynamics (`hgl`)

- **License Class:** `HGL_CHANNELS` (`ANY_CHANNELS` fallback)
- **OS Support:** Windows 64-bit and Linux 64-bit.
- **Hardware:** HGL **Dragonfly V2–V5B** and **Hummingbird** Ethernet dynamic systems (`FE-1410-DYN`, `FE-1408-DFY+PSU`, `FE-1408-DFY+PSU-B`, `FE-1418-DFY+PSU`), registered as combo acquisition hardware (`PLUGINDEV_TYPE_COMBO`).
- **Network Protocol Ports:**
  - UDP device discovery: port **`19999`**
  - TCP control/command: port **`30000`** *(driver configuration option defaults to `14002` when overriding)*
  - Data stream: port **`11770`**
- **Rates & Sync:** Supports **16-bit** and **24-bit** payloads (both big-endian and little-endian), per-module power-of-two sample rate scaling (**`1/16x` through `16x`** relative to chassis base clock), and **`1` synchronization parameter**.

---

## IMC Cronos (`imcdevice`)

- **License Class:** `IMC_CHANNELS` (`ANY_CHANNELS` fallback)
- **OS Support:** Windows 64-bit and Linux 64-bit.
- **Transport:** Connects over TCP/IP (`device=<HOST>:<PORT>`) to an **IMC Studio Data Streaming** forwarder pushing live IMC Cronos measurements.
- **Multi-Rate Handling:** Automatically imports IMC channel setup metadata:
  - Channels sampled at **`>= 1/16`** of the chassis maximum rate are interpolated automatically to match the DS primary sample rate as dynamic channels.
  - Slower channels are mapped automatically as **1-per-block low-speed DS parameters**.
- **Capture/Replay:** Supports `datafile=` option for saving and replaying raw IMC stream captures.

---

## MeCalc Quantus (`mecalc`)

- **License Class:** `MECALC_CHANNELS` (`ANY_CHANNELS` fallback)
- **OS Support:** Windows 64-bit and Linux 64-bit.
- **Transport & Sync:** Discovers and controls MeCalc Quantus chassis via **QServer HTTP REST API (`port 8080`)** and high-speed sample streams, synchronized across modules via **IEEE 1588 PTP**.
- **Supported Modules:**

| Module | Channels | Max Sample Rate | Measurement Type |
| :--- | :---: | :---: | :--- |
| **`ICS42`** | 6 | `102.4 kHz` | Simultaneous analog voltage/IEPE |
| **`ICP42S`** | 4 | `204.8 kHz` | High-speed dynamic IEPE/voltage |
| **`ICT42S`** | 2 + 2 tach | `204.8 kHz` | Dynamic inputs + dual tachometer inputs |
| **`WSB42X`** | 4 | `204.8 kHz` | Wheatstone bridge / strain inputs |

- **Options:** Supports `autozero=off|open*|start*` zero-calibration control policies.

---

## Pacific Instruments `PI7000` (`pi7000`)

- **License Class:** `PACIFIC_CHANNELS` (`ANY_CHANNELS` fallback)
- **OS Support:** Windows 64-bit and Linux 64-bit.
- **Supported Card Targets:** `pi7218`, `pi7318`, `pi7418`, `pi7220`, `pi7320`, `pi7420`.
- **Specifications:**
  - Ethernet IP networked chassis (`4` channels per plug-in card)
  - Analog voltage, IEPE, and bridge transducer conditioning
  - Integrated **IRIG A / B / G** timecode synchronization
  - Maximum sample rates: **`25.6 kHz`** (`72xx`), **`102.4 kHz`** (`73xx`), **`204.8 kHz`** (`74xx`) depending on installed card family

---

## TEAC `WX-7000` (`wx7000`) — *Windows Only*

- **License Class:** `TEAC_CHANNELS` (`ANY_CHANNELS` fallback)
- **OS Support:** **Windows only** (`drv-wx7000.dll` links against TEAC `Wx00.dll` / `Wx00.lib`; *note: older vendor SDK distributions documented 32-bit DLL constraints, whereas current DS Windows builds compile against 64-bit `mingw64/Wx00.lib`*).
- **Capabilities:**
  - Ethernet LAN connection to TEAC **WX-7000** chassis (up to **`128` channels** across `8` expansion modules)
  - Sample rates: **`1 kHz` to `204.8 kHz`**
  - Programmable **`24 V` / `28 V` IEPE** sensor compliance
  - **Network Throughput Ceiling:** Sustains approximately **`1.6 MB/s`** aggregate LAN streaming throughput; balance active channel count and sample rate accordingly during continuous acquisition.

See also: [Driver Matrix Overview](README.md) · [Architecture & Licensing](architecture-and-licensing.md)
