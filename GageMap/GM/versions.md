# GageMap Version History

## Version 3.14.12

### GM Base

- Fixed crash when doing CSS phase search with NSMS sensor (#102335)
- Corrected naming and values for von Misses and max/min principal stresses in the Model Informaiton report (#102350)

### GM Script

- Fatigue assessment bug fixes (#102191, #102193)

### SdrConverter

- Fixed occasional crash
- Improved speed for large models and defined coordinate systems in RST

## Version 3.12.23

### General

- Corrected crash from core library error.

## Version 3.12.20

### General

- Corrected various bugs and performance issues reported by users among these the most notable can be seen below.

### GmScript

- Mode sup algorithm improved.
- Corrected crash when writing BCX.
- Image export of fatigue task corrected.

### GM-LegacyUI

- List Frequency and ND next to mode in optimizer window.
- Show in-variants in Node Info Dialogue.

## Version 3.12

### General

- Versioning reverted back to Major.Minor.Micro.Tick rather than Year.Minor.Micro.Tick. This was done to better distinguish between the current generation GageMap and the next generation GageMap.
- Licensing changed to use composite host ID’s and new APEX Host daemon. LICENSING WILL HAVE TO BE RE-KEYED. Please refer to: [https://documentation.docs.edasglobal.com/FlexLicensing/migration.html](https://documentation.docs.edasglobal.com/FlexLicensing/migration.html)
- All GageMap products changed over to GCC 6.3 toolchain for LINUX and use of MSVC 2017 for Windows.
- Corrected issue: Geometry loaded but no modes for files > 2 GB
- Linux packages changed over to be in standard RPM and DEB packaging. A tar.gz archive is also available for easy extraction.
- Linux packages removed the need for a shell wrapper.
- Linux packages require X11 and libXcb libraries on Linux. This requirement is imposed by the graphics toolkit.

### Minimum Supported Systems

- LINUX: Linux systems must be newer or equal to RHEL 7.0 and UBUNTU 16.04
- WINDOWS: Windows systems must be newer or equal to Windows 7.

### SDR Converter (SdrConverter.exe)

- ansys2sdr, aba2sdr, and nas2sdr have been combined into a single tool: SdrConverter.
- ANSYS version 17, 18 and 19 supported. Earlier versions supported but no QA was performed.
- ABAQUS API for version 2018 supported. ABAQUS API may upgrade earlier ODB files prior to conversion.
- Permits creation of multiple jobs for conversions.

### GmScript

- Fixed various issues with regards to file looping in SDRFM, GM, and exporting
- GM.main().node() extended to include whether or not it is a mid-side node and the thickness
- Close function added to SDRFM and GM for multiple file processing
- All output articles have been set to use the set output path unless an absolute path is specified
- Corrected issues with virtual mode shapes in SDRFM
- Reduced amount of logging
- Additional module added: SdrConverter - ansys module still supported
- GmScript -v prints the current version of GmScript
- Version 3.12 stability issue. If the script is exiting with an error it may be due to the "set_overwrite" not being set or set to "false". Set GM.set_overwite to "true".

### GageMap

- Space Mouse support added
- Added panel for adjusting sensitivities for the Space Mouse
- Corrected issue where speed was not exported to Limits file
- Corrects issue where setting a high number of contour levels caused a freeze
- Non-Linear static loads strains and stresses for gage computations use the average of the imported strains/stresses from the FEA application

### Known Issues

- No support for Linux license servers. There is an issue with the new Flexera modules & GageMap with Linux based license servers that prevents serving of either GageMap or GmScript licenses.
- Linux versions of GageMap that utilize a Windows license server may require restarting the application to acquire a valid licenses.
- Shell element imported strain & stresses may be incorrect. Imported values for shell elements should be checked against values in the FE solver prior to beginning a GageMap analysis. The conversion process has issues consistently averaging values from the upper & lower surfaces in some instances.
- Occasional crashes can occur in the conversion of ANSYS files. This appears to be related to the ANSYS API, and mainly for cyclic files.

## Version 2017.3.1

### ANSYS Converter

- Corrected issue where temperature "BF" commands could not be found in the CDB

## Version 2017.3

### General

- New versioning numbers
- Licensing Panels have been updated
- Package installers for both linux and windows are graphical
- Command line package installers available for linux
- Install names and locations have been updated
- Graphical installers for linux dynamically create the shell wrapper script for application execution
- XCB libraries are now **REQUIRED** to run GM applications. Please be sure the needed libxcb libraries are installed on linux systems

### GageMap

- Application updated to use latest APEX CORE
- Application updated to use latest libraries for its components
- Application is c++11 optimized
- Application has been updated to use QT 5.8 for part of its UI and a lot of its core functions
- Feature to specify strain gage color has been added
- Feature to Specify Model color has been added
- Feature to specify color of plate element negative face has been added
- CSS phase search can now normalize sensor results to a specified group
- Quantity optimizer updated to use max available threads from the OS
- Model manipulation updated to minimize calculations on every screen refresh
- Model manipulation updated to go into wireframe mode for large models
- Model animation updated speed enhanced
- NSMS optimizer removed. Please use the newer tool available on the User's site
- Limit export updated to latest limit file format
- Limit export no longer allows specifying RPM. RPM must be set in the fatigue task
- Print support removed from GageMap. Printing to PDF of HTML is supported
- Memory leak in model exporter resolved
- Sensor mapping calculations improved
- Fatigue task corrected to update when applying a stress adder
- Phase search corrected to not re-run on every action in the dialog
- GM has been tested to support models of >2M nodes and >10 mode cases. It is reccommended to have a computer with more RAM than 2 X the SDR file size. A decent GPU and CPU is reccommended as well.

### GmScript

- The Off Screen rendering library has been updated to the latest version (libOSMesa 17.0.0)
- Modesup command updated to use the maximum allowable threads for computation
- RPM option in the export_limits command has been removed. User must first set the RPM using set_rpm
- Lua library updated to 5.3

### ANSYS Converter

- Version 18.1 supported
- Duplicate sector is no longer required for Cyclic models
- **STRICT** Policy that every node and element defined in the CDB exist within a solution
- Issue corrected for materials definition being blank
- Solution loading function improved to consume less memory
- Converter overall improved for large models (53 GB RST + 1 GB CDB loaded w/o issue during QA)

### Abaqus Converter

- abqconvert DLL re-built with latest updates explained above

### SDRFM

- Various bug corrections

## Version 3.8.2

### GageMap

- Corrected issue involving gage mapping on tet 10 and tet 4 elements.
- Corrected issue of GM icon not displaying for Windows versions
- In the Animate task, the increment and decrement buttons for mode amplitude have been improved.

### ANSYS Converter (ANSYS2SDR)

- Minor corrections made

### GmScript

- Corrected issue involving returned node index in the modesup command
- Documentation for 3.8.0 command additions added.

## Version 3.8.0

### GageMap

- Gage locations, displacements, rotations, & strain calculations re-worked and optimized.
- Full sensor misplacement report added
- Gage displacements/rotations added to detail sensor report
- Sensor summary report updated for complex mode shape
- UI improvements made
- Model animator defaults to auto-scale mode.
- Limits export function updated to current format

### SDR File Manager (SDRFM)

- UI improvements made
- Issue in cyclic exporting corrected

### ANSYS Converter (ANSYS2SDR)

- Ansys version 16 files supported
- Minor fixes made
- Now allows for multiple static solutions to be defined in a single RST(p) file, where the converter will search for the appropriate static solution for the supplied CDB and additional RST files.

### GmScript

- The following functions have been added:

  > - GM.Sensors() function group:
  >
  >   > - **gage_perturb**: Perturbs gage at a given dx, dy, and dTheta.
  >   > - **gage_perturb_X**: Perturbs gage at a specified dx
  >   > - **gage_perturb_Y**: Perturbs gage at a specified dy
  >   > - **gage_perturb_Theta**: perturbs gage at a specified dTheta
  >   > - **gage_strain**: returns eX, eY, and eXY for given gage and mode
  >   > - **gage_stress**: returns ex, eY, SigmaX, SigmaY, tauXY, vonmises, SigmaMax, SigmaMin, TauMax, and Theta for the given gage and mode
  >   > - **gage_misplacement_coeffs**: Returns gage misplacement coefficients and fit statistics
  >   > - **gage_misplacement_maxmins**: Returns the mislacement table seen in the sensor summary report at the specified mode for the given gage
  >   > - **misplacement_prefs**: Can set or retrieve the gage misplacement bounds
  > - GM.Fatigue() function group:
  >
  >   > - **limit_export**: Exports the scope limits file
  > - GM.SDRFM() function group:
  >
  >   > - **nnodes**: returns the number of nodes in the model
  >   > - **node**: returns info for the given node
  >   > - **shape_info**: returns info for the given shape
  >   > - **list_freq**: returns a list of the mode frequencies

## Version 3.6.4

### GageMap

- Sensor Summary report updated to output sensor misplacement table in scientific notation.
- Corrects issue involving a failure to update Group information in fatigue task.
- Optimization added to Quantity Optimizer routine.
- Corrects issue involving Quantity Optimizer not covering all modes in specific cases.

### ANSYS Converter (ANSYS2SDR)

- Corrected bug that appeared to cause crash for large files.
- Corrected bug involving a  memory allocation issue for large files.
- Added progress bar in Report panel in order to retain communication with Windows event structure. This helps to prevent the "Program is not responding" message in Windows.
- As of Version 3.6, the Ansys Converter requires all elements and element nodes defined within the CDB to be contained within a solution.

### SDR File Manager (SDRFM)

- Corrects issue involving in correct results in mode arithmatic function.

### Scripting

- Corrects issue involving Collections function outputting a file in Windows. Issue involved incorrect format for windows file names.

## Version 3.6.2

### GageMap

- Updates licensing technique to base licenses on maintenance date instead of version number
- Corrects issues with Matlab fatigue reports
- Corrects scientific notation display in NSMS reports

### Scripting

- Under fatigue().report_sensor() the following has been modified:

  > - fatigue_sensor_strain_report
  >
  >   > 1. Cell Matrix with Dimension: num_fatigue_modes x num_fatigue_sensors
  >   > 2. Each Cell contains the following 14 items:
  >   >
  >   >   > 1. Nodal Diameter (Integer) – Will always be zero if the model is non-cyclic
  >   >   > 2. Modal Frequency (Real)
  >   >   > 3. Amplitude (Real) – The amplitude at which the critical node reaches the fatigue limit
  >   >   > 4. Nominal Vibratory Ratio (Real)
  >   >   > 5. Nominal Vibratory Node (Integer)
  >   >   > 6. Nominal Critical Ratio (Real)
  >   >   > 7. Nominal Critical Node (Integer)
  >   >   > 8. Nominal Limit (Real)
  >   >   > 9. Minimum Vibratory Ratio (Real)
  >   >   > 10. Minimum Critical Ratio (Real)
  >   >   > 11. Minimum Limit (Integer)
  >   >   > 12. Maximum Vibratory Ratio (Real)
  >   >   > 13. Maximum Critical Ratio (Real)
  >   >   > 14. Maximum Limit (Real)
  > - fatigue_sensor_stress_report
  >
  >   > 1. Cell Matrix with Dimension: num_fatigue_modes x num_fatigue_sensors
  >   > 2. Each Cell contains the following 14 items:
  >   >
  >   >   > 1. Nodal Diameter (Integer) – Will always be zero if the model is non-cyclic
  >   >   > 2. Modal Frequency (Real)
  >   >   > 3. Amplitude (Real) – The amplitude at which the critical node reaches the fatigue limit
  >   >   > 4. Nominal Vibratory Ratio
  >   >   > 5. Nominal Vibratory Node
  >   >   > 6. Nominal Critical Ratio
  >   >   > 7. Nominal Critical Node
  >   >   > 8. Nominal Limit
  >   >   > 9. Minimum Vibratory Ratio
  >   >   > 10. Minimum Critical Ratio
  >   >   > 11. Minimum Limit
  >   >   > 12. Maximum Vibratory Ratio
  >   >   > 13. Maximum Critical Ratio
  >   >   > 14. Maximum Limit

### Nastran Converter (NAS2SDR)

- Corrects possible crash when running

### Abaqus Converter (ABA2SDR)

- Corrects corrupted abqconvert DLL **(Windows)**

### ANSYS Converter (ANSYS2SDR)

- Corrects issue with importing nodal diameter from RST solution header

## Version 3.6

### GageMap

- Strain Gage Validation task updated and added to Tasks Menu
- Model Validation task renamed to Vibrometry Validation
- Quick launch tool bar moved next to menu items
- GageMap Logos updated
- Issue resolved involving NSMS sensor adjustments
- Issue resolved involving Circumferential Optimization task not working in Linux
- Issue resolved involving mapping gages to bottom surface of Quadratic Shell models
- Quadratic Shell calculations updated
- Mapping of NSMS sensors have been re-worked to correct issue of mapping across similar geometries
- SDR file format updated and **WILL NOT** load in prior versions

### Scripting

- "EDAS" function directive changed  to "GM" (Former is still supported)
- "gagemap" function group changed to "main" under GM function directive
- Strain gage validation task added to Scripting as function group "validate()"
- The following functions are available under the validation task function group:

  > 1. load_ex(filename)
  > 2. set_modes(modes)
  > 3. run_validation(useMac,dxTol,dyTol,dthetaTol,shapeWeight)
  > 4. mac()
  > 5. mfdp()
  > 6. mode_pairs()
  > 7. results()
  > 8. apply()
  > 9. save_sga(filename)
  > 10. ex_strains()
  > 11. ex_frequencies()
  > 12. gm_strains()
  > 13. gm_frequencies()
  > 14. ex_scaled()
  > 15. loaded_gages()

### ANSYS Converter (ANSYS2SDR)

- Use of ANSYS API now supported
- ANSYS v15 files are now supported
- Support of SECBLOCK updated and saved in SDR file

### General

- Install location for Linux updated to /opt/GageMap
- Install location for Windows updated to C:\Program Files\GageMap

## Version 3.4.2

### GageMap

- Corrects issue of phase sweeping in Sensor summary report for cyclic models.
- Adds footnote in Detailed and summary sensor reports stating the phase sweep increment.
- Phase sweep increments used in reports can be changed by running the "CSS Phase Search" task with the desired increment.
- Corrects issue in fatigue assessment task where internal nodes were not being considered as limiting nodes.
- Corrects issue involving incorrect temperatures being assigned to nodes when an elemnt contains midside nodes.
- Fatigue assessment export "Model setup to DataDetective" has been changed to Scope Limits.
- Corrects issue when mapping NSMS sensors.
- Corrects issue in fatigue assessment task where the selected plot would follow the users subsequent mose clicks.

### Scripting

- Corrects issue where the fatigue assessment would not display contours after the animation task had been run.
- Corrects issue of reading in collections.
- The following functions have been added to the collections task:

  > 1. nrows()
  > 2. ncols()

### ANSYS Converter (ANSYS2SDR)

- Corrects issue in assigning correct nodal transformations when converting cyclic models.

## Version 3.4

### GageMap

- NSMS Blade Tip Panel moved to Sensor Editor's **Tools** menu.
- NSMS Blade Tip information saved to SGA and SDR files.
- NSMS reports have been updated.
- CSS Phase Search Reports have been updated to not include static load cases.
- Corrects issue in CSS Phase Search when viewing grouped regions.
- Corrects issue in Quantity Optimizer involving all modes not being covered in select cases.
- SDR File updated. File format will **NOT** be able to be opened in earlier versions.
- Fatigue Assessment Task now allows assessment to be performed for Static Aligned & Vibratory Aligned.
- Sensor reports have been updated in presence of cyclic symmetry.
- Handling of Shell elements revised. (4 Node Only).
- Corrects issue in viewing node selections in grouping task.
- Corrects issue in dynamically updating model maximums report.
- MAT file export variable extended.
- Note concerning optimization process for cyclic modes added to documentation.
- File open dialog now only has the following loading options:

  > 1. Load Shapes
  > 2. Load Gages
- Issue involving crash for too long of a sensor name has been resolved.
- Blade tip search now requires input of 2 axis.
- License splash screen has been updated.
- "Upgrade" items have been removed in licensing. Licenses are now in the format of "GageMap or "Scripting".

### Scripting

- Mode Superposition inputs have been extended to include Minimum Principal Stress.
- Default output location set to Script's containing directory.
- Contour Plots issue has been resolved.
- If OutDir does not exist, the program will create it.
- Mode_Sup issue involving assign adder being 2X display on plot has been resolved.
- max_phase issue involving incorrect values returned has been resolved.
- Issue involving sensor reports not outputting correctly has been resolved.
- SDRFM separate logging has been changed to output into the main log file.
- Report_Snapshot is now able to create directories, getting rid of prior file creation errors.
- Issue involving contour plots not displaying has been resolved.
- sdrfm.export_vmode issue has been resolved.
- Scripting documentation has been updated
- **NEW** features added:

  > - gagemap.list_freq - lists frequencies and nodal diameters for each mode
  > - sdrfm.group_info - returns group name, number of nodes, and opcode
  > - sdrfm.ngages - returns number of gages
  > - sdrfm.ngroups - returns number of groups
  > - gagemap.gage_info & sdrfm.gage_info - returns sensor name, type, and location
  > - gagemap.isRPM - returns true if the load case is RPM based
  > - gagemap.getRPM - returns the RPM for the load case
  > - optimize.quantity_optimize - sensor quantity optimization routine
  > - optimize.apply_design - applies a design to the model
  > - sensors.geom_remap - Hot/Cold geometry remapping of gages

### Ansys Converter

**IMPORTANT PLEASE READ**

- Cyclic Symmetry Conversion requirements are as follows:

  > 1. A CDB file is required due to the CDB containing information for which the converter relies.
  > 2. The CDB and RST **MUST** contain both the basic and duplicate sectors.
  > 3. The RST **MUST** contain the solutions for **ALL** nodes and elements defined in the CDB.
  > 4. **ALL** Geometry defined within the CDB **MUST** exist in the RST.
- Corrects issue found in converting shell elements.
- Material properties loading issue has been resolved.
- Issue loading temperture data using commands "BF,ALL" and "BFUNIF" has been resolved.
- Issue involving 0's being reported for Shell 2nd surfaces has been resolved.
- Issue involving incorrect values for Material properties in log file has been resolved.
- Duplicate static load cases issue resolved.
- Shell thickness now able to be pulled from SECBLOCK in cdb file

### Abaqus Converter

- Abaqus libraries updated to version 6.14-1
- Corrected issue in linux where the abaqus libraries were required to be placed in /usr/lib64/abaqus. Now, the user can have the libraries in any directory as long as the directory is specified in the aba2sdr shell script wrapper.

## Version 3.2

### GageMap

- Visual improvements to the 3d model view, including speed optimizations
- New model selection information widget with fewer issues
- Various Improvements to the UI
- 'Copy to clipboard' is enabled again for Linux. No issues seen.
- New packages; tentative end of 32-bit support and specific packages for various executables
- Grouped windows in taskbar are now properly titled
- Fixed a crash when printing plots to image files under Windows

### Scripting

- GmBatch is no longer able to be supported. Use GmScript.
- Mode superposition is now significantly faster
- MSF coefficients for Mode superposition can now be small numbers (< 1) without an issue that was happening under Windows
- Defunct GmBatch is gone.

### Ansys Converter

- Ansys 14.5 is now supported
- Most column widths in CDB files are no longer a concern

### Abaqus Converter

- Abaqus 6.12-3 is now supported

## Version 3.0.8

### Scripting

- Fixed windows issues with floating point precision in Mode Superposition
- Fixed a bug that prevented old optimizer configuration files from opening

## Version 3.0.6

### GageMap

- Console window is no longer present in GUI applications
- New instructions for ANSYS and MATLAB usage ... no more DLL copying

### NASTRAN Converter

- New handling for cyclic symmetry conversions

## Version 3.0.2

### GageMap

- Fixes to the progress bar in the optimizer
- Fixes to ABCD and Misplacement values in the sensor text reports

### ABAQUS Converter

- Packages are now available for all systems except Linux 32-bit

### NASTRAN Converter

- Fixed bug that would cause converter to hang usage of a file after conversion
- Fixed element degrading logic

### GmScript

- Fixed glitch in collections which caused added fields to work improperly

## Version 3.0

### GageMap

- Support added for 3Dconnexion Motion Controllers.
- Vibratory strain validation added to the Model Validation task.
- New strain gage optimization method added to determine minimum sensor count at a provided sensitivity/ratio.
- Fixed numerous MATLAB™ related memory leaks that would cause excessive memory usage each time a MAT file was created.
- MATLAB is now an optional installation package that is dynamically loaded as required. It is highly recommended that GageMap be executed from a computer with MATLAB installed if it desired to use the MATLAB interface.
- ABAQUS™ interface is now an optional installation package that is dynamically loaded when needed. It is highly recommended that the ABAQUS converter be executed from a computer with ABAQUS installed.
- Help system is now HTML based.
- Gage temperature added to detailed sensor report.
- GageMap GUI and batch log file reflect 32 or 64 bit version.
- Added model background color options.
- Gage misplacement model error coefficients calculated and reported.
- Polygon & lasso selection methods available for grouping.
- Fatigue Assessment task - Identify limiting node on plots as applicable.
- Fatigue Assessment task - Limiting node information listed in contour legend.
- Fatigue Assessment task - Additional GMF command, assignadder for application of a constant stress to either dynamic or static stress just prior to calculation of the fatigue limit.
- Fatigue Assessment task - simplified snapshot report available.
- Fixed truncation of legend when printing fatigue assessment plots.
- In the Grouping Task, for any group of type "Nodes" that is selected, nodes on the model will be highlighted. This should remove confusion regarding what nodes are members of the group.
- Removed support for JPEG images under Linux, PNG still supported.

### ANSYS Converter (ANSYS2SDR)

- Support for ANSYS v14.0
- Option to maintain element results in element coordinate system.
- Updated nodal averaging to consider only one instance per element definition in node average. Previous averaging considered all nodal instances in an element definition.
- Normalization removed as an option for both GUI and under batch. Scaling of static and dynamic shapes may be performed within the SDR File Manager.
- Support for SOLID186 & SOLSH190, however materials associated with layered sections of SOLSH190 are not supported.
- Fixed improper identification of non-linear geometry.

### GmBatch

- New Beta for GmScript exists. Batch will officially be deprecated in favor of the new LUA format.
- Several collections commands added to permit interface with Workflow.
- MAXSHAPE command to return maximum values for any static or dynamic shape.
- FATIGUENODE command to return fatigue related information regarding any node.
- MODESUP command added to perform mode superposition.
- FATAMP command added to set amplitudes to modes individually. Similar to ANIMAMP command.
- FATRPM command added to set centrifugal load case RPM, similar to ANIMRPM command.
- A simplified snapshot report is now the default. The detailed snapshot is still available but is not the default. See RPTFASNAP for details.
- READMATCURVE command added to return limit information for any curve at any stress without an existing node

## Version 2.10

### GageMap

- Increased file overwrite detections.
- Removed JPG saving because of a bug; now images always save to PNG.
- Options to toggle on/off display properties (legend, color bar, file path, max/min indicators)
- 32 & 64 bit identifications added.
- Dialogue entry verification.
- Sensor temperature listed in the Detailed Sensor Report.
- Detailed Sensor Report correctly reports angle to maximum principal direction in degrees.
- Fixed NSMS placement crash.
- Fatigue Assessment - Limiting node identified within legend of HCF contour.
- Fatigue Assessment - Limiting node identied on all fatigue assessment plots.
- Fatigue Assessment - Fixed bug that caused Goodman legends to be cut off when exported.
- Fatigue Assessment - Fixed crash when opening a GMF file where more loads or modes are defined than the model actually has.
- Animation - Max/min indicators only displayed of node resides in current view..
- Optimizer - Advanced Amplitude Options - Select All under Minimum Ratios slects all modes.
- Optimizer - Icon now active for cyclic models in magnitude & phase mode.
- Grouping - Lasso and polygon face selections.

### Converters - All

- Output directory can now be specified under Linux.
- New option to retain element results (strain & stresses) in local coordinate system.

### ABAQUS Converter (ABA2SDR)

- Utilizes TMPDIR environment variable for conversion process.

### ANSYS Converter (ANSYS2SDR)

- Support for SOLID186 & SOLSH190
- Create & Edit Sensors

### GmBatch

- Increased stability resulting from user input errors.
- Two new commands:  MAXSHAPE and FATIGUENODE
- Removed JPG saving because of a bug; now images always save to PNG.
- RPTFASNAP will now create the provided directory if it doesn't exist.

### SDR File Manager

- Fixed icon placement.
