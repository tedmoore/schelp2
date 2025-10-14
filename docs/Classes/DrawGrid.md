# DrawGrid

*Draws grid lines on a UserView for plotting*

**Categories:** GUI>Accessories

**Related:** [plot](../Reference/plot.md), [AbstractGridLines](../Classes/AbstractGridLines.md), [GridLines](../Classes/GridLines.md), [Plotter](../Classes/Plotter.md), [UserView](../Classes/UserView.md)

## Description

`DrawGrid` is used to draw [GridLines](../Classes/GridLines.md) and its labels on a [UserView](../Classes/UserView.md). It is notably used by [Plotter](../Classes/Plotter.md) to draw the grid lines on a plot but can also be used to add grid lines to any `UserView`, e.g. behind sliders or another GUI element.
See the example below for its [basic use in a UserView](#basic-use-in-a-userview).
Note that `DrawGrid` does not hold any reference to the `UserView` but is meant to have its `-draw` method called inside of the `-drawFunc` of the `UserView`. It only needs to know what bounds to draw the grid lines in and what the horizontal and vertical `GridLines` are.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bounds` | A [Point](../Classes/Point.md) or [Rect](../Classes/Rect.md) describing the size and position of the grid within the parent view (not including any labels). |  
| `horzGrid` | A grid lines object for the x-axis, instantiated via [GridLines](../Classes/GridLines.md), or [ControlSpec#-grid](../Classes/ControlSpec.md#-grid) method, or `nil` (resulting in no grid lines). |  
| `vertGrid` | A grid lines object for the y-axis, see **horzGrid**. |  
**Returns:** A `DrawGrid`.The warp behavior of the **horizGrid** and **vertGrid** is based on the warp behavior of the `ControlSpec` used by the grid lines object assigned to each axis.Multiple `DrawGrid` may be used to draw grids on a single [UserView](../Classes/UserView.md).See [preview](#preview) if you'd like to preview modifications of this `DrawGrid`. See [Examples](#testing-and-modifying) below.

## Instance Methods

### `draw`
This draws to the currently active [UserView](../Classes/UserView.md). This method is meant to be called from inside the [-drawFunc](../Classes/UserView.md#-drawfunc) of a `UserView`.**Returns:** `nil`See the example below for its [basic use in a UserView](#basic-use-in-a-userview), including how to manage its bounds when the enclosing view resizes.### `horzGrid`
Set the x-axis grid lines.**Arguments:**

| Argument | Description |
|----------|-------------|
| `g` | An [AbstractGridLines](../Classes/AbstractGridLines.md) subclass, instantiated via [GridLines](../Classes/GridLines.md), or [ControlSpec#-grid](../Classes/ControlSpec.md#-grid) method, or `nil` (resulting in no grid lines). |  
**Returns:** Self.### `vertGrid`
Set the y-axis grid lines.**Arguments:**

| Argument | Description |
|----------|-------------|
| `g` | An [AbstractGridLines](../Classes/AbstractGridLines.md) subclass, instantiated via [GridLines](../Classes/GridLines.md), or [ControlSpec#-grid](../Classes/ControlSpec.md#-grid) method, or `nil` (resulting in no grid lines). |  
**Returns:** Self.### `bounds`
Get/set bounds describing the extents of the grid (not including any labels).**Arguments:**

| Argument | Description |
|----------|-------------|
| `b` | A [Rect](../Classes/Rect.md). |  
**Returns:** A [Rect](../Classes/Rect.md).### `font`
Get/set the font used by the grid lines labels.**Arguments:**

| Argument | Description |
|----------|-------------|
| `f` | A [Font](../Classes/Font.md). |  
**Returns:** A [Font](../Classes/Font.md).### `fontColor`
Get/set the font color.**Arguments:**

| Argument | Description |
|----------|-------------|
| `c` | A [Color](../Classes/Color.md). |  
**Returns:** A [Color](../Classes/Color.md).### `gridColors`
Set the colors of the grid lines for each axis.**Arguments:**

| Argument | Description |
|----------|-------------|
| `colors` | An [Array](../Classes/Array.md) of two colors for the x and y grid lines, respectively. |  
**Returns:** Self.### `opacity`
Get/set opacity.**Returns:** A `Float`.### `smoothing`
A `Boolean` which turns on/off anti-aliasing. See [Pen#*smoothing](../Classes/Pen.md#*smoothing).**Returns:** A `Boolean`.### `linePattern`
Set the line dash pattern. The **value** should be a [FloatArray](../Classes/FloatArray.md) of values that specify the lengths of the alternating dashes and spaces. For example, `FloatArray[10.0, 3.0, 5.0, 3.0]`, for dashes of lengths `10.0` and `5.0` pixels, separated by spaces of `3.0` pixels. See [Pen#*lineDash](../Classes/Pen.md#*linedash).**Returns:** Self.### `x`
A `DrawGridX` object that draws the x (horizontal) axis. In general you shouldn't need to set this.**Returns:** A `DrawGridX`.### `y`
A `DrawGridY` object that draws the y (vertical) axis. In general you shouldn't need to set this.**Returns:** A `DrawGridY`.### `numTicks`
Set the *approximate* number of grid lines ("ticks") for each axis. If set, the number of ticks is fixed and `numTicks` takes precedence over [tickSpacing](#tickspacing). If `nil`, the number of grid lines change with the view size, constrained by the `tickSpacing`. Default: `nil`.See [Examples](#testing-and-modifying) below.**Arguments:**

| Argument | Description |
|----------|-------------|
| `x` | *Approximate* number of grid lines ("ticks") for the x-axis. |  
| `y` | *Approximate* number of grid lines for the y-axis. |  
The resulting number of ticks is approximate because of the underlying algorithm in [AbstractGridLines#-niceNum](../Classes/AbstractGridLines.md#-nicenum), which tries to find suitable values for the grid lines based on the data range and your requested `numTicks`. You can observe the behavior of `GridLines:-niceNum` with this snippet:
```supercollider
(
g = GridLines([0, 200].asSpec);
"requested / returned".postln;
(0, 3 .. 21).do({ |ntck|
  "% / %\n".postf(ntck, g.niceNum(ntck, true))
})
)
```

### `tickSpacing`
Set the *minimum* spacing between grid lines ("ticks") for each axis. The number of grid lines will change with the view size, but won't be spaced less than this `tickSpacing`, allowing you to control the density of grid lines. However if [numTicks](#numticks) is not `nil`, it takes precedence over `tickSpacing`.See [Examples](#testing-and-modifying) below.**Arguments:**

| Argument | Description |
|----------|-------------|
| `x` | *Minimum* spacing between grid lines ("ticks") on the x-axis (pixels, default: 64). |  
| `y` | *Minimum* spacing between grid lines on the y-axis (pixels, default: 64). |  
### `preview`
Preview this `DrawGrid` object by creating a window with a view showing the `DrawGrid` in its current state.
```supercollider
d = DrawGrid(nil, \freq.asSpec.grid, \amp.asSpec.grid);
d.linePattern_(FloatArray[10.0, 5.0, 2.0, 5.0]);
d.preview;
```

If the `DrawGrid` is modified, you can `-refresh` the returned `UserView` to see its updated state, or simply call `-preview` again to update the view (or create the preview again if the `Window` was closed). See [Examples](#testing-and-modifying) below.**Returns:** A [UserView](../Classes/UserView.md) which draws this `DrawGrid`.### `copy`
Safely make a copy of this object and its working members.**Returns:** A new `DrawGrid`.
## Examples


### Basic use in a UserView

```supercollider
(
w = Window.new.front;
u = UserView(w, w.bounds.size.asRect);

// The spec defines its preferred grid system
x = \lofreq.asSpec.grid; // x grid lines
y = \amp.asSpec.grid;    // y grid lines
i = 40;                  // grid inset

d = DrawGrid(u.bounds.size.asRect.insetBy(i), x, y);

u.drawFunc = { d.draw };
u.resize_(5);
u.onResize = { |u|
    d.bounds = u.bounds.size.asRect.insetBy(i)
};
)
```




### Testing and modifying
For previewing the look and feel of your `GridLines`, you can render your `DrawGrid` using the [preview](#preview) method:


```supercollider
(
x = [0, 10].asSpec.units_("sec");
y = [0, 1].asSpec.units_("amp");
d = DrawGrid((500@250).asRect, x.grid, y.grid);

// set its properties before testing
d.x.tickSpacing_(25);
d.linePattern_(FloatArray[10.0, 5.0, 2.0, 5.0]);

// generate a preview
~testView = d.preview;
)
```


Use `DrawGrid`'s convenience methods to set the grids' properties, then refresh the view:


```supercollider
d.tickSpacing_(50, 25).linePattern_(FloatArray[1.0]);
~testView.refresh;
```


Or just call `.preview` again and it will refresh the existing view:


```supercollider
d.linePattern_(FloatArray[10.0, 5.0, 2.0, 5.0]).preview;
```


Proterties of the individual x- and y-grids can also be accessed and changed separately:


```supercollider
// Modify the number of grid lines on each axis separately
d.x.tickSpacing_(18); // fixed (max) *density* of x ticks
d.y.numTicks_(8);     // fixed *number* of y ticks (approximate)
d.preview;            // refresh the test view

d.y.numTicks_(nil);   // numTicks = nil: auto, follows -tickSpacing
d.preview;
```






