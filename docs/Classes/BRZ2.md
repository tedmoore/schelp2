# BRZ2

*Two zero fixed midcut.*

**Related:** [BPZ2](../Classes/BPZ2.md), [HPZ2](../Classes/HPZ2.md), [LPZ2](../Classes/LPZ2.md)

**Categories:** UGens>Filters>Linear

## Description

A special case fixed filter. Implements the formula:

```supercollider
out(i) = 0.5 * (in(i) + in(i - 2)).
```


This filter cuts out frequencies around ½ of the Nyquist frequency.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  

## Examples


```supercollider
// Compare:

{ WhiteNoise.ar(0.25) }.play;

{ BRZ2.ar(WhiteNoise.ar(0.25)) }.play;
```




