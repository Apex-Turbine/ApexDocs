# DX Version History

see also: [Issues & Limitations](issues.md)

## 2025.50

**Sensitivity UI Improvements:**

> - Updated the Signals element with clearer instructions on how to apply sensitivity, including a new help button and improved target unit display for easier configuration.

**Grid ARD "All" Option:**

> - Added "All" option for bins in Grid ARD element to select all blocks of data instead of requiring users to enter a large parameter number (e.g. 9999999). This provides a clearer and more user-friendly interface.

**Parameter Display Number Formatting and Overflow Control:**

> - Added ability to configure significant figures and number formatting across different parameter display types. Users can now set specific formatting for LED displays, Gauge displays, Thermometer displays, and Text displays.

**Parameter Display Automatic Resizing:**

> - Fixed issue where RPM values would get clipped past 10,000 on Gauge displays. Text numbers now automatically resize when additional digits are displayed, preventing overflow and ensuring all values are visible regardless of magnitude.

**Offsetting Time:**

> - Added time offset functionality to allow alignment of files from different systems with +/- time nudging capabilities. Also improved support for maintaining symbol colors for strain gage names across multiple files in composite Campbell diagrams.

**Upper Threshold Option for Campbell Diagrams:**

> - Added upper threshold setting called 'Ceiling' to Campbell diagrams to complement the existing lower threshold, now called 'Floor.' This allows users to filter out peaks above a specified upper threshold, useful for isolating lower responding signals when high response peaks are present. This feature is separate from the Max Z range setting.

**RWX and Dewesoft Data File Processing:**

> - Fixed crash that occurred when processing RWX and Dewesoft data files.

**Waterfall Plot Setup Loading:**

> - Fixed crash that occurred when loading plot setup files containing Waterfall plots. This resolves stability issues when restoring saved plot configurations with waterfall visualizations.

**Merged Parameters File Processing:**

> - Fixed crash that occurred when processing files with merged parameters. This improves stability when working with parameter-merged data files.

**Dewesoft DXD to RAW File Conversion:**

> - Fixed issue where RAW files created from splitting and saving segments of Dewesoft DXD data files could not be read back into DX. The conversion process now properly handles speed traces and other parameters, allowing the converted RAW files to be processed as if they were recorded originally in that format.

**DATX Multi-Channel Reading:**

> - Fixed issue where DATX multi-channel files were not correctly reading channel names beyond the first channel. All channels now retain their proper names instead of being assigned generic labels like C0002, C0003, etc.

**Playable Plots Block Number with FFT Overlap:**

> - Fixed issue where playable plots displayed incorrect block numbers when FFT overlap was set to anything other than 1x. Block numbers now correctly align between Time plots and History plots, ensuring that data values match exactly for the same block. The offset issue where 2x overlap caused a 1-block offset and 4x overlap caused a 2-block offset has been resolved.

**PDF Generation for Multiple Files:**

> - Fixed crash that occurred when generating PDF files in batch mode, particularly when processing multiple Dewesoft DXD files. The system now properly handles batch PDF creation without crashing during file output. Additionally, improved batch compatibility for creating composite plots with multiple overlaid traces from the same file, such as all gages from one rotor or speed trace overlays.

**Autoscaling RPM Plots with Spike Filter:**

> - Fixed issue where RPM history plots and speed Campbell plots incorrectly autoscaled the RPM axis minimum to zero instead of the actual minimum RPM value when using a spike filter between the Signals element and FFT element. The RPM axis now correctly autoscales from minimum to maximum RPM values, providing properly scaled plots for accel/decel runs.

**Plot Block Number Manual Entry:**

> - Fixed issue where manually typing a block number in Time plots, Synchronous Oscope plots, and other playable plots resulted in incorrect block number display or navigation. Block numbers now correctly update and navigate to the specified block when manually entered.

**Sensor Health Sheet Clear Function:**

> - Fixed issue where using the 'Clear sheet' function did not close the open sensor health sheet window. The sensor health sheet now properly closes when cleared, and a new sheet correctly replaces the old one when assigning and viewing a sheet again.

**Per-Block Metrics Versus Parameters Plotting:**

> - Fixed issue where dragging a signal and parameter onto a plot area to create a history plot resulted in two traces plotted versus time instead of plotting the signal versus the parameter. History plots now correctly display the signal metric plotted against the parameter as expected. This also fixes plot setup files (.dxs) that previously contained signal versus parameter plots.

**Sensor Health Sheet Peaks Collection Filtering:**

> - Fixed issue where gages marked as "0" in the sensor health sheet were not omitted or flagged as noise in peaks collections (BCX/CSV exports). Gages marked as inactive in the sensor health sheet now properly affect collection outputs, ensuring they are either omitted or flagged as noise in the exported data.

**Style Theme Preference Change:**

> - Fixed crash that occurred when changing the style theme preference to Fusion while a plot setup file was loaded. Style theme changes now complete successfully without causing application crashes.

**ZMod Plot Deletion:**

> - Fixed crash that could occur when deleting a ZMod plot. All ZMod plots can now be deleted safely.

