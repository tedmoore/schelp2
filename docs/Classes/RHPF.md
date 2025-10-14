# RHPF

*A resonant high pass filter.*

**Related:** [Formlet](../Classes/Formlet.md), [RLPF](../Classes/RLPF.md), [Resonz](../Classes/Resonz.md), [Ringz](../Classes/Ringz.md)

**Categories:** UGens>Filters>Linear

## Description

A resonant high pass filter.


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


```supercollider
{ RHPF.ar(Saw.ar(200, 0.1), FSinOsc.kr(XLine.kr(0.7, 300, 20), 0, 3600, 4000), 0.2) }.play;

(
{     var ctl = RHPF.kr(LFSaw.kr(2), SinOsc.kr(XLine.kr(0.07, 30, 20), 0, 35, 40), 0.05);
    SinOsc.ar(ctl * 200 + 500);
}.play;
)
```




