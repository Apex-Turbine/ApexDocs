# SGA File Format

> [!IMPORTANT]
> **End-User Format License Notice:** All APEX file formats and schemas (including `.sga` and `.sdr`) are provided strictly for internal end-user use with authorized APEX software and cannot be used for commercial means unless explicitly authorized by APEX through formal written agreement. See the **[Software License Agreement](../../Release%20Policies/software-license-agreement.md)**.

The strain gage file format is a text file containing the necessary mapping information for all supported sensors. The format is text and can be created or modified easily outside of GageMap. In addition to the sensor mapping information, additional information relating to the mapping domain can be present. For tip timing sensors, this would be the definition of the blade tip.

The following information is required to completely define a strain gage:

> 1. Keyword “Single”. Must be the first entry defining a strain gage. Currently only uniaxial strain gages are supported.
> 2. Gage name. Unique name that cannot contain any spaces.
> 3. Gage centroid X location in global Cartesian coordinates. Must be in model units.
> 4. Gage centroid Y location in global Cartesian coordinates. Must be in model units.
> 5. Gage centroid Z location in global Cartesian coordinates. Must be in model units.
> 6. Gage sensing direction vector, *i* component.
> 7. Gage sensing direction vector, *j* component.
> 8. Gage sensing direction vector, *k* component.
> 9. Gage size in the sensing direction, model units.
> 10. Gage size in the transverse direction, model units.

The gage sensing direction vector, items 6-8 should form a unit vector describing the sensing direction in the global Cartesian coordinate system.

  

The following information is required to completely define a tip timing (spot) sensor:

> 1. Keyword “NSMS_Spot”. Must be the first entry defining a tip timing sensor. Currently only spot probes are supported.
> 2. Sensor name. Unique name that cannot contain any spaces.
> 3. Sensor centroid X location in global Cartesian coordinates. Must be in model units.
> 4. Sensor centroid Y location in global Cartesian coordinates. Must be in model units.
> 5. Sensor centroid Z location in global Cartesian coordinates. Must be in model units.
> 6. Sensor sensing direction vector, *i* component.
> 7. Sensor sensing direction vector, *j* component.
> 8. Sensor sensing direction vector, *k* component.
> 9. Beam width, model units. (for visualization purposes only)
> 10. Beam depth, model units. (Not used)

The sensor sensing direction vector, items 6-8 should form a unit vector describing the sensing direction in the global Cartesian coordinate system and should align with the global direction vector describing the rotation direction.

  

The “Blade Tip” is defined using a combination of two properties:  “Rotation” and “Edges”. The Rotation is defines as follows:

> 1. Keyword “Blade_Tip”. Must be the first entry.
> 2. “Rotation”. Must be the second entry.
> 3. Number of element/face edges that define the tip.
> 4. Cyclic coordinate system axial direction vector, *i* component.
> 5. Cyclic coordinate system axial direction vector, *j* component.
> 6. Cyclic coordinate system axial direction vector, *k* component.
> 7. Cyclic coordinate system radial direction vector, *i* component.
> 8. Cyclic coordinate system radial direction vector, *j* component.
> 9. Cyclic coordinate system radial direction vector, *k* component.
> 10. Cyclic coordinate system tangential direction vector, *i* component.
> 11. Cyclic coordinate system tangential direction vector, *j* component.
> 12. Cyclic coordinate system tangential direction vector, *k* component.

The “Edges” are defined as follows:

> 1. Keyword “Blade_Tip”. Must be the first entry.
> 2. “Edges”. Must be the second entry.
> 3. Node labels defining the tip

Line #3 is repeated as necessary until all edges defining the tip are entered.

  

The example below contains both a strain gage definition and a spot probe definition as well as the necessary lines to define the blade tip:

`NSMS_Spot SpotLE  8.63031472e-001  5.94031950e+000  1.03683951e+001   1.00000000e+000  0.00000000e+000  0.00000000e+000   1.00000000e-002  0.00000000e+000  00`

`Single    Ga      6.22341877e-001  4.64931487e+000  1.03975449e+001   8.57281557e-001  1.29074460e-004  5.14847856e-001   6.30000000e-002  6.30000000e-002  00`

