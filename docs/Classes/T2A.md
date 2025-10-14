# T2A

*Control rate trigger to audio rate trigger converter*

**Categories:** UGens>Conversion, UGens>Triggers

**Related:** [T2K](../Classes/T2K.md), [K2A](../Classes/K2A.md), [A2K](../Classes/A2K.md)

## Description

Converts control rate trigger into audio rate trigger (maximally one per control period).


## Class Methods

### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | A control rate input signal. |  
| `offset` | A sample offset within a control period. Internally clipped to an `int` in the range `[0..blockSize-1]`. |  

## Examples


```supercollider
// example
(
{
    var trig = Impulse.kr(MouseX.kr(1, 100, 1));
    Ringz.ar(T2A.ar(trig), 800, 0.01) * 0.4
}.play;
)

// compare with K2A
(
{
    var trig = Impulse.kr(200);
    [T2A.ar(trig), K2A.ar(trig)].lag(0.001)
}.plot(10/200);
)

// removing jitter by randomising offset
(
{
    var trig = Impulse.kr(MouseX.kr(1, 100, 1));
    Ringz.ar(T2A.ar(trig, WhiteNoise.kr.range(0, s.options.blockSize - 1)), 800, 0.01) * 0.4
}.play;
)
```




