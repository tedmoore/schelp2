# Compander

*Compressor, expander, limiter, gate, ducker*

**Categories:** UGens>Dynamics

**Related:** [Normalizer](../Classes/Normalizer.md), [CompanderD](../Classes/CompanderD.md), [Limiter](../Classes/Limiter.md)

## Description

General purpose (hard-knee) dynamics processor.


## Class Methods


### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The signal to be compressed / expanded / gated. |  
| `control` | The signal whose amplitude determines the gain applied to the input signal. Often the same as in (for standard gating or compression) but should be different for ducking. |  
| `thresh` | Usually between 0 and 1. Amplitude threshold of the control signal, which determines the break point between slopeBelow and slopeAbove. The control signal amplitude is calculated using RMS. |  
| `slopeBelow` | Slope of applied amplitude curve if control signal amplitude is below `thresh`. If > 1.0, the amplitude drops off more quickly the softer the control signal gets; when the control signal is close to 0 amplitude, the output should be exactly zero -- hence, noise gating. Values < 1.0 are possible, but it means that a very low-level control signal will cause the input signal to be amplified, which would raise the noise floor. |  
| `slopeAbove` | Slope of applied amplitude curve if control signal amplitude is above `thresh`. Values < 1.0 achieve compression (louder signals are attenuated) whereas values > 1.0 expand (louder signals are made even louder). A value of `1/3` achieves a 3:1 compression. |  
| `clampTime` | time (in seconds) it takes for the amplitude adjustment to kick in fully after the control signal is above `thresh`. Usually a small value around 10ms (0.01), often set as low as 2ms (0.002). |  
| `relaxTime` | time (in seconds) for the amplitude adjustment to be released (control signal below `thresh`). Usually longer than `clampTime`; depending on the input and control signal, setting both times too short results in (possibly unwanted) artifacts. |  
| `mul` | output is multiplied by this value. |  
| `add` | value added to the output. |  
See for example [http://en.wikipedia.org/wiki/Audio_level_compression](http://en.wikipedia.org/wiki/Audio_level_compression) for a more in-depth explanation.
## Examples

Clean signal (for reference)

```
(
{
    Decay2.ar(
        Impulse.ar(8, 0, LFSaw.kr(0.3, 1, -0.3, 0.3)),
        0.001,
        0.3
    )
    * Mix.ar(Pulse.ar([80, 81], 0.3))
}.play;
)
```


Noise gate

```
(
{
    var z;

    // signal (clean)
    z = Decay2.ar(
        Impulse.ar(8, 0, LFSaw.kr(0.3, 1, -0.3, 0.3)),
        0.001,
        0.3
    )
    * Mix.ar(Pulse.ar([80, 81], 0.3));

    // apply gate (mouse x sets treshold)
    Compander.ar(z, z,
        thresh: MouseX.kr(0.001, 1),
        slopeBelow: 10,
        slopeAbove:  1,
        clampTime:   0.01,
        relaxTime:   0.01
    )
}.play;
)
```


Compressor

```
(
{
    var z;

    // signal (clean)
    z = Decay2.ar(
        Impulse.ar(8, 0, LFSaw.kr(0.3, 1, -0.3, 0.3)),
        0.001,
        0.3
    )
    * Mix.ar(Pulse.ar([80, 81], 0.3));

    // apply compression  (mouse x sets amount)
    Compander.ar(z, z,
        thresh: MouseX.kr(0.01, 1),
        slopeBelow: 1,
        slopeAbove: 0.5,
        clampTime:  0.01,
        relaxTime:  0.01
    )
}.play;
)
```


Limiter

```
(
{
    var z;

    // signal (clean)
    z = Decay2.ar(
        Impulse.ar(8, 0, LFSaw.kr(0.3, 1, -0.3, 0.3)),
        0.001,
        0.3
    )
    * Mix.ar(Pulse.ar([80, 81], 0.3));


    // apply limiter (mouse x sets amount)
    Compander.ar(z, z,
        thresh: MouseX.kr(0.01, 1),
        slopeBelow: 1,
        slopeAbove: 0.1,
        clampTime:  0.01,
        relaxTime:  0.01
    )
}.play;
)
```


Sustainer

```
(
// note the pops at the beginning of signal due to lack of lookahead
{
    var z;

    // signal (clean)
    z = Decay2.ar(
        Impulse.ar(8, 0, LFSaw.kr(0.3, 1, -0.3, 0.3)),
        0.001,
        0.3
    )
    * Mix.ar(Pulse.ar([80, 81], 0.3));

    // apply sustainer
    Compander.ar(z, z,
        thresh: MouseX.kr(0.1, 1),
        slopeBelow: 0.1,
        slopeAbove: 1,
        clampTime:  0.01,
        relaxTime:  0.01
    ) * 0.1
}.play;
)
```




