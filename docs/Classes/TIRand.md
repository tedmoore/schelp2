# TIRand

*Triggered integer random number generator.*

**Related:** [ExpRand](../Classes/ExpRand.md), [IRand](../Classes/IRand.md), [LinRand](../Classes/LinRand.md), [NRand](../Classes/NRand.md), [Rand](../Classes/Rand.md), [TExpRand](../Classes/TExpRand.md), [TRand](../Classes/TRand.md), [TChoose](../Classes/TChoose.md)

**Categories:** UGens>Random, UGens>Triggers

## Description

Generates a random integer value in uniform distribution from `lo` to `hi` each time the trigger signal changes from nonpositive to positive values.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `lo` | Lower limit of the output range. |  
| `hi` | Upper limit of the output range. |  
| `trig` | The trigger. Trigger can be any signal. A trigger happens when the signal changes from non-positive to positive. |  

## Examples


```supercollider
(
SynthDef("help-TIRand", {
    var trig, outBus;
    trig = Dust.kr(10);
    outBus = TIRand.kr(0, 1, trig); // play on random channel between 0 and 1
    Out.ar(outBus, PinkNoise.ar(0.2))

}).play;
)

(
{
    var trig = Dust.kr(10);
    SinOsc.ar(
            TIRand.kr(4, 12, trig) * 100
        ) * 0.1
}.play;
)

(
{
    var trig = Dust.ar(MouseX.kr(1, 8000, 1));
    SinOsc.ar(
            TIRand.ar(4, 12, trig) * 100
        ) * 0.1
}.play;
)
```




