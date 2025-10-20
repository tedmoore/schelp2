# PV_Add

*Complex addition.*

**Related:** [FFT](../Classes/FFT.md), [IFFT](../Classes/IFFT.md), [PV_CopyPhase](../Classes/PV_CopyPhase.md), [PV_MagMul](../Classes/PV_MagMul.md), [PV_Max](../Classes/PV_Max.md), [PV_Min](../Classes/PV_Min.md), [PV_Mul](../Classes/PV_Mul.md)

**Categories:** UGens>FFT

## Description

Complex addition:

```
RealA + RealB, ImagA + ImagB
```




## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bufferA` | FFT buffer A. |  
| `bufferB` | FFT buffer B. |  

## Examples


```
s.boot;
b = Buffer.read(s, ExampleFiles.child);

(
SynthDef("help-add", { |out = 0, soundBufnum|
    var inA, chainA, inB, chainB, chain ;
    inA = PlayBuf.ar(1, soundBufnum, BufRateScale.kr(soundBufnum), loop: 1);
    inB =  PlayBuf.ar(1, soundBufnum, BufRateScale.kr(soundBufnum) * 0.5, loop: 1);
    chainA = FFT(LocalBuf(2048), inA);
    chainB = FFT(LocalBuf(2048), inB);
    chain = PV_Add(chainA, chainB);
    Out.ar(out, 0.1 * IFFT(chain).dup);
}).play(s, [\soundBufnum, b.bufnum]);
)

b.free
```




