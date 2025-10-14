# Dxrand

*Demand rate random sequence generator.*

**Related:** [Demand](../Classes/Demand.md), [Drand](../Classes/Drand.md), [Dseq](../Classes/Dseq.md), [Dser](../Classes/Dser.md), [Duty](../Classes/Duty.md), [TDuty](../Classes/TDuty.md)

**Categories:** UGens>Demand

## Description

Dxrand never plays the same value twice, whereas [Drand](../Classes/Drand.md) chooses any value in the list.
See [Pxrand](../Classes/Pxrand.md) for structurally related equivalent.


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
    a = Dxrand([1, 3, 2, 7, 8], inf);
    trig = Impulse.kr(MouseX.kr(1, 400, 1));
    freq = Demand.kr(trig, 0, a) * 30 + 340;
    SinOsc.ar(freq) * 0.1

}.play;
)
```




