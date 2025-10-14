# Integrator

*A leaky integrator.*

**Categories:** UGens>Filters>Linear, UGens>Maths

## Description

Integrates an input signal with a leak. The formula implemented is:

```supercollider
out(0) = in(0) + (coef * out(-1))
```




## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `coef` | Leak coefficient. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```supercollider
{ Integrator.ar(LFPulse.ar(300, 0.2, 0.1), MouseX.kr(0.001, 0.999, 1)) }.play

// used as an envelope
{ Integrator.ar(LFPulse.ar(3, 0.2, 0.0004), 0.999, FSinOsc.ar(700), 0) }.play


// scope

{ Integrator.ar(LFPulse.ar(1500 / 4, 0.2, 0.1), MouseX.kr(0.01, 0.999, 1)) }.scope
```