`Blade_Tip Rotation 7.80000000e+001  0.00000000e+000  0.00000000e+000  1.00000000e+000   0.00000000e+000  1.00000000e+000  0.00000000e+000   1.00000000e+000  0.00000000e+000  0.00000000e+000`

`Blade_Tip Edges   1.00430000e+004  1.00420000e+004   1.00400000e+004  1.00390000e+004   1.00410000e+004  1.00400000e+004   1.00420000e+004  1.00410000e+004   1.00380000e+004  1.00370000e+004   1.00390000e+004  1.00380000e+004`

`Blade_Tip Edges   1.00370000e+004  1.09530000e+004   1.09530000e+004  1.51940000e+004   1.51940000e+004  1.51930000e+004   1.51930000e+004  1.51920000e+004   1.51920000e+004  1.51910000e+004   1.51910000e+004  1.51900000e+004`

`Blade_Tip Edges   1.51900000e+004  1.51890000e+004   1.51890000e+004  1.51880000e+004   1.51880000e+004  1.51870000e+004   1.51870000e+004  1.51860000e+004   1.51860000e+004  1.51850000e+004   1.51850000e+004  1.51840000e+004`

`Blade_Tip Edges   1.51840000e+004  1.51830000e+004   1.51830000e+004  1.51820000e+004   1.51820000e+004  1.51810000e+004   1.51810000e+004  1.51800000e+004   1.51800000e+004  1.51790000e+004   1.51790000e+004  1.51780000e+004`

`Blade_Tip Edges   1.51780000e+004  1.51770000e+004   1.51770000e+004  1.51760000e+004   1.51760000e+004  1.51750000e+004   1.51750000e+004  1.51740000e+004   1.51740000e+004  1.51730000e+004   1.51730000e+004  1.51720000e+004`

`Blade_Tip Edges   1.51720000e+004  1.51710000e+004   1.51710000e+004  1.51700000e+004   1.51700000e+004  1.51690000e+004   1.51690000e+004  1.51680000e+004   1.51680000e+004  1.51670000e+004   1.51670000e+004  1.51660000e+004`

`Blade_Tip Edges   1.51660000e+004  1.51650000e+004   1.51650000e+004  1.51640000e+004   1.51640000e+004  1.51630000e+004   1.51630000e+004  1.51620000e+004   1.51610000e+004  1.06540000e+004   1.51620000e+004  1.51610000e+004`

`Blade_Tip Edges   1.63600000e+004  1.63590000e+004   1.63610000e+004  1.63600000e+004   1.63620000e+004  1.63610000e+004   1.63630000e+004  1.63620000e+004   1.63640000e+004  1.63630000e+004   1.63650000e+004  1.63640000e+004`

`Blade_Tip Edges   1.63660000e+004  1.63650000e+004   1.63670000e+004  1.63660000e+004   1.63680000e+004  1.63670000e+004   1.63690000e+004  1.63680000e+004   1.63700000e+004  1.63690000e+004   1.63710000e+004  1.63700000e+004`

`Blade_Tip Edges   1.63720000e+004  1.63710000e+004   1.63730000e+004  1.63720000e+004   1.63740000e+004  1.63730000e+004   1.63750000e+004  1.63740000e+004   1.63760000e+004  1.63750000e+004   1.63770000e+004  1.63760000e+004`

`Blade_Tip Edges   1.63780000e+004  1.63770000e+004   1.63790000e+004  1.63780000e+004   1.63800000e+004  1.63790000e+004   1.63810000e+004  1.63800000e+004   1.63820000e+004  1.63810000e+004   1.63830000e+004  1.63820000e+004`

`Blade_Tip Edges   1.63840000e+004  1.63830000e+004   1.63850000e+004  1.63840000e+004   1.63860000e+004  1.63850000e+004   1.84130000e+004  1.63860000e+004   1.06540000e+004  1.84060000e+004   1.82710000e+004  1.84170000e+004`

`Blade_Tip Edges   1.84060000e+004  1.82720000e+004   1.82720000e+004  1.82710000e+004   1.84140000e+004  1.84130000e+004   1.84170000e+004  1.81650000e+004   1.81640000e+004  1.84140000e+004   1.81650000e+004  1.81640000e+004`
