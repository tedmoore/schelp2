# Latch

*Sample and hold*

**Related:** [Gate](../Classes/Gate.md)

**Categories:** UGens>Triggers

## Description

Holds input signal value when triggered. Latch will output 0 until it receives its first trigger.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `trig` | Trigger. Trigger can be any signal. A trigger happens when the signal changes from non-positive to positive. |  

## Examples


```
{ Blip.ar(Latch.ar(WhiteNoise.ar, Impulse.ar(9)) * 400 + 500, 4, 0.2) }.play;
```


The above is just meant as example. LFNoise0 is a faster way to generate random steps:

```
{ Blip.ar(LFNoise0.kr(9, 400, 500), 4, 0.2) }.play;
```




