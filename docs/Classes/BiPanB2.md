# BiPanB2

*2D Ambisonic B-format panner.*

**Related:** [DecodeB2](../Classes/DecodeB2.md), [PanB](../Classes/PanB.md), [PanB2](../Classes/PanB2.md), [Rotate2](../Classes/Rotate2.md)

**Categories:** UGens>Multichannel>Ambisonics

## Description

Encode a two channel signal to two dimensional ambisonic B-format. This puts two channels at opposite poles of a 2D ambisonic field. This is one way to map a stereo sound onto a soundfield. It is equivalent to:

```supercollider
PanB2(inA, azimuth, gain) + PanB2(inB, azimuth + 1, gain)
```




## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `inA` | Input signal A |  
| `inB` | Input signal B. |  
| `azimuth` | Position around the circle from -1 to +1.-1 is behind, -0.5 is left, 0 is forward, +0.5 is right, +1 is behind. |  
| `gain` | Amplitude control. |  

## Examples


```supercollider
(
{
    var w, x, y, p, q, a, b, c, d;

    p = LFSaw.ar(200);
    q = LFSaw.ar(301);

    // B-format encode
    #w, x, y = BiPanB2.ar(p, q, MouseX.kr(-1, 1), 0.1);

    // B-format decode to quad
    #a, b, c, d = DecodeB2.ar(4, w, x, y);

    [a, b, d, c] // reorder to my speaker arrangement: Lf Rf Lr Rr
}.play;
)
```




