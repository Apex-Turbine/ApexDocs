# APEX DS Quick Start Guide

This guide walks through verifying licensing, creating an acquisition setup, monitoring live channels, recording `.rwx` / `.pkx` files, and connecting remote displays with **APEX DS**.

> [!TIP]
> **Evaluation Without Hardware or a License**
> You can launch **APEX DS** immediately in simulated input mode (`simul`) without physical acquisition hardware or license checkouts. All configuration, plotting, and recording workflows work identically.

---

## Step 1: Verify Licensing

Current and future **APEX DS** releases use **[APEX License Manager (`ApexLM`)](../License%20Manager/README.md)** (**APEX LM Daemon** & **APEX LM Server Daemon**; legacy FLEXlm / `lmgrd` licensing will be **discontinued as of October 2027**):

1. Open the local ApexLM Web Admin UI at `http://127.0.0.1:27887/` (or click **Configure** in the DS splash dialog) to confirm your mode (`LOCAL` or `PASSTHROUGH`) and active `DS` / `<VENDOR>_CHANNELS` / `ANY_CHANNELS` seats.
2. For client-server setups, verify TCP ports `27884`–`27886` are reachable.
3. Detailed instructions: [APEX License Manager Quick Start](../License%20Manager/quick-start.md) · [APEX DS Installation Licensing](DS/installation/licensing.md) · [Licensing Dialog](DS/interface/licensing.md).

---

## Step 2: Configure Acquisition Setup

1. Launch **APEX DS** and open the **Setup Editor** from the top menu bar (or click **Setup** on the [Record Bar](DS/interface/recordbar.md)).
2. Under **[Devices](DS/setup/devices.md)**, add your acquisition hardware (`NI`, `VTI`, `GS`, `Datatel`, `MeCalc`, etc.) or select the built-in **Simulator** (`simul`).
3. Under **[Channels](DS/setup/channels.md)** and **[Amplifiers](DS/setup/amplifiers.md)**, map physical inputs, engineering units (EU), sensitivity, and coupling.
4. Under **[Processing](DS/setup/processing.md)**, choose block sample rates, windowing, FFT resolution, and peak tracking options.
5. Under **[Storage](DS/setup/storage.md)**, specify output directory and recording formats (`.rwx`, `.pkx`, or `.datx`).
6. Save your project configuration to a `.dspro` file (`File -> Save Setup`).

---

## Step 3: Monitor Live Data & Create Plots

1. Click **Monitor** on the [Record Bar](DS/interface/recordbar.md) to arm hardware and begin streaming.
2. Right-click inside the [Plot Area](DS/plots/plotarea.md) or use the plot toolbar ([Creating Plots](DS/plots/plotcreate.md)) to open a **Scope**, **Spectrum (FFT)**, **Campbell**, or **Bar** plot.
3. Drag channels or processed parameters onto plot traces and adjust auto-scaling, cursors, and engineering limits ([All Plot Types](DS/plots/README.md)).

---

## Step 4: Record Test Runs

1. Set the next Data Point Number and Tag (`[A]ccel`, `[D]ecel`, `[S]teady State`, `[T]ransient`) in the [Data Point Dialog](DS/interface/datapoint.md).
2. Click **Record** to begin writing synchronized `.rwx` and `.pkx` files, or click **Rec++** to seamlessly increment to the next data point without sample gaps.
3. Click **Stop Recording**, then **Stop Monitoring** when the run completes.

---

## Step 5: Next Workflows

- **Remote Viewing (`APEX DR`)**: Connect [APEX DR](DR/README.md) over TCP (`10995`–`11004`) to monitor live DS telemetry from operator stations ([Server Connections](DR/interface/servers.md)).
- **Cluster & Batch Automation (`APEX DM`)**: Coordinate synchronized multi-chassis `N:M` nodes or headless scripted runs via [DM Command Reference](DM/dm-cmd-reference.md) and [Automation CLI Utilities](DM/automation-utilities.md).
- **Analog Replay (`APEX DO`)**: Stream recorded `.rwx` / `.datx` files or live DS feeds out to DAC hardware via [APEX Data Output](DO/README.md).
- **Hardware Drivers**: Check hardware-specific setup notes in the [Hardware Driver Matrix](Drivers/README.md).
