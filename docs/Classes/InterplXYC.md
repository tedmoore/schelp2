# InterplXYC

*envelope specification*

**Related:** [InterplEnv](../Classes/InterplEnv.md)

**Categories:** Control, Envelopes

## Description

Takes sets of x, y and curve values and returns a new instance of InterplEnv. x values can be negative (for use in indexing with negative values or signals). See [InterplEnv](../Classes/InterplEnv.md) Help for more info.

## Examples


```supercollider
a = InterplXYC([0, 0, \lin], [1, 2, \sin], [2, 0]);
a.plot;

a = InterplXYC([[-1, 1, \sin], [0, 2, \lin], [1, 0]]);
a.plot;
a.at(-0.5);
a.at(0.2);
```




