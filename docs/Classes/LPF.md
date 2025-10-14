# LPF

*2nd order Butterworth lowpass filter*

**Related:** [BPF](../Classes/BPF.md), [BRF](../Classes/BRF.md), [HPF](../Classes/HPF.md)

**Categories:** UGens>Filters>Linear

## Description

A second order low pass filter.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `freq` | Cutoff frequency in Hertz. WARNING: due to the nature of its implementation frequency values close to 0 may cause glitches and/or extremely loud audio artifacts! |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```supercollider
{ LPF.ar(Saw.ar(200, 0.1), SinOsc.kr(XLine.kr(0.7, 300, 20), 0, 3600, 4000)) }.play;

// kr:
(
{ var ctl = LPF.kr(LFPulse.kr(8), SinOsc.kr(XLine.kr(1, 30, 5)) + 2);
    SinOsc.ar(ctl * 200 + 400)
}.play;
)

(
{ var ctl = LPF.kr(LFPulse.kr(8), MouseX.kr(2, 50, 1));
    SinOsc.ar(ctl * 200 + 400)
}.play;
)
```




