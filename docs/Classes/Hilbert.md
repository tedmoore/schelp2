# Hilbert

*Applies the Hilbert transform to an input signal.*

**Related:** [HilbertFIR](../Classes/HilbertFIR.md), [FreqShift](../Classes/FreqShift.md)

**Categories:** UGens>Filters>Nonlinear

## Description

Returns two channels with the original signal and a copy of that signal that has been shifted in phase by 90 degrees (0.5 pi radians). Hilbert outputs two channels containing the input signal and the transformed signal. Due to the method used, distortion occurs in the upper octave of the frequency spectrum (See HilbertFIR for an FFT implementation that avoids this, but introduces a significant delay).


## Class Methods


### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal to transform. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```
s.boot;
s.scope;
a = { Hilbert.ar(SinOsc.ar(100)) * -20.dbamp }.play;
a.release;
```




