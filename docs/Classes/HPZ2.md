# HPZ2

*Two zero fixed midcut.*

**Related:** [BPZ2](../Classes/BPZ2.md), [BRZ2](../Classes/BRZ2.md), [LPZ2](../Classes/LPZ2.md), [HPZ1](../Classes/HPZ1.md)

**Categories:** UGens>Filters>Linear

## Description

A special case fixed filter. Implements the formula:

```supercollider
out(i) = 0.25 * (in(i) - (2 * in(i - 1)) + in(i - 2)).
```




## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```supercollider
// Compare:

{ WhiteNoise.ar(0.25) }.play;

{ HPZ2.ar(WhiteNoise.ar(0.25)) }.play;

// HPZ2 is useful to detect changes in a signal:
// see also HPZ1
(
{
    var changingSignal = LFNoise0.ar(1000);
    var hpz2 = HPZ2.ar(changingSignal);
    [hpz2, hpz2 > 0]
}.plot
);
```




