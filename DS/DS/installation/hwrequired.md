# Hardware Requirements

This section should can be used as guidance for users wishing to build their own
APEX DS based acquisition systems. There is some opportunity for trade-offs in
the requirements below: twice the channel count but half the maximum sample rate
requires about the same hardware performance. Component (CPU, graphics, etc..)
benchmarks are available at:

[http://www.cpubenchmark.net](http://www.cpubenchmark.net)

## CPU

Minimum 1000 cpubenchmark.net CPU Mark for each unit of 16 channels at 200kHz
sample rate.

> [!NOTE]
> Example: Intel Core i3-370M @ 2.40GHz : 2038 CPU Mark would support 32
> channels at 200kHz.

## Memory

Minimum 1GB, 1GB for each additional unit of 16 channels at 200kHz sample rate.

## Video

Recommend the use of an Nvidia brand video card with performance that meets or
exceeds a Nvida Geforce 8400 GS. Other brand video cards can be used but must
have a minimum 100 G3D cpubenchmark.net score.

> [!NOTE]
> Example: Nvidia Geforce 8400 GS: 115 G3D

## Storage

Sufficient sustained 3x disk write rate to satisfy aggregate SR and channel
count. As a rule of thumb, a rotating hard drive can support sustained raw (i.e.
**not** counting the file system performance penalty) data write rates of about
50 MBytes/sec. The same figure for SSD drives is typically over 500MBytes/sec.
RAID configurations are recommended for systems that require higher storage
bandwidth.

> [!NOTE]
> Example: 32 channels 200kHz simultaneous raw and peak storage = ~13MB/sec
> would require absolute 39MB/sec sustained storage write rate.
