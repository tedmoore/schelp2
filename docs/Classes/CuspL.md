# CuspL

*Cusp map chaotic generator*

**Categories:** UGens>Generators>Chaotic

**Related:** [CuspN](../Classes/CuspN.md)

## Description

A linear-interpolating sound generator based on the difference equation:

sclang code translation:

```
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

## Examples


```
// vary frequency
{ CuspL.ar(MouseX.kr(20, SampleRate.ir), 1.0, 1.99) * 0.3 }.play(s);

// mouse-controlled params
{ CuspL.ar(SampleRate.ir/4, MouseX.kr(0.9, 1.1, 1), MouseY.kr(1.8, 2, 1)) * 0.3 }.play(s);

// as a frequency control
{ SinOsc.ar(CuspL.ar(40, MouseX.kr(0.9, 1.1, 1), MouseY.kr(1.8, 2, 1))*800+900)*0.4 }.play(s);
```




