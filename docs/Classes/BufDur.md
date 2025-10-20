# BufDur

*Current duration of soundfile in buffer.*

**Related:** [BufChannels](../Classes/BufChannels.md), [BufFrames](../Classes/BufFrames.md), [BufRateScale](../Classes/BufRateScale.md), [BufSampleRate](../Classes/BufSampleRate.md), [BufSamples](../Classes/BufSamples.md)

**Categories:** UGens>Buffer>Info

## Description

Get the current duration of soundfile.


## Class Methods


### `kr`, `ir`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bufnum` | Buffer index. |  
**Returns:** the current duration.> **⚠️ Warning:** The `.ir` method is not the safest choice. Since a buffer can be reallocated at any time, using `.ir` will not track the changes.
## Examples


```
b = Buffer.read(s, ExampleFiles.child);

{ BufRd.ar(1, b, Sweep.ar(Impulse.ar(BufDur.kr(b).reciprocal), BufSampleRate.kr(b))) }.play;

b.free
```




