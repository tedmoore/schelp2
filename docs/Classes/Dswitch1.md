# Dswitch1

*Demand rate generator for switching between inputs.*

**Related:** [Demand](../Classes/Demand.md), [Duty](../Classes/Duty.md), [TDuty](../Classes/TDuty.md), [Dswitch](../Classes/Dswitch.md)

**Categories:** UGens>Demand

## Description

Demand rate generator for switching between inputs.
See [Pswitch1](../Classes/Pswitch1.md) for structurally related equivalent.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `list` | Array of values or other UGens. |  
| `index` | Which of the inputs to return. |  

## Examples


```supercollider
(
{
    var a, freq, trig;
    a = Dswitch1([1, 3, MouseY.kr(1, 15), 2, Dwhite(0, 3, 2)], MouseX.kr(0, 4));
    trig = Impulse.kr(3);
    freq = Demand.kr(trig, 0, a) * 30 + 340;
    SinOsc.ar(freq) * 0.1

}.play;
)

(
{
    var a, freq, trig;
    a = Dswitch1({ |i| Dseq((0..i*3), inf) } ! 5, MouseX.kr(0, 4));
    trig = Impulse.kr(6);
    freq = Demand.kr(trig, 0, a) * 30 + 340;
    SinOsc.ar(freq) * 0.1

}.play;
)
```




