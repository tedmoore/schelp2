# BAllPass

*All Pass Filter*

**Categories:** UGens>Filters>BEQSuite

**Related:** [SOS](../Classes/SOS.md), [BLowPass](../Classes/BLowPass.md), [BLowPass4](../Classes/BLowPass4.md), [BHiPass](../Classes/BHiPass.md), [BHiPass4](../Classes/BHiPass4.md), [BPeakEQ](../Classes/BPeakEQ.md), [BLowShelf](../Classes/BLowShelf.md), [BHiShelf](../Classes/BHiShelf.md), [BBandPass](../Classes/BBandPass.md), [BBandStop](../Classes/BBandStop.md)

## Description

The B equalization suite is based on the Second Order Section ([SOS](../Classes/SOS.md)) biquad UGen.

> **Note:** Biquad coefficient calculations imply certain amount of CPU overhead. These plugin UGens contain optimizations such that the coefficients get updated only when there has been a change to one of the filter's parameters. This can cause spikes in CPU performance and should be considered when using several of these units.




## Class Methods


### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | input signal to be processed. |  
| `freq` | center frequency. WARNING: due to the nature of its implementation frequency values close to 0 may cause glitches and/or extremely loud audio artifacts! |  
| `rq` | the reciprocal of Q. bandwidth / cutoffFreq. |  
| `mul` |  |  
| `add` |  |  

## Examples


```
s.boot;
(
z = { // thru
BAllPass.ar(
    SoundIn.ar([0, 1]),
    MouseX.kr(10, 18000, \exponential),
    0.8, // rq
    0.5); // mul
}.play)
z.release;

(
z = { // like a bandpass
    var sig;
    sig = SoundIn.ar([0, 1]) * 0.5;
    BAllPass.ar(sig, MouseX.kr(10, 18000, \exponential), 0.8) + sig.neg
}.play)
z.release;
```




