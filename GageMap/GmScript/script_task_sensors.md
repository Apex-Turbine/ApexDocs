# Sensors Functions for Scripting

Using the GM.fatigue() function group, the following functions are available:

- [name(sensor_index)](#namesensor_index)
- [open(filename)](#openfilename)
- [save(filename)](#savefilename)
- [report_detail](#report_detail)
- [report_summary](#report_summary)
- [mapping_prefs](#mapping_prefs)
- [reporting_prefs](#reporting_prefs)
- [cyc_ratio](#cyc_ratio)
- [geom_remap](#geom_remap)
- [gage_strain](#gage_strain)
- [gage_stress](#gage_stress)
- [gage_misplacement_coeffs](#gage_misplacement_coeffs)
- [gage_perturb](#gage_perturb)
- [gage_perturb_X](#gage_perturb_x)
- [gage_perturb_Y](#gage_perturb_y)
- [gage_perturb_Theta](#gage_perturb_theta)
- [misplacement_prefs](#misplacement_prefs)

## name(sensor_index)

**Description:**

Retrieves the name of the sensor based on the index.

**Arguments:**

- sensor_index: Index of the sensor to retrieve information

**Returns:**

The name of the requested sensor, STRING

**Example:**

> `sens = GM.sensors()`
>
> `name = sensors.name(1)`

## open(filename)

**Description:**

Loads a SGA file for use with the model.

**Arguments:**

- filename: Full path and file name, STRING

**Example:**

> `infolder = "c:/tmp"`
>
> `sens = GM.sensors()`
>
> `sens.open(infolder .. "/example.sga")`

## save(filename)

**Description:**

Saves an SGA file for all the active and mapped sensors to a file.

**Arguments:**

- filename: File name (without path), STRING

**Example:**

> `infolder = "c:/tmp"`
>
> `sens = GM.sensors()`
>
> `sens.save("gages.sga")`

## report_detail(sensor_name, filename, format)

**Description:**

Saves a Detailed Sensor Report.

**Arguments:**

- sensor_name: The name of the sensor for the detailed report, STRING
- filename: File name (without path) for the file to be saved, STRING
- format: format of the report ("PDF" / "TXT" / "HTML"), STRING

**Example:**

> `sens = GM.sensors()`
>
> `sens.report_detail("gage01", "sensors.pdf", "PDF")`

## report_summary(filename, format)

**Description:**

Saves a Sensor Summary Report.

**Arguments:**

- filename: File name (without path) for the file that should be saved out, STRING
- format: format of the report ("PDF" / "TXT", "HTML"), STRING

**Example:**

> `sens = GM.sensors()`
>
> `sens.report_summary("summary.html", "HTML")`

## mapping_prefs(dir_tol, normal_tol)

**Description:**

Sets the sensors mapping preferences.

**Arguments:**

- dir_tol: Direction tolerance, FLOAT
- normal_tol: Normal tolerance, FLOAT

**Example:**

> `sens = GM.sensors()`
>
> `sens.mapping_prefs(0.1, 0.2)`

## reporting_prefs(strain_type, stress_type, strain_threshold, [report_group])

**Description:**

Sets the reporting preferences for use with sensor reports and optimization options.

**Arguments:**

- strain_type = reporting strain type, INTEGER

  > - 1  - Overall Max (Eoa = max(Eeqv or abs(E1) or abs(E3) or Ex or Ey or Ez or Exy or Eyz or Ezx))
  > - 2  - Max Invariant (Einv = max(Eeqv or abs(E1) or abs(E3)))
  > - 3  - Max Component (Ec = max(Ex or Ey or Ez or Exy or Eyz or Ezx))
  > - 4  - Equivalent (Eeqv)
  > - 5  - Max Principals (E1,3 = max(abs(E1)or abs(E3))
  > - 6  - X Component (Ex)
  > - 7  - Y Component (Ey)
  > - 8  - Z Component (Ez)
  > - 9  - XY Shear (Exy)
  > - 10 - YZ Shear (Eyz)
  > - 11 - ZX Shear (Ezx)
- stress_type = reporting stress type, INTEGER

  > - 1  - Overall Max (Soa = max(Svm or abs(S1) or abs(S3) or Sx or Sy or Sz or Sxy or Syz or Szx))
  > - 2  - Max Invariant (Sinv = max(Svm or abs(S1) or abs(S3)))
  > - 3  - Max Component (Sc = max(Sx or Sy or Sz or Sxy or Syz or Szx))
  > - 4  - Von Mises (Svm)
  > - 5  - Max Principals (S1,3 = max(abs(S1) or abs(S3))
  > - 6  - X Component (Sx)
  > - 7  - Y Component (Sy)
  > - 8  - Z Component (Sz)
  > - 9  - XY Shear (Sxy)
  > - 10 - YZ Shear (Syz)
  > - 11 - ZX Shear (Szx)
- strain_threshold = strain threshold, FLOAT (0.0 - 1.0)
- report_group (OPTIONAL) = normalize to group name, STRING

**Example:**

> `sens = GM.sensors()`
>
> `sens.reporting_prefs(5, 5)`

## cyc_ratio(sensor_name, mode_index, phase, search_variable, norm)

**Description:**

Performs a phase sweep of the sensor response. Applies only to complex mode shapes.

**Arguments:**

- sensor_name, STRING
- mode_index, INTEGER
- phase, phase increment (degrees), FLOAT
- search_variable, INTEGER

  > - Displacement/Rotation Variables
  >
  >   > - 1 - Ux
  >   > - 2 - Uy
  >   > - 3 - Uz
  >   > - 4 - Usum
  >   > - 5 - Rx
  >   > - 6 - Ry
  >   > - 7 - Rz
  >   > - 8 - Rsum
  > - Strain/Stress Variables
  >
  >   > - 9 - eeqv
  >   > - 10 - ep1
  >   > - 11 - ex
  >   > - 12 - ey
  >   > - 13 - ez
  >   > - 14 - exy
  >   > - 15 - eyz
  >   > - 16 - ezx
  >   > - 17 - seqv
  >   > - 18 - sp1
  >   > - 19 - sx
  >   > - 20 - sy
  >   > - 21 - sz
  >   > - 22 - sxy
  >   > - 23 - syz
  >   > - 24 - szx
- norm = Mass normalization, (1=true, 0=false), INTEGER

**Returns:**

Returns an object which can be accessed for seven data members:

> 1. sensorLabel :   The name of the sensor( same as arg1 above )
> 2. sensorValue :   The numerator value.
> 3. sensorPhase :   The phase of the numerator
> 4. sensorRatio :   The numerator divided by the denominator.
> 5. nodePhase   :   The phase of the denominator
> 6. nodeValue   :   The denominator value, determined by search variable( arg4 )
> 7. nodeLabel   :   The original index of the node

Any of the above data members may be accessed using the standard C++ method of a dot (.) followed by the member.

**Example:**

> `sens = GM.sensors()`
>
> `sens.cyc_ratio("sgage0A", 1, 2.2, 14, 1)`

## geom_remap(from_filename, to_filename, (optional) SGA_filename)

**Description**

Remaps all strain gage sensors from one geometry to another by maintaining the relative position and direction vector from the original gage definition. It does NOT permit the strain gage to change size. This is intended to re-map gages across 2 similar geometries, i.e., gages defined on a statically deformed geometry but desire gage locations on the non-statically deformed model. Execution of the command without the third argument results in the generation of an SDR file with the same name as "to_filename" appended with "_geomRemap" containing the same sensors defined in "from_filename". The file is placed in the same location as "to_filename". If the third argument is used then no SDR file is generated.

**Theory:**

Determine the isoparametric coordinates for the center & corners of each gage saved in the SDR file "from_filename". Enforce these same locations on the SDR file "to_filename".

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
3. The curvature of the geometry between SDR files is not significant such that the new gage positions on the "to_filename" SDR file will not map.
4. Only strain gage sensors are supported. All other sensor types will be ignored.
5. All gages resident in the SDR "from_filename" are re-mapped.

**Arguments:**

- from_filename: File name of the SDR file that contains the sensors you wish to remap, STRING
- to_filename: File name of the SDR file which contains the new geometry. If last argument, the sensor definitions will be saved to this file as described above, STRING
- SGA_filename(optional): If this Argument is included, the sensor definitions will be written to this SGA file name in lieu of the SDR file, STRING

**Example:**

> `sens = GM.sensors()`
>
> `input_dir = "c:/tmp/"`
>
> `output_dir = "c:/out/"`
>
> `from_file = input_dir .. "old_geom_with_sensors.sdr"`
>
> `to_file = input_dir .. "new_geom.sdr"`
>
> `out_sga = output_dir .. "new_sens.sga"`
>
> `sens.geom_remap(from_file, to_file)`
>
> `sens.geom_remap(from_file, to_file, out_sga)`

## gage_strain(sensor_index, mode_type, mode_index)

**Description**

> Retrieves a 3-element vector containing the normalized strains.

**Arguments:**

- sensor_index, INTEGER
- - **mode_type, INTEGER**: - 1  - DYNAMIC
  - 2  - STATIC
- mode_index, INTEGER

**Returns:**

Returns an object which can be accessed for 3 data members:

> 1. eX  :   Normalized strain in the sensing direction.
> 2. eY  :   Normalized strain in the transverse direction.
> 3. eXY :   Normalized shear strain.

Any of the above data members may be accessed using the standard C++ method of a dot (.) followed by the member.

**Example:**

> `sens = GM.sensors()`
>
> `strain = sens.gage_strain(2, 1, 3)`
>
> `print(strain.eX)`

## gage_stress(sensor_index, mode_type, mode_index)

**Description**

> Retrieves a 10-element vector containing the normalized stress, for given input.

**Arguments:**

- sensor_index, INTEGER
- - **mode_type, INTEGER**: - 1  - DYNAMIC
  - 2  - STATIC
- mode_index, INTEGER

**Returns:**

Returns an object which can be accessed for 10 data members:

- eX       :   Stress ratio.
- eY       :   Uniaxiality measure.
- sigmaX   :   Gage stress along the sensing direction normalized by the maximum stress.
- sigmaY   :   Transverse stress normalized by the maximum stress.
- tauXY    :   Shear stress normalized by the maximum stress.
- vonmises :   Von Mises stress normalized by the maximum stress.
- sigmaMax :   Maximum principal stress normalized by the maximum stress.
- sigmaMin :   Minimum principal stress normalized by the maximum stress.
- tauMax   :   Maximum shear stress normalized by the maximum stress.
- theta    :   Angle to the maximum principal stress direction.

Any of the above data members may be accessed using the standard C++ method of a dot (.) followed by the member.

**Example:**

> `sens = GM.sensors()`
>
> `stress = sens.gage_stress(1, 1, 5)`
>
> `print(stress.sigmaX)`

## gage_misplacement_coeffs(sensor_index, mode_type, mode_index)

**Description**

> Retrieves a 7-element vector containing the misplacement coefficients and errors, for given input.

**Arguments:**

- sensor_index, INTEGER
- - **mode_type, INTEGER**: - 1  - DYNAMIC
- mode_index, INTEGER

**Returns:**

Returns an object which can be accessed for 7 data members:

- A      :   Misplacement coefficient A.
- B      :   Misplacement coefficient B.
- C      :   Misplacement coefficient C.
- D      :   Misplacement coefficient D.
- eRSqrd :   Misplacement error R-Squared.
- eSSE   :   Misplacement error SSE.
- eRMSE  :   Misplacement error RMSE.

Any of the above data members may be accessed using the standard C++ method of a dot (.) followed by the member.

**Example:**

> `sens = GM.sensors()`
>
> `coeffs = sens.gage_misplacement_coeffs(2, 1, 5)`
>
> `print(coeffs.eRSqrd)`

## gage_misplacement_maxmins(sensor_index, mode_type, mode_index)

**Description**

> Retrieves a 7-element vector containing the maximum and minimum misplacement offset values , for given input.

**Arguments:**

- sensor_index, INTEGER
- - **mode_type, INTEGER**: - 1  - DYNAMIC
- mode_index, INTEGER

**Returns:**

Returns an object which can be accessed for 7 data members:

- norm  : Normalized nominal
- - **max**: - maxNorm : Normalized maximum
  - maxXoffset : Maximum normalized offset X
  - maxYoffset : Maximum normalized offset Y
  - maxToffset : Maximum normalized offset Theta
- - **min**: - minNorm : Normalized minimum
  - minXoffset : Minimum normalized offset X
  - minYoffset : Minimum normalized offset Y
  - minToffset : Minimum normalized offset Theta

Any of the above data members may be accessed using the standard C++ method of a dot (.) followed by the member.

**Example:**

> `sens = GM.sensors()`
>
> `maxmins = sens.gage_misplacement_maxmins(1, 1, 7)`
>
> `print(maxmins.max.maxXoffset)`

## gage_perturb(sensor_index, deltaX, deltaY, deltaTheta)

**Arguments:**

- sensor_index, INTEGER
- deltaX, FLOAT
- deltaY, FLOAT]
- deltaTheta, FLOAT

**Returns:**

Returns wheather the mapping is successful or not, for given inputs

**Example:**

> `sens = GM.sensors()`
>
> `status = sens.gage_perturb(1, 0.00056, 0.00035, 0.000234)`
>
> `print(status)`

## gage_perturb_X(sensor_index, deltaX)

**Description**

> Sets delta X to the input given by user and sets delta Y and delta Theta to zero's.

**Arguments:**

- sensor_index, INTEGER
- deltaX, FLOAT

**Returns:**

Returns wheather the mapping is successful or not, for given input delta X.

**Example:**

> `sens = GM.sensors()`
>
> `status = sens.gage_perturb_X(1, 0.000234)`
>
> `print(status)`

## gage_perturb_Y(sensor_index, deltaY)

**Description**

> Sets delta Y to the input given by user and sets delta Z and delta Theta to zero's.

**Arguments:**

- sensor_index, INTEGER
- deltaY, FLOAT

**Returns:**

Returns wheather the mapping is successful or not, for given input delta X.

**Example:**

> `sens = GM.sensors()`
>
> `status = sens.gage_perturb_Y(1, 0.00035)`
>
> `print(status)`

## gage_perturb_Theta(sensor_index, deltaTheta)

**Description**

> Sets delta theta to the input given by user and sets delta X and delta Y to zero's.

**Arguments:**

- sensor_index, INTEGER
- deltaTheta, FLOAT

**Returns:**

Returns wheather the mapping is successful or not, for given input delta .

**Example:**

> `sens = GM.sensors()`
>
> `status = sens.gage_perturb_Theta(1, 0.000234)`
>
> `print(status)`

## misplacement_prefs(deltaX, deltaY, deltaTheta)

**Description**

> It can be used as a get function or set function.
> No need to pass any arguments, in case of get function. It just returns the structure that were set before.
> In case of set function, it sets the values for sensor reports
>
> These arguments are used for set function.

**Arguments:**

- deltaX, FLOAT
- deltaY, FLOAT]
- deltaTheta, FLOAT

**Returns:**

Returns an object which can be accessed for 3 data members:

> 1. deltaX  :   MIsplacement offset x.
> 2. deltaY  :   MIsplacement offset Y.
> 3. deltaTheta :   MIsplacement offset Theta.

Any of the above data members may be accessed using the standard C++ method of a dot (.) followed by the member.

**Example:**

> `sens = GM.sensors()`
>
> `m = sensor.misplacement_prefs()`
>
> `print(m.deltaX, m.deltaY, m.deltaTheta)`
>
> `m = sensor.misplacement_prefs(0.0023, 0.0045, 0.0082)`
