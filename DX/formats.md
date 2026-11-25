# Data Formats

| Name | Extension | Read | Write |
| --- | --- | --- | --- |
| [APEX Data Acquisition](#apex-data-acquisition) | *.pkx, *.rwx | Yes | Yes |
| [DATX Data Acquisition](#datx-data-acquisition) | *.datx_index,*.datx_* | Yes | Yes |
| [Pacific Instruments](#pacific-instruments) | *.raw | Yes | No |
| [National Instruments](#national-instruments) | *.tdms, *.tdm | Yes | No |
| [MATLAB Binary](#matlab-binary) | *.mat | Yes | Yes |
| [Universal File Format](#universal-file-format) | *.uff, *.unv, *.bin | Yes | Yes |
| [Sony Data Acquisition](#sony-data-acquisition) | *.BIN | Yes | No |
| [TEAC Data Acquisition](#teac-data-acquisition) | *.DAT | Yes | No |
| [ATFX Data Format](#atfx-data-format) | *.atfx | Yes | No |
| [CDF Data Format](#cdf-data-format) | *.cdf | Yes | No |
| [APEX RAW CSV Format](#apex-raw-csv-format) | *.csv | Yes | No |
| [Simple CSV Format](#simple-csv-format) | *.csv | Yes | No |
| [Dewesoft Format](#dewesoft-data-acquisition) | *.d7d, *.dxd | Yes | No |
| [DEWETRON Format](#dewetron-dmd-format) | *.dmd | Yes | No |
| [HDF5 Format](#hierarchical-data-format-5) | *.h5 | Yes | No |

| APEX CSV Export Formats |
| --- |
| Time |
| Time w/ Parameters |
| Parameters |
| Spectrum CSV |
| Spectrum Envelope |
| Spectrum Average |
| Extended Envelope |
| Peaks |
| Order Peaks |

## APEX Data Acquisition

**Peak Domain (*.pkx, *.pks)**

Time domain data may or may not be available. If time domain data is available it is on a decimated basis. PKX files support channel dependent sample rates.

**Time Domain (*.rwx, *.raw)**

RWX files support channel dependent sample rates

## DATX Data Acquisition

**CATS (*.cats_index, *.c*) Time Domain**

All associated individual channel files are supported directly through the index file. Individual channel files are also supported by selecting the channel file(s) desired.

**DATX (*.datx_index, *.datx_*) Time Domain**

All associated A/D brick files are supported directly through the index file. Individual A/D brick files are also supported by selecting the A/D brick file(s) desired.

Channels in CATS/DATX files are assigned the following processing options by default:

> 1. Channels that have a valid tach ratio are interpreted as a rotational velocity and are processed as parameters.
> 2. All signals are AC coupled.
> 3. Signals are processed with a Base Block Rate of 2048.
> 4. Signals are processed with the Blackman-Harris FFT window.

> [!NOTE]
> All information from a datx file is extracted from the binary datx files not the datx_index

<table>
  <tbody>
    <tr>
      <td colspan="3">DATX Keyword Mappings to APEX Datapoint Information</td>
    </tr>
    <tr>
      <td>DATX Keyword(s)</td>
      <td>DATX Example</td>
      <td>Apex Setting</td>
    </tr>
    <tr>
      <td>channel_#</td>
      <td>channel_#=1</td>
      <td>Channel #</td>
    </tr>
    <tr>
      <td>channel_label</td>
      <td>channel_label=N1</td>
      <td>Signal or Parameter Name</td>
    </tr>
    <tr>
      <td>display_units</td>
      <td>display_units=RPM</td>
      <td>Units</td>
    </tr>
    <tr>
      <td>display_scale_type</td>
      <td>display_scale_type=Peak-Peak</td>
      <td>FFT Scaling</td>
    </tr>
    <tr>
      <td>cal_coeff_1</td>
      <td>cal_coeff_1=0</td>
      <td>EUB (offset)</td>
    </tr>
    <tr>
      <td>cal_coeff_2</td>
      <td>cal_coeff_2=7.8242</td>
      <td>EUA (scalar)</td>
    </tr>
    <tr>
      <td>sample_rate</td>
      <td>sample_rate=65536</td>
      <td>Channel sample rate</td>
    </tr>
    <tr>
      <td>test_date_time</td>
      <td>test_date_time=20-Nov-2015 19:37:49.382</td>
      <td>Start Time</td>
    </tr>
    <tr>
      <td>test_description</td>
      <td>test_description=sample_tes</td>
      <td>Data Point Info, "dplnfo"</td>
    </tr>
    <tr>
      <td>test_id</td>
      <td>test_id=1423</td>
      <td>Data Point Number (if numeric), "dpNumber"</td>
    </tr>
    <tr>
      <td>test_number</td>
      <td>test_number=1423</td>
      <td>Data Point Number (if numeric)</td>
    </tr>
    <tr>
      <td>test_operator</td>
      <td>test_operator=t1166_r02</td>
      <td>Operator Name</td>
    </tr>
    <tr>
      <td>test_location</td>
      <td>test_location=VILLAROCHE</td>
      <td>Test Site</td>
    </tr>
    <tr>
      <td>YYYYMMDD HHMMSS+engine_type</td>
      <td>20141125-171904A</td>
      <td>Test ID, "testld"</td>
    </tr>
    <tr>
      <td>specimen_model</td>
      <td>X848</td>
      <td>Test Article Model, "model"</td>
    </tr>
    <tr>
      <td>specimen_name specimen_build</td>
      <td>SILVERCREST-1A</td>
      <td>Serial Number</td>
    </tr>
    <tr>
      <td>config_description</td>
      <td>APEX 64-CHANNEL SYSTEM</td>
      <td>Test Info, "testInfo"</td>
    </tr>
    <tr>
      <td>part_no/id</td>
      <td>ABC-123</td>
      <td>Test Article, "testArticle"</td>
    </tr>
    <tr>
      <td>specimen_buile</td>
      <td>01</td>
      <td>Build, "build"</td>
    </tr>
  </tbody>
</table>

## Pacific Instruments

**RAW (*.RAW) Time Domain**

## National Instruments

The NI TDMS File Format

**TDM (*.tdms, *.tdm) Time Domain**

> [!NOTE]
> DX does not support multi sample rate tdms files and the 'wf_increment' property is required for processing

## MATLAB Binary

> [!NOTE]
> A installation of the MATLAB runtime is required to use MATLAB files. Visit [https://www.mathworks.com/products/compiler/mcr.html](https://www.mathworks.com/products/compiler/mcr.html) to download. R2015b 9.0 64bit is the recommended version and has been tested on Windows and Linux. Other versions may or may not work.

> [!NOTE]
> Multiple sample rates are supported however they must be power of two multiple of each other.

**MAT (*.mat) Time Domain**

Binary MATLAB files are supported, however, the format defined below is required. MAT signal files are not required to have all channels sampled at the same rate.

> [!NOTE]
> For MATLAB files to be supported you must provide the MATLAB dlls, DX will look for the dlls in the default locations and if they are available load them.

Each channel must be defined within a structure with the name "Signal". The size of the structure is equal to the number of channels., i.e., Signal(1), Signal(2), ..., Signal(n) where n is the number of signals. The SampleRate and Data fields are required, all other fields are optional.

The fields defined below are imported, however, additional fields are permitted to be defined in the Signal structure.

.SampleRate (required)

> - Property:  Sample rate
> - Format:  Integer
> - Default:  N/A
> - Notes:  none

.Data  (required)

> - Purpose:  Data vector
> - Format:  Double, int16, int32
> - Default:  N/A
> - Notes:  EUA & EUB (if applicable) are applied to convert to engineering units

.BlockSize (optional)

> - Purpose:  Set the base block size
> - Format:  Integer
> - Default:  1024
> - Notes:  Must be a power of 2 and only read from first signal in file, field is ignored for all subsequent signals.

.Name (optional)

> - Purpose:  Channel name
> - Format:  Character
> - Default:  ChannnelXXX where XXX represents a 3 digit integer automatically sequenced
> - Notes:   none

.Type (optional)

> - Purpose:  Channel type: AC or DC
> - Format:  Character.
> - Default:  DC
> - Notes:  none

.EUA (optional)

> - Purpose:  Coefficient for converting the channel from voltage to engineering units
> - Format:  Double
> - Default:  1.0
> - Notes:  none

.EUB (optional)

> - Purpose:  Channel offset for converting from voltage to engineering units.
> - Format:  Float
> - Default:  0.0
> - Notes:  Only applicable for channels of type "DC"

.Range (optional)

> - Purpose:  Response range of the channel in engineering units
> - Format:  Double
> - Default:  Set individually for each channel
> - Notes:  none

.Threshold (optional)

> - Purpose:  Threshold for peak extraction in engineering units
> - Format:  Double
> - Default:  0.0
> - Notes:  none

.FFTwindow (optional)

> - Purpose:  FFT window
> - Format:  Character
> - Default:  BlackmanHarris
> - Notes:  Rectangular, FlatTop, Hanning, Hamming, Rectangular, BlackmanHarris are valid entries and are not case sensitive

.FFTscaling (optional)

> - Purpose:  Scaling for reporting of peak values
> - Format:  Character
> - Default:  Pk2Pk
> - Notes:  Pk2Pk, Pk and RMS are valid entries and are not case sensitive

.Label  (optional)

> - Purpose:  Label for plotting
> - Format:  Character
> - Default:  Volts
> - Notes:  This is typically the units, i.e., volts, psi, ksi, gs, etc.

The following MATLAB code generates a valid structure for import within DX:

```
Signal(1).BlockSize = 2048;

Signal(1).SampleRate = 8192;
Signal(2).SampleRate = 8192;
Signal(3).SampleRate = 8192;
%
Signal(1).Name = 'Channel000';
Signal(2).Name = 'Signal 2';
Signal(3).Name = 'Signal 3';
%
Signal(1).Type = 'DC';
Signal(2).Type = 'AC';
Signal(3).Type = 'DC';
%
Signal(1).EUA = 1.0;
Signal(2).EUA = 10.0;
Signal(3).EUA = 100.0;
%
Signal(1).EUB = 6;
Signal(2).EUB = 0;
Signal(3).EUB = 0;
%
Signal(1).Range = 10;
Signal(2).Range = 12;
Signal(3).Range = 7;
%
Signal(1).Threshold = 0;
Signal(2).Threshold = 0;
Signal(3).Threshold = 0;
%
Signal(1).FFTwindow = 'BlackmanHarris';
Signal(2).FFTwindow = 'FlatTop';
Signal(3).FFTwindow = 'Rectangular';
%
Signal(1).FFTscaling = 'Pk2Pk';
Signal(2).FFTscaling = 'Pk';
Signal(3).FFTscaling = 'RMS';
%
Signal(1).Label = 'Volts';
Signal(2).Label = 'MicroStrain';
Signal(3).Label = 'MPa';
%
Signal(1).Data = data(:,1);
Signal(2).Data = data(:,2);
Signal(3).Data = data(:,3);
```

## Universal File Format

**UFF (*.uff, *.unv, *.bin)**

Only files of type 58 and 58b.

> [!NOTE]
> DX does not support multi sample rate UFF files, or files with complex numbers.

## Sony Data Acquisition

**Binary (*.BIN) Time Domain**

## TEAC Data Acquisition

**Binary (*.DAT) Time Domain**

## CDF Data Format

**Binary (*.cdf) Common Data Format**

## ATFX Data Format

**ASAM Transport Format in XML (*.atfx)**

## APEX RAW CSV Format

**APEX Raw CSV Format (*.csv)**

> [!NOTE]
> The example csv and those exported by DX contain the columns IRIG, Time and Block. These are created as a convenience for the exported CSV. Upon re-import these columns are not used in any way to determine the time stamp or time delta between samples. The initial time is set by the Test Date field and the subsequent samples are calculated based on the Sample Frequency and number of samples.

> [!NOTE]
> Additional text (comments or related) can be appended to a keyword line so long as the Data Type is not a List (csv), Option List excluded.

The Raw CSV format defines the file meta data at the begining of the file using keyword value pairs. This section (the header) is indicated by the '#' character. It is expected that there exists a contiguous set of lines that begin with the '#' character. After the last '#' it is expected that the comma seperated values to start. The keyword value pairs are not read in a specific order and can occur in any order in the header. Any lines starting with the '#' character that do not match a keyword as specified will be ignored.

| Keyword | Data Type | Example | Note |
| --- | --- | --- | --- |
| Version | Float | 1.0 | Must be 1.0 |
| Test ID | String | T10001 |  |
| Test Date | Custom | 02-Feb-2014 15:15:15.125 | sscanf(string, "%2d-%3c-%4d %2d:%2d:%lf", &day, mon, &year, &hour, &mins, &secs); |
| Datapoint | Integer | 1000 |  |
| Datapoint Info | String | My test point |  |
| Article Model | String | XF10191 |  |
| Serial Number | String | 0010571A |  |
| Stand | String | TS011 |  |
| Operator | String | Joe |  |
| Sample Frequency | Float | 10240 | This determines absolute time of sample when combined with Test Date (See Note) |
| Block Size | Integer | 1024 | Must be a power of 2 and only read from first signal in file, field is ignored for all subsequent signals. |
| Data Start Column | Integer | 4 | Count starts at 1 not 0 |
| Num Blocks | Integer | 899 | Determines how many samples are read when combined with Block Size |
| Parameter Count | Integer | 2 | Number of parameters defined, these must begin a the Data Start Column |
| Parameter Names | String List | P0001,P0002 | List must match Parameter count length |
| Parameter Units | String List | PSI,PSI | List must match Parameter count length |
| Parameter Range | Int List | 0-100,0-1000 | List must match Parameter count length, sscanf(string, "%d-%d", &min, &max) |
| Channel Count | Integer | 2 | Number of channels (signals) defined, these must begin after the parameters. |
| Channel Names | String List | CH0,CH1 | List must match Channel count length |
| Channel Units | String List | g,g | List must match Channel count length |
| Channel EUA | Float List | 1.0,1.0 | List must match Channel count length |
| Channel EUB | Float List | 0.0,0.0 | List must match Channel count length |
| Channel Mode | String Option List | Counts, Counts | Must be either "Volts" or "Counts" |
| Channel Scaling | String Option List | Single Peak,Single Peak | Must be either "Single Peak" or "P2P" or "RMS" |
| Channel Range | Float List | 10,10 | List must match Channel count length, range will be set to +- value specified |
| Channel Type | String Option List | DC,DC | List must match Channel count length, must be "AC" or "DC" |
| Channel Window | String Option List | flattop, flattop | List must match Channel count length, must be "flattop" or "rectangular" or "gaussian" or "hamming" or "blackman harris" |

** EXAMPLE **

```
# APEX CSV Format
#   Version, 1.0
# Datapoint info:
#   Test ID,"Test Data"
#   Test Date,"02-Feb-2014 15:15:15.125"
#   Datapoint,"000001A"
#   Datapoint Info,"Ambient P2"
#   Article Model,""
#   Serial Number,""
#   Stand,""
#   Operator,"joeuser"
# File Info
#   Sample Frequency,20480.00
#   Block Size,2048
#   Num Blocks,1200
#   Data Column Start,4 // CSV column where the first parameter or channel data begins
# Parameter info:
#   Parameter Count,2
#   Parameter Names,"N","P2A"
#   Parameter Units,RPM,PSI
#   Parameter Range,0-15000,10-20
# Channel info:
#   Channel Count,8
#   Channel Names,"SG01A","SG01B","SG05C","SG05D","SG10A","SG10B","SG15C","SG15D"
#   Channel Units,KSI,KSI,KSI,KSI,KSI,KSI,KSI,KSI
#   Channel EU Mode,Counts,Counts,Counts,Counts,Counts,Counts,Counts,Counts // Options Counts or Volts
#   Channel Type,DC,DC,DC,DC,DC,DC,DC,DC // AC
#   Channel EUA,1,1,1,1,1,1,1,1
#   Channel EUB,0,0,0,0,0,0,0,0
#   Channel Window,BlackmanHarris,BlackmanHarris,BlackmanHarris,BlackmanHarris,BlackmanHarris,BlackmanHarris,BlackmanHarris,BlackmanHarris // Rectangular, FlatTop, Hanning, Hamming, Rectangular, BlackmanHarris
#   Channel Range,200,200,200,200,200,200,200,200
#   Channel Scaling,Single Peak,Single Peak,Single Peak,Single Peak,Single Peak,Single Peak,Single Peak,Single Peak // Options 'Single Peak', 'P2P', 'RMS'

#IRIG, Time, Block,N (RPM),P2A (PSI),SG01A (KSI),SG01B (KSI),SG05C (KSI),SG05D (KSI),SG10A (KSI),SG10B (KSI),SG15C (KSI),SG15D (KSI)

2014:059:15:12:36.000000, 0.000000, 0, 1513.300537,15.000000,-2.294922,-0.903320,-1.098633,-2.087402,-2.227783,-0.915527,-1.177979,-2.099609,
2014:059:15:12:36.000048, 0.000049, 0, 1513.300537,15.000000,-2.075195,-0.738525,-0.891113,-1.647949,-2.008057,-0.744629,-0.952148,-1.647949,
2014:059:15:12:36.000097, 0.000098, 0, 1513.300537,15.000000,-1.770020,-0.500488,-0.585938,-1.013184,-1.702881,-0.506592,-0.622559,-0.988770,

...
```

## Simple CSV Format

**Simple CSV Format (*.csv)**

A simplified CSV reader, first line is the header which the first column must be "Time" followed by channel names.

Example

```
Time,Chan1,Chan2,Chan3
0.0,0,0.112842,0.174073
0.15,0.0212,0.090273,0.108795
0.30,0.0212,0.067705,0.043518
0.45,-0.042401,0.157979,0.065277
```

## APEX CSV Export Formats

1. Time CSV - outputs signal data in CSV format at each time sample.
2. Time w/ Parameters CSV file - outputs signal and parameter data in CSV format. Parameters are processed block-by-block, therefore all parameters are constant over a block.
3. Spectrum CSV - Outputs the spectrum for all magnitudes above the threshold for each block. Spectra are are at the lines of resolution and not parabolically interpolated.
4. Spectrum Envelope CSV - Single spectra for the entire data point. Spectra are are at the lines of resolution and not parabolically interpolated.
5. Spectrum Average CSV
6. Extended Envelope CSV - Same as Spectrum Envelope with the additional information:  Time at which peak occurs, Time domain Pk-to-Pk value for the block at which the peak occurs, Time domain Mxi (Max Instantaneous, if available) peak value for the block at which the peak occurs, Time domain RMS peak value for the block at which the peak occurs.
7. Parameters CSV - Parameters only
8. Peaks CSV - Parabolically interpolated peaks.

## Dewesoft Data Acquisition

**d7d (*.d7d) Time Domain**
**dxd (*.dxd) Time Domain**

## DEWETRON DMD Format

**dmd (*.dmd) Time Domain**

DEWETRON OXYGEN DMD data format

| Data Types | Supported |
| --- | --- |
| DMDReader_SAMPLETYPE_DOUBLE | Yes |
| DMDReader_SAMPLETYPE_REDUCED | No |
| DMDReader_SAMPLETYPE_SINT32 | No |
| DMDReader_SAMPLETYPE_DOUBLE_VECTOR | No |
| DMDReader_SAMPLETYPE_COMPLEX_VECTOR | No |

> [!NOTE]
> Windows Only

## Hierarchical Data Format 5

**HDF5 (*.h5) Time Domain**

File Metadata:

["multi" indicates auto conversion of H5T_INTEGER", H5T_FLOAT or H5T_STRING]

| Field | HDF5 Type | Usage in APEX Setup | Notes |
| --- | --- | --- | --- |
| DELTA_SEC | H5T_INTEGER | Sets sample rate |  |
| ACQUISITION_DATE | H5T_INTEGER | Sets year month day | %4d%2d%2d, &year, &month, &day |
| ACQUISITION_TIME | H5T_INTEGER | Sets hour minute second | %2d%2d%2d, &hour, &minute, &second |
| TEST_ARTICLE | multi | Sets File Data Point "Engine" |  |
| TEST_ARTICLE_SN | multi | Sets File Data Point "Engine Info" |  |
| TEST_CELL | multi | Sets File Data Point "Test Cell" |  |
| TEST_CENTER | multi | Sets File Data Point "Test Facility" |  |
| TEST_NUM | multi | Sets File Data Point "DP Number" |  |

Channel Metadata:

| UNITS | H5T_STRING | Sets Unit Name |
| --- | --- | --- |
| MAX | H5T_STRING | Sets Max Range |
| MIN | H5T_STRING | Sets Min Range |

Channel Data Types:

| HDF5 Type | Byte order |
| --- | --- |
| H5T_FLOAT | H5T_ORDER_LE |
| H5T_FLOAT | H5T_ORDER_BE |
| H5T_INTEGER | H5T_ORDER_LE |
| H5T_INTEGER | H5T_ORDER_BE |
