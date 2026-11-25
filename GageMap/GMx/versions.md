# GageMap Version History

## 2025.51

Changes:

> 1. Fixed an issue in GM where gages were not mapped to the correct group when using the Quantity Optimizer with placement set to a specific group.
> 2. - **Fixed various Sensor List interface issues:**: - Sensor List not updating when switching Library
>   - Sensors not being selected when the sensor library selection is changed
>   - Sensor summary panel not being filled out even though a sensor is selected
>   - Arrow keys not having the same effect as clicking in the sensor libraries list
> 3. Fixed a crash in GM that could occur when deleting a sensor.

Known Issues:

1. **Different strain gage coordinate systems between GMx and GM Legacy**

  > - **Impact:** Minor Inconvenience
  > - **Details:** GMx (New UI) reports local gage coordinates with y-axis reflected across XZ-plane (left-hand orientation) while GM Legacy uses global coordinate system as expected. This can make direct comparisons between versions more difficult.
2. **Reports do not display normalization group information**

  > - **Impact:** Inconvenience
  > - **Details:** When normalization group is set in sensors section, reports fail to display which group sensors are being normalized to, unlike GageMap Legacy behavior
3. **Quantity Optimizer takes longer than GM Legacy**

  > - **Impact:** Minor Inconvenience
  > - **Details:** May be caused by thread count not utilizing full hardware capability by default
  > - **Workaround:** Manually set number of threads in preferences to maximum thread count to improve performance
4. **Table headers may not be sized in a user-friendly way**

  > - **Impact:** Minor Inconvenience
  > - **Details:** Column headers and sizing can make tables difficult to read and navigate
5. **CSV export contains only absolute values of modal displacements**

  > - **Impact:** Inconvenience
  > - **Details:** Nodal results exported to CSV show only positive modal displacements, even for nodes with negative displacements. Issue not present in GM 3.14.12
6. **Imaginary result export is incorrect for complex results**

  > - **Impact:** Inconvenience
  > - **Details:** Displacement/strain/stress exported for imaginary results are identical to real results instead of correct imaginary values. Issue not present in GM 3.14.12
7. **Switching the Current Sensor Library while in the Sensors tab and returning to the Model tab may clear the Micro Strain values in the Modes table**

  > - **Impact:** Minor inconvenience
  > - - ****Workarounds:****: - If the Current Sensor Library has multiple sensors, simply switch to another sensor in the Scale Sensor dropdown and switch back
  >   - If the Current Sensor Library has only one sensor, return to the Sensors tab, click the name of the sensor in the Sensors table to activate it, go back to the Model tab, switch the radio button to Stress and then back to Strain
8. **Opening more than 2 models/projects causes previous projects to reset their contour & displacement settings**

  > - **Impact:** Minor inconvenience
  > - **Workaround:** Click on affected models' sub-windows to re-activate and refresh them
9. **Saving an SDR as a Project with no additional libraries creates a Fatigue library anyway**

  > - **Impact:** No impact; logged for informational purposes
  > - **Details:** The underlying GM framework currently requires a default Fatigue library to be created, so one will be created for you and referenced in the Project file. The automatically created fatigue library is not visible in the UI
10. **Sensors previously mapped to high curvature locations may not be mapped when reloading the project**

  > - **Impact:** Minor inconvenience.
  > - **Workaround:** Remap the sensor if unmapped when the project is loaded, increasing the curvature tolerance as needed
11. **Selected Face Indicator moves to an adjacent face when the model is switched between Max and Neutral displacement**

  > - **Impact:** Minor inconvenience
  > - **Workaround:** This is just something to be aware of until it is fixed. The Property & Value pairs for the selected Face in the Model Info panel remain unchanged; only the red graphical indicator changes
12. **Sensor Color changes to black when Cancel button is pressed in color picker dialog**

  > - **Impact:** Minor inconvenience
  > - - ****Workaround:** Until this is fixed, avoid clicking cancel and/or save important colors with the Add to Custom Colors button.**: - If you've changed your previous color and would like to revert, you can reclaim it from the Selected Sensor color swatch with the Pick Screen Color button BEFORE you click OK in the Select Color dialog.
13. **Newly created sensors do not always use the color set in Preferences**

  > - **Impact:** Minor inconvenience
  > - **Workaround:** Until this is fixed, you may need to change the color in the Sensor Setup panel (the Prefs color will be used for newly created sensor libraries)
14. **Sensor selection indicator only shows up for one sensor**

  > - **Impact:** Minor inconvenience
  > - **Workaround:** Until this is fixed, you may need to click the sensor on the model to ensure your desired selection is made

## 2024.39

Changes:

- Refactored code for more efficient operation
- UI updates
- Fixed bugs:

  > 1. Addressed an issue in GAGEMAP BASE v2024.2.4 where sensors did not map correctly when loading from a file.
  > 2. Fixed an issue in GM where changes in the animation table did not prompt changes in the Goodman diagram.
  > 3. Resolved an issue in GM where mode amplitudes were not updated properly in the animation table.
  > 4. Fixed a problem in GM where there was no prompt to save when closing a project.
  > 5. Addressed an issue in GM where the File menu initially showed a “Quit Gagemap” button instead of the File menu.
  > 6. Fixed a crash in GM when changing the displacement scale after closing the animation library.
  > 7. Resolved a crash in GM that occurred in the release build but not in the debug build when opening a project
  > 8. Addressed an issue in GM where newly opened models were cropped at the top and bottom of the model window
  > 9. Fixed a problem in GM where mode amplitudes loaded from a file were incorrect when more than one sensor was active.
  > 10. Resolved an issue in GM where the animation was not cleared when the last library was closed.
  > 11. Fixed an issue in GM where saving an animation library reset the animation mode
  > 12. Addressed a problem in GM where loading an animation library disregarded animation mode and contour settings.
  > 13. Fixed an issue in GM where saving an animation library caused the last library in the list to be selected.
  > 14. Resolved an issue in GM where closing an animation library left the list with no selection.
  > 15. Fixed a problem in GM where the contour type was not being loaded from a file or handled when changing animation libraries.
  > 16. Fixed an issue in GM where the sensor color code on the color swatch was sometimes unreadable
  > 17. Fixed an issue in GM where the property columns showing face and node selections would be resized too small on each selection

