# Fatigue Functions for Scripting

Using the GM.fatigue() function group, the following functions are available:

- [open(filename)](#openfilename)
- [save(filename)](#savefilename)
- [find_limit](#find_limit)
- [node(node_label)](#nodenode_label)
- [mode_sup](#mode_sup)
- [report_limits](#report_limits)
- [report_page](#report_page)
- [report_plot](#report_plot)
- [report_sensor](#report_sensor)
- [report_snapshot](#report_snapshot)
- [limit_export](#limit_export)

## open(filename)

**Description:**

Read and process a fatigue GMF file. Multiple GMFs may be loaded in by calling the function multiple times.

**Arguments:**

- filename: Full path and name of the GMF file, STRING

**Example:**

> `infolder = "c:/tmp"`
>
> `fat = GM.fatigue()`
>
> `fat.open(infolder .. "/example.gmf")`

## save(filename)

**Description:**

Save a single GMF for the current setup. This will combine all GMF's loaded in as well as any changes made.

**Arguments:**

- filename: File name (without path), STRING

**Example:**

> `infolder = "c:/tmp"`
>
> `fat = GM.fatigue()`
>
> `fat.open(infolder .. "/example1.gmf")`
>
> `fat.open(infolder .. "/example2.gmf")`
>
> `fat.save("combined.gmf")`

## find_limit(curve_name, static_stress, temperature)

**Description:**

Retrieves a limit value by directly inputting the fatigue material curve, static stress value and temperature (if applicable). This function can be used to verify the correct fatigue limit values prior to performing a fatigue analysis. Results can be checked against a reference variable.

**Arguments:**

- curve_name: Fatigue material curve name, STRING
- static_stress: Static Stress value, FLOAT
- temperature: Temperature value, FLOAT

**Returns:**

The calculated limit, FLOAT

**Example:**

> `infolder = "c:/tmp"`
>
> `fat = GM.fatigue()`
>
> `fat.open(infolder .. "/example1.gmf")`
>
> `limit = fat.find_limit("Airfoil", 1.0, 2.0)`

## node(node_label)

**Description:**

Retrieves a structure containing node information related to fatigue assessment.

**Arguments:**

- node_label: Node label for the node desired

**Returns:**

- A structure containing all the fatigue information for the provided node. This structure includes:

  > - nodeLabel: Node label for limiting or requested node, INTEGER
  > - limit: Percent limit of the node, FLOAT
  > - sstress: Percent limit of the node, FLOAT
  > - vstress: Vibratory stress for limiting or requested node, FLOAT
  > - temperature: Temperature for limiting or requested node, FLOAT
  > - material: Fatigue material assigned to the limiting or requested node, STRING
  > - group: Group limiting or requested node is assigned to, STRING

**Example:**

> `infolder = "c:/tmp"`
>
> `fat = GM.fatigue()`
>
> `fat.open(infolder .. "/example1.gmf")`
>
> `node = fatigue.node(1019) print("The static stress is:", mnode.sstress)`

## mode_sup(static_type, dynamic_type, mode_scales, [static_case, load_case], [write])

**Description:**

Return the positive/negative combination of a set of mode scaling factors that creates the highest % limit for any grouped node. All groups with Boolean AND or OR are evaluated. Groups that are disabled or have Boolean NOT are ignored. All nodes that are not a member of any group are assigned to the "Default" group and are evaluated (with default fatigue properties if not explicitly defined). It is HIGHLY recommended that ALL nodes be a member of at least one group. If a node is a member of more than one group the following rules apply:  the order of the groups as they appear within the GRP file dictates group membership such that the lowest group as listed in the file takes precedence. The order of the groups may be overridden by the order of the group assignments within the fatigue assignments. Specifically those commands that assign the fatigue material properties to the group:

- assignment,Default,Airfoil Material,Max Principal,Max Principals
- assignment,Airfoil,Airfoil Material,Max Principal,Max Principals
- assignment,Disk,Disk Material,Max Principal,Max Principals
- assignment,LeadingEdge,LeadingEdge Material,Max Principal,Max Principals
- assignment,TrailingEdge,TrailingEdge Material,Max Principal,Max Principals

MODESUP will make use of any static or dynamic adders set to the model groups. To use this feature, the GMF (fatigue preferences) file must include the following command: "assignadder,<group name>,<static adder>,<dynamic adder>":

- assignscale,Default,100,100
- assignscale,Airfoil,100,100
- assignscale,Disk,100,100
- assignscale,LeadingEdge,100,100
- assignscale,TrailingEdge,100,100
- assignadder,Default,0,0
- assignadder,Airfoil,0,0
- assignadder,Disk,0,0
- assignadder,LeadingEdge,0,0
- assignadder,TrailingEdge,0,0

**MODESUP theory:**

1. Determine number of active modes for the superposition evaluation. This is the number of modes with non-zero mode scalars (mode_scales).
2. Compute the independent +/- combinations of the mode scalars. For example for 2 active modes this would result in 2 combinations:  [+ +], [+ -].
3. For all nodes in each active group (Or, And Boolean) evaluate all superposition combinations. Retain the combination that produces the highest % of limit across all groups. This combination returned is identical to the mode scalars supplied in mode_scales but with the appropriate sign attached to each entry.
4. Superposition combinations are evaluated using the static and dynamic types supplied in args 1 & 2. The static scale factor (static_scale) is a scalar to be applied to the static stress shape.
5. Stress types:

  > - Min Principal - the S3 invariant, applies only to static stress
  > - Max Principal - the S1 invariant, applies only to static stress.
  > - Max Principals - max(S1, S3), applies only to dynamic stress
  > - VonMises - applies to both static and dynamic stress.
  > - Aligned - alignment results in a transformation of the stress tensor. If align is specified as the static type, the static stress tensor is aligned with the dynamic max principal(s) direction. If align is specified as the dynamic type, alignment is either in the static min or max principal direction, depending on the static type. If both static and dynamic are set to aligned, then perform alignment in both directions and retain the alignment that produces the highest % of limit.
  > - R-ratio - align (transform) either the static into dynamic or dynamic into static based on a comparison of static max or min principal to dynamic max principals. If static max (or abs(min)) principal > dynamic max principals then align dynamic into static otherwise align static into dynamic.
6. If any node in any group returns a dynamic stress limit of zero, MODESUP will exit with an error. A dynamic limit of zero indicates failure of the part due to the static stress. The log file will report the offending node. The user must either change the static load scale, remove the node from assessment and/or change the fatigue material properties assigned to that node.

The results returned from MODESUP are those from the most limiting (highest % limit) node across all active groups. These results can be used to perform a downstream fatigue analysis under certain conditions. Summary of argument possibilities and their inherent limitations:

1. static_type = -1, 1 or 2 & dynamic type = 1 or 2: static_type = -1 utilizes min principal stress, =1 utilizes max principal stress, =2 utilizes Von Mises stress. Can be replicated in both the GUI and with subsequent BATCH commands. Subsequent BATCH commands (FATAMP) apply the same modal scale factors identically for all nodes.
2. static_type = 3 & dynamic_type = 1 or 2:  Align static shape into dynamic max principals direction. Can only be replicated within the GUI or alternative SCRIPT commands in the limiting case of only one active mode. However, the static shape can be aligned to a combination of dynamic shapes if the dynamic shapes are combined using the SDR file manager.
3. static_type = -1, 1 or 2 & dynamic_type = 3:  Align dynamic shape into static max (static_type=1) principal or static min (static_type=-1) direction. There is no restriction that the static_type the result of the dynamic alignment, i.e., align dynamic stress into static max principal direction, yet use static Von Mises for determining static fatigue capability. Cannot be replicated in the GUI or using alternative SCRIPT commands. Access to fatigue results is only available if write = 1.
4. static_type = 3, dynamic_type = -3,3:  If dynamic_type =-3, then then dynamic max principal(s) is compared to static min principal. If dynamic_type =3, then then dynamic max principal(s) is compared to static max principal.Worst case alignment based on % limit. Can be replicated if most limiting case is static shape into dynamic max principals direction. If so, proceed as in #2 above, otherwise, cannot be replicated in the GUI or using alternative SCRIPT commands. Access to results is ONLY available if write = 1.
5. static_type = 4, dynamic_type = 4:  Alignment based on comparison of max principal stress. Can be replicated if most limiting case is static shape into dynamic max principals direction. If so, proceed as in #2 above, otherwise, cannot be replicated in the GUI or using alternative SCRIPT commands. Access to results is ONLY available if write = 1.
6. static_type = -4, dynamic_type = -4:  Alignment based on comparison of dynamic max principal(s) stress & static min principal stress. Can be replicated if most limiting case is static shape into dynamic max principals direction. If so, proceed as in #2 above, otherwise, cannot be replicated in the GUI or using alternative SCRIPT commands. Access to results is ONLY available if write = 1.
7. static_type = -1, 1, 2, 3,-4 dynamic_type = 4:  not possible, setting this combination results in the algorithm overriding the input such that static_type = dynamic_type = 4.
8. static_type = -1, 1, 2, 3,4 dynamic_type = -4:  not possible, setting this combination results in the algorithm exiting with an error.
9. static_type = -4, dynamic_type = 1, 2, -3, 3, 4:  not possible, setting this combination results in the algorithm exiting with an error.

Currently, there is no equivalent functionality within the GageMap GUI to perform aligned mode superposition fatigue analysis. As identified above, if static_type =3 and/or dynamic_type = +/-3 or static_type = +/-4 and dynamic_type = +/-4 results in the either the static or dynamic shape to be aligned, there are no equivalent SCRIPT or GUI commands to replicate this scenario as ALIGNSTRESS cannot be used to align dynamic into static or align static into a summation of dynamic shapes. Access to fatigue results is only available if write = 1.

write = 1 implications:

- The fatigue results (static stress, dynamic stress, % limit) reported (via a non-detailed snapshot report) or plotted are the result of each node having a set of modal scale factors resulting in a maximum % limit for that node, i.e., the modal scale factors from node-to-node are not necessarily the same.
- There is no procedure to replicate these results within the GUI and/or SCRIPT regardless of the value of static_type & dynamic_type other than evaluating each node independently.

**Arguments: (Details in Description)**

- static_type: (-1=MIN PRINCIPAL, 1=MAX PRINCIPAL, 2=VON MISES, 3=ALIGNED, -4, 4=R RATIO), INTEGER
- dynamic_type: (1=MAX PRINCIPALS, 2=VON MISES, -3, 3=ALIGNED, -4, 4=R RATIO), INTEGER
- mode_scales: 1-D array with length equal to the number of modes in the SDR file, FLOATS
- static_case(OPTIONAL, default=0): Static case index, 0 for no static case, INTEGER
- static_scale(OPTIONAL, default=1.0): Static scale factor, FLOAT
- write(OPTIONAL,default=0): Flag to retain each node's highest modal scale factor results (0=false, 1=true), INTEGER.

> [!NOTE]
> If write is used it is STRONGLY recommended that FATCLEARAMPS be invoked as soon as either reporting and/or plots are completed. In addition the only recommended commands to be executed if write=1 are PICFAPAGE, PICFAPLOT and RPTFASNAP (with arg3 = 0) prior to issuing FATCLEARAMPS.

**Returns:**

- Returns an object containing the following members for the most limiting node (highest % of limit):

  > - MSF - Modal scale factors or mode amplitudes. An array of MSF values, float.
  > - Group - Name of the group containing the limiting node, string.
  > - Plimit - % Dynamic Limit, float.
  > - Limit - Dynamic Limit, float.
  > - Node - Node label, integer.
  > - StaticStress - The static stress value, float. This is the value used to generate the limiting nodes' dynamic limit.
  > - DynamicStress -  Dynamic Stress value, float
  > - StaticType - Type of static stress (1=MAX PRINCIPAL, 2=VON MISES, 3=ALIGNED)
  > - DynamicType - Type of dynamic stress (1=MAX PRINCIPALS, 2=VON MISES, 3=ALIGNED)

**Example:**

> `fat = GM.fatigue()`
>
> `-- Modal scaling factors are an array, which is defined like so`
>
> `msf = {0,0,0,2e-5,0,0,0,0,1e-5,1e-5}`
>
> `-- Find a superposition using static max principal and dynamic max principals`
>
> `msuper = fat.mode_sup(1,1,msf,1,1)`
>
> `-- print result of superposition`
>
> `log("Superposition Results for Limiting Node:")`
>
> `log("\t        Length: " .. msuper.MSF.length)`
>
> `log("\t          Node: " .. msuper.Node)`
>
> `log("\t         Group: " .. msuper.Group)`
>
> `log("\t Static Stress: " .. msuper.StaticStress)`
>
> `log("\t   Static Type: " .. msuper.StaticType)`
>
> `log("\tDynamic Stress: " .. msuper.DynamicStress)`
>
> `log("\t  Dynamic Type: " .. msuper.DynamicType)`
>
> `log("\t Dynamic Limit: " .. msuper.Limit)`
>
> `log("Participation coefficients:")`
>
> `for i=1,msuper.MSF.length`
>
> > `log("\tMode: " .. i .. "=\t" .. msuper.MSF[i])`
>
> `end`

## report_limits(filename, [type])

**Description:**

Save the modal limit report to a file.

**Arguments:**

- filename: File name (Without Path) for the report file, STRING
- type(OPTIONAL, default="TXT"): File type ("TXT"=text file, "MAT"=MATLAB file), STRING

**Example:**

> `infolder = "c:/tmp"`
>
> `fat = GM.fatigue()`
>
> `fat.report_limits("limits.txt")`
>
> `fat.report_limits("limits_matlab.mat", "MAT")`

## report_page(filename, [page], [width], [height])

**Description:**

Saves a PNG picture of the requested plot page to a file.

**Arguments:**

- filename: File name (without path), STRING
- page(OPTIONAL, default=1): Index of the page to save, INTEGER
- width(OPTIONAL, default=1600): Width resolution of output image, INTEGER
- height(OPTIONAL, default=1200): Height resolution of output image, INTEGER

**Example:**

> `infolder = "c:/tmp"`
>
> `fat = GM.fatigue()`
>
> `fat.report_page("page2.png", 2, 640, 480)`

## report_plot(filename, [page], [row], [column], [width], [height])

**Description:**

Saves a PNG picture of the requested plot.

**Arguments:**

- filename: File name (without path), STRING
- page(OPTIONAL, default=1): Index of the page to save, INTEGER
- row(OPTIONAL, default=1): Row of the plot to save, INTEGER
- column(OPTIONAL, default=1): Column of the plot to save, INTEGER
- width(OPTIONAL, default=1600): Width resolution of output image, INTEGER
- height(OPTIONAL, default=1200): Height resolution of output image, INTEGER

**Example:**

> `infolder = "c:/tmp"`
>
> `fat = GM.fatigue()`
>
> `fat.report_plot("page2plot3.png", 2, 2, 1, 640, 480)`

## report_sensor(filename, type)

**Description:**

Saves the sensor limit and ratio report to a file.

**Arguments:**

- filename: File name (without path), STRING
- type(OPTIONAL, default="TXT"): File type to write out ("TXT"=text file, "MAT"=MATLAB file), STRING

**Example:**

> `infolder = "c:/tmp"`
>
> `fat = GM.fatigue()`
>
> `fat.report_sensor("sensors.txt", "TXT")`

## report_snapshot(filename, type, [detailed])

**Description:**

Saves the detailed or simplified snapshot report to a file.

**Arguments:**

- filename: File name (without path), STRING
- type(OPTIONAL, default="TXT"): File type to write out ("TXT"=text file, "MAT"=MATLAB file), STRING
- detailed (OPTIONAL, default=1): Whether to write out all additional information (0=false, 1=true), INTEGER

**Example:**

> `infolder = "c:/tmp"`
>
> `fat = GM.fatigue()`
>
> `fat.report_snapshot("snap.mat", "MAT", 1)`

## limit_export(atCritical, ComponentName, FileName)

**Description:**

Exports a scope limits CSV file.

**Arguments:**

- RPM: RPM at which to export calculated limits, DOUBLE
- atCritical: ratio sensor strains at critical location (TRUE) or max dynamic stress (FALSE), BOOLEAN
- ComponentName: Name of component, STRING
- FileName: File name (with path), STRING

**Example:**

> `infolder = "c:\tmp"`
>
> `fat = GM.fatigue()`
>
> `gm = GM.main()`
>
> `gm.set_rpm(0,10000)`
>
> `fat.limit_export(false,"C1",infolder .. "Limits.csv")`
