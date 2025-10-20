# LinXFade2

*Two channel linear crossfade.*

**Related:** [XFade2](../Classes/XFade2.md)

**Categories:** UGens>Multichannel>Select

## Description

Two channel linear crossfader.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `inA` | Input signal A. |  
| `inB` | Input signal B. |  
| `pan` | Cross fade position from -1 to +1. |  
| `level` | A control rate level input. |  

## Examples


```
play({ LinXFade2.ar(FSinOsc.ar(800, 0, 0.2), PinkNoise.ar(0.2), FSinOsc.kr(1)) });
```




