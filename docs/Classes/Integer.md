# Integer

*32-bit Integer number*

**Categories:** Math

## Description

A 32-bit integer. Integer inherits most of its behaviour from its superclass, [SimpleNumber](../Classes/SimpleNumber.md).

> **Note:** Integer can represent values in the range -2147483648 (`-2^31`) to 2147483647 (`2^31 - 1`).The overflow behavior of an Integer is undefined. This occurs whenever the result of an operation does not fit in the range of values supported by the return type, in this case, a 32-bit signed integer. Consider using the 64-bit [Float](../Classes/Float.md) for larger numbers (up to `±2^53`).




## Instance Methods


### Iteration

### `do`
Executes **function** for all integers from zero to this minus one.**Arguments:**

| Argument | Description |
|----------|-------------|
| `function` | a [Function](../Classes/Function.md) which is passed two arguments, both of which are the same integer from zero to this minus one. The reason two arguments are passed is for symmetry with the implementations of do in [Collection](../Classes/Collection.md). |  


### `reverseDo`
Executes **function** for all integers from this minus one to zero.

### `for`
Executes **function** for all integers from this to **endval**, inclusive.**Arguments:**

| Argument | Description |
|----------|-------------|
| `endval` | an [Integer](../Classes/Integer.md). |  
| `function` | a [Function](../Classes/Function.md) which is passed two arguments, the first which is an integer from this to endval, and the second which is a number from zero to the number of iterations minus one. |  


### `forBy`
Executes **function** for all integers from this to **endval**, inclusive, stepping each time by **stepval**.**Arguments:**

| Argument | Description |
|----------|-------------|
| `endval` | an [Integer](../Classes/Integer.md). |  
| `stepval` | an [Integer](../Classes/Integer.md). |  
| `function` | a [Function](../Classes/Function.md) which is passed two arguments, the first which is an integer from this to endval, and the second which is a number from zero to the number of iterations minus one. |  


### `collect`
**Returns:** an [Array](../Classes/Array.md) of this size filled by objects generated from evaluating the **function**.

### `collectAs`
**Returns:** a [Collection](../Classes/Collection.md) of **class** of this size filled by objects generated from evaluating the **function**.

### `to`
**Returns:** an [Interval](../Classes/Interval.md) from this to **hi**.

### `geom`
**Returns:** an array with a geometric series of this size from start.

### `fib`
**Returns:** an array with a fibonacci series of this size beginning with **a** and **b**.

### `factors`
**Returns:** the prime factors as array.

### Random Numbers
See also: [Randomness](../Guides/Randomness.md)


### `xrand`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `exclude` | an [Integer](../Classes/Integer.md). |  
**Returns:** a random value from zero to this, excluding the value exclude.

### `xrand2`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `exclude` | an [Integer](../Classes/Integer.md). |  
**Returns:** a random value from this.neg to this, excluding the value exclude.

### Conversion

### `asAscii`
**Returns:** a [Char](../Classes/Char.md) which has the ASCII value of the receiver.

### `asDigit`
**Returns:** a [Char](../Classes/Char.md) which represents the receiver as an ASCII digit.For example `5.asDigit` returns `$5`.

### `asBinaryDigits`
**Returns:** an array with the binary digits (integer 0 or 1).

