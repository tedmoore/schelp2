# PulseCount

*Pulse counter.*

**Related:** [Stepper](../Classes/Stepper.md)

**Categories:** UGens>Triggers

## Description

Each trigger increments a counter which is output as a signal.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `trig` | Trigger. Trigger can be any signal. A trigger happens when the signal changes from non-positive to positive. |  
| `reset` | Resets the counter to zero when triggered. |  

## Examples


```supercollider
SynthDef("help-PulseCount", { |out = 0|
    Out.ar(out,
        SinOsc.ar(
            PulseCount.ar(Impulse.ar(10), Impulse.ar(0.4)) * 200,
            0, 0.05
        )
    )
}).play;
```




