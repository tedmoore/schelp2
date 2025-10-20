# PV_MagFreeze

*Freeze magnitudes.*

**Categories:** UGens>FFT

## Description

Freezes magnitudes at current levels when `freeze` > 0.


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `buffer` | FFT buffer. |  
| `freeze` | If > 0, then magnitudes are frozen at current levels. |  

## Examples


```
s.boot;
b = Buffer.read(s, ExampleFiles.child);


(
SynthDef("help-magFreeze", { |out = 0|
    var in, chain;
    in = SinOsc.ar(LFNoise1.kr(5.2, 250, 400));
    chain = FFT(LocalBuf(2048), in);
    // moves in and out of freeze
    chain = PV_MagFreeze(chain, SinOsc.kr(0.2));
    Out.ar(out, 0.1 * IFFT(chain).dup);
}).play(s);

)

(
// trig with MouseY
SynthDef("help-magFreeze2", { |out = 0, soundBufnum = 2|
    var in, chain;
    in = PlayBuf.ar(1, soundBufnum, BufRateScale.kr(soundBufnum), loop: 1);
    chain = FFT(LocalBuf(2048), in);
    chain = PV_MagFreeze(chain, MouseY.kr > 0.5);
    Out.ar(out, 0.1 * IFFT(chain).dup);
}).play(s, [\soundBufnum, b]);
)

b.free
```




