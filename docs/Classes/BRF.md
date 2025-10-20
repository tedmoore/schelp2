# BRF

*2nd order Butterworth band reject filter.*

**Related:** [BPF](../Classes/BPF.md), [HPF](../Classes/HPF.md), [LPF](../Classes/LPF.md)

**Categories:** UGens>Filters>Linear

## Description

A second order band reject filter.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `freq` | Cutoff frequency in Hertz. WARNING: due to the nature of its implementation frequency values close to 0 may cause glitches and/or extremely loud audio artifacts! |  
| `rq` | The reciprocal of Q (bandwidth / cutoffFreq). |  

## Examples


```
{ BRF.ar(Saw.ar(200, 0.1), FSinOsc.kr(XLine.kr(0.7, 300, 20), 0, 3800, 4000), 0.3) }.play;

{ BRF.ar(Saw.ar(200, 0.5), MouseX.kr(100, 10000, 1), 0.3) }.play;


    // BRF on control signals:
(
{     var vib = BRF.kr(SinOsc.kr([1, 3, 10], 0, [1, 0.5, 0.25]).sum, MouseX.kr(1, 10, 1), 0.3);
    SinOsc.ar(vib * 200 + 600) * 0.2 }.play;
)
```




