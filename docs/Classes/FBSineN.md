# FBSineN

*Feedback sine with chaotic phase indexing*

**Categories:** UGens>Generators>Chaotic

**Related:** [FBSineL](../Classes/FBSineL.md), [FBSineC](../Classes/FBSineC.md)

## Description

A non-interpolating sound generator based on the difference equations:

This uses a linear congruential function to drive the phase indexing of a sine wave. For `im = 1`, `fb = 0`, and `a = 1` a normal sinewave results.
sclang code translation:

```
(
var im = 1, fb = 0.1, a = 1.1, c = 0.5, xi = 0.1, yi = 0.1, size = 64;
plot(size.collect { xi = sin((im * yi) + (fb * xi)); yi = (a * yi + c) % 2pi; xi });
)
```




## Class Methods


### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `freq` | Iteration frequency in Hertz |  
| `im` | Index multiplier amount |  
| `fb` | Feedback amount |  
| `a` | Phase multiplier amount |  
| `c` | Phase increment amount |  
| `xi` | Initial value of x |  
| `yi` | Initial value of y |  
| `mul` |  |  
| `add` |  |  

## Examples


```
// default initial params
{ FBSineN.ar(SampleRate.ir/4) * 0.2 }.play(s);
```



```
// increase feedback
{ FBSineN.ar(SampleRate.ir, 1, Line.kr(0.01, 4, 10), 1, 0.1) * 0.2 }.play(s);
```



```
// increase phase multiplier
{ FBSineN.ar(SampleRate.ir, 1, 0, XLine.kr(1, 2, 10), 0.1) * 0.2 }.play(s);
```



```
// modulate frequency and index multiplier
{ FBSineN.ar(LFNoise2.kr(1, 1e4, 1e4), LFNoise2.kr(1, 16, 17), 1, 1.005, 0.7) * 0.2 }.play(s);
```



```
// randomly modulate params
(
{ FBSineN.ar(
    LFNoise2.kr(1, 1e4, 1e4),
    LFNoise2.kr(1, 32, 33),
    LFNoise2.kr(1, 0.5),
    LFNoise2.kr(1, 0.05, 1.05),
    LFNoise2.kr(1, 0.3, 0.3)
) * 0.2 }.play(s);
)
```




