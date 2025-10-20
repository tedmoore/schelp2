# PV_MagBelow

*Pass bins below a threshold.*

**Related:** [FFT](../Classes/FFT.md), [IFFT](../Classes/IFFT.md), [PV_MagAbove](../Classes/PV_MagAbove.md), [PV_LocalMax](../Classes/PV_LocalMax.md), [PV_MagClip](../Classes/PV_MagClip.md)

**Categories:** UGens>FFT

## Description

Passes only bins whose magnitude is below a threshold.


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `buffer` | FFT buffer. |  
| `threshold` | Magnitude threshold. |  

## Examples


```
s.boot;

(
b = Buffer.alloc(s, 2048, 1);
c = Buffer.read(s, ExampleFiles.child);
)

(
SynthDef("help-magBelow", { |out = 0, bufnum = 0|
    var in, chain;
    in = SinOsc.ar(SinOsc.kr(SinOsc.kr(0.08, 0, 6, 6.2).squared, 0, 100, 800));
    chain = FFT(bufnum, in);
    chain = PV_MagBelow(chain, 10);
    Out.ar(out, 0.5 * IFFT(chain).dup);
}).play(s, [\out, 0, \bufnum, b.bufnum]);
)

(
SynthDef("help-magBelow2", { |out = 0, bufnum = 0|
    var in, chain;
    in = WhiteNoise.ar(0.2);
    chain = FFT(bufnum, in);
    chain = PV_MagBelow(chain, MouseX.kr(0, 7));
    Out.ar(out, 0.5 * IFFT(chain).dup);
}).play(s, [\out, 0, \bufnum, b.bufnum]);
)

(
SynthDef("help-magBelow3", { |out = 0, bufnum = 0, soundBufnum = 2|
    var in, chain;
    in = PlayBuf.ar(1, soundBufnum, BufRateScale.kr(soundBufnum), loop: 1);
    chain = FFT(bufnum, in);
    chain = PV_MagBelow(chain, MouseX.kr(0, 310));
    Out.ar(out, 0.5 * IFFT(chain).dup);
}).play(s, [\out, 0, \bufnum, b.bufnum, \soundBufnum, c.bufnum]);
)
```




