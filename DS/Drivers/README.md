# Hardware Device Drivers (`DS/Drivers`)

**APEX DS** acquires data through modular dynamically loaded hardware plugins (`drv-*.dll` on Windows, `drv-*.so` on Linux) and optional out-of-process `ProxyDev` device servers (`srv-*`).

## Driver Documentation Index

- [Driver Architecture, `ProxyDev` IPC & Licensing](architecture-and-licensing.md) — `PluginDev` loading, `ProxyDev` local shared-memory / TCP daemons (`18400`), hardware serial checking, and `<VENDOR>_CHANNELS` vs `ANY_CHANNELS` licensing.
- [National Instruments (`nidaq` & Utilities)](national-instruments.md) — Native NI-DAQmx PXI/PXIe/USB/cDAQ drivers, LabVIEW RT proxies (`rni44xx`, `nni*`), NI-SYNC (`ni6674T`), and `nidaqd2a` / `dout` / `pxidump`.
- [VTI Instruments (`vtex`, `vtitc`)](vti-instruments.md) — LXI PXIe (`EMX-4250`), Ethernet RX series (`RX0124`, `RX0424`), `EX1403`, and `EX1048A`/`EX10xxA` thermocouple VXI-11 / ONC-RPC scanners.
- [General Standards & PCI / PCIe / USB (`gsdaq`, `adv17x4`, `ccurdscc`, `lttdevice`, `caddmas`)](general-standards-and-pci.md) — 32/64-bit `ProxyDev` high-speed PMC/PCI/PCIe cards, Linux-only Advantech/Concurrent/Tasler LTT24 drivers, and Caddmas USB hardware.
- [Telemetry & High-Speed Network Systems](telemetry-and-high-speed.md) — Astech DSR, Datatel `dt8060`/`dt6090`, HGL Dragonfly/Hummingbird, IMC Cronos, MeCalc Quantus, Pacific `PI7000`, and TEAC `WX-7000`.
- [Pressure Scanners, Parameter Servers & Auxiliary](pressure-and-auxiliary.md) — PSI `9016`/`9021`, Scanivalve `DSA`/`MPS`, `param`/`paramds` TCP parameter bridges, `datafile`/`datxfile`/`bttfile` file replay, `simul`/`nsimul`, and `sndcard`.

---

## Master Hardware Device Driver Support Matrix

