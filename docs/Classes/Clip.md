# Clip

*Clip a signal outside given thresholds.*

**Related:** [Fold](../Classes/Fold.md), [Wrap](../Classes/Wrap.md)

**Categories:** UGens>Maths

## Description

This differs from the [BinaryOpUGen](../Classes/BinaryOpUGen.md) [clip2](../Overviews/Methods.md#clip2) in that it allows one to set both low and high thresholds.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | Signal to be clipped. |  
| `lo` | Low threshold of clipping. Must be less then hi. |  
| `hi` | High threshold of clipping. Must be greater then lo. |  

## Examples


```supercollider
s.boot;

{ Clip.ar(SinOsc.ar(440, 0, 0.2), -0.07, 0.07) }.scope;
```




