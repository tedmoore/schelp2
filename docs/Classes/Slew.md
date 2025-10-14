# Slew

*Slew rate limiter.*

**Related:** [Slope](../Classes/Slope.md), [Ramp](../Classes/Ramp.md), [Lag](../Classes/Lag.md), [VarLag](../Classes/VarLag.md)

**Categories:** UGens>Filters>Nonlinear

## Description

Limits the slope of an input signal. The slope is expressed in units per second.
For smoothing out control signals, take a look at [Lag](../Classes/Lag.md) and [VarLag](../Classes/VarLag.md)


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `up` | Maximum upward slope in units per second. |  
| `dn` | Maximum downward slope in units per second. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```supercollider
(
{
    z = LFPulse.ar(800);
    [z, Slew.ar(z, 4000, 4000)]
}.plot)



Has the effect of removing transients and higher frequencies.
(
{

    z = Saw.ar(800, mul: 0.2);
    Slew.ar(z, 400, 400)

}.play
)
```




