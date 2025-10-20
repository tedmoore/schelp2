# TRand

*Triggered random number generator.*

**Related:** [ExpRand](../Classes/ExpRand.md), [IRand](../Classes/IRand.md), [LinRand](../Classes/LinRand.md), [NRand](../Classes/NRand.md), [Rand](../Classes/Rand.md), [TExpRand](../Classes/TExpRand.md), [TIRand](../Classes/TIRand.md)

**Categories:** UGens>Random, UGens>Triggers

## Description

Generates a random float value in uniform distribution from `lo` to `hi` each time the trigger signal changes from nonpositive to positive values.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `lo` | Lower limit of the output range. |  
| `hi` | Upper limit of the output range. |  
| `trig` | The trigger. Trigger can be any signal. A trigger happens when the signal changes from non-positive to positive. |  

## Examples


```
(
{
    var trig = Dust.kr(10);
    SinOsc.ar(
            TRand.kr(300, 3000, trig)
        ) * 0.1
}.play;
)

(
{
    var trig = Dust.ar(MouseX.kr(1, 8000, 1));
    SinOsc.ar(
            TRand.ar(300, 3000, trig)
        ) * 0.1
}.play;
)
```




