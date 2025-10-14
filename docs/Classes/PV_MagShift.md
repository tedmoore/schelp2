# PV_MagShift

*shift and stretch magnitude bin position.*

**Related:** [FFT](../Classes/FFT.md), [IFFT](../Classes/IFFT.md), [PV_BinShift](../Classes/PV_BinShift.md)

**Categories:** UGens>FFT

## Description

Shift and stretch the positions of only the magnitude of the bins. Can be used as a very crude frequency shifter/scaler.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `buffer` | FFT buffer. |  
| `stretch` | Scale bin location by factor. |  
| `shift` | Add an offset to bin position. |  

## Examples


```supercollider
s.boot;
b = Buffer.read(s, ExampleFiles.child);

(
SynthDef("help-magStretch", { |out = 0, bufnum = 0|
    var in, chain;
    in = LFSaw.ar(200, 0, 0.2);
    chain = FFT(LocalBuf(2048), in);
    chain = PV_MagShift(chain, MouseX.kr(0.25, 4, \exponential));
    Out.ar(out, 0.1 * IFFT(chain).dup);
}).play(s);
)

(
SynthDef("help-magStretch2", { |out = 0, soundBufnum = 2|
    var in, chain;
    in = PlayBuf.ar(1, soundBufnum, BufRateScale.kr(soundBufnum), loop: 1);
    chain = FFT(LocalBuf(2048), in);
    chain = PV_MagShift(chain, MouseX.kr(0.25, 4, \exponential));
    Out.ar(out, 0.1 * IFFT(chain).dup);
}).play(s, [\soundBufnum, b]);
)

(
SynthDef("help-magShift", { |out = 0|
    var in, chain;
    in = LFSaw.ar(200, 0, 0.2);
    chain = FFT(LocalBuf(2048), in);
    chain = PV_MagShift(chain, 1, MouseX.kr(-128, 128));
    Out.ar(out, 0.1 * IFFT(chain).dup);
}).play(s);
)

(
SynthDef("help-magShift2", { |out = 0, soundBufnum = 2|
    var in, chain;
    in = PlayBuf.ar(1, soundBufnum, BufRateScale.kr(soundBufnum), loop: 1);
    chain = FFT(LocalBuf(2048), in);
    chain = PV_MagShift(chain, 1, MouseX.kr(-128, 128));
    Out.ar(out, 0.1 * IFFT(chain).dup);
}).play(s, [\soundBufnum, b]);
)
```




