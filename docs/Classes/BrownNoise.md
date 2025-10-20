# BrownNoise

*Brown Noise.*

**Related:** [ClipNoise](../Classes/ClipNoise.md), [GrayNoise](../Classes/GrayNoise.md), [PinkNoise](../Classes/PinkNoise.md), [WhiteNoise](../Classes/WhiteNoise.md)

**Categories:** UGens>Generators>Stochastic

## Description

Generates noise whose spectrum falls off in power by 6 dB per octave.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples

compare:

```
{ BrownNoise.ar(0.1) }.play;
{ WhiteNoise.ar(0.1) }.play;
```


brownian noise as a frequency modulator:

```
{ SinOsc.ar(BrownNoise.ar(100, 200)) * 0.1 }.play;
```


filtered brown noise:

```
{ BPF.ar(BrownNoise.ar(0.1.dup), MouseX.kr(40, 17000, 1), 0.2) }.play;
```




