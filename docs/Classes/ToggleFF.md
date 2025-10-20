# ToggleFF

*Toggle flip flop.*

**Related:** [SetResetFF](../Classes/SetResetFF.md)

**Categories:** UGens>Triggers

## Description

Toggles between 0 and 1 upon receiving a trigger.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `trig` | Trigger input. |  

## Examples


```
(
play({
    SinOsc.ar((ToggleFF.ar(Dust.ar(XLine.kr(1, 1000, 60))) * 400) + 800, 0, 0.1)
}))
```




