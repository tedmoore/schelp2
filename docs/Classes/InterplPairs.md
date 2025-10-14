# InterplPairs

*envelope specification*

**Related:** [InterplEnv](../Classes/InterplEnv.md)

**Categories:** Control, Envelopes

## Description

Takes an array of [x, y] pairs and a curve value for all break points. x values can be negative (for use in indexing with negative values or signals). See [InterplEnv](../Classes/InterplEnv.md) Help for more info.

## Examples


```supercollider
a = InterplPairs([[0, 1], [1, 2], [2, 0]], \sin);
a.plot;

a = InterplPairs([[-1, 1], [0, 2], [1, 0]], \sin);
a.plot;
a.at(-0.5);
a.at(0.2);
```




