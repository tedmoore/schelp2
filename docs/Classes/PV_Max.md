# PV_Max

*Maximum magnitude.*

**Related:** [FFT](../Classes/FFT.md), [IFFT](../Classes/IFFT.md), [PV_Add](../Classes/PV_Add.md), [PV_CopyPhase](../Classes/PV_CopyPhase.md), [PV_MagMul](../Classes/PV_MagMul.md), [PV_Min](../Classes/PV_Min.md), [PV_Mul](../Classes/PV_Mul.md)

**Categories:** UGens>FFT

## Description

Output copies bins with the maximum magnitude of the two inputs.


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
var exBuf;
Dialog.getPaths({ |paths| // get a second soundfile;
    paths.do({ |p| exBuf = Buffer.read(s, p);
        SynthDef("help-max", { |out = 0, soundBufnum1 = 2, soundBufnum2 = 3|
            var inA, chainA, inB, chainB, chain ;
            inA = PlayBuf.ar(1, soundBufnum1, BufRateScale.kr(soundBufnum1), loop: 1);
            inB =  PlayBuf.ar(1, soundBufnum2, BufRateScale.kr(soundBufnum2), loop: 1);
            chainA = FFT(LocalBuf(2048), inA);
            chainB = FFT(LocalBuf(2048), inB);
            chain = PV_Max(chainA, chainB);
            Out.ar(out, 0.1 * IFFT(chain).dup);
        }).play(s, [\soundBufnum1, b.bufnum, \soundBufnum2, exBuf.bufnum]);
    })
}, {
    "cancelled".postln;
});
)

b.free;
```




