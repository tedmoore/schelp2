# K2A

*Control to audio rate converter.*

**Related:** [A2K](../Classes/A2K.md)

**Categories:** UGens>Conversion

## Description

To be able to play a control rate UGen into an audio rate UGen, sometimes the rate must be converted. K2A converts via linear interpolation.


## Class Methods

### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  

## Examples


```supercollider
{ K2A.ar(WhiteNoise.kr(0.3)) }.scope;


// compare:
(
{
    [
        K2A.ar(WhiteNoise.kr(0.3)),
        WhiteNoise.ar(0.3)
    ]
}.scope;
)

(
{
    var freq, blockSize, sampleRate;
    blockSize = s.options.blockSize; // usually 64
    sampleRate = s.sampleRate;
    freq = MouseX.kr(0.1, 40, 1) / blockSize * sampleRate;
    [
        K2A.ar(LFNoise0.kr(freq)),
        LFNoise0.ar(freq)
    ] * 0.3
}.scope;
)
```




