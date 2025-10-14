# HPF

*2nd order Butterworth highpass filter.*

**Related:** [BPF](../Classes/BPF.md), [BRF](../Classes/BRF.md), [LPF](../Classes/LPF.md)

**Categories:** UGens>Filters>Linear

## Description

A second order high pass filter.


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
{ HPF.ar(Saw.ar(200, 0.1), FSinOsc.kr(XLine.kr(0.7, 300, 20), 0, 3600, 4000), 5) }.play;

(
{     var ctl = HPF.kr(LFSaw.kr(5), SinOsc.kr(XLine.kr(0.07, 30, 20), 0, 35, 40)) ;
    SinOsc.ar(ctl * 200 + 500);
}.play;
)

(
{     var ctl = HPF.kr(LFSaw.kr(5, 0.1), MouseX.kr(2, 200, 1));
    SinOsc.ar(ctl * 200 + 400) * 0.1;
}.play;
)
```




