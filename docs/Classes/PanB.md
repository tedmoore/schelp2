# PanB

*Ambisonic B-format panner.*

**Related:** [BiPanB2](../Classes/BiPanB2.md), [DecodeB2](../Classes/DecodeB2.md), [PanB2](../Classes/PanB2.md), [Rotate2](../Classes/Rotate2.md)

**Categories:** UGens>Multichannel>Ambisonics

## Description

Ambisonic B format panner. Output channels are in order W, X, Y, Z.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `azimuth` | Azimuth in radians, -π to +π. |  
| `elevation` | Elevation in radians, -0.5π to +0.5π. |  
| `gain` | A control rate level input. |  

## Examples


```
// You'll only hear the first two channels on a stereo setup.
play({
    #w, x, y, z = PanB.ar(WhiteNoise.ar, LFSaw.kr(0.5, pi), FSinOsc.kr(0.31, 0.5pi), 0.3);
    // decode for 4 channels
    DecodeB2.ar(4, w, x, y, 0.5);
});
```




