# PV_Mul

*Complex multiply.*

**Related:** [FFT](../Classes/FFT.md), [IFFT](../Classes/IFFT.md), [PV_Add](../Classes/PV_Add.md), [PV_CopyPhase](../Classes/PV_CopyPhase.md), [PV_MagMul](../Classes/PV_MagMul.md), [PV_Max](../Classes/PV_Max.md), [PV_Min](../Classes/PV_Min.md)

**Categories:** UGens>FFT

## Description

Complex Multiplication:

```supercollider
(RealA * RealB) - (ImagA * ImagB),
(ImagA * RealB) + (RealA * ImagB)
```




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

(
SynthDef("help-mul", { |out = 0|
    var inA, chainA, inB, chainB, chain ;
    inA = SinOsc.ar(500, 0, 0.5);
    inB =  SinOsc.ar(Line.kr(100, 400, 5), 0, 0.5);
    chainA = FFT(LocalBuf(2048), inA);
    chainB = FFT(LocalBuf(2048), inB);
    chain = PV_Mul(chainA, chainB);
    Out.ar(out, 0.1 * IFFT(chain).dup);
}).play(s);
s.scope;
)

(
SynthDef("help-mul2", { |out = 0|
    var inA, chainA, inB, chainB, chain ;
    inA = SinOsc.ar(500, 0, 0.5) * Line.kr;
    inB = LFNoise1.ar(20);
    chainA = FFT(LocalBuf(2048), inA);
    chainB = FFT(LocalBuf(2048), inB);
    chain = PV_Mul(chainA, chainB);
    Out.ar(out, 0.1 * IFFT(chain).dup);
}).play(s);
s.scope;
)
```




