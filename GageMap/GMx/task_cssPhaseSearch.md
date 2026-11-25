# Cyclic Symmetry Solutions

OverviewCyclic Symmetry is a means of representing system mode shapes by only modeling a single sector. This can greatly expedite solutions and post-processing.

GageMap supports the use of cyclic symmetry models which were created in ANSYS or ABAQUS. These features are only available when using a model which was converted using the cyclic symmetry flag during the conversion process. Upon conversion, GM stores cyclic symmetry results as a complex variable such that: the basic sector solution for the first mode in the mode pair is mapped as the REAL coefficient and the duplicate sector solution for the first mode in the mode pair is mapped as the IMAGINARY coefficient. The duplicate mode information is ignored. See conversion report. Cyclic symmetry modes in GageMap are stored as complex modes

GageMap allows for Strain Gage optimization and cyclic phase search (similar to ANSYS). In addition to nodal variables, strain gages can also be swept over phase.

## Complex Modes

Two representations:
- Individual modes (default)
- Complex modes

> - Real coefficients assigned to 1st mode
> - Imaginary coefficients assigned to 2nd mode
> - Both modes have same frequency
> - Invariants available but computed for each individual mode

- - **Magnitude & phase**: - Single mode, magnitude
  - Phase available via “Model Export”
  - Magnitude, 1st mode
  - Phase, 2nd mode
  - Invariants of vectors and tensors unavailable
  - This representation is required for optimization on cyclic modes
- - **Change format via Options -> Complex Modes**: - Use as complex (magnitude & phase)
  - Use as individual modes
