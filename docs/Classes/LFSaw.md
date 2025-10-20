# LFSaw

*Sawtooth oscillator*

**Related:** [LFCub](../Classes/LFCub.md), [LFPar](../Classes/LFPar.md), [LFPulse](../Classes/LFPulse.md), [LFTri](../Classes/LFTri.md), [Saw](../Classes/Saw.md)

**Categories:** UGens>Generators>Deterministic

## Description

A non-band-limited sawtooth oscillator. Output ranges from -1 to +1.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `freq` | Frequency in Hertz. |  
| `iphase` | Initial phase offset. For efficiency reasons this is a value ranging from 0 to 2.
> **Note:** enter "1" for an initial phase of 0 radians. A value of 0 would start the cycle at pi radians. See the example below. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```
{ LFSaw.ar(500, 1, 0.1) }.play

// used as both Oscillator and LFO:
{ LFSaw.ar(LFSaw.kr(4, 0, 200, 400), 0, 0.1) }.play
```


Display the special behaviour of the initial phase parameter:

```
 // three channels, three phases
{ LFSaw.ar(20, [0, 1, 2]) }.plot(0.1)
```




