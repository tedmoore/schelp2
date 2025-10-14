# TwoZero

*Two zero filter.*

**Related:** [TwoPole](../Classes/TwoPole.md)

**Categories:** UGens>Filters>Linear

## Description

A two zero filter.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `freq` | Frequency of zero angle. |  
| `radius` | Radius of zero. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```supercollider
{ TwoZero.ar(WhiteNoise.ar(0.125), XLine.kr(20, 20000, 8), 1) }.play
```




