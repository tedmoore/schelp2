# PinkNoise

*Pink Noise.*

**Related:** [BrownNoise](../Classes/BrownNoise.md), [GrayNoise](../Classes/GrayNoise.md), [ClipNoise](../Classes/ClipNoise.md), [WhiteNoise](../Classes/WhiteNoise.md)

**Categories:** UGens>Generators>Stochastic

## Description

Generates noise whose spectrum falls off in power by 3 dB per octave, which gives equal power over the span of each octave. This version is band-limited to 8 octaves.
Internally, this UGen calculates its output by means of the Voss-McCartney algorithm. [http://www.firstpr.com.au/dsp/pink-noise/allan-2/spectrum2.html](http://www.firstpr.com.au/dsp/pink-noise/allan-2/spectrum2.html)

> **Note:** The values produced by this UGen were observed to lie with very high probability between approximately -0.65 and +0.81 (before being multiplied by mul). The signal's RMS is approximately -16 dB.




## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```
(
SynthDef("help-PinkNoise", { |out = 0|
    Out.ar(out,
        PinkNoise.ar(0.4)
    )
}).play;
)
```




