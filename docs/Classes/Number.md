# Number

*Mathematical quantity*

**Categories:** Math

## Description

Number represents a mathematical quantity.


## Instance Methods


### Math

### `+`
Addition.

### `-`
Subtraction.

### `*`
Multiplication.

### `/`
Division.

### `div`
Integer division.

### `%`
Modulo.

### `modSeaside`
Pre-3.14 modulo with unexpected behavior for negative integer modulus; see [Integer#-modSeaside](../Classes/Integer.md#-modseaside). Calling `modSeaside` on a floating-point operand will fall back to `mod` behavior.

### `**`
Exponentiation.

### Polar Coordinate Support

### `rho`
Answer the polar radius of the number.

### `theta`
Answer the polar angle of the number.

### Complex Number Support

### `real`
Answer the real part of the number.

### `imag`
Answer the imaginary part of the number.

### Conversion

### `@`
Create a new [Point](../Classes/Point.md) whose x coordinate is the receiver and whose y coordinate is aNumber.

### `complex`
Create a new [Complex](../Classes/Complex.md) number whose real part is the receiver with the given imaginary part.

### `polar`
Create a new [Polar](../Classes/Polar.md) number whose radius is the receiver with the given angle.

### Iteration

### `for`
Calls **function** for numbers from this up to endval, inclusive, stepping each time by 1.**Arguments:**

| Argument | Description |
|----------|-------------|
| `endValue` | a [Number](../Classes/Number.md). |  
| `function` | a [Function](../Classes/Function.md) which is passed two arguments, the first which is an number from this to argument endval, and the second which is a number from zero to the number of iterations minus one. |  


### `forBy`
Calls **function** for numbers from this up to endval stepping each time by step.**Arguments:**

| Argument | Description |
|----------|-------------|
| `endValue` | a [Number](../Classes/Number.md). |  
| `stepValue` | a [Number](../Classes/Number.md). |  
| `function` | a [Function](../Classes/Function.md) which is passed two arguments, the first which is an number from this to endval, and the second which is a number from zero to the number of iterations minus one. |  


### `forSeries`
Calls **function** for numbers from this up to endval stepping each time by a step specified by second.**Arguments:**

| Argument | Description |
|----------|-------------|
| `second` | a [Number](../Classes/Number.md). |  
| `last` | a [Number](../Classes/Number.md). |  
| `function` | a [Function](../Classes/Function.md) which is passed two arguments, the first which is an number from this to endval, and the second which is a number from zero to the number of iterations minus one. |  



