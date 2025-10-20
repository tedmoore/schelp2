# Rect

*Rectangle*

**Categories:** Geometry


## Class Methods


### `new`
Return a new Rect with the given upper left corner and dimensions.

### `newSides`
Return a new Rect with the given boundaries.

### `fromPoints`
Return a new Rect defined by the given Points.

## Instance Methods


### `left`
Get or set the value of the boundary.
### `top`
Get or set the value of the boundary.
### `right`
Get the value of the boundary.
### `bottom`
Get the value of the boundary.
### `set`
Set the boundaries to the given values.
### `setExtent`
Set the dimensions.
### `width`
Set or get the width.
### `height`
Set or get the height.
### `origin`
Return the upper left corner as a Point.
### `extent`
Return a Point whose x value is the height and whose y value is the width.
### `leftTop`
Return the upper left corner as a Point.
### `rightTop`
Return the upper right corner as a Point.
### `leftBottom`
Return the lower left corner as a Point.
### `rightBottom`
Return the lower right corner as a Point.
### `moveBy`
Returns a new Rect which is offset by x and y.
### `moveTo`
Returns a new Rect whose upper left corner is moved to (x, y).
### `moveToPoint`
Returns a new Rect whose upper left corner is moved to aPoint.
### `resizeBy`
Returns a new Rect whose dimensions have been changed by (x, y).
### `resizeTo`
Returns a new Rect whose dimensions are (x, y).
### `insetBy`
Returns a new Rect whose boundaries have been inset by (x, y). If only one argument is supplied, it will be used for both x and y.
### `insetAll`
Returns a new Rect whose boundaries have been inset by the given amounts.
### `contains`
Answers whether aPoint is in the receiver.
### `union`, `|`
Returns a new Rect which contains the receiver and aRect.
### `sect`, `&`
Returns a new Rect which is the intersection of the receiver and aRect.
### `minSize`
Return a new [Rect](../Classes/Rect.md) that ensures the minimum dimensions. If either the width or height of the receiver is smaller than the argument of this method, the new [Rect](../Classes/Rect.md) will reflect the specified minimum values accordingly.**Arguments:**

| Argument | Description |
|----------|-------------|
| `minSize` | minWidth@minHeight. |  


