# SDRFM Functions for Scripting

Using the GM.sdrfm() function group, the following functions are available:

- [open(filename)](#openfilename)
- [save(filename)](#savefilename)
- [load_shapes](#load_shapes)
- [load_sensors_sga](#load_sensors_sga)
- [load_sensors_sdr](#load_sensors_sdr)
- [load_groups](#load_groups)
- [nshapes()](#nshapes)
- [nmodes()](#nmodes)
- [nloads()](#nloads)
- [ngages()](#ngages)
- [ngroups()](#ngroups)
- [group_info](#group_info)
- [mgage_info](#mgage_info)
- [nnodes()](#nnodes)
- [node(index)](#nodeindex)
- [mshape_info](#mshape_info)
- [mlist_freq](#mlist_freq)
- [max_phase](#max_phase)
- [export_shape](#export_shape)
- [export_nshapes](#export_nshapes)
- [export_vmode](#export_vmode)
- [export_cssmode](#export_cssmode)
- [export_arithadd](#export_arithadd)
- [export_arithdone](#export_arithdone)
- [export_removeshape](#export_removeshape)
- [export_trim](#export_trim)
- [export_expand](#export_expand)
- [export_expand_clr](#export_expand_clr)
- [export_expand_opt](#export_expand_opt)
- [export_model](#export_model)
- [load_GBF](#load_gbf)
- [save_GBF](#save_gbf)

## open(filename)

**Description:**

Load an SDR Model as a project for the file manager. Only one project/SDR model may be opened in a session. Subsequent attempts to open additional SDR files will be ignored.

**Arguments:**

- filename: Full path and file name, STRING

**Example:**

> `infolder = "c:/tmp"`
>
> `sdrfm = GM.sdrfm()`
>
> `sdrfm.open(infolder .. "/example.sdr")`

## save(filename)

**Description:**

Save the current SDR Model. Saves the current SDR model with all shapes and sensors that are currently loaded.

**Arguments:**

- filename: File name (without path), STRING

**Example:**

> `sdrfm = GM.sdrfm()`
>
> `sdrfm.save("new_file.sdr")`

## load_shapes(filename)

**Description:**

Load shapes into the file manager from an existing SDR file.

**Arguments**

- filename: Full path and name, STRING

**Example**

> `infolder = "c:/tmp"`
>
> `sdrfm = GM.sdrfm()`
>
> `sdrfm.load_shapes(infolder .. "/example.sdr")`

## load_sensors_sga(filename)

**Description:**

Load sensors into the file manager from an existing SGA file.

**Arguments:**

- filename: Full path and name, STRING

**Example:**

> `infolder = "c:/tmp"`
>
> `sdrfm = GM.sdrfm()`
>
> `sdrfm.load_sensors_sga(infolder .. "/example.sga")`

## load_sensors_sdr(filename)

**Description:**

Load sensors into the file manager from an existing SDR file.

**Arguments:**

- filename: Full path and name, STRING

**Example:**

> `infolder = "c:/tmp"`
>
> `sdrfm = GM.sdrfm()`
>
> `sdrfm.load_sensors_sdr(infolder .. "/example.sdr")`

## load_groups(filename)

**Description:**

Load groups into the file manager from an existing GRP file.

**Arguments:**

- filename: Full path and name, STRING

**Example:**

> `infolder = "c:/tmp"`
>
> `sdrfm = GM.sdrfm()`
>
> `sdrfm.load_groups(infolder .. "/example.grp")`

## nshapes()

**Description:**

Query the SDR file manager for the total number of shapes. This includes both static and dynamic shapes.

**Returns:**

The current number of shapes in the file manager.

**Example:**

> `sdrfm = GM.sdrfm()`
>
> `num = sdrfm.nshapes()`

## nmodes()

**Description:**

Query the SDR file manager for the total number of dynamic shapes.

**Returns:**

The current number of dynamic modes in the file manager.

**Example:**

> `sdrfm = GM.sdrfm()`
>
> `num = sdrfm.nmodes()`

## nloads()

**Description:**

Query the SDR file manager for the total number of static shapes.

**Returns:**

The current number of static loads in the file manager.

**Example:**

> `sdrfm = GM.sdrfm()`
>
> `num = sdrfm.nloads()`

## ngages()

**Description:**

Query the SDR file manager for the total number of sensors.

**Returns:**

The current number of gages in the file manager.

**Example:**

> `infolder = "c:/tmp"`
>
> `sdrfm = GM.sdrfm()`
>
> `sdrfm.open(infolder .. "/example.sdr")`
>
> `gagecount = sdrfm.ngages()`

## ngroups()

**Returns:**

The number of groups currently loaded in the file manager.

**Example:**

> `infolder = "c:/tmp"`
>
> `sdrfm = GM.sdrfm()`
>
> `sdrfm.load_groups(infolder .. "/groupFile.grp")`
>
> `groupCount = sdrfm.ngroups()`

## group_info(index)

**Description:**

Query the SDR file manager for information on a particular group. Name, number of nodes and boolean.

**Arguments:**

- index: Index of the desired group, INTEGER

**Returns:**

- A structure containing information about a group. This structure includes:

  > - name: name of the group, STRING
  > - nnodes: How many nodes belong to the group, INTEGER
  > - opcode: The and/or opcode of the group, INTEGER

**Example:**

> `infolder = "c:/tmp"`
>
> `sdrfm = GM.sdrfm()`
>
> `sdrfm.open(infolder .. "/example.sdr")`
>
> `group = sdrfm.group(1)`
>
> `print("group: ", group.name)`

## gage_info(index)

**Description:**

Query the SDR file manager for information on a particular sensor.

**Arguments:**

- index: Index of desired sensor, INTEGER

**Returns:**

An object containing the following items:

> - name - The name of the gage, STRING
> - type - The gage type, INTEGER
>
>   > - 1 - Strain Gage
>   > - 2 - ROS 3x90
>   > - 3 - ROS 3x135
>   > - 4 - Accelerometer
>   > - 5 - NSMS Spot
>   > - 6 - NSMS Cap
>   > - 7 - NSMS Line
>   > - 8 - NSMS Beam
> - pos
>
>   > - x - X coordinate, FLOAT
>   > - y - Y coordinate, FLOAT
>   > - z - Z coordinate, FLOAT

**Example:**

> `infolder = "c:/tmp"`
>
> `sdrfm = GM.sdrfm()`
>
> `sdrfm.open(infolder .. "/example.sdr")`
>
> `gage1_info = sdrfm.gage_info(1)`
>
> `name = gage1_info.name`
>
> `type = gage1_info.type`
>
> `xPos = gage1_info.pos.x`

## nnodes()

**Returns:**

The number of nodes in the loaded model.

**Example:**

> `infolder = "c:/tmp"`
>
> `sdrfm = GM.sdrfm()`
>
> `sdrfm.open(infolder .. "/example.sdr")`
>
> `nodecount = sdrfm.nnodes()`

## node(index)

**Arguments:**

- index: Index of the desired node.

**Returns:**

- A structure containing information about a node. This structure includes:

  > - id: original index of the node
  > - pos.x, pos.y, pos.z: geometric coordinates
  > - normal.i, normal.j, normal.k: Node normals

**Example:**

> `infolder = "c:/tmp"`
>
> `sdrfm = GM.sdrfm()`
>
> `sdrfm.open(infolder .. "/example.sdr")`
>
> `node = sdrfm.node(100)`
>
> `print("x: ", node.pos.x, " i: ", node.normal.i)`

## shape_info(index,load)

**Arguments:**

- index: Index of the desired shape. (INT)
- load: Is this shape a load or mode. (BOOL)

**Returns:**

- A structure containing information of the shape. This structure includes:

  > - sdrnum: Shape SDR number
  > - nNodes: number of nodes within the shape
  > - amp: mode amplitude
  > - freq: mode frequency
  > - iscomplex: Is this a complex shape?

**Example:**

> `infolder = "c:/tmp"`
>
> `sdrfm = GM.sdrfm()`
>
> `sdrfm.open(infolder .. "/example.sdr")`
>
> `shape = sdrfm.shape(0, false)`
>
> `print("SDRNUM: ", shape.sdrnum, " nNodes: ", shape.nNodes)`

## list_freq(shape type)

**Description:**

Lists frequencies of each mode. If cyclic, also lists the corresponding Nodal Diameter.

**Arguments:**

- **(OPTIONAL)** load: 0 = Dynamic Mode, 1 = Static Load, INTEGER

(The function defaults to Dynamic Modes)

**Returns:**

An object containing the following items:

> - Freq - A list of the modes frequencies.
> - NDD - A list of the modes Nodal Diameters if cyclic. If not cyclic, the value will be -1.

**Example:**

> `sdrfm = GM.sdrfm()`
>
> `sdrfm.open(infolder .. "/example.sdr")`
>
> `t = sdrfm.list_freq()`
>
> `mode_1_freq = t.Freq[1]`
>
> `mode_1_ndd = t.NDD[1]`

## max_phase(mode_index, phase, search_type)

**Description:**

Perform a phase sweep at the user desired phase angle to determine when a desired variable achieves either a maximum or minimum value.

**Arguments:**

- mode_index: Index of the dynamic mode, INTEGER
- phase: phase increment in degrees, FLOAT
- search_type: variable to search, INTEGER

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
  >   > - 10 - MaxPrinStrain
  >   > - 11 - ex
  >   > - 12 - ey
  >   > - 13 - ez
  >   > - 14 - exy
  >   > - 15 - eyz
  >   > - 16 - ezx
  >   > - 17 - seqv
  >   > - 18 - MaxPrinStress
  >   > - 19 - sx
  >   > - 20 - sy
  >   > - 21 - sz
  >   > - 22 - sxy
  >   > - 23 - syz
  >   > - 24 - szx

**Example:**

> `sdrfm = GM.sdrfm()`
>
> `max = sdrfm.max_phase(1, 1.0, 1)`

## export_shape(shape_index, real, imaginary, shape_type)

**Description:**

Add an existing shape to the exported model using REAL & IMAGINARY scalars.

**Arguments:**

- shape_index: shape to be exported by index, INTEGER
- real: real coefficient, FLOAT
- imaginary: imaginary coefficient, FLOAT
- shape_type: (0=modes, 1=loads), INTEGER

**Example:**

> `sdrfm = GM.sdrfm()`
>
> `sdrfm.export_shape(10, 1.0, -2.0, 1)`

## export_nshapes()

**Description:**

Query for the total number of shapes to be exported.

**Returns:**

Number of shapes in the exported model

**Example:**

> `sdrfm = GM.sdrfm()`
>
> `num = sdrfm.export_nshapes()`

## export_vmode(shape_index, search_type, phase, phase_id, mass_norm, info_mode)

**Description:**

Create a virtual mode shape for export. A virtual mode shape is one in which each active node is phase swept and the resulting maximum value and associated vectors & tensors are assigned to the node upon export. Therefore, each node may be at a different phase angle. Activating the "info_mode" results in an identical mode at the same frequency but contains the following in the displacement vector:  Ux = maximum value, Uy = phase angle, degrees. The remaining nodal values are set to zero. This permits access to the phase angle (animation, reporting, etc.) within the GUI. The "phase_id" should be used for those variables that do not exhibit a sinusoidal response as a function of the phase angle. These would be Usum, equivalent strain, max principal strain, Von Mises Stress, etc. Setting phase_id = 1 ensures the phase angle to lie between 0 & 180 degrees thus eliminating phase discontinuities. This is only available for complex mode shapes.

**Arguments:**

- shape_index: INTEGER
- search_type: INTEGER

  > - Displacement/Rotation variables
  >
  >   > - 1 - Ux
  >   > - 2 - Uy
  >   > - 3 - Uz
  >   > - 4 - Usum
  >   > - 5 - Rx
  >   > - 6 - Ry
  >   > - 7 - Rz
  >   > - 8 - Rsum
  > - Strain/Stress variables
  >
  >   > - 9 - eeqv
  >   > - 10 - MaxPrinStrain
  >   > - 11 - ex
  >   > - 12 - ey
  >   > - 13 - ez
  >   > - 14 - exy
  >   > - 15 - eyz
  >   > - 16 - ezx
  >   > - 17 - seqv
  >   > - 18 - MaxPrinStress
  >   > - 19 - sx
  >   > - 20 - sy
  >   > - 21 - sz
  >   > - 22 - sxy
  >   > - 23 - syz
  >   > - 24 - szx
- phase: phase angle increment in degrees, FLOAT
- phase_id: phase identification option, INTEGER

  > - 1 - Absolute value (first found)
  > - 2 - Absolute value (last found)
  > - 3 - Maximum value
  > - 4 - Minimum value
- mass_norm: mass normalization, (0=no, 1=yes), INTEGER
- info_mode: storage of additional information mode, (0=no, 1=yes), INTEGER

**Example:**

> `sdrfm = GM.sdrfm()`
>
> `sdrfm.export_vmode(5, 4, 5.0, 1, 1, 0)`

## export_cssmode(shape_index, phase, mass_norm, imaginary)

**Description:**

Expand the cyclic mode to the desired phase angle and optionally export the complimentary imaginary mode.

**Arguments:**

- shape_index: INTEGER
- phase: phase relationship in degrees, FLOAT
- mass_norm: mass normalization, (0=no, 1=yes), INTEGER
- imaginary storage of imaginary shape, (0=no, 1=yes), INTEGER

**Example:**

> `sdrfm = GM.sdrfm()`
>
> `sdrfm.export_cssmode(5, 200.0, 1, 1)`

## export_arithadd(shape_index, real_scale, imaginary_scale, shape_type)

**Description:**

Create a dynamic shape by combining (summing) existing shapes. Shapes can be combines using REAL and/or IMAGINARY scalars can be applied prior to summation, however, only REAL coefficients are available for static shapes.

**Arguments:**

- shape_index: INTEGER
- real_scale: real coefficient scale factor, FLOAT
- imaginary_scale: imaginary coefficient scale factor, FLOAT
- shape_type: (0=mode, 1=static), INTEGER

**Example:**

> `sdrfm = GM.sdrfm()`
>
> `sdrfm.export_arithadd(12,0.25, 0.25, 0)`

## export_arithdone()

**Description:**

Complete the summation and add the combined shape to the existing shape list in preparation for export.

**Example:**

> `sdrfm = GM.sdrfm()`
>
> `sdrfm.export_arithadd(12,0.25, 0.25, 0)`
>
> `sdrfm.export_arithdone()`

## export_removeshape(shape_index, shape_type)

**Description:**

Remove Shape. Once removed, the shapes are then re stacked in GageMap. It is not recommended to perform this within a for-loop.

**Arguments:**

- shape_index: INTEGER
- shape_type: (0=mode, 1=static), INTEGER

**Example:**

> `sdrfm = GM.sdrfm()`
>
> `sdrfm.export_arithadd(12,0.25, 0.25, 0)`
>
> `sdrfm.export_arithdone()`
>
> `sdrfm.export_removeshape(1,0)`

## export_trim(group, function)

**Description:**

Sets the groups function type to be used for trimming the model during export.

**Arguments:**

- group: Name of selected group, STRING
- function: group Boolean function, INTEGER

  > - 0 - Disabled
  > - 1 - AND
  > - 2 - OR
  > - 3 - NOT

**Example:**

> `sdrfm = GM.sdrfm()`
>
> `sdrfm.export_trim("Airfoil", 2)`

## export_expand(sector)

**Description:**

Expand a cyclic symmetry model to user defined sectors and add to the list for export.

**Arguments:**

- sector: sector number, INTEGER

**Example:**

> `sdrfm = GM.sdrfm()`
>
> `sdrfm.export_expand(4)`

## export_expand_clr()

**Description:**

Resets the export functionality to only export sector 1 from a cyclic symmetry model.

**Example:**

> `sdrfm = GM.sdrfm()`
>
> `sdrfm.export_expand(4)`
>
> `sdrfm.export_expand_clr()`

## export_expand_opt(axis)

**Description:**

Set the expansion options.

**Arguments:**

- axis: Axis Case, INTEGER

**Example:**

> `sdrfm = GM.sdrfm()`
>
> `sdrfm.export_expand_opt(1)`

## export_model(file_name)

**Description:**

Complete the export process.

**Arguments:**

- file_name: File name (without path), STRING

**Example:**

> `sdrfm = GM.sdrfm()`
>
> `sdrfm.export_model("output.sdr")`

## load_GBF(file_name)

**Description:**

Open shapes from a GBF file.

**Arguments:**

- file_name: Path and file name, STRING

**Example:**

> `sdrfm = GM.sdrfm()`
>
> `sdrfm.load_GBF("c:/test/input.gbf")`

## save_GBF(file_name)

**Description:**

Save shapes to a GBF file.

**Arguments:**

- file_name: File name (without path), STRING

**Example:**

> `sdrfm = GM.sdrfm()`
>
> `sdrfm.save_GBF("output.gbf")`
