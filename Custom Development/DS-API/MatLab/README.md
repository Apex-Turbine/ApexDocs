# DS-API MATLAB Interface

> [!IMPORTANT]
> **End-User License Notice:** `DS-API` MATLAB libraries and APEX file/data formats are licensed strictly for internal end-user use and cannot be used for commercial means without formal written authorization from APEX ([Software License Agreement](../../../Release%20Policies/software-license-agreement.md)). Legacy FLEXlm (`lmgrd`) licensing ends in **October 2027**; see **[APEX License Manager](../../../License%20Manager/README.md)**. (`mxapi`)

Access DS/EDAS recordings, stream live DS 3.x acquisition packets, and control DS servers directly from **64-bit MATLAB** using the `mxapi` C wrapper library (`mxapi.dll` on Windows, `libmxapi.so` / `mxapi.so` on Linux) and `mxapi.h`.

## Prerequisites & Toolchain Setup

- **64-bit MATLAB required**: `mxapi` targets 64-bit MATLAB environments matching DS-API's `lib64/` / `bin/` libraries (`CMakeLists.txt`).
- **Supported C Compiler (`mex -setup C`)**: MATLAB's `loadlibrary` requires a supported C compiler configured in MATLAB in order to parse `mxapi.h`.
- **Shared Library Search Path**: Ensure `mxapi` and its companion core DLLs/`so`s (`dsapi`, `ApexDsp*`, `ApexFile`, `ApexIpc`, `ApexLicenser`, `ApexUtils`, and FlexNet `libfnp64`/`libfnpts64` if legacy licensing is enabled) are on the system `PATH` (Windows) or `LD_LIBRARY_PATH` (Linux) before launching MATLAB.

## Loading and Unloading `mxapi`

Load the library once at startup with `loadlibrary` and clean up with `unloadlibrary` when finished:

```matlab
% Windows example (adjust paths to match your SDK bin/include folders)
if ~libisloaded('mxapi')
    loadlibrary('mxapi.dll', 'mxapi.h');
end

ver = calllib('mxapi', 'mxapi_version');
disp(ver);

% ... perform file I/O or network acquisition ...

if libisloaded('mxapi')
    unloadlibrary('mxapi');
end
```

On Linux, replace `'mxapi.dll'` with `'libmxapi.so'` (or the exact `.so` filename in your SDK `bin/` or `lib64/` directory).

## MATLAB Indexing Convention

> [!IMPORTANT]
> Unlike the C/C++ and Python DS-API interfaces (which use 0-based indexing), **all host, channel, parameter, resource, and statistic indices in `mxapi_*` functions are 1-based** to match standard MATLAB arrays.

## Handle Types and Error Checking Patterns

- **File Open Handle Check (`mxapi_file_*`)**: Opening a file returns an unsigned 64-bit integer handle (`uint64`) on success, or a `char` error message on failure. Check `isinteger(file)` before using the handle.
- **Session vs. Manager Handles (`mxapi_net_*`)**: Live operations use two distinct handle types (`hsession` from `mxapi_net_startup` and `hmanager` from `mxapi_net_manage`). See [Network Streaming & Acquisition Manager](network-streaming-and-manager.md) for an important handle validation detail when invoking monitor/record commands.

## Developer Licensing Rules

- **Offline File Reading (`mxapi_file_*`)**: Does **not** initialize a network session and does **not** check out floating network licenses.
- **Network Streaming & Remote Control (`mxapi_net_startup`)**: Initializes `DSAPI_session_handle` under application `DSAPI`, checking out `APEXAPI_NET_STREAM`, `APEXAPI_NET_RECORD`, and `APEXAPI_NET_CONFIG`. See [Developer Licensing Guide](../README.md#developer-licensing-guide).

## Guides

- [Offline File Reader (`matdataviewer.m`)](file-reader.md)
- [Live Network Streaming & Acquisition Manager (`matdataclient.m`)](network-streaming-and-manager.md)
