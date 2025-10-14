# PV_MagNoise

*Multiply magnitudes by noise.*

**Related:** [FFT](../Classes/FFT.md), [IFFT](../Classes/IFFT.md)

**Categories:** UGens>FFT

## Description

Magnitudes are multiplied with noise.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `buffer` | FFT buffer. |  

## Examples


```supercollider
s.boot;

b = Buffer.read(s, ExampleFiles.child);

(
SynthDef("help-magNoise", { |out = 0|
    var in, chain;
    in = SinOsc.ar(SinOsc.kr(SinOsc.kr(0.08, 0, 6, 6.2).squared, 0, 100, 800));
    chain = FFT(LocalBuf(2048), in);
    chain = PV_MagNoise(chain);
    Out.ar(out, 0.1 * IFFT(chain).dup);
}).play(s);
)

(
SynthDef("help-magNoise2", { |out = 0, soundBufnum = 2|
    var in, chain;
    in = PlayBuf.ar(1, soundBufnum, BufRateScale.kr(soundBufnum), loop: 1);
    chain = FFT(LocalBuf(2048), in);
    chain = PV_MagNoise(chain);
    Out.ar(out, 0.2 * IFFT(chain).dup);
}).play(s, [\soundBufnum, b]);
)

b.free;
```




