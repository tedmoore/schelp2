# Dibrown

*Demand rate brownian movement generator.*

**Related:** [Dbrown](../Classes/Dbrown.md), [Demand](../Classes/Demand.md), [Duty](../Classes/Duty.md), [TDuty](../Classes/TDuty.md)

**Categories:** UGens>Demand

## Description

[Dbrown](../Classes/Dbrown.md) returns numbers in the continuous range between `lo` and `hi`, Dibrown returns integer values.
The arguments can be a number or any other UGen.
See [Pbrown](../Classes/Pbrown.md), [BrownNoise](../Classes/BrownNoise.md) for structurally related equivalents.


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `lo` | Minimum value. |  
| `hi` | Maximum value. |  
| `step` | Maximum step for each new value. |  
| `length` | Number of values to create. Use `inf` for an infinite number. |  

## Examples


```
(
{
    var a, freq, trig;
    a = Dibrown(0, 15, 1, inf);
    trig = Impulse.kr(MouseX.kr(1, 40, 1));
    freq = Demand.kr(trig, 0, a) * 30 + 340;
    SinOsc.ar(freq) * 0.1

}.play;
)
```




