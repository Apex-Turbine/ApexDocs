# Mapping Sensors Between Similar Geometry

GageMap scripting contains the ability (see the command geom_remap) to map strain sensors between any two similar geometries. The geometries may have different nodal coordinates that would be from a non-linear static analysis. The function operates by maintaining the natural coordinates of the gage centroid and corners between any two geometries. The natural coordinates are computed for the center of each gage mapped to the base geometry then these same natural coordinates are maintained on the new geometry. This defines the location of the gage on the new geometry. Similarly, for each corner of the gage mapped to the base geometry the natural coordinates are computed then these same natural coordinates are maintained on the new geometry. This defines the sensing direction vector.
Limitations/Restrictions/Assumptions:

1. The following (3-D) element types are supported:

  > - Linear tetrahedral - 4 nodes.
  > - Linear wedge - 6 nodes.
  > - Linear hexahedral - 8 nodes.
  > - Quadratic tetrahedral - 10 nodes.
  > - Quadratic wedge - 15 nodes.
  > - Quadratic hexahedral - 20 nodes.
2. The finite element properties in both models are required to be identical. The following will be verified:

  > - Number of nodes.
  > - Node indices/labels.
  > - Number of elements.
  > - Element indices/labels.
  > - Element connectivity.
  > - Number of faces.
3. The curvature of the geometry between SDR files is not significant such that the new gage positions on the “to_filename” SDR file will not map.
4. Only strain gage sensors are supported. All other sensor types will be ignored.
5. Only gages that are mapped will be transformed.

  

The following example illustrates the process of mapping the sensors saved with the SDR file “TrainingModel_2000RPM.sdr” to SDR files with the following non-linear static analyses at RPM’s of; 10k, 20k, 30k and 40k:

> `local fromFile = "TrainingModel_2000RPM.sdr";`
>
> `local toFile = "TrainingModel_10000RPM.sdr";`
>
> `local sgaFileName = toFile .. ".sga";`
>
> `sensors.geom_remap(fromFile,toFile,sgaFileName);`

  

> `local toFile = "TrainingModel_20000RPM.sdr";`
>
> `local sgaFileName = toFile .. ".sga";`
>
> `sensors.geom_remap(fromFile,toFile,sgaFileName);`

  

> `local toFile = "TrainingModel_30000RPM.sdr";`
>
> `local sgaFileName = toFile .. ".sga";`
>
> `sensors.geom_remap(fromFile,toFile,sgaFileName);`

  

> `local toFile = "TrainingModel_40000RPM.sdr";`
>
> `local sgaFileName = toFile .. ".sga";`
>
> `sensors.geom_remap(fromFile,toFile,sgaFileName);`
