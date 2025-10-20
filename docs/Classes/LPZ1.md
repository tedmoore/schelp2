# LPZ1

*Two point average filter*

**Related:** [HPZ1](../Classes/HPZ1.md)

**Categories:** UGens>Filters>Linear

## Description

A special case fixed filter. Implements the formula:

```
out(i) = 0.5 * (in(i) + in(i-1))
```


which is a two point averager.


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

{ LPZ1.ar(WhiteNoise.ar(0.25)) }.play;
```




