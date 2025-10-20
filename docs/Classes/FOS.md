# FOS

*First order filter section.*

**Related:** [SOS](../Classes/SOS.md)

**Categories:** UGens>Filters>Linear

## Description

A standard first order filter section. Filter coefficients are given directly rather than calculated for you. Formula is equivalent to:

```
out(i) = (a0 * in(i)) + (a1 * in(i-1)) + (b1 * out(i-1))
```




## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | Signal input. |  
| `a0` | See formula above. |  
| `a1` | See formula above. |  
| `b1` | See formula above. |  
| `mul` |  |  
| `add` |  |  

## Examples


```
(
// same as OnePole
{    var x;
    x = LFTri.ar(0.4, 0, 0.99);
    FOS.ar(LFSaw.ar(200, 0, 0.2), 1 - x.abs, 0.0, x)
}.play;
)

(
// same as OneZero
{    var x;
    x = LFTri.ar(0.4, 0, 0.99);
    FOS.ar(LFSaw.ar(200, 0, 0.2), 1 - x.abs, x, 0.0)
}.play;
)

(
// same as OnePole, kr
{    var x, ctl;
    x = LFTri.kr(0.2, 0, 0.99);
    ctl = FOS.kr(LFSaw.kr(8, 0, 0.2), 1 - x.abs, 0.0, x);
    LFTri.ar(ctl * 200 + 500);
}.play;
)
```




