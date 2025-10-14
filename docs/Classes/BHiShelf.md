# BHiShelf

*Hi Shelf*

**Categories:** UGens>Filters>BEQSuite

**Related:** [SOS](../Classes/SOS.md), [BLowPass](../Classes/BLowPass.md), [BLowPass4](../Classes/BLowPass4.md), [BHiPass](../Classes/BHiPass.md), [BHiPass4](../Classes/BHiPass4.md), [BPeakEQ](../Classes/BPeakEQ.md), [BLowShelf](../Classes/BLowShelf.md), [BBandPass](../Classes/BBandPass.md), [BBandStop](../Classes/BBandStop.md), [BAllPass](../Classes/BAllPass.md)

## Description

The B equalization suite is based on the Second Order Section ([SOS](../Classes/SOS.md)) biquad UGen.

> **Note:** Biquad coefficient calculations imply certain amount of CPU overhead. These plugin UGens contain optimizations such that the coefficients get updated only when there has been a change to one of the filter's parameters. This can cause spikes in CPU performance and should be considered when using several of these units.




## Class Methods

### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | input signal to be processed. |  
| `freq` | WARNING: due to the nature of its implementation frequency values close to 0 may cause glitches and/or extremely loud audio artifacts! center frequency. |  
| `rs` | the reciprocal of S. Shell boost/cut slope. When S = 1, the shelf slope is as steep as it can be and remain monotonically increasing or decreasing gain with frequency. The shelf slope, in dB/octave, remains proportional to S for all other values for a fixed `freq/SampleRate.ir` and `db`. |  
| `db` | gain. boost/cut the center frequency in dBs. |  
| `mul` |  |  
| `add` |  |  

## Examples


```supercollider
s.boot;
(
z = { // toy around with boost/cut
BHiShelf.ar(
    SoundIn.ar([0, 1]),
    MouseX.kr(2200, 18000, \exponential),
    1.0, // rs
    MouseY.kr(18.0, -18.0, \linear),
    0.5); // mul
}.play)
z.release;

(
z = { // toy around with rs
BHiShelf.ar(
    SoundIn.ar([0, 1]),
    MouseX.kr(2200, 18000, \exponential),
    MouseY.kr(0.1, 1.0, \linear), // rs
    6, // db
    0.5); // mul
}.play)
z.release;
```




