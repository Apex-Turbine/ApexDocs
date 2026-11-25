# DS-API C / C++ Data Types

DS-API organizes acquisition metadata, network state, and time/frequency blocks around opaque session handles (`DSAPI_session`, `DSAPI_file`) and core container/DSP structures shared across offline files and live TCP streams.

## Opaque Handles & Containers

| Type | Kind | Description |
| --- | --- | --- |
| `DSAPI_session` | `struct DSAPI_session_handle*` | Network session handle created by `DSAPI_net_startup` |
| `DSAPI_file` | `struct DSAPI_file_handle*` | Open file reader or writer handle from `DSAPI_file_open` / `DSAPI_file_create_*` |
| `UtilString` | Core string type | Error output and string fields (`DSAPI_string_init`/`_dispose` in C, RAII in C++) |
| `UtilArray` | Core dynamic array | Typed container backing setup lists, packets, and channel collections |
| `FileDataPoint` | Test metadata struct | Datapoint / test metadata descriptor passed to files and monitor/record starts |
| `DspNetHost` | Host descriptor | Discovered or connected DS server metadata returned by `DSAPI_net_discover*` / `DSAPI_net_hosts` |
| `DspNetReply` | Async reply descriptor | Host response & recording status from `DSAPI_net_reply_record_state` |

## Setup Hierarchy: `DspSetup`, `DspChannel`, `DspParam`, `DspStat`

A `DspSetup` describes the global sample rate, FFT/processing block size, and channel/parameter/resource tables (from a file header via `DSAPI_file_setup` or from a live host via `DSAPI_net_peer_setup`).

Key `DspSetup` members (demonstrated in `samples/showsetup.c`):
- `sampleFrequency` — Base acquisition rate in Hz
- `blockSizeLog2` — Block size exponent; samples per block = `1 << s->blockSizeLog2`
- `channels` — Array of `DspSetupChannel*` (`DspChannel`) descriptors (`channels.size`, `channels.at[i]`)
- `params` — Array of `DspSetupParam*` (`DspParam`) parameter descriptors (`params.size`, `params.at[i]`)
- `resources` — Array of hardware resource descriptors (`resources.size`)

Inspecting channel and parameter definitions (`samples/showsetup.c`):

```c
void showsetup(const DspSetup *s) {
  printf("Setup info: rate = %.2fHz, blocksize = %u, ",
         s->sampleFrequency, (1 << s->blockSizeLog2));
  printf("channels = %u, params = %u, resources = %u\n",
         s->channels.size, s->params.size, s->resources.size);

  for (index_t i = 0; i < s->channels.size; i++) {
    const DspSetupChannel *c = s->channels.at[i];
    printf("  channel[%u] = { '%s', %d, %d, '%s', %.4f, %.4f, %.4f, %.4f }\n",
           i, c->name, c->type, c->sampleRatioLog2, c->unitName,
           c->minRange, c->maxRange, c->combinedEuA, c->combinedEuB);
  }

  for (index_t i = 0; i < s->params.size; i++) {
    const DspSetupParam *p = s->params.at[i];
    printf("  param[%u] = { '%s', %d, '%s', %.4f, %.4f, %d }\n",
           i, p->name, p->type, p->unitName,
           p->minValue, p->maxValue, p->channelIndex);
  }
}
```

Use `DSAPI_setup_stats(setup, chan, nstats)` (and `DspStat` definitions) to query configured DSP statistics on a given channel, and `DSAPI_setup_size(setup, &nc, &np, &nr)` to retrieve counts cleanly.

## Data Blocks & Packets: `DspBlock` and `DspPacket`

Each acquisition block returned by `DSAPI_file_read` or `DSAPI_net_read` is delivered as a `const DspBlockData *` (`DspBlock`), containing per-channel pointers/accessors to individual `DspPacketData *` (`DspPacket`) payloads:

| Stream / Payload | C Struct Access (`DspBlockData`) | C++ Method Access (`DspBlockData`) | Contents |
| --- | --- | --- | --- |
| Raw ADC (`raw16i`, `raw32i`, `raw32f`) | `data->channel[ch].raw` | `data->raw(ch)` | Unscaled 16-bit/32-bit integer or 32-bit float samples |
| Scaled Time (`time`) | `data->channel[ch].time` | `data->time(ch)` | Calibrated engineering-unit (`EU`) time samples |
| Complex FFT (`fft`) | `data->channel[ch].fft` | `data->fft(ch)` | Complex spectrum frames |
| Magnitude & Envelope (`mag`, `env`) | `data->channel[ch].mag` | `data->mag(ch)` | Paired magnitude (`mag.data[0..n-1]`) & envelope (`mag.data[n..2n-1]`) arrays |
| Peak, Stats & Speed Triggers (`peak`, `stat`, `trigger`) | `data->channel[ch].peak` | `data->peak(ch)` | Speed/tach trigger positions OR scalar stats + frequency peak triplets |
| Parameters (`param`) | `data->param` | `data->param()` | Scalar parameter vector for the block |

