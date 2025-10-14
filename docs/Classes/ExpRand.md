# ExpRand

*Exponential single random number generator.*

**Related:** [IRand](../Classes/IRand.md), [LinRand](../Classes/LinRand.md), [NRand](../Classes/NRand.md), [Rand](../Classes/Rand.md), [TExpRand](../Classes/TExpRand.md), [TIRand](../Classes/TIRand.md), [TRand](../Classes/TRand.md)

**Categories:** UGens>Random

## Description

Generates a single random float value in an exponential distributions from `lo` to `hi` . It generates this when the SynthDef first starts playing, and remains fixed for the duration of the synth's existence.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `lo` | Lower limit of the output range. |  
| `hi` | Upper limit of the output range. |  

## Examples


```supercollider
(
SynthDef("help-ExpRand", { |out = 0|
    Out.ar(out,
        FSinOsc.ar(
            ExpRand(100.0, 8000.0),
            0, Line.kr(0.2, 0, 0.01, doneAction: Done.freeSelf))
    )
}).add;
)

(
Routine({
    inf.do({ |i|
        Synth.new("help-ExpRand"); 0.05.wait;
    })
}).play;
)
```




