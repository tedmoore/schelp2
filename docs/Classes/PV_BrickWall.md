# PV_BrickWall

*Zero bins.*

**Related:** [FFT](../Classes/FFT.md), [IFFT](../Classes/IFFT.md)

**Categories:** UGens>FFT

## Description

Clears bins above or below a cutoff point.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `buffer` | FFT buffer. |  
| `wipe` | Can range between -1 and +1.If `wipe` == 0 then there is no effect.If `wipe` > 0 then it acts like a high pass filter, clearing bins from the bottom up.If `wipe` < 0 then it acts like a low pass filter, clearing bins from the top down. |  

## Examples


```supercollider
s.boot;

(
{
    var in, chain;
    in = WhiteNoise.ar(0.2);
    chain = FFT(LocalBuf(2048), in);
    chain = PV_BrickWall(chain, SinOsc.kr(0.1));
    IFFT(chain);
}.play
)
```




