# Saw

*Band limited sawtooth.*

**Related:** [SyncSaw](../Classes/SyncSaw.md), [VarSaw](../Classes/VarSaw.md), [LFSaw](../Classes/LFSaw.md)

**Categories:** UGens>Generators>Deterministic

## Description

Band limited sawtooth wave generator.


## Class Methods


### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `freq` | Frequency in Hertz. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```
// modulating the frequency

{ Saw.ar(XLine.kr(40, 4000, 6), 0.2) }.play;

// two band limited sawtooth waves through a resonant low pass filter

{ RLPF.ar(Saw.ar([100, 250], 0.1), XLine.kr(8000, 400, 5), 0.05) }.play;
```




