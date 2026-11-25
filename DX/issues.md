# Issues & Limitations

## General

- Changing the default block to a value less than the default results in playable plots not showing all the data blocks (102120).
- Magnitude Envelope plot - block numbers must match other plots if plots are linked together. (101802).
- Batch - Crash can occur when cancelling Batch during processing
- Plotting - When Bode plot setup is loaded back in, the Y axis on the Magnitude plot resets to default values [0 - 100]
- Plot style preferences may not be saved or recalled correctly across application restarts starting with the second restart.
- The First-run Quickplot preference may not be applied on startup even when enabled in Preferences.

## Operating system

- DX 2019.43 and later may crash on exit with Windows 7 SP1. Work around is to run DX in compatibility mode as Windows 7.

## Splitting

- Splitting files using a design that contains more than one output (more than 1 viewer or export element) will double (for every output) the number of splits listed in the validation report. All data within the report, and all splits within the viewer are still correct.
- Validation Report can clip rendered design images at the bottom of the report if long design names or element settings are present.

## Data Formats

For limitations in data formats see the [Data Formats](formats.md) page in this documentation

- DX may only load the Tach channel from large SQLite .db files created by DX+; the full channel set will load correctly in DX+ and DX+ File Viewer.
- Parameters in CSV exports may appear in a different order between Linux and Windows builds. A previous fix that sorted parameters early caused indexing issues and was reverted for this version.
- Time Tabulation CSV can contain inconsistent unit casing (for example ksi vs Ksi).

## Collections

- Collections are limited to a maximum of 2,097,152 collected peaks.

## Spike Filter

Under certain conditions, implementing the “spike” filter may cause a one block offset in the “Time” plot display for signal scopes connected to the spike filter processing path relative to the same signal not connected to the spike filer processing path. This is confirmed to be a display issue only and that the results (repair or identify as noise) of the spike filter are being applied to the correct block. This may be confirmed using a “time Campbell” plot or a History plot of the “Spikes” statistic.

## Designer

- APEX PKX files Cannot change any processing steps other than adding a Peak Filter. An FFT and Peaks element are still required to attach export peaks, peak filter, or export peaks elements. PKX files will not be affected by changes in these elements or by digital filters.
- Arrow colors do not always function as expected.

## Campbell/Z-Mod plots

- DX will only plot 2 Million peaks per channel per Campbell or Z-Mod plot. If there are more than this DX will pick the peaks with the highest magnitude greater than 0.001.
- Mode ID as indicated on Campbell either by peak highlighting or labels may differ from the ModeID specified by run collections (ARD). This viewing capability is mainly meant for a general and visual basis based on the contents of the limits file. However, If precise mode ID is needed, please use collections (ARD) elements for identification.
- PWMIP-related crashes have been observed when loading certain plot setups or history plots that reference PWMIP-created statistics. Please ensure your PWMIP plugin is up to date to avoid compatibility issues.
- Campbell plot setups may load with the wrong channel type (e.g., frequency-based channel saved but time-based channel loaded).
- Campbell Triple peak table may show extra entries and differing values when compared to previous versions.
- Plot axes and zoom levels may sometimes be reset to default values after reprocessing a design.
- History plots can display a gap after the X Axis when placed below a Campbell plot; removing the Campbell and then changing the History X Axis may resolve rendering problems.
- Campbell Floor/Ceiling labels can be clipped when resizing plots based on Windows display settings, and the Ceiling slider will not be visible if the slider is moved higher than the current Ceiling value.

Ribbon Tabulate

- The Ribbon "Tabulate" button may fail to tabulate plots in some cases.

## Plot Settings

- Plot settings copy/paste may not transfer all settings between plots; observed missing items include Plot Title, X & Y axis ranges, Legend keys and colors, Enable Limits/Mode Overlay, Campbell Symbol Angle, Synchronous Oscilloscope Speed Parameter, Synchronous Oscilloscope EO Number, Response Table settings (font sizes, number of rows, sort), and some Tracking Plot options.
- Axis values and appearances may differ from previous versions for STRIP, TIME, TRACKING, and MAG+ENV plots.

## Envelope Plots

- Envelope plots may display different results between older and newer versions.

## Parameter Display

- Parameter Displays can exhibit scaling and clipping issues when rendered.
- Parameter Display 'Format' and 'Precision' settings may not apply consistently when changed.
- Plot spaces containing multiple Parameter Displays may not show 'Format' or 'Precision' options in the Parameter Display context menu.
- Plot titles and labels can be clipped or resized incorrectly when Parameter Displays are present or when panels are resized.

## UI/Window Management

- Status Bar text can be hard to read when using the "2016 Black" style or other dark themes.
- Title bar can sometimes retain the previously opened design name until the title bar is clicked or the Viewer is visited.

## Export/Reports

- Exported PDF reports may omit Graphic Plots and the Collection Table content (PDFs show blank areas where graphics/tables appear in Viewer).
- Popping out the Plot Options ribbon section can cause the ribbon tab to disappear when the ribbon is minimized.

## Tracking plots

- Phase may not be accurate when plotting a channel against a speed with a different number of blocks.
- Applied time offsets are not visible when a plot is switched to Absolute Time mode.
- Tracking plots saved in plot setup files (.dxs) prior to this release may need to be re-created due to changes in the Dewesoft file reader affecting Speed and Reference indexes.
- Decel trace may be scaled differently during mouse-wheel zoom than the accel trace and the non-split trace after splitting PKX files by rotor speed sets.
- Plot pages may not load all traces when speed parameters change order in the parameter tree (which can happen after restarting DX and reprocessing).
- Overlaid traces may disappear when the FFT blocksize is changed and the design is reprocessed; clicking the disappeared trace in the plot options dialog can cause a crash.
- FFT data may not autoscale the Magnitude plot Y-axis correctly.

## Signal/Parameter Math

- DX may crash when reprocessing a design that adds Signal Math and Parameter Math elements while existing plots (for example Order Track plots) remain open in the Viewer.
