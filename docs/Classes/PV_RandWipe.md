# PV_RandWipe

*Crossfade in random bin order.*

**Related:** [PV_RandComb](../Classes/PV_RandComb.md)

**Categories:** UGens>FFT

## Description

Crossfades between two sounds by copying bins in a random order.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bufferA` | FFT buffer A. |  
| `bufferB` | FFT buffer B. |  
| `wipe` | Copies bins from bufferB in a random order as wipe goes from 0 to 1. |  
| `trig` | A trigger, that selects a new random ordering. |  

## Examples


```supercollider
s.boot;

(
// trig with MouseY
SynthDef("help-randWipe", { |out = 0|
    var inA, chainA, inB, chainB, chain;
    inA = Mix.arFill(6, { LFSaw.ar(exprand(400, 1000), 0, 0.1) });
    inB = Mix.arFill(6, { LFPulse.ar(exprand(80, 400), 0, 0.2, SinOsc.kr(8.0.rand, 0, 0.2).max(0)) });
    chainA = FFT(LocalBuf(2048), inA);
    chainB = FFT(LocalBuf(2048), inB);
    chain = PV_RandWipe(chainA, chainB, MouseX.kr.poll, MouseY.kr.poll > 0.5);
    Out.ar(out, 0.5 * IFFT(chain).dup);
}).play(s);
)
```




