# CuspN

*Cusp map chaotic generator*

**Categories:** UGens>Generators>Chaotic

**Related:** [CuspL](../Classes/CuspL.md)

## Description

A non-interpolating sound generator based on the difference equation:

sclang code translation:

```supercollider
(
var a = 1.0, b = 1.9, xi = 0, size = 64;
plot(size.collect { xi = a - (b * sqrt(abs(xi))) });
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
| `xi` | Initial value of x |  
| `mul` |  |  
| `add` |  |  

## Examples


```supercollider
// vary frequency
{ CuspN.ar(MouseX.kr(20, SampleRate.ir), 1.0, 1.99) * 0.3 }.play(s);

// mouse-controlled params
{ CuspN.ar(SampleRate.ir/4, MouseX.kr(0.9, 1.1, 1), MouseY.kr(1.8, 2, 1)) * 0.3 }.play(s);

// as a frequency control
{ SinOsc.ar(CuspN.ar(40, MouseX.kr(0.9, 1.1, 1), MouseY.kr(1.8, 2, 1))*800+900)*0.4 }.play(s);
```




