# VTI Instruments Drivers (`vtex`, `vtitc`)

VTI Instruments drivers support **Windows 64-bit** and **Linux 64-bit** natively over Gigabit Ethernet (LXI / VXI-11 / ONC-RPC) and draw channel counts from **`VTI_CHANNELS`** (with automatic fallback to `ANY_CHANNELS`).

---

## Dynamic & PXIe / Ethernet Hardware (`vtex`)

The **`drv-vtex`** plugin communicates over Gigabit Ethernet with VTI LXI chassis controllers (such as **EMX-2500** PXIe controllers) and standalone **RX Series** instruments.

| Hardware Target | Card / Architecture | Channels | Resolution | Max Sample Rate | Signal Types & Features |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **`vtex-emx4250`** | EMX-4250 (via EMX-2500 LXI PXIe) | 16 per card | 24-bit ADC (`32`-bit output) | `204.8 kHz` | Simultaneous dynamic voltage / IEPE; supports optional **EMX-1434** tachometer card |
| **`vtex-rx0124`** | RX-0124 | 24 | 24-bit | `128 kHz` | Bridge, strain gauge, resistance, and voltage acquisition |
| **`vtex-rx0424`** | RX-0424 | 24 + 2 tach | 24-bit | `204.8 kHz` | Simultaneous dynamic inputs plus 2 integrated tachometer channels |
| **`vtex-ex1403`** | EX1403 | 16 | 24-bit | Per EX1403 LXI spec | LXI Ethernet 16-channel bridge/strain acquisition |

### Multi-Chassis Synchronization
EMX-2500 and RX series instruments support LXI / IEEE 1588 PTP clock synchronization across distributed Ethernet chassis so multi-chassis setups share phase-aligned timestamps.

---

## Thermocouple & Precision Voltage Scanner (`vtitc`)

The **`drv-vtitc`** plugin connects to VTI **EX1048A** and **EX10xxA** Ethernet thermocouple / precision voltage scanners over **VXI-11 / ONC-RPC**.

### Specifications & Transport
- **Channel & Parameter Mapping:**
  - **48** analog voltage / thermocouple measurement channels (`INT16` / `FLOAT32` scaled engineering units)
  - **12** Cold-Junction Compensation (CJC) readings (configurable as channels or DS low-speed parameters)
  - Embedded **IEEE 1588** timecode parameter support
- **Sample Rate:** Standard configuration scan range **`1`–`1000 Hz`** (`vtitc.info` specification; internal driver attribute supports `0.01`–`16000` Hz for custom rate alignment).
- **OS Transport Libraries:**
  - **Windows:** Uses `oncrpc.dll` for VXI-11 RPC communication.
  - **Linux:** Uses system `libtirpc` (`TI-RPC`) for VXI-11 RPC communication.

See also: [Driver Matrix Overview](README.md) · [Architecture & Licensing](architecture-and-licensing.md)
