# PV_RectComb2

*Make gaps in spectrum.*

**Related:** [FFT](../Classes/FFT.md), [IFFT](../Classes/IFFT.md), [PV_RectComb](../Classes/PV_RectComb.md)

**Categories:** UGens>FFT

## Description

Alternates blocks of bins between the two inputs.


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bufferA` | FFT buffer A. |  
| `bufferB` | FFT buffer B. |  
| `numTeeth` | Number of teeth in the comb. |  
| `phase` | Starting phase of comb pulse. |  
| `width` | Pulse width of the comb. |  

## Examples


```
s.boot;
b = Buffer.read(s, ExampleFiles.child);

(
var exBuf;
Dialog.getPaths({ |paths| // get a second soundfile;
    paths.do({ |p| exBuf = Buffer.read(s, p);

        SynthDef("help-max", { |out = 0, soundBufnum1 = 2, soundBufnum2 = 3|
            var inA, chainA, inB, chainB, chain ;
            inA = PlayBuf.ar(1, soundBufnum1, BufRateScale.kr(soundBufnum1), loop: 1);
            inB =  PlayBuf.ar(1, soundBufnum2, BufRateScale.kr(soundBufnum2), loop: 1);
            chainA = FFT(LocalBuf(2048), inA);
            chainB = FFT(LocalBuf(2048), inB);
            chain = PV_RectComb2(chainA, chainB, MouseX.kr(0, 32), MouseY.kr, 0.3);
            Out.ar(out, 0.5 * IFFT(chain).dup);
        }).play(s, [\soundBufnum1, b, \soundBufnum2, exBuf]);
    })
}, {
    "cancelled".postln;
});
)
```




