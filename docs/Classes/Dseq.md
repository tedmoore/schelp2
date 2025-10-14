# Dseq

*Demand rate sequence generator.*

**Related:** [Demand](../Classes/Demand.md), [Drand](../Classes/Drand.md), [Dser](../Classes/Dser.md), [Duty](../Classes/Duty.md), [Dxrand](../Classes/Dxrand.md), [TDuty](../Classes/TDuty.md)

**Categories:** UGens>Demand

## Description

Demand rate sequence generator.
See [Pseq](../Classes/Pseq.md) for structurally related equivalent.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `list` | An array of values or other UGens. |  
| `repeats` | Number of repeats. |  

## Examples


```supercollider
(
{
    var a, freq, trig;
    a = Dseq([1, 3, 2, 7, 8], 3);
    trig = Impulse.kr(MouseX.kr(1, 40, 1));
    freq = Demand.kr(trig, 0, a) * 30 + 340;
    SinOsc.ar(freq) * 0.1

}.play;
)

// audio rate
(
{
    var a, freq, trig;
    a = Dseq({ 10.rand } ! 32, inf);
    trig = Impulse.ar(MouseX.kr(1, 10000, 1));
    freq = Demand.ar(trig, 0, a) * 30 + 340;
    SinOsc.ar(freq) * 0.1

}.play;
)
```




