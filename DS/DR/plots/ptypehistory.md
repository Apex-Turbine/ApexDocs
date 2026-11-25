# History Plots

History Plots display long term collected values for one or more
parameters or channel stats. These plots:

> - Require the selection of the following items on the [plotcreate-link](#plotcreate-link) tab
>   before adding them to the plot grid:
>
>   > - One or more primary parameters or channel stats.
>   > - Optionally, one parameter or channel stat to use as the X axis value instead of time.
> - Do **not** extend the [plotmenu-link](#plotmenu-link) with additional choices.
> - Do **not** add extra pages to the [plotsetup-link](#plotsetup-link) dialog.
> - Provide **no** additional user interaction mechanisms beyond the 'standard' ones
>   described in the [plotactions-link](#plotactions-link) section.

![Example History Plot](../images/plots/images/ptypehistory-c447ad2e.png)

*Example History Plot*

The time (or equivalent block) range of all history plots is configured to
match the length of the data file when it is opened for playback. Time values
displayed on the X axis (when not overridden) are relative to the start of
the file.
