# Group Functions for Scripting

Using the GM.group() function group, the following functions are available:

- [open(filename)](#openfilename)
- [save(filename)](#savefilename)
- [func(group_name, function)](#funcgroup_name-function)
- [view(option)](#viewoption)

## open(filename)

**Description:**

Loads the GRP file used for grouping. Multiple group files can be loaded using multiple instances of this command. Additional groups are always appended to the current groups. Groups can contain identical names.

**Arguments:**

- filename: Full path and name of the file to be loaded.

**Example:**

> `infolder = "c:/tmp"`
>
> `gp = GM.group()`
>
> `gp.open(infolder .. "/example.grp")`

## save(filename)

**Description:**

Saves the current set of groups into a new GRP file.

**Arguments:**

- filename: New group filename (without path) including the .grp file extension.

**Example:**

> `infolder = "c:/tmp"`
>
> `gp = GM.group()`
>
> `gp.open(infolder .. "/example.grp")`
>
> `gp.save("mine.grp")`

## func(group_name, function)

**Description:**

Changes the group function Boolean type.

**Arguments:**

- group_name = group name, STRING (case-insensitive)
- function = group Boolean function, INTEGER

  > - 0 - Disabled
  > - 1 - AND
  > - 2 - OR
  > - 3 - NOT
- filename: Filename (without path) that should be saved out.

**Example:**

> `infolder = "c:/tmp"`
>
> `gp = GM.group()`
>
> `gp.open(infolder .. "/example.grp")`
>
> `gp.func("blade", 1)`

## view(option)

**Description:**

Sets the option to view grouped regions only. Performs an internal trim of the model for subsequent analysis.

**Arguments:**

- show grouped regions only? (0=no, 1=yes) INTEGER

**Example:**

> `infolder = "c:/tmp"`
>
> `gp = GM.group()`
>
> `gp.open(infolder .. "/example.grp")`
>
> `gp.view(1)`
