# BufFrames

*Current number of frames allocated in the buffer.*

**Related:** [BufChannels](../Classes/BufChannels.md), [BufDur](../Classes/BufDur.md), [BufRateScale](../Classes/BufRateScale.md), [BufSampleRate](../Classes/BufSampleRate.md), [BufSamples](../Classes/BufSamples.md)

**Categories:** UGens>Buffer>Info

## Description

Get the current number of allocated frames.


## Class Methods

### `kr`, `ir`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bufnum` | Buffer index. |  
**Returns:** the current number of allocated frames.> **⚠️ Warning:** The `.ir` method is not the safest choice. Since a buffer can be reallocated at any time, using `.ir` will not track the changes.
## Examples


```supercollider
b = Buffer.read(s, ExampleFiles.child);

// indexing with a phasor
{ BufRd.ar(1, b, Phasor.ar(0, BufRateScale.kr(b), 0, BufFrames.kr(b))) }.play;

// indexing by hand
{ BufRd.ar(1, b, K2A.ar(MouseX.kr(0, BufFrames.kr(b)))) }.play;

b.free
```




