# ModDif

*Minimum difference of two values in modulo arithmetics*

**Related:** [Clip](../Classes/Clip.md), [Wrap](../Classes/Wrap.md)

**Categories:** UGens>Maths

## Description

Returns the minimum difference of two values in modulo arithmetics. On a circle, there are two distances between two points. This UGen returns the smaller value of the two.

```
{ var a = Line.ar(0, 4, 0.01), d = ModDif.ar(a); [a, d] }.plot;
{ var a = Line.ar(0, 4, 0.01); ModDif.ar(a, 0, (1..4)) }.plot;
{ var a = Line.ar(0, 4, 0.01); ModDif.ar(a, (0, 0.25 .. 1), 1) }.plot;
```




## Class Methods


### `ar`, `kr`, `ir`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `x` | First input value |  
| `y` | Second input value |  
| `mod` | Modulo (maximum value, double of the maximal difference).
```
// different moduli
(
{
    var sig = LFSaw.ar(10);
    var dist = ModDif.kr(sig, 0, (0..8) * MouseX.kr(0, 1/5));
    Splay.ar(SinOsc.ar(dist * 4000 + 400)) * 0.1
}.play;
)

// wrapping amplitude crossfade
(
{
    var numChan = 12;
    var x = SinOsc.ar({ rrand(300.0, 800.0) } ! numChan);
    var dist = ModDif.kr(MouseX.kr(0, numChan * 2), (0..numChan-1), numChan);
    x = x * max(0, 1 - dist);
    Splay.ar(x) * 0.1
}.play;
)
``` |  


