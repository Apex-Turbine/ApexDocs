# Known Issues

## General [LEGACY GageMap]

- **No support for Linux license servers:** There is an issue with the new Flexera modules & GageMap with Linux based license servers that prevents serving of either GageMap or GmScript licenses.
- **Linux version: Unable to acquire a license:** Linux versions of GageMap that utilize a Windows license server may require restarting the application to acquire a valid licenses.
- **Shell element imported strain & stresses may be incorrect:** Imported values for shell elements should be checked against values in the FE solver prior to beginning a GageMap analysis. The conversion process has issues consistently averaging values from the upper & lower surfaces in some instances.
- **Shell Element models may produce incorrect gage results:** Applies to 3, 6 and 8 node shell elements.
- **Occasional crashes can occur in the conversion of ANSYS files:** This appears to be related to the ANSYS API, and mainly for cyclic files.
- **Anisotropic material properties interface:**  Limited support for anisotropic materials. Both TYPE=ANISOtropic and TYPE=ORTHOTROPIC are not supported. Additionally, EXPANSION, TYPE=ANISO is not supported.
- **Stresses and strains not averaged for all nodes:** When using GageMap calculated results (Options/Stresses/Use GageMap computed), node contributions from some faces may be excluded from the averaging.

  > - **Work-Around:**  Use Imported results
- **Mis-identification of free faces:**  During conversion from FE results to SDR geometry, free faces on the model are generated. Free faces are those element faces that are not mated to any other elements. Free faces that are incorrectly identified may have sensor placed upon them and whose nodes are incorrectly labeled as "external". Incorrect identification of free faces occurs under the following conditions:

  > - 3 node triangle mated with collapsed 4 node quad
  > - 6 node triangle mated with collapsed 8 node quad
  > - 2-3 node triangles mated with a single 4 node quad
  > - 2-6 node triangles mated with a single 8 node quad
  > - **Work-Around:**  Use grouping task to identify and eliminate face/nodes that are incorrectly identified as "free" or "external" for gage placement and/or within the fatigue assessment task.
- **Only constant thickness shells are supported:** the first thickness defined is assigned to the all nodes for the shell element.
- **Incorrect number of static load cases when creating a virtual mode shape from the SDR File Manager:** If the SDR basis file contains a static load case and is cyclic symmetric, when exporting a virtual mode shape the resulting SDR file may contain additional (incorrect) static load cases. If this problem is encountered, the following work-around can be implemented with ANSYS results:

  > - Create 2 SDR files from the cyclic results:  CDB + Static & CDB + Modal
  > - Load static SDR as a project.
  > - Load shapes from the modal SDR using the shapes menu.
  > - Proceed as before to create the VMS SDR.

## GmScript

- **Application requires a connection to a display for linux systems**

## ABAQUS Converter (ABA2SDR)

- **No support for initial temperatures:**  Initial Temperatures are not currently supported when importing from ABAQUS. For this reason, stresses and strains might be incorrect when using GageMap Computed values.

  > - **Work-around:** Adjust material properties and thermal conditions such that zero initial conditions are valid.
