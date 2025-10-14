# DelayL

*Simple delay line with linear interpolation.*

**Related:** [DelayC](../Classes/DelayC.md), [DelayN](../Classes/DelayN.md), [BufDelayL](../Classes/BufDelayL.md)

**Categories:** UGens>Delays

## Description

Simple delay line with linear interpolation. See also [DelayN](../Classes/DelayN.md) which uses no interpolation, and [DelayC](../Classes/DelayC.md) which uses cubic interpolation. Cubic interpolation is more computationally expensive than linear, but more accurate.
The term "delay" is often used in electronic music to refer to a delay line with feedback. If you are looking for that, try CombL.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `maxdelaytime` | The maximum delay time in seconds. used to initialize the delay buffer size. |  
| `delaytime` | Delay time in seconds. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```supercollider
(
// Dust randomly triggers Decay to create an exponential
// decay envelope for the WhiteNoise input source
{
z = Decay.ar(Dust.ar(1, 0.5), 0.3, WhiteNoise.ar);
DelayL.ar(z, 0.2, 0.2, 1, z); // input is mixed with delay via the add input
}.play
)

(
// recursive application of delay.
{
z = Decay2.ar(Dust.ar(1, 0.5), 0.01, 0.1, Saw.ar(100 + [0, 1]));
5.do { |i| z = DelayL.ar(RLPF.ar(z, Rand(100, 3000), 0.03), 1, 1 / (2**i), 1, z * 0.5) };
z
}.play
)
```




