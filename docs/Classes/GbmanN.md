# GbmanN

*Gingerbreadman map chaotic generator*

**Categories:** UGens>Generators>Chaotic

**Related:** [GbmanL](../Classes/GbmanL.md)

## Description

A non-interpolating sound generator based on the difference equations:

The behavior of the system is only dependent on its initial conditions.
sclang code translation:

```supercollider
(
var xi = 1.2, yi = 2.1, size = 64;
plot(size.collect { var x; xi = 1 - yi + abs(x = xi); yi = x; xi });
)
```


Reference: *Devaney, R. L. "The Gingerbreadman." Algorithm 3, 15-16, Jan. 1992.*


## Class Methods

### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `freq` | Iteration frequency in Hertz |  
| `xi` | Initial value of x |  
| `yi` | Initial value of y |  
| `mul` |  |  
| `add` |  |  

## Examples


```supercollider
// default initial params
{ GbmanN.ar(MouseX.kr(20, SampleRate.ir)) * 0.1 }.play(s);

// change initial params
{ GbmanN.ar(MouseX.kr(20, SampleRate.ir), -0.7, -2.7) * 0.1 }.play(s);

// wait for it...
{ GbmanN.ar(MouseX.kr(20, SampleRate.ir), 1.2, 2.0002) * 0.1 }.play(s);

// as a frequency control
{ SinOsc.ar(GbmanN.ar(40)*400+500)*0.4 }.play(s);
```




