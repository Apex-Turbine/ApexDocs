# Collection Functions for Scripting

For a detailed look on use of collections, visit the Collections Overview

Using the GM.collection() function group, the following functions are available:

- [open(filename)](#openfilename)
- [close()](#close)
- [nrows()](#nrows)
- [ncols()](#ncols)
- [read()](#read)
- [get_row](#get_row)
- [row_string](#row_string)
- [fields()](#fields)
- [add_field](#add_field)
- [reset_fields](#reset_fields)
- [dump_file](#dump_file)

## open(filename)

**Description:**

Loads an input collection file and generates one for output

**Arguments:**

- filename: Full path to the file that should be loaded in.

**Example:**

> `infolder = "c:/tmp"`
>
> `col = GM.collection()`
>
> `col.open(infolder .. "/example.collection")`

## close()

**Description:**

Completes the collections task

**Example:**

> `infolder = "c:/tmp"`
>
> `col = GM.collection()`
>
> `col.open(infolder .. "/example.collection")`
>
> `col.close()`

## nrows()

**Returns:**

Returns the number of rows in the collections file

**Example:**

> `col = GM.collection()`
>
> `rows = col.nrows()`

## ncols()

**Returns:**

Returns the number of columns in the collections file

**Example:**

> `col = GM.collection()`
>
> `columns = col.ncols()`

## read()

**Description:**

Read one row of the input collection file. This isn't returned but is held in memory.

**Example:**

> `infolder = "c:/tmp"`
>
> `col = GM.collection()`
>
> `col.open(infolder .. "/example.collection")`
>
> `while col.read()`
>
> > `-- Do stuff here`
>
> `end`

## get_row()

**Returns:**

Returns an object whose members give access to the current row. The elements are accessed by:

1. Using Column name (row["collection_block"])
2. Using the column as the member name (row.collection_block)
3. Using the index (row[1])

**Example:**

> `infolder = "c:/tmp"`
>
> `col = GM.collection()`
>
> `col.open(infolder .. "/example.collection")`
>
> `while col.read()`
>
> > `row = get_row()`
> >
> > `print(row.MyField)`
>
> `end`

## row_string()

**Returns:**

Returns the current row in string form

**Example:**

> `infolder = "c:/tmp"`
>
> `col = GM.collection()`
>
> `col.open(infolder .. "/example.collection")`
>
> `while col.read()`
>
> > `print(col.row_string())`
>
> `end`

## fields()

**Returns:**

Returns a string array of all fields

**Example:**

> `infolder = "c:/tmp"`
>
> `col = GM.collection()`
>
> `col.open(infolder .. "/example.collection")`
>
> `while col.read()`
>
> > `fields = col.fields()`
> >
> > `for i=1,#fields do`
> >
> > > ``print(string.format("field[%d] = %s",i,fields[i]))
> >
> > `end`
>
> `end`

## add_field(field_name)

**Returns:**

Creates a new custom field. Must be done prior to opening the collection.

**Example:**

> `infolder = "c:/tmp"`
>
> `col = GM.collection()`
>
> `col.add_field("my_own_field")`
>
> `col.open(infolder .. "/example.collection")`

## reset_fields()

**Returns:**

Clears all custom fields

**Example:**

> `infolder = "c:/tmp"`
>
> `col = GM.collection()`
>
> `col.open(infolder .. "/example.collection")`
>
> `while col.read()`
>
> > `col.add_field("my_own_field")`
> >
> > `col.reset_fields()`
>
> `end`

## dump_file()

**Returns:**

Dumps all of the collection to the terminal

**Example:**

> `infolder = "c:/tmp"`
>
> `col = GM.collection()`
>
> `col.open(infolder .. "/example.collection")`
>
> `col.dump_file()`
