# PV_MagMul

*Multiply magnitudes.*

**Related:** [FFT](../Classes/FFT.md), [IFFT](../Classes/IFFT.md), [PV_Add](../Classes/PV_Add.md), [PV_CopyPhase](../Classes/PV_CopyPhase.md), [PV_Max](../Classes/PV_Max.md), [PV_Min](../Classes/PV_Min.md), [PV_Mul](../Classes/PV_Mul.md)

**Categories:** UGens>FFT

## Description

Multiplies magnitudes of two inputs and keeps the phases of the first input.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bufferA` | FFT buffer A. |  
| `bufferB` | FFT buffer B. |  

## Examples


```supercollider
s.boot;
b = Buffer.read(s, ExampleFiles.child);

(
SynthDef("help-magMul", { |out = 0|
    var inA, chainA, inB, chainB, chain;
    inA = WhiteNoise.ar(0.2);
    inB = LFSaw.ar(100, 0, 0.2);
    chainA = FFT(LocalBuf(2048), inA);
    chainB = FFT(LocalBuf(2048), inB);
    chain = PV_MagMul(chainA, chainB);
    Out.ar(out, 0.1 * IFFT(chain).dup);
}).play(s);
)

(
SynthDef("help-magMul2", { |out = 0, soundBufnum = 2|
    var inA, chainA, inB, chainB, chain;
    inA = LFSaw.ar([100, 150], 0, 0.2);
    inB = PlayBuf.ar(1, soundBufnum, BufRateScale.kr(soundBufnum), loop: 1);
    chainA = FFT(LocalBuf(2048), inA);
    chainB = FFT(LocalBuf(2048), inB);
    chain = PV_MagMul(chainA, chainB);
    Out.ar(out, 0.03 * IFFT(chain));
}).play(s, [\soundBufnum, b.bufnum]);
)

b.free
```




