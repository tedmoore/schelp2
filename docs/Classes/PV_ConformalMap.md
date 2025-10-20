# PV_ConformalMap

*Complex plane attack.*

**Related:** [FFT](../Classes/FFT.md), [IFFT](../Classes/IFFT.md)

**Categories:** UGens>FFT

## Description

Applies the conformal mapping

```
z → (z - a) / (1 - za*)
```


to the phase vocoder bins z with a given by the real and imag inputs to the UGen.
Makes a transformation of the complex plane so the output is full of phase vocoder artifacts but may be musically fun. Usually keep

```
|a| < 1
```


but you can of course try bigger values to make it really noisy.

```
a = 0
```


should give back the input mostly unperturbed.
See [http://mathworld.wolfram.com/ConformalMapping.html](http://mathworld.wolfram.com/ConformalMapping.html) .


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `buffer` | FFT buffer. |  
| `areal` | Real part of a. |  
| `aimag` | Imaginary part of a. |  

## Examples


```
// explore the effect

(
SynthDef("conformer2", { |out|
    var in, chain, sound;
    in = Mix.ar(LFSaw.ar(SinOsc.kr(Array.rand(3, 0.1, 0.5), 0, 10, [1, 1.1, 1.5, 1.78, 2.45, 6.7]*220), 0, 0.3));
    chain = FFT(LocalBuf(2048), in);
    chain = PV_ConformalMap(chain, MouseX.kr(0.01, 2.0, 'exponential'), MouseY.kr(0.01, 10.0, 'exponential'));
    sound = IFFT(chain);

    Out.ar(out, Pan2.ar(CombN.ar(sound, 0.1, 0.1, 10, 0.5, sound), 0, 0.3));
}).add;
)

a = Synth("conformer2")
a.free

// sound input: use headphones to prevent feedback
(
SynthDef("conformer1", { |out|
    var in, chain;
    in = SoundIn.ar(0, 0.5);
    chain = FFT(LocalBuf(1024), in);
    chain = PV_ConformalMap(chain, MouseX.kr(-1.0, 1.0), MouseY.kr(-1.0, 1.0));
    Out.ar(out, Pan2.ar(IFFT(chain), 0));
}).add;
)

a = Synth("conformer1")
a.free
```




