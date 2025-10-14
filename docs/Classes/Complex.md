# Complex

*complex number*

**Categories:** Math

**Related:** [Polar](../Classes/Polar.md), [SimpleNumber](../Classes/SimpleNumber.md), [Float](../Classes/Float.md), [Integer](../Classes/Integer.md)

## Description

A class representing complex numbers. Note that this is a simplified representation of a complex number, which does not implement the full mathematical notion of a complex number.


## Class Methods

### `new`
Create a new complex number with the given real and imaginary parts.**Arguments:**

| Argument | Description |
|----------|-------------|
| `real` | the real part |  
| `imag` | the imaginary part |  
**Returns:** a new instance of Complex.
```supercollider
a = Complex(2, 5);
a.real;
a.imag;
```



## Instance Methods


### math support
### `real`
The real part of the number.
### `imag`
The imaginary part of the number.
### `conjugate`
the complex conjugate.
```supercollider
Complex(2, 9).conjugate
```


### `+`
Complex addition.
```supercollider
Complex(2, 9) + Complex(-6, 2)
```


### `-`
Complex subtraction
```supercollider
Complex(2, 9) - Complex(-6, 2)
```


### `*`
Complex multiplication
```supercollider
Complex(2, 9) * Complex(-6, 2)
```


### `/`
Complex division.
```supercollider
Complex(2, 9) / Complex(-6, 2)
```


### `exp`
Complex exponentiation with base e.
```supercollider
exp(Complex(2, 9))
```


```supercollider
exp(Complex(0, pi)) == -1 // Euler's formula: true
```


### `squared`
Complex self multiplication.
```supercollider
squared(Complex(2, 1))
```


### `cubed`
complex triple self multiplication.
```supercollider
cubed(Complex(2, 1))
```


### `sqrt`
Complex square rootreturns the principal root
```supercollider
Complex(4, 1.neg).sqrt

// compare...
Complex(4, 1.neg).pow(2.reciprocal)
```


### `**`

### `pow`
Complex exponentiationnot implemented for all combinations - some are mathematically ambiguous.
```supercollider
Complex(0, 2) ** 6
```


```supercollider
2.3 ** Complex(0, 2)
```


```supercollider
Complex(2, 9) ** 1.2 // not defined
```


### `<`
the comparison of just the real parts.
```supercollider
Complex(2, 9) < Complex(5, 1);
```


### `==`
the comparison assuming that the reals (floats) are fully embedded in the complex numbers
```supercollider
Complex(1, 0) == 1;
Complex(1, 5) == Complex(1, 5);
```


### `neg`
negation of both parts
```supercollider
Complex(2, 9).neg
```


### `reciprocal`
the reciprocal of a complex number
```supercollider
Complex(3, 4).reciprocal
1 / Complex(3, 4) // same, but less efficient
```


### `abs`
the absolute value of a complex number is its magnitude.
```supercollider
Complex(3, 4).abs
```


### `magnitude`
distance to the origin.
### `magnitudeApx`

### `rho`
the distance to the origin.
### `angle`, `phase`, `theta`
the angle in radians.

### conversion
### `asPoint`
Convert to a [Point](../Classes/Point.md).
### `asPolar`
Convert to a Polar
### `asInteger`
real part as [Integer](../Classes/Integer.md).
### `asFloat`
real part as [Float](../Classes/Float.md).
### `asComplex`
returns this

### misc
### `coerce`

### `hash`
a hash value
### `printOn`
print this on given stream
### `performBinaryOpOnSignal`

### `performBinaryOpOnComplex`

### `performBinaryOpOnSimpleNumber`

### `performBinaryOpOnUGen`


## Examples

Basic example:

```supercollider
a = Complex(0, 1);
a * a; // returns Complex(-1, 0);
```


Julia set approximation:

```supercollider
f = { |z| z * z + Complex(0.70176, 0.3842) };

(
var n = 80, xs = 400, ys = 400, dx = xs / n, dy = ys / n, zoom = 3, offset = -0.5;
var field = { |x| { |y| Complex(x / n + offset * zoom, y / n + offset * zoom) } ! n } ! n;

w = Window("Julia set", bounds: Rect(200, 200, xs, ys)).front;
w.view.background_(Color.black);
w.drawFunc = {
    n.do { |x|
        n.do { |y|
            var z = field[x][y];
            z = f.(z);
            field[x][y] = z;
            Pen.color = Color.gray(z.rho.linlin(-100, 100, 1, 0));
             Pen.addRect(
                Rect(x * dx, y * dy, dx, dy)
            );
            Pen.fill
        }
    }
};

fork({ 6.do { w.refresh; 2.wait } }, AppClock)
)
```




