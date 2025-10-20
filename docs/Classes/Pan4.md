# Pan4

*Four channel equal power pan.*

**Related:** [Balance2](../Classes/Balance2.md), [LinPan2](../Classes/LinPan2.md), [Pan2](../Classes/Pan2.md), [PanAz](../Classes/PanAz.md)

**Categories:** UGens>Multichannel>Panners

## Description

Four channel equal power panner. Outputs are in order LeftFront, RightFront, LeftBack, RightBack.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `xpos` | X pan position from -1 to +1 (left to right). |  
| `ypos` | Y pan position from -1 to +1 (back to front). |  
| `level` | A control rate level input. |  

## Examples


```
// You'll only hear the front two channels on a stereo setup.

{ Pan4.ar(PinkNoise.ar, FSinOsc.kr(2), FSinOsc.kr(1.2), 0.3)) }.play;


{ Pan4.ar(PinkNoise.ar, -1,  0, 0.3) }.play; // left pair
{ Pan4.ar(PinkNoise.ar,  1,  0, 0.3) }.play; // right pair
{ Pan4.ar(PinkNoise.ar,  0, -1, 0.3) }.play; // back pair
{ Pan4.ar(PinkNoise.ar,  0,  1, 0.3) }.play; // front pair

{ Pan4.ar(PinkNoise.ar,  0,  0, 0.3) }.play; // center
```




