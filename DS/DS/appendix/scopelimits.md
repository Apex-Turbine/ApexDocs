# Scope Limits File Format

**Scope Limits File**

The CSV Scope Limits file is an APEX mode setup configuration file that
is comma separated. Notice that during the explanation of the different
sections of the file you will see the word "Optional" which specifies
that this section is not required to be in the file. The CSV file format
is flexible in the sense that you can have multiple variations of the
content and the setup information will load in fine. The Scope Limits
file is a reduced model that is used throughout APEX products, such as
GageMap, DS/DR, and DX. Scope Limits files support component, part, and
signal breakdown. A component is an assembly of "similar" parts. A part
is a single structure with identical modes that contains one or more
sensors. A signal is the measurement identity.

**Keywords**

**Keyword: project (Optional)**

Project is a keyword providing project information followed by the
Project Name, the Engine Model, the Facility ID, the Manufacturer,and
the Number of Parts.

- Project Name: string, name of the project (Optional).
- Engine Model: string, model of the engine (Optional).
- Facility ID: string, name of the testing facility (Optional).
- Manufacturer: string, engine manufacturer (Optional).
- Number of Parts: integer, number of parts in the component (Required).

Example:  

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| project | Test Rig | SN0001 | ACME | Acme Turbine Engines | 2 |

**Keyword: part (Required)**

The part keyword is a required string followed by the Part Name, Component Name,
the Number of Modes, the Number of Parameter Entries, the Number of Sensors,
the Parameter Name, and the Interpolation Scheme.

- Component Name: string, name of the component (Optional).
- Number of Modes: integer, number of modes present (Required).
- Number of Parameter Entries: integer, number of parameter values provided in
- the data tables (Optional).
- Number of Sensors: integer, number of sensors used on the part
  (Required).
- Parameter Name: string, name of the parameter that is being used for
  interpolating between points (Optional).
- Interpolation scheme: integer (Optional).

Example:  

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| part | Blade 01 | Fan R1 | 10 | 3 | 2 | N | 0 |

**Part Dependent Keywords**

These keywords must follow the "part" keyword.

**Keyword: modenames (Required)**

modenames: string, list of all mode names.

Example:  

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| modenames | 1B | 1T | 2B | 2T | 1CWB |

**Keyword: ftol (Optional)**

ftol- float, single peak frequency band for which a specific mode
applies. No ftol = adjacent mode bins.

Example:  

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ftol | 50 | 25 | 100 | 200 |

