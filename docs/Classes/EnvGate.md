# EnvGate

*singleton fade envelope*

**Categories:** JITLib>NodeProxy

**Related:** [EnvGen](../Classes/EnvGen.md)

## Description

Convenience class for an envelope generator combining fadeTime and gate arguments.


## Class Methods


### `new`
Returns an [EnvGen](../Classes/EnvGen.md).**Arguments:**

| Argument | Description |
|----------|-------------|
| `i_level` | initial level of envelope (if set to 1, it starts open) |  
| `gate` | a gate input. if nil, EnvGate creates a [NamedControl](../Classes/NamedControl.md) named 'gate' |  
| `fadeTime` | an input for both attack and decay time. if nil, EnvGate creates a [NamedControl](../Classes/NamedControl.md) named 'fadeTime' (default time: 0.02) |  
| `doneAction` | doneAction of the [EnvGen](../Classes/EnvGen.md) |  
| `curve` | envelope curve |  

## Examples


```
a = { LPF.ar(Saw.ar(200), 600) * EnvGate.new }.play;
a.set(\fadeTime, 2);
a.release;

// the same as:
a.set(\gate, 0);

// several env gates can coexist in one synth def.
(
a = {
    var sound1 = LPF.ar(Saw.ar(80), 600) * EnvGate.new;
    var sound2 = RLPF.ar(Saw.ar(200) * 0.5, 6000 * EnvGate.new + 60, 0.1) * EnvGate.new;
    sound1 + sound2
}.play;
)
a.set(\fadeTime, 5);
a.release;
```




