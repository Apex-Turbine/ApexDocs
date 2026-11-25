# Python Setup & Configuration (`dsapi.py` & `tdf2dspro.py`)

Inspect, modify, and build DS acquisition setups programmatically via `dsapi.py`, and understand how `tdf/tdf2dspro.py` inspects Excel test-definition workbooks.

## Programmatic Setup API Groups (`dsapiscript.h` / `dsapi.py`)

`dsapi.py` wraps five setup-management families exported by `dsapiscript`:

| Prefix Family | Target Entity | Typical Operations |
| --- | --- | --- |
| `dsapi_setup_*` | `DspSetup` | Create/free setups, load/save setup files, query/set sample rate (`sampleFrequency`), block size (`blockSizeLog2`), counts |
| `dsapi_rsrc_*` | Hardware Resources | Enumerate and configure acquisition hardware resource entries |
| `dsapi_param_*` | Scalar Parameters | Add, inspect, and update external/computed parameter metadata (name, units, min/max, linked channel) |
| `dsapi_chan_*` | Signal Channels | Query or configure analog/tach channel properties (name, type, sample ratio, unit, range, EU calibration coefficients) |
| `dsapi_stat_*` | Channel DSP Statistics | Query and attach per-channel DSP statistical metrics |

### Inspecting a Loaded Setup

When opening a `.rwx`/`.datx`/`.pkx` recording via `dsapi_file_*` or connecting to a live DS 3.x host via `get_network_session()`, retrieve the setup handle and pass it to the `dsapi_setup_*`, `dsapi_chan_*`, `dsapi_param_*`, `dsapi_rsrc_*`, and `dsapi_stat_*` accessors bound in `dsapi.py`.

## Excel Test Definition Inspector (`tdf/tdf2dspro.py`)

The SDK includes `tdf/tdf2dspro.py` alongside sample Excel workbooks (`ADD_TDF_TEMPLATE_PFI_TESTMODES.xlsx`, `T247 X634-43 Test Def.xlsx`) for automating **Test Definition File (TDF)** workflows.

### Important Status Note
`tdf/tdf2dspro.py` uses **`openpyxl`** to open `ADD_TDF_TEMPLATE_PFI_TESTMODES.xlsx` and prints out structured workbook sections:
- **`File Header`**
- **`System Variables`**
- **`Channel Dynamic`**

> [!NOTE]
> As shipped in `DS/API/tdf/tdf2dspro.py`, the script acts as an **Excel template reader/inspector** that parses and prints those sections—it does **not** yet call `dsapi` to write an output `.dspro` setup file directly.

### Combining `tdf2dspro.py` Parsing with `dsapi.py`

To build an automated Excel-to-`.dspro` generator in Python:

1. **Parse workbook metadata** with `openpyxl` (following the sheet/section layout demonstrated in `tdf/tdf2dspro.py`).
2. **Initialize a DS setup** in `dsapi.py` using the `dsapi_setup_*` create/rate/blocksize helpers.
3. **Populate hardware, channels, stats, and parameters** using `dsapi_rsrc_*`, `dsapi_chan_*`, `dsapi_stat_*`, and `dsapi_param_*` from the parsed `File Header`, `System Variables`, and `Channel Dynamic` tables.
4. **Persist or push the setup** using `dsapi_setup_*` save helpers (or upload directly to a managed DS 3.x server over the network API).
