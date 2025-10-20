# TwoPole

*Two pole filter.*

**Related:** [TwoZero](../Classes/TwoZero.md)

**Categories:** UGens>Filters>Linear

## Description

A two pole filter. This provides lower level access to setting of pole location. For general purposes [Resonz](../Classes/Resonz.md) is better.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `freq` | Frequency of pole angle. |  
| `radius` | Radius of pole. Should be between 0 and +1. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```
{ TwoPole.ar(WhiteNoise.ar(0.005), 2000, 0.95) }.play

{ TwoPole.ar(WhiteNoise.ar(0.005), XLine.kr(800, 8000, 8), 0.95) }.play

{ TwoPole.ar(WhiteNoise.ar(0.005), MouseX.kr(800, 8000, 1), 0.95) }.play
```




