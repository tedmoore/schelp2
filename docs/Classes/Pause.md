# Pause

*When triggered, pauses a node.*

**Related:** [Free](../Classes/Free.md)

**Categories:** UGens>Synth control

## Description

When triggered, pauses a node.


## Class Methods

### `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `gate` | When gate is 0, node is paused, when 1 it runs. |  
| `id` | Node to be paused. |  

## Examples


```supercollider
s.boot;

SynthDef(\a, { Out.ar(0, SinOsc.ar(800, 0, 0.2)) }).add;

SynthDef(\b, { |gate = 1| Out.ar(1, PinkNoise.ar(0.3)); Pause.kr(gate, 1001) }).add;

s.sendMsg(\s_new, \a, 1001, 0, 0);

s.sendMsg(\s_new, \b, 1002, 0, 0);

s.sendMsg(\n_set, 1002, \gate, 0);

s.sendMsg(\n_set, 1002, \gate, 1);
```




