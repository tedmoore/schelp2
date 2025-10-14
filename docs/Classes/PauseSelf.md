# PauseSelf

*When triggered, pause enclosing synth.*

**Related:** [FreeSelf](../Classes/FreeSelf.md)

**Categories:** UGens>Synth control

## Description

Pause enclosing synth when input signal crosses from non-positive to positive.


## Class Methods

### `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  

## Examples


```supercollider
(
SynthDef("pauseSelf-help", { |out, t_trig|
    PauseSelf.kr(t_trig);
    Out.ar(out, SinOsc.ar(400, 0, 0.2));
}).add;
)

s.sendMsg("/s_new", "pauseSelf-help", 1731);
s.sendMsg("/n_set", 1731, \t_trig, 1);
s.sendMsg("/n_run", 1731, 1);
s.sendMsg("/n_set", 1731, \t_trig, 1);
s.sendMsg("/n_free", 1731);
```




