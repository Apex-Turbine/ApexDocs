# Fatigue Tab - Performing Assessments

## Preliminaries

The Fatigue Assessment task is model based tool based on a constant life (Goodman/Haigh) diagram (stress-life).  Fatigue Assessment should be used to define mode-based limits before a test.  It can also be used for post-test determination of "HCF margin" based on measurements.

The Fatigue Assessment task is designed to perform the following functions:

1. Generalized plotting of fatigue parameters (percent limit, static and vibratory stresses, coordinates).
2. Assignment of fatigue material properties based on group membership.
3. Multiple methods of fatigue material property temperature interpolation as well as user programmable interpolation via a DLL.
4. Plotting properties based on group membership.
5. Extensive reporting including generation of sensor limits and ratios.

If the fatigue assessment is to be performed on a group basis, i.e., groups are to be used to assign plot properties, materials, scalars and/or adders, the Boolean of the group and the order the groups appear within the grouping task become important. In order for a group to be available for assignment of fatigue properties it must have a Boolean (function) of Or or And. Groups that are disabled or have function Not will not be available. In addition, nodes can be a member of one and only one group. The group membership is determined by the top-down order of the groups within the grouping task. The lowest group that contains the node takes precedence and therefore, will be removed by all groups above. Any nodes that are not a member of any group are assigned to the "Default" group. The "Default" group is available within the fatigue task.

## Pre-Task Check List

Before entering the fatigue assessment task, confirm:

> - Model representation is valid (expanded cyclic symmetry model is acceptable).
> - - **Groups & their respective membership profile (recall a node can be a member of one and only one group)**: - It is advised that ALL nodes be assigned to at least one group or nodes not assigned to a group be removed from the model
>   - Sensor design (required for generating limits)
> - Stress-life material fatigue properties (static stress & dynamic stress)
> - For post-test analysis:  Modal amplitudes

### Fatigue Material Properties

The limits section lists the currently loaded material fatigue limits.  By default GageMap uses an internally derived limit diagram based upon the model characteristics. This is for notional use only and should not be used for fatigue evaluations. User material fatigue limit properties can be entered via the GageMap preference (.gmf) file. The format of the material properties within the preference file is provided below. A preference file is loaded within the main fatigue assessment window under the File menu. For legacy users there is also an option to import .glm files within the File menu, however, this is not the preferred method and support for this format may be dropped in a future release.

#### Fatigue Material Specification

`CLEAR,MATERIALS` (clears all current material definitions)

material,<material name>,<# of temperatures>
curve,<material name>,<temperature index>,<temperature in model units>,<number of points (n pairs)>,<static limit for pair 1>,<dynamic limit for pair 1>,...,<static limit for pair n>,<dynamic limit for pair n>
repeat above as necessary for each material
An example material (.gmf):

> `START,FATIGUE`
>
> `CLEAR,MATERIALS`
>
> `material,Airfoil Material,5`
> `material,Disk Material,1`
> `material,LE Material,1`
> `material,TE Material,1`
> `material,Tip Material,1`
> `material,FOR Material,1`
> `material,AFT Material,1`
>
> `curve,Airfoil Material,1,70,3,-100000,0,0,100000,100000,0`
> `curve,Airfoil Material,2,100,3,-90000,0,0,90000,90000,0`
> `curve,Airfoil Material,3,200,3,-80000,0,0,80000,80000,0`
> `curve,Airfoil Material,4,300,3,-70000,0,0,70000,70000,0`
> `curve,Airfoil Material,5,400,3,-60000,0,0,60000,60000,0`
> `curve,Disk Material,1,70,3,-200000,150000,0,150000,200000,0`
> `curve,LE Material,1, 70,3,-60000,0,0,60000,60000,0`
> `curve,TE Material,1, 70,3,-60000,0,0,60000,60000,0`
> `curve,Tip Material,1, 70,3,-60000,0,0,60000,60000,0`
> `curve,FOR Material,1,70,3,-200000,150000,0,150000,200000,0`
> `curve,AFT Material,1,70,3,-200000,150000,0,150000,200000,0`
>
> `FINISH`

The material data is viewable by under Fatigue Material Properties. Each material is listed in the order it was created along the temperature and points defining the limit curve.  Entries cannot be modified within GageMap. Modifying entries requires modification and re-loading of the material preference file.

### Mean Stress Alignment

