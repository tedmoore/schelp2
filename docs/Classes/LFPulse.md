# LFPulse

*pulse oscillator*

**Categories:** UGens>Generators>Deterministic

**Related:** [LFSaw](../Classes/LFSaw.md)

## Description

A non-band-limited pulse oscillator. Outputs a high value of one and a low value of zero.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `freq` | frequency in Hertz |  
| `iphase` | initial phase offset in cycles (0..1) |  
| `width` | pulse width duty cycle from zero to one. |  
| `mul` |  |  
| `add` |  |  


## Instance Methods


## Examples

a plot:

```
{ LFPulse.ar(Line.kr(100, 800, 0.1)) }.plot(0.1);
```


50 Hz wave:

```
{ LFPulse.ar(50) * 0.1 }.play;
```


modulating frequency:

```
{ LFPulse.ar(XLine.kr(1, 200, 10), 0, 0.2, 0.1) }.play;
```


amplitude modulation:

```
{ LFPulse.kr(XLine.kr(1, 200, 10), 0, 0.2) * SinOsc.ar(440) * 0.1 }.play;
```


used as both Oscillator and LFO:

```
{ LFPulse.ar(LFPulse.kr(3, 0, 0.3, 200, 200), 0, 0.2, 0.1) }.play;
```


scope:

```
{ LFPulse.ar(500, 0, MouseX.kr, 0.5) }.scope;
```


compare with band limited Pulse UGen:

```
(
{
    [
        Pulse.ar(100, 0.3, 0.5),
        LFPulse.ar(100, 0, 0.3, 0.5)
    ] * 0.2
}.scope(bufsize: 44100, zoom: 5)
)
```




