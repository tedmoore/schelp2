# Ppar

*embed event streams in parallel*

**Related:** [Ptpar](../Classes/Ptpar.md), [Pgpar](../Classes/Pgpar.md), [Pbus](../Classes/Pbus.md), [Pgroup](../Classes/Pgroup.md)

**Categories:** Streams-Patterns-Events>Patterns>Parallel

## Description

Embeds several event streams so that they form a single output stream with all their events in temporal order. When one stream ends, the other streams are further embedded until all have ended.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `list` | list of patterns or streams. |  
| `repeats` | repeat the whole pattern n times. |  

## Examples


```supercollider
// see the delta values in the resulting events
(
var a, b, c, t;
a = Pbind(\x, Pseq([1, 2, 3, 4]), \dur, 1);
b = Pbind(\x, Pseq([10, 20, 30, 40]), \dur, 0.4);
c = Ppar([a, b]);
t = c.asStream;
20.do({ t.next(Event.default).postln });
)

// sound example
(
var a, b;
a = Pbind(\note, Pseq([7, 4, 0], 4), \dur, Pseq([1, 0.5, 1.5], inf));
b = Pbind(\note, Pseq([5, 10, 12], 4), \dur, 1);
Ppar([a, b]).play;
)
```




