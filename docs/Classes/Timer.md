# Timer

*Returns time since last triggered.*

**Categories:** UGens>Triggers

## Description

When triggered, Timer measures the time (in seconds) elapsed since the previous trigger, and outputs this time value as a constant. Its output will not change until the next trigger. The initial value is 0.
If you need the time since the last trigger, where the time is continually updated, see [Sweep](../Classes/Sweep.md).


## Class Methods



### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `trig` | A trigger occurs when trig signal crosses from non-positive to positive. |  

## Examples


```
// using timer to modulate sine frequency: the slower the trigger is the higher the frequency
(
{ var trig;
    trig = Impulse.kr(MouseX.kr(0.5, 20, 1));
    SinOsc.ar(Timer.kr(trig) * 500 + 500, 0, 0.2)
}.play;
)
```




