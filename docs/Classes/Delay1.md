# Delay1

*Single sample delay.*

**Related:** [Delay2](../Classes/Delay2.md), [TDelay](../Classes/TDelay.md)

**Categories:** UGens>Delays

## Description

Delays the input by one audio frame or control period.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `mul` | The output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  
| `x1` | The sample value preceding the delayed input, which is the value of the first output sample. This can be a numeric value or a `UGen`.
> **Note:** When running at audio rate, **x1** defaults to `0.0`, i.e. "silence" precedes the delayed input. At control rate, the default value is set to the first sample of **in**, i.e. the first input sample is held during the delay. |  
The output sequence is:For audio-rate signals the delay is one audio frame, and for control-rate signals the delay is one control period.Why is the default value of **x1** different depending on the `UGen`'s rate?At audio-rate, an analog delay model is followed—the input signal is preceded by silence (zero). At control-rate, leading with a zero is less appropriate because control signals are often DC or other non zero-mean signals (e.g. a frequency or gain control signal).
## Examples


```
// Create bipolar Dust
(
{
    var z = Dust.ar(1500);
    // [original, subtract delayed from original]
    [z, z - Delay1.ar(z)]
}.plot(0.01)
)

// Make a delayed sine wave continuous using the x1 argument
(
{
    var freq = 1000;
    var phaseStep = 2pi * freq / s.sampleRate;
    var sine = SinOsc.ar(freq);
    [
        // default: silence before delay
        Delay1.ar(sine),
        // reconstruct predelay sample
        Delay1.ar(sine, x1: phaseStep.sin.neg)
    ]
}.plot(0.001).plotMode_(\points)
)
```




