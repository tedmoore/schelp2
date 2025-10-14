# VarLag

*Variable shaped lag*

**Related:** [Lag](../Classes/Lag.md), [Ramp](../Classes/Ramp.md), [Slew](../Classes/Slew.md)

**Categories:** UGens>Filters>Linear

## Description

Similar to [Lag](../Classes/Lag.md) but with other curve shapes than exponential. A change on the input will take the specified time to reach the new value. Useful for smoothing out control (not audio) signals.
> **⚠️ Warning:** `VarLag.ar` currently accepts audio-rate input, but the underlying implementation treats the input as control rate. Effectively, then, the "sampling rate" of VarLag's input is `ControlRate.ir` or `server.sampleRate / server.options.blockSize`, and the maximum safe frequency to feed into VarLag is half of this. VarLag does not currently yield correct results for full-bandwidth audio-rate signals. Use `VarLag.ar` at your own risk.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `time` | Lag time in seconds. |  
| `curvature` | Control curvature if **warp** input is 5 (default). 0 means linear, positive and negative numbers curve the segment up and down. |  
| `warp` | Determines the shape. The possible values are:| `\step` |  | flat segment | 
| --- | --- | --- || `\linear` | `\lin` | linear segment, the default | | `\exponential` | `\exp` | natural exponential growth and decay. In this case, the levels must all be nonzero and the have the same sign. | | `\sine` | `\sin` | sinusoidal S shaped segment. | | `\welch` | `\wel` | sinusoidal segment shaped like the sides of a Welch window. | | `\squared` | `\sqr` | squared segment | | `\cubed` | `\cub` | cubed segment | All values above will ignore **curvature** input.
> **Note:** When controlling this from the outside, use `Env.shapeNumber(symbol)` to get the numeric value for each shape. |  
| `start` | Initial value. If not specified, same as the input signal. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```supercollider
(
// used to lag pitch
{
    SinOsc.ar(                              // sine wave
        VarLag.kr(                            // lag the modulator
            LFPulse.kr(1).range(100, 400),   // frequency modulator
            0.2,                            // lag time
            Line.kr(-8, 8, 15, doneAction: Done.freeSelf) // modulate shape
        ),
        0,                                  // sine phase
        0.3                                 // sine amplitude
    )
}.play
)
```



```supercollider
(
x = play { |amp = 0, time = 0, curve = 0, warp = 5|
    PinkNoise.ar(VarLag.kr(amp, time, curve, warp) ! 2)
}
)

x.set(\amp, 1, \time, 5, \warp, Env.shapeNumber(\sin)) // s-shaped curve up
x.set(\amp, 0, \time, 1, \warp, Env.shapeNumber(\lin)) // linear down

x.set(\amp, 1, \time, 2, \warp, 5, \curve, 7); // slow curvature
x.set(\amp, 0, \time, 0);

x.set(\amp, 1, \time, 2, \warp, 5, \curve, -7); // fast curvature
x.set(\amp, 0, \time, 0);

x.free;
```




