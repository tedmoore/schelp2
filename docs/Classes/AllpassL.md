# AllpassL

*Schroeder allpass delay line with linear interpolation.*

**Related:** [AllpassC](../Classes/AllpassC.md), [AllpassN](../Classes/AllpassN.md), [BufAllpassL](../Classes/BufAllpassL.md)

**Categories:** UGens>Delays

## Description

A Schroeder allpass filter is given by the difference equations

```supercollider
s(t) = x(t) + k * s(t - D)
y(t) = -k * s(t) + s(t - D)
```


where `x(t)` is the input signal, `y(t)` is the output signal, `D` is the delay time, and `k` is the allpass coefficient.
In this UGen, `k` is computed as `k == 0.001 ** (delay / decay.abs) * decay.sign` (0.001 is -60 dBFS).
See also [AllpassN](../Classes/AllpassN.md) which uses no interpolation, and [AllpassC](../Classes/AllpassC.md) which uses cubic interpolation. Cubic interpolation is more computationally expensive than linear, but more accurate.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `maxdelaytime` | The maximum delay time in seconds. Used to initialize the delay buffer size. |  
| `delaytime` | Delay time in seconds. |  
| `decaytime` | Time for the echoes to decay by 60 decibels. If this time is negative then the feedback coefficient will be negative, thus emphasizing only odd harmonics at an octave lower. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```supercollider
// Since the allpass delay has no audible effect as a resonator on
// steady state sound ...

{ AllpassL.ar(WhiteNoise.ar(0.1), 0.01, XLine.kr(0.0001, 0.01, 20), 0.2) }.play;

// ...these examples add the input to the effected sound and compare variants so that you can hear
// the effect of the phase comb:

(
{
    z = WhiteNoise.ar(0.2);
    z + AllpassN.ar(z, 0.01, XLine.kr(0.0001, 0.01, 20), 0.2)
}.play)

(
{
    z = WhiteNoise.ar(0.2);
    z + AllpassL.ar(z, 0.01, XLine.kr(0.0001, 0.01, 20), 0.2)
}.play)

(
{
    z = WhiteNoise.ar(0.2);
    z + AllpassC.ar(z, 0.01, XLine.kr(0.0001, 0.01, 20), 0.2)
}.play)

// used as an echo - doesn't really sound different than Comb,
// but it outputs the input signal immediately (inverted) and the echoes
// are lower in amplitude.
{ AllpassL.ar(Decay.ar(Dust.ar(1, 0.5), 0.2, WhiteNoise.ar), 0.2, 0.2, 3) }.play;
```