### Packet Type Constants (`DspPacket.h` / `DspPacket.hpp`)

Low-level packet headers identify the binary payload encoding:

| Constant | Category | Notes |
| --- | --- | --- |
| `DSP_PACKET_RAW_PI32` (`0xbaef`), `DSP_PACKET_RAW_PF32` | Packed raw | Packed 32-bit int / float raw streams |
| `DSP_PACKET_RAW_I32`, `DSP_PACKET_RAW_F32`, `DSP_PACKET_RAW_I16` | Uncompressed raw | 32-bit int, 32-bit float, and 16-bit int ADC streams |
| `DSP_PACKET_TIME` | Time | Calibrated EU time-domain packet |
| `DSP_PACKET_FFT` | FFT | Complex FFT frequency-domain packet |
| `DSP_PACKET_MAG` | Magnitude / Env | Spectral magnitude and envelope packet |
| `DSP_PACKET_PEAK` | Peak / Trigger | Stats + peaks (`DspPacketItemPeak`) or tach triggers (`DSP_PACKET_TRIGGER_BITS = 30`) |
| `DSP_PACKET_PARAM` | Parameter | Block-aligned scalar parameter vector |
| `DSP_PACKET_ZRAW`, `DSP_PACKET_ZTIME`, `DSP_PACKET_ZMAG`, `DSP_PACKET_ZFFT` | Compressed | zlib-compressed counterparts (auto-decompressed when enabled) |
| `DSP_PACKET_RMPEAK`, `DSP_PACKET_RMMAG`, `DSP_PACKET_RMREV` | Rotating machinery | Order/revolution/tachometer-tracked spectra & peaks |

### Inspecting Packet Payloads

**Time Packet (`samples/showtime.c`)**:
```c
index_t n = DspPacketTimeBlockSize(p);
printf("Time packet: block=%.0f, channel=%u\n",
       (double)(DspPacketBlock(p)), DspPacketChannel(p));
for (index_t i = 0; i < n; i++) {
  printf("  time[%d] = %.4f\n", i, p->time.data[i]);
}
```

**Magnitude & Envelope Packet (`samples/showmag.c`)**:
`p->mag.data` stores `n` magnitude bins followed immediately by `n` envelope bins:
```c
index_t n = DspPacketMagBlockSize(p);
for (index_t i = 0; i < n; i++) {
  printf("  mag:env[%d] = { %.4f, %.4f }\n",
         i, p->mag.data[i], p->mag.data[i + n]);
}
```

**Peak, Statistics & Speed Trigger Packet (`samples/showpeak.c`)**:
Check `DspPacketPeakIsTrigger(p)` to distinguish speed/tachometer trigger packets from regular signal statistics & spectral peaks:
```c
if (DspPacketPeakIsTrigger(p)) {
  printf("speed=%.4f, triggers=%u\n",
         p->peak.value, DspPacketPeakNumTriggers(p));
  for (index_t i = 0; i < DspPacketPeakNumTriggers(p); i++) {
    /* Fraction of block duration using DSP_PACKET_TRIGGER_BITS (30) */
    double frac = (double)(p->peak.trigger[i]) / (double)(1 << 30);
    printf("  trigger[%u] = %.8f\n", i, frac);
  }
} else {
  for (index_t i = 0; i < DspPacketPeakNumStats(p); i++) {
    printf("  stat[%u] = %.4f\n", i, DspPacketPeakStats(p)[i].f32);
  }
  for (index_t i = 0; i < DspPacketPeakNumPeaks(p); i++) {
    const DspPacketItemPeak *pk = DspPacketPeakPeaks(p) + i;
    printf("  peak[%u] = { mag=%.4f, freq=%.4f, phase=%.2f, %s }\n",
           i, pk->magnitude, pk->frequency, pk->phase,
           DspPacketPeakValid(p, i) ? "good" : "bad");
  }
}
```
