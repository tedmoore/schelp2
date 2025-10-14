# PV_MagSquared

*Square magnitudes.*

**Related:** [FFT](../Classes/FFT.md), [IFFT](../Classes/IFFT.md)

**Categories:** UGens>FFT

## Description

Squares the magnitudes and renormalizes to previous peak. This makes weak bins weaker.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `buffer` | FFT buffer. |  

## Examples


```supercollider
s.boot;

(
b = Buffer.alloc(s, 2048, 1);
c = Buffer.read(s, ExampleFiles.child);
)

(
SynthDef("help-magSquared", { |out = 0, bufnum = 0, soundBufnum = 2|
    var in, chain;
    in = PlayBuf.ar(1, soundBufnum, BufRateScale.kr(soundBufnum), loop: 1);
    chain = FFT(bufnum, in);
    chain = PV_MagSquared(chain);
    Out.ar(out, 0.003 * IFFT(chain).dup);
}).play(s, [\out, 0, \bufnum, b.bufnum, \soundBufnum, c.bufnum]);
)
```




