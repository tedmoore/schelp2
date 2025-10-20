# ClipNoise

*Clip Noise.*

**Related:** [BrownNoise](../Classes/BrownNoise.md), [GrayNoise](../Classes/GrayNoise.md), [PinkNoise](../Classes/PinkNoise.md), [WhiteNoise](../Classes/WhiteNoise.md)

**Categories:** UGens>Generators>Stochastic

## Description

Generates noise whose values are either -1 or 1. This produces the maximum energy for the least peak to peak amplitude.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```
{ ClipNoise.ar(0.2) }.play;
```




