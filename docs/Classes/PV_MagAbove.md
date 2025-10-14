# PV_MagAbove

*Pass bins above a threshold.*

**Related:** [FFT](../Classes/FFT.md), [IFFT](../Classes/IFFT.md), [PV_LocalMax](../Classes/PV_LocalMax.md), [PV_MagBelow](../Classes/PV_MagBelow.md), [PV_MagClip](../Classes/PV_MagClip.md)

**Categories:** UGens>FFT

## Description

Passes only bins whose magnitude is above a threshold.


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
SynthDef("help-magAbove", { |out = 0|
    var in, chain;
    in = SinOsc.ar(SinOsc.kr(SinOsc.kr(0.08, 0, 6, 6.2).squared, 0, 100, 800));
    // in = WhiteNoise.ar(0.2);
    chain = FFT(LocalBuf(2048), in);
    chain = PV_MagAbove(chain, 310);
    Out.ar(out, 0.1 * IFFT(chain).dup);
}).play(s);
)

(
SynthDef("help-magAbove2", { |out = 0|
    var in, chain;
    in = WhiteNoise.ar(0.2);
    chain = FFT(LocalBuf(2048), in);
    chain = PV_MagAbove(chain, MouseX.kr(0, 10));
    Out.ar(out, 0.1 * IFFT(chain).dup);
}).play(s);
)

(
SynthDef("help-magAbove3", { |out = 0, soundBufnum = 2|
    var in, chain;
    in = PlayBuf.ar(1, soundBufnum, BufRateScale.kr(soundBufnum), loop: 1);
    chain = FFT(LocalBuf(2048), in);
    chain = PV_MagAbove(chain, MouseX.kr(0, 310));
    Out.ar(out, 0.1 * IFFT(chain).dup);
}).play(s, [\soundBufnum, b]);
)
```




