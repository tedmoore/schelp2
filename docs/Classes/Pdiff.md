# Pdiff

*returns the difference between the current and previous values of an enclosed pattern*

**Related:** [Pseries](../Classes/Pseries.md)

**Categories:** Streams-Patterns-Events>Patterns

## Description

A pattern that returns the difference between the current and previous values of an enclosed pattern.

## Examples


```
p = Pbind(
    \degree, Pxrand([0, 2, 3, 4, 6, 7], 12),
    \dur, Pdiff(Pkey(\degree)).abs/4,
).play;
```