Known Issues:

1. **Documentation does not contain up-to-date screenshots, and some buttons, features, and text may have changed or been removed**

  > - **Impact:** Inconvenience
  > - **Workaround:** While most functionality should be apparent via text and tooltips in the software, if any usability questions should arise please log a ticket @ [https://users.apexturbine.com/](https://users.apexturbine.com/)
2. **Opening more than 2 models/projects may cause previous projects to reset their contour & displacement settings. This is suspected to be an OpenGL bug.**

  > - **Impact:** Minor inconvenience
  > - **Workaround:** Click on the affected models' sub-windows to re-activate and refresh them
3. **Opening more than 2 models/projects may cause the contour legend to appear distorted until a different animation library is selected. This is suspected to be an OpenGL bug.**

  > - **Impact:** Minor inconvenience.
  > - **Workaround:** Switch to a different animation library if multiple are present, then switch back. Alternatively, change the Animation Mode setting and then change back to the previous setting.
4. **Sensors previously mapped to high curvature locations may not be mapped when reloading the project**

  > - **Impact:** Minor inconvenience.
  > - **Workaround:** Remap the sensor if unmapped when the project is loaded, increasing the curvature tolerance as needed
5. **Switching the Current Sensor Library while in the Sensors tab and returning to the Model tab may clear the Micro Strain values in the Modes table**

  > - **Impact:** Minor inconvenience.
  > - - ****Workarounds:****: - If the Current Sensor Library has multiple sensors, simply switch to another sensor in the Scale Sensor dropdown and switch back
  >   - If the Current Sensor Library has only one sensor, return to the Sensors tab, click the name of the sensor in the Sensors table to activate it, go back to the Model tab, switch the radio button to Stress and then back to Strain
6. **The red Selected Node and Selected Face indicators as well as the small Node indicators may briefly become invisible when changing the view (rotating, panning, zooming, etc.) This is suspected to be an OpenGL bug.**

  > - **Impact:** Minor inconvenience
  > - **Workaround:** Change the viewing angle such that the invisible elements become visible again. Until the issue is resolved, it will be best to refrain from changing the view while selecting faces or nodes for inspection
7. **Selected Face Indicator moves to an adjacent face when the model is switched between Max and Neutral displacement**

  > - **Impact:** Minor inconvenience
  > - **Workaround:** This is just something to be aware of until it is fixed. The Property & Value pairs for the selected Face in the Model Info panel remain unchanged; only the red graphical indicator changes
8. **Saving an SDR as a Project with no additional libraries creates a Fatigue library anyway**

  > - **Impact:** No impact; logged for informational purposes
  > - **Details:** The underlying GM framework currently requires a default Fatigue library to be created, so one will be created for you and referenced in the Project file
9. **Newly created sensors do not always use the color set in Preferences**

  > - **Impact:** Minor inconvenience
  > - **Workaround:** Until this is fixed, you may need to change the color in the Sensor Setup panel (the Prefs color will be used for newly created sensor libraries)
10. **Sensor selection indicator only shows up for one sensor**

  > - **Impact:** Minor inconvenience
  > - **Workaround:** Until this is fixed, you may need to click the sensor on the model to ensure your desired selection is made
11. **Sensor Color changes to black when Cancel button is pressed in color picker dialog**

  > - **Impact:** Minor inconvenience
  > - - ****Workaround:** Until this is fixed, avoid clicking cancel and/or save important colors with the Add to Custom Colors button.**: - If you've changed your previous color and would like to revert, you can reclaim it from the Selected Sensor color swatch with the Pick Screen Color button BEFORE you click OK in the Select Color dialog.

## 2020.8.xxx

Changes:

- Initial Release

Known Issues:

# GageMap Version History (pre-release)

## 2020.5.1777

- Fix generic window titles (e.g. "Dialog," "Form," etc.)
- Fix generic Qt window icons
- Fix missing GageMap icon in tray/shortcuts on Windows
- Add missing GageMap and APEX logos in all reports.
- Make the reports footer more consistent; fix issue where report footer was red
- Implement License Agreement action for associated task in "File" menu

## 2020.4.1731

- Fixed Sensor Length and Width UI layout to be consistent.
- Added Help link to online documentation.
- Added 3Dconnexion spaceball support.
- Fixed Contour Scaling preference.
- Change snapshot report to text improve performance (using pure HTML is not workable for performance reasons).
- Fixed where Max Principals normalization was not set correctly.

## 2020.1.1692

- Complete GageMap Update
- New UI
- New File System
- Updated Design Features
- Multi-Model Support
- Multi Threaded Rendering
- Saving Designs from Optimizer Runs
- Fatigue Material Definitions - User Defined
- Dynamic Updated Reports for Sensor Modification
