# SinOscFB

*Feedback FM oscillator*

**Related:** [SinOsc](../Classes/SinOsc.md), [FSinOsc](../Classes/FSinOsc.md), [PMOsc](../Classes/PMOsc.md)

**Categories:** UGens>Generators>Deterministic, UGens>Generators>Chaotic

## Description

SinOscFB is a sine oscillator that has phase modulation feedback; its output plugs back into the phase input. Basically this allows a modulation between a sine wave and a sawtooth like wave. Overmodulation causes chaotic oscillation. It may be useful if you want to simulate feedback FM synths.
Please note: The frequency of SinOscFB can be modulated at control rate. When trying to modulate the frequency of SinOscFB at audio rate, you will notice audible artefacts at higher frequency modulation frequencies. This is due to SinOscFB updating incoming frequency modulation values only once every control period (which is 64 samples long per default), instead of updating on every sample (like e.g. SinOsc).


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `freq` | The base frequency of the sine oscillator in Hertz. |  
| `feedback` | The second argument is the amplitude of phase feedback in radians. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output after any multiplication. |  

## Examples


```
{ SinOscFB.ar(440, MouseX.kr(0, 4))*0.1 }.play


{ SinOscFB.ar(MouseY.kr(10, 1000, 'exponential'), MouseX.kr(0.5pi, pi))*0.1 }.play


{ SinOscFB.ar(100*SinOscFB.ar(MouseY.kr(1, 1000, 'exponential'))+200, MouseX.kr(0.5pi, pi))*0.1 }.play


// Scope the wave form
{ SinOscFB.ar([400, 301], MouseX.kr(0, 4), 0.3) }.scope;
```




