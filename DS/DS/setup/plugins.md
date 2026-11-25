# Processing Plugins

The APEX DS software installation includes a "standard" set of data processing
plugins.  The usage of these is described in this Section. In addition to the
standard ones, users can also use their own custom plugins built using the DS
API package.

## Eval Plugin

This plugin evaluates an arithmetic expression and replaces the data sample(s)
of its owner to with the result. This plugin is available for both  parameters
and channels, for the latter it executes at the **time plugin** stage of the
data processing. It is activated by the following configuration line:

```
eval expression
```

The supported expression format is identical to the one described on the
[setupcomputed-link](#setupcomputed-link) with one exception: In this context self referencing
expressions (i.e. ones that contain  the owner as an operand) are allowed.

## FIR Filter Plugin

This plugin implements an FIR (Finite Impulse Response) digital filter. These
filters execute at the **raw plugin** stage of the data processing. This module
is activated by entering a line with one of the following two forms in the
processing configuration:

```
firfilter Type Proto Order Fmin [Fmax [Tune]]
firfilter Type File
```

*Where:*

> - Type: L, H, N, B.
>
>   > - L = Low pass
>   > - H = High pass
>   > - N = Notch
>   > - B = Band pass
> - Proto: PM, HN, HM, NU, BL, BH, BN, GA.
>
>   > - PM = Parks-McClellan optimal filter design (recommended).
>   > - HN = DFT generated filter with Hanning Window.
>   > - HM = DFT generated filter with Hamming Window.
>   > - NU = DFT generated filter with Nuttall Window.
>   > - BL = DFT generated filter with Blackman Window.
>   > - BH = DFT generated filter with Blackman-Harris Window.
>   > - BN = DFT generated filter with Blackman-Nuttall Window.
>   > - GA = DFT generated filter with Gaussian Window.
> - Order: Filter order (number of 'taps').
> - Fmin: Filter frequency (Low end value for notch and band pass).
> - Fmax: High end frequency value for notch and band pass.
> - Tune: Tuning parameter for 'PM' filters.
> - File: Filter coefficient file to use. See below.

**Synthesized Filters**

All frequency specifications are for the cutoff frequency (or 3dB point)
of the filter. The built-in synthesizer will accept the 1..99% range of the
channel's Nyquist rate for the filter frequencies. The accepted order range is
5...253 for the FFT-based filters and 9..127 for the Parks-McClellan filter.

The optional tuning parameter for the Parks-McClellan filter has a
practical range of 0.5..2.0. It can be used to adjust the width of the filter's
transition band. In general, a narrower transition band will mean more
ripples and vice-versa. The default transition band size is determined based on
the filter's order, and results in approximately 0.1dB pass-band ripple.

**Filters Created from Data Files**

This module supports loading FIR filter coefficients from a custom APEX defined
CSV file format. Several such files have been included with this distribution,
consult any of them for the supported syntax.

> - Filter types L and H require only one additional argument: The filter file name.
> - Filter types N and B require two filter file name arguments: These are used to
>   define the lower and upper frequencies of the resulting notch or band filter.

All included filter files are defined as low pass filters with inversion and
concatenation taking place within the plugin as necessary for H, N and B filter
types. All files contain zero phase filters meaning that there will be no phase
shift as a function of frequency when using them.

The FIR filters listed below are provided in the install package of this APEX
software. The pass band and stop band are listed as a percentage of the sample
rate for the channel. Keep in mind that the pass and stop band values will swap
whenever the filter is transformed for a high pass application.

| Name | Pass Band (%SR) | Stop Band (%SR) |
| --- | --- | --- |
| FIR-LP-000175.csv | 0.175 | 3.1 |
| FIR-LP-000175L.csv | 0.175 | 1.925 |
| FIR-LP-00035.csv | 0.35 | 3.85 |
| FIR-LP-00035L.csv | 0.35 | 2.3 |
| FIR-LP-000525.csv | 0.525 | 4.5 |
| FIR-LP-000525L.csv | 0.525 | 2.33 |
| FIR-LP-0007L.csv | 0.7 | 2.375 |
| FIR-LP-000875.csv | 0.875 | 4.675 |
| FIR-LP-000875L.csv | 0.875 | 2.75 |
| FIR-LP-00105.csv | 1.05 | 4.75 |
| FIR-LP-00105L.csv | 1.05 | 3.0 |
| FIR-LP-001225.csv | 1.225 | 4.78 |
| FIR-LP-001225L.csv | 1.225 | 3.1125 |
| FIR-LP-0014.csv | 1.4 | 4.85 |
| FIR-LP-0014L.csv | 1.4 | 3.1875 |
| FIR-LP-001575.csv | 1.575 | 4.95 |
| FIR-LP-001575L.csv | 1.575 | 3.275 |
| FIR-LP-00175.csv | 1.75 | 5.475 |
| FIR-LP-00175L.csv | 1.75 | 3.615 |
| FIR-LP-025.csv | 2.5 | 10.0 |
| FIR-LP-050.csv | 5.0 | 12.5 |
| FIR-LP-075.csv | 7.5 | 15.0 |
| FIR-LP-100.csv | 10.0 | 17.5 |
| FIR-LP-125.csv | 12.5 | 20.0 |
| FIR-LP-150.csv | 15.0 | 22.5 |
| FIR-LP-175.csv | 17.5 | 25.0 |
| FIR-LP-200.csv | 20.0 | 27.5 |
| FIR-LP-225.csv | 22.5 | 30.0 |
| FIR-LP-250.csv | 25.0 | 32.5 |
| FIR-LP-275.csv | 27.5 | 35.0 |
| FIR-LP-300.csv | 30.0 | 37.5 |
| FIR-LP-325.csv | 32.5 | 40.0 |
| FIR-LP-350.csv | 35.0 | 42.5 |
| FIR-LP-375.csv | 37.5 | 45.0 |

## IIR Filter Plugin

This plugin implements an IIR (Infinite Impulse Response) digital filter. This
plugin is used at the **time plugin** stage of the processing.  It is activated
by entering a line with one of the following two forms in the processing
configuration:

```
iirfilter Type Proto Order Fmin [Fmax [Ripple [Atten]]]
iirfilter File
```

*Where:*

> - Type: L, H, N, B.
>
>   > - L = Low pass
>   > - H = High pass
>   > - N = Notch
>   > - B = Band pass
> - Proto: BU, BE, CH, IC, EL.
>
>   > - BU = Butterworth Filter.
>   > - BE = Bessel Filter.
>   > - CH = Chebyshev Filter.
>   > - IC = Inverse Chebyshev Filter.
>   > - EL = Elliptical Filter.
> - Order: Filter order (number of 'poles' and 'zeros').
> - Fmin: Filter frequency (Low end value for notch and band pass).
> - Fmax: High end frequency value for notch and band pass.
> - Ripple: Pass band ripple in dB (0.01..6.0).
> - Atten: Mimimum stop band attenuation in dB (30..120).
> - File: Filter coefficient file to use. See below.

**Synthesized Filters**

All frequency specifications are for the cutoff frequency (or 3dB point) of the
filter. The built-in synthesizer will accept the 0.05..99% range of the
channel's Nyquist rate for the filter frequencies. The accepted order range is
1..10. The Elliptical and both Chebyshev filter types can be tuned with the
optional pass band ripple and stop band attenuation parameters. Defaults are
0.1dB for ripple and 60dB for attenuation. Generally, using more permissive
values for these will result in a sharper transition band.

**Filters Created from Data Files**

This module supports loading IIR filter coefficients from a custom APEX defined
file format. Several such files have been included with this distribution,
consult any of them for the supported syntax. Matlab generated 'FCF' format
files are also supported.

The included filter files are pre-generated low frequency high pass Butterworth
filters mostly intended for removing low frequency noise (such as 50 or 60 Hz
power, etc..) from measured channels. These filters are **not** invertable
(unnlike the FIR filter files listed above). Their naming convention is:

```
IIR_H_BU_###_##.dat
```

Where the first group of three digits represents the cutoff frequency in
1/1000th-s of the sample rate. The second two digit group indicates the filter
order (3, 6 or 10). Filters were generated for every 1/1000th increment in the
cutoff frequency, but only the numerically stable ones are included in this
software distribution.

> [!WARNING]
> IIR filters will cause a phase distortion in the data. They should
> not be used if phase retention is desired.

## Decibel Scaled Stats

This plugin generates dB scaled channel stats from the supported 'standard’ APEX
DS/DX 'amplitude' type stat values (RMS, peak to peak, zero to peak or
average). This plugin executes at the **peak plugin** stage of the data
processing.  It is invoked via a formula line of the following form:

```
dbstat nominal stat min max alarm warning
```

The arguments and their default values (when omitted) to this plugin are as follows.
Note that the last four values are optional.

> - nominal: nominal signal level for 0 dB [in EU].
> - stat: base stat name. accepted: RMS, P2P, PEAK and AVG
> - min: plot axis minimum [dB] (default: -40)
> - max: plot axis maximum [dB] (default: 40)
> - alarm: alarm level [dB] (default: no alarm)
> - warning: warning level [dB] (default: no warning)

This plugin applies to processed data only.

## Windowed Stats Plugin

This plugin produces a copy of the 'standard' APEX DS/DX channel stats over a
longer time window instead of the duration of a single block. The new statistics
are available under signals in the plot data selector tree and can be used in
the alarms window. This plugin executes at the **time plugin** stage of the data
processing.  It is activated by the following configuration line setup:

```
windowstats avgtime
```

Where:

> avgtime: time interval in seconds over which the stats will be
> averaged. Specify time range from 0.01 to 10.00 seconds.

## Order Track Plugin

This plugin adds channel stats tracking selected orders based on the value of
the default forcing speed parameter assigned to the channel. This plugin
executes the **peak plugin** stage of the data processing. It is invoked via a
configuration line of the following form:

> ordertrack orderspec ...

One or more order specifications can be given. Each order specification has
the following format:

```
ORDER/ORDERTOL/FREQTOL:ALARM:WARNING
```

Where:

> - ORDER: The value [i.e. forcing parameter multiplier] of the order to track.
> - ORDERTOL: Tolerance band in order units, Default is 0.1
> - FREQTOL: Tolerance band in frequency units. Default is the channel FFT bin width.
> - ALARM: The [red] alarm level. Default is no alarm.
> - WARNING: The [yellow] warning level. Default is no warning.

> [!NOTE]
> - For this plugin to work channels **must** have default assigned speed parameters.
> - Tolerance and/or alarm level values can be omitted.
> - The actual frequency tolerance will be the maximum of the two values specified.

## Alarm Levels Plugin

This plugin does not do any processing on the data. Its only purpose is to add
alarm limit values to already defined 'standard' channel statistics. This plugin
is nominally assigned to the **peak plugin** stage of the data processing.  It
is invoked via a configuration line of the following form:

```
statlimit limitdef ...
```

One or more limit definitions can be given. Each limit definition has
the following format:

```
STATNAME:ALARM:WARNING
```

Where:

> - STATNAME: The name of the stat for which limits are defined.
> - ALARM: The [red] alarm level.
> - WARNING: The [yellow] warning level. This can be omitted.

## Thermocouple Plugin

This plugin converts measured DC voltage data into a temperature value using
standard thermocouple (type B, E, J, K, N, R, S, T) conversion tables available
from NIST. Output can be scaled in different temperature units. This plugin
executes at the **time plugin** stage of the data processing. It is activated by
the following configuration line:

```
thermocouple TYPE CJC UNIT
```

Where:

> - TYPE: thermocouple type (B, E, J, K, N, R, S, T)
> - CJC: cold junction compensation
> - UNIT: temperature units (K, C, F)

## Spike Filter Plugin

The spike filter plugin implements an non-linear digital filter for removing
short duration spikes from a channel's raw input data. This plugin executes at
the **raw plugin** stage of the data processing. It is activated by the
following configuration line:

```
spikefilter CFL MAXN MAXW CSAT
```

*Where:*

> - CFL: Crest Factor Limit, samples above this limit are considered noise. The
>   crest factor is the ratio of a sample's deviation from the data block's mean
>   value versus the data block's RMS average. [Default = 4]
> - MAXN: Maximum number of noise spikes the filter will remove from a data
>   block. [Default = 4]
> - MAXW: Maximum permitted width of a noise spike the filter will remove from a
>   data block. [Default = 6]
> - CSAT: When non-zero then re-check the data for saturation if it was flagged
>   as saturated, and if this filter removed any spikes. [Default = 0]

If the input data block contains more spikes or wider spike(s) than the
specified limits, the data is not modified at all. If the count and width(s) of
the detected spikes are within the specified limits then all found spikes are
removed via linear interpolation using samples on the sides of each spike.

This filter adds the number of spikes as a 1/block statistics value to the
channel's stats.

## Spike Noise Plugin

This plugin is a companion to the spike filter plugin described above. It will
flag peaks as noisy when spikes found by the spike filter could not be removed.
If all spikes were removed or no spikes were found, the data will not be flagged
as noise. This plugin executes at the **peak plugin** stage of the data
processing. It is activated by the following configuration line:

```
noisespikes
```

This plugin has no arguments.
