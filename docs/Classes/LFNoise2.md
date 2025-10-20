# LFNoise2

*Quadratic noise.*

**Related:** [LFClipNoise](../Classes/LFClipNoise.md), [LFDClipNoise](../Classes/LFDClipNoise.md), [LFDNoise0](../Classes/LFDNoise0.md), [LFDNoise1](../Classes/LFDNoise1.md), [LFDNoise3](../Classes/LFDNoise3.md), [LFNoise0](../Classes/LFNoise0.md), [LFNoise1](../Classes/LFNoise1.md)

**Categories:** UGens>Generators>Stochastic

## Description

Generates quadratically interpolated random values at a rate given by the nearest integer division of the sample rate by the `freq` argument.

> **Note:** quadratic interpolation means that the noise values can occasionally extend beyond the normal range of +-1, if the freq varies in certain ways. If this is undesirable then you might like to clip2 the values, or use a linearly-interpolating unit instead.




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
{ LFNoise2.ar(1000, 0.25) }.play;

// modulate frequency

{ LFNoise2.ar(XLine.kr(1000, 10000, 10), 0.25) }.play;

// as frequency modulator
(
{ SinOsc.ar(
        LFNoise2.ar(4, 400, 450),
        0, 0.2
    )
}.play;
)

// freq is the rate of interpolation points
{ var freq = 1000; [LFNoise2.ar(freq), Impulse.ar(freq)] }.plot
```




