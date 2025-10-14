# LFCub

*A sine like shape made of two cubic pieces*

**Related:** [LFPar](../Classes/LFPar.md), [LFPulse](../Classes/LFPulse.md), [LFSaw](../Classes/LFSaw.md), [LFTri](../Classes/LFTri.md)

**Categories:** UGens>Generators>Deterministic

## Description

A sine like shape made of two cubic pieces. Smoother than [LFPar](../Classes/LFPar.md) .


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `freq` | Frequency in Hertz. |  
| `iphase` | Initial phase offset. For efficiency reasons this is a value ranging from 0 to 2. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```supercollider
{ LFCub.ar(LFCub.kr(LFCub.kr(0.2, 0, 8, 10), 0, 400, 800), 0, 0.1) }.play
{ LFCub.ar(LFCub.kr(0.2, 0, 400, 800), 0, 0.1) }.play
{ LFCub.ar(800, 0, 0.1) }.play
{ LFCub.ar(XLine.kr(100, 8000, 30), 0, 0.1) }.play

// compare:

{ LFPar.ar(LFPar.kr(LFPar.kr(0.2, 0, 8, 10), 0, 400, 800), 0, 0.1) }.play
{ LFPar.ar(LFPar.kr(0.2, 0, 400, 800), 0, 0.1) }.play
{ LFPar.ar(800, 0, 0.1) }.play
{ LFPar.ar(XLine.kr(100, 8000, 30), 0, 0.1) }.play


{ SinOsc.ar(SinOsc.kr(SinOsc.kr(0.2, 0, 8, 10), 0, 400, 800), 0, 0.1) }.play
{ SinOsc.ar(SinOsc.kr(0.2, 0, 400, 800), 0, 0.1) }.play
{ SinOsc.ar(800, 0, 0.1) }.play
{ SinOsc.ar(XLine.kr(100, 8000, 30), 0, 0.1) }.play

{ LFTri.ar(LFTri.kr(LFTri.kr(0.2, 0, 8, 10), 0, 400, 800), 0, 0.1) }.play
{ LFTri.ar(LFTri.kr(0.2, 0, 400, 800), 0, 0.1) }.play
{ LFTri.ar(800, 0, 0.1) }.play
{ LFTri.ar(XLine.kr(100, 8000, 30), 0, 0.1) }.play
```




