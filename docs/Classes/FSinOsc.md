# FSinOsc

*Fast sine oscillator.*

**Related:** [SinOsc](../Classes/SinOsc.md), [SinOscFB](../Classes/SinOscFB.md)

**Categories:** UGens>Generators>Deterministic

## Description

Very fast sine wave generator (2 PowerPC instructions per output sample!) implemented using a ringing filter. This generates a much cleaner sine wave than a table lookup oscillator and is a lot faster. However, the amplitude of the wave will vary with frequency. Generally the amplitude will go down as you raise the frequency and go up as you lower the frequency.
> **⚠️ Warning:** In the current implementation, the amplitude can blow up if the frequency is modulated by certain alternating signals.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `freq` | Frequency in Hertz.
> **Note:** While an audio-rate frequency input is accepted, frequency is is currently only updated internally at only control-rate. |  
| `iphase` | Initial phase offset. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```
{ FSinOsc.ar(800) * 0.2 }.play;

{ FSinOsc.ar(XLine.kr(200, 4000, 1)) * 0.2 }.play;

// loses amplitude towards the end
{ FSinOsc.ar(FSinOsc.ar(XLine.kr(4, 401, 8), 0.0, 200, 800)) * 0.2 }.play;
```




