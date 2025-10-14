# IRand

*Single integer random number generator.*

**Related:** [ExpRand](../Classes/ExpRand.md), [LinRand](../Classes/LinRand.md), [NRand](../Classes/NRand.md), [Rand](../Classes/Rand.md), [TExpRand](../Classes/TExpRand.md), [TIRand](../Classes/TIRand.md), [TRand](../Classes/TRand.md)

**Categories:** UGens>Random

## Description

Generates a single random integer value in uniform distribution from `lo` to `hi` . It generates this when the SynthDef first starts playing, and remains fixed for the duration of the synth's existence.


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
SynthDef("help-IRand", {
    Out.ar(
        IRand(0, 1), // play on random channel between 0 and 1
        FSinOsc.ar(500,
            0, Line.kr(0.2, 0, 0.1, doneAction: Done.freeSelf))
    )
}).add;
)

(
Routine({
    16.do({
        Synth.new("help-IRand"); 0.5.wait;
    })
}).play;
)
```




