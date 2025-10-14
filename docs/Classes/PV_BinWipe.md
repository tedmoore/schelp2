# PV_BinWipe

*Combine low and high bins from two inputs.*

**Categories:** UGens>FFT

## Description

Copies low bins from one input and the high bins of the other.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bufferA` | FFT buffer A. |  
| `bufferB` | FFT buffer B. |  
| `wipe` | Can range between -1 and +1.If `wipe` == 0, then the output is the same as `bufferA` .If `wipe` > 0, then it begins replacing with bins from `bufferB` from the bottom up.If `wipe` < 0, then it begins replacing with bins from `bufferB` from the top down. |  

## Examples


```supercollider
s.boot;
b = Buffer.read(s, ExampleFiles.child);

(
SynthDef("help-binWipe", { |out = 0|
    var inA, chainA, inB, chainB, chain;
    inA = WhiteNoise.ar(0.2);
    inB = LFSaw.ar(100, 0, 0.2);
    chainA = FFT(LocalBuf(2048), inA);
    chainB = FFT(LocalBuf(2048), inB);
    chain = PV_BinWipe(chainA, chainB, MouseX.kr(-1, 1));
    Out.ar(out, 0.1 * IFFT(chain).dup);
}).play(s);
)

(
SynthDef("help-binWipe2", { |out = 0, soundBufnum = 2|
    var inA, chainA, inB, chainB, chain;
    inA = WhiteNoise.ar(0.2);
    inB = PlayBuf.ar(1, soundBufnum, BufRateScale.kr(soundBufnum), loop: 1);
    chainA = FFT(LocalBuf(2048), inA);
    chainB = FFT(LocalBuf(2048), inB);
    chain = PV_BinWipe(chainA, chainB, MouseX.kr(-1, 1));
    Out.ar(out, 0.1 * IFFT(chain).dup);
}).play(s, [\soundBufnum, b]);
)
```




