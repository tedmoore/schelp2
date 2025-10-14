# AbstractGridLines

*Calculates the numerical values suitable for grid lines to be used for plotting or other UI elements.*

**Categories:** GUI>Accessories

**Related:** [GridLines](../Classes/GridLines.md), [LinearGridLines](../Classes/LinearGridLines.md), [ExponentialGridLines](../Classes/ExponentialGridLines.md), [DrawGrid](../Classes/DrawGrid.md), [ControlSpec](../Classes/ControlSpec.md), [Plotter](../Classes/Plotter.md), [plot](../Reference/plot.md)

## Description

`AbstractGridLines` and its subclasses are strategy objects that find suitable intervals for plotting grid lines and labels. The data range and warping behavior (e.g. linear or exponential) are derived from the corresponding [ControlSpec](../Classes/ControlSpec.md). The instance methods of `AbstractGridLines` are used by [DrawGrid](../Classes/DrawGrid.md) (which is in turn used by [Plotter](../Classes/Plotter.md)) for getting logically spaced intervals that span the data for drawing grid lines on a plot.
`AbstractGridLines` shouldn't be instantiated directly. Instead, the [GridLines](../Classes/GridLines.md) factory class or the [ControlSpec#-grid](../Classes/ControlSpec.md#-grid) method should be used to return the appropriate `AbstractGridLines` subclass for the given spec.

```supercollider
\freq.asSpec.grid
```


Subclasses of `AbstractGridLines` correspond to the range and warp behavior of their assigned `ControlSpec`. For example, `LinearGridLines` and `ExponentialGridLines` represent data on a linear and exponential scale, respectively.

```supercollider
(
// LinearGridLines
var linGrid = ControlSpec(0, 100, \lin, units: "Time").grid;
// ExponentialGridLines
var expGrid = \freq.asSpec.grid;

DrawGrid.test(linGrid, expGrid);
)
```


This default implementation does not know anything about the data is displaying:

```supercollider
DrawGrid.test(nil, \midinote.asSpec.grid);
```


A theoretical `MidinoteGridLines` could be written that labels these correctly, shows octaves and individual notes depending on the current zoom. Or a `DegreeGridLines` could draw pitch degree grid lines behind a frequency plot.
Note that the `AbstractGridLines` does not know which axis it is to be used on and could also be used in polar plots or in 3D rendering.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `spec` | A [ControlSpec](../Classes/ControlSpec.md) that defines the numerical range, warp, and step. |  
**Returns:** An instance of this class.
> **Note:** `AbstractGridLines` shouldn't be instantiated directly. Instead, the [GridLines](../Classes/GridLines.md) factory class or the [ControlSpec#-grid](../Classes/ControlSpec.md#-grid) method should be used to return the appropriate `AbstractGridLines` subclass.



## Instance Methods

### `spec`
Get/set the `ControlSpec` that defines the numerical range, warp, and step.**Returns:** A [ControlSpec](../Classes/ControlSpec.md).### `asGrid`
Return this object.`nil.asGrid` returns a `BlankGridLines` (a subclass of `AbstractGridLines`) which produces no drawn lines. So if `nil` is passed to the **grid** argument of `DrawGrid`, no lines are drawn on the corresponding axis.### `niceNum`
Rounds a value to a logical "nice number" that is within the same order of magnitude. See the discussion below for details.**Arguments:**

| Argument | Description |
|----------|-------------|
| `val` | The value you'd like to make nicer. |  
| `round` | A boolean. Roughly speaking, rounding will allow the returned number to be above or below the input **val** (similar to a `round` operation), while when `false` the returned number will tend to be higher than **val** (similar to `ceil`). |  
**Returns:** The nice number.This method is used to support internal calculations for determining grid line values, though it may be useful for other applications.Observe the rounding behavior:
```supercollider
(
var g = GridLines([0, 10000].asSpec);
"in val / rounded / not rounded".postln;
10.collect{ 10000.rand }.sort.do({ |x|
    postf("% / % / %\n", x, g.niceNum(x, true), g.niceNum(x, false))
})
)
```

The implementation is based on: [A. S. Glassner, Ed., Graphics Gems. San Diego: Morgan Kaufmann, 1990](https://www.sciencedirect.com/book/9780080507538/graphics-gems).### `looseRange`
Returns the logical minimum and maximum that will contain the **min** and **max**, determed internally using [niceNum](#nicenum).**Arguments:**

| Argument | Description |
|----------|-------------|
| `min` | Minimum value to include in the returned range. |  
| `max` | Maximum value to include in the returned range. |  
| `ntick` | The number of lines ("ticks") you would like within the range of `[min, max]`, default: `5`. |  
**Returns:** An [Array](../Classes/Array.md) with the lower and upper bounds of the range containing your **min** and **max**, i.e. `[rangeMin, rangeMax]`.### `getParams`
Specifically for use by [DrawGrid](../Classes/DrawGrid.md). This returns a [Dictionary](../Classes/Dictionary.md) with keys: `'lines'`, an array of values where lines should be drawn, and `'labels'`, an array of 2-element arrays `[value, "formatted label"]` for each line.Note that the highest and lowest values returned don't necessarily contain your **valueMin** and **valueMax**, but rather represent the values where grid lines will be drawn by `DrawGrid` (endcap lines are subsequently drawn at the data/grid bounds).**Arguments:**

| Argument | Description |
|----------|-------------|
| `valueMin` | Minimum value of the data to be plotted. The lowest grid line value returned may be higher than this value. |  
| `valueMax` | Maximum value of the data to be plotted. The highest grid line value returned may be lower than this value. |  
| `pixelMin` | Lower bound of the grid's range, in pixels. Used to calculate the size of the available grid space when determining grid values based on **tickSpacing** (if **numTicks** is `nil`). |  
| `pixelMax` | Upper bound of the grid's range, in pixels. Used to calculate the size of the available grid space when determining grid values based on **tickSpacing** (if **numTicks** is `nil`). |  
| `numTicks` | Explicit number of ticks you would like to see on the graph (though the result is approximate). Set to `nil` if you'd like the number of ticks to be found automatically, based on **pixelMin**, **pixelMax**, and **tickSpacing**. |  
| `tickSpacing` | Minimum distance between ticks (in pixels). This value is only used when **numTicks** is `nil`. |  
**Returns:** A [Dictionary](../Classes/Dictionary.md).### `formatLabel`
Format a numerical value for display as text, rounded to a desired precision.**Arguments:**

| Argument | Description |
|----------|-------------|
| `val` | The value to round and convert to a text label. |  
| `numDecimalPlaces` | Number of decimal places to represent in the returned `String`. |  
**Returns:** A [String](../Classes/String.md).

