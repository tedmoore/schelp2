# Dser

*Demand rate sequence generator.*

**Related:** [Demand](../Classes/Demand.md), [Drand](../Classes/Drand.md), [Dseq](../Classes/Dseq.md), [Duty](../Classes/Duty.md), [Dxrand](../Classes/Dxrand.md), [TDuty](../Classes/TDuty.md)

**Categories:** UGens>Demand

## Description

Demand rate sequence generator.
See [Pser](../Classes/Pser.md) for structurally related equivalent.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `list` | An array of values or other UGens. |  
| `repeats` | Number of values to return. |  

## Examples


```supercollider
(
{
    var a, freq, trig;
    a = Dser([1, 3, 2, 7, 8], 8);
    trig = Impulse.kr(MouseX.kr(1, 40, 1));
    freq = Demand.kr(trig, 0, a) * 30 + 340;
    SinOsc.ar(freq) * 0.1

}.play;
)
```




