# ExponentialGridLines

*Calculates the numerical values suitable for exponentially-spaced grid lines to be used for plotting or other UI elements.*

**Categories:** GUI>Accessories

**Related:** [GridLines](../Classes/GridLines.md), [AbstractGridLines](../Classes/AbstractGridLines.md), [LinearGridLines](../Classes/LinearGridLines.md), [DrawGrid](../Classes/DrawGrid.md), [ControlSpec](../Classes/ControlSpec.md), [Plotter](../Classes/Plotter.md), [plot](../Reference/plot.md)

## Description

`ExponentialGridLines` is a strategy object that finds suitable intervals for plotting grid lines and labels. The values span the range defined by a corresponding [ControlSpec](../Classes/ControlSpec.md). Most of the functionality of `ExponentialGridLines` is inherited from its superclass, [AbstractGridLines](../Classes/AbstractGridLines.md). The instance methods are used by [DrawGrid](../Classes/DrawGrid.md) (which is in turn used by [Plotter](../Classes/Plotter.md)) which handles the drawing of the lines and labels.
`ExponentialGridLines` isn't usually instantiated directly, but rather by the [GridLines](../Classes/GridLines.md) factory class or the [ControlSpec#-grid](../Classes/ControlSpec.md#-grid) method which return the appropriate `AbstractGridLines` subclass for the given spec.

```supercollider
(
// LinearGridLines
var linGrid = ControlSpec(0, 100, \lin, units: "Time").grid;
// ExponentialGridLines
var expGrid = \freq.asSpec.grid;

DrawGrid.test(linGrid, expGrid);
)
```




## Class Methods



## Instance Methods



