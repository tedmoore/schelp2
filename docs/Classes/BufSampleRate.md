# BufSampleRate

*Buffer sample rate.*

**Related:** [BufChannels](../Classes/BufChannels.md), [BufDur](../Classes/BufDur.md), [BufFrames](../Classes/BufFrames.md), [BufRateScale](../Classes/BufRateScale.md), [BufSamples](../Classes/BufSamples.md)

**Categories:** UGens>Buffer>Info

## Description

Returns the buffer's current sample rate.


## Class Methods

### `kr`, `ir`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bufnum` | Buffer index. |  
**Returns:** the buffer's current sample rate.> **⚠️ Warning:** The `.ir` method is not the safest choice. Since a buffer can be reallocated at any time, using `.ir` will not track the changes.
## Examples


```supercollider
b = Buffer.read(s, ExampleFiles.child);

// compares a 1102.5 Hz sine tone (11025 * 0.1, left) with a 1100 Hz tone (right)
// the apollo sample has a sample rate of 11.025 kHz
(
{
    var freq;
    freq = [BufSampleRate.kr(b) * 0.1, 1100];
    SinOsc.ar(freq, 0, 0.1)
}.play;
)

b.free;
```




