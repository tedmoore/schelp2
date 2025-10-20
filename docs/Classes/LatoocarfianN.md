# LatoocarfianN

*Latoocarfian chaotic generator*

**Categories:** UGens>Generators>Chaotic

**Related:** [LatoocarfianL](../Classes/LatoocarfianL.md), [LatoocarfianC](../Classes/LatoocarfianC.md)

## Description

A non-interpolating sound generator based on a function given in Clifford Pickover's book Chaos In Wonderland, pg 26. The function is:

According to Pickover, parameters `a` and `b` should be in the range from -3 to +3, and parameters `c` and `d` should be in the range from 0.5 to 1.5. The function can, depending on the parameters given, give continuous chaotic output, converge to a single value (silence) or oscillate in a cycle (tone).
sclang code translation:

```
(
var a = 1, b = 3, c = 0.5, d = 0.5, xi = 0.5, yi = 0.5, size = 64;
plot(size.collect { var x = xi;
xi = sin(b * yi) + (c * sin(b * xi));
yi = sin(a * x) + (d * sin(a * yi));
xi
});
)
```



> **Note:** This UGen is experimental and not optimized currently, so is rather hoggish of CPU.




## Class Methods


### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `freq` | Iteration frequency in Hertz |  
| `a` | Equation variable |  
| `b` | Equation variable |  
| `c` | Equation variable |  
| `d` | Equation variable |  
| `xi` | Initial value of x |  
| `yi` | Initial value of y |  
| `mul` |  |  
| `add` |  |  

## Examples


```
// default initial params
{ LatoocarfianN.ar(MouseX.kr(20, SampleRate.ir)) * 0.2 }.play(s);
```



```
// randomly modulate all params
(
{ LatoocarfianN.ar(
    SampleRate.ir/4,
    LFNoise2.kr(2, 1.5, 1.5),
    LFNoise2.kr(2, 1.5, 1.5),
    LFNoise2.kr(2, 0.5, 1.5),
    LFNoise2.kr(2, 0.5, 1.5)
) * 0.2 }.play(s);
)
```




