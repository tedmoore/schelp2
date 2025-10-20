# RLPF

*A resonant low pass filter.*

**Related:** [Formlet](../Classes/Formlet.md), [RHPF](../Classes/RHPF.md), [Resonz](../Classes/Resonz.md), [Ringz](../Classes/Ringz.md)

**Categories:** UGens>Filters>Linear

## Description

A resonant low pass filter.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `freq` | Cutoff frequency in Hertz. WARNING: due to the nature of its implementation frequency values close to 0 may cause glitches and/or extremely loud audio artifacts! |  
| `rq` | The reciprocal of Q (bandwidth / cutoffFreq). |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```
{ RLPF.ar(Saw.ar(200, 0.1), SinOsc.ar(XLine.kr(0.7, 300, 20), 0, 3600, 4000), 0.2) }.play;


(
{ var ctl = RLPF.ar(Saw.ar(5, 0.1), 25, 0.03);
    SinOsc.ar(ctl * 200 + 400) * 0.1;
}.play;
)


(
{ var ctl = RLPF.ar(Saw.ar(5, 0.1), MouseX.kr(2, 200, 1), MouseY.kr(0.01, 1, 1));
    SinOsc.ar(ctl * 200 + 400) * 0.1;
}.play;
)
```




