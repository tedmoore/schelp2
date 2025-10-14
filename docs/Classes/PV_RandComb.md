# PV_RandComb

*Pass random bins.*

**Related:** [PV_RandWipe](../Classes/PV_RandWipe.md)

**Categories:** UGens>FFT

## Description

Randomly clear bins.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `buffer` | FFT buffer. |  
| `wipe` | Clears bins from input in a random order as wipe goes from 0 to 1. |  
| `trig` | A trigger, that selects a new random ordering. |  

## Examples


```supercollider
s.boot;
c = Buffer.read(s, ExampleFiles.child);

(
SynthDef("help-randcomb", { |out = 0|
    var sig, chain;
    sig = WhiteNoise.ar(0.8);
    chain = FFT(LocalBuf(2048), sig);
    chain = PV_RandComb(chain, 0.95, Impulse.kr(0.4));
    Out.ar(out, IFFT(chain).dup);
}).play(s);
)

(
// trig with MouseY
SynthDef("help-randcomb2", { |out = 0, soundBufnum = 2|
    var sig, chain;
    sig = PlayBuf.ar(1, soundBufnum, BufRateScale.kr(soundBufnum), loop: 1);
    chain = FFT(LocalBuf(2048), sig);
    chain = PV_RandComb(chain, MouseY.kr, Impulse.kr(0.4));
    Out.ar(out, IFFT(chain).dup);
}).play(s, [\soundBufnum, c.bufnum]);
)
```




