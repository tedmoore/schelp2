# BufRateScale

*Buffer rate scaling in respect to server samplerate.*

**Related:** [BufChannels](../Classes/BufChannels.md), [BufDur](../Classes/BufDur.md), [BufFrames](../Classes/BufFrames.md), [BufSampleRate](../Classes/BufSampleRate.md), [BufSamples](../Classes/BufSamples.md)

**Categories:** UGens>Buffer>Info

## Description

Returns a ratio by which the playback of a soundfile is to be scaled.


## Class Methods


### `kr`, `ir`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bufnum` | Buffer index. |  
**Returns:** a ratio by which the playback of a soundfile is to be scaled.> **⚠️ Warning:** The `.ir` method is not the safest choice. Since a buffer can be reallocated at any time, using `.ir` will not track the changes.
## Examples


```
b = Buffer.read(s, ExampleFiles.child);

(
x = { |rate = 1|
    BufRd.ar(1, b, Phasor.ar(0, BufRateScale.kr(b) * rate, 0, BufFrames.kr(b)))
}.play;
)
```




