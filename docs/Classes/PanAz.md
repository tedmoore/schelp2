# PanAz

*Azimuth panner*

**Related:** [Balance2](../Classes/Balance2.md), [LinPan2](../Classes/LinPan2.md), [Pan2](../Classes/Pan2.md), [Pan4](../Classes/Pan4.md)

**Categories:** UGens>Multichannel>Panners

## Description

Multichannel equal power panner.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `numChans` | Number of output channels. Must be a nonzero, positive integer. This is fixed when the SynthDef is compiled so cannot be assigned to a SynthDef argument. |  
| `in` | The input signal. |  
| `pos` | pan position (`kr` or `ar`). Channels are evenly spaced over a cyclic period of `2.0` in pos with `0.0` equal to channel zero and `2.0/numChans` equal to channel 1, `4.0/numChans` equal to channel 2, etc.Thus all channels will be cyclically panned through if a bipolar sawtooth wave from `-1` to `+1` is used to modulate the pos. |  
| `level` | A control rate level input. |  
| `width` | The width of the panning envelope. Nominally this is `2.0` which pans between pairs of adjacent speakers. Values greater than `2` will spread the pan over greater numbers of speakers. Values less than `1` will leave silent gaps between speakers. The absolute of this value is taken as negative values have no meaning (a width of `-1` is the same as a width of `1`). |  
| `orientation` | Should be `0` if the front is a vertex of the spanning polygon. The first speaker will be directly in front. Should be `0.5` if the front bisects a side of the spanning polygon. Then the first speaker will be the one left of center. |  


## Comparison to Pan2
Despite a certain similarity, [Pan2](../Classes/Pan2.md) and [PanAz](../Classes/PanAz.md) with 2 channels behave differently.


```
// one full cycle for PanAz: from -1 to 1
{ PanAz.ar(2, DC.ar(1), Line.ar(-1, 1, 0.1), orientation: 0) }.plot(0.1)
// comparing with Pan2
{ Pan2.ar(DC.ar(1), Line.ar(-1, 1, 0.1)) }.plot(0.1)
// to create one full cycle for Pan2, move from 1 to -1 and back to 1
{ Pan2.ar(DC.ar(1), EnvGen.ar(Env([1, -1, 1], [0.05, 0.05]))) }.plot(0.1)
```


The same in one plot window:


```
(
{
    [
        PanAz.ar(2, DC.ar(1), Line.ar(-1, 1, 0.1), orientation: 0),
        Pan2.ar(DC.ar(1), Line.ar(-1, 1, 0.1)),
        Pan2.ar(DC.ar(1), EnvGen.ar(Env([1, -1, 1], [0.05, 0.05])))
    ].flat;
}.plot(0.1)
)
```


In other words, while `Pan2` needs a position change of `2` from channel `0` to `1`


```
{ Pan2.ar(DC.ar(1), Line.ar(-1, 1, 0.1)) }.plot(0.1)
// we need a position change of 1 in PanAz:
{ PanAz.ar(2, DC.ar(1), Line.ar(0, 1, 0.1), orientation: 0) }.plot(0.1)
```


In one plot window:


```
(
{
    [
        Pan2.ar(DC.ar(1), Line.ar(-1, 1, 0.1)),
        PanAz.ar(2, DC.ar(1), Line.ar(0, 1, 0.1), orientation: 0)
    ].flat
}.plot(0.1)
)
```



## Examples

Five channel circular panning with first channel on the left

```
(
{
    PanAz.ar(
        numChans: 5,
        in: ClipNoise.ar(0.1),
        pos: LFSaw.kr(MouseX.kr(0.2, 8, 'exponential')),
        level: 0.5,
        width: 3,
        orientation: 0.5
    );
}.scope
)
```




