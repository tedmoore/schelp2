# WhiteNoise

*White noise.*

**Related:** [BrownNoise](../Classes/BrownNoise.md), [GrayNoise](../Classes/GrayNoise.md), [ClipNoise](../Classes/ClipNoise.md), [PinkNoise](../Classes/PinkNoise.md)

**Categories:** UGens>Generators>Stochastic

## Description

Generates noise whose spectrum has equal power at all frequencies.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```supercollider
(
SynthDef("help-WhiteNoise", { |out = 0|
    Out.ar(out,
        WhiteNoise.ar(0.25)
    )
}).play;
)
```




