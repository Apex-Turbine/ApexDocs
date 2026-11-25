# National Instruments Drivers (`nidaq` & Utilities)

The **`nidaq`** driver family connects **APEX DS** to National Instruments PXI, PXIe, PCIe, CompactDAQ (cDAQ), and USB hardware using NI-DAQmx (`>= 9.6`), NI-SYNC (`>= 3.3.5`), and optional LabVIEW RT / `ProxyDev` remote servers. All NI drivers map to the **`NI_CHANNELS`** ApexLM pool (with automatic fallback to `ANY_CHANNELS`).

---

## PXIe, PXI, PCIe, and USB Acquisition Plugins

| Driver ID | Card Models | Channels | Resolution | Max Sample Rate | Conditioning / Notes |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **`ni4303`** | NI PXIe-4303 | 32 | 24-bit | `51.2 kHz` | Simultaneous differential voltage inputs |
| **`ni4310`** | NI PXIe-4310 | 8 | 16-bit | `400 kHz` | High-voltage / isolated analog inputs |
| **`ni4331`** | NI PXIe-4331 | 8 | 24-bit | `100`–`102.4 kHz` | Simultaneous bridge/strain gauge inputs with excitation |
| **`ni4353`** | NI PXIe-4353 | 32 | 24-bit | `100 Hz` scan (upsampled `10`–`204.8 kHz`) | Thermocouple input with CJC; upsamples slow scan to match dynamic DS rate |
| **`ni4357`** | NI PXIe-4357 | 20 | 24-bit | `100 Hz` scan (upsampled `10`–`204.8 kHz`) | RTD resistance temperature detector module |
| **`ni4461` / `ni4461v`** | NI PXI/PXIe-4461 | 2 | 24-bit | `204.8 kHz` | Dynamic signal analyzer; `v` suffix enables voltage-only defaults without IEPE current |
| **`ni446x` / `ni446xv`** | NI PXI-4462, PXIe-4464 | 4 | 24-bit | `204.8 kHz` | Simultaneous IEPE/SE/DIFF dynamic inputs |
| **`ni4472` / `ni4472v`** | NI PXI-4472 | 8 | 24-bit | `102.4 kHz` | Legacy PXI dynamic signal acquisition with IEPE |
| **`ni4474` / `ni4474v`** | NI PXI-4474 | 4 | 24-bit | `102.4 kHz` | Legacy 4-channel PXI dynamic signal module |
| **`ni4492` / `ni4492v`** | NI PXIe-4492 | 8 | 24-bit | `204.8 kHz` | High-density PXIe IEPE dynamic inputs |
| **`ni449x` / `ni449xv`** | NI PXIe-4495, 4496, 4497, 4498, 4499 | 16 | 24-bit | `204.8 kHz` | High-density PXIe IEPE (`449x` selects IEPE options; `v` variant voltage mode) |
| **`ni6001`** | NI USB-6001 | 8 | 14-bit | `100 Hz`–`20 kHz` | Low-cost USB multifunction DAQ |
| **`ni6124`** | NI PXIe-6124 | 4 | 16-bit | `4 MHz` | Simultaneous high-speed analog input; also supported in `DO` for D2A output |
| **`ni6341`** | NI PCIe/PXIe-6341 | `16 SE` / `8 DIFF` | 16-bit | `500 kHz` aggregate | X-Series multiplexed analog input |
| **`ni6363`** | NI PCIe/PXIe-6363 | `32 SE` / `16 DIFF` | 16-bit | `2 MHz` aggregate | X-Series high-channel multiplexed analog input |
| **`ni63x8`** | NI PXIe-6358, PXIe-6368 | 16 | 16-bit | `1.25 MHz` (`6358`) / `2 MHz` (`6368`) | X-Series simultaneous high-speed inputs |

---

## CompactDAQ (cDAQ) Modules

| Driver ID | Module | Channels | Input Type | Max Sample Rate |
| :--- | :--- | :---: | :--- | :--- |
| **`ni9201`** | NI 9201 | 8 | `±10 V` single-ended analog | `500 kS/s` |
| **`ni9208`** | NI 9208 | 16 | `±20 mA` current loop | `500 S/s` |
| **`ni9209`** | NI 9209 | `16 DIFF` / `32 SE` | Analog voltage (supports channel or parameter output mode) | `500 S/s` |
| **`ni9232`** | NI 9232 | 3 | `±30 V` IEPE/voltage dynamic input | `102.4 kS/s` |
| **`ni9234`** | NI 9234 | 4 | `±5 V` IEPE sound & vibration | `51.2 kS/s` |
| **`ni9402`** | NI 9402 | 4 | High-speed bidirectional TTL DIO (configured as tach/digital input) | Up to `500 kHz` |

---

## Proxy & LabVIEW RT Drivers (`nni*`, `rni44xx`)

To connect Windows or Linux **APEX DS** servers to remote NI chassis or LabVIEW Real-Time PXI controllers:

- **Native `ProxyDev` Servers (`nni4353`, `nni449x`, `nni6124`):** Pair standard client plugins (`drv-nni4353`, `drv-nni449x`, `drv-nni6124`) with matching remote proxy servers (`srv-nni4353`, `srv-nni449x`, `srv-nni6124`) via `ProxyDev` / `daqproxy` (`TCP 18400`).
- **LabVIEW RT Target Proxy (`rni44xx` / `srv-rni44xx`):** Communicates via `RTserver.dll` with LabVIEW Real-Time PXI controllers running `nni449x`, `nni449xv`, `nni446x`, `nni446xv`, or `nni4331`. Allows Linux and Windows DS servers to control NI PXIe systems without local NI-DAQmx installation.

---

## Synchronization (`NI-SYNC` & `ni6674T`)

Multi-card and multi-chassis setups coordinate sample clocks, start triggers, and IRIG/GPS/PTP timestamps through **NI-SYNC (`>= 3.3.5`)**:
- Supports **NI PXIe-6674T** timing & synchronization modules.
- Device options support `sync` timing-source selection and `drop=` trigger/sample alignment controls to phase-lock acquisition across PXIe slots and external clusters.

---

## Companion NI Tools & Analog Output (`nidaqd2a`, `dout`, `pxidump`)

- **`nidaqd2a`:** Windows NI-DAQmx digital-to-analog output module powering **[APEX Data Output (`DO`)](../DO/README.md)** across `NI PXIe-4322`, `NI PXIe-6738`, `NI PXIe-6124`, and `NI PXI-4462`. Automatically switches from `float64` voltage writes (`<= 205 kHz`) to calibrated 16-bit raw non-regenerating DMA streaming (`> 205 kHz`).
- **`dout`:** Command-line analog signal output diagnostic utility built on the NI D2A layer.
- **`pxidump`:** Diagnostic enumeration utility inspecting NI PXI/PXIe chassis slots, card identifiers, serial numbers, and DAQmx routes on Windows hosts.

See also: [Driver Matrix Overview](README.md) · [Architecture & Licensing](architecture-and-licensing.md)
