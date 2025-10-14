# Pindex

*pattern that indexes into an array*

**Related:** [Pswitch](../Classes/Pswitch.md)

**Categories:** Streams-Patterns-Events>Patterns>List>Indexing

## Description

This allows an [ArrayedCollection](../Classes/ArrayedCollection.md) to be accessed within patterns.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `listPat` | the array. Can be a [Pattern](../Classes/Pattern.md). |  
| `indexPat` | the value to retrieve. Can be a [Pattern](../Classes/Pattern.md). |  
| `repeats` | specifies the number of repeats. |  

## Examples


```supercollider
(
SynthDef(\help_pindex, { |out, amp = 0.1, freq = 440, gate = 1|
    var son = Saw.ar(freq * [0.99, 1, 1.01]).mean;
    son = son * EnvGen.ar(Env.adsr, gate: gate, doneAction: Done.freeSelf);
    Out.ar(out, son.dup * amp);
}).add;
)

(
var data = [7, 13, 12, 2, 2, 2, 5];
var indices = [0, 0, 2, 0, 4, 6, 7];
Pbind(
    \instrument, \help_pindex,
    \choice, Prand(indices, inf),
    \degree, Pindex(data, Pkey(\choice), inf),
    \dur, 0.7
).play
)
```




