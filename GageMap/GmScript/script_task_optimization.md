# Optimization Functions for Scripting

Using the GM.optimize() function group, the following functions are available:

- [apply()](#apply)
- [open(filename)](#openfilename)
- [save(filename)](#savefilename)
- [reset()](#reset)
- [sensor_add](#sensor_add)
- [sensor_reset](#sensor_reset)
- [mode(index, enabled, [priority])](#modeindex-enabled-priority)
- [mode_amp](#mode_amp)
- [mode_reset](#mode_reset)
- [amp(min, [redundant_count], [redundant_enabled], [apply_to], [priority])](#ampmin-redundant_count-redundant_enabled-apply_to-priority)
- [run(time, [stop])](#runtime-stop)
- [report(filename)](#reportfilename)
- [quantity_optimize](#quantity_optimize)
- [apply_design](#apply_design)

## apply()

**Description:**

Applies the sensors from the last optimization run to the model.

**Example:**

> `opt = GM.optimize()`
>
> `-- Following Optimization`
>
> `opt.apply()`

## open(filename)

**Description:**

Loads the optimizer configuration file.

**Arguments:**

- filename: Full path and name, STRING

**Example:**

> `infolder = "c:/tmp"`
>
> `opt = GM.optimize()`
>
> `opt.open(infolder .. "myfile")`

## save(filename)

**Description:**

Saves the optimizer configuration to a file.

**Arguments:**

- filename: File name (without path), STRING

**Example:**

> `opt = GM.optimize()`
>
> `opt.save("myfile")`

## reset()

**Description:**

Clears and resets the entire optimization configuration

**Example:**

> `opt = GM.optimize()`
>
> `-- Following Optimization Configuration`
>
> `opt.reset()`

## sensor_add(type, quantity, [length, width], [placement_group], [sensitive_group])

**Description:**

Adds a sensor to the configuration for optimization.

**Arguments:**

- type = sensor type, INTEGER

  > - 1 - Strain gage
  > - 2 - Displacement sensor
- quantity = number of this sensor to add, INTEGER
- length (REQUIRED when type is Strain Gage): sensor length, FLOAT
- width (REQUIRED when type is Strain Gage): sensor width, FLOAT
- placement_group (OPTIONAL, must be a loaded group): placement group name, STRING
- sensitive_group (OPTIONAL, must be a loaded group): sensitive group name, STRING

**Example:**

> `opt = GM.optimize()`
>
> `opt.sensor_add(1, 1, 0.25, 0.25, "blade")`

## sensor_reset()

**Description:**

Removes all of the sensors from the optimization configuration.

**Example:**

> `opt = GM.optimize()`
>
> `-- Following Sensor Configuration`
>
> `opt.sensor_reset()`

## mode(index, enabled, [priority])

**Description:**

Controls the modes being optimized.

**Arguments:**

- index = index of the mode to enable or disable, INTEGER
- enabled = (0=Disable, 1=Enable), INTEGER
- priority (OPTIONAL) = Priority of this mode during optimization, INTEGER

**Example:**

> `opt = GM.optimize()`
>
> `opt.mode(1,1)`
>
> `opt.mode(2,1,1)`

## mode_amp(mode_index, min, [max])

**Description:**

Overrides the general objective amplitude ratio with custom ratios for a mode.

**Arguments:**

- mode_index = index of the mode to edit, INTEGER
- min = minimum mode amplitude ratio, FLOAT
- max (OPTIONAL) = maximum mode amplitude ratio, FLOAT

**Example:**

> `opt = GM.optimize()`
>
> `opt.mode_amp(1,0.2)`
>
> `opt.mode_amp(2,0.2,0.7)`

## mode_reset()

**Description:**

Resets all custom mode amplitudes and disables all modes from being optimized.

**Example:**

> `opt = GM.optimize()`
>
> `-- Following Mode Amplitude Configuration`
>
> `opt.mode_reset()`

## amp(min, [redundant_count], [redundant_enabled], [apply_to], [priority])

**Description:**

Sets the mode amplitude objective settings.

**Arguments:**

- min = minimum amplitude ratio, FLOAT
- redundant_count (OPTIONAL) = number of redundant sensors, INTEGER
- redundant_enabled (OPTIONAL) = enable redundant sensor optimization, (0=false, 1=true), INTEGER
- apply_to (OPTIONAL) = minimum amplitude ratio applies to, (0=best, 1=average), INTEGER
- priority (OPTIONAL) = objective priority, INTEGER

  > 1 - Lowest Priority
  > ...
  > 5 - Average Priority
  > ...
  > 9 - Highest Priority

**Example:**

> `opt = GM.optimize()`
>
> `opt.amp(0.3, 2, 1, 0, 5)`

## run(time, [stop])

**Description:**

Run the optimizer with the current configuration.

**Arguments:**

- time = total run length in seconds, FLOAT
- stop (OPTIONAL) = time in seconds to stop after no better design found, FLOAT

**Example:**

> `opt = GM.optimize()`
>
> `opt.run(120.0)`

## report(filename)

**Description:**

Optimizer Design Report (HTML).

**Arguments:**

- filename: File name (without path), STRING

**Example:**

> `opt = GM.optimize()`
>
> `opt.report("design_report.html")`

## quantity_optimize(Placmentgroup,sensitiveGroup,length,width,min_ratio,**(OPTIONAL)**report_name)

**Description:**

Quantity Optimizer routine. User needs to set the modes with *[mode(index, enabled, [priority])](#modeindex-enabled-priority) before calling this function.

**Arguments:**

- Placementgroup: name of the placement group. If there are no groups, use "Visual Model", STRING
- sensitiveGroup: name of the sensitive group. If there are no groups, use "Visual Model", STRING
- length: Strain gage length, FLOAT
- width: Strain gage width, FLOAT
- min_ratio: minimum amplitude ratio, FLOAT
- **(OPTIONAL)** report_name: name of the HTML report without path, STRING

**Returns:**

An object containing the following items:

> - numDesigns: The number of designs generated (up to 4)
> - numGages: The number of gages in the specified design.
> - ratio: The mean ratio for the specified design

**Example:**

> `opt = GM.optimize()`
>
> `for imode=1,nmodes do`
>
> > `opt.mode(imode,1) --enable all modes`
>
> `end`
>
> `designs = opt.quantity_optimize("Visible Model","Visible Model",0.0625,0.0625,0.4,"report.html")`
>
> `for idesign=1,designs.numDesigns do`
>
> > `print("  Design ", idesign, " has ", designs.numGages[idesign]," Gages with a ", designs.ratio[idesign], "ratio.")`
>
> `end`

## apply_design(design_index)

**Description:**

Applies the requested design to the model. The design will then be able to be saved to an SGA file (see [Sensors Functions for Scripting](script_task_sensors.md).

**Arguments:**

- design_index: The index of the design to be applied, INTEGER

**Example**

> `opt = GM.optimize()`
>
> `sens = GM.sensors()`
>
> `designs = opt.quantity_optimize("Visible Model","Visible Model",0.0625,0.0625,0.4)`
>
> `for idesign=1,designs.numDesigns do`
>
> > `opt.apply_design(idesign)`
> >
> > `sens.save("Design-" .. idesign .. ".sga")`
>
> `end`
