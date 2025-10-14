# Wrap

*Wrap a signal outside given thresholds.*

**Related:** [Clip](../Classes/Clip.md), [Fold](../Classes/Fold.md)

**Categories:** UGens>Maths

## Description

This differs from the [BinaryOpUGen](../Classes/BinaryOpUGen.md) [wrap2](../Overviews/Methods.md#wrap2) in that it allows one to set both low and high thresholds.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | Signal to be wrapped. |  
| `lo` | Low threshold of wrapping. |  
| `hi` | High threshold of wrapping. |  

## Examples


```supercollider
s.boot;

{ Wrap.ar(SinOsc.ar(440, 0, 0.2), -0.15, 0.15) }.scope;
```




