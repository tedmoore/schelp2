# LFDClipNoise

*Dynamic clipped noise*

**Related:** [LFClipNoise](../Classes/LFClipNoise.md), [LFDNoise0](../Classes/LFDNoise0.md), [LFDNoise1](../Classes/LFDNoise1.md), [LFDNoise3](../Classes/LFDNoise3.md), [LFNoise0](../Classes/LFNoise0.md), [LFNoise1](../Classes/LFNoise1.md), [LFNoise2](../Classes/LFNoise2.md)

**Categories:** UGens>Generators>Stochastic

## Description

Like [LFClipNoise](../Classes/LFClipNoise.md), it generates the values -1 or +1 at a rate given by the `freq` argument, with two differences:
- no time quantization
- fast recovery from low freq values> *[LFClipNoise](../Classes/LFClipNoise.md), as well as [LFNoise0](../Classes/LFNoise0.md), [LFNoise1](../Classes/LFNoise1.md) and [LFNoise2](../Classes/LFNoise2.md) quantize to the nearest integer division of the samplerate, and they poll the `freq` argument only when scheduled; thus they often seem to hang when freqs get very low.*

If you don't need very high or very low freqs, or use fixed freqs, [LFClipNoise](../Classes/LFClipNoise.md) is more efficient.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `freq` | Approximate rate at which to generate random values. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```supercollider
// try wiggling the mouse quickly;
// LFNoise frequently seems stuck, LFDNoise changes smoothly.

{ LFClipNoise.ar(MouseX.kr(0.1, 1000, 1), 0.1) }.play

{ LFDClipNoise.ar(MouseX.kr(0.1, 1000, 1), 0.1) }.play

// silent for 2 secs before going up in freq

{ LFClipNoise.ar(XLine.kr(0.5, 10000, 3), 0.1) }.scope;

{ LFDClipNoise.ar(XLine.kr(0.5, 10000, 3), 0.1) }.scope;


// LFNoise quantizes time steps at high freqs, LFDNoise does not:

{ LFClipNoise.ar(XLine.kr(1000, 20000, 10), 0.1) }.scope;

{ LFDClipNoise.ar(XLine.kr(1000, 20000, 10), 0.1) }.scope;
```




