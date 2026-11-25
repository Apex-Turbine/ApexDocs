# Strain Gage Validation Functions for Scripting

Using the GM.validate() function group, the following functions are available:

- [load_ex](#load_ex)
- [set_modes](#set_modes)
- [run_validation](#run_validation)
- [mac()](#mac)
- [mfdp()](#mfdp)
- [mode_pairs](#mode_pairs)
- [results()](#results)
- [apply()](#apply)
- [save_sga](#save_sga)
- [ex_strains](#ex_strains)
- [ex_frequencies](#ex_frequencies)
- [gm_strains](#gm_strains)
- [gm_frequencies](#gm_frequencies)
- [ex_scaled](#ex_scaled)
- [loaded_gages](#loaded_gages)

> [!NOTE]
> The Strain Gage Validation Task **REQUIRES** the model have at least 1 mode. The task also **REQUIRES** the names of the strain gages within the model, be the same as the names referenced in the input file.

## load_ex(fileName)

**Description:**

Loads the test data CSV file.

**Arguments:**

- fileName: The full path to the file

**Example:**

> `infolder = "c:/tmp"`
>
> `val = GM.validate()`
>
> `val.load_ex(infolder .. "/example.csv")`

## set_modes(modes)

**Description:**

Sets the task to use the specified modes from the file

**Arguments:**

- modes: An Int array of mode indexes

**Example:**

> `modes = {1,3,5,7,9}`
>
> `val = GM.validate()`
>
> `val.set_modes(modes)`

## run_validation(useMac, (optional) dxTol, (optional) dyTol, (optional) dthetaTol, (optional) shapeWeight)

**Description:**

Runs the validator with the specified parameters. This function **DOES NOT** apply the deltas.

**Arguments:**

- useMac: Integer to specify whethter to use MAC or MFDP for the Mode Matching algorithm, 1=MAC, 2=MFDP
- dxTol (optional): The delta X tolerance. If not set, the default will be used.  DOUBLE
- dyTol (optional): The delta Y tolerance. If not set, the default will be used.  DOUBLE
- dthetaTol (optional): The delta Theta tolerance. If not set, the default will be used.  DOUBLE
- shapeWeight (optional): The weight factor for the Mode Match algorithm. If not set, a factor of 80 will be used. Value range is 0 - 100.  DOUBLE

**Example:**

> `file = ./example.csv`
>
> `val = GM.validate()`
>
> `val.load_ex(file)`
>
> `val.run_validation(1, 0.1, 0.1, 5.0, 70)`

## mac()

**Description:**

This is the MAC Matrix computed in the validator. The "run_validation" **MUST** be run before calling this function.

**Returns:**

- 2D Array containing the the Experimental Modes as rows, and the GageMap Modes as columns.

**Example:**

> `file = ./example.csv`
>
> `val = GM.validate()`
>
> `val.load_ex(file)`
>
> `val.run_validation(1, 0.1, 0.1, 5.0, 70)`
>
> `mac = val.mac()`
>
> `for i=1,#mac do`
>
> ``      row = ""        ``
>
> ``      for j=1,#mac[i] do``
>
> ``              row = row .. string.format("%.3f",mac[i][j]) .. ", "``
>
> ``      end``
>
> ``      print(row)``
>
> `end`

## mfdp()

**Description:**

This is the MFDP Matrix computed in the validator. The "run_validation" **MUST** be run before calling this function.

**Returns:**

- 2D Array containing the the Experimental Modes as rows, and the GageMap Modes as columns.

**Example:**

> `file = ./example.csv`
>
> `val = GM.validate()`
>
> `val.load_ex(file)`
>
> `val.run_validation(1, 0.1, 0.1, 5.0, 70)`
>
> `mfdp = val.mfdp()`
>
> `for i=1,#mfdp do`
>
> ``      row = ""        ``
>
> ``      for j=1,#mfdp[i] do``
>
> ``              row = row .. string.format("%.3f",mfdp[i][j]) .. ", "``
>
> ``      end``
>
> ``      print(row)``
>
> `end`

## mode_pairs()

**Description:**

This is the mode pairs computed in the validator. The "run_validation" **MUST** be run before calling this function.

**Returns:**

- String array in the format "'Experimental Mode Number','GageMap Mode Number'"

**Example:**

> `val = GM.validate()`
>
> `val.load_ex("./example.csv")`
>
> `val.run_validation(1, 0.1, 0.1, 5.0, 70)`
>
> `pair = val.mode_pairs()`
>
> `print("Format = TestMode,GmMode")`
>
> `for i=1,#pair do`
>
> ``      print(pair[i])``
>
> `end`

## results()

**Description:**

This is the results structure created in the validator. The "run_validation" **MUST** be run before calling this function.

**Returns:**

- Array of structures with the length being the number of gages validated.

  > - Gage: The name of the gage
  > - dx: The delta X value
  > - dy: The delta Y value
  > - dtheta: The delta Theta value
  > - error: The average error for placing the gage at the specified deltas

**Example:**

> `val = GM.validate()`
>
> `val.load_ex("./example.csv")`
>
> `val.run_validation(1, 0.1, 0.1, 5.0, 70)`
>
> `results = val.results()`
>
> `for i=1,#results do`
>
> ``      print(results[i].Gage)``
>
> ``      print("  dx = ",string.format("%.3f",results[i].dx))``
>
> ``      print("  dy = ",string.format("%.3f",results[i].dy))``
>
> ``      print("  dt = ",string.format("%.3f",results[i].dtheta))``
>
> ``      print("  error = ",string.format("%.3e",results[i].error))``
>
> `end`

## apply()

**Description:**

This function applies the deltas to the gages and the recalculates the sensitivities. If a gage is unable to be mapped, it will be stated in the log file.

**Example**

> `val = GM.validate()`
>
> `val.load_ex("./example.csv")`
>
> `val.run_validation(1, 0.1, 0.1, 5.0, 70)`
>
> `val.apply()`

## save_sga(filename)

**Description:**

This function saves the gages mapped to to the specified offsets to an sga file.

**Arguments:**

- filename: Name of the SGA file to save the gages to.

**Example:**

> `val = GM.validate()`
>
> `val.load_ex("./example.csv")`
>
> `val.run_validation(1, 0.1, 0.1, 5.0, 70)`
>
> `val.save_sga("./output/Test.sga")`

## ex_strains()

**Descriptinon:**

The Strains read in from the input file. If "Set_Modes" has not been set, this returns all read in modes.

**Returns:**

- 2D Array containing the gages as the rows and the modes as the columns

**Example**

> `val = GM.validate()`
>
> `val.load_ex("./example.csv")`
>
> `exS = val.ex_strains()`
>
> `for ig=1,#exS do`
>
> ``      row = Gage .. ig .. ": "``
>
> ``      for iex=1,#exS[ig] do``
>
> ``              row = row .. string.format("%.3f",exS[ig][iex]) .. ", "``
>
> ``      end``
>
> `       print(row)``
>
> `end`

## ex_frequencies()

**Descriptinon:**

The Frequencies read in from the input file. If "Set_Modes" has not been set, this returns all read in modes.

**Returns:**

- 2D Array containing the gages as the rows and the modes as the columns

**Example**

> `val = GM.validate()`
>
> `val.load_ex("./example.csv")`
>
> `exF = val.ex_frequencies()`
>
> `for ig=1,#exF do`
>
> ``      row = Gage .. ig .. ": "``
>
> ``      for iex=1,#exFig] do``
>
> ``              row = row .. string.format("%.3f",exF[ig][iex]) .. ", "``
>
> ``      end``
>
> `       print(row)``
>
> `end`

## gm_strains()

**Descriptinon:**

The GageMap Strains. If this function is called before "run_validation" has been called, the returned structure will contain all GageMap modes. If it is called after, it will return the structure ordered to match the Experimental modes.

**Returns:**

- 2D Array containing the gages as the rows and the modes as the columns

**Example**

> `val = GM.validate()`
>
> `val.load_ex("./example.csv")`
>
> `gmS = val.gm_strains()`
>
> `for ig=1,#gmS do`
>
> ``      row = Gage .. ig .. ": "``
>
> ``      for igm=1,#gmS[ig] do``
>
> ``              row = row .. string.format("%.3f",gmS[ig][igm]) .. ", "``
>
> ``      end``
>
> `       print(row)``
>
> `end`

## gm_frequencies()

**Descriptinon:**

The GageMap frequencies. If this function is called before "run_validation" has been called, the returned structure will contain all GageMap modes. If it is called after, it will return the structure ordered to match the Experimental modes.

**Returns:**

- 2D Array containing the gages as the rows and the modes as the columns

**Example**

> `val = GM.validate()`
>
> `val.load_ex("./example.csv")`
>
> `gmF = val.gm_frequencies()`
>
> `for ig=1,#gmF do`
>
> ``      row = Gage .. ig .. ": "``
>
> ``      for igm=1,#gmF[ig] do``
>
> ``              row = row .. string.format("%.3f",gmF[ig][igm]) .. ", "``
>
> ``      end``
>
> `       print(row)``
>
> `end`

## ex_scaled()

**Descriptinon:**

The Strains read in from the input file scaled to match the GageMap Strains. If "Set_Modes" has not been set, this returns all read in modes. The "run_validation" **MUST** be run before calling this function.

**Returns:**

- 2D Array containing the gages as the rows and the modes as the columns

**Example**

> `val = GM.validate()`
>
> `val.load_ex("./example.csv")`
>
> `exS = val.ex_scaled()`
>
> `for ig=1,#exS do`
>
> ``      row = Gage .. ig .. ": "``
>
> ``      for iex=1,#exS[ig] do``
>
> ``              row = row .. string.format("%.3f",exS[ig][iex]) .. ", "``
>
> ``      end``
>
> `       print(row)``
>
> `end`

## loaded_gages()

**Description:**

The names of the gages from the input file that matched the names of the gages in GageMap.

**Returns:**

- String Array of Gage Names

**Example:**

> `val = GM.validate()`
>
> `val.load_ex("./example.csv")`
>
> `names = val.loaded_gages()`
>
> `for igage=1,#names do`
>
> ``      print(names[igage])``
>
> `end`
