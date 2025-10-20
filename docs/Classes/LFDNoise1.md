# LFDNoise1

*Dynamic ramp noise*

**Related:** [LFClipNoise](../Classes/LFClipNoise.md), [LFDClipNoise](../Classes/LFDClipNoise.md), [LFDNoise0](../Classes/LFDNoise0.md), [LFDNoise3](../Classes/LFDNoise3.md), [LFNoise0](../Classes/LFNoise0.md), [LFNoise1](../Classes/LFNoise1.md), [LFNoise2](../Classes/LFNoise2.md)

**Categories:** UGens>Generators>Stochastic

## Description

Like [LFNoise1](../Classes/LFNoise1.md), it generates linearly interpolated random values at a rate given by the `freq` argument, with two differences:
- no time quantization
- fast recovery from low freq values> *[LFNoise0](../Classes/LFNoise0.md), [LFNoise1](../Classes/LFNoise1.md) and [LFNoise2](../Classes/LFNoise2.md) quantize to the nearest integer division of the samplerate, and they poll the `freq`argument only when scheduled; thus they often seem to hang when freqs get very low.*

If you don't need very high or very low freqs, or use fixed freqs, [LFNoise1](../Classes/LFNoise1.md) is more efficient.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `freq` | Approximate rate at which to generate random values. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```
// try wiggling mouse quickly;
// LFNoise frequently seems stuck, LFDNoise changes smoothly.

{  SinOsc.ar(LFNoise1.ar(MouseX.kr(0.1, 1000, 1), 200, 500), 0, 0.2) }.play

{  SinOsc.ar(LFDNoise1.ar(MouseX.kr(0.1, 1000, 1), 200, 500), 0, 0.2) }.play


// LFNoise quantizes time steps at high freqs, LFDNoise does not:

{ LFNoise1.ar(XLine.kr(2000, 20000, 8), 0.1) }.scope;

{ LFDNoise1.ar(XLine.kr(2000, 20000, 8), 0.1) }.scope;
```




