# Delay2

*Two sample delay.*

**Related:** [Delay1](../Classes/Delay1.md), [TDelay](../Classes/TDelay.md)

**Categories:** UGens>Delays

## Description

Delays the input by two samples.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `mul` | The output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  
| `x1` | The sample directly preceding the delayed input signal, which is the second output sample. This can be a numeric value or a `UGen`. |  
| `x2` | The sample preceding the delayed input signal by two samples, which is the first output sample. This can be a numeric value or a `UGen`.
> **Note:** When running at audio rate, **x1** and **x2** default to `0.0`, i.e. "silence" precedes the delayed input. At control rate, the default values are set to the first sample of **in**, i.e. the first input sample is held during the delay. |  
The output sequence is:For audio-rate signals the delay is one audio frame, and for control-rate signals the delay is one control period.Why are the default values of **x1** and **x2** different depending on the `UGen`'s rate?At audio-rate, an analog delay model is followed—the input signal is preceded by silence (zeros). At control-rate, leading with zeros is less appropriate because control signals are often DC or other non zero-mean signals (e.g. a frequency or gain control signal).
## Examples


```supercollider
(
{
    var z = Dust.ar(1000);
    // [ original, subtract delayed from original ]
    [z, z - Delay2.ar(z)]
}.plot(0.01)
)

// Make a delayed sine wave continuous using the x1 and x2 arguments
(
{
    var freq = 1000;
    var phaseStep = 2pi * freq / s.sampleRate;
    var sine = SinOsc.ar(freq);
    [
        // default: silence before delay
        Delay2.ar(sine),
        // reconstruct predelay samples
        Delay2.ar(sine,
            x1: phaseStep.sin.neg,
            x2: (2 * phaseStep).sin.neg
        )
    ]
}.plot(0.001).plotMode_(\points)
)
```




