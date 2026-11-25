# SDR File Manager (`SDRFM`)

The **SDR File Manager** (`SDRFM`) is the standalone inspection, model-reduction, shape-combination, and cyclic-symmetry expansion utility for APEX GageMap `.sdr` (Standard Reduced) finite-element model files.

## Core Capabilities

- **Model Inspection & Validation**: View node/element statistics, element-type breakdowns, external surface faces, material properties, shell thickness constants, modes, static load cases, sensors, and groups. Validate geometric compatibility (`1.0e-8` tolerance) before appending shapes from secondary `.sdr` files.
- **Reduced `.sdr` Export & Trimming**: Export memory-efficient `.sdr` subsets containing selected modes, static load cases, sensors, and geometry trimmed via GageMap group (`.grp`) Boolean filters.
- **Cyclic Symmetry Operations**:
  - Expand cyclic-symmetric models to arbitrary sector lists around the rotation axis.
  - Generate **virtual mode shapes** by searching phase angles (`0°`–`360°`) per node for maximum displacement, strain, or stress responses.
  - Export phase-shifted and complementary (`90°`) mode pairs while preserving complex cyclic relationships.
- **Shape Arithmetic & Scaling**: Combine multiple static load cases (real scalar multipliers) or modal shapes (real or complex scalar multipliers) via linear summation.
- **User-Defined Shape & Temperature I/O**: Import and export ASCII/GBF user-defined nodal temperatures and static or modal displacements, rotations, engineering strains, and stresses.

## Launching SDRFM

### Standalone Desktop Application

Launch `SDRFM` (`SDRFM.exe` on Windows, `SDRFM` on Linux) directly from your installation `bin` directory or Start Menu shortcut. Upon launch, `SDRFM` opens with an empty project ready to load a base `.sdr` file (**File > Load Base SDR** or **Geometry > Load from SDR File**).

### Within GageMap (`GM` & `GMx`) Workflows

- **GageMap Classic (`GM`) & Next Gen (`GMx`)**: Prepare, trim, combine, or expand large FE `.sdr` models in `SDRFM` prior to opening them in `GM` or `GMx` so model memory fits workstation limits. For inspecting or exporting tabular data from a loaded model inside `GM`, use **Options > Model Export** (see [Working With SDR Models](../GM/usingSDR.md)).
- **Automated Scripting (`GmScript`)**: Full `SDRFM` functionality is available headlessly via the `GM.sdrfm()` Lua module (see [SDRFM Functions for Scripting](../GmScript/script_sdrfm.md) and [File Format & Batch Utilities](file-format-and-batch.md)).

## Licensing

> [!WARNING]
> Legacy **FLEXlm / FlexNet** (`lmgrd`, `27000@host`) licensing will be **discontinued as of October 2027**. All product versions going forward use **[APEX License Manager](../../License%20Manager/README.md)** (`ApexLM`). (`SDRFM` & `SDRDUMP`)

`SDRFM` and its companion export utility `SDRDump` (`SDRDUMP`) support both **APEX License Manager (ApexLM)** and **Legacy FlexNet Publisher**:

| Aspect | ApexLM (Modern) | Legacy FlexNet |
| --- | --- | --- |
| **Registered Applications** | `SDRFM`, `SDRDUMP` (category `ANALYSIS`) | `SDRFM`, `SdrDump` (shares `GAGEMAP_FLEX_SERVER`) |
| **Server / Endpoint** | Local ZeroMQ `127.0.0.1:27884` (`LOCAL` / `PASSTHROUGH` / `SERVER` modes; external listen `27886`) | `GAGEMAP_FLEX_SERVER` or `LM_LICENSE_FILE` (`27000@host` or `.lic` path) |
| **Admin Portal** | `http://127.0.0.1:27887/` (`27888` for server) | `lmtools` (Windows) / `lmstat` / `lmutil` |
| **Feature Notes** | Checks `SDRFM` / `SDRDUMP` app entitlement; version must not exceed license `YYYY.MM`. | Legacy builds gated custom shape import/export and cyclic operations under `CUST_MODELING` and `CSS`. |

For full ApexLM and FlexNet configuration steps, see [GM Licensing](../GM/flex.md) and [GMx Licensing](../GMx/flex.md).

## Documentation Guide

- **[Browsers and Operations](browsers-and-operations.md)** — Complete UI walkthrough covering the Model, Shape, Cyclic, Sensor, Group, Exporter, and History browsers, project loading/saving, shape arithmetic, cyclic expansion, virtual mode shapes, mass normalization, geometry trimming, and unit consistency.
- **[File Format and Batch Utilities](file-format-and-batch.md)** — `.sdr` binary schema overview, model compatibility comparison rules, user-defined ASCII/GBF shape format, `GmScript` automation, `SDRDump` / `SdrToJson` export utilities, and troubleshooting.