## 2024.39

**Scopelimit Ratios and Frequencies:**

> - Fixed an issue where the full table of scopelimit ratios, frequencies, and limits for a given block of data could not be read from a bcx file in version 2022.33.6671. Fixed ARD Mode Frequency field for CSV output to fix formatting bug. Support Ticket #102752

**PWMIP.dll Version Confirmation:**

> - We now append a -${VERSION} to the PWMIP.dll name to confirm the version. The version should match the version of DS/DX for which it was built. Support Ticket #102800

**Absolute Time Setting for Tracking Plots:**

> - Fixed an issue where applying the "Absolute Time" setting to a time-based tracking plot also incorrectly applied it to a speed-based tracking plot when plot settings were shared. Support Ticket #102847

**DATX File Absolute Time:**

> - Fixed an issue where DX did not read absolute time correctly from DATX files, displaying the time axis as midnight January 1, 1970, and showing incorrect recorded start and final times in the validation report. Support Ticket #102926

**Signal Math in Viewer:**

> - Fixed an issue where signals created and validated using signal math did not appear in the viewer and could not be plotted. Support Ticket #102933

**Additional Fields for .mat Files:**

> - Added datapoint fields to .mat files to align with what CSVs have available. Updated DX documentation on the Help page to indicate how to populate these fields. Support Ticket #102934

**Build from Limits Unresponsive:**

> - Fixed an issue where the "Build from Limits" function was unresponsive, preventing the creation of signal elements from an existing scopelimit file. Support Tickets #102935 & #102942

**Multi Sample Rate DATX+1 Data Set:**

> - Fixed an issue where processing a multi sample rate DATX+1 data set resulted in incorrect record lengths, showing doubled or quadrupled lengths in validation reports, strip chart plots, and calculated frequency ranges. Support Ticket #102938

## 2024.31

- Corrected DX issue with reading parameter flagged data from Datx files

## 2024.4

