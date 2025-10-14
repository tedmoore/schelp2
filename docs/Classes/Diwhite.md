# Diwhite

*Demand rate white noise random generator.*

**Related:** [Dwhite](../Classes/Dwhite.md), [Demand](../Classes/Demand.md), [Duty](../Classes/Duty.md), [TDuty](../Classes/TDuty.md)

**Categories:** UGens>Demand

## Description

[Dwhite](../Classes/Dwhite.md) returns numbers in the continuous range between `lo` and `hi` . Diwhite returns integer values.
The arguments can be a number or any other UGen.
See [Pwhite](../Classes/Pwhite.md), [WhiteNoise](../Classes/WhiteNoise.md) for structurally related equivalents.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `lo` | Minimum value. |  
| `hi` | Maximum value. |  
| `length` | Number of values to create. |  

## Examples


```supercollider
(
{
    var a, freq, trig;
    a = Diwhite(0, 15, inf);
    trig = Impulse.kr(MouseX.kr(1, 40, 1));
    freq = Demand.kr(trig, 0, a) * 30 + 340;
    SinOsc.ar(freq) * 0.1

}.play;
)
```




