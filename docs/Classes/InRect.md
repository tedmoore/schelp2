# InRect

*Test if a point is within a given rectangle.*

**Related:** [InRange](../Classes/InRange.md), [Schmidt](../Classes/Schmidt.md)

**Categories:** UGens>Maths

## Description

A pair of signals x and y are treated as a point (x, y) in 2-D; if they fall within the bounds of the rectangle, then this UGen outputs a one; else it outputs zero.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `x` | X component signal. If `InRect` is running at audio rate, **x** must also be audio rate. |  
| `y` | Y component signal. If `InRect` is running at audio rate, **y** must also be audio rate. |  
| `rect` | A [Rect](../Classes/Rect.md) which defines the rectangular region to monitor; note that Rects are in screen co-ordinates, so the top is smaller than the bottom. The Rect is created once and cannot be modulated. |  

## Examples


```supercollider
// We'll hear the sawtooth wave when the two sine oscillators are both in the region x = 0.0 to 0.5, y = 0.5 to 1.0
(
{
    InRect.ar(
        SinOsc.ar(1), SinOsc.ar(1.3), Rect(0, 0.5, 0.5, 0.5)
    ) * LFSaw.ar(44, 0, 0.1)
}.play
)

// Stereo effect
(
{
    InRect.ar(
        LFNoise0.ar([140, 141]), LFNoise0.ar(143), Rect(0, 0, 0.5, 1)
    ).lag(0.1) * LFSaw.ar(SinOsc.ar(10, 0, 5, 400), 0, 0.1)
}.play
)

// For the Rect, create as left, 'top', width, height;
r = Rect(0, 0, 1, 1)

r.left
r.top
r.right
r.bottom
```




