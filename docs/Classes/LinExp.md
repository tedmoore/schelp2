# LinExp

*Map a linear range to an exponential range*

**Related:** [LinLin](../Classes/LinLin.md)

**Categories:** UGens>Maths

## Description

Converts a linear range of values to an exponential range of values.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal to convert. |  
| `srclo` | Lower limit of input range. |  
| `srchi` | Upper limit of input range. |  
| `dstlo` | Lower limit of output range. |  
| `dsthi` | Upper limit of output range. |  
The `dstlo` and `dsthi` arguments must be nonzero and have the same sign.
## Examples


```supercollider
// compare:
(
{
    var mod = SinOsc.kr(Line.kr(1, 10, 10));
    SinOsc.ar(mod * 400 + 500) * 0.1
}.play;
)

(
{
    var mod = SinOsc.kr(Line.kr(1, 10, 10));
    SinOsc.ar(LinExp.kr(mod, -1, 1, 100, 900)) * 0.1
}.play;
)

// modulating destination values.
(
{
    var mod = LFNoise2.ar(80);
    SinOsc.ar(LinExp.ar(mod, -1, 1, MouseX.kr(200, 8000, 1), MouseY.kr(200, 8000, 1))) * 0.1
}.play;
)
```


`linexp` and `exprange` can be used to create a LinExp implicitly from a ugen, mapping its output values from linear range to an exponential one. The rate is derived from the ugen.

```supercollider
// linexp
(
{
    var mod = LFNoise2.ar(80);
    SinOsc.ar(mod.linexp(-1, 1, MouseX.kr(200, 8000, 1), MouseY.kr(200, 8000, 1))) * 0.1
}.play;
)

// exprange
(
{
    var mod = LFNoise2.ar(80).exprange(MouseX.kr(200, 8000, 1), MouseY.kr(200, 8000, 1));
    SinOsc.ar(mod) * 0.1
}.play;
)
```




