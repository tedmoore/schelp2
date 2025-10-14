# DC

*Create a constant amplitude signal*

**Related:** [LeakDC](../Classes/LeakDC.md)

**Categories:** UGens>Generators>Single-value

## Description

This UGen simply outputs the initial value you give it.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | constant value to output, cannot be modulated, set at initialisation time |  

## Examples


```supercollider
// won't work (the output is 0.5*0.0), which is why we need the DC UGen!
{ 0.5 }.play

// constantly zero
{ DC.ar(0.0) }.play;


// DC offset; will click on start and finish
{ DC.ar(0.5) + SinOsc.ar(440, 0, 0.1) }.play;


// test - note the transient before LeakDC adapts and suppresses the offset
{ LeakDC.ar(DC.ar(0.5)) }.play;


// show scope
s.scope
```




