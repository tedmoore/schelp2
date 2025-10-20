# XFade2

*Equal power two channel cross fade.*

**Related:** [LinXFade2](../Classes/LinXFade2.md)

**Categories:** UGens>Multichannel>Select

## Description

Two channel equal power crossfader.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `inA` | Input signal A. |  
| `inB` | Input signal B. |  
| `pan` | Crossfade position from -1 to +1. |  
| `level` | A control rate level input. |  

## Examples


```
{ XFade2.ar(Saw.ar, SinOsc.ar, LFTri.kr(0.1)) }.play
```




