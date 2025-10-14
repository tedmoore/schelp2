# BufAllpassN

*Buffer based all pass delay line with no interpolation.*

**Related:** [BufAllpassC](../Classes/BufAllpassC.md), [BufAllpassL](../Classes/BufAllpassL.md), [AllpassN](../Classes/AllpassN.md)

**Categories:** UGens>Delays>Buffer

## Description

All pass delay line with no interpolation which uses a buffer for its internal memory. See also [BufAllpassC](../Classes/BufAllpassC.md) which uses cubic interpolation, and which [BufAllpassL](../Classes/BufAllpassL.md) uses linear interpolation. Cubic interpolation is more computationally expensive than linear, but more accurate.


## Class Methods

### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `buf` | Buffer number. |  
| `in` | The input signal. |  
| `delaytime` | Delay time in seconds. |  
| `decaytime` | Time for the echoes to decay by 60 decibels. If this time is negative then the feedback coefficient will be negative, thus emphasizing only odd harmonics at an octave lower. |  
> **⚠️ Warning:** For reasons of efficiency, the effective buffer size is limited to the previous power of two. So, if 44100 samples are allocated, the maximum delay would be 32768 samples.
## Examples


```supercollider
// allocate buffer
b = Buffer.alloc(s, 44100, 1);

// Since the allpass delay has no audible effect as a resonator on
// steady state sound ...

{ BufAllpassC.ar(b.bufnum, WhiteNoise.ar(0.1), XLine.kr(0.0001, 0.01, 20), 0.2) }.play;

// ...these examples add the input to the effected sound and compare variants so that you can hear
// the effect of the phase comb:

(
{
    z = WhiteNoise.ar(0.2);
    z + BufAllpassN.ar(b.bufnum, z, XLine.kr(0.0001, 0.01, 20), 0.2)
}.play)

(
{
    z = WhiteNoise.ar(0.2);
    z + BufAllpassL.ar(b.bufnum, z, XLine.kr(0.0001, 0.01, 20), 0.2)
}.play)

(
{
    z = WhiteNoise.ar(0.2);
    z + BufAllpassC.ar(b.bufnum, z, XLine.kr(0.0001, 0.01, 20), 0.2)
}.play)

// used as an echo - doesn't really sound different than Comb,
// but it outputs the input signal immediately (inverted) and the echoes
// are lower in amplitude.
{ BufAllpassN.ar(b.bufnum, Decay.ar(Dust.ar(1, 0.5), 0.2, WhiteNoise.ar), 0.2, 3) }.play;
```




