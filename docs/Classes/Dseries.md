# Dseries

*Demand rate arithmetic series UGen.*

**Related:** [Demand](../Classes/Demand.md), [Dgeom](../Classes/Dgeom.md), [Duty](../Classes/Duty.md), [TDuty](../Classes/TDuty.md)

**Categories:** UGens>Demand

## Description

Demand rate arithmetic series UGen.
See [Pseries](../Classes/Pseries.md) for structurally related equivalent.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `start` | Start value. Can be a number or any other UGen. |  
| `step` | Step value. Can be a number or any other UGen. |  
| `length` | Number of values to create. Can be a number or any other UGen. |  

## Examples


```supercollider
(
{
    var a, freq, trig;
    a = Dseries(0, 1, 15);
    trig = Impulse.kr(MouseX.kr(1, 40, 1));
    freq = Demand.kr(trig, 0, a) * 30 + 340;
    SinOsc.ar(freq) * 0.1

}.play;
)

(
{
    var a, freq, trig;
    a = Dseries(0, 1, inf);
    trig = Dust.kr(MouseX.kr(1, 40, 1));
    freq = Demand.kr(trig, 0, a) % 15 * 30 + 340;
    SinOsc.ar(freq) * 0.1

}.play;
)
```




