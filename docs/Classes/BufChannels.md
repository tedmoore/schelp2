# BufChannels

*Current number of channels of soundfile in buffer.*

**Related:** [BufDur](../Classes/BufDur.md), [BufFrames](../Classes/BufFrames.md), [BufRateScale](../Classes/BufRateScale.md), [BufSampleRate](../Classes/BufSampleRate.md), [BufSamples](../Classes/BufSamples.md)

**Categories:** UGens>Buffer>Info

## Description

Get the current number of channels of soundfile.


## Class Methods

### `kr`, `ir`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bufnum` | Buffer index. |  
**Returns:** the current number of channels.> **⚠️ Warning:** The `.ir` method is not the safest choice. Since a buffer can be reallocated at any time, using `.ir` will not track the changes. Use `.kr` instead.

