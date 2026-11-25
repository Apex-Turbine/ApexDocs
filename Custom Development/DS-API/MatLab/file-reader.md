# MATLAB Offline File Reader (`mxapi_file_*`)

Read `.rwx`, `.rwz`, `.pkx`, `.raw`, `.pks`, `.datx`, and `.cats_index` recordings directly into native MATLAB matrices using `mxapi`. Offline file access requires **no network license**.

## Core File, Setup, and Data Extraction Functions

> [!NOTE]
> All channel, parameter, resource, and statistic indices passed to `mxapi_setup_*` and data extraction functions are **1-based**.

| Function / Family | Purpose |
| --- | --- |
| `mxapi_version` | Query the loaded `mxapi` library version string |
| `mxapi_file_*` | Open (`uint64` handle on success, `char` error string on failure), inspect metadata/block range, seek/rewind, decompress, read blocks, and close files |
| `mxapi_setup_info` | Query global sample frequency, block size, and channel/parameter/resource counts |
| `mxapi_setup_channel` | Query 1-based channel metadata (name, units, ranges, downsampling ratio, EU scale) |
| `mxapi_setup_param` | Query 1-based scalar parameter metadata (name, units, range, source channel) |
| `mxapi_setup_resource` | Query 1-based hardware resource descriptors |
| `mxapi_setup_stat_info` | Query configured DSP statistics metadata for a 1-based channel |
| `mxapi_raw_data` | Extract raw unscaled integer/float ADC samples from the active block |
| `mxapi_raw_scaled` | Extract scaled time-domain samples derived from raw ADC data |
| `mxapi_time_data` | Extract calibrated EU time-domain waveform samples |
| `mxapi_mag_data` | Extract spectral magnitude / envelope bins |
| `mxapi_peak_*` | Extract DSP statistics vectors, FFT spectral peaks, and tachometer/speed trigger events |
| `mxapi_param_*` | Extract block-aligned scalar parameter arrays |

## Checking `mxapi_file_open` Return Values

Because `mxapi` returns either a `uint64` handle or an error `char` vector, validate the return type with `isinteger` before proceeding:

```matlab
hfile = calllib('mxapi', 'mxapi_file_open', filepath);
if ~isinteger(hfile)
    error('Failed to open DS recording: %s', hfile);
end
```

## Walkthrough: `examples/matdataviewer.m`

The SDK's `examples/matdataviewer.m` script illustrates the end-to-end offline MATLAB workflow:

1. **Load Library**: Call `loadlibrary` with `mxapi.dll` / `libmxapi.so` and `mxapi.h`, verifying `mxapi_version`.
2. **Open Recording**: Invoke file open (`mxapi_file_*`), verify `isinteger(file)` succeeds, and enable decompression if reading compressed `.rwx` / `.rwz` data.
3. **Inspect Setup**: Query `mxapi_setup_info` to obtain block count, sample rate, and channel/parameter counts, then loop `1..N` using `mxapi_setup_channel`, `mxapi_setup_param`, `mxapi_setup_resource`, and `mxapi_setup_stat_info`.
4. **Iterate Blocks**: Advance block-by-block through the recording, calling:
   - `mxapi_raw_data` / `mxapi_raw_scaled` or `mxapi_time_data` for time waveforms
   - `mxapi_mag_data` for spectrum magnitude/envelope plots
   - `mxapi_peak_*` for block statistics, peak frequency tracking, or tachometer triggers
   - `mxapi_param_*` for auxiliary scalar parameters
5. **Cleanup**: Close the file handle cleanly via `mxapi_file_*` close and unload `mxapi` when the script terminates (`unloadlibrary`).
