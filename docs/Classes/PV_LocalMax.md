# PV_LocalMax

*Pass bins which are a local maximum.*

**Related:** [FFT](../Classes/FFT.md), [IFFT](../Classes/IFFT.md), [PV_MagAbove](../Classes/PV_MagAbove.md), [PV_MagBelow](../Classes/PV_MagBelow.md), [PV_MagClip](../Classes/PV_MagClip.md)

**Categories:** UGens>FFT

## Description

Passes only bins whose magnitude is above a threshold and above their nearest neighbors.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `buffer` | FFT buffer. |  
| `threshold` | Magnitude threshold. |  

## Examples


```supercollider
s.boot;
b = Buffer.read(s, ExampleFiles.child);


(
SynthDef("help-localMax", { |out = 0|
    var in, chain;
    in = Mix.arFill(3, { LFSaw.ar(exprand(100, 500), 0, 0.1) });
    chain = FFT(LocalBuf(2048), in);
    chain = PV_LocalMax(chain, MouseX.kr(0, 50));
    Out.ar(out, 0.5 * IFFT(chain).dup);
}).play(s);
)

(
SynthDef("help-localMax2", { |out = 0, soundBufnum = 2|
    var in, chain;
    in = PlayBuf.ar(1, soundBufnum, BufRateScale.kr(soundBufnum), loop: 1);
    chain = FFT(LocalBuf(2048), in);
    chain = PV_LocalMax(chain, MouseX.kr(0, 100));
    Out.ar(out, 0.1 * IFFT(chain).dup);
}).play(s, [\soundBufnum, b]);
)
```




