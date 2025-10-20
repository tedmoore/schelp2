# PV_JensenAndersen

*FFT feature detector for onset detection.*

**Related:** [PV_HainsworthFoote](../Classes/PV_HainsworthFoote.md)

**Categories:** UGens>FFT

## Description

FFT feature detector for onset detection based on work described in *Jensen, K. & Andersen, T. H. (2003). Real-time Beat Estimation Using Feature Extraction. In Proceedings of the Computer Music Modeling and Retrieval Symposium, Lecture Notes in Computer Science. Springer Verlag.*
First order derivatives of the features are taken. `threshold` may need to be set low to pick up on changes.


## Class Methods



### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `buffer` | FFT buffer. |  
| `propsc` | Proportion of spectral centroid feature. |  
| `prophfe` | Proportion of high frequency energy feature. |  
| `prophfc` | Proportion of high frequency content feature. |  
| `propsf` | Proportion of spectral flux feature. |  
| `threshold` | Threshold level for allowing a detection. |  
| `waittime` | If triggered, minimum wait until a further frame can cause another spot (useful to stop multiple detects on heavy signals). |  

## Examples


```
(
SynthDef(\fftod, { |out|
    var source1, detect, chain;
    source1 = SoundIn.ar(0);
    chain = FFT(LocalBuf(2048), source1);
    detect = PV_JensenAndersen.ar(chain, threshold: MouseX.kr(0.1, 1.0));
    Out.ar(out, SinOsc.ar([440, 445], 0, Decay.ar(0.1 * detect, 0.1)));
}).play(s);
)
```