| Driver ID | Vendor / Hardware Family | Bus / Interface | Windows (64-bit) | Linux (64-bit) | Proxy Architecture | Channel / Rate Highlights | ApexLM License Pool |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| **`ni4303`** | NI PXIe-4303 | PXIe | Native | — | In-process `drv-ni4303` | 32 ch, 24-bit, up to `51.2 kHz` | `NI_CHANNELS` |
| **`ni4310`** | NI PXIe-4310 | PXIe | Native | — | In-process `drv-ni4310` | 8 ch, 16-bit, up to `400 kHz` | `NI_CHANNELS` |
| **`ni4331`** | NI PXIe-4331 (Bridge/Strain) | PXIe | Native | Proxy | In-process (`rni44xx` RT proxy option) | 8 ch simultaneous bridge, up to `102.4 kHz` | `NI_CHANNELS` |
| **`ni4353` / `nni4353`** | NI PXIe-4353 (Thermocouple) | PXIe | Native + Proxy | Proxy | In-process / `srv-nni4353` | 32 ch TC (`100 Hz` scan upsampled to `10`–`204.8 kHz`) | `NI_CHANNELS` |
| **`ni4357`** | NI PXIe-4357 (RTD) | PXIe | Native | — | In-process `drv-ni4357` | 20 ch RTD (`100 Hz` scan upsampled to `10`–`204.8 kHz`) | `NI_CHANNELS` |
| **`ni4461` / `ni446x`** (+`v`) | NI PXI/PXIe-4461, 4462, 4464 | PXI / PXIe | Native + Proxy | Proxy (`rni44xx`) | In-process (`rni44xx` RT proxy option) | 2 ch (`4461`) / 4 ch (`446x`), up to `204.8 kHz`, IEPE | `NI_CHANNELS` |
| **`ni4472` / `ni4474`** (+`v`) | NI PXI-4472 / 4474 | PXI | Native | — | In-process | 8 ch (`4472`) / 4 ch (`4474`), up to `102.4 kHz`, IEPE | `NI_CHANNELS` |
| **`ni4492` / `ni449x`** (+`v`, `nni449x`) | NI PXIe-4492, 4495–4499 | PXIe | Native + Proxy | Proxy | In-process / `srv-nni449x` / `rni44xx` | 8 ch (`4492`) / 16 ch (`449x`), up to `204.8 kHz`, IEPE | `NI_CHANNELS` |
| **`ni6001`** | NI USB-6001 | USB | Native | — | In-process `drv-ni6001` | 8 ch, `100 Hz`–`20 kHz` | `NI_CHANNELS` |
| **`ni6124` / `nni6124`** | NI PXIe-6124 | PXIe | Native + Proxy | Proxy | In-process / `srv-nni6124` | 4 ch simultaneous, up to `4 MHz` | `NI_CHANNELS` |
| **`ni6341` / `ni6363`** | NI X-Series 6341, 6363 | PXIe / PCIe | Native | — | In-process | Mux `16 SE`/`8 DIFF` (`500 kHz` agg) or `32 SE`/`16 DIFF` (`2 MHz` agg) | `NI_CHANNELS` |
| **`ni63x8`** | NI PXIe-6358, 6368 | PXIe | Native | — | In-process `drv-ni63x8` | 16 ch simultaneous, `1.25 MHz` / `2 MHz` | `NI_CHANNELS` |
| **`ni9201`, `9208`, `9209`, `9232`, `9234`, `9402`** | NI CompactDAQ Modules | cDAQ Chassis | Native | — | In-process | `500 S/s`–`500 kS/s` voltage, 20 mA, IEPE, and TTL DIO | `NI_CHANNELS` |
| **`rni44xx`** | NI LabVIEW RT PXI Target | Ethernet (`RTserver.dll`) | Proxy | Proxy | `srv-rni44xx` -> LabVIEW RT | Remote RT streaming for `nni449x`, `nni446x`, `nni4331` | `NI_CHANNELS` |
| **`vtex`** | VTI EMX-4250, RX0124, RX0424, EX1403 | LXI GbE / PXIe | Native | Native | In-process `drv-vtex` | 16–24 ch (+2 tach on RX0424), up to `128`–`204.8 kHz` | `VTI_CHANNELS` |
| **`vtitc`** | VTI EX1048A / EX10xxA | Ethernet VXI-11 / ONC-RPC | Native (`oncrpc.dll`) | Native (`libtirpc`) | In-process `drv-vtitc` | 48 V/TC ch + 12 CJC ch/params, IEEE 1588, `1`–`1000 Hz` (`0.01`–`16000` attr) | `VTI_CHANNELS` |
| **`gsdaq`** | General Standards (`pmc64ss`, `pci16sdi`, `pci16sdihs`, `pmc24dsi`, `pci24dsi`, `pcie24dsi`, `pmc16ssai`) | PMC / PCI / PCIe | 64-bit plugin -> 32-bit `srv-*` | 64-bit kernel module -> `srv-*` | `ProxyDev` (`bin32/srv-*.exe` on Win) | 8–64 ch, 16/24-bit, `100 Hz` up to `1.1 MHz` | `GS_CHANNELS` |
| **`adv17x4`** | Advantech `PCI-1714U`/`UL`, `PCIe-1744E` | PCI / PCIe | — | Native (`/dev/pci1714*`) | In-process `drv-adv17x4` | 4 ch, 12-bit (`->16b`), `10 MHz` / `30 MHz` | `ADVTECH_CHANNELS` |
| **`ccurdscc`** | Concurrent DSCC rev1 (`5 V`) / rev2 (`10 V`) | PCIe | — | Native (RedHawk/kdrv) | In-process `drv-ccurdscc` | 32 ch simultaneous 24-bit sigma-delta, `2`–`216 kHz` | `CC_CHANNELS` |
| **`lttdevice`** | Tasler LTT24 Combo | USB | — | Native (`libltt2api30.so`) | In-process `drv-lttdevice` | 8/16 ch, `10 Hz`–`20.48 MHz` | `LTT_CHANNELS` |
| **`caddmas`** | Caddmas `3x8` (USB1) & `8x4` (USB2) | USB (`libusb-1.0` / WinUSB) | Native (Zadig WinUSB) | Native (`libusb`) | In-process `drv-caddmas3x8` / `8x4` | `24 ch` up to `216 kHz` (`3x8`); `32 ch` up to `100 kHz` (`8x4`) | `CADDMAS_CHANNELS` |
| **`astechdsr`** | Astech DSR Telemetry | RS-422 Serial (Linux TCP proxy) | Proxy client | Native / Proxy | Serial TCP proxy | 4 ch/port + aux/params (`5` base ch), `100 kHz / 2^N` | `ASTECH_CHANNELS` |
| **`datatel`** | Datatel `dt8060` WebGUI & `dt6090` DO | Ethernet HTTP (`80`) + LAN | Native | Native | In-process (`drv-datatel`, `datatel++`) | 32 ch, 82 params, `decimate=1..16`, IRIG | `DATATEL_CHANNELS` |
| **`hgl`** | HGL Dragonfly V2–V5B & Hummingbird | Ethernet UDP/TCP (`19999`/`30000`/`11770`) | Native | Native | In-process `drv-hgl` | Multi-chassis `16`/`24`-bit, `2^N` rates, 1 sync param | `HGL_CHANNELS` |
| **`imcdevice`** | IMC Cronos (via IMC Studio Data Streaming) | Ethernet (`HOST:PORT`) | Native | Native | Connects to IMC forwarder | Auto-interpolated multi-rate ch + params | `IMC_CHANNELS` |
| **`mecalc`** | MeCalc Quantus (`ICS42`, `ICP42S`, `ICT42S`, `WSB42X`) | Ethernet QServer HTTP (`8080`) + PTP | Native | Native | In-process `drv-mecalc` | 2–6 ch/module, `102.4`–`204.8 kHz`, tach & bridge | `MECALC_CHANNELS` |
| **`pi7000`** | Pacific Instruments `7218`/`7318`/`7418`/`7220`/`7320`/`7420` | Ethernet IP | Native | Native | In-process `drv-pi7000` | 4 ch/card, voltage/IEPE/bridge, IRIG, `25.6`–`204.8 kHz` | `PACIFIC_CHANNELS` |
| **`wx7000`** | TEAC WX-7000 (`Wx00.dll`) | Ethernet LAN | Native | — | In-process `drv-wx7000` | Up to 128 ch, `1`–`204.8 kHz` (~`1.6 MB/s` LAN limit) | `TEAC_CHANNELS` |
| **`psi9016`** | PSI 9016 / 9021 Pressure Scanner | Ethernet Optomux (`9000`) | Native | Native | In-process `drv-psi9016` | Parameter-only (`0` ch, `16` params/unit, `100 ms` default) | `PSI_CHANNELS` |
| **`scani`** | Scanivalve `DSA32xx`, `DSA5000`, `MPS42xx` | Ethernet Telnet (`23`) + Binary (`503`) | Native | Native | In-process `drv-scani*` | 16 ch (`DSA`, `250`/`5000 Hz`) or 64 ch + temps (`MPS`, `1000 Hz`) | `SCANI_CHANNELS` |
| **`param` / `paramds`** | External / DS-to-DS Parameter Feeds | TCP (`6600` or DS protocol) | Native | Native | In-process `drv-param*` | Parameter-only (`0` ch, `10` default params, `map=`) | `OTHER_CHANNELS` |
| **`datafile` / `bttfile`** | Replay (`apexfile`, `datxfile`, `bttfile` CDT) | Local Files (`.rwx`/`.raw`/`.datx`/`.cdt`) | Native | Native | In-process replay | Offline hardware simulation from recorded files | `OTHER_CHANNELS` / `BTT_CHANNELS` |
| **`simul` / `nsimul`** | Built-in Swept-Sine & UI Mimic Simulator | Virtual | Native | Native + Proxy | In-process / `srv-nsimul` | 32 ch, 4 params, `I16`/`I32`/`F32`, `8`–`24` bits | **Waived** *(eval)* |
| **`sndcard`** | PC Audio Input (Windows / Linux ALSA) | System Audio (`asound`) | Native | Native | In-process `drv-sndcard` | 1–2 ch, 16-bit AC-coupled, `8000`–`44100 Hz` | `OTHER_CHANNELS` |

> [!NOTE]
> All vendor channel drivers fall back automatically to **`ANY_CHANNELS`** in ApexLM (or `APEXDS_CHANNELS_ANY` in legacy FlexNet) when the corresponding vendor pool (`<VENDOR>_CHANNELS`) does not contain enough available seats.

See also: [APEX DS Suite Overview](../README.md) · [APEX Data Output (`DO`)](../DO/README.md) · [APEX DS Licensing](../DS/installation/licensing.md)
