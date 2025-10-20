# Gate

*Gate or hold.*

**Related:** [Latch](../Classes/Latch.md)

**Categories:** UGens>Triggers

## Description

Allows input signal value to pass when gate is positive, otherwise holds last value.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `trig` | Gate - can be any signal. The output is held fixed when this is non-positive. |  

## Examples


```
s.boot;
// Control rate so as not to whack your speakers with DC
{ Gate.kr(WhiteNoise.kr(1, 0), LFPulse.kr(1.333, 0.5)) }.scope(zoom: 20);
```




