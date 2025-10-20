# Pgate

*A gated stream that only advances when a particular event key is true.*

**Related:** [Pn](../Classes/Pn.md)

**Categories:** Streams-Patterns-Events>Patterns>Repetition

## Description

Pgate advances its subpattern whenever **key** is true. Pgate must be used within an Event pattern. You can either set the key manually, or use [Pn](../Classes/Pn.md).


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `pattern` | The source pattern to be filtered. |  
| `repeats` | Repeat the enclosed pattern **repeats** times. |  
| `key` | Pgate will only return the next value in the source pattern if the event that it belongs to has **key** set to true. Otherwise it will keep returning the same value. This allows for a gated effect on streams. |  

## Examples


```
// Use \step to change the octave randomly
(
Pbind(
    \degree, Pseq((0..7), inf),
    \step, Pseq([false, false, false, true, false, true, false], inf),
    \octave, Pgate(Pwhite(3, 7), inf, \step),
    \dur, 0.2
).play
)
```



```
// Pn advances Pgate each time its subpattern is repeated
(
Pbind(
    \degree, Pn(Pseq((0..7)), inf, \step),
    \mtranspose, Pgate(Pwhite(0, 5), inf, \step),
    \dur, 0.2
).play
)


// Two different Pgates advanced at two different rates
(
Pbind(

    \scale,    Scale.minor,
    \foo, Pn(Pseq((0..2)), inf, \step1),
    \degree, Pn(Pseq((0..7).mirror), inf, \step),
    \ctranspose, Pgate(Pwhite(0, 5), inf, \step) + Pgate(Pseq([0, 7, 0, -7], inf), inf, \step1),
    \dur, 0.2
).play
)
```




