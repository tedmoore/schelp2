# PdegreeToKey

*index into a scale*

**Related:** [Scale](../Classes/Scale.md)

**Categories:** Streams-Patterns-Events>Patterns>Math

## Description

Returns a series of notes derived from an index into a scale.


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `pattern` | integer index into the scale. |  
| `scale` | an array or pattern. If a pattern, it streams the scales accordingly. |  
| `stepsPerOctave` | the number of steps per octave in the scale. |  

## Examples


```
(
Pbind(\note, PdegreeToKey(
            Pseq([1, 2, 3, 2, 5, 4, 3, 4, 2, 1], 2),
            #[0, 2, 3, 6, 7, 9],
            12
        ),
    \dur, 0.25
).play;
)


(
var scales;
scales = #[[0, 2, 3, 6, 7, 9], [0, 1, 5, 6, 7, 9, 11], [0, 2, 3]];
Pbind(\note, PdegreeToKey(
            Pseq([1, 2, 3, 2, 5, 4, 3, 4, 2, 1], 4),
            Pdup(3, Prand(scales, inf)),
            12
        ),
    \dur, 0.25
).play;
)
```




