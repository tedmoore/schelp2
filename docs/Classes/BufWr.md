# BufWr

*Buffer writing oscillator.*

**Related:** [BufRd](../Classes/BufRd.md)

**Categories:** UGens>Buffer

## Description

Write to a buffer at an index.

> **Note:** BufWr (in difference to [BufRd](../Classes/BufRd.md)) does not do multichannel expansion, because input is an array.




## Class Methods



### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `inputArray` | Input UGens (channelArray). |  
| `bufnum` | The index of the buffer to use. |  
| `phase` | Modulateable index into the buffer (has to be audio rate).> **⚠️ Warning:** The phase argument only offers precision for addressing 2**24 samples (about 6.3 minutes at 44100Hz) |  
| `loop` | 1 means true, 0 means false. This is modulateable. |  


## Instance Methods


## Examples


```
(
// allocate a buffer for writinig into
s = Server.local;
s.sendMsg("/b_alloc", 0, 44100 * 2);
)


// write into the buffer with a BufWr
(
y = { |rate = 1|
    var in;
    in = SinOsc.ar(LFNoise1.kr(2, 300, 400), 0, 0.1);
    BufWr.ar(in, 0, Phasor.ar(0, BufRateScale.kr(0) * rate, 0, BufFrames.kr(0)));
    0.0 // quiet
}.play;
)

// read it with a BufRd
(
x = { |rate = 1|
    BufRd.ar(1, 0, Phasor.ar(0, BufRateScale.kr(0) * rate, 0, BufFrames.kr(0)))
}.play(s);
)



x.set(\rate, 5);
y.set(\rate, 2.0.rand);
x.set(\rate, 2);
```




