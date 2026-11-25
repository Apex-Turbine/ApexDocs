# GageMap Main Functions for Scripting

Using the GM.main() function group, the following functions are available:

- [filelist(pattern)](#filelistpattern)
- [log(message)](#logmessage)
- [set_logging](#set_logging)
- [set_overwrite](#set_overwrite)
- [set_logname](#set_logname)
- [set_output](#set_output)
- [open(filename)](#openfilename)
- [nnodes()](#nnodes)
- [ngages()](#ngages)
- [nshapes()](#nshapes)
- [nmodes()](#nmodes)
- [nloads()](#nloads)
- [node(index)](#nodeindex)
- [group(index)](#groupindex)
- [list_freq](#list_freq)
- [ggage_info](#ggage_info)
- [maxshape(shape_type, shape_index, variable, [min_max], [node_label])](#maxshapeshape_type-shape_index-variable-min_max-node_label)
- [use_stress](#use_stress)
- [use_complex](#use_complex)
- [set_amp](#set_amp)
- [set_rpm](#set_rpm)
- [isRPM(index)](#isrpmindex)
- [getRPM(index)](#getrpmindex)
- [clear_amps](#clear_amps)
- [amps([shape_type])](#ampsshape_type)
- [snapshot(filename)](#snapshotfilename)
- [view_center](#view_center)
- [view_create](#view_create)
- [view_custom](#view_custom)
- [view_reset](#view_reset)
- [view_rotate](#view_rotate)
- [view_setting](#view_setting)
- [view_zoom](#view_zoom)

## filelist(pattern)

**Description:**

Wildcard-based search of a particular pattern of files.

**Arguments:**

- pattern: Search pattern, which can include wildcards. STRING

**Returns:**

- An array of strings, each representing a file found.

**Example:**

> `gm = GM.main() files = gm.filelist("./*.txt") -- Get all text files in the local folder`
>
> `for i=1,#files do`
>
> > `print(files[i])`
>
> `end`

## log(message)

**Description:**

Write anything desired to the log file.

**Arguments:**

- message: Whatever is to be logged. Any value or string is accepted.

**Example:**

> `gm = GM.main()`
>
> `gm.log("Hello, log")`

## set_logging(type, state)

**Description:**

Turn logging on and off for either the log file or the terminal screen.

**Arguments:**

- type: Either "file" or "screen" depending on which option is needing to be changed. STRING
- state: "true" or "false" to turn logging on or off to the given type.

**Example:**

> `gm = GM.main()`
>
> `gm.set_logging("file", true)`
>
> `gm.set_logging("screen", false)`

## set_overwrite(flag)

**Description:**

Specify whether allowing overwriting of files is permitted this session. This is false by default.

**Arguments:**

- flag: "true" or "false" to enable or disable overwriting.

**Example:**

> `gm = GM.main()`
>
> `gm.set_overwrite(true)`

## set_logname(filename)

**Description:**

Change the name (not the path) of the log output file to write at the end of the process.

**Arguments:**

- filename: New file name to write out to.

**Example:**

> `gm = GM.main()`
>
> `gm.set_logname("mylog.txt")`

## set_output(path)

**Description:**

Change the path that all files, including the log, will be written out to. If the folder does not exist, it will automatically be created.

**Arguments:**

- filename: The desired output path.

**Example:**

> `gm = GM.main()`
>
> `gm.set_output("/home/user/me/")`

## open(filename)

**Description:**

Load an SDR Model into GageMap

**Arguments:**

- filename: Full path to the file that should be loaded in.

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`

## nnodes()

**Returns:**

The number of nodes in the loaded model.

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `nodecount = gm.nnodes()`

## ngages()

**Returns:**

The number of gages in the loaded model.

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `gagecount = gm.ngages()`

## ngroups()

**Returns:**

The number of groups in the loaded model.

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `groupcount = gm.ngroups()`

## nshapes()

**Returns:**

The number of shapes in the loaded model.

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `shapecount = gm.nshapes()`

## nmodes()

**Returns:**

The number of dynamic shapes in the loaded model.

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `modecount = gm.nmodes()`

## nloads()

**Returns:**

The number of static load shapes in the loaded model.

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `loadcount = gm.nloads()`

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
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `node = gm.node(100)`
>
> `print("x: ", node.pos.x, " i: ", node.normal.i)`

## group(index)

**Arguments:**

- index: Index of the desired group.

**Returns:**

- A structure containing information about a group. This structure includes:

  > - name: name of the group, STRING
  > - nnodes: How many nodes belong to the group, INTEGER
  > - opcode: The and/or opcode of the group, INTEGER

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `group = gm.group(1)`
>
> `print("group: ", group.name)`

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

> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `t = gm.list_freq()`
>
> `mode_1_freq = t.Freq[1]`
>
> `mode_1_ndd = t.NDD[1]`

## gage_info(index)

**Arguments:**

- index: Index of desired gage, INTEGER

**Returns:**

An object containing the following items:

> - name - The name of the gage, STRING
> - mapped - If the gage is mapped, INTEGER
> - temperature - The gage temperature, FLOAT
> - modulus - The gage modulus, FLOAT
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
> - dir
>
>   > - i - Gage sensing direction i, FLOAT
>   > - j - Gage sensing direction j, FLOAT
>   > - k - Gage sensing direction k, FLOAT
> - dir90
>
>   > - i - Gage lateral direction i, FLOAT
>   > - j - Gage lateral direction j, FLOAT
>   > - k - Gage lateral direction k, FLOAT
> - normal
>
>   > - i - Gage direction i, FLOAT
>   > - j - Gage direction j, FLOAT
>   > - k - Gage direction k, FLOAT
> - - **mapping**: - - **center**: - x - X coordinate, FLOAT
>     - y - Y coordinate, FLOAT
>     - z - Z coordinate, FLOAT
>   - - **corner1**: - x - sensor corner coordinates X, FLOAT
>     - y - sensor corner coordinates Y, FLOAT
>     - z - sensor corner coordinates Z, FLOAT
>   - - **corner2**: - x - sensor corner coordinates X, FLOAT
>     - y - sensor corner coordinates Y, FLOAT
>     - z - sensor corner coordinates Z, FLOAT
>   - - **corner3**: - x - sensor corner coordinates X, FLOAT
>     - y - sensor corner coordinates Y, FLOAT
>     - z - sensor corner coordinates Z, FLOAT
>   - - **corner4**: - x - sensor corner coordinates X, FLOAT
>     - y - sensor corner coordinates Y, FLOAT
>     - z - sensor corner coordinates Z, FLOAT

**Example:**

> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `gage1_info = gm.gage_info(1)`
>
> `name = gage1_info.name`
>
> `type = gage1_info.type`
>
> `xPos = gage1_info.pos.x`
>
> `temp = gage1_info.temperature`
>
> `mod = gage1_info.modulus`
>
> `xCenter = gageInfo.mapping.center.x`
>
> `xCorner4 = gageInfo.mapping.corner4.x`

## maxshape(shape_type, shape_index, variable, [min_max], [node_label])

**Arguments:**

- shape_type: 0 = Static Load, 1 = Dynamic Mode
- shape_index: Index of the load or mode (relative to type), INTEGER
- variable: Displacement, strain or stress variable, INTEGER

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
  >   > - 11 - eeqv
  >   > - 12 - ep1
  >   > - 13 - ep3
  >   > - 14 - ex
  >   > - 15 - ey
  >   > - 16 - ez
  >   > - 17 - exy
  >   > - 18 - eyz
  >   > - 19 - ezx
  >   > - 21 - seqv
  >   > - 22 - sp1
  >   > - 23 - sp3
  >   > - 24 - sx
  >   > - 25 - sy
  >   > - 26 - sz
  >   > - 27 - sxy
  >   > - 28 - syz
  >   > - 29 - szx
  >   > - 31 - overall max strain, max(Eeqv or abs(E1) or abs(E3) or Ex or Ey or Ez or Yxy or Yyz or Yzx)
  >   > - 32 - max invariant strain, max(Eeqv or abs(E1) or abs(E3))
  >   > - 33 - max component strain, max(Ex or Ey or Ez or Yxy or Yyz or Yzx)
  >   > - 34 - max principals strain, max(abs(E1)or abs(E3)
  >   > - 41 - overall max stress, max(avm or abs(a1) or abs(a3) or ax or ay or az or Txy or Tyz or Tzx)
  >   > - 42 - max invariant stress, max(avm or abs(a1) or abs(a3))
  >   > - 43 - max component stress, max(ax or ay or az or Txy or Tyz or Tzx)
  >   > - 44 - max principals stress, max(abs(a1) or abs(a3)
- min_max (OPTIONAL, default=0): Return maximum or minimum value. Only applies if arg3 is less than 11 (0=maximum 1=minimum) INTEGER
- node_label (OPTIONAL, default=0): If > 0, the returned value is for the specified node. Otherwise, it will return the maximum shape value in the model. INTEGER

**Returns:**

- A structure containing max value information about the node found or specified. This structure includes:

  > - nodeLabel: Label that was ultimately selected, INTEGER
  > - nodeValue: Maximum value of the node, FLOAT

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `max = gm.maxshape(1, 7, 44)`
>
> `print("max value: ", max.nodeValue)`

use_stress(shape_type, setting)

---

**Description:**

Changes either dynamic or static stresses to be either imported or GageMap computed

*NOTE -- shape_type can be a STRING or INTEGER value as shown below*

**Arguments:**

- shape_type: ("static", "dynamic"), STRING

-OR-

- shape_type: (0=static, 1=dynamic), INTEGER
- setting: (0=imported, 1=computed), INTEGER

**Example:**

`infolder = "c:/tmp"`

`gm = GM.main()`

`gm.open(infolder .. "/example.sdr")`

`gm.use_stress("static",1)`

-OR-

`gm.use_stress(0,1)`

## use_complex(setting)

**Description:**

Set whether the model uses its modes as complex or individual shapes

**Arguments:**

- setting: (0=complex, 1=individual), INTEGER

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `gm.use_complex(0)`

## set_amp(shape_index, amplitude, shape_type)

**Description:**

Set the amplitude of any shape. However, loads must not be centrifugal.

**Arguments:**

- shape_index: Index of the shape relative to its type, INTEGER
- amplitude: Desired Amplitude, FLOAT
- shape_type:(0=dynamic, 1=static), INTEGER

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `gm.set_amp(1,2.5,1)`

## set_rpm(load_index, rpm)

**Description:**

Set the rpm of any CENTRIFUGAL static load for animation for fatigue analysis.

**Arguments:**

- load_index: Index of the static centrifugal load, INTEGER
- rpm: Desired rpm value, FLOAT

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `gm.set_rpm(1,2000)`

## isRPM(index)

**Arguments:**

- index: Index of the static load case, INTEGER

**Returns:**

True or False value if the given load case is RPM based

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `if gm.isRPM(1) then`
>
> > `print("Load 1 is RPM Based")`
>
> `end`

## getRPM(index)

**Arguments:**

- index: Index of the static load case, INTEGER

**Returns:**

RPM of the given load case.

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `if gm.isRPM(1) then`
>
> > `print("Load 1 RPM = ", gm.getRPM(1))`
>
> `end`

## clear_amps()

**Description:**

Clear all amplitudes for every dynamic mode by setting them to 0.

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `gm.set_amp(1,2.5,1)`
>
> `gm.clear_amps()`

## amps([shape_type])

**Arguments:**

shape_type (OPTIONAL, default=0): (0=dynamic, 1=static), INTEGER

**Returns:**

- Array containing all amplitudes of a given shape type

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `mode_amps = gm.amps()`
>
> `for i=1,#mode_amps do`
>
> > `print(mode_amps[i])`
>
> `end`

## snapshot(filename)

**Description:**

Saves a PNG image of the model

**Arguments:**

filename: File name (without path) to save PNG to.

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `gm.snapshot("pic.png")`

## view_center(x, y, z)

**Description:**

Center the model view on a 3d model coordinate

**Arguments:**

- x, y, z: Coordinate arguments, FLOATS

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `gm.view_center(2,3,4)`

## view_create(Name, Eye_i, Eye_j, Eye_k, Up_i, Up_j, Up_k)

**Description:**

Defines a named custom view based upon an eye and up direction .

**Arguments:**

- Name: custom view label, string
- Eye_i: X-coordinate for "eye" direction, FLOAT
- Eye_j: Y-coordinate for "eye" direction, FLOAT
- Eye_k: Z-coordinate for "eye" direction, FLOAT
- Up_i: X-coordinate for "up" direction, FLOAT
- Up_j: Y-coordinate for "up" direction, FLOAT
- Up_k: Z-coordinate for "up" direction, FLOAT

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `gm.view_create("Isometric", 0.5, 0.5, 0.5, 0.0, -1.0, 0.0)`

## view_custom(Name)

Description:

Sets the view of the model based upon a custom view which the user has setup (names are case insensitive, can use default names also i.e. top, bottom, etc.)

**Arguments:**

- Name: name of desired view

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `gm.view_custom("pressure_side")`

## view_reset()

**Description:**

Resets the model view back to the original state

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `gm.view_reset()`

## view_rotate(angle, i_direction, j_direction, k_direction)

**Description:**

Rotates the model view about a combination of axes given the degrees desired.

**Arguments:**

- angle: rotation angle, STRING
- i_direction: X-coordinate of axis for rotation, FLOAT
- j_direction: Y-coordinate of axis for rotation, FLOAT
- k_direction: Z-coordinate of axis for rotation, FLOAT

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `gm.view_rotate(45, 0, 1, 0)`

## view_setting(Setting, Value)

**Description:**

Set a particular view setting to true or false.

**Arguments:**

- Setting = The setting to change, STRING

  > Available settings(NOT case sensitive):
  >
  > - FACES - Draw the filled faces. ( Default: 1 )
  > - LINES - Draw the "wires" outlining each face. ( Default: 1 )
  > - NODES - Highlight and draw every node on the model. (Default: 0 )
  > - NODE_LABELS - Whether to label each node with its associated index. ( Default: 0 )
- Value = New value for the setting, (0=off, 1=on), INTEGER

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `gm.view_setting("NODES",1)`

## view_zoom(scale_factor)

**Description:**

Zoom the model view

**Arguments:**

- scale_factor: zooming scale factor, FLOAT

**Example:**

> `infolder = "c:/tmp"`
>
> `gm = GM.main()`
>
> `gm.open(infolder .. "/example.sdr")`
>
> `gm.view_zoom(2.5)`
