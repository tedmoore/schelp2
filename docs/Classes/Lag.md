# Lag

*Exponential lag*

**Related:** [Lag2](../Classes/Lag2.md), [Lag3](../Classes/Lag3.md), [VarLag](../Classes/VarLag.md), [LagUD](../Classes/LagUD.md)

**Categories:** UGens>Filters>Linear

## Description

This is essentially the same as [OnePole](../Classes/OnePole.md) except that instead of supplying the coefficient directly, it is calculated from a 60 dB lag time. This is the time required for the filter to converge to within 0.01% of a value. This is useful for smoothing out control signals.
For linear and other alternatives, see [VarLag](../Classes/VarLag.md).


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `lagTime` | 60 dB lag time in seconds. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```
(
// used to lag pitch
{
    SinOsc.ar(                              // sine wave
        Lag.kr(                             // lag the modulator
            LFPulse.kr(4, 0, 0.5, 50, 400), // frequency modulator
            Line.kr(0, 1, 15)               // modulate lag time
        ),
        0,                                  // phase
        0.3                                 // sine amplitude
    )
}.play
)
```




