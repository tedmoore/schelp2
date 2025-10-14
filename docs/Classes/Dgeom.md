# Dgeom

*Demand rate geometric series UGen.*

**Related:** [Demand](../Classes/Demand.md), [Dseries](../Classes/Dseries.md), [Duty](../Classes/Duty.md), [TDuty](../Classes/TDuty.md)

**Categories:** UGens>Demand

## Description

Demand rate geometric series UGen.
See [Pgeom](../Classes/Pgeom.md) for structurally related equivalent.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `start` | Start value. Can be a number or any other UGen. |  
| `grow` | Value by which to grow (x = x[-1] * grow). Can be a number or any other UGen. |  
| `length` | Number of values to create. |  
The arguments can be a number or any other ugen
## Examples


```supercollider
// example

(
{
    var a, freq, trig;
    a = Dgeom(1, 1.2, 15);
    trig = Impulse.kr(MouseX.kr(1, 40, 1));
    freq = Demand.kr(trig, 0, a) * 30 + 340;
    SinOsc.ar(freq) * 0.1

}.play;
)

(
{
    var a, freq, trig;
    a = Dgeom(1, 1.2, inf);
    trig = Dust.kr(MouseX.kr(1, 40, 1));
    freq = Demand.kr(trig, 0, a) * 30 + 340;
    SinOsc.ar(freq) * 0.1

}.play;
)
```




