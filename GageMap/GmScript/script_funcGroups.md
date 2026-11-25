# Function Groups for Scripting

All GageMap functions are accessible through special structures that group them together. This is done mostly for organizational reasons. It also assists in license validation and task management. For example, a request for an unlicensed function group will warn and then return nil, allowing it to be handled in a case statement.

To access these function groups, use the global GM structure to assign them to any variable name desired. For example:

> `def main()`
>
> > `gm = GM.main()`
> >
> > `gp = GM.groups()`
> >
> > `opt = GM.optimize()`
> >
> > `if opt == nil then`
> >
> > > `print("No Optimizing!")`
> >
> > `end`
>
> `end`

The following groups are supported. Click below or using the navigation pane to access individual documentation. Please remember that Lua is case-sensitive and all groups are in lower case.

- [GageMap Main Functions for Scripting](script_main.md)
- [Group Functions for Scripting](script_task_grouping.md)
- [Animation Functions for Scripting](script_task_animate.md)
- [Fatigue Functions for Scripting](script_task_fatigue.md)
- [SDRFM Functions for Scripting](script_sdrfm.md)
- [Export Functions for Scripting](script_export.md)
- [Ansys Functions for Scripting](script_ansys.md)
- [Sensors Functions for Scripting](script_task_sensors.md)
- [Optimization Functions for Scripting](script_task_optimization.md)
- [Collection Functions for Scripting](script_collection.md)
- [Strain Gage Validation Functions for Scripting](script_validate.md)
