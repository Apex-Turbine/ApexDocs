# General Standards & PCI / PCIe / USB Drivers

This group covers high-density General Standards (`gsdaq`) PMC/PCI/PCIe boards as well as Linux-native Advantech PCI/PCIe (`adv17x4`), Concurrent DSCC (`ccurdscc`), Tasler USB (`lttdevice`), and cross-platform Caddmas USB (`caddmas`) devices.

---

## General Standards (`gsdaq` ProxyDev Family)

General Standards cards map to **`GS_CHANNELS`** (with fallback to `ANY_CHANNELS`). Because General Standards' legacy Windows drivers are **32-bit**, `gsdaq` runs every hardware session through **`ProxyDev`** (`srv-<card>`):
- **Windows (64-bit DS):** 64-bit `drv-<card>.dll` launches `bin32/srv-<card>.exe` in local transient mode (`-t <port>`) using vendor MSI-installed 32-bit kernel drivers.
- **Linux (64-bit DS):** 64-bit `drv-<card>.so` communicates with 64-bit `srv-<card>` backed by the Linux GS kernel module.

| Driver ID | Board Model | Form Factor | Channels | Resolution (HW -> DS) | Sample Rate Range |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **`pmc64ss`** | PMC-64SS / PMC66-64SS | PMC | 64 simultaneous | 16-bit -> 16-bit | `100 Hz`–`200 kHz` |
| **`pci16sdi`** | PCI-16SDI | PCI | 16 | 16-bit -> 16-bit | `5 kHz`–`220 kHz` |
| **`pci16sdihs`** | PCI-16SDIHS | PCI | 8 | 16-bit -> 16-bit | `25 kHz`–`1.1 MHz` |
| **`pmc24dsi`** | PMC-24DSI | PMC | 12 | 24-bit -> 16-bit | `2 kHz`–`200 kHz` |
| **`pci24dsi`** | PCI-24DSI | PCI | 32 | 24-bit -> 16-bit | `2 kHz`–`200 kHz` |
| **`pcie24dsi`** | PCIe-24DSI | PCIe | 32 | 24-bit -> 16-bit | `2 kHz`–`200 kHz` |
| **`pmc16ssai`** | PMC-16SSAI | PMC (Windows build) | 16 | 16-bit -> 16-bit | `5 kHz`–`1 MHz` |

---

## Advantech High-Speed PCI / PCIe (`adv17x4`) — *Linux 64-bit Only*

- **License Class:** `ADVTECH_CHANNELS` (`ANY_CHANNELS` fallback)
- **OS Support:** **Linux 64-bit only** via vendor character device nodes `/dev/pci1714u0`, `/dev/pci1714ul0`, and `/dev/pci1744e0`.
- **Supported Cards:**
  - **`PCI-1714UL`:** 4 channels, 12-bit ADC (packed to 16-bit output), max **`10 MHz`**.
  - **`PCI-1714U` & `PCIe-1744E`:** 4 channels, 12-bit ADC (packed to 16-bit output), max **`30 MHz`**.
- **Clocking:** Supports integer clock division up to **`128`** from the card's base sample clock (select rates that divide cleanly into `10 MHz` or `30 MHz`).

---

## Concurrent Real-Time DSCC (`ccurdscc`) — *Linux 64-bit Only*

- **License Class:** `CC_CHANNELS` (`ANY_CHANNELS` fallback)
- **OS Support:** **Linux 64-bit only** (RedHawk / Linux kernel driver).
- **Hardware:** Concurrent Computer DSCC PCIe boards:
  - **Rev 1:** `5 V` full-scale input range
  - **Rev 2:** `10 V` full-scale input range
- **Specifications:** **32 simultaneous** 24-bit sigma-delta channels spanning **`2 kHz` to `216 kHz`**.

---

## Tasler LTT24 (`lttdevice`) — *Linux 64-bit Only*

- **License Class:** `LTT_CHANNELS` (`ANY_CHANNELS` fallback)
- **OS Support:** **Linux 64-bit only**, linking vendor libraries `libltt2api30.so` and `liblttosal30.so`.
- **Hardware:** Tasler **LTT24** USB high-speed combo acquisition units supporting **`8` or `16` channels** across **`10 Hz` to `20.48 MHz`**.

---

## Caddmas USB (`caddmas3x8`, `caddmas8x4`)

- **License Class:** `CADDMAS_CHANNELS` (`ANY_CHANNELS` fallback)
- **OS Support:** Windows 64-bit and Linux 64-bit (`libusb-1.0`; Windows requires **WinUSB** device binding installed via **Zadig**).

| Driver ID | USB Interface | Analog Channels | Resolution | Sample Rate Range | Auxiliary Inputs |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **`caddmas3x8`** | USB (1st Gen) | `24` (`3 x 8` banks) | 16-bit | `4.883 kHz`–`216 kHz` | `3` RPM tachometers + IRIG timecode |
| **`caddmas8x4`** | USB 2.0 | Up to `32` (`8 x 4` banks) | 16-bit | `796 Hz`–`100 kHz` | Integrated bank configuration |

See also: [Driver Matrix Overview](README.md) · [Architecture & Licensing](architecture-and-licensing.md)
