# DecodeB2

*2D Ambisonic B-format decoder.*

**Related:** [BiPanB2](../Classes/BiPanB2.md), [PanB](../Classes/PanB.md), [PanB2](../Classes/PanB2.md), [Rotate2](../Classes/Rotate2.md)

**Categories:** UGens>Multichannel>Ambisonics

## Description

Decode a two dimensional ambisonic B-format signal to a set of speakers in a regular polygon. The outputs will be in clockwise order. The position of the first speaker is either center or left of center.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `numChans` | Number of output speakers. Typically 4 to 8. Must be a nonzero, positive integer. This is fixed when the SynthDef is compiled so cannot be assigned to a SynthDef argument. |  
| `w` | The B-format signal. |  
| `x` | The B-format signal. |  
| `y` | The B-format signal. |  
| `orientation` | Should be zero if the front is a vertex of the polygon. The first speaker will be directly in front. Should be 0.5 if the front bisects a side of the polygon. Then the first speaker will be the one left of center. |  
**Returns:** An array of channels, one for each speaker.
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