### `asDigits`
**Returns:** an array with the n-ary digits.See also the complementary method [SequenceableCollection#-convertDigits](../Classes/SequenceableCollection.md#-convertdigits).
```
2007.asDigits;
2007.asDigits(2);
```



### `asBinaryString`
**Returns:** a string with the binary digits (0 or 1).

### `asHexString`
**Returns:** a string with the hexadecimal digits (integer 0 to F).

### `asIPString`
**Returns:** a string in IP format.

### `asStringToBase`
**Returns:** a string with `width`-rightmost digits in base `base`.
```
15.asStringToBase(3, 5); // returns 00120
```



### `asUnicode`
**Returns:** the receiver.

### `degreeToKey`
Interpret this as index into a scale with a given number of steps per ocatve.
```
2.degreeToKey([0, 2, 5, 7, 11]);
```



### `grayCode`
**Returns:** the gray code for the number.
```
2.grayCode
```



### `hash`
**Returns:** a hash value.

### Binary Representation

### `setBit`
set nth bit to zero (bool = false) or one (bool = true)

### `leadingZeroes`
`{ _CLZ }`

### `trailingZeroes`
`{ _CTZ }`

### `numBits`
**Returns:** number of required bits

### Properties

### `even`
**Returns:** true if dividable by 2 with no rest

### `odd`
**Returns:** true if not dividable by 2 with no rest

### Powers Of Two

### `nextPowerOfTwo`
**Returns:** the next power of two greater than or equal to the receiver.
```
13.nextPowerOfTwo.postln;
64.nextPowerOfTwo.postln;
```



### `isPowerOfTwo`
**Returns:** the whether the receiver is a power of two.
```
13.isPowerOfTwo.postln;
64.isPowerOfTwo.postln;
```



### Prime Numbers

### `nthPrime`
**Returns:** the nth prime number. The receiver must be from 0 to 6541.
```
[0, 1, 2, 3, 4, 5].collect({ |i| i.nthPrime }).postln;
```



### `prevPrime`
**Returns:** the next prime less than or equal to the receiver up to 65521.
```
25.prevPrime.postln;
```



### `nextPrime`
**Returns:** the next prime less than or equal to the receiver up to 65521.
```
25.nextPrime.postln;
```



### `isPrime`
**Returns:** whether the receiver is prime.
```
25.isPrime.postln;
13.isPrime.postln;
```



### `indexOfPrime`
**Returns:** the index of a prime number less than or equal to the receiver up to 65521. If the receiver is not a prime, the answer is nil.
```
23.indexOfPrime;
25.indexOfPrime;
```



### Integer Math

### `*`
Multiplication.

### `+`
Addition.

### `-`
Subtraction.

### `modSeaside`
Pre-3.14 modulo with unexpected behavior for negative integer modulus.For dividends smaller than a negative divisor, modSeaside pulls the resulting remainder below the divisor. It thereby leaves zero as peaks on the zero line. Like in the usual mod, all larger dividends result in remainders above zero.
```
(..-9).mod(-3);
// returns [0, -1, -2, 0, -1, -2, 0, -1, -2, 0]
(..-9).modSeaside(-3);
// returns [0, 2, 1, 0, -4, -5, 0, -4, -5, 0]

// plot
(-25..25).modSeaside(-5).plot.plotMode_(\steps);

// modSeaside
Pbind(\note, modSeaside(Pseries(-15, 1, 25), -5), \dur, 0.2).play;

// modSeaside with different divisors
Pbind(\note, modSeaside(Pseries(-15, 1, 25), [3, -4, -5]), \dur, 0.2).play;

// mod
Pbind(\note, mod(Pseries(-15, 1, 25), -5), \dur, 0.2).play;

// mod with different divisors
Pbind(\note, mod(Pseries(-15, 1, 25), [3, -4, -5]), \dur, 0.2).play;
```



### `clip`
**Returns:** - the receiver if it is between `lo` and `hi`
- `lo` if the receiver is less than `lo`
- `hi` if the receiver is greater than `hi`
The result is an Integer only if both `lo` and `hi` are Integers.
```
4.clip(2, 5); // returns 4
0.clip(2, 5); // returns 2
7.clip(2, 5); // returns 5
```



### `factorial`
**Returns:** the factorial of the receiver as an integer. This will overflow for numbers `> 12` and throw an error. Floating point factorials can be used in such cases (see: [SimpleNumber#-factorial](../Classes/SimpleNumber.md#-factorial)).
```
12.factorial
23.0.factorial // for larger factorials, use floats.
```



### `fold`
Folds in to a value between `lo` and `hi`.**Returns:** an Integer between `lo` and `hi`.
```
(0..12).fold(0, 3); // returns [0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0]
```



### `log2Ceil`
**Returns:** next larger integer of the base 2 logarithm of the receiver.
```
17.log2; // returns 4.0874628412503
17.log2Ceil; // returns 5
17.log2.ceil.asInteger; // equivalent to the previous line
```



### `wrap`
Wraps in to a value between `lo` and `hi`.**Returns:** an Integer between `lo` and `hi`.
```
(0..12).wrap(0, 3); // returns [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0]
```



### Range Limiting



### `wrap`
Wrap this around [lo, hi] such that it falls in range. Equivalent to (this % (hi - lo + 1)) + lo. Note that this behavior is different from [Float#-wrap](../Classes/Float.md#-wrap).**Arguments:**

| Argument | Description |
|----------|-------------|
| `lo` | The low threshold (inclusive) of wrapping. |  
| `hi` | The high threshold (inclusive) of wrapping. |  


### Misc

### `exit`
**Returns:** exits the sclang program and returns the receiver as an exit code to the parent process (e.g. Unix shell).
```
7.exit; // this line stops the interpreter and returns 7 as exit code
```



### `generate`
**Returns:** calls `function.value(receiver)` but returns the receiver.
```
f = { |i| "foo".postln; i*2 }
3.generate(f) // returns 3 but the function f is executed
f.value(3) // returns 6
```



### `isInteger`
**Returns:** true (the receiver is an integer).

### `isAlt`, `isCaps`, `isCmd`, `isCtrl`, `isFun`, `isHelp`, `isNumPad`, `isShift`
**Returns:** a Boolean for whether or not the given key modifier is in effect. For a list of these, see [Modifiers](../Reference/Modifiers.md).
```
v = TextView(nil, Rect(800, 100, 400, 300)).front;

v.keyDownAction = { |view, char, modifiers|
    case
    { modifiers.isAlt } { \alt }
    { modifiers.isCaps } { \caps }
    { modifiers.isCmd } { \cmd }
    { modifiers.isCtrl } { \ctrl }
    { modifiers.isFun } { \fun }
    { modifiers.isHelp } { \help }
    { modifiers.isNumPad } { \numpad }
    { modifiers.isShift } { \shift }
    .postln
};
```



### `pidRunning`
**Returns:** a Boolean for whether or not the specified pid is running.
```
p = "cat".unixCmd;
p.pidRunning; // cat will stay alive
("kill" + p).unixCmd
p.pidRunning;
```





