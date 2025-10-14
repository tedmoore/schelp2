# StandardN

*Standard map chaotic generator*

**Categories:** UGens>Generators>Chaotic

**Related:** [StandardL](../Classes/StandardL.md)

## Description

A non-interpolating sound generator based on the difference equations:

The standard map is an area preserving map of a cylinder discovered by the plasma physicist Boris Chirikov.
sclang code translation:

```supercollider
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
| `mul` |  |  
| `add` |  |  

## Examples


```supercollider
// vary frequency
{ StandardN.ar(MouseX.kr(20, SampleRate.ir)) * 0.3 }.play(s);
```



```supercollider
// mouse-controlled param
{ StandardN.ar(SampleRate.ir/2, MouseX.kr(0.9, 4)) * 0.3 }.play(s);
```



```supercollider
// as a frequency control
{ SinOsc.ar(StandardN.ar(40, MouseX.kr(0.9, 4))*800+900)*0.4 }.play(s);
```




