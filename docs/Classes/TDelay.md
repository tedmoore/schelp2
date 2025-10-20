# TDelay

*Trigger delay.*

**Categories:** UGens>Triggers, UGens>Delays

## Description

Delays a trigger by a given time. Any triggers which arrive in the time between an input trigger and its delayed output, are ignored.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | Input trigger signal. |  
| `dur` | Delay time in seconds. |  

## Examples


```
(
{
    z = Impulse.ar(2);
    [z * 0.1, ToggleFF.ar(TDelay.ar(z, 0.5)) * SinOsc.ar(mul: 0.1)]
}.scope)
```




