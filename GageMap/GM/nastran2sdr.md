# NASTRAN Converter

> [!NOTE]
> For the consolidated `SdrConverter` MSC Nastran and NX Nastran `.op2` guide, see **[NASTRAN Converter Guide](../SDR%20Converter/nastran.md)** and **[SDR Converter Overview](../SDR%20Converter/README.md)**.

## Overview

The "NASTRAN to SDR" option of the SdrConverter application is designed to take native NASTRAN FE (.OP2) model's output files and convert them into an SDR file to be used GageMap.

## Converter Options

- **Do NOT Load STATIC LOAD Stresses and Strains:** If the .OP2 file contain static load cases with strain and stress solutions, then selecting this option will store static load cases in the GageMap SDR file without the NASTRAN strain and stress values. This will force GageMap to calculate its own strain and stress values for the model.
- **Do NOT Load DYNAMIC Stresses and Strains:** If the .OP2 file contain modes with strain and stress solutions, then selecting this option will store modes in the GageMap SDR file without the NATRAN strain and stress values. This will force GageMap to calculate its own strain and stress values for the model.
- **Use First-Order Face Types for Elements:** This option allows you to force the converter to use first-order face types for elements which are defined with post order face types. This will effect how strains and stresses are computed for not only faces, but also for gages. If you are getting a stress distribution on a 10 node tetrahedral or 20 node brick elements that is irregular or not what you were expecting, try reconverting the model with this option selected.

> [!NOTE]
> For example, if you use this option corresponding with a model that contains 20 node brick elements, the converter will not use an 8-node face with mid-side nodes but will rather use a 4-node face type without mid-side nodes.

- **Normalize Eigenvectors to:** This option allows you to normalize all the modal eigenvectors to the value desired. This can also be performed after converting the model using the SDR File Manager utility. See the SDR File Manager Utility section for further details.
