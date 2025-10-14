# OneZero

*One zero filter.*

**Related:** [OnePole](../Classes/OnePole.md)

**Categories:** UGens>Filters>Linear

## Description

A one zero filter. Implements the formula:

```supercollider
out(i) = ((1 - abs(coef)) * in(i)) + (coef * in(i-1)).
```




## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `coef` | Feed forward coefficient.+0.5 makes a two point averaging filter (see also [LPZ1](../Classes/LPZ1.md)).-0.5 makes a differentiator (see also [HPZ1](../Classes/HPZ1.md)).+1 makes a single sample delay (see also [Delay1](../Classes/Delay1.md)).-1 makes an inverted single sample delay. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```supercollider
{ OneZero.ar(WhiteNoise.ar(0.5), 0.5) }.play

{ OneZero.ar(WhiteNoise.ar(0.5), -0.5) }.play

{ OneZero.ar(WhiteNoise.ar(0.5), Line.kr(-0.5, 0.5, 10)) }.play
```




