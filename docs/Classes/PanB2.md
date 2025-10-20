# PanB2

*2D Ambisonic B-format panner.*

**Related:** [BiPanB2](../Classes/BiPanB2.md), [DecodeB2](../Classes/DecodeB2.md), [PanB](../Classes/PanB.md), [Rotate2](../Classes/Rotate2.md)

**Categories:** UGens>Multichannel>Ambisonics

## Description

Encodes a mono signal to 2-dimensional ambisonic B-format.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `azimuth` | Position around the circle from -1 to +1. -1 is behind, -0.5 is left, 0 is forward, +0.5 is right, +1 is behind. |  
| `gain` | Amplitude control. |  

## Examples


```
(
{
    var w, x, y, p, a, b, c, d;

    p = PinkNoise.ar; // source

    // B-format encode
    #w, x, y = PanB2.ar(p, MouseX.kr(-1, 1), 0.1);

    // B-format decode to quad
    #a, b, c, d = DecodeB2.ar(4, w, x, y);

    [a, b, d, c] // reorder to my speaker arrangement: Lf Rf Lr Rr
}.play;
)
```




