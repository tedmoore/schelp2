# PV_Diffuser

*Random phase shifting.*

**Related:** [FFT](../Classes/FFT.md), [IFFT](../Classes/IFFT.md), [PV_PhaseShift](../Classes/PV_PhaseShift.md), [PV_PhaseShift90](../Classes/PV_PhaseShift90.md), [PV_PhaseShift270](../Classes/PV_PhaseShift270.md)

**Categories:** UGens>FFT

## Description

Adds a different constant random phase shift to each bin. When triggered, it selects a new set of random phases.


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `buffer` | FFT buffer. |  
| `trig` | A trigger, that selects a new set of random values. |  

## Examples


```
(
// trig with MouseY crossing center of screen
{
    var in, chain;
    in = Mix.ar(SinOsc.ar(200 * (1..10), 0, Array.fill(10, { rrand(0.1, 0.2) })));
    chain = FFT(LocalBuf(2048), in);
    chain = PV_Diffuser(chain, MouseY.kr > 0.5);
    0.5 * IFFT(chain).dup;
}.play
);

(
b = Buffer.read(s, ExampleFiles.child);

// trig with MouseY crossing center of screen
{
    var in, chain;
    in = PlayBuf.ar(1, b, BufRateScale.kr(b), loop: 1);
    chain = FFT(LocalBuf(2048), in);
    chain = PV_Diffuser(chain, MouseY.kr > 0.5);
    0.5 * IFFT(chain).dup;
}.play
);
```




