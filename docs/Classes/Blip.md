# Blip

*Band limited impulse oscillator.*

**Related:** [Impulse](../Classes/Impulse.md)

**Categories:** UGens>Generators>Deterministic

## Description

Band Limited ImPulse generator. All harmonics have equal amplitude. This is the equivalent of 'buzz' in *MusicN* languages.
*Synth-O-Matic* (1990) had an impulse generator called blip, hence that name here rather than 'buzz'.
It is improved from other implementations in that it will crossfade in a control period when the number of harmonics changes, so that there are no audible pops. It also eliminates the divide in the formula by using a 1/sin table (with special precautions taken for 1/0). The lookup tables are linearly interpolated for better quality.
> **⚠️ Warning:** This waveform in its raw form could be damaging to your ears at high amplitudes or for long periods.


## Class Methods


### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `freq` | Frequency in Hertz. |  
| `numharm` | Number of harmonics. This may be lowered internally if it would cause aliasing. |  
| `mul` |  |  
| `add` |  |  

## Examples


```
// modulate frequency
{ Blip.ar(XLine.kr(20000, 200, 6), 100, 0.2) }.play;

// modulate numharmonics
{ Blip.ar(200, Line.kr(1, 100, 20), 0.2) }.play;
```




