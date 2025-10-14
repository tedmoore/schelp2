# Trig

*Timed trigger.*

**Related:** [Trig1](../Classes/Trig1.md)

**Categories:** UGens>Triggers

## Description

When a nonpositive to positive transition occurs at the input, Trig outputs the level of the triggering input for the specified duration, otherwise it outputs zero.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | Trigger. Trigger can be any signal. A trigger happens when the signal changes from non-positive to positive. |  
| `dur` | Duration of the trigger output. |  

## Examples


```supercollider
{ Trig.ar(Dust.ar(1), 0.2) * FSinOsc.ar(800, 0.5) }.play

{ Trig.ar(Dust.ar(4), 0.1) }.play
```