**Keyword: param(#) (Required)**

param(#): float, (#) = 1 (default) or the parameter index entry.

Example:  

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| param1 | 0 | 0 | 0 | 0 | 0 |

**Keyword: freq(#) (Required)**

freq(#): float, (#) = 1 (default) or the parameter index entry
followed by the nominal frequency values defined for each mode.

Example:  

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| freq1 | 100 | 250 | 400 | 600 | 1000 |

**Keyword: freqmin(#) (Optional)**

freqmin(#): float, (#) = 1 (default) or the parameter index entry
followed by the min frequency values.

Example:  

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| freqmin1 | 0 | 332.629 | 848.732 | 1398.89 | 1894.86 | 2418.47 | 2867.31 |

**Keyword: freqmax(#) (Optional)**

freqmax(#)- float, (#) = 1 (default) or the parameter index entry
followed by the max frequency values defined for each mode.

Example:  

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| freqmax1 | 332.529 | 848.632 | 1398.79 | 1894.76 | 2418.37 | 2867.21 | 3184.76 |

**Signal Keywords**

**Keyword: Sensor Name**
Sensor: string followed by a list of sensors.

Example:  

| Item | Details |
| --- | --- |
| signal | SG01 |

**Signal Dependent Keywords**

**Keyword: scopelimit(#) (Optional)**

scopelimit(#): float, (#) = 1 (default) or the parameter entry
followed by the limit defined at each mode for a given signal.

Example:  

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| scopelimit1 | 20 | 10 | 40 | 60 | 35 |

**Keyword: reducedlimit(#) (Optional)**

reducedlimit(#): float, (#) = 1 (default) or the parameter entry.
reducedlimit does not trigger a response in DS.

Example:  

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| reducedlimit1 | 50 | 60 | 35 | 80 |

**Keyword: strainratio(#) (Optional)**

strainratio(#): float, (#) = 1 (default) or parameter entry
followed by the ratio defined at each mode for a given signal.

Example:  

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| strainratio1 | 0.308609 | 0.455828 | 0.157961 | 0.373862 | 0.120844 | 0.263427 |

**Example Scope Limits**

Now that we know the individual keywords, we can now see how they are
integrated together to create a scope limits file. There are several
ways of defining scope limits. All of the examples below would work.

**Example #1: Single Limit Across Many Signals**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| project |  |  |  |  | 1 |
| part | Part 1 |  | 1 |  | 4 |
| freq1 | 2500 |  |  |  |  |
| signal | SG01 |  |  |  |  |
| signal | SG02 |  |  |  |  |
| signal | SG03 |  |  |  |  |
| signal | SG04 |  |  |  |  |
| strainratio1 | 1.0 |  |  |  |  |
| scopelimit1 | 60 |  |  |  |  |
| reducedlimit1 | 40 |  |  |  |  |

**Example #2: Single Limit, Signal Dependent**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| project |  |  |  |  | 1 |
| part | Part 1 |  | 1 |  | 4 |
| modenames | all_modes |  |  |  |  |
| freq1 | 2500 |  |  |  |  |
|  |  |  |  |  |  |
| signal | SG01 |  |  |  |  |
| scopelimit1 | 40 |  |  |  |  |
| strainratio1 | 1.0 |  |  |  |  |
|  |  |  |  |  |  |
| signal | SG02 |  |  |  |  |
| scopelimit1 | 60 |  |  |  |  |
| strainratio1 | 1.0 |  |  |  |  |
|  |  |  |  |  |  |
| signal | SG03 |  |  |  |  |
| scopelimit1 | 30 |  |  |  |  |
| strainratio1 | 1.0 |  |  |  |  |
|  |  |  |  |  |  |
| signal | SG04 |  |  |  |  |
| scopelimit1 | 100 |  |  |  |  |
| strainratio1 | 1.0 |  |  |  |  |

**Example #3: Time & Frequency Domain Limits**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| project |  |  |  |  | 1 |
| part | Part1 |  | 2 |  | 4 |
| modenames | Time | Freq |  |  |  |
| freq1 | 0 | 2500 |  |  |  |
| signal | SG01 |  |  |  |  |
| signal | SG02 |  |  |  |  |
| signal | SG03 |  |  |  |  |
| signal | SG04 |  |  |  |  |
| scopelimit1 | 80 | 60 |  |  |  |
| strainratio1 | 1.0 | 1.0 |  |  |  |

**Example #4: Frequency Dependent Limits, Adjacent Modes**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| project |  |  |  |  | 1 |
| part | Part 1 |  | 4 |  | 4 |
| freq1 | 500 | 1000 | 2000 | 3000 |  |
| modenames | 1F | 1T | 2F | Unk |  |
|  |  |  |  |  |  |
| signal | SG01 |  |  |  |  |
| scopelimit1 | 30 | 40 | 50 | 60 |  |
|  |  |  |  |  |  |
| signal | SG02 |  |  |  |  |
| scopelimit1 | 55 | 44 | 53 | 68 |  |
|  |  |  |  |  |  |
| signal | SG03 |  |  |  |  |
| scopelimit1 | 89 | 100 | 64 | 77 |  |
|  |  |  |  |  |  |
| signal | SG04 |  |  |  |  |
| scopelimit1 | 41 | 93 | 47 | 35 |  |

**Example #4A: Frequency Dependent Limits, Non-adjacent Modes**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| project |  |  |  |  | 1 |
| part | Part 1 |  | 4 |  | 4 |
| ftol | 50 | 100 | 200 | 0 |  |
| freq1 | 500 | 1000 | 2000 | 3000 |  |
| modenames | 1F | 1T | 2F | Unk |  |
|  |  |  |  |  |  |
| signal | SG01 |  |  |  |  |
| scopelimit1 | 30 | 40 | 50 | 60 |  |
|  |  |  |  |  |  |
| signal | SG02 |  |  |  |  |
| scopelimit1 | 55 | 44 | 53 | 68 |  |
|  |  |  |  |  |  |
| signal | SG03 |  |  |  |  |
| scopelimit1 | 89 | 100 | 64 | 77 |  |
|  |  |  |  |  |  |
| signal | SG04 |  |  |  |  |
| scopelimit1 | 41 | 93 | 47 | 35 |  |

**Example #5: Frequency Dependent Limits, Limits Vary with a Parameter**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| project |  |  |  |  | 1 |  |  |
| part | Part 1 |  | 5 | 4 | 5 | N | 0 |
| modenames | Time | 1F | 1T | 2F | Unk |  |  |
| param1 | 600 | 600 | 600 | 600 | 600 |  |  |
| freq1 | 0 | 300 | 800 | 1500 | 2000 |  |  |
| param2 | 1200 | 1200 | 1200 | 1200 | 1200 |  |  |
| freq2 | 0 | 400 | 800 | 1700 | 2200 |  |  |
| param3 | 6000 | 6000 | 6000 | 6000 | 6000 |  |  |
| freq3 | 0 | 500 | 950 | 1900 | 2400 |  |  |
| param4 | 9000 | 9000 | 9000 | 9000 | 9000 |  |  |
| freq4 | 0 | 600 | 1100 | 2000 | 2500 |  |  |
|  |  |  |  |  |  |  |  |
| signal | SG01 |  |  |  |  |  |  |
| scopelimit1 | 90 | 60 | 40 | 50 | 60 |  |  |
| scopelimit2 | 80 | 55 | 35 | 45 | 60 |  |  |
| scopelimit3 | 70 | 50 | 30 | 40 | 60 |  |  |
| scopelimit4 | 60 | 45 | 25 | 35 | 60 |  |  |

Note: Limits are extrapolated! "Fix" by defining maximum speed point.

**Example #5a: Alternate Definition**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| project |  |  |  |  | 1 |  |  |
| part | Part 1 |  | 5 | 4 | 5 | N | 0 |
| modenames | Time | 1F | 1T | 2F | Unk |  |  |
|  |  |  |  |  |  |  |  |
| param1 | 600 | 600 | 600 | 600 | 600 |  |  |
| param2 | 1200 | 1200 | 1200 | 1200 | 1200 |  |  |
| param3 | 6000 | 6000 | 6000 | 6000 | 6000 |  |  |
| param4 | 9000 | 9000 | 9000 | 9000 | 9000 |  |  |
|  |  |  |  |  |  |  |  |
| freq1 | 0 | 300 | 800 | 1500 | 2000 |  |  |
| freq2 | 0 | 400 | 800 | 1700 | 2200 |  |  |
| freq3 | 0 | 500 | 950 | 1900 | 2400 |  |  |
| freq4 | 0 | 600 | 1100 | 2000 | 2500 |  |  |
|  |  |  |  |  |  |  |  |
| signal | SG01 |  |  |  |  |  |  |
| scopelimit1 | 90 | 60 | 40 | 50 | 60 |  |  |
| scopelimit2 | 80 | 55 | 35 | 45 | 60 |  |  |
| scopelimit3 | 70 | 50 | 30 | 40 | 60 |  |  |
| scopelimit4 | 60 | 45 | 25 | 35 | 60 |  |  |

The 'signal' lines designate the APEX DS signals to which the
following mode and limit definitions apply. They are matched up by
name. It is not an error for a scope limit file to have mode
definitions for a non acquired signal. It is also not a requirement
that it contains mode definitions for all measured signals. The line
should also specify the number of modes defined in the following
table.

The following five lines (freq(#), freqmin(#), freqmax(#), param(#),
scopelimit(#)) can be given once or repeated multiple times. If given
multiple times with different parameter values, they can be used to
implement parameter (i.e. speed) dependent mode frequencies and
limits. APEX DS will interpolate between parameter points using the
actual value of the parameter. The parameter used for the
interpolation is the default parameter assigned to the channel in the
APEX DS setup.

If a 'mode' with all three frequencies (freq(#), freqmin(#), and freqmax(#))
equal to zero is present then the limit value for that mode is used as
a limit for the time domain peak to peak signal value.

If an APEX DS channel has modes associated with it via the scope limit
file, the following additional features are available in APEX DS:

- Spectrum plots show the limits
- Campbell plots have display modes which show the mode and limit data
- History records (by expanding signals in the selector box) are
  available for mode amplitudes and limit ratios.
- Mode over limit events are logged in a file in the log directory set
  up on the Setup Panel.
