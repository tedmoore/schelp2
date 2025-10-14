# PV_CopyPhase

*Copy magnitudes and phases.*

**Related:** [FFT](../Classes/FFT.md), [IFFT](../Classes/IFFT.md), [PV_Add](../Classes/PV_Add.md), [PV_MagMul](../Classes/PV_MagMul.md), [PV_Max](../Classes/PV_Max.md), [PV_Min](../Classes/PV_Min.md), [PV_Mul](../Classes/PV_Mul.md)

**Categories:** UGens>FFT

## Description

Combines magnitudes of first input and phases of the second input.


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
SynthDef("help-copyPhase", { |out = 0|
    var inA, chainA, inB, chainB, chain;
    inA = SinOsc.ar(SinOsc.kr(SinOsc.kr(0.08, 0, 6, 6.2).squared, 0, 100, 800));
    inB = WhiteNoise.ar(0.2);
    chainA = FFT(LocalBuf(2048), inA);
    chainB = FFT(LocalBuf(2048), inB);
    chain = PV_CopyPhase(chainA, chainB);
    Out.ar(out, 0.1 * IFFT(chain).dup);
}).play(s);
)

(
SynthDef("help-copyPhase2", { |out = 0, soundBufnum = 2|
    var inA, chainA, inB, chainB, chain;
    inA = PlayBuf.ar(1, soundBufnum, BufRateScale.kr(soundBufnum), loop: 1);
    inB =  SinOsc.ar(SinOsc.kr(SinOsc.kr(0.08, 0, 6, 6.2).squared, 0, 100, 800));
    chainA = FFT(LocalBuf(2048), inA);
    chainB = FFT(LocalBuf(2048), inB);
    chain = PV_CopyPhase(chainA, chainB);
    Out.ar(out, 0.1 * IFFT(chain).dup);
}).play(s, [\soundBufnum, b]);

)
```




