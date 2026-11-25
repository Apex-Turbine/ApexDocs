# Setup Considerations

This section is intended to provide a review of how different settings within
the DS setup can effect bandwidth and resolution. Understanding how these
settings interact will provide an efficient means for performing a setup with
the desired characteristics thus minimizing trial-and-error. DS has five
settings than effect bandwidth and resolution:

> 1. Sample Rate (samples/second)
> 2. Block Size (samples/block)
> 3. Sample Ratio
> 4. FFT Overlap
> 5. FFT Zoom

## Sample Rate

Sample rate is a fundamental property that applies to all channels. It is
entered at the top of the Setup panel as highlighted below. The sample rate is
restricted based on the hardware. Please consult the hardware specification for
the lower/upper limits on sample rate. The sample rate is specified in
samples-per-second.

## Block Size

The second fundamental property is the Block Size. It is entered at the top of
the Setup panel as highlighted below. DS is a block based system whereby a
block of samples is displayed and recorded in sequential order. The minimum
permissible block size is 64 and the maximum permissible block size is 131072.

## Sample Ratio

The sample ratio specified the up or down sampling ratio (multiplier or
divisor) of the base sample rate specified above. The sampling ratio is entered
on the Channels tab of the setup panel as shown below. The minimum sampling
ratio is 16 meaning 1/16th of the base sample rate specified above. The maximum
sample ratio is 16 times the base sample rate. Depending on the H/W device,
sampling ratios may be specified at the channel level (e.g., General Standards
PCI16SDI) or device level (e.g., National Instruments 4497). The resulting
channel or device sample rate must not exceed the A/D device capability. Please
consult the hardware specification for the lower/upper limits on sample rate.

## FFT Overlap

The FFT Overlap extends the block size by the factor entered for FFT
processing. One or more blocks of samples are concatenated together to form an
ensemble for performing the FFT. This results in an increased frequency
resolution (lower bin width). As time progresses, the oldest block is discarded
and the newest block is added, therefore only a single block is added/discarded
at a time.

## FFT Zoom

The FFT Zoom truncates the bandwidth by the zoom factor. The upper section of
the bandwidth is discarded. The resulting bandwidth is reduced by the zoom
factor. The FFT Zoom is entered on the FFT Settings tab of the setup panel as
shown below.

Changing any/all of these settings may have an impact on the signals. resulting
bandwidth and resolution. The relationship between these settings and
bandwidth/resolution are presented below.

Define the following inputs:

> 1. SR, sample rate
> 2. BS, block size
> 3. SRR, sample rate ratio; possible entries are 1/16, 1/8, 1/4, 1/2, 1, 2, 4, 8, 16
> 4. Overlap, FFT Overlap; possible entries are 1, 2, 4, 8, 16
> 5. Zoom, FFT Zoom; possible entries are 1, 2, 4, 8, 16

Then:

> - Bandwidth, BW = (SR*SRR)/(Zoom*2.56)
> - Resolution, delta f = SR/(BS*Overlap)

In addition to bandwidth and resolution, the following variables are also
relevant. Effective Block Size (FFT Ensemble Size), N, considering sample rate
ratio, overlap and zoom:

> - N = (BS*SRR*Overlap)/Zoom
>
>   N cannot be less than 64 so this may limit the maximum zoom factor permitted.

Maximum number of peaks:  the maximum number of peaks (default is 32) extracted
per ensemble is limited to 1/8th the ensemble size. Since the ensemble size is
based on BS, SRR and zoom, we have:

> - MaxPeaks = (BS*SRR*Overlap)/(Zoom*8)

For example, assume the following settings:

> - SR = 20480
> - BS = 2048
> - SRR = 1/8
> - Overlap = 2
> - Zoom = 8

Using the above equations, we can compute the following:

> - Bandwidth = 125 Hz
> - Resolution = 5 Hz
> - Ensemble Size = 64 samples
> - Maximum peaks extracted per ensemble = 8
