# LinRand

*Skewed random number generator.*

**Related:** [ExpRand](../Classes/ExpRand.md), [IRand](../Classes/IRand.md), [NRand](../Classes/NRand.md), [Rand](../Classes/Rand.md), [TExpRand](../Classes/TExpRand.md), [TIRand](../Classes/TIRand.md), [TRand](../Classes/TRand.md)

**Categories:** UGens>Random

## Description

Generates a single random float value in linear distribution from `lo` to `hi`, skewed towards `lo` if `minmax` < 0, otherwise skewed towards `hi` .


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `lo` | Lower limit of the output range. |  
| `hi` | Upper limit of the output range. |  
| `minmax` | The output is skewed towards `lo` if `minmax` < 0, otherwise skewed towards `hi`. |  

## Examples


```supercollider
(
SynthDef("help-LinRand", { |out = 0, minmax = 1|
    Out.ar(out,
        FSinOsc.ar(
            LinRand(200.0, 10000.0, minmax),
            0, Line.kr(0.2, 0, 0.01, doneAction: Done.freeSelf))
    )
}).add;
)

// towards hi
(
Routine({
    loop({
        Synth.new("help-LinRand"); 0.04.wait;
    })
}).play;
)

// towards lo (doesn't work like that yet)
(
Routine({
    loop({
        Synth.new("help-LinRand", [\minmax, -1]); 0.04.wait;
    })
}).play;
)
```




