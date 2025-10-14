# Point

*Cartesian point*

**Related:** [Polar](../Classes/Polar.md), [Complex](../Classes/Complex.md)

**Categories:** Geometry

## Description

Defines a point on the Cartesian plane.


## Class Methods

### `new`
Defines a new point.

## Instance Methods


### Accessing
### `x`
Get or set the x coordinate value.
### `y`
Get or set the y coordinate value.
### `set`
Sets the point x and y values.

### Testing
### `==`
Answers a Boolean whether the receiver equals the argument.
### `hash`
Returns a hash value for the receiver.

### Math
### `+`
Addition.
### `-`
Subtraction.
### `*`
Multiplication.
### `/`
Division.
### `translate`
Addition by a Point.
### `scale`
Multiplication by a Point.
### `rotate`
Rotation about the origin by the angle given in radians.
### `abs`
Absolute value of the point.
### `rho`
Return the polar coordinate radius of the receiver.
### `theta`
Return the polar coordinate angle of the receiver.
### `dist`
Return the distance from the receiver to aPoint.
### `transpose`
Return a Point whose x and y coordinates are swapped.
### `round`
Round the coordinate values to a multiple of quantum.
### `trunc`
Truncate the coordinate values to a multiple of quantum.

### Conversion
### `asPoint`
Returns the receiver.
### `asComplex`
Returns a complex number with x as the real part and y as the imaginary part.
### `asString`
Return a string representing the receiver.


