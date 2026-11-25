# Display Toolbar

![statusbar](../images/interface/images/statusbar.png)

The parameter display area is a mouse click configured display that
allows for any parameter name and current value to be pinned. Multiple
parameters can be added to the box, as many of them will be visible as
the window size allows.

The limit indicator has three LED displays. These have four possible
states:

> - **Background** (typically gray) color indicates that the condition is not
>   applicable in the current configuration. Example: no limits are loaded.
> - **Green** color indicates that all channels are within limits.
> - **Yellow** color indicates that some channels are close to configured
>   limits.
> - **Red** color indicates that some channels have exceeded their limits.

The meaning of the three LED displays is as follows:

> - **Top|Left** LED indicates ADC channels are saturated.
> - **Center** LED indicates overall time domain amplitudes are exceeded.
> - **Bottom|Right** LED indicates mode limits are exceeded.

These LED displays are clickable. This causes them to display a summary dialog
with the list of channels that exceed their respective limits.

> [!NOTE]
> The parameter display area is the part of the top tool bar that expands or
> shrinks as the application window is resized. So the number of parameter
> values that can be displayed, and the display configuration (single or
> double row) will depend on the window size.
