# Rand

*Single random number generator.*

**Related:** [ExpRand](../Classes/ExpRand.md), [IRand](../Classes/IRand.md), [LinRand](../Classes/LinRand.md), [NRand](../Classes/NRand.md), [TExpRand](../Classes/TExpRand.md), [TIRand](../Classes/TIRand.md), [TRand](../Classes/TRand.md)

**Categories:** UGens>Random

## Description

Generates a single random float value in uniform distribution from `lo` to `hi` . It generates this when the SynthDef first starts playing, and remains fixed for the duration of the synth's existence.


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
SynthDef("help-Rand", { |out = 0|
    Out.ar(out,
        FSinOsc.ar(
            Rand(200.0, 400.0),
            0, Line.kr(0.2, 0, 1, doneAction: Done.freeSelf))
    )
}).add;
)

(
Routine({
    8.do({
        Synth.new("help-Rand"); 1.0.wait;
    })
}).play;
)
```




