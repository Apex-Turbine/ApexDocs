# SDR File Format, Batch Automation, and Utilities

This reference covers the binary `.sdr` schema, model validation and comparison rules, `GmScript` batch automation, companion export tools (`SDRDump` and `SdrToJson`), and troubleshooting tips.

## `.sdr` Binary Schema Overview

The APEX Standard Reduced (`.sdr`) format stores a compact, self-contained representation of finite-element geometry and solution results optimized for rapid 3D loading and strain-gage / fatigue analysis:

| Section | Stored Contents |
| --- | --- |
| **Header & Endianness** | Format magic (`SDR_MAGIC_OLD`, `SDR_MAGIC_NEW`, `SDR_MAGIC_CSS`, `SDR_MAGIC_NEWER`), format version (`2.0` through `3.6+`), byte-order verification tokens (automatic cross-platform byte swapping on read), and byte offsets to geometry, sensors, and shapes. |
| **Geometry** | Node records (`origidx`, 3D coordinates, nodal temperature, stress layer count); Element records (`origeidx`, element type, corner node connectivity, material ID, real-constant/section ID); External free faces (`bl_face` connectivity & adjacency); Material property tables (isotropic/anisotropic flag, temperature-dependent `E`, `G`, `nu`, `alpha`, reference temperature, `ESYS` Euler orientation); Shell real constants & section thickness data. |
| **Cyclic Symmetry & Blade Tip** | Sector count (`nsecs`), cyclic expansion flag, rotation axis (`axial`, `radial`, `tangential` direction vectors), and optional NSMS blade-tip edges (`v3.05`). |
| **Sensors** | Embedded strain gages and tip-timing spot probes (`v3.0+`), including gage type, coordinates, sensing vectors, dimensions, and mapped surface status. |
| **Solution Shapes** | Ordered list of dynamic modes (`frequency`, `nodalDiameter`, `isStatic=false`) and static load cases (`rpm`, `isStatic=true`), each holding real and optional imaginary per-node displacements (`Ux, Uy, Uz`), rotations (`Rx, Ry, Rz`), engineering strains (`ex, ey, ez, gxy, gyz, gzx`), and stresses (`sx, sy, sz, txy, tyz, tzx`) across stress layers (top/bottom for shells). |

> [!NOTE]
> An `.sdr` file can flag whether imported strains/stresses are stored in the **element local coordinate system** (`usesLocalCoords`) or transformed to the global Cartesian coordinate system. When stresses/strains are omitted during conversion, GageMap computes them from nodal displacements and material constitutive properties.

---

## Model Comparison & Compatibility Validation

Whenever shapes are loaded from a secondary `.sdr` file (**Shapes > Load from SDR File** or `sdrfm.load_shapes()`), `SDRFM` performs a structural diff (`sdrfm_model_validate`) between the loaded base model (`Model #1`) and the incoming `.sdr` file (`Model #2`):

1. **Entity Counts**: `nnodes`, `nelems`, `nfaces`, `nmatprop`, and `nreals` must match exactly.
2. **Nodal Geometry**: Every node is compared index-by-index for:
   - `origidx` (original FE node ID)
   - Coordinates ($|x_1 - x_2| \le 1.0\times 10^{-8}$, $|y_1 - y_2| \le 1.0\times 10^{-8}$, $|z_1 - z_2| \le 1.0\times 10^{-8}$)
   - `temperature` and `nstress` (stress layer count)
3. **Elements**: Matching original element ID (`origeidx`), corner count, material index (`matnum`), and real-constant/thickness index (`realnum`).
4. **Materials & Real Constants**: Matching `aniflag`, temperature count, temperature points, elastic/shear/Poisson constants (within `1.0e-8`), and thickness values.

Any mismatch aborts the shape import and writes a side-by-side comparison (`Model #1` vs. `Model #2`, or `Original Material` vs. `New Material`) into the **History Browser** log.

---

## Batch Automation & Companion Utilities

### `GmScript` (`GM.sdrfm()`)

All interactive `SDRFM` workflows can be scripted headlessly in Lua using `GmScript` (see [SDRFM Functions for Scripting](../GmScript/script_sdrfm.md) for the complete API):

