# IFFT

*Inverse Fast Fourier Transform*

**Related:** [FFT](../Classes/FFT.md), [FFT-Overview](../Guides/FFT-Overview.md)

**Categories:** UGens>FFT

## Description

The inverse fast fourier transform converts from frequency content to a signal.
The fast fourier transform analyzes the frequency content of a signal. The IFFT UGen converts this *frequency-domain* information back into *time-domain* audio data. Most often this is used as the end of a process which begins with [FFT](../Classes/FFT.md), followed by frequency-domain processing using PV (phase-vocoder) UGens, followed by IFFT.


## Class Methods

### `new`, `ar`, `kr`
returns a time domain signal from converting the FFT frequency domain signal chain. The *new method is equivalent to the *ar message returns an audio rate signal.**Arguments:**

| Argument | Description |
|----------|-------------|
| `buffer` | The FFT "chain" signal coming originally from an FFT UGen, perhaps via other PV UGens. |  
| `wintype` | Defines how the data is windowed:| -1 | **rectangular** windowing, simple but typically not recommended; | 
| --- | --- || 0 | (the default) **Sine** windowing, typically recommended for phase-vocoder work; | | 1 | **Hann** windowing, typically recommended for analysis work. | |  
| `winsize` | Can be used to account for zero-padding, in the same way as the [FFT](../Classes/FFT.md) UGen. |  
**Returns:** The *time-domain* audio signal.The IFFT UGen converts the FFT data in-place (in the original FFT buffer) and overlap-adds the result to produce a continuous signal at its output.
## Examples


```supercollider
// without any modification, convert FFT chain (frequency domain signal) back to audio (time domain signal)
(
{   var in, chain;
    in = WhiteNoise.ar;
    chain = FFT(LocalBuf(2048), in);
    IFFT.ar(chain) * -20.dbamp // inverse FFT
}.play;
)
```




