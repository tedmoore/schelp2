# HPZ1

*Two point difference filter*

**Related:** [LPZ1](../Classes/LPZ1.md), [HPZ2](../Classes/HPZ2.md)

**Categories:** UGens>Filters>Linear

## Description

A special case fixed filter. Implements the formula:

```
out(i) = 0.5 * (in(i) - in(i-1))
```


Which is a two point differentiator.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```
// Compare:

{ WhiteNoise.ar(0.25) }.play;

{ HPZ1.ar(WhiteNoise.ar(0.25)) }.play;

// HPZ1 is useful to detect changes in a signal:
// see also HPZ2
(
{
    var changingSignal = LFNoise0.ar(1000);
    var hpz1 = HPZ1.ar(changingSignal);
    [hpz1, hpz1 > 0, hpz1.abs > 0]
}.plot
);
```




