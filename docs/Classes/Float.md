# Float

*64-bit Floating point number*

**Categories:** Math

## Description

A 64-bit double precision floating point number. Float inherits most of its behaviour from its superclass, [SimpleNumber](../Classes/SimpleNumber.md).

```supercollider
// generate 10 random floats between 0 and 1
{ 1.0.rand }.dup(10)

// Pythagorean comma
// expressed as a floating point number resulting from calculations with integers
(
var apotome = (3 ** 7) / (2 ** 11);
var limma =   (2 ** 8) / (3 ** 5);

apotome / limma
)
```


Note that despite its name, [FloatArray](../Classes/FloatArray.md) only holds 32-bit (single precision) floats. For a raw array of 64-bit floats, use [DoubleArray](../Classes/DoubleArray.md).

> **Note:** The overflow/underflow behavior of a Float is undefined but usually `inf`/`-inf`, respectively, since most CPUs comply well enough IEEE-754 floating point. However, the overflow/underflow behavior is still usually handed to the hardware and thus can vary per system. This (overflow/underflow) occurs whenever the result of an operation does not fit in the range of values supported by the return type, in this case, a 64-bit floating point number.




## Class Methods

### `from32Bits`
**Returns:** a new Float from a 32-bit word.
### `from64Bits`
**Returns:** a new Float from a 64-bit word.

## Instance Methods

### `do`
iterates a [Function](../Classes/Function.md) from `0` to `this - 1`. See also: [Integer#-do](../Classes/Integer.md#-do), [Collection#-do](../Classes/Collection.md#-do)**Arguments:**

| Argument | Description |
|----------|-------------|
| `function` | The function to iterate. |  
### `reverseDo`
iterates function from `this - 1` to 0**Arguments:**

| Argument | Description |
|----------|-------------|
| `function` | The function to iterate. |  
### `clip`
Return this if lo <= this <= hi, otherwise return the nearest boundary: lo if this < lo, hi if this > hi.**Arguments:**

| Argument | Description |
|----------|-------------|
| `lo` | The low threshold of clipping. |  
| `hi` | The high threshold of clipping. |  
### `fold`
Fold this to [lo, hi].**Arguments:**

| Argument | Description |
|----------|-------------|
| `lo` | The low threshold of folding. |  
| `hi` | The high threshold of folding. |  
### `wrap`
Wrap this around [lo, hi) such that it falls in range. Equivalent to (this % (hi - lo)) + lo.**Arguments:**

| Argument | Description |
|----------|-------------|
| `lo` | The low threshold (inclusive) of wrapping. |  
| `hi` | The high threshold (exclusive) of wrapping. |  
### `coin`
Let *x* be the receiver clipped to the range [0, 1]. With probability *x*, return true. With probability 1 - *x*, return false.**Returns:** a [Boolean](../Classes/Boolean.md)
```supercollider
0.2.coin; // 20 % chance for true.
```

See also: [Randomness](../Guides/Randomness.md)### `xrand2`
**Returns:** a random float from this.neg to this, excluding the value exclude.### `modSeaside`
**Returns:** the same result as `this.mod(aNumber, adverb)`; provided for compatibility with [Integer#-modSeaside](../Classes/Integer.md#-modseaside).### `isFloat`
**Returns:** `true` since this is a Float.### `asFloat`
**Returns:** `this` since this is a Float.### `as32Bits`
**Returns:** an Integer which is the bit pattern of this as a 32bit single precision float### `high32Bits`
**Returns:** an Integer which is the bit pattern of high 32-bits of the 64-bit double precision floating point value### `low32Bits`
**Returns:** an Integer which is the bit pattern of high 32-bits of the 64-bit double precision floating point value### `asCompileString`
**Returns:** a string that when interpreted matches the receiver, if the number is within the range given in `storeOn`.
```supercollider
a = 2.81882773638;
a.asCompileString.interpret == a;
```

### `asStringPrec`
Returns a string representation of the number, with the desired precision (i.e. number of significant figures).
```supercollider
// example:
pi
pi.asStringPrec(3)
pi.asStringPrec(6)
(pi * 0.0001).asStringPrec(3)
7.4.asStringPrec(5)
7.4.asStringPrec(50)
```

### `dump`

```supercollider
-1.0.dump
```

returnsThe last two groups of an 8-digit integer are the raw hexadecimal representation of the 64-bit double value according to [IEEE 754 Floating Point](https://ieeexplore.ieee.org/document/8766229) ([https://ieeexplore.ieee.org/document/8766229](https://ieeexplore.ieee.org/document/8766229)). Each part is represented as follows:
### Using Floats as replacement for Integers
In SuperCollider, Floats are 64 bits wide. Because an [Integer](../Classes/Integer.md) is 32-bit, it can only capture integers in the range -2147483648 (`-2^31`) to 2147483647 (`2^31 - 1`).

Therefore, in some situations it can be useful to calculate with floats also when only whole numbers are needed. You can use 64-bit floats for integer calculations in the range `± 9007199254740992`, or about `±2^53`. Sometimes one can go even further (see example below).


```supercollider
// compare factorial:
f = { |x| if(x < 2) { x } { x * f.(x - 1) } };
f.(14); // integer
f.(18) // integer overflow: -898433024
f.(18.0) // float is ok.
// check the ratio between adjacent factorials:
f.(18.0) / f.(17.0) == 18 // true
// 18 is already the largest possible factorial representable in 64-bit float (< 2^53)
{ :x, x<-(1.0..40), f.(x) < (2 ** 53) }.all.last
```


Here is a classical example for an algorithm:


```supercollider
// euclidean algorithm
(
g = { |a, b|
    if(b == 0) {
        a
    } {
        g.(b, mod(a, b))
    }
}
)

// check if a power of two

x = 2147483647 * 3;
g.(x, 3); // wrong, returns 1
x = 2147483647.0 * 3;
g.(x, 3); // correct, returns 3

x = 2007199254740992.0 * 3;
g.(x, 3); // correct, returns 3
x = 9007199254740992.0 * 3;
g.(x, 3); // still happens to be correct, but better not count on it …
```


Testing the limits of 64-bit float (2^53)


```supercollider
a = 2 ** 53 - 1
b = a + 1;
c = a + 2;
b - a // correct (1)
c - a // incorrect (also 1)


// How high you can go depends on the calculation:
// here we divide two numbers that follow each other
// and it is correct up to f.(170), about 7.25e+306.
f = { |x| if(x < 2) { x } { x * f.(x - 1) } };
{ :x, x<-(1.0..180), f.(x) / f.(x - 1) == x }.all.last
```






