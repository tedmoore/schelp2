# LFClipNoise

*Clipped noise*

**Related:** [LFDClipNoise](../Classes/LFDClipNoise.md), [LFDNoise0](../Classes/LFDNoise0.md), [LFDNoise1](../Classes/LFDNoise1.md), [LFDNoise3](../Classes/LFDNoise3.md), [LFNoise0](../Classes/LFNoise0.md), [LFNoise1](../Classes/LFNoise1.md), [LFNoise2](../Classes/LFNoise2.md)

**Categories:** UGens>Generators>Stochastic

## Description

Randomly generates the values -1 or +1 at a rate given by the nearest integer division of the sample rate by the `freq` argument. It is probably pretty hard on your speakers!


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
(
SynthDef("help-LFClipNoise", { |out = 0|
    Out.ar(out,
        LFClipNoise.ar(1000, 0.25)
    )
}).play;
)

// modulate frequency
(
SynthDef("help-LFClipNoise", { |out = 0|
    Out.ar(out,
        LFClipNoise.ar(XLine.kr(1000, 10000, 10), 0.25)
    )
}).play;
)

// use as frequency control
(
SynthDef("help-LFClipNoise", { |out = 0|
    Out.ar(out,
        SinOsc.ar(
            LFClipNoise.ar(4, 200, 600),
            0, 0.2
        )
    )
}).play;
)
```




