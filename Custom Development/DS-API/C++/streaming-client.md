# DS-API C / C++ Streaming Client

Connect to live **APEX DS (DS 3.x)** servers to discover hosts on the subnet, inspect active setups, subscribe to real-time packet streams, and integrate with DS GUI views.

> [!NOTE]
> Calling `DSAPI_net_startup` initializes the licensed network session under app `DSAPI` (`APEXAPI_NET_STREAM`, `APEXAPI_NET_RECORD`, `APEXAPI_NET_CONFIG`). See [Developer Licensing Guide](../README.md#developer-licensing-guide) for FlexNet and ApexLM license configuration details.

## Session Startup, Discovery, and Shutdown

| Function | Description |
| --- | --- |
| `DSAPI_net_startup(dfifo, efifo)` | Initialize network runtime & licensing; sets data FIFO and event FIFO depths (typical default: `16`, `16`) |
| `DSAPI_net_discover(...)` | Broadcast UDP discovery for online DS 3.x hosts |
| `DSAPI_net_discover_tout(..., toutms)` | UDP discovery with explicit timeout in milliseconds |
| `DSAPI_net_hosts(...)` | Retrieve `DspNetHost` table of discovered or configured servers |
| `DSAPI_net_debug(...)` | Toggle verbose SDK network trace logging |
| `DSAPI_net_shutdown(net)` | Disconnect peers, release license handles, and tear down networking |

DS servers listen starting at `NET_DSP_BASE_PORT = 10995` across `NET_DSP_MAX_PORTS = 10` consecutive ports.

## Connecting and Inspecting Peer State

| Function | Description |
| --- | --- |
| `DSAPI_net_connect(net, host, prio, pass)` | Connect as client to `host` with priority `prio` and optional password `pass` (`NET_ERR_SUCCESS = 0`) |
| `DSAPI_net_disconnect(net, id)` | Close client connection to host `id` |
| `DSAPI_net_is_connected(net, id)` | Returns whether connection `id` is active |
| `DSAPI_net_peer_setup(net, id)` | Retrieve live `const DspSetup *` from connected DS server `id` |
| `DSAPI_net_peer_state(net, id)` | Query remote node state (`NET_DSP_STATE_IDLE=60`, `RUNNING=61`, `FAILED=62`, `STOPPED=63`) |
| `DSAPI_net_state(net)` | Query overall local network session state |

## Subscribing to Packets and Reading Live Data

Once connected, enable the desired packet streams per host and channel, then poll or attach a push callback:

| Function | Purpose |
| --- | --- |
| `DSAPI_net_subscribe(net, id, ...)` | Enable/disable streaming subscription for host `id` |
| `DSAPI_net_packets(net, id, chan, types)` | Select packet types using type characters `'R'` (Raw), `'T'` (Time), `'M'` (Mag), `'P'` (Peak/Param) |
| `DSAPI_net_uncompress(net, enable)` | Auto-decompress incoming compressed packets (`ZRAW`, `ZTIME`, `ZMAG`, `ZFFT`) |
| `DSAPI_net_poll(net, ...)` | Poll socket events & service network I/O loop |
| `DSAPI_net_waiting(net)` | Return count of queued data blocks awaiting `DSAPI_net_read` |
| `DSAPI_net_read(net, ...)` | Dequeue next live `DspBlockData *` packet group |
| `DSAPI_net_event(net, ...)` | Dequeue server status/recording event notification |
| `DSAPI_net_callback(net, fn, ap)` | Register callback function invoked on incoming data/events |
| `DSAPI_net_missed_blocks(net, id)` | Count blocks dropped due to client FIFO overflow (`dfifo`) |
| `DSAPI_net_missed_events(net, id)` | Count events dropped due to event FIFO overflow (`efifo`) |

### Discovery & Streaming Workflow (`examples/discover.cxx`)

A typical C++ client follows the structure illustrated in `discover.cxx`:

```cpp
#include "dsapi.h"

void run_client() {
  /* 1. Startup with 16-block data FIFO and 16-entry event FIFO */
  DSAPI_session net = DSAPI_net_startup(16, 16);
  if (!net) return;

  /* 2. Discover DS servers on the subnet */
  DSAPI_net_discover_tout(net, 1000);
  const DspNetHost *hosts = /* inspect DSAPI_net_hosts(...) */;

  /* 3. Connect to target host, enable decompression, subscribe to T/M/P */
  /* DSAPI_net_connect(net, host, prio, pass) == NET_ERR_SUCCESS */
  DSAPI_net_uncompress(net, true);
  /* DSAPI_net_packets(net, id, chan, "TMP"); */
  /* DSAPI_net_subscribe(net, id, ...); */

  /* 4. Poll and drain blocks via DSAPI_net_read(...) and DSAPI_net_event(...) */

  /* 5. Clean disconnect and teardown */
  DSAPI_net_shutdown(net);
}
```

> [!TIP]
> Size `dfifo` in `DSAPI_net_startup(dfifo, efifo)` generously if downstream visualization or disk logging occasionally blocks, and monitor `DSAPI_net_missed_blocks` to detect consumer backpressure early.

## DS GUI View Integration

When connecting to an interactive DS workstation, clients can inspect or switch the active GUI workspace perspective and send view commands:

| Function | Arguments / Return Values |
| --- | --- |
| `DSAPI_net_gui_view(net, id, view)` | Set or query GUI view: `-1 = Query`, `0 = Engineering`, `1 = TestOps`, `2 = Calibration` |
| `DSAPI_net_gui_view_command(net, id, cmd, response)` | Execute a view-level GUI command and capture the text response |
