# Ansys Functions for Scripting

Using the GM.ansys() function group, the following functions are available:

- [add_rst](#add_rst)
- [clear_rst](#clear_rst)
- [mode_subset](#mode_subset)
- [set_option](#set_option)
- [convert(file_name)](#convertfile_name)

## add_rst(file_name)

**Description:**

Adds an RST file for conversion.

**Arguments:**

- file_name: Full file path and name, STRING

**Example:**

> `path = "/home/me/"`
>
> `ansys = GM.ansys()`
>
> `ansys.add_rst(path .. "myrst.rst")`

## clear_rst()

**Description:**

Clears all added RST files.

**Example:**

> `path = "/home/me/"`
>
> `ansys = GM.ansys()`
>
> `ansys.add_rst(path .. "myrst.rst")`
>
> `ansys.clear_rst()`

## mode_subset(mode_list)

**Description:**

Declares a subset of the available modes to be processed, passed in as a string. Allows comma seperated values and range values denoted by a hyphen.

**Example:**

> `path = "/home/me/"`
>
> `ansys = GM.ansys()`
>
> `ansys.mode_subset("1-5, 6")`

## set_option(option, setting)

**Description:**

Change the converter options.

**Arguments:**

- option = converter option, string

  > - 'modal_stress', converts modal strains and stresses, default is yes (1)
  > - 'static_stress', converts static strains and stresses, default is yes (1)
  > - 'cyclic', converts model as cyclic symmetric, default is no (0)
  > - 'first_order', converts the model using first order faces, default is no (0)
  > - - **'local_coord', retain element results in local coordinate system, default is no (0)**: - 'apply_nl', enables application of NL geometry, default is no(0). Takes a third argument for file index, if none given defaults to first.
- setting = converter option toggle, INTEGER/FLOAT

**Example:**

> `path = "/home/me/"`
>
> `ansys = GM.ansys()`
>
> `ansys.set_option('avg_ext', 0)`

## convert(file_name)

**Description:**

Specify the SDR file and Execute the conversion.

**Arguments:**

- file_name: File name or absolute name (with path) of the output SDR file, STRING

**Example 1:**

> `ansys = GM.ansys()`
>
> `ansys.convert("myfile.sdr")`

**Example 2:**

> `ansys = GM.ansys()`
>
> `sdrFolder = "C:/tmp/"`
>
> `ansys.convert(sdrFolder .. "myfile" .. ".sdr")`
