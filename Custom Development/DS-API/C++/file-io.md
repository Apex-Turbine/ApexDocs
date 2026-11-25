# DS-API C / C++ File I/O

> [!IMPORTANT]
> **End-User Format License Notice:** Reading or writing APEX data files (`.rwx`, `.pkx`, `.datx`, etc.) via `DSAPI_file_*` does not consume live network seats, but all APEX file formats, schemas, and `DS-API` libraries are licensed strictly for **internal end-user use** and cannot be used for commercial means unless explicitly authorized by APEX through formal written agreement ([Software License Agreement](../../../Release%20Policies/software-license-agreement.md)).

Use the `DSAPI_file_*` functions to inspect, read, seek, create, and write DS/EDAS data recordings. Calling `DSAPI_file_*` operates strictly on local or network-mounted files and **does not require a DS-API network license**.

## Supported File Formats

| Extension / Pattern | Internal Handler | Read | Write (`DSAPI_file_create_*`) | Notes |
| --- | --- | --- | --- | --- |
| `.rwx`, `.rwz` | `FileDspEdas` | Yes | Yes (`DSAPI_file_create_raw`) | Extended DS raw/time data with optional compression |
| `.pkx` | `FileDspEdas` | Yes | Yes (`DSAPI_file_create_peak`) | Extended DS peak, stats, and speed trigger archive |
| `.raw`, `.pks` | `FileDspEdasLegacy` | Yes | No | Legacy EDAS raw and peak recordings |
| `.datx`, `.datx_index*`, `.datx_[0-9]*` | `FileDspCustomDatx*` | Yes | Yes (`DSAPI_file_create_datx`) | High-speed indexed block format |
| `.cats_index`, `*.[Cc][0-9]*` | `FileDspCustomCats*` | Yes | No | CATS multi-file archive reader |

## Opening, Inspecting, Seeking, and Reading

### File API Summary (`dsapi.h`)

| Function | Purpose |
| --- | --- |
| `DSAPI_file_open(filename, &errors)` | Open any supported DS/EDAS/DATX/CATS file for reading (`NULL` on failure) |
| `DSAPI_file_setup(file)` | Return `const DspSetup *` describing channels, sample rate, params, resources |
| `DSAPI_file_datapoint(file)` | Return `const FileDataPoint *` metadata stored in the recording header |
| `DSAPI_file_starttime(file, &tzone)` | Start timestamp in **microseconds since Unix epoch**, plus timezone offset output |
| `DSAPI_file_startblock(file)` | First block index present in the file |
| `DSAPI_file_numblocks(file)` | Total number of acquisition blocks in the file |
| `DSAPI_file_position(file)` | Current 0-based read cursor block position |
| `DSAPI_file_seek(file, block)` | Jump directly to a specific block offset |
| `DSAPI_file_rewind(file)` | Reset read cursor back to the beginning of the recording |
| `DSAPI_file_uncompress(file, enable)` | Enable or disable automatic decompression of `Z*` packets during `DSAPI_file_read` |
| `DSAPI_file_read(file, &result, &errors)` | Read next `const DspBlockData *` (`NULL` at EOF or error; inspect `result` and `errors`) |
| `DSAPI_file_close(file)` | Close handle and release file buffers |

## Creating and Writing Files (`.rwx`, `.pkx`, `.datx`)

Three creation entry points let C/C++ applications author DS-compatible recordings using a constructed `DspSetup` and `FileDataPoint`:

- `DSAPI_file_create_raw(...)` — Creates an extended `.rwx` raw file
- `DSAPI_file_create_peak(...)` — Creates a `.pkx` peak/statistics archive
- `DSAPI_file_create_datx(...)` — Creates an indexed `.datx` file
- `DSAPI_file_write(...)` — Writes `DspBlockData` blocks sequentially to an open writable handle
- `DSAPI_file_close(file)` — Flushes file headers/indices and closes the output file

## Annotated Example (`examples/showfile.c`)

The canonical `showfile` utility opens an existing DS recording, optionally toggles decompression, prints metadata, and walks every `DspBlockData` block to count or dump packets:

```c
#include <stdio.h>
#include "dsapi.h"

int main(int argc, char *argv[]) {
  UtilString errors;
  DSAPI_file file;

  if (argc < 2) {
    fprintf(stderr, "Usage: showfile <datafile>\n");
    return 1;
  }

  DSAPI_string_init(&errors);
  file = DSAPI_file_open(argv[1], &errors);
  if (!file) {
    fprintf(stderr, "Open failed: %s\n", errors);
    DSAPI_string_dispose(&errors);
    return 1;
  }

  /* Ensure compressed blocks (ZRAW/ZTIME/ZFFT/ZMAG) decode automatically */
  DSAPI_file_uncompress(file, true);

  const DspSetup *setup = DSAPI_file_setup(file);
  int tzone = 0;
  int64_t start_us = DSAPI_file_starttime(file, &tzone);
  printf("Sample rate: %.2f Hz, BlockSize: %u, Blocks: %lld, Start(us): %lld\n",
         setup->sampleFrequency,
         (1 << setup->blockSizeLog2),
         (long long)DSAPI_file_numblocks(file),
         (long long)start_us);

  const DspBlockData *block;
  int result = 0;
  while ((block = DSAPI_file_read(file, &result, &errors)) != NULL) {
    if (block->param) {
      /* Inspect block->param parameter packet */
    }
    for (index_t ch = 0; ch < block->channels; ch++) {
      if (block->channel[ch].raw)  { /* Unscaled ADC data */ }
      if (block->channel[ch].time) { /* Calibrated EU time data */ }
      if (block->channel[ch].mag)  { /* Magnitude + envelope */ }
      if (block->channel[ch].fft)  { /* Complex spectrum */ }
      if (block->channel[ch].peak) { /* Stats/peaks or tach triggers */ }
    }
  }

  DSAPI_file_close(file);
  DSAPI_string_dispose(&errors);
  return 0;
}
```

For random access, call `DSAPI_file_seek(file, DSAPI_file_startblock(file) + offset)` between reads, or `DSAPI_file_rewind(file)` to restart iteration from block zero.