- "Info Format" on Zmod scope limit options now updates properly (#102893)
- DX now properly tracks duplicated speed channels after export (#102884)

## 2023.39

- Playable Plots (Time, Magnitude, Magnitude+Envelope, Waterfall, and Orbit) now fully load when selected or created, instead of being read directly from the file based on current block number. This change fixes several issues related to block numbering consistency, especially in cases where channels have been filtered or have overlap applied to the FFT. In addition, once loaded, playable plots will generally be more responsive. Plots are playable while loading and load from beginning to end. Once a plot type has been loaded for a specific channel, it will not need to be reloaded until the file is reprocessed or DX is closed. Note: In some cases, it is possible to seek faster than the plot loads, which will cause playback to stop at the last loaded block, waiting a moment for the plot to load will continue playback.
- Fixed issue where time and magnitude block number would not show the same values when linked #102737
- Playable plots no longer decrement when their slider is clicked - #102791
- Time and magnitude plots now properly match when processing with spike filter - #102812
- [Beta Issue] Second time plot now correctly shows data - #102860
- Filtering no longer causes block number shift in Time Plots - #102862
- Block Numbers and Times are now correctly zero-aligned when first data block is non-zero - #102863
- Fixed Issue where DX would hold CSV files open until after close -  #102383
- Dewesoft file driver improvements and stability fixes
- Fixed crash when processing multiple files and plotting RPM #102734
- Fixed file crashing on process - #102810
- Fixed dewesoft dxd compatibility issue - #102866
- Fixed issue where Batch Export did not work with a parameter created with Parameter Math -#102740
- Fixed issue with some files crashing when using Grid Response Detection - #102741
- Fixed error on damping fit tabulation nomenclature. “Center RPM” now correctly reads “Center” - #102753
- Fixed plot creation issue when selecting multiple of the same parameter from different files to overlay on a single plot. All selected channels are now properly added. - #102754
- Auto Scaling absolute time now works for overlaid channels containing different time ranges - #102755
- Updated wording for appending or overwriting noise definition files for clarity - #102771
- Fixed bug where the Campbell Slice feature would be activated when left or middle clicking on a Campbell Plot immediately after reprocessing - #102787
- Fixed issue where text cursor would jump to the end of the field when editing some text boxes - #102792
- Multi-Samplerate DATX Improvements - #102796
- Fixed Shift-Clicking to remove marker when in multi-mode. Note: Shift-click to remove marker only works if Auto Link Markers has been turned _off_ - #102797
- “isParameter” keyword to load Signal as Parameter in indexed DATX files. - #102804
- DATX Validation Reader Improvements - #102859
- Fixed issue where the UI was not properly showing a loaded limits file when loading limits with a design - #102809
- Generic Parameters can now be plotted as absolute time.
- Corrected issue where default units were sometimes incorrect when loading through the signals element - #102819
- Fixed bug where waterfall plot was not keeping settings changed in the spectral tab of the plot options - #102825
- Fixed backwards compatibility issues with specific rwx files - #102827
- Signals set as parameters now appear as parameters in exports - #102830
- Fixed linux incompatibility with PWD and TDMS files - #102831, #102833
- ARD and ARD Export can no longer include signals not found in the design - #102836
- fftoverall bug fixed - #102838

## 2022.50

- Fixed an issue where inputting signal name with Chinese name caused a crash
- Fixed an issue present in version 2021.50.6009 where DX was not collecting all of the peaks that were collected in 2020.47.3055 or 2020.47.4980.
- Fixed an issue where dragging a signal onto the canvas in viewer and selecting Magnitude plot, the Time and Block Number did not display in the top left corner.
- Fixed an issue where the x-axis selection for envelope plots was greyed out and could only be set to linear in the plot options
- Fixed an issue where history plots of a time parameter could not be tabulated without causing a crash
- Fixed an issue where a speed pulse train signal defined as a parameter in a .rwx or .datx file could not be converted to a signal and plotted.
- Fixed an issue where batch export of plots did not include Z scale and threshold on the Campbell.
- Fixed an issue where DX crashed with an error message when opening .uff files.
- Fixed an issue where a speed pulse train signal defined as a parameter in an .rwx or .datx file could not be converted to a signal and plotted. This capability existed in previous versions and is useful for visualizing alignment of other signals with 1/rev or multi-tooth tach pulses.
- Fixed an issue where history plots of a time parameter couldn't be tabulated from the right-click menu.
- Fixed an issue where processing a design with multiple ADRs and creating a tracking plot with both ADRs caused DX to crash. This occurred when dragging speed and signal from one ADR, and then dragging the same signal from another ADR on top.
- Fixed an issue where processing a design with multiple ADRs and creating a speed Campbell with both ADRs could impact the result. Dragging speed and signal from one ADR onto the canvas, selecting Campbell, and then dragging the same signal from a different ADR on top caused the plot to generate incorrectly.
- Fixed an issue where the noise definition file was not correctly applied to Dewesoft files. Manually selecting noise on a Campbell plot, saving the noise selection to a noise definition file, and reprocessing the file with a filter element containing the noise definition file did not remove the defined noise. This issue was specific to Dewesoft files, as the noise definition file worked correctly with .datx files.
- Fixed an issue where DX crashed when plotting an RPM-based Campbell with channels from multiple Dewesoft files that had extra calculated channels.
- Fixed an issue where time did not increment correctly when linking the slider between a time plot and a magnitude plot. The time block number and time were offset between the two plots.
- Fixed an issue where processing the same signal with multiple block sizes on the same tracking plot resulted in different plots depending on which block size was plotted first.

## 2022.23

- Fixed issue where low frequencies were not handled correctly for integration and differentiation in 2022.14.6409
- Fixed block / time offset in Time, Magnitude, and StripChart plots when using certain filters
- Expanded Signal Element tolerance for custom unit integrations not found in unit table / simplified formatting for custom integrations
- Re-introduced ability to overlay filtered and unfiltered signals in time, magnitude and strip chart plots
- Fixed crash with spike filters on certain files
- Disabled settings changes on synchronous oscope plots during playback as this could occasionally cause a block offset
- Updated dewesoft driver to read asynchronous channels as parameters
- Fixed bug with SimpleCSV format that would cause crash if CSV had a prime number of rows

## 2021.50

- Signal Math added
- Phase calculations improved. Phase calculation is performed at block center and used in calculations/reference in this manner. For reporting and collections, phase is reported for front of block.
- Additional tach channel setup options: rising/falling edge and minimum signal amplitude for decoding
- Processing Speeds improved for all file types, greatly improved for simple CSVs
- Parameter history plots can now be created vs other parameters (#102559, #102313)
- Speed reference for Tracking / Bode plots now appears on plot as text in top left corner (#102607)
- Peak Noise plugins, noise1stoa, noisebias, noisecfl, noisethpk, noiseovr, noiserem, and noisesum now correctly create signal statistics in viewer (#102319)
- Zeros are written for empty data in Pramater CSV Exports (#102508)
- Ordertrack Plugin in DS data now supported in DX (#102545)
- Time zones are now read correctly in rwx files (#102544)
- MATLAB RAW files now export correctly (#102552
- “Show Export Directory” now functions as expected (#102553)
- "All Statistics" Order Peaks Export – removed extra 5 peaks columns that should not be present (#102509)
- Single FFT for multiple Adv. DSP elements now yields correct results when processed without Viewer (#102589, #102420)
- Peak noise plugins that require a speed parameter now function with speeds created by parameter math (#102484)
- Order Zmods now export correctly in batch (#102325)
- Fixed query filters for response detection tables (#102375)
- Filename string option will now appear after choosing export directory for tabulated files (#102365)
- Batch export memory leak fixed (#102382)
- Auto Setting added to Z axis for Campbell, Zmod and Order Zmod plots. (#102419)
- Fixed parameters for export - parameters that are not in the file will no longer be added to the export (#102413)
- Fixed plot title edit crash (#102615)
- Linked markers are no longer drawn outside of plot bounds
- Linked markers are turned off by default

## 2021.29

> [!NOTE]
> This package has been removed, all features included in 2021.50

- Linked Cursors
- Format Painter-Right Click>Copy/Paste Formatting On Plots
- Added Text and Image Plots
- Tracking Plot Signal Subtraction
- Auto/Response Detection Tables Can Now Have Text and Labels Resized, Resolved Scaling Issue on 4K Displays
- Updated Ribbon for Better Performance and 4K Support
- Enhancement to Grid Resizer for 4K Displays
- Tabulation Information for Campbell Diagrams Now Includes Extra Information Based on Markers Selected in Options Menu
- Campbell Diagrams Can Now Be Created with Other Parameters Other Than Speed
- FFT Zoom Added To FFT Element
- Improved Matlab Reader
- Fix for Split Element Bug
- Dewesoft, HDF5, and Other File Format Driver Improvements

## 2020.47.3055

- Ribbon update - High DPI scaling now better supported / “Fusion” theme now preferred DX style
- Zmod Triple auto-page button added
- 101665 + 102432 – O’scope Plot added
- 102151 – Parameter display added
- 102113 + 102429 + 102398 – Quality of life changes to plotting and apply all
- 102431 – Updated gird response detection to take speed parameter
- 101693 + 102235 – 'C01_reference_delay' considered when processing DATX files.
- 102358 + 101696 + 102374 – Block Offset with filter data fixed
- 102404 – All plots on a current page can now be copied / pasted into another document as an image with the “copy page” button in the ribbon.
- 102366 + 101459 – Additional file naming strings added to exporters
- 102408 – Custom unit conversion now have a higher acceptability
- 102449 – Plot moving area is now more obvious and easier to grab
- 102185 – Signals from different processing chains can now be overlaid on the same playable plot
- 101583 – Plot marker font size can now be changed
- 101347 – Ability to set any axis setting as default for all plots
- 102359 – DX samplerate issue fixed
- 101651 – Damping fit now only takes current plot boundaries into consideration on creation
- Damping fit annotation can now be copied to clipboard
- 102396 – Tracking plots from different files now overlay correctly

> - MOD: 102468
> - MOD: Independent Selection vs. Group selection and drag to plot

- 102446 – Extended Envelope output now allows users to specify what speed parameters to export
- 102448 + 102301 – Exporters now include DS legacy 2.8.X options
- 102447 – DX now reads in CSV files with more flexibility
- 102310 – Adv. DSP - Threshold Now Applied correctly
- 102414 – Export response detection now only includes peaks specified in Adv. DSP
- 102309 – Collections now collecting peaks correctly as specified in min + max ranges throughout the design path
- - **102460 – Mode ID with Speed Dependent ScopeLimits File now functioning correctly**: - MOD: Speed Dependent Mode Lines on Campbell Auto Selected Param from Limits
- 102441 – Strip Charts now scale correctly
- 102415 – Sony files now process and are read correctly
- 102435 + 102354 – DX now correctly reads CDF files
- 102445 – Modifying a legend label in Plot Options now changes the correct legend entry for the selected trace
- 102403 – EO Displayed on Speed Campbell no longer Rounds to Nearest Integer
- 102378 – Multiple time plots may now be dragged and overlayed at once
- 101779 – More significant digits added to EO cursor display on Campbell plots
- 101820 – Orbit plots can no longer be created with parameters
- 101604 – Mode lines now match signal colors on overlay plots
- 102188 – History plot manual scaling issue resolved
- 101827 – IRIG now displays correct year when read into DX
- 102092 – “Smooth Factor” is now considered an advanced option
- 102008 - Increased Max BCX Extracted Peaks
- 102007 – Max peaks increased in Adv. DSP to 16384
- 101977 – Min/Max frequency added to tracking plots
- 102469 – Extended envelope now matches tabulated results
- 102391 – DB Display now allows more digits
- RWX files with Chinese characters in channel names now replay correctly
- Reloading tracking plots no longer loses axis settings
- UFF58 and UFF58b now separate export options
- Parameters can now be merged to different directories
- Time Waterfall Point selection fixed

## 2020.26

- Fixed issue with block offset when using digital filters (101696, 102358, 102374, 102421)
- Fixed CDF import failure (102354)
- Fixed waterfall point selection issue
- Removed Log scaling on Waterfall plots due to performance issues
- General plot settings bug fixes
- Improved manual / auto scaling feature when new traces are added to an existing plot

## 2020.17

- "Apply All" and "Apply Page" plot overhaul implemented to make plot edits more in line with APEX DS (#101719, #101851, #101861, #101871, #101884)
- Improvements to the "Print" function including improvements to Zmod printing and page sizing (#102392, #102392, #102394, #102395)
- "Duplicate Page" feature now works with parameter data (#102377)
- Parameter Merge bug fixes relating to time zones (#102287)
- File format reading improvements (#102269, #102415)
- Various minor bug fixes

## DX 2020.8.1884

- Added training license file to package with training data files to package directory "training" (DX#770)
- Fixed issue where Time Campbell in ABS time mode would not show marker (102346)
- Fixed issue where Time plot could show incorrect trace information with multiple viewers (DX#773)
- Several internal OT fixes (DX#771)
- Fixed OT lead lag phase issue (DX#771)
- Fixed issue where designer mode buttons were both active (102348)
- Fixed playable plots to seek to block indicated (102297)
- Fix to print value for zero bin parameter values for exteneded envelope csv (102266)

## DX 2019.52.1687

- Added Tach processing element, provides converting signal to speed parameter (102018)
- Removed quick plots and replaced with quick pages (102304)
- Improved Order Track phase accuracy (102265)

## DX 2019.47.1589

- Improved digital filters. Frequency cutoffs and filter types directly specified, no need for predefined filter files. (101976)
- Added HDF5 file driver (102329)
- Updated and improved RM package, COT DOT now in single element OT - order track (102265, 101921, 101915, 101970, 101972, 101971, 102023)
- Fixed crash when using circle symbol type on linked campbell plots to response table (102057)
- Added additional statistic for long term averaging for use from DS recorded data files (102315)

## DX 2019.46.1560

- Fixed RM tokens being acquired when using AM plots (102328)
- Fixed speed decoder to properly handle non-(integer/adc count) data types (102332)

## DX 2019.43.1459

- Added parameter math using formulas (102284)
- Added ability to borrow tokens (requires license with borrow enabled) (DX#741)
- Added dB scaling to Mag Env plots (102213)
- Fixed Datx multirate file sample rate (102206)
- Fixed Time Parameter CSV export to use data proper file time stamp (102224)
- Fixed CSV export errors related to file type (101631)
- Added optional ability to password protect licensing panel (102284)
- Added Thermocouple conversion plugin, requires DS recorded data. (102284)
- Extended signal integration to allow custom scaling with integrated and DC signals (102256)
- Changed CSV export to be compatible with CSV import (102285)
- Fixed Y2 axis controls disabling after using Campbell Y2 (102243)
- Fixed crash when tabulating a History plot (102271)
- Fixed crash on Time Campbell Y2 click-drag (102281)
- Added ability to specify ARD (collections) parameters for export (102252,102036)
- Added ability to specify multiple speeds for Order Peaks CSV output (102266)
- Added exporting of all parameters to Extended Envelope CSV output (102266)
- Fixed Order Peaks CSV output to always select highest peak in EO band (102266)

## DX 2019.28.1060

- Added ability to include Training files with license (102189)
- Fixed RWX process crash with malformed setup (102179)
- Fixed #C naming on export (102168)
- Fixed DP Flag name on export (102183)
- Fixed Licensing crash on Linux w/multiple users (102159)
- Fixed USE_SERVER option in Licensing (102150)
- Fixed issue with exporting CSV from RWX (102186, 102165)
- Added Token counter to main window, set default token to base (102125)
- Fixed Permanent license indicator (102125)
- Fixed Token Manager to show token counts properly over 999 (102125)
- Fixed missing DX icon on windows (102173)
- Added ability to export additional peaks as CSV (101528)

## DX 2019.18.758

Large feature and quality of life update.

### Fixes / Features

- Parameter CSV file – fixed units exported and imported (DX#637)
- Design from file group by units (102056)
- Enabled Time Campbell frequency slice (101929)
- Fixed Time/Param Campbell frequency slicing (101929)
- Fixed memory leak and files being left open (DX#562)
- Fixed dialogs off screen (102074)
- Fixed massive matlab file reader memory leak (102069)
- Fixed .unv crash when using multiple rates (102068)
- Fixed inoperable Cancel buttons (102067)
- Fixed stale cursor on Campbell when slicing (DX#639)
- Fixed Y1/Y2 Axis labeling when using mixed units (101884)
- Fixed Axis labeling to match designer unit changes (DX#655)
- Removed ability for changing plot Axis Labels (DX#656)
- Added ability to use alternate Param CSV time (102063)
- Added built-in integration conversions, e.g. g->ips (102056)
- Added ability to change units w/o integration, e.g. meters->inches (102056)
- Added ability to use “Load” button for signal to select units for integration (102056)
- Added plot legend for Unit name
- Removed plot based (freq domain) integration (DX#663)
- Fixed waterfall trace selection (DX#630)
- Set FFT Scaling to legend default (DX#662)
- Made FFT Scaling names consistent (DX#662)
- Removed custom scaling option for integration (DX#665)
- Fixed (windows) cursor behavior (DX#667)
- Added color coding of axis labels based on units (DX#677)
- Fixed mag and env plots to label PSD properly (DX#669)
- Updated “Hotkeys” in Designer and Viewer (See Tooltips) (DX#660)
- Updated designer to prevent non-sense connections between elements (102071)
- Added units as trace legend option (DX#678)
- Fixed incorrect overlapping mode assignment (101804)
- Added ability to load units for integration from signals load button (DX#699)
- Fixed default plugins to run after filters (101659)
- Fixed Mag and Mag/Env playback with overlap (101963)
- Marker now works with XY axis swap (102112)
- Added indication that 5 tokens are required to run DX (102093)
- Fixed error message when exporting peaks to .csv (101631)
- Fixed campbell plot scaling when selecting absolute time (101829)
- Fixed issue when creating multiple tracking/bode plots (101859)
- Fixed issue where plot scaling would reset when add a signal to existing plot (DX#679)
- Fixed issue where campbell z axis slider would disappear (DX#631)
- Fixed issue where waterfall vs param would not load properly (DX#668)(102109)
- Removed dark theme due to external library problems. (102026)
- Fixed incorrect number of columns for external legend. (101869)

## DX 2019.10.651

### New Features

- Added ability to specify Flexera license server port using GUI (102025)
- Added ability to specify Flexera license server port using ENV variable (102025)

### Fixes

- Parameter math crash fix (101991)

## DX 2019.8.647

### New Features

- Token licensing (101708)
- Parameter merge (101689)

### Fixes

- Parameter math crash fix (101991)
- Campbell triple tracking scaling fixes (102000,101999, 101872)
- Collections renamed to "Auto Response Detection" (101998)
- BCX export crash fix (101997)
- BCX sort fix (102009)
- Waterfall parameter cursor fix (101959)

## DX 2019.5.601

### Fixes

- Playable plot block seek was not seeking to correct block number, some issues still present when seeking .raw files (101963)
- Dewesoft file reader shared library was missing from install packages (589)
- Noise element when using multiple noise files was using last noise file (101933)

## DX 2018.49.553

### New Features

- Batch Reporting
- Plot setup version checking
- Changed some element icons and names to be more user-friendly
- 'Collect only on flagged noise' option for Collections

### Fixes

- Deleting a very large number of plots sometimes caused a crash on Windows
- Some hyperlinks in the software were incorrect
- Sometimes the Crash Handler didn't appear on Linux
- Many plot setup items weren't being saved and/or loaded
- Sometimes plot setups used signals from the wrong scope or file
- Sometimes selecting a parameter Campbell after loading a plot setup caused a crash
- Waterfall plots were slow to be created and sometimes didn't display correctly
- Sometimes processing TDMS files caused a crash
- Sometimes removing Linear Gradient colors caused a crash
- Disabled some options for ZMod/Order ZMod that don't apply to those plots
- Speed Campbell zoom caused shift with regard to the Y2 axis
- Speed Campbell plot picking did not qork correctly
- Mag trace on mag+env plots changed when the plot legend was edited
- Some elements could connect to other elements when it they shouldn't have been able to
- Swapping XY axes didn't work or produced incorrect results on some plots
- Many of the Bode Plot options were not working correctly
- Printing some plots to PDF covered the header information
- Campbell Triple Envelope Plot had the wrong title
- Bode Plot internal Legend didn't work
- Adding a parameter to a time plot caused a crash
- RAW part files didn't play DX
- Changing coupling from DC to AC and reprocessing with an Orbit Plot casued a crash
- Creating a waterfall from a file that had overlaps caused a crash

## DX 2018.44.364

### New Features

- Orbit Plot
- Y2 Axis - Time & Magnitude
- Y2 Axis - History
- Y2 Axis - Time Campbell
- Y1 Y2 Legend Indicators
- Zmod Legend
- Campbell Block Variables in Markers
- Custom "Print" File Names & Patterns
- Campbell Triple Speed Choice
- Improved Collection Noise Checkbox
- Change Legend Font Size
- Help Documentation Online
- Decimal Precision in Manual Split Ranges
- History Plot Default Axis Scaling
- Plot Tabulation Decimal Precision
- Link Noise File to Data File
- Append to Noise Definition
- Campbell Threshold Slider
- Campbell Auto EO Lines

### Fixes

- Damping Fit curve was sometimes shifted and incorrect
- Some pks files caused a crash on Windows when processing
- Some plots used signals from the wrong file if the signal names were the same
- Noise definition regions were not always displayed correctly
- Marker size and line color were reset on reprocess
- Annotations were not always correctly loaded from plot setup
- Disabling an External Legend and reprocessing caused a crash
- External Legend was missing contents after reprocess
- Y2 axis was not always loaded correctly from plot setup
- Creating a waterfall from a datx_index signal and reprocessing caused crash
- Custom range scales on Mag+Env plots were reset on reprocess
- Accel & decel parameters from the same file confused plot setup
- Filtered & unfiltered signals from the same file confused plot setup
- Couldn't scale the y-axis for the Magnitude or Phase independently
- Changing the order of mode lines wasn't reflected in saved limits file
- Peak noise element ribbon didn't update properly
- CSV Export tooltip showed incorrect information
- Custom page labels did not persist after reprocess
- Damping Fit Legend persisted after damping fit was cleared and reprocessed
- Some plot types were available when they shouldn't have been
- Viewer tree was empty if processed file could no longer be found
- Zooming on a plot affected picking ability
- Custom Campbell marker would not apply to all pages
- Tabulating a Tracking Plot that included a Damping Fit caused a crash
- Plot setup failed for split files of similar data
- Grid & EO Collections couldn't be easily placed on the same plot
- Accel & Decel noise were not both saved in the noise definition
- Collections noise wasn't drawn on Campbell
- Default Design preference didn't load design or limits name into status bar
- Exported scope limits strainratio values were all zeros for the last gage
- Mulitple noise elements in series didn't function properly
- Custom text on marker was lost when cursor was moved
- Scope element name didn't show up in legend
- Speed dependent mode lines on a Campbell moved as speed range was changed
- Link button didn't untoggle when hitting Esc key
- Text was clipped in EO & Grid Collection dialogs

## DX 2018.2.1

### Fixes

- Improved plot persistence and loading/saving plot setups files
  - Fixes for identifying filtered signals and split parameters
  - Added additional parameters including: Min/Max Peak frequency range, peak threshold, number of peaks
  - Additional checks for recreating History plots when reloading
  - *NOTE:* Older plot setup files will not take advantage of the loading improvements
- Fixed crash that appeared sometimes when configuring real time plots on reload
- Fixed issue where limits were marked “*” as editing when they were not
- Fixed issue where loading a setup or quickplot would use a parameter not in the design
- Fixed design from file issues with DATX/raw files and unused channels
- Fixed issues with IRIG decoding in non-APEX file formats
- Fixed issue with plot titles, all plots titles are now static, adding data to a plot no longer overrides the title
- Fixed issue when switching between “Time” & “Block” using the shift key on real time plots
- Changed EO collection settings to allow more than ‘All’ or ‘Maximum Peak’, a number can now be entered
- Checks added to ensure order resolution is in the range: 0 < resolution <= 1.000, with 3 decimal places
- Fixed inconsistent reference time (1970/epoch) from DATX files
- Fixed issue where invalid limits files still loaded
- Fixed issue with DX creating corrupt limits file
- Fixed issue with DSPCon Dataflex file loading incorrect sample rate
- Fixed FlexNet license issue where licenses would check in and out randomly
- Fixed limited zoom issue on strip chart
- Fixed issue with non-integer custom EO’s on Campbell plots
- Campbell plot now shows legend on creation
- Fixed issue where connecting components would not mark (*) the design as edited
- Fixed issue where ftol entries in excess of number of modes caused DX to crash
- Fixed issue where user plot symbol changes were not retained when switching pages/plots
- Fixed issues with exporting foreign files to RWX/PKX with “parameter from signal”
- Fixed possible crash when attempting to convert a signal to a parameter using invalid parameter type
- Fixed issue with manual noise flagging not using ‘Flag All as Noise’ option
- Added additional open SSL library to Linux packages, to fix some xdg-open issues
- Parameters added to quick plot signal selection, allows History quickplots to use parameters
- Quick plots with multiple history plots that are “one channel per page” will now be prompted to select ‘n’ number of statistics
- Overwriting quick plots now works correctly
- Improvements made to playing real time plots with overlapped data, or data using filters requiring an overlap
- Made additional improvements to real time plots when seeking through a file, slider jump back issue fixed
- Fixed an RM issue where users received error messages when using parameters created from signals as the speed parameter.
- Fixed an RM issue where it would sometimes fail when the tach ratio was an exact multiple of revs per trigger.
- Fixed an issue where files exported to the RWX format and containing parameters created from signals would fail to play history plots in DV for those parameters.
- Additional stability improvements

## DX 2018.2

### New Features

- Waterfall Plot
- Strip Chart
- Improved EO collection algorithm
- Improved collection processing speed
- Manual noise flagging added
- Absolute time added to more plots
- Playback speed is now adjustable
- Viewer tabulate/export collections added
- Custom plot trace labels added
- Ability to add statistics to Campbell markers
- Improved plot persistence (collections, tables, etc.)
- Copy/paste tabulation
- Remove trace added to trace options dialog
- DEWEsoft format added
- Added speed dependent limits on Mag+Env plots
- Default trace colors now customizable
- Plot trace options cleaned up and improved
- Recent files menu added to 'Process' button
- Recent files menu added to 'Assign Limits' button
- 'New Design' button added
- Added ability to copy paste from tabulated table
- Non integer custom EOs now supported in Campbell plots

Note: Internal version number changed, DX may require a new license file

### Fixes

- Fixed RM processing for some file types
- UFF export improved, ouputs 1 file now
- MAT export improved, ouputs 1 file now
- File parameter decoding fixed for floating point files
- Fixed issues with exporting plot images
- Improved swapping XY axis on plots
- Axis min/max spinboxes decimal places fixed
- Fixed mode line drawing on Campbell plots
- Fixed plot options ribbon updating
- Numerous performance and stability improvements
- Fixed DPFlag export name in designs with a splitter
- Improved quickplot axis scaling and linking
- Fixed split report in the validation report
- Fixed crash when dragging invalid large files onto the canvas
- Fixed Windows issue with element badges not updating after change
- Fixed issues with disabling or not having scopes while exporting files
- Fixed plot axis ribbon changing issues
- Fixed collection table column persistance
- Fixed issue with exporting parameter subsets to rwx pkx files
- Fixed quick plot reference parameter issues
- Fixed issue with saving and loading designs with custom axes/title font sizes
- Fixed UI issue with quickplots gallery on some resolution screens
- Design badge and label update issues on windows resolved
- Fixed zoom reset inconsistencies in Campbell plots

## DX 2017.3.2

- Fixed issue splitting files that have been reblocked
- Fixed Campbell/zmod peak block number offset

## DX 2017.3.1

- Fixed issue replaying (magnitude, time) for some reblocked datafiles.
- Fixed issue where you could not save modified limits on plots created from a quick plot
- Fixed permissions issues when assigning limits under some conditions in Windows
- Fixed issue where a signal when converted to a parameter was then not available as a signal in the viewer
- Fixed issue with 'Apply to all plots' after using a quickplot the first time
- Fix for additional legend text on History plots (scope component name etc.)
- Fixed non-integral EO collection algorithm, also allow user to set 0 integral peaks to collect
- Added missing options for Ordered Peaks CSV export
- Fixed 1xInt, 2xInt & Diff coefficient processing for signals
- Some signal history statistics have been renamed, “Peak” = “0-Pk”, “Pk2Pk" = “P2P”, and “HalfP2P” = “sa-Pk”

## DX 2017.3

### New Features

- Added Order Processing (DX-RM)
  - Components
    * REV breaks file into 1/rev packets
    * COT (Computed Order Track)
    * DOT (Discrete Order Track)
  - Plots
    * Order ZMod - ZMod plot with order on the y-axis
- Improved the Engine Order collection
- Renamed the column variables when writing a binary collection .bcx file
- We always write the column names when saving a collection (even in the merged file)
- Added a sensor health sheet feature
- Dynamically adjust mode lines on Campbell plots and save/as the altered limits file
- NIV/IV filters - flag non-integral or integral peaks, respectively, as noise
- Added capability to export plot images in the viewer
- Plot setups can now be saved and reloaded in the viewer
- Peak element frequency range added
- History plots time axis can be changed to absolute time in the plot options

## DX 2017.2

### New Features

- Manual and event based file splitting added to split element
- New spectrum statistic - FFT Overall
- New Plot: Bode Plot
- Damping estimates for single traces on Envelope, History, and Tracking plots
- Exported collections can be concatenated to the same collection file
- All exported files are saved in the specified export directory (without sub-directories)
- Validation report is automatically exported whenever anything else is exported
- Ability to order track vs any parameter added to Tracking Plots
- Improved support for Hi-Res monitors
- Simple text plot annotations added to all plot types

## DX 2017-Q1

### New Features

- Improved validation process and resulting validation report.
- Added Parameter Math element, which allows for applying basic math functions to parameter data.
- Added the Half Power Filter and Saturation Filter to the digital filtering element.
- Support added for third-party data formats via plugins.
- Binary export feature added to collection exporter.
- First run quick design and default design preferences added.
- One click tabulate all pages feature added to the viewer.
- Ability to disable elements on the design added.

## DX 2016-Q4

### New requirements

> - all designs must now include a "Parameters" or "Parameters*" element. Designs created in previous versions are automatically updated to include all parameters.
> - Only one FFT element can be connected to a Scope.

### Overall Updates

> - Layout
>
>   > - updated ribbon design
>   > - redesigned window layout
>   > - removed modes (Designer, Viewer, Export) along the left side of the window. Switching between Designer and Viewer is now handled by two buttons in the upper right corner of the screen and exporting was move to a new set of elements.
>   > - Designer and Viewer can now be undocked and Help is in its own window
> - Features
>
>   > - the user can now modify the FFT size when processing with multi-sample-rate files
>   > - added a preferences dialog to view/change program-wide options
>   > - two versions
>   >
>   >   > - PRO which includes the following features
>   >   >
>   >   >   > - the user can select multiple files to process with the same design - all processed output is available in the viewer
>   >   >   > - various collection options
>   >   >   > - multiple export options
>   >   >   > - ability to automatically split input files into accel/decel sections
>   >   > - Basic
>   >   >
>   >   >   > - the user can add a single export element to a design

### Designer updates

> - New features
>
>   > - the user can now create Quick Designs
>   > - the user can zoom and pan designs - there is also a new navigation map in the upper right of the Designer window to show you where you are in a design
> - New elements
>
>   > - parameter - parameters, parameters*
>   > - export - raw, pkx, csv, and collections
>   > - collection - grid, EO, and largest peak
>   > - filter - digital and peak
>   > - auto split

### Viewer updates

> - New features
>
>   > - plot linking
>   > - the user can now create Quick Plots
>   > - peaks identified in collections can be highlighted in Campbell and Envelope plots
>   > - the tree on the left side where you select which channels to plot can be filtered to only show certain items
>   > - General, Axis, Trace options can be changed from the ribbon.
> - Feature updates
>
>   > - the tracking plot interface has been re-designed
>   > - the tree on the left side where you select which channels to plot has been re-organize by file (multiple input files) and collection output has been added. Additionally items are sorted by Scope name, channel indices, and statistic ids.
>   > - the user can now define a page layout using a standard grid button
>   > - typically accessed plot settings can now be changed in the ribbon
>   > - the user can choose to apply plot option changes to the selected plot, all similar plots on the same page, or all pages
> - New plots
>
>   > - collection table

## DX 1.0 DX 2016-Q2

- Initial Release
