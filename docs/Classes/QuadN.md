# QuadN

*General quadratic map chaotic generator*

**Categories:** UGens>Generators>Chaotic

**Related:** [QuadL](../Classes/QuadL.md), [QuadC](../Classes/QuadC.md)

## Description

A non-interpolating sound generator based on the difference equation:

sclang code translation:

```supercollider
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
| `mul` |  |  
| `add` |  |  

## Examples


```supercollider
// default params
{ QuadN.ar(SampleRate.ir/4) * 0.2 }.play(s);
```



```supercollider
// logistic map
// equation: x1 = -r*x0^2 + r*x0
(
{ var r;
    r = MouseX.kr(3.5441, 4);    // stable range
    QuadN.ar(SampleRate.ir/4, r.neg, r, 0, 0.1) * 0.4;
}.play(s);
)
```



```supercollider
// logistic map as frequency control
(
{ var r;
    r = MouseX.kr(3.5441, 4);    // stable range
    SinOsc.ar(QuadN.ar(40, r.neg, r, 0, 0.1, 800, 900)) * 0.4;
}.play(s);
)
```




