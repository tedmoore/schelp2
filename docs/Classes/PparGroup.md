# PparGroup

*Starts a new ParGroup and plays the pattern in this group*

**Related:** [ParGroup](../Classes/ParGroup.md), [Pgroup](../Classes/Pgroup.md)

**Categories:** Streams-Patterns-Events>Patterns>Server Control

## Description

The class has a semantics similar to [Pgroup](../Classes/Pgroup.md), but instead of a Group, it creates a ParGroup on the server.

## Examples


```
(
var p, q, r, o;
p = Pbind(\degree, Prand((0..7), 12), \dur, 0.3, \legato, 0.2);

PparGroup(p).play;

// post the node structure:
fork {
    s.queryAllNodes;
    3.wait;
    s.queryAllNodes;
    2.wait;
    s.queryAllNodes;
}
)
```