> - Project static stress tensor into the vibratory principal direction
> - - **Storage of a single “mean stress aligned” static variable**: - Fatigue assessment task
>   - Animate task
> - - **Process**: - Select static load case
>   - - **Select vibratory tensor for alignment**: - Stress
>     - Strain
>   - - **Select static variable for storage**: - Max prin, mid prin, min prin
>     - XY, YZ, ZX shears
>   - - **Export**: - Static / vibratory stress and strain principal directions are available for export
>     - Aligned static stress and strain tensors are also available in model export

### Pre-Test Fatigue Assessment

> 1. Launch GageMap and load an SDR or GMP file.
> 2. If gages are not already mapped, map them.
> 3. Load a group file and confirm the order and Booleans are correct.
> 4. Navigate to the "Fatigue" tab
> 5. On the left side panel, navigate to the "fatigue setup" tab
> 6. - **If materials have not already been loaded with the GMP file, set up the materials for the model as follows:**: 1. Create a new fatigue file with the "New Fatigue File" button. The new file will appear in the "files" section of the Fatigue Setup Tab.
>   2. Locate the Green "+" button towards the bottom of the panel, next to "Material:" to create a new material
>   3. Name the New Material using the now unlocked text box
>   4. A Temperature field and a X, Y Value field will be created automatically under the new material
>   5. Change the Temperature value by selecting it in the tree in the materials box, and changing the value in the "Temperature:" field
>   6. Once this is done, change the X and Y values by selecting it in the tree and changing the values in the corresponding fields
>   7. Multiple values can be added to a given temperature by clicking on the green "+" button next to the X and Y value fields
>   8. Add a new temperature to the Material by click the green "+" button next to the "temperature:" field.
>   9. Repeat as needed
> 7. Materials can also be imported from Assignment files (GMM) or Legacy file formats (GMF)
> 8. Once materials have been defined, navigate to the "Assignments" tab in the left side panel
> 9. Select the active group file and define the active group in their respective dropdowns
> 10. Match the materials to the groups in the "Material" Dropdown
> 11. Select each group and confirm it is the correct material.
> 12. - **Define Static and Dynamic Stress types using their respective dropdowns**: - This can be done either on a material basis under the assignments tab or globally in the fatigue preferences panel
> 13. - **Assign stress scales and adders**: - Stress scales and adders can be used to artificially increase or decrease all of the stresses (stress type) in a group. They can be applied to both the static and dynamic stresses
> 14. - **Assign plot Identifiers**: - The plot identifiers dictate what colors & symbols to use for each group so they may be distinguished on the Goodman diagram.
> 15. Navigate to the "Plot Setup" tab
> 16. Select the Static Stresses and Dynamic Stresses for the X and Y-Axis values
> 17. Select the group to create the desired plot. The plot will appear in the bottom right panel
> 18. Navigate to the "Animate Setup" tab in the left side panel
> 19. Select a static load case and enter a speed in the "Static Load (RPM)" box under the "scaling" section
> 20. Select a mode and enter a value into the "Mode Amplitude" box under the "scaling" section
> 21. Besides manual scaling, mode amplitudes and static loads can be scaled by fatigue percent limit in the "Fatigue" tab of the Scaling section
>
>   > GageMap has scaled the dynamic stresses such that a single node lies at 100% of limit. The node is identified by a red “star” and the label is listed in the legend. For this mode it is in the Airfoil group.  Note in the setup panel, the mode amplitude to achieve 100% of limit is listed. Also review the model window as the model has been contoured to now display “% of limit”.
>   >
>   > The Sensor Limit & Ratio Report is the most important report in the fatigue task. It summarizes all the sensor ratio and scope limit information for all modes in a single report. When initiated GageMap loops through each mode in sequence, determines the MSF to achieve 100% limit and reports the following for each strain gage:
>   >
>   > > - MSF = Modal Scale Factor
>   > > - The critical HCF node
>   > > - The limiting vibratory node
>   > > - Critical stress ratio
>   > > - Vibratory stress ratio
>   > > - Scope limit
>   > > - Variation in limit/ratios due to sensor misplacement
> 22. Fatigue -> Sensor Limit and Ratio
>
>   > > [!NOTE]
>   > > The stress scope limit is in model units (0-Pk). The bounds of the min/max are set in the "Optimizer" task. If NSMS sensors are present, deflection units are also computed.
