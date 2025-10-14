# InRange

*Tests if a signal is within a given range.*

**Related:** [InRect](../Classes/InRect.md), [Schmidt](../Classes/Schmidt.md)

**Categories:** UGens>Maths

## Description

If `lo ≤ in ≤ hi`, output 1.0, otherwise output 0.0.


## Class Methods

### `ar`, `kr`, `ir`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | Signal to be tested. If `InRange` is running at audio rate, **in** must also be audio rate. |  
| `lo` | Low threshold. Updated at control rate. |  
| `hi` | High threshold. Updated at control rate. |  

## Examples


```supercollider
// See the trigger
{ InRange.kr(SinOsc.kr(1, 0, 0.2), -0.15, 0.15) }.scope;

// Trigger noise burst
{ InRange.kr(SinOsc.kr(1, 0, 0.2), -0.15, 0.15) * BrownNoise.ar(0.1) }.scope;
```




