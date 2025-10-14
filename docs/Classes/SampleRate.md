# SampleRate

*Server sample rate.*

**Related:** [ControlRate](../Classes/ControlRate.md), [RadiansPerSample](../Classes/RadiansPerSample.md), [SampleDur](../Classes/SampleDur.md), [SubsampleOffset](../Classes/SubsampleOffset.md)

**Categories:** UGens>Info

## Description

Returns the current sample rate of the server.


## Class Methods

### `ir`

## Examples


```supercollider
// compares a 441 Hz sine tone derived from sample rate (44100 * 0.01, left)
// with a 440 Hz tone (right), resulting in a 1 Hz beating
(
{
    var freq;
    freq = [SampleRate.ir * 0.01, 440];
    SinOsc.ar(freq, 0, 0.1)
}.play;
)
```




