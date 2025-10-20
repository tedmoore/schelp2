# Crackle

*Chaotic noise function.*

**Related:** [LatoocarfianN](../Classes/LatoocarfianN.md), [Logistic](../Classes/Logistic.md)

**Categories:** UGens>Generators>Stochastic

## Description

A noise generator based on a chaotic function.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `chaosParam` | A parameter of the chaotic function with useful values from just below 1.0 to just above 2.0. Towards 2.0 the sound crackles. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```
{ Crackle.ar(1.95, 0.5) }.play;

// modulate chaos parameter
{ Crackle.ar(Line.kr(1.0, 2.0, 3), 0.5, 0.5) }.play;
```




