# SyncSaw

*Hard sync sawtooth wave.*

**Related:** [Saw](../Classes/Saw.md), [VarSaw](../Classes/VarSaw.md), [LFSaw](../Classes/LFSaw.md)

**Categories:** UGens>Generators>Deterministic

## Description

A sawtooth wave that is hard synched to a fundamental pitch. This produces an effect similar to moving formants or pulse width modulation. The sawtooth oscillator has its phase reset when the sync oscillator completes a cycle. This is not a band limited waveform, so it may alias.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `syncFreq` | Frequency of the fundamental. |  
| `sawFreq` | Frequency of the synched sawtooth wave. Should always be greater than **syncFreq**.> **⚠️ Warning:** `SyncSaw` will go out of range if the frequency exceeds the sampling rate (which for control rate is `s.sampleRate / s.options.blockSize`). |  
| `mul` | The output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```
{ SyncSaw.ar(100, Line.kr(100, 800, 12), 0.1) }.play;


(
plot { [
    SyncSaw.ar(800, 1200),
    Impulse.ar(800) // to show sync rate
] }
)

(
plot { [
    SyncSaw.ar(800, Line.kr(800, 1600, 0.01)), // modulate saw freq
    Impulse.ar(800) // to show sync rate
] }
)

// scoping the saw: hit 's' when focused on the scope window to compare the channels
(
scope {
    var freq = 400;
    [
    SyncSaw.ar(freq, freq * MouseX.kr(1, 3)), // modulate saw freq
    Impulse.ar(freq) // to show sync rate
] * 0.3 }
)
```




