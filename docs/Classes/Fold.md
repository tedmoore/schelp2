# Fold

*Fold a signal outside given thresholds.*

**Related:** [Clip](../Classes/Clip.md), [Wrap](../Classes/Wrap.md)

**Categories:** UGens>Maths

## Description

This differs from the [BinaryOpUGen](../Classes/BinaryOpUGen.md) [fold2](../Overviews/Methods.md#fold2) in that it allows one to set low and high thresholds.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | Signal to be folded. |  
| `lo` | Low threshold of folding. Sample values < lo will be folded. must be less then hi. |  
| `hi` | High threshold of folding. Sample values > hi will be folded. must be greater then lo. |  

## Examples


```supercollider
s.boot;

{ Fold.ar(SinOsc.ar(440, 0, 0.2), -0.1, 0.1) }.scope;
```




