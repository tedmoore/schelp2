# MultiTap

*Multiple tap delay.*

**Related:** [Tap](../Classes/Tap.md)

**Categories:** UGens>Buffer, UGens>Delays>Buffer

## Description

This is a wrapper which creates a multiple tap delay line using [RecordBuf](../Classes/RecordBuf.md) and [PlayBuf](../Classes/PlayBuf.md) .

> **Note:** `RecordBuf.ar` and `PlayBuf.ar` operate block by block. If a delay time is greater than the buffer size minus the server's block size, the write and read heads might interfere in unintended ways. Use a slightly larger buffer if this happens.




## Class Methods

### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `timesArray` | A Ref to an Array of delay times in seconds. |  
| `levelsArray` | A Ref to an Array of amplitudes. |  
| `in` | The input signal. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  
| `bufnum` | The number of the buffer to use for the delay. This must be at least as long as the longest tap time. |  

## Examples


```supercollider
s.boot;
b = Buffer.alloc(s, s.sampleRate);
(
{
    MultiTap.ar(`[0.1, 0.2, 0.3, 0.4], `[0.1, 0.2, 0.4, 0.8],
        Decay.ar(Dust.ar(2), 0.1, PinkNoise.ar), bufnum: b.bufnum)
}.play
)
```




