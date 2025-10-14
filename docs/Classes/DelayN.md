# DelayN

*Simple delay line with no interpolation.*

**Related:** [Delay1](../Classes/Delay1.md), [Delay2](../Classes/Delay2.md), [DelayC](../Classes/DelayC.md), [DelayL](../Classes/DelayL.md), [BufDelayN](../Classes/BufDelayN.md)

**Categories:** UGens>Delays

## Description

Simple delay line with no interpolation. See also [DelayL](../Classes/DelayL.md) which uses linear interpolation, and [DelayC](../Classes/DelayC.md) which uses cubic interpolation.
This UGen will create aliasing artifacts if you modulate the delay time, which is also quantized to the nearest sample period. If these are undesirable properties, use DelayL or DelayC. But if your delay time is fixed and sub-sample accuracy is not needed, this is the most CPU-efficient choice with no loss in quality.
The term "delay" is often used in electronic music to refer to a delay line with feedback. If you are looking for that, try CombN.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `maxdelaytime` | The maximum delay time in seconds, used to initialize the delay buffer size. |  
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
DelayN.ar(z, 0.2, 0.2, 1, z); // input is mixed with delay via the add input
}.play
)

(
// recursive application of delay.
{
z = Decay2.ar(Dust.ar(1, 0.5), 0.01, 0.1, Saw.ar(100 + [0, 1]));
5.do { |i| z = DelayN.ar(RLPF.ar(z, Rand(100, 3000), 0.03), 1, 1 / (2**i), 1, z * 0.5) };
z
}.play
)
```




