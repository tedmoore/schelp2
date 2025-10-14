# Slope

*Slope of signal*

**Categories:** UGens>Analysis, UGens>Filters>Linear, UGens>Maths

## Description

Measures the rate of change per second of a signal. Formula implemented is:

```supercollider
out[i] = (in[i] - in[i-1]) * sampling_rate
```




## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | Input signal to measure. |  
| `mul` |  |  
| `add` |  |  

## Examples


```supercollider
(
{
    var a, b, c, scale;
    a = LFNoise2.ar(2000);  // quadratic noise
    b = Slope.ar(a);        // first derivative produces line segments
    c = Slope.ar(b);        // second derivative produces constant segments
    scale = 0.0002; // needed to scale back to +/- 1.0
    [a, b * scale, c * scale.squared]
}.plot
)
```


For another example of Slope see [AbstractFunction#-hypot](../Classes/AbstractFunction.md#-hypot).

