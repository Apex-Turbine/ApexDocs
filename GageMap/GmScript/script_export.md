# Export Functions for Scripting

Using the GM.export() function group, the following functions are available:

- [add_node](#add_node)
- [add_shape](#add_shape)
- [clear_nodes](#clear_nodes)
- [clear_shapes](#clear_shapes)
- [export_matlab](#export_matlab)

## add_node(start, end)

**Description:**

Adds a range of nodes for export.

**Arguments:**

- start: starting node index, INTEGER
- end: ending node index, INTEGER

**Example:**

> `exp = GM.export()`
>
> `exp.add_node(10001, 10010)`

## add_shape(shape_index, shape_type)

**Description:**

Adds a single shape to be exported.

**Arguments:**

- shape_index: the index of the shape to add, INTEGER
- shape_type: (0=dynamic, 1=static) INTEGER

**Example:**

> `exp = GM.export()`
>
> `exp.add_shape(1,0) exp.add_shape(1,1)`

## clear_nodes()

**Description:**

Removes all individual nodes to export and instead sets the export to all nodes of the model.

**Example:**

> `exp = GM.export()`
>
> `exp.clear_nodes()`

## clear_shapes()

**Description:**

Removes all shapes from the export list.

**Example:**

> `exp = GM.export()`
>
> `exp.clear_shapes()`

## export_matlab(filename)

**Description:**

Export data to a MATLAB file.

**Arguments:**

- filename: File name or absolute name (with path) of the MATLAB file, STRING

**Example 1:**

> `infolder = "c:/tmp"`
>
> `exp = GM.export()`
>
> `exp.export_matlab("myfile.mat")`

**Example 2:**

> `export = GM.export()`
>
> `matFile = "myfile.mat"`
>
> `matFolder = "C:/tmp/"`
>
> `export.export_matlab(matFolder .. matFile)`
