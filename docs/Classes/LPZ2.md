# LPZ2

*Two zero fixed lowpass*

**Related:** [BPZ2](../Classes/BPZ2.md), [BRZ2](../Classes/BRZ2.md), [HPZ2](../Classes/HPZ2.md)

**Categories:** UGens>Filters>Linear

## Description

A special case fixed filter. Implements the formula:

```
out(i) = 0.25 * (in(i) + (2 * in(i - 1)) + in(i - 2)).
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


```
// Compare:

{ WhiteNoise.ar(0.25) }.play;

{ LPZ2.ar(WhiteNoise.ar(0.25)) }.play;
```




