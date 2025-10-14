# Ptpar

*embed event streams in parallel, with time offset*

**Related:** [Ppar](../Classes/Ppar.md)

**Categories:** Streams-Patterns-Events>Patterns>Parallel

## Description

Embeds several event streams so that they form a single output stream with all their events in temporal order, providing a global **offset** for each. When one stream ends, the other streams are further embedded until all have ended.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `list` | list of pairs of times and patterns: [time, pat, time, pat ..].
> **Note:** times are in beats and depend on the tempo of the [TempoClock](../Classes/TempoClock.md) in use. |  
| `repeats` | repeat the whole pattern n times. |  

## Examples


```supercollider
// see the delta values in the resulting events
(
var a, b, c, t;
a = Pbind(\x, Pseq([1, 2, 3, 4]), \dur, 1);
b = Pbind(\x, Pseq([10, 20, 30, 40]), \dur, 0.4);
c = Ptpar([0.0, a, 1.3, b]);
t = c.asStream;
20.do({ t.next(Event.default).postln });
)

// sound example
(
var a, b;
a = Pbind(\note, Pseq([7, 4, 0], 4), \dur, Pseq([1, 0.5, 1.5], inf));
b = Pbind(\note, Pseq([5, 10, 12], 4), \dur, 1);
Ptpar([0.0, a, 1.3, b]).play;
)
```




