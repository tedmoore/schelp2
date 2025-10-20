# LinCongC

*Linear congruential chaotic generator*

**Categories:** UGens>Generators>Chaotic

**Related:** [LinCongN](../Classes/LinCongN.md), [LinCongL](../Classes/LinCongL.md)

## Description

A cubic-interpolating sound generator based on the difference equation:

The output signal is automatically scaled to a range of [-1, 1].
sclang code translation:

```
(
var a = 1.1, c = 0.13, m = 1, xi = 0, size = 64;
plot(size.collect { xi = (a * xi + c) % m });
)
```




## Class Methods


### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `freq` | Iteration frequency in Hertz |  
| `a` | Multiplier amount |  
| `c` | Increment amount |  
| `m` | Modulus amount |  
| `xi` | Initial value of x |  

## Examples


```
// default initial params
{ LinCongC.ar(MouseX.kr(20, SampleRate.ir)) * 0.2 }.play(s);
```



```
// randomly modulate params
(
{ LinCongC.ar(
    LFNoise2.kr(1, 1e4, 1e4),
    LFNoise2.kr(0.1, 0.5, 1.4),
    LFNoise2.kr(0.1, 0.1, 0.1),
    LFNoise2.kr(0.1)
) * 0.2 }.play(s);
)
```



```
// as frequency control...
(
{
SinOsc.ar(
    LinCongC.ar(
        40,
        LFNoise2.kr(0.1, 0.1, 1),
        LFNoise2.kr(0.1, 0.1, 0.1),
        LFNoise2.kr(0.1),
        0, 500, 600
    )
) * 0.4 }.play(s);
)
```




