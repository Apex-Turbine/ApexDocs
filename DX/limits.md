# Scope Limits Format

Revision: 2.0

This document defines the format of scope limits files for use in APEX
products (GageMap, GmScript, DS, DR, DV, and DX). All products do not
necessarily use all components of a scope limits file.

**Overview**

Scope limits files typically contain the modal information of one or
more parts within a structure. The information is defined as sensor
(e.g., strain gage) properties. These properties can then be used to
assist the test engineer and analyst in assessing the frequency response
relative to a “limit”. The modal information consists of the following:

1. Mode name: Used to identify a specific frequency response with a
  non-numerical description, e.g., “1B”, “1F”, “2CWB”, etc.
2. Frequency: The modal frequency in Hertz. These are typically derived
  from a normal modes analysis. A frequency should be provided for each
  mode.
3. Ratio: The ratio of the sensor magnitude to some critical location.
  The critical location can be either the maximum vibratory location or
  the critical location. These locations may be different with the
  inclusion of static stress in the analysis. Ratios are typically less
  than 1.0 but may be greater than 1.0. A ratio should be provided for
  each mode.
4. Limit: The maximum vibratory response such that when achieved results
  in 100%. These are referred to as the “red line” limits. A limit
  should be provided for each mode.
5. Reduced Limit: The maximum vibratory response such that when achieved
  results in less than 100% of limit. These are referred to as the
  “yellow line” limits. A limit should be provided for each mode.

Scope limits files can be configured such that multiple sensors share
the same modal information (mode names & frequencies) or for each sensor
to have its own modal information. In the case of the former, where
multiple sensors exist on the same part, the modal ratio information can
be used to assist in assignment of the proper mode to the response.

Capability is also provided to permit the frequency, ratio and limit
definitions to vary with some other measured parameter. Typically, this
is the rotational velocity of the part, e.g., shaft speed.

**Layout**

The scope limits are defined in a Comma Separated Value (CSV) file. The
file consists of a keyword followed by one or more values separated by a
comma. Some keywords are optional and are identified below as such. Not
all keywords are used by all products, those are also identified below.
The order of the keywords as they appear in the file is important as the
file is read sequentially from top to bottom. Some flexibility does
exist and variations are shown in the examples.

**Keyword**: “Project” (Required) The project keyword contains meta-data
information

Fields:

1. Project Name, string (optional)
2. Engine Model, string (optional)
3. Facility ID, string (optional)
4. Manufacturer, string (optional)
5. Number of Parts, integer (required)

Example:

```
project, Test Rig, SN0001, Spring Hill, Apex Turbine Engines, 2
```

**Keyword**: “Part” (Required) Modal information regarding a specific
“part”. Multiple similar parts may form a component. Parts share the
same modal information.

Fields:

1. Part Name, string (optional)
2. Component Name, string (optional)
3. Number of Modes, integer (required)
4. Number of Parameter entries, integer (optional)
5. Number of Sensors, integer (required)
6. Parameter Name, string (optional)

Example:

```
part, Blade 01, Fan R1, 10, 3, 2, N,
```

In the example above, “Blade 01” is a member of component “Fan R1” and
contains 2 sensors (signals as defined below). There are 10 modes
defined for “Blade 01”, 3 parameter entries and the reference parameter
is “N”. The existence of multiple parameter entries means that at least
some of the modal information (frequencies, limits and ratios) vary with
the measured parameter “N”. “N” must be defined as a parameter in the DS
setup or in the DX design. If the parameter “N” does not exist then the
first (or lowest N) parameter information is used.

**Keyword:** “modenames” (Required) Must immediately follow the “part”
keyword. A non-numerical description for each frequency bin.

Fields: comma-separated entries the number of which must match the part
keyword, field #3

Example:

```
modenames,1B,1T,2B,2T,1CWB,
```

