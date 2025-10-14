# Line

*Line generator.*

**Related:** [XLine](../Classes/XLine.md)

**Categories:** UGens>Envelopes

## Description

Generates a line from the start value to the end value.


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
| `doneAction` | A doneAction to be evaluated when the Line is completed. See[Done](../Classes/Done.md) for more detail. |  

## Examples


```supercollider
// XLine is usually better than Line for frequency
play({ SinOsc.ar(Line.kr(200, 17000, 10), 0, 0.1) });
```




