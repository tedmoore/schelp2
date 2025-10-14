# Dust

*Random impulses.*

**Related:** [Dust2](../Classes/Dust2.md)

**Categories:** UGens>Generators>Stochastic

## Description

Generates random impulses from 0 to +1.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `density` | Average number of impulses per second. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```supercollider
(
SynthDef("help-Dust", { |out = 0|
    Out.ar(out,
        Dust.ar(200, 0.5)
    )
}).play;
)

(
SynthDef("help-Dust", { |out = 0|
    Out.ar(out,
        Dust.ar(XLine.kr(20000, 2, 10), 0.5)
    )
}).play;
)
```




