# Pdrop

*skips (drops) the first n events from a pattern*

**Related:** [Pclutch](../Classes/Pclutch.md)

**Categories:** Streams-Patterns-Events>Patterns

## Description

Skips an initial (count) number of events from a pattern.


## Class Methods


### `new`
drops **count** elements of the **pattern** from the stream.
## Examples


```
(
p = Pdrop(2, Pseq([1, 2, 3, 4], 6));
q = p.asStream.nextN(20).postln;
)
```




