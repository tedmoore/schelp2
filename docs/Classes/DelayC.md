# DelayC

*Simple delay line with cubic interpolation.*

**Related:** [DelayL](../Classes/DelayL.md), [DelayN](../Classes/DelayN.md), [BufDelayC](../Classes/BufDelayC.md)

**Categories:** UGens>Delays

## Description

Simple delay line with cubic interpolation. See also [DelayN](../Classes/DelayN.md) which uses no interpolation, and [DelayL](../Classes/DelayL.md) which uses linear interpolation. Cubic interpolation is more computationally expensive than linear, but more accurate.
The term "delay" is often used in electronic music to refer to a delay line with feedback. If you are looking for that, try CombC.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `maxdelaytime` | The maximum delay time in seconds. used to initialize the delay buffer size. |  
| `delaytime` | Delay time in seconds. |  

> **Note:** DelayC needs at least 4 samples buffer. Therefore the minimum `maxdelaytime` and `delaytime` must be `SampleDur.ir * 4`.


## Examples


```
(
// Dust randomly triggers Decay to create an exponential
// decay envelope for the WhiteNoise input source
{
z = Decay.ar(Dust.ar(1, 0.5), 0.3, WhiteNoise.ar);
DelayC.ar(z, 0.2, 0.2, 1, z); // input is mixed with delay via the add input
}.play
)

(
// recursive application of delay.
{
z = Decay2.ar(Dust.ar(1, 0.5), 0.01, 0.1, Saw.ar(100 + [0, 1]));
5.do { |i| z = DelayC.ar(RLPF.ar(z, Rand(100, 3000), 0.03), 1, 1 / (2**i), 1, z * 0.5) };
z
}.play
)
```




