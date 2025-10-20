# BPF

*2nd order Butterworth bandpass filter.*

**Related:** [BRF](../Classes/BRF.md), [HPF](../Classes/HPF.md), [LPF](../Classes/LPF.md)

**Categories:** UGens>Filters>Linear

## Description

A second order band pass filter.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `freq` | Centre frequency in Hertz. WARNING: due to the nature of its implementation frequency values close to 0 may cause glitches and/or extremely loud audio artifacts! |  
| `rq` | The reciprocal of Q. Q is conventionally defined as freq / bandwidth, meaning rq = (bandwidth / freq). |  
| `mul` |  |  
| `add` |  |  

## Examples


```
{ BPF.ar(Saw.ar(200, 0.5), FSinOsc.kr(XLine.kr(0.7, 300, 20), 0, 3600, 4000), 0.3) }.play;

{ BPF.ar(Saw.ar(200, 0.5), MouseX.kr(100, 10000, 1), 0.3) }.play;

    // BPF on control signals:
(
{     var vib = BPF.kr(PinkNoise.kr, MouseX.kr(1, 100, 1), 0.3) * 10;
    SinOsc.ar(vib * 200 + 600) * 0.2 }.play;
)
```