```lua
function main()
    local sdrfm = GM.sdrfm()
    sdrfm.open("C:/models/rotor_base.sdr")
    sdrfm.load_shapes("C:/models/rotor_modes.sdr")
    sdrfm.load_groups("C:/models/airfoil_only.grp")

    -- Trim to Airfoil group and generate a virtual mode shape at 1.0 deg step
    sdrfm.export_trim("Airfoil", 1)
    sdrfm.export_vmode(1, 16, 1.0, 1, 0, 0) -- Mode 1, VonMises stress, mass normalized
    sdrfm.export_model("C:/models/rotor_airfoil_vms.sdr")
end
```

Key `GM.sdrfm()` methods include:
- **Load & Inspect**: `open`, `save`, `load_shapes`, `load_sensors_sga`, `load_sensors_sdr`, `load_groups`, `nshapes`, `nmodes`, `nloads`, `ngages`, `ngroups`, `nnodes`, `node`, `mshape_info`, `mlist_freq`, `max_phase`.
- **Shape Export & Manipulation**: `export_shape`, `export_nshapes`, `export_vmode`, `export_cssmode`, `export_arithadd`, `export_arithdone`, `export_removeshape`.
- **Geometry Reduction & Cyclic Expansion**: `export_trim`, `export_expand`, `export_expand_clr`, `export_expand_opt`, `export_model`.
- **User-Defined Shape I/O**: `load_GBF`, `save_GBF`.

### `SDRDump` Export Utility

`SDRDump` (`SDRDump.exe` / `SDRDump`) is a dedicated companion utility for extracting raw numerical arrays from any `.sdr` file into external analysis formats:

- **Export Formats**:
  - **CSV (`.csv`)** — Comma-separated tables
  - **Text (`.txt`)** — Formatted ASCII report
  - **MATLAB Script (`.m`)** — MATLAB ASCII array definitions
  - **MATLAB Binary (`.mat`)** — Native MATLAB binary file (requires MATLAB `libmat` on `PATH` / `LD_LIBRARY_PATH`)
- **Selectable Data Blocks**: Node indices/normals/temperatures, face indices/normals/center strains, element node/face connectivity, sensor definitions, material properties, mode eigenvalues/eigenvectors/strains/stresses, static load eigenvalues/eigenvectors/strains/stresses, mean-stress aligned tensors, node-subset filtering (e.g., `1-100, 250`), double precision (`2X`), and complex magnitude/phase representation.

Inside GageMap Classic (`GM`), this same capability is integrated under **Options > Model Export** (see [Working With SDR Models](../GM/usingSDR.md#exporting-a-model)).

### `SdrToJson` Utility

The `SdrToJson` command-line utility exports `.sdr` node, face, and element geometry structures to JSON files for custom tooling pipelines:

```text
SdrToJson <SDR_filepath> <output_file_prefix>
```

---

## Troubleshooting

| Symptom | Cause | Resolution |
| --- | --- | --- |
| **Incompatible model error on `Load Shapes`** | Node coordinates differ by more than `1.0e-8`, or node/element/material/thickness counts differ (common when one `.sdr` was generated from a non-linear deformed state or different `.cdb`). | Inspect the History Browser diff (`Model #1` vs `Model #2`). Re-convert both results against identical undeformed geometry or check `Apply Non-Linear Geometry` / `Relax Geometry Comparison` settings in [SDR Converter](../SDR%20Converter/README.md). |
| **Out-of-memory warning loading `.sdr` in `GM`/`GMx`** | Full 3D mesh + all modes/stresses exceed workstation RAM. | Open the `.sdr` in `SDRFM`, use **Edit > SDR Editor** to keep only required modes/loads and trim non-critical regions via `.grp` groups, and verify **GageMap Model Size** fits physical RAM. |
| **Extra/incorrect static load cases in cyclic Virtual Mode export** | Known issue when exporting a VMS from a cyclic `.sdr` that already bundles a static load case. | Generate two separate `.sdr` files from ANSYS (`CDB + Static` and `CDB + Modal`), load the static `.sdr` as the base project, append shapes from the modal `.sdr` via **Shapes > Load from SDR File**, and then export the VMS (see [Known Issues](../GM/known_issues.md)). |
| **User-defined strain values look scaled wrong** | Tensor shear strains ($\varepsilon_{xy}$) were supplied instead of engineering shear strains ($\gamma_{xy} = 2\varepsilon_{xy}$). | Convert shear entries in `nodestrain` lines to engineering strain before running **Shapes > Import User-Defined**. |
| **Cannot load a second base `.sdr` project** | `SDRFM` locks **Load Base SDR** once a model is active to prevent unintended overwrites. | Exit and restart `SDRFM` before loading a different base project. |
