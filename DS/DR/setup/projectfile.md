# Project file

DS, DR and DV need to manage and store many settings to
configure their data acquisition. processing and display environments.
These settings fall into two categories:

1. Global settings are values that are the same no matter what data
  acquisition or processing job is performed. Typical settings for this
  group include user interface preferences, printer configuration, etc.
  These are stored separately for each user in a "profile directory"
  under the user's home folder.
2. Project settings are values that are specific to a given data
  processing or acquisition job. These are grouped together into an
  DS project file. These project files have several sections, many
  of which can be individually exported to or imported from more "user
  friendly" file formats such as CSV. The DS project file sections
  include:
  - Data source: for specifying and configuring the input for the data
    processing.
  - Data processing: for specifying the options for each data channel
    such as names, units, scales, etc.
  - Modes and limits: for specifying mode frequencies and limits for
    overall time domain and spectral peak amplitudes.
  - Plot setup: for specifying the layout and contents of the plot
    areas of the DS user interface.
  - Data recording: includes data recording directories, data point
    header fields and data file templates.

Project settings are stored in APEX internal format project files. These
have the ".dspro" extension.

The DS user interface uses the title bar of its main window to show
the status of the currently active project. The text displayed here
includes:

- The name of the currently active project.
- The status of the currently active project. i.e. whether it contains
  unsaved changes.
- The name of the currently recorded data point (if any).
- The name of the currently processed data file in playback mode (if
  any).

Although the DS project files are human readable text files, users
are strongly discouraged from editing them  manually. APEX, Inc. make no
guarantees that the format of these files will stay identical between
software revisions. The only thing guaranteed is that later versions
will be able to "import" earlier versions' project files.
