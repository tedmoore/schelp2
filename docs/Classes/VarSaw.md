# VarSaw

*Variable duty saw*

**Related:** [Saw](../Classes/Saw.md), [SyncSaw](../Classes/SyncSaw.md), [LFSaw](../Classes/LFSaw.md)

**Categories:** UGens>Generators>Deterministic

## Description

Sawtooth-triangle oscillator with variable duty.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `freq` | Frequency in Hertz. Positive frequencies only.> **⚠️ Warning:** `VarSaw` will go out of range if the frequency exceeds the sampling rate (which for control rate is `s.sampleRate / s.options.blockSize`). |  
| `iphase` | Initial phase offset in cycles. [0..1] |  
| `width` | Duty cycle, denoting where in the cycle the waveform peaks. E.g. for widths of `0, 0.5,` or `1.0`, the waveform will peak at the beginning, middle, or end of the cycle, respectively. [0..1] (clipped internally to [0.001..0.999]) |  
| `mul` | The output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```supercollider
// observe different duty widths
{ VarSaw.ar(1000, 0, [0, 0.5, 1]) }.plot

(
play({
    VarSaw.ar(
        LFPulse.kr(3, 0, 0.3, 200, 200),
        0,
        LFTri.kr(1.0).range(0, 1), // width
        0.1)
});
)

play({ VarSaw.ar(LFPulse.kr(3, 0, 0.3, 200, 200), 0, 0.2, 0.1) });

// compare:

play({ LFPulse.ar(LFPulse.kr(3, 0, 0.3, 200, 200), 0, 0.2, 0.1) });
```




