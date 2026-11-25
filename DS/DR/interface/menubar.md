# Menu Toolbar

![menubar-e6c11377](../images/interface/images/menubar-e6c11377.png)

The Main Menu of the APEX DR user interface can be used to access most functions of
the application. Entries under the different sub-menus will be activated or
deactivated based on the status (idle or running, input source, valid or invalid
configuration, etc..) of the application.

> [!NOTE]
> Any menu option that requires a file browser is always disabled when the
> APEX DR application is in the “running” state. The reason is that
> displaying a file browser would stop all updates on all user interface
> windows.

## Time Display

The time status display has two components.

> - The time source display (left, showing SYS) shows either “IRIG” or “SYS”
>   indicating the source of the time stamp. SYS indicates the time and date is
>   directly from the OS system clock. IRIG means the time is sourced from an
>   input data source. This can be either an analog channel configured to acquire
>   the output of an IRIG-B generator or a digital time stamp provided by an
>   acquisition device.
> - The time value display (on the right) indicates the acquisition time and
>   date that corresponds to the currently displayed data block.

## File Menu

![menufile-c7675de8](../images/interface/images/menufile-c7675de8.png)

The entries under this sub-menu perform various project and project
file component related operations.

> - **New Project**: Clear out the current project and create a new project with
>   16 channels and a simulated data source. User will be prompted for the new
>   project name. The new project will inherit the current project's storage
>   "data root" settings. All other project items are reset to their default
>   values.
> - **Open Project**: Select a previously saved project file and attempt to load
>   it into the DS application.
> - **Save Project**: Save all project components using the last selected
>   project file name.
> - **Save As**: Save all project components using a newly selected project
>   file name.
> - **Import** sub-menu:
>   - **Plot Setup**: Import plot setup from a .csv file. The plot setup can be
>     from any previous DS (3.x or later) or EDAS-ds (2.x) version.
>   - **Limit Setup**: Import limit setup from a .csv file. The limit setup can
>     be from any previous APEX DS (3.x or later), EDAS-ds (2.x),  APEX DX,
>     WorkFlow or Limit Utility version. The .csv format reader used for this
>     task is fairly flexible, it can recognize and convert almost all
>     "historical" EDAS and APEX limit file formats.
>   - **Remove Limits**: Unloads a previously loaded limit file, thereby removes
>     any limit indicators from data plots and other displays.
>   - **Unit Table**: Import table of integration units from a .csv file.
> - **Export** sub-menu:
>   - **Plot Setup**: Export current plot layout to a .csv file.
>   - **Limit Setup**: Export limit setup to a .csv file.
>   - **Plot Data**: Export plots to png images, text or pptx. Export panel
>     provides option to export for selected plots, current page or all plots.
>   - **Unit Table**: Export the table of the integration units to a .csv file.
>     This will create an example integration table if a table has not already
>     been loaded.
>   - **Channels**: Export setup channels to a .csv file. The matching “export”
>     functionality is under the "Setup" sub-menu.
>   - **Parameters**: Export setup parameters to a .csv file. The matching
>     “export” functionality is under the "Setup" sub-menu.
> - **APEX Utilities** sub-menu:
>   - **Limits Utility**: Attempts to launch the APEX Limits Utility
>     (limit file editor) if it is installed.
>   - **DV**: Attempts to launch the APEX DV utility if it is installed.
> - **Exit**: Terminates the APEX DR application. Will prompt the user to save
>   any pending changes to the current project. This choice is grayed out while
>   the application is in the "running" state.

## View Menu

![menuview-dr-cc243863](../images/interface/images/menuview-dr-cc243863.png)

The entries under this sub-menu switch the main workspace area of the
application window into different modes, or show and hide various
additional dialog windows.

> - **Servers**: Switches the main workspace area of the application window
>   to a view that shows the available running DS server instances and
>   allows connecting to them.
> - **Channels**: Switches the main workspace area of the application window
>   to a view that shows the available channels on the connected Servers and
>   allows subscribing to them.
> - **Monitoring**: Switches the main workspace area of the application
>   window to the default "Data Plots" view.
> - **Screen 2**, **Screen 3**, **Screen 4**: These menu choices enable or
>   disable additional windows that display separate instances of the Data Plots
>   view. These choices may be grayed out depending on the licensing status of
>   the application.
> - **Alarms**: Displays the alarm monitoring dialog window. This can be used to
>   monitor the current value and alarm levels of parameter and channel
>   statistics data items.
> - **Preferences**: Shows application preferences dialog.

## Data Menu

![menudata-ds-0176c8e8](../images/interface/images/menudata-ds-0176c8e8.png)

This sub-menu contains entries for controlling the data monitoring and recording
functions of the APEX DR application. Entries may be enabled or grayed out
depending on the status of the data acquisition.

> - **Monitor Start**: Start data monitoring. Monitoring starts the input
>   device(s) and depending on the setup will start writing the data to the appropriate
>   data file(s). Monitoring also activates data to the plots, indicators
>   and values on any and all panels.
> - **Monitor Stop**: Stop data monitoring. Once monitoring is stopped no
>   data will be written to data files.
> - **Record On**: Begin a data point recording.
> - **Record Off**: Stop a data point recording and return to monitor mode.
> - **Record++**: Auto increment the data point number by one and then
>   start a new data point recording.
> - **Data Point Setup**: Shows the data point setup window.

## Setup Menu

![menusetup-dr-82429a0e](../images/interface/images/menusetup-dr-82429a0e.png)

Most entries under this sub-menu launch the Setup Editor of the APEX DR
application pre-focused to the information from a remote DS server application.
The editor is always shown in *read-only* mode, meaning that it only allows
inspecting the configuration data, but not editing it. Choices are:

> - **Options**: Displays a dialog (shown below) that allows the user to
>   configure  a limited number of local data acquisition options for the DR
>   application that may  be different from the configuration provided by the
>   connected DS data servers.
>
>   Locally configurable options include:
>
>   > - DS server connection priority and password (if needed).
>   > - Local data recording options.
>   > - The time limit for history data buffers,
>   > - Source of the limit setup data,
>
>   ![Example APEX DR local option configuration dialog.](../images/interface/images/menusetup-dr-aa8c451d.png)
>
>   *Example APEX DR local option configuration dialog.*
> - **Host:Project**: These choices are dynamically added to the menu based on
>   the  discovered DS data servers available on the local network. Selecting
>   any of these choices Will didplay the Setup Editor dialog for the given data
>   server.

## Help Menu

![menuhelp-88a9db96](../images/interface/images/menuhelp-88a9db96.png)

The entries under this sub-menu provide access to the help documentation
and licensing information of the application.

> - **Help Index**: Display the interactive (HTML) version of this manual focused
>   on the main index page. This uses the default web browser of the user's
>   account.
> - **User Interface**: Display the interactive (HTML) version of this manual
>   focused on the "User Interface" section. This uses the default web browser of
>   the user's desktop environment.
> - **License Agreement**: Show the APEX DS license agreement window.
> - **About**: Show the APEX DS splash panel. This contains version and
>   licensing information. This panel also provides access to all other
>   license configuration related dialogs.
