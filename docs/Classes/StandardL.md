# StandardL

*Standard map chaotic generator*

**Categories:** UGens>Generators>Chaotic

**Related:** [StandardN](../Classes/StandardN.md)

## Description

A linear-interpolating sound generator based on the difference equations:

The standard map is an area preserving map of a cylinder discovered by the plasma physicist Boris Chirikov.
sclang code translation:

```
(
var k = 1, xi = 0.5, yi = 0, size = 64;
plot(size.collect { yi = yi + (k * sin(xi)) % 2pi; xi = (xi + yi) % 2pi; xi - pi * 0.3183098861837907 });
)
```




## Class Methods


### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `freq` | Iteration frequency in Hertz |  
| `k` | Perturbation amount |  
| `xi` | Initial value of x |  
| `yi` | Initial value of y |  

## Examples


```
// vary frequency
{ StandardL.ar(MouseX.kr(20, SampleRate.ir)) * 0.3 }.play(s);
```



```
// mouse-controlled param
{ StandardL.ar(SampleRate.ir/2, MouseX.kr(0.9, 4)) * 0.3 }.play(s);
```



```
// as a frequency control
{ SinOsc.ar(StandardL.ar(40, MouseX.kr(0.9, 4))*800+900)*0.4 }.play(s);
```




