# OnePole

*One pole filter.*

**Related:** [OneZero](../Classes/OneZero.md)

**Categories:** UGens>Filters>Linear

## Description

A one pole filter. Implements the formula:

```
out(i) = ((1 - abs(coef)) * in(i)) + (coef * out(i-1)).
```




## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `coef` | Feedback coefficient. Should be between -1 and +1 |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```
{ OnePole.ar(WhiteNoise.ar(0.5), 0.95) }.play

{ OnePole.ar(WhiteNoise.ar(0.5), -0.95) }.play

{ OnePole.ar(WhiteNoise.ar(0.5), Line.kr(-0.99, 0.99, 10)) }.play
```




