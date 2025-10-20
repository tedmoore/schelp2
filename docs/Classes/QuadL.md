# QuadL

*General quadratic map chaotic generator*

**Categories:** UGens>Generators>Chaotic

**Related:** [QuadC](../Classes/QuadC.md), [QuadN](../Classes/QuadN.md)

## Description

A linear-interpolating sound generator based on the difference equation:

sclang code translation:

```
(
var a = 1, b = -1, c = -0.75, xi = 0, size = 64;
plot(size.collect { xi = (a * (xi ** 2)) + (b * xi) + c; xi });
)
```




## Class Methods


### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `freq` | Iteration frequency in Hertz |  
| `a` | Equation variable |  
| `b` | Equation variable |  
| `c` | Equation variable |  
| `xi` | Initial value of x |  

## Examples


```
// default params
{ QuadL.ar(SampleRate.ir/4) * 0.2 }.play(s);
```



```
// logistic map
// equation: x1 = -r*x0^2 + r*x0
(
{ var r;
    r = MouseX.kr(3.5441, 4);    // stable range
    QuadL.ar(SampleRate.ir/4, r.neg, r, 0, 0.1) * 0.4;
}.play(s);
)
```



```
// logistic map as frequency control
(
{ var r;
    r = MouseX.kr(3.5441, 4);    // stable range
    SinOsc.ar(QuadL.ar(40, r.neg, r, 0, 0.1, 800, 900)) * 0.4;
}.play(s);
)
```




