# Ramp

*Break a continuous signal into line segments*

**Related:** [Lag](../Classes/Lag.md), [VarLag](../Classes/VarLag.md), [Slew](../Classes/Slew.md)

**Categories:** UGens>Filters>Linear

## Description

Break a continuous signal into linearly interpolated segments with specific durations.
Feeding Ramp with noise is similar to [LFNoise1](../Classes/LFNoise1.md)

```supercollider
Ramp.kr(WhiteNoise.kr(1), 0.5)
```


is equal to:

```supercollider
LFNoise1.kr(1 / 0.5)
```


For smoothing out control signals, take a look at [Lag](../Classes/Lag.md) and [VarLag](../Classes/VarLag.md)


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `lagTime` | segment duration in seconds. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```supercollider
s.boot;
(
// used to lag pitch
{
    SinOsc.ar(        // sine wave
        Ramp.kr(            // lag the modulator
            LFPulse.kr(4, 0, 0.5, 50, 400),    // frequency modulator
            Line.kr(0, 1, 15)                // modulate lag time
        ),
        0,    // phase
        0.3    // sine amplitude
    )
}.scope;
)

// Compare
(
var pulse;
{
    pulse = LFPulse.kr(8.772);
    Out.kr(0, [Ramp.kr(pulse, 0.025), Lag.kr(pulse, 0.025), pulse]);
}.play;
s.scope(3, bufsize: 44100, rate: \control, zoom: 40);
)
```




