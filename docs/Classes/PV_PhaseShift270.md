# PV_PhaseShift270

*Shift phase by 270 degrees.*

**Related:** [FFT](../Classes/FFT.md), [IFFT](../Classes/IFFT.md), [PV_PhaseShift](../Classes/PV_PhaseShift.md), [PV_PhaseShift90](../Classes/PV_PhaseShift90.md), [PV_Diffuser](../Classes/PV_Diffuser.md)

**Categories:** UGens>FFT

## Description

Shift phase of all bins by 270 degrees.


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `buffer` | FFT buffer. |  

## Examples


```
s.boot;

(
{
    var in, fft, fft2, shifted;
    in = SinOsc.ar(500, 0, 0.1);
    fft = FFT(LocalBuf(2048), in);
    fft2 = FFT(LocalBuf(2048), in);
    shifted = PV_PhaseShift270(fft);
    [IFFT(fft2), IFFT(shifted)]
}.scope
)
```




