# Lag2

*Exponential lag*

**Related:** [Lag](../Classes/Lag.md), [Lag3](../Classes/Lag3.md), [Ramp](../Classes/Ramp.md), [Lag2UD](../Classes/Lag2UD.md)

**Categories:** UGens>Filters>Linear

## Description

Lag2 is equivalent to `Lag.kr(Lag.kr(in, time), time)`, thus resulting in a smoother transition. This saves on CPU as you only have to calculate the decay factor once instead of twice. See [Lag](../Classes/Lag.md) for more details.


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


```supercollider
(
// used to lag pitch
{
    SinOsc.ar(        // sine wave
        Lag2.kr(            // lag the modulator
            LFPulse.kr(4, 0, 0.5, 50, 400),    // frequency modulator
            Line.kr(0, 1, 15)                // modulate lag time
        ),
        0,    // phase
        0.3    // sine amplitude
    )
}.play
)
```




