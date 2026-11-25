# ANSYS DB to SDR Converter

> [!NOTE]
> For the consolidated `SdrConverter` ANSYS guide (covering ANSYS 2019 R2+, CDB/RST workflows, all GUI options, non-linear geometry, and cyclic symmetry), see **[ANSYS Converter Guide](../SDR%20Converter/ansys.md)** and **[SDR Converter Overview](../SDR%20Converter/README.md)**.

## Overview

The ANSYS DB to SDR Converter option in the SdrConverter Application is used to convert ANSYS FE Models to the standard reduced file format for use with GageMap. Both static (ANTYPE,STATIC) and frequency extraction (ANTYPE,MODAL) steps are converted. Non-linear (NLGEOM,ON) static solutions are also supported, however, by default, the base state of geometry saved within the SDR file is the geometry at the end of the static step. This is important for dimensioning sensor locations. The format of files that can be read from ANSYS are:

1. Structural results file, referred to as the RST file

Ansys will be required to be installed on the system and the following steps taken:

This will require some paths be added to your PATH environment variable with your ansys installation (Instructions [https://docs.microsoft.com/en-us/previous-versions/office/developer/sharepoint-2010/ee537574(v=office.14](https://docs.microsoft.com/en-us/previous-versions/office/developer/sharepoint-2010/ee537574(v=office.14))#:~:text=%20To%20add%20a%20path%20to%20the%20PATH,scroll%20to%20Path%20and%20select%20it.%20More%20 ). These are as follows (Linux will be similar):

1. C:/Program Files/ANSYS Inc/${ANSYS_VER}/ansys/bin/winx64
2. C:/Program Files/ANSYS Inc/${ANSYS_VER}/tp/IntelMKL/2020.0.166/winx64
3. C:/Program Files/ANSYS Inc/${ANSYS_VER}/tp/IntelCompiler/2019.3.203/winx64

Where ${ANSYS_VER} is your ansys version directory:
1. v201 for 2020 R1
2. v202 for 2020 R2
3. v211 for 2021 R1
4. v212 for 2021 R2
5. etc.

Please verify these directories exist for your installation and the following libraries exist in the first path:
1. CadoeKernel.dll & CadoeReader.dll for 2021 R1 and above
2. CadoeCore.dll for 2019 R2 to 2020 R2

This converter will not work for ansys installations before 2019 R2.

Backwards compatibility is NOT available in the Ansys API. i.e. RST files written using version 2021 will crash the Ansys libraries if you perform a conversion with Ansys 2020 libraries in your path.

If the Ansys libraries are unable to be loaded a message "Ansys does not appear to be installed on your system..." will appear.

## ELEMENTS

The following elements are supported:

### 1-D elements (visualization only, no results other than node displacements are supported)

LINK1, BEAM3, BEAM4, LINK8, LINK10, PIPE20, BEAM23, BEAM24, BEAM44, BEAM54, PIPE59, LINK180, BEAM188

### 2-D Continuum elements

PLANE42, PLANE82, PLANE182, PLANE183

### 2-D Structural shell elements

SHELL28, SHELL41, SHELL43, SHELL63, SHELL181, SHELL93, SHELL281

### 3-D Continuum elements

SOLID45, SOLID92, SOLID95, SOLID185, SOLID186, SOLID187, SOLSH190

> [!NOTE]
> Other elements may be present in the CDB/RST files, however, they will not be imported during conversion. The converter log file will list elements present but not supported.
>
> It is important to note that element definitions for some parabolic element types may have incomplete definitions. This is especially true for mesh transition regions if the TCHG command has not been performed. Any element that does not contain a proper connectivity definition (node labels must be non-zero positive integers and the nodes must exist in the CDB file) will be reduced to the linear counterpart, i.e., 20 node brick to 8 node brick. Warnings will be issued during conversion.
>
> The shell element thickness property must be defined using REAL constants. Section information is ignored.

> [!NOTE]
> Shell Element Support is limited. There is no support for mid-surface element results, therefore mid-plane results should not be written to the RST file.

## MATERIAL PROPERTIES

The following elastic materials types are supported:Isotropic (MP,<EX,NUXY,PRXY>) and MPDATA,<EX,...>.

1. Orthotropic (MP,<EX,EY,EZ,NUXY,NUYZ,NUXZ,PRXY,PRYZ,PRXZ, GXY,GYZ,GXZ, and MPDATA,<EX,...>
2. Isotropic thermal expansion (MP,ALPX) and (MPDATA,ALPX)
3. Thermal expansion reference temperature, MP,REFT and TREF.

Material properties may be temperature dependent and oriented arbitrarily (ESYS).

## OUTPUT

Displacement output must be present for both static load cases and modes, however element solution output (strains & stresses) is optional. It is highly recommended that strain & stress output for shell elements be present for both static load cases and modes as GageMap contains only basic shell element theory. Output split between multiple files (/CONFIG,FSPLIT) is also supported, supply only the main RST (.rst) file to the converter input.

Both top/upper and bottom/lower surface element results for shell elements are required.  Results at other locations (mid for example) are not permitted.

While the geometry for both the CDB and RST files must be consistent, it is not required to supply output or geometry for the full model. For example, output for only a subset of the model with a full model CDB is supported or a partial CDB for a full output is also supported. In the former case the geometry will be as defined in the CDB file while only a subset (those nodes/elements with results in the RST file) of the model will have results defined. In the latter case the geometry will be as defined in the CDB file with node/element results for those nodes/elements not in the CDB file ignored.

## Converter Options

- **Average Nodes for External Faces Only:** Mimics POWERGRAPHICS on or off within ANSYS.  If selected, this option will produce a model with the imported strains and stress from the modes and static load cases equivalent to having the POWERGRAPHICS ANSYS option ON. An exception is that GageMap considers any element on the surface if it has a free face, whereas ANSYS considers any element on the surface that has a free edge.
- **Do NOT Load STATIC Load Stresses and Strains:** If any RST files contain static load cases with strain and stress solutions, then selecting this option will store static load cases in the GageMap SDR file without the ANSYS strain and stress values. This will force GageMap to calculate its own strain and stress values for the model.
- **Do NOT Load DYNAMIC Stresses and Strains:** If any RST files contain modes with strain and stress solutions, then selecting this option will store modes in the GageMap SDR file without the ANSYS strain and stress values. This will force GageMap to calculate its own strain and stress values for the model.
- **Load Cyclic Symmetry Solution:** Selecting this option will allow the converter to extract the cyclic symmetry solution. If this option is selected and the model is not valid for cyclic symmetry, the converter will error and quit. If this option is not selected and the model is valid for cyclic symmetry, the converter will process the geometry as non-cyclic.
- **Use First-Order Face Types for Elements:** This option forces the converter to use first-order (linear) face types for elements which are defined with second order (parabolic) face types. This will effect how strains and stresses are computed for faces only (sensor strain and stress ratios may be subsequently affected also). If the model contains parabolic elements and the GageMap computed stress distribution is non-smooth or not what as expected, reconvert the model with this option selected.
- **Maintain Local Coordinate System (Strains/Stresses):** Enabling this option will retain the element results in the coordinate system as defined by the ESYS property. By default all element results are transformed into the global Cartesian coordinate system and then averaged at the nodes.
