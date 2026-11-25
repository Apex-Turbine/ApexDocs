# SDR Converter (`SdrConverter`)

The **SDR Converter** (`SdrConverter`) is the unified finite-element-to-SDR translation application for APEX GageMap. It extracts mesh geometry, material definitions, nodal temperatures, mode shapes, static load cases, and optional nodal stresses/strains from native FE solver result files into compact `.sdr` (Standard Reduced) models.

## Supported Finite-Element Solvers

| Solver | Selection Option in Wizard | Supported Input Files | Documentation |
| --- | --- | --- | --- |
| **ANSYS** | `Ansys (.RST)` | `.rst`, `.rstp` (including `/CONFIG,FSPLIT` split files), and legacy `.cdb` + `.rst` | [ANSYS Converter Guide](ansys.md) |
| **ABAQUS** | `Abaqus (.ODB)` | `.odb` (Abaqus Output Database) | [ABAQUS Converter Guide](abaqus.md) |
| **MSC Nastran** | `MSC Nastran (.OP2)` | `.op2` (MSC Nastran binary output2) | [NASTRAN Converter Guide](nastran.md) |
| **NX Nastran** | `NX Nastran (.OP2)` | `.op2` (NX Nastran / Simcenter Nastran binary output2) | [NASTRAN Converter Guide](nastran.md) |

> [!NOTE]
> Earlier GageMap releases shipped separate standalone converter binaries (`ansys2sdr`, `aba2sdr`, `nas2sdr`). Current releases unify all four solver pipelines inside the single **SdrConverter** Qt Wizard application.

---

## GUI Wizard & Batch Queue Workflow

The `SdrConverter` graphical interface operates as a three-step wizard:

1. **Page 1 — Solver Selection**: Choose `Ansys (.RST)`, `Abaqus (.ODB)`, `MSC Nastran (.OP2)`, or `NX Nastran (.OP2)` and click **Next**.
2. **Page 2 — Files, Options & Conversion List**:
   - Specify input result file(s) (`RST` list for ANSYS, `ODB` for ABAQUS, `OP2` for NASTRAN) and the destination `.sdr` output path.
   - Toggle solver-specific conversion options (stress/strain loading, first-order surface faces, local coordinate systems, cyclic symmetry, custom mode subsets, or non-linear geometry).
   - Click **Add To Conversion List** to stage one or more jobs (each output `.sdr` path in the queue must be unique). Click **Convert** to launch the queue.
3. **Page 3 — Progress & Output Logs**:
   - Conversions execute sequentially in the background while tracking per-job progress bars and live log output.
   - Each job automatically writes a timestamped log file (`<sdr_basename>-dd-MM-yy-hh-mm-ss-zzz.log`) alongside the output `.sdr` file.

---

## Programmatic & Batch Conversion (`GmScript`)

Automated workflows can invoke the same converter libraries (`AnsysLib`, `AbaqusLib`, `NastranLib`) directly from Lua scripts in [GmScript](../GmScript/README.md) via `GM.sdrconverter()` (or the legacy `GM.ansys()` helper; see [Ansys Functions for Scripting](../GmScript/script_ansys.md)):

- `sdrconverter.ansys(rst_list, outfile)` — Converts one or more ANSYS `.rst` files to `.sdr`.
- `sdrconverter.abaqus(odb_file, outfile)` — Converts an ABAQUS `.odb` file to `.sdr`.
- `sdrconverter.nastran(op2_file, outfile)` — Converts a NASTRAN `.op2` file to `.sdr`.
- `sdrconverter.set_option(key, value)` / `sdrconverter.reset_option([key])` — Configures converter flags (`modal_stress`, `static_stress`, `cyclic`, `first_order`, `local_coord`, `apply_nl`, `nl_file_index`, `nl_shape_index`, `use_max`, `file_rpm`).
- `sdrconverter.mode_subset(mode_list)` — Restricts ANSYS mode extraction to specific indices/ranges (e.g., `"1-5, 10"`).

---

## Element, Material, and Strain/Stress Preservation Notes

- **Required vs. Optional Solution Fields**: Nodal **displacements** are required for every static load case and mode shape. Nodal **strains and stresses** are optional (disabling them produces smaller `.sdr` files and causes GageMap to compute nodal strains/stresses directly from displacements and material properties), though importing solver stresses/strains is strongly recommended for **shell elements**.
- **Elastic vs. Total Strains**:
  - **ANSYS** and **ABAQUS** (`EE`) import **elastic** strains.
  - **NASTRAN** imports **total** strains.
- **Coordinate Systems**: By default, element strains and stresses are transformed into the **global Cartesian** coordinate system before nodal averaging. Enable **Maintain Local Coordinate System (Strains / Stresses)** to preserve element material/coordinate orientations (`ESYS` / local CSYS).
- **First-Order Face Option**: Selecting **Use First Order Types for Elements** forces parabolic solid/shell elements (e.g., 20-node bricks, 10-node tetrahedra) to generate linear (4-node / 3-node) surface faces, eliminating mid-side interpolation artifacts on complex curved faces.
- **Surface Detection & Shell Thickness**: Free external faces are identified automatically for sensor placement. For ANSYS shells, thickness must be defined via `REAL` constants rather than section (`SECTYPE`) definitions, and both top and bottom surface results (not mid-plane) are required when importing shell stresses/strains.
- **Materials & Thermal Expansion**: Isotropic, orthotropic/engineering-constant, and temperature-dependent elastic materials plus isotropic thermal expansion (`ALPX` / `EXPANSION, TYPE=ISO`) and reference temperatures (`REFT` / `TREF`) are preserved in the `.sdr` material table.

---

## Licensing

> [!WARNING]
> Legacy **FLEXlm / FlexNet** (`lmgrd`, `27000@host`) licensing will be **discontinued as of October 2027**. All product versions going forward use **[APEX License Manager](../../License%20Manager/README.md)** (`ApexLM`).

`SdrConverter` follows the GageMap dual-licensing architecture (`GM_FLEX_SERVER` for FlexNet, or **ApexLM** on `127.0.0.1:27884` with Web Admin UI at `http://127.0.0.1:27887/`):

- **ApexLM & Converter Entitlements**: Deployed alongside `GM` / `GMx` / `GMSCRIPT` and solver converter entitlements (`ANSYS_CONVERTER`, `ABAQUS_CONVERTER`, `NASTRAN_CONVERTER`).
- **Legacy FlexNet**: Configured via `GM_FLEX_SERVER` or `LM_LICENSE_FILE` (`27000@host` or `.lic` path).

See [GM Licensing](../GM/flex.md) and [GMx Licensing](../GMx/flex.md) for server setup and troubleshooting.

---

## Solver Guides

- **[ANSYS to SDR Converter (`ansys.md`)](ansys.md)** — ANSYS 2019 R2+ library configuration (`CadoeKernel`/`CadoeReader`/`CadoeCore`), `.rst`/`.rstp`/`.cdb` inputs, element/material tables, non-linear geometry, and cyclic symmetry conversion.
- **[ABAQUS to SDR Converter (`abaqus.md`)](abaqus.md)** — Abaqus ODB extraction, runtime DLL/SO prerequisites (Abaqus 2018–2021 and legacy 6.14-1), field output requests, rotational static steps, and supported elements.
- **[NASTRAN to SDR Converter (`nastran.md`)](nastran.md)** — MSC Nastran and NX Nastran `.op2` conversion, supported elements/materials (`MAT1`/`MAT8`/`MAT9`), orthogonal mode merging, and eigenvector normalization.
