# LeakDC

*Remove DC*

**Related:** [DC](../Classes/DC.md)

**Categories:** UGens>Filters>Linear

## Description

This is a linear filter that removes DC bias from a signal. Specifically, this is a one-pole highpass filter implementing the formula `y[n] = x[n] - x[n-1] + coef * y[n-1]`. The frequency response of this filter is dependent on the sample rate of the server and the calculation rate of the UGen.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `coef` | Leak coefficient. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```
(
{
    var a;
    a = LFPulse.ar(800, 0.5, 0.5, 0.5);
    [a, LeakDC.ar(a, 0.995)]
}.scope(bufsize: 22050)
)
```




