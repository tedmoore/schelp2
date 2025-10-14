# Pseg

*timed embedding of values*

**Related:** [Ptime](../Classes/Ptime.md), [Pstep](../Classes/Pstep.md), [Env](../Classes/Env.md)

**Categories:** Streams-Patterns-Events>Patterns>Time

## Description

Pseg defines a function of time as a breakpoint envelope using the same parameters as [Env](../Classes/Env.md). These patterns can be used to describe tempo or dynamic variations independent of the rhythmic patterns that express them.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `levels` | A [Pattern](../Classes/Pattern.md) that returns the levels. The first level is the initial value of the envelope, all subsequent values are interpolated. |  
| `durs` | A [Pattern](../Classes/Pattern.md) that returns segments durations in beats. |  
| `curves` | a [Symbol](../Classes/Symbol.md), [Float](../Classes/Float.md), or an [Array](../Classes/Array.md) of those. Determines the shape of the segments. |  
| `repeats` | a number.The possible values are:| `\step` |  | flat segments. | 
| --- | --- | --- || `\linear` | `\lin` | linear segments, the default. | | `\exponential` | `\exp` | natural exponential growth and decay. In this case, the levels must all be nonzero and the have the same sign. | | `\sine` | `\sin` | sinusoidal S shaped segments. | | `\welch` | `\wel` | sinusoidal segments shaped like the sides of a Welch window. | | `\squared` | `\sqr` | squared segment. | | `\cubed` | `\cub` | cubed segment. | | a [Float](../Classes/Float.md) |  | a curvature value for all segments. 0 means linear, positive and negative numbers curve the segment up and down. | | an [Array](../Classes/Array.md) of symbols or floats |  | curvature values for each segment. | |  

## Examples


```supercollider
// change a parameter
(
Pbind(
    \note, Pseg(Pseq([1, 5], inf), Pseq([4, 1], inf), \linear),
    \dur, 0.1
).play;
)

(
Pbind(
    \freq, Pseg(Pseq([400, 1500], inf), Pseq([4, 4], inf), Pseq([\linear, \exp], inf)),
    \dur, 0.1
).play;
)
```




