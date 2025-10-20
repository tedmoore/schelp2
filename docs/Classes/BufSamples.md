# BufSamples

*Current number of samples in buffer.*

**Related:** [BufChannels](../Classes/BufChannels.md), [BufDur](../Classes/BufDur.md), [BufFrames](../Classes/BufFrames.md), [BufRateScale](../Classes/BufRateScale.md), [BufSampleRate](../Classes/BufSampleRate.md)

**Categories:** UGens>Buffer>Info

## Description

Returns the current number of allocated samples. A sample is not the same as a frame (compare with [BufFrames](../Classes/BufFrames.md)); a frame includes the samples in each channel of the buffer. Only for a mono buffer are samples the same as frames.

```
samples = frames * numChannels
```




## Class Methods


### `kr`, `ir`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bufnum` | Buffer index. |  
> **⚠️ Warning:** The `.ir` method is not the safest choice. Since a buffer can be reallocated at any time, using `.ir` will not track the changes.
## Examples


```
// example; this buffer is mono, so the number of samples matches the number of frames
b = Buffer.read(s, ExampleFiles.child);

// indexing with a phasor
{ BufRd.ar(1, b, Phasor.ar(0, BufRateScale.kr(b), 0, BufSamples.kr(b))) }.play;

// indexing by hand
{ BufRd.ar(1, b, K2A.ar(MouseX.kr(0, BufSamples.kr(b)))) }.play;

b.free;
```




