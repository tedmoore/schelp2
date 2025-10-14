# T2K

*Audio rate trigger to control rate trigger converter*

**Categories:** UGens>Conversion, UGens>Triggers

**Related:** [T2A](../Classes/T2A.md), [K2A](../Classes/K2A.md), [A2K](../Classes/A2K.md)

## Description

Converts audio rate trigger into control rate trigger, using the maximum trigger level in the input during each control period.


## Class Methods

### `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | An audio rate input signal. |  

> **Note:** During initialization of the UGen graph, `T2K` will only produce a trigger if one is received on the first audio-rate input frame. Any trigger received after the first frame, but within the first block, will not be seen at initialization time. Therefore, downstream UGens will also not receive that missed trigger, which may affect their initialization state. Once the Synth runs, however, `T2K` will trigger as expected.


## Examples


```supercollider
// this does not work:
(
{
    var trig = Dust.ar(4);
    Trig.kr(trig, 0.1) * SinOsc.ar(800) * 0.1
}.play;
)

// this works:
(
{
    var trig = T2K.kr(Dust.ar(4));
    Trig.kr(trig, 0.1) * SinOsc.ar(800) * 0.1
}.play;
)
```




