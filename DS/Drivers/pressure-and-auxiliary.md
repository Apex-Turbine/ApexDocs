# Pressure Scanners, Parameter Servers & Auxiliary Drivers

These plugins provide steady-state pneumatic pressure scanning, external network parameter bridges, offline file-based acquisition simulation, built-in signal synthesis, and PC audio input.

---

## PSI 9016 / 9021 Pressure Scanners (`psi9016`)

- **License Class:** `PSI_CHANNELS` (`ANY_CHANNELS` fallback)
- **OS Support:** Windows 64-bit and Linux 64-bit.
- **Interface:** Ethernet TCP/IP using the **Optomux** protocol (`port=9000` default).
- **Mapping & Behavior:**
  - **Parameter-only driver** (`numChannels = 0`, `numParameters = 16` per unit).
  - Polls scanner pressures at configurable intervals (`period=100` ms default), supports subset selection (`channels=1-16`), and block-averages values into DS parameter frames.
  - Does **not** support IEEE 1588 PTP timestamp synchronization.

---

## Scanivalve Scanners (`scani`)

- **License Class:** `SCANI_CHANNELS` (`ANY_CHANNELS` fallback)
- **OS Support:** Windows 64-bit and Linux 64-bit.
- **Supported Modules:**

| Driver ID | Hardware Series | Analog Channels | Extra Parameters | Max Sample Rate | Ethernet Protocol Ports |
| :--- | :--- | :---: | :--- | :---: | :--- |
| **`scani321x` / `scanidsa`** | DSA 32xx | 16 pressure | Unit metadata | `250 Hz` | Telnet ASCII (`23`) |
| **`scanidsa5000`** | DSA 5000 | 16 pressure | Calibration/status | `5000 Hz` | Telnet (`23`) + Binary stream (`503`) |
| **`scanimps`** | MPS 42xx | 64 pressure | `8` temperature params/ch + **PTP timecode** | `1000 Hz` | Telnet (`23`) + Binary stream (`503`) |

---

## Network Parameter Bridges (`param`, `paramds`)

- **License Class:** `OTHER_CHANNELS` (`ANY_CHANNELS` fallback), plus `PARAMETER_SERVER` on DS when external parameters are active.
- **OS Support:** Windows 64-bit and Linux 64-bit.
- **Mapping:** Parameter-only (`numChannels = 0`, default `numParameters = 10`, configurable via `map=PARAMLIST`).
- **Two Connection Protocols:**
  - **`param` (`drv-param`):** Connects to a legacy EDAS/DS 2.x TCP parameter socket (`localhost:6600` default).
  - **`paramds` (`drv-paramds`):** Subscribes to parameters emitted by another running **APEX DS** server using the DS-to-DR protocol (`server=<HOST>:<CONFIG>`).

---

## File Replay Drivers (`datafile`, `bttfile`)

Offline replay drivers expose recorded data files as virtual acquisition hardware inside DS so plot layouts, limits, triggers, and downstream consumers (`DR`, `DM`, `DO`) can be tested without live sensors:

| Driver ID | Plugin Module | Supported Inputs | ApexLM License Pool |
| :--- | :--- | :--- | :--- |
| **`apexfile`** | `drv-datafile` | Recorded `.rwx`, `.rwz`, and legacy `.raw` dynamic files | `OTHER_CHANNELS` |
| **`datxfile`** | `drv-datafile` | Recorded `.datx` / `.datx_index` DspCON brick files | `OTHER_CHANNELS` |
| **`bttfile`** | `drv-bttfile` | Recorded `.cdt` Blade Tip-Timing (BTT) datasets | `BTT_CHANNELS` |

---

## Built-in Signal Simulator (`simul`, `nsimul`, `simuldll`)

- **License Requirement:** Selecting simulated input (`INPUT_SIMULATOR` / `simul`) in **APEX DS** runs in **evaluation mode**, waiving hardware channel and optional DS feature checkouts (`AEROPLOTS`, `PARAMETER_SERVER`, `RWX_COMPRESSION`, `DS_MANAGER`).
- **Capabilities:**
  - Generates **`32` dynamic channels** and **`4` low-speed parameters** using continuous swept-sine waveforms.
  - Configurable output types (`I16`, `I32`, `F32`), effective bit depth (`bits=8..24`), and multi-card skew testing (`diverge`).
  - Supports amplifier UI mimic modes emulating NI `449x`, `446x`, and `4331` configuration panels.
  - **`nsimul` (`drv-nsimul` + `srv-nsimul`):** Proxy-wrapped variant used for validating `ProxyDev` IPC transport without physical cards.

---

## PC Sound Card (`sndcard`)

- **License Class:** `OTHER_CHANNELS` (`ANY_CHANNELS` fallback)
- **OS Support:** Windows and Linux (ALSA `asound`).
- **Capabilities:** Uses standard PC audio inputs for `1` or `2` AC-coupled 16-bit channels at **`8000`**, **`11025`**, **`22050`**, or **`44100 Hz`**.

---

## Unbuilt / Experimental Source Notes

- **`modbus`:** A `libmodbus`-based driver scaffold resides in the DS driver source tree (`drivers/modbus`) and is currently disabled in `drivers/CMakeLists.txt` (`#MODBUS TODO`), so no `drv-modbus` binary is built in standard releases.

See also: [Driver Matrix Overview](README.md) · [Architecture & Licensing](architecture-and-licensing.md)
