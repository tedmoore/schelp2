# Ringz

*Ringing filter.*

**Related:** [Formlet](../Classes/Formlet.md), [RHPF](../Classes/RHPF.md), [RLPF](../Classes/RLPF.md), [Resonz](../Classes/Resonz.md)

**Categories:** UGens>Filters>Linear

## Description

This is the same as [Resonz](../Classes/Resonz.md), except that it is a constant skirt gain filter, meaning that the peak gain depends on the value of Q. Also, instead of the resonance parameter in Resonz, the bandwidth is specified in a 60dB ring decay time. One Ringz is equivalent to one component of the [Klank](../Classes/Klank.md) UGen.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `freq` | Resonant frequency in Hertz. |  
| `decaytime` | The 60 dB decay time of the filter. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```
{ Ringz.ar(Dust.ar(3, 0.3), 2000, 2) }.play

{ Ringz.ar(WhiteNoise.ar(0.005), 2000, 0.5) }.play

// modulate frequency
{ Ringz.ar(WhiteNoise.ar(0.005), XLine.kr(100, 3000, 10), 0.5) }.play

{ Ringz.ar(Impulse.ar(6, 0, 0.3), XLine.kr(100, 3000, 10), 0.5) }.play

// modulate ring time
{ Ringz.ar(Impulse.ar(6, 0, 0.3), 2000, XLine.kr(4, 0.04, 8)) }.play

// modulate ring time opposite direction
{ Ringz.ar(Impulse.ar(6, 0, 0.3), 2000, XLine.kr(0.04, 4, 8)) }.play

(
{
    var exciter;
    exciter = WhiteNoise.ar(0.001);
    Mix.arFill(10, {
        Ringz.ar(exciter,
        XLine.kr(exprand(100.0, 5000.0), exprand(100.0, 5000.0), 20),
        0.5)
    })
}.play
)
```



## Interaction with sample rate
Ringz (and UGens that are based on it: [Klank](../Classes/Klank.md), [DynKlank](../Classes/DynKlank.md) and [Formlet](../Classes/Formlet.md)) are "sample-rate independent" with respect to *impulses* at the input. That is, given single-sample impulses, the output signal at different sample rates should be the same frequency and amplitude.

This design has a side effect: If the input is not made of impulses, the output amplitude is proportional to the sample rate.


```
(
a = {
    // rectangular pulse exciter (deterministic input)
    var exc = EnvGen.ar(Env([1, 1, 0], [0.01, 0], \lin)),
    sig = Ringz.ar(exc, 440, decaytime: 0.2),
    rms = sqrt(Integrator.ar(sig.squared) * (0.2 / SampleRate.ir)),
    end = DetectSilence.ar(sig, doneAction: 2);
    rms.poll(end);
    Silent.ar(1)
}.play;
)
```


At 44.1 kHz, this prints a RMS amplitude of 1.0758. At 88.2 kHz, the amplitude doubles.

Modal synthesis (simulating the vibrating modes of a struck surface) feeds a short, decaying burst of noise into Ringz-style resonators. This is a common use case that *is* subject to this amplitude effect.

If you will need the results to be compatible at different sample rates, make sure to scale the volume appropriately: if `sig` is the Ringz, Klank or Formlet signal, use `sig * (originalSampleRate / SampleRate.ir)` and substitute the right value in place of `originalSampleRate`.



