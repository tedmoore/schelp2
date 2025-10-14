# Pulse

*Band limited pulse wave.*

**Related:** [LFPulse](../Classes/LFPulse.md)

**Categories:** UGens>Generators>Deterministic

## Description

Band limited pulse wave generator with pulse width modulation.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `freq` | Frequency in Hertz. |  
| `width` | Pulse width ratio from zero to one. 0.5 makes a square wave. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```supercollider
// modulate frequency
{ Pulse.ar(XLine.kr(40, 4000, 6), 0.1, 0.2) }.play;

// modulate pulse width
{ Pulse.ar(200, SinOsc.kr(0.2).range(0.01, 0.99), 0.2) }.play;

// two band limited square waves thru a resonant low pass filter
{ RLPF.ar(Pulse.ar([100, 250], 0.5, 0.1), XLine.kr(8000, 400, 5), 0.05) }.play;
```




