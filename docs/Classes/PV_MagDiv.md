# PV_MagDiv

*Division of magnitudes*

**Categories:** UGens>FFT

## Description

Divides magnitudes of two inputs and keeps the phases of the first input.


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bufferA` | fft buffer A. |  
| `bufferB` | fft buffer B. |  
| `zeroed` | number to use when bins are zeroed out, i.e. causing division by zero (defaults to 0.0001) |  

## Examples


```supercollider
s.boot;

(
SynthDef("help-magMul", { |out = 0|
    var inA, chainA, inB, chainB, chain;
    inA = WhiteNoise.ar(0.2);
    inB = LFSaw.ar(100, 0, 0.2);
    chainA = FFT(LocalBuf(2048), inA);
    chainB = FFT(LocalBuf(2048), inB);
    chain = PV_MagDiv(chainA, chainB);
    Out.ar(out, 0.5 * IFFT(chain).dup);
}).play;
)


c = Buffer.read(s, ExampleFiles.child);

(
SynthDef("help-magMul2", { |out = 0, soundBufnum = 0|
    var inA, chainA, inB, chainB, chain;
    inA = LFSaw.ar([100, 150], 0, 0.2);
    inB = PlayBuf.ar(1, soundBufnum, BufRateScale.kr(soundBufnum), loop: 1);
    chainA = FFT(LocalBuf(2048), inA);
    chainB = FFT(LocalBuf(2048), inB);
    chain = PV_MagDiv(chainA, chainB);
    Out.ar(out, 0.1 * IFFT(chain));
}).play(s, [\out, 0, \soundBufnum, c]);
)

c.free;
```




