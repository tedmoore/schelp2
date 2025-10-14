# BufDelayN

*Buffer based simple delay line with no interpolation.*

**Related:** [BufDelayC](../Classes/BufDelayC.md), [BufDelayL](../Classes/BufDelayL.md), [DelayN](../Classes/DelayN.md)

**Categories:** UGens>Delays>Buffer

## Description

Simple delay line with no interpolation which uses a buffer for its internal memory. See also [BufDelayL](../Classes/BufDelayL.md) which uses linear interpolation, and [BufDelayC](../Classes/BufDelayC.md) which uses cubic interpolation. Cubic interpolation is more computationally expensive than linear, but more accurate.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `buf` | Buffer number.
> **Note:** The buffers provided to any of the BufDelay units must be one channel. If you want to delay a multichannel signal, you must provide as many separate (one-channel) buffers as there are input channels. |  
| `in` | The input signal. |  
| `delaytime` | Delay time in seconds. |  
| `mul` |  |  
| `add` |  |  
> **⚠️ Warning:** For reasons of efficiency, the effective buffer size is limited to the previous power of two. So, if 44100 samples are allocated, the maximum delay would be 32768 samples.
## Examples


```supercollider
// allocate buffer
b = Buffer.alloc(s, 44100, 1);

(
// Dust randomly triggers Decay to create an exponential
// decay envelope for the WhiteNoise input source
{
z = Decay.ar(Dust.ar(1, 0.5), 0.3, WhiteNoise.ar);
BufDelayN.ar(b.bufnum, z, 0.2, 1, z); // input is mixed with delay via the add input
}.play
)

b.free;


// multichannel

// two channels, two buffers
b = Buffer.allocConsecutive(2, s, 32768, 1);

a = { |bufs = #[0, 1]|
    var sig = SinOsc.ar([440, 880]) * Decay2.kr(Impulse.kr([2, 4]), 0.01, 0.15);
    sig + BufDelayN.ar(bufs, sig, delaytime: 0.125)
}.play(args: [bufs: b]);

a.free;
b.do(_.free);
```