**Keyword:** “ftol” (Optional) Must follow the “modenames” keyword.
“ftol” defines the single peak frequency tolerance (Hz) band for which
each mode applies. “ftol” is not permitted to vary with the reference
parameter. “ftol” is optional and if not present, results in adjacent
mode bins. “ftol”, at most, can result in adjacent mode bins, i.e., ftol
will be truncated such that overlapping mode bins are not permitted.

Fields: comma-separated entries the number of which must match the part
keyword, field #3

Example:

```
ftol,50,100,25,200,
```

**Keyword:** “param(#)” (Optional) Must be subsequent to the “part”
keyword. Defines the variation of the basis for varying frequencies,
limits and ratios. The “param” entries are required if the part keyword
field #4 is greater than 0. The “#” following “param” is simply an index
that goes from 1 to the value in the part keyword field #4. While the
parameter values are permitted to vary by mode it is discouraged such
that a subsequent release of the scope limits format will remove this
capability. The parameter entries must increase with the index value.

Fields: comma-separated entries the number of which must match the part
keyword, field #3

Assume part keyword #4 is equal to 3, therefore, there must be 3 “param”
fields indexed by 1, 2 and 3.

Example:

```
param1, 2000, 2000, 2000, 2000,

param2, 5000, 5000, 5000, 5000,

param3, 10000, 10000, 10000, 10000,
```

**Keyword:** “freq(#)” (Required) Must be subsequent to the “part”
keyword. Mode frequency values in Hertz. Multiple “freq” entries are
required if the part keyword field #4 is greater than 0. The “#”
following “freq” is simply an index that goes from 1 to the value in the
part keyword field #4. A “time domain” can be defined by specifying a
frequency of 0 Hz. This must be the first mode defined.

Fields: comma-separated entries the number of which must match the part
keyword, field #3

Example:

```
freq1, 100, 250, 400, 600, 1000,
```

**Keyword:** “signal” (Required) Must be subsequent to the “part” &
“freq” keywords. Must exactly match a channel name in the dynamic data
file. The number of signal entries must match the 5 <sup>th</sup> field in
the part keyword prior to the next “part” keyword.

Fields: signal name (string)

Example:

```
signal,SG01,
```

**Keyword:** “scopelimit(#)” (Optional) Must be subsequent to the
“signal” keyword. Mode limit values, e.g., “red line” limits. Multiple
“scopelimit” entries are required if the part keyword field #4 is
greater than 0. The “#” following “scopelimit” is simply an index that
goes from 1 to the value in the part keyword field #4. The values should
be consistent with the units (PSI, KSE, MPa, g’s, etc.) and scaling
(Peak-to-Peak, RMS, single Peak) used for decoding the dynamic signal
data.

Fields: comma-separated entries the number of which must match the part
keyword, field #3

Example:

```
scopelimit1, 200, 100, 80, 60, 35,
```

**Keyword:** “reducedlimit (#)” (Optional) Must be subsequent to the
“signal” keyword. Mode limit values, e.g., “yellow line” limits.
Multiple “reducedlimit” entries are required if the part keyword field
#4 is greater than 0. The “#” following “reducedlimit” is simply an
index that goes from 1 to the value in the part keyword field #4. The
values should be consistent with the units (PSI, KSE, MPa, g’s, etc.)
and scaling (Peak-to-Peak, RMS, single Peak) used for decoding the
dynamic signal data. “Yellow” limits are generally lower than “red”
limits but this is not enforced. “reducedlimit” is not required and not
utilized in DX.

Fields: comma-separated entries the number of which must match the part
keyword, field #3

Example:

```
reducedlimit1, 120, 60, 50, 30, 25,
```

**Keyword:** “strainratio (#)” (Optional) Must be subsequent to the
“signal” keyword. Mode ratio values. Multiple “strainratio” entries are
required if the part keyword field #4 is greater than 0. The “#”
following “strainratio” is simply an index that goes from 1 to the value
in the part keyword field #4. The values are typically less than 1 and
can be either positive or negative. “strainratio” is not required and
not utilized in DS & DR.

Fields: comma-separated entries the number of which must match the part
keyword, field #3

Example:

```
strainratio1, -0.85, 0.32, -0.90, 0.01, 0.65,
```

## Example Scope Limit Files

Example #1: Single limit across many signals:

```
project,,,,,1

part,Part 1,,1,,4,

modenames,all_modes,

freq1,2500,

signal,SG01,

signal,SG02,

signal,SG03,

signal,SG04,

strainratio1,1.0,

scopelimit1,60,

reducedlimit1,40,
```

Example #2: Single limit, signal dependent:

```
project,,,,,1

part,Part 1,,1,,4,

modenames,all_modes,

freq1,2500,

signal,SG01,

scopelimit1,40,

strainratio1,1.0,

signal,SG02,

scopelimit1,60,

strainratio1,1.0,

signal,SG03,

scopelimit1,30,

strainratio1,1.0,

signal,SG04,

scopelimit1,100,

strainratio1,1.0,
```

Example #3: Time & frequency domain limits:

```
project,,,,,1,

part,Part 1,,2,,4,

modenames,Time,Freq,

freq1,0,2500,

signal,SG01,

signal,SG02,

signal,SG03,

signal,SG04,

scopelimit1,80,60,

strainratio1,1.0,1.0,
```

Example #4: Frequency dependent limits, adjacent modes:

```
project,,,,,1,

part,Part 1,,4,,4,

modenames,1F,1T,2F,Unk,

freq1,500,1000,2000,3000,

signal,SG01,

scopelimit1,30,40,50,60,

signal,SG02,

scopelimit1,55,44,53,68,

signal,SG03,

scopelimit1,89,100,64,77,

signal,SG04,

scopelimit1,41,93,47,35,
```

Example #4a: Frequency dependent limits, non-adjacent modes:

```
project,,,,,1,

part,Part 1,,4,,4,

modenames,1F,1T,2F,Unk,

ftol,50,100,200,0

freq1,500,1000,2000,3000,

signal,SG01,

scopelimit1,30,40,50,60,

signal,SG02,

scopelimit1,55,44,53,68,

signal,SG03,

scopelimit1,89,100,64,77,

signal,SG04,

scopelimit1,41,93,47,35,
```

Example #5: Frequency dependent limits, limits vary with a parameter:

```
project,,,,,1,

part,Part 1,,5,4,1,N,0,

modenames,Time,1F,1T,2F,Unk,

param1, 600, 600, 600, 600, 600,

freq1 , 0, 300, 800, 1500, 2000,

param2, 1200, 1200, 1200, 1200, 1200,

freq2 , 0, 400, 900, 1700, 2200,

param3, 6000, 6000, 6000, 6000, 6000,

freq3 , 0, 500, 950, 1900, 2400,

param4, 9000, 9000, 9000, 9000, 9000,

freq4 , 0, 600, 1100, 2000, 2500,

signal,SG01,

scopelimit1,90,60,40,50,60,

scopelimit2,80,55,35,45,60,

scopelimit3,70,50,30,40,60,

scopelimit4,60,45,25,35,60,
```

Example #5a: Frequency dependent limits, limits vary with a parameter
(alternate definition):

```
project,,,,,1,

part,Part 1,,5,4,1,N,0,

modenames,Time,1F,1T,2F,Unk,

param1, 600, 600, 600, 600, 600,

param2, 1200, 1200, 1200, 1200, 1200,

param3, 6000, 6000, 6000, 6000, 6000,

param4, 9000, 9000, 9000, 9000, 9000,

freq1 , 0, 300, 800, 1500, 2000,

freq2 , 0, 400, 900, 1700, 2200,

freq3 , 0, 500, 950, 1900, 2400,

freq4 , 0, 600, 1100, 2000, 2500,

signal,SG01,

scopelimit1,90,60,40,50,60,

scopelimit2,80,55,35,45,60,

scopelimit3,70,50,30,40,60,

scopelimit4,60,45,25,35,60,
```
