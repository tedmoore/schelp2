# GridLines

*A factory class for AbstractGridLines*

**Categories:** GUI>Accessories

**Related:** [AbstractGridLines](../Classes/AbstractGridLines.md), [LinearGridLines](../Classes/LinearGridLines.md), [ExponentialGridLines](../Classes/ExponentialGridLines.md), [DrawGrid](../Classes/DrawGrid.md), [ControlSpec](../Classes/ControlSpec.md), [Plotter](../Classes/Plotter.md), [plot](../Reference/plot.md)

## Description

`GridLines` is a factory class that returns the appropriate subclass of [AbstractGridLines](../Classes/AbstractGridLines.md) for a given `ControlSpec`, e.g. a [LinearGridLines](../Classes/LinearGridLines.md) or [ExponentialGridLines](../Classes/ExponentialGridLines.md) for a linear or exponential spec, respectively. See those help files for examples and information on modifying their behavior.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `spec` | A [ControlSpec](../Classes/ControlSpec.md) that defines the minimum and maximum values, warp and step. |  
**Returns:** A subclass of [AbstractGridLines](../Classes/AbstractGridLines.md), e.g. [LinearGridLines](../Classes/LinearGridLines.md) or [ExponentialGridLines](../Classes/ExponentialGridLines.md).

