# BLowPass4

*24db/oct rolloff - 4th order resonant Low Pass Filter [1]*

**Categories:** UGens>Filters>BEQSuite

**Related:** [SOS](../Classes/SOS.md), [BLowPass](../Classes/BLowPass.md), [BHiPass](../Classes/BHiPass.md), [BHiPass4](../Classes/BHiPass4.md), [BPeakEQ](../Classes/BPeakEQ.md), [BLowShelf](../Classes/BLowShelf.md), [BHiShelf](../Classes/BHiShelf.md), [BBandPass](../Classes/BBandPass.md), [BBandStop](../Classes/BBandStop.md), [BAllPass](../Classes/BAllPass.md)

## Description

The B equalization suite is based on the Second Order Section ([SOS](../Classes/SOS.md)) biquad UGen.

> **Note:** Biquad coefficient calculations imply certain amount of CPU overhead. These plugin UGens contain optimizations such that the coefficients get updated only when there has been a change to one of the filter's parameters. This can cause spikes in CPU performance and should be considered when using several of these units.


[1] this is a composite pseudo [UGen](../Classes/UGen.md). BLowPass4 is built by cascading 2 [SOS](../Classes/SOS.md) sections.


## Class Methods

### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | input signal to be processed. |  
| `freq` | cutoff frequency. WARNING: due to the nature of its implementation frequency values close to 0 may cause glitches and/or extremely loud audio artifacts! |  
| `rq` | the reciprocal of Q. bandwidth / cutoffFreq. |  
| `mul` |  |  
| `add` |  |  

## Examples


```supercollider
s.boot;
(
z = {
    BLowPass4.ar(
        SoundIn.ar([0, 1]),
        MouseX.kr(10, 20000, \exponential), // cutoff freq.
        MouseY.kr(0.1, 1.0, \linear), // rq - compensate for 2 biquad sections.
        0.5); // mul
}.play)
z.release;
```




