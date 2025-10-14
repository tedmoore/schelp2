# PV_PhaseShift

*Shift phase.*

**Related:** [FFT](../Classes/FFT.md), [IFFT](../Classes/IFFT.md), [PV_PhaseShift90](../Classes/PV_PhaseShift90.md), [PV_PhaseShift270](../Classes/PV_PhaseShift270.md), [PV_Diffuser](../Classes/PV_Diffuser.md)

**Categories:** UGens>FFT

## Description

Shift phase of all bins.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `buffer` | FFT buffer. |  
| `shift` | Phase shift in radians. |  
| `integrate` | If greater than zero, integrate the phase-shift across calls (for an accumulating phase shift). |  

## Examples


```supercollider
s.boot;

(
SynthDef("help-phaseShift", { |out = 0|
        var in, chain;
        in = SinOsc.ar(500);
        chain = FFT(LocalBuf(2048), in);
        chain = PV_PhaseShift(chain, LFNoise2.kr(1, 180, 180));
        Out.ar(out, 0.1 * IFFT(chain).dup);
}).play(s);
)
```




