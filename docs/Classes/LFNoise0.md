# LFNoise0

*Step noise*

**Related:** [LFClipNoise](../Classes/LFClipNoise.md), [LFDClipNoise](../Classes/LFDClipNoise.md), [LFDNoise0](../Classes/LFDNoise0.md), [LFDNoise1](../Classes/LFDNoise1.md), [LFDNoise3](../Classes/LFDNoise3.md), [LFNoise1](../Classes/LFNoise1.md), [LFNoise2](../Classes/LFNoise2.md)

**Categories:** UGens>Generators>Stochastic

## Description

Generates random values at a rate given by the nearest integer division of the sample rate by the `freq` argument.


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
{ LFNoise0.ar(1000, 0.25) }.play;

// modulate frequency

{ LFNoise0.ar(XLine.kr(1000, 10000, 10), 0.25) }.play;

// as frequency modulator
(
{ SinOsc.ar(
        LFNoise0.ar(4, 400, 450),
        0, 0.2
    )
}.play;
)

// freq is the rate of starting points
{ var freq = 1000; [LFNoise0.ar(freq), Impulse.ar(freq)] }.plot
```




