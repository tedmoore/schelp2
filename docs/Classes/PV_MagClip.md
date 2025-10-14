# PV_MagClip

*Clip bins to a threshold.*

**Related:** [FFT](../Classes/FFT.md), [IFFT](../Classes/IFFT.md), [PV_MagAbove](../Classes/PV_MagAbove.md), [PV_LocalMax](../Classes/PV_LocalMax.md), [PV_MagBelow](../Classes/PV_MagBelow.md)

**Categories:** UGens>FFT

## Description

Clips bin magnitudes to a maximum threshold.


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
    var in, chain;
    in = Mix.arFill(3, { LFSaw.ar(exprand(100, 500), 0, 0.1) });
    chain = FFT(LocalBuf(2048), in);
    chain = PV_MagClip(chain, MouseX.kr(0, 15));
    Out.ar(out, 0.5 * IFFT(chain).dup);
}).play(s);
)

(
SynthDef("help-magClip2", { |out = 0, soundBufnum = 2|
    var in, chain;
    in = PlayBuf.ar(1, soundBufnum, BufRateScale.kr(soundBufnum), loop: 1);
    chain = FFT(LocalBuf(2048), in);
    chain = PV_MagClip(chain, MouseX.kr(0, 50));
    Out.ar(out, 0.5 * IFFT(chain).dup);
}).play(s, [\soundBufnum, b]);
)
```




