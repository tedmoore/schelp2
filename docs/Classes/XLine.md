# XLine

*Exponential line generator.*

**Related:** [Line](../Classes/Line.md)

**Categories:** UGens>Envelopes

## Description

Generates an exponential curve from the start value to the end value. Both the start and end values must be non-zero and have the same sign.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `start` | Starting value. |  
| `end` | Ending value. |  
| `dur` | Duration in seconds. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  
| `doneAction` | A doneAction to be evaluated when the line is completed. See[Done](../Classes/Done.md) for more detail. |  

## Examples


```
play({ SinOsc.ar(XLine.kr(200, 17000, 10), 0, 0.1) });
```




