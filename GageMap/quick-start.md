# APEX GageMap Quick Start Guide

Follow this end-to-end workflow to verify GageMap licensing, convert a finite-element (FE) model to `.sdr`, inspect reduced modal results, place or optimize sensors, and evaluate high-cycle fatigue (HCF) margins.

---

## Step 1: Verify Licensing

1. Verify your active license in **[APEX License Manager (ApexLM)](../License%20Manager/README.md)** at `http://127.0.0.1:27887/` (`GM`, `GMx`, `GMSCRIPT`, `SDRFM`, and converter entitlements — see the [License Manager Quick Start](../License%20Manager/quick-start.md)), or confirm your legacy FlexNet server (`27000@host`).
2. See [GM Licensing](GM/flex.md), [GMx Licensing](GMx/flex.md), and [GmScript Installation & Licensing](GmScript/install.md).

> [!NOTE]
> Legacy **FLEXlm / FlexNet (`lmgrd`)** licensing is being **discontinued as of October 2027**. All product versions going forward will exclusively use **APEX License Manager** (`ApexLM`). See [Software Release Policies](../Release%20Policies/README.md) for system requirements, the 18-month version support policy, and end-user licensing terms.

---

## Step 2: Convert an FE Model to `.sdr`

Launch the unified **`SdrConverter`** wizard (or open it directly from GageMap) to translate solver results into APEX reduced `.sdr` format ([SDR Converter Overview](SDR%20Converter/README.md)):

- **ANSYS**: Supply `.cdb` mesh + `.rst` / `.rstp` result files ([ANSYS Converter Guide](SDR%20Converter/ansys.md)).
- **ABAQUS**: Ensure required Abaqus runtime libraries are on `PATH` / `LD_LIBRARY_PATH` and select the `.odb` database ([ABAQUS Converter Guide](SDR%20Converter/abaqus.md)).
- **NASTRAN**: Select the MSC or NX Nastran `.op2` file and configure eigenvector normalization ([NASTRAN Converter Guide](SDR%20Converter/nastran.md)).

---

## Step 3: Inspect or Reduce the `.sdr` Model (Optional)

Open the converted `.sdr` file in **[SDR File Manager (`SDRFM`)](SDRFM/README.md)** to:

- Verify node/element counts, materials, modal frequencies, and static load steps.
- Trim large geometries with `.grp` groups, expand cyclic symmetry sectors, or combine shapes ([Browsers & Operations](SDRFM/browsers-and-operations.md)).

---

## Step 4: Place Sensors, Optimize & Evaluate Fatigue

1. Launch **GageMap Next Gen (`GMx`)** ([GMx Guide](GMx/README.md)) or **GageMap Classic (`GM`)** ([GM Guide](GM/README.md)) and load your `.sdr` file.
2. In the **Model** tab, animate mode shapes to verify normalized displacements and strains ([Model Animation](GMx/task_modelAnim.md)).
3. Create strain gages or tip-timing sensors manually or run **Optimizer** to place sensors for maximum observability and mode separation ([Optimization](GMx/task_optimize.md) · [Sensors](GMx/task_sensors.md)).
4. Run **CSS Phase Search** (for cyclic symmetry models), **Mean Stress Alignment**, and **Fatigue Assessment** ([Fatigue](GMx/task_fatigue.md)), then export `.sga` sensor definitions and `.csv` / Scope Limits reports.
5. Save your `.gmp` project (`.gma`, `.gms`, `.gmo`, `.gmg`, `.gml` libraries).

---

## Step 5: Automate with GmScript & Theory Reference

- **Headless Lua Batch Automation**: Automate SDR conversion, `GM.sdrfm()`, sensor sweeps, and reporting using [GmScript](GmScript/intro.md).
- **Engineering Reference**: Review underlying tensor, misplacement, optimization, and Goodman fatigue equations in the [GM Theory Manual](GM%20Theory/README.md).
