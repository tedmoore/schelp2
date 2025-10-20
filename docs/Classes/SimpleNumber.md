# SimpleNumber

*one-dimensional value*

**Categories:** Math

**Related:** [Polar](../Classes/Polar.md), [Complex](../Classes/Complex.md), [Float](../Classes/Float.md), [Integer](../Classes/Integer.md), [UnaryOpUGen](../Classes/UnaryOpUGen.md), [BinaryOpUGen](../Classes/BinaryOpUGen.md), [Tour-of-Special-Functions](../Guides/Tour-of-Special-Functions.md)

## Description

Base class for numbers which can be represented by a single one dimensional value.
Most of the Unary and Binary operations are also implemented by [UnaryOpUGen](../Classes/UnaryOpUGen.md) and [BinaryOpUGen](../Classes/BinaryOpUGen.md), so you can get more examples by looking at the help for those.


## Class Methods


### `new`
allocates a new SimpleNumber.

## Instance Methods


### math support

### `+`
Addition

### `-`
Subtraction

### `*`
Multiplication

### `/`
Division

### `%`
Modulo

### `mod`
Modulo

### `div`
Integer Division

### `**`
Exponentiation

### `!=`
Is not

### `>`
greater than

### `<`
greater than

### `>=`
greater or equal than

### `<=`
smaller or equal than

### `lcm`
Least common multiple

### `gcd`
Greatest common divisor

### `round`
Round to multiple of aNumber

### `roundUp`
Round up to a multiple of aNumber. For roundDown use [trunc](../Classes/SimpleNumber.md#-trunc).

### `smallButNotZero`
Check if the value is closer to zero than a threshold, but not zero.**Arguments:**

| Argument | Description |
|----------|-------------|
| `thresh` | The threshold to use for comparison. |  


### `trunc`
Truncate to multiple of aNumber (e.g. it rounds numbers down to a multiple of aNumber).

### `softRound`
Rounds the value to a multiple of **resolution**. By using **margin** and **strength** you can control which values will be rounded, and by how much.Conceptually this is the equivalent of MIDI quantization in a DAW/MIDI sequencer. In particular it allows a certain sloppiness close to the **resolution** value.Note: this method expects values >= 0.**Arguments:**

| Argument | Description |
|----------|-------------|
| `resolution` | Round this value to a multiple of resolution. E.g. if you chose 1, then all values would be rounded to the nearest integer. |  
| `margin` | Values that are within ±**margin** from a multiple of **resolution** will be left as they are.E.g. if you chose a resolution value of 0.5 and a margin of 0.01, then the values 0.501 and 0.499 would be left as they are, but the value 0.502 would become 0.5.This should be a value between 0 and **resolution**. |  
| `strength` | Determines the degree to which this number will be changed.If strength is 1, then this function will return the nearest resolution. If it is 0, then value of this number will be left unchanged.E.g. If the resolution was 1 and strength was 0.5, then the value 0.6 would become 0.8. |  

```
((0..10) / 5).collect { |num| [num, num.softRound(1, 0, 1)] };
((0..10) / 5).collect { |num| [num, num.softRound(1, 0.3, 1)] };
((0..10) / 5).collect { |num| [num, num.softRound(1, 0, 0.5)] };
```



### `snap`
Rounds the values **margin** distance from resolution to a multiple of resolution. By using **margin** and **strength** you can control when values will be rounded, and by how much.Conceptually this is the equivalent of 'snap' in a graphics program. Values within a certain distance (**margin**) from a grid line are snapped to it. All other values are unchanged.Note: this method expects values >= 0.**Arguments:**

| Argument | Description |
|----------|-------------|
| `resolution` | Snap this value to a multiple of resolution. E.g. if you chose 1, then all values would be rounded to the nearest integer. |  
| `margin` | Only values that are greater ±**margin** from a multiple of **resolution** value will be changed. Values that are less than **margin** will be unchanged.E.g. if you chose a resolution value of 0.5 and a margin of 0.01, then the values 0.501 and 0.499 would be snapped to 0.5, but the value 0.502 would be unchanged.This should be a value between 0 and **resolution**. |  
| `strength` | Determines the degree to which this number will be changed.If strength is 1, then this function will return the nearest resolution. If it is 0, then value of this number will be left unchanged.E.g. If the resolution was 1 and strength was 0.5, then the value 0.6 would become 0.8. |  

```
((0..10) / 5).collect { |num| [num, num.snap(1, 0, 1)] };
((0..10) / 5).collect { |num| [num, num.snap(1, 0.3, 1)] };
((0..10) / 5).collect { |num| [num, num.snap(1, 0, 0.5)] };
```



### `thresh`


### `min`
Minimum

### `max`
Maximum

### `wrap2`


### `atan2`
Arctangent of (this/aNumber)

### `hypot`
Square root of the sum of the squares.

### `log`
**Returns:** Base e logarithm.

### `log2`
**Returns:** Base 2 logarithm.

### `log10`
**Returns:** Base 10 logarithm.

### `neg`
**Returns:** negation

### `abs`
**Returns:** absolute value.

### `sign`
**Returns:** Answer -1 if negative, +1 if positive or 0 if zero.

### `ceil`
**Returns:** next larger integer.

### `floor`
**Returns:** next smaller integer

### `sin`
Sine

### `cos`
Cosine

### `tan`
Tangent

### `asin`
Arcsine

### `acos`
Arccosine

### `atan`
Arctangent

### `sinh`
Hyperbolic sine

### `cosh`
Hyperbolic cosine

### `tanh`
Hyperbolic tangent

### `frac`
fractional part

### `squared`
the square of the number

### `cubed`
the cube of the number

### `sqrt`
the square root of the number.

### `exp`
e to the power of the receiver.

### `reciprocal`
1 / this

### `pow`
this to the power of aNumber

### `fold2`
the folded value, a bitwise or with aNumber

### `previousPowerOf`
the number relative to this that is the previous power of aNumber

### `nextPowerOf`
the next power of aNumber

### `nextPowerOfTwo`
**Returns:** the number relative to this that is the next power of 2

### `nextPowerOfThree`
the next power of three

### `hash`
**Returns:** a hash value

### `<!`
**Returns:** the receiver. aNumber is ignored.

### `&`
Bitwise And

### `|`
Bitwise Or

### `bitXor`
Bitwise Exclusive Or

### `bitHammingDistance`
Binary Hamming distance: the count of bits that are not the same in the two numbers

### `bitTest`
**Returns:** true if bit at index aNumber is set.

### `bitNot`
**Returns:** ones complement

### `<<`
Binary shift left.

### `>>`
Binary shift right.

### `+>>`
Unsigned binary shift right.

### `rightShift`
**Returns:** performs a binary right shift

### `unsignedRightShift`
**Returns:** performs an unsigned right shift

### `leftShift`
**Returns:** performs a binary left shift

### `bitOr`
**Returns:** performs a bitwise or with aNumber

### `bitAnd`
**Returns:** performs a bitwise and with aNumber

### `ring1`
(a * b) + a

### `ring2`
((a*b) + a + b)

### `ring3`
(a * a *b)

### `ring4`
((a*a *b) - (a*b*b))

### `difsqr`
(a*a) - (b*b)

### `sumsqr`
(a*a) + (b*b)

### `sqrdif`
(a - b) ** 2

### `sqrsum`
(a + b) ** 2

### `absdif`
(a - b).abs

### `moddif`
On a circle, there are two distances between two points. This operator returns the smaller value of the two.
```
moddif(0.75, 0, 1)
```



### `amclip`
0 when b <= 0,  a*b when b > 0

### `scaleneg`
a * b when a < 0, otherwise a.

### `clip2`
clips receiver to +/- aNumber

### `excess`
Returns the difference of the receiver and its clipped form.
```
(a - clip2(a, b))
```



### `madd`

```
this * a + b
```



### testing

### `isPositive`
Answer if the number is >= 0.

### `isNegative`
Answer if the number is < 0.

### `isStrictlyPositive`
Answer if the number is > 0.

### `booleanValue`
**Returns:** true, if strictly positive (> 0), otherwise false (see [Boolean](../Classes/Boolean.md))

### `isNaN`


### `==`


### conversion

### `asFraction`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `denominator` |  |  
| `fasterBetter` | if true, asFraction may find a much closer approximation and do it faster. |  
**Returns:** an array of denominator and divisor of the nearest and smallest fraction

### `asAudioRateInput`
Converts this into an audiorate input.

### `asTimeString`
Produces a time string in the clock format inspired by ISO 8601 time interval display (truncated representation) `(ddd:)hh:mm:ss(.z)`, interpreting the receiver as time in seconds. See [String#-asSecs](../Classes/String.md#-assecs) for the inverse function.**Arguments:**

| Argument | Description |
|----------|-------------|
| `precision` | accuracy of the fraction of seconds; since the number of decimal places is also an argument, `precision` is clamped to `10.pow(decimalPlaces.neg)`, i.e. `0.001` for `decimalPlaces = 3` |  
| `maxDays` | maximum number of days |  
| `dropDaysIfPossible` | a [Boolean](../Classes/Boolean.md). If set to `true`, and the number of days in the formatted string would be 0, that section of the resulting string is omitted |  
| `decimalPlaces` | number of decimal places representing fraction of seconds, clamped to `0`; if `0`, the string is formatted as `(ddd:)hh:mm:ss` |  

```
(
var start;
start = Main.elapsedTime;
{
    loop {
        (Main.elapsedTime - start).asTimeString.postln;
        0.05.wait
    }
}.fork;
)
```



### `asPoint`
**Returns:** this as [Point](../Classes/Point.md). x = y = this.

### `asComplex`
**Returns:** this as [Point](../Classes/Point.md). x = y = this.

### `asWarp`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `spec` | a [ControlSpec](../Classes/ControlSpec.md) |  
**Returns:** this as [CurveWarp](../Classes/CurveWarp.md) according to spec.

### `asFloat`
**Returns:** this as [Float](../Classes/Float.md)

### `asRect`
**Returns:** a [Rect](../Classes/Rect.md) with x = y = w = h = this.

### `asBoolean`
**Returns:** this as a [Boolean](../Classes/Boolean.md). this > 0

### `asQuant`
**Returns:** the values as [Quant](../Classes/Quant.md)

### `asInteger`
**Returns:** this as [Integer](../Classes/Integer.md)

### timing

### `wait`
within a routine, yield the number so that the clock can wait for this many beats. Outside a Routine, this trows an error (see also Routine for details).Create a routine by a function fork
```
(
fork {
    1.wait;
    "I did wait".postln;
    1.0.rand.wait;
    "No you didn't".postln;
    2.wait;
    (1..).do { |i|
        "yes I did".postln;
        i.asFloat.rand.wait;
        "no you didn't".postln;
        i.wait
    }
}
)
```



### `waitUntil`
like wait, only specify a time (measured in beats of the current thread's clock). Outside a Routine, this throws an error (see also Routine for details).

### `sleep`
make the current thread sleep, until woken up by re-scheduling. Outside a Routine, this trows an error (see also Routine for details).

### `nextTimeOnGrid`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `clock` |  |  
**Returns:** the next possible multiple of the clock's beats.

### `schedBundleArrayOnClock`


### series and arrays

### `nearestInList`
**Returns:** the value in the list closest to this
```
(
l = [0, 0.5, 0.9, 1];
(0, 0.05..1).collect { |i| i.nearestInList(l) }
)
```



### `nearestInScale`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `scale` | an array of SimpleNumbers each treated as a step in the octave. |  
| `stepsPerOctave` | 12 by default |  
**Returns:** the value in the collection closest to this, assuming an octave repeating table of note values.
```
(
l = [0, 1, 5, 9, 11]; // pentatonic scale
(60, 61..76).collect { |i| i.nearestInScale(l, 12) }
)
```



### `series`
Generate an arithmetic series from `this` over **second** to **last**.If **second** is `nil`, it is one magnitude step towards last (1 or -1).
```
series(5, 7, 10);
series(5, nil, 10);
(5, 7 .. 10)
```

This is used in the shortcuts:
```
(0..100);
(1, 3 .. 17)
```

**Returns:** An [Array](../Classes/Array.md).The last value may not be included in the result if the step size does not divide evenly into the range of the series.

### `seriesIter`
Create a [Routine](../Classes/Routine.md) that iterates over an arithmetic series from `this` over **second** to **last**.Since this is a lazy operation, **last** can be `inf`, generating an endless series. If unspecified, **last** is `inf` or `-inf` depending on the step direction.
```
r = seriesIter(0, 5, 52);
r.nextN(8);
r.nextN(8); // reaches 'last', then nils

r = seriesIter(0, 5); // last = inf
r.nextN(8); // run repeatedly
```

See also [#-series](#-series) and [ListComprehensions](../Guides/ListComprehensions.md).**Returns:** A [Routine](../Classes/Routine.md).

### windowing

### `rectWindow`
**Returns:** a value for a rectangular window function between 0 and 1.

### `hanWindow`
**Returns:** a value for a hanning window function between 0 and 1.

### `welWindow`
**Returns:** a value for a welsh window function between 0 and 1.

### `triWindow`
**Returns:** a value for a triangle window function between 0 and 1.

### mapping

### `distort`
A nonlinear distortion function.Implements:Visualize:
```
(
{ var saw = LFSaw.ar(2 * 0.01.reciprocal);
    [saw, saw.distort]
}.plot.superpose_(true)
)
```



### `softclip`
Distortion with a perfectly linear region from -0.5 to +0.5.Implements:Visualize:
```
(
{ var saw = LFSaw.ar(2 * 0.01.reciprocal);
    [saw, saw.softclip]
}.plot.superpose_(true)
)
```



### `scurve`
Map receiver in the onto an S-curve bound to [0, 1]. Implements:with `this` clipped to [0, 1].
```
((-100..200) / 100).collect(_.scurve).plot
```



### `ramp`
Map the receiver onto a ramp starting at `0.0`, ending at `1.0`, effectively clipping the receiver at [0, 1].
```
(
    var vals = (-100..200) / 100;
    vals.collect(_.ramp).plot
    .domainSpecs_(
        [vals.minItem, vals.maxItem].asSpec
    )
    .axisLabelX_("input").axisLabelY_("output")
)
```



### `magnitude`
**Returns:** The absolute value.Alternatively conceived of as the [Polar#-magnitude](../Classes/Polar.md#-magnitude) or [Complex#-magnitude](../Classes/Complex.md#-magnitude), wherein the receiver is the real part and the imaginary part is `0.0`.

### `angle`
**Returns:** Angle of receiver (in radians) conceived as [Polar](../Classes/Polar.md) or [Complex](../Classes/Complex.md) number, wherein the receiver is the real part and the imaginary part is `0.0`. I.e. `if (this.isPositive) { 0.0 } { pi }`.

### `degreeToKey`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `scale` | an array of SimpleNumbers each treated as a step in the octave. |  
| `stepsPerOctave` | 12 is the standard chromatic scale. |  
the value is truncated to an integer and used as an index into an octave repeating table of note values. Indices wrap around the table and shift octaves as they do.
```
(
l = [0, 1, 5, 9, 11]; // pentatonic scale
(1, 2..15).collect{ |i|
    i.degreeToKey(l, 12)
};
)
```



### `keyToDegree`
inverse of degreeToKey.**Arguments:**

| Argument | Description |
|----------|-------------|
| `scale` | an array of SimpleNumbers each treated as a step in the octave. |  
| `stepsPerOctave` | 12 is the standard chromatic scale. |  

```
(
l = [0, 1, 5, 9, 11]; // pentatonic scale
(60, 61..75).collect { |i| i.keyToDegree(l, 12) }
)
```


```
(
l = [0, 1, 5, 9, 11]; // pentatonic scale
(60, 61..75).postln.collect { |i| i.keyToDegree(l, 12).degreeToKey(l) }
)
```



### `gaussCurve`
Map the receiver onto a gauss function.Uses the formula:where `a` is the distribution amplitude, `b` is the mean (typically denoted *mu*), and the variance is `c.squared` (*sigma*^2).The method defaults to a "standard normal distribution": a zero mean and both the peak amplitude and variance are `1.0` (`a = 1.0, b = 0.0, c = 1.0`).
```
(0..1000).normalize(-10, 10).collect { |num| num.gaussCurve }.plot;
```



### `equalWithPrecision`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `that` | the number to compare with within precision |  
| `precision` | The absolute precision, independent of the value compared |  
| `relativePrecision` | The precision relative to the larger absolute of the values compared. |  
**Returns:** true if receiver is closer to that than precision.
```
3.1.equalWithPrecision(3.0, 0.05); // false
3.1.equalWithPrecision(3.0, 0.1); // false
3.1.equalWithPrecision(3.0, 0.11); // true
3000.1.equalWithPrecision(3000.0, 0, 0.01); // true
3.1.equalWithPrecision(3.0, 0, 0.01); // false
```



### `quantize`
Deprecated. Round the receiver to the quantum. If you're looking for MIDI quantization type features use `SimpleNumber#-softRound`**Arguments:**

| Argument | Description |
|----------|-------------|
| `quantum` | amount. |  
| `tolerance` | allowed tolerance. |  
| `strength` | Determines how much the value is allowed to differ in the tolerance range. |  

```
((0..10) / 10).collect { |num| num.quantize(1, 0.3, 0.5) }.postcs.plot;
((0..10) / 10).collect { |num| num.quantize(1, 0.6, 0.5) }.postcs.plot;
((0..10) / 10).collect { |num| num.quantize(1, 1.0, 0.5) }.postcs.plot;
```



### `linlin`
map the receiver from an assumed linear input range to a linear output range. If the input exceeds the assumed input range, the behaviour is specified by the clip argument.**Arguments:**

| Argument | Description |
|----------|-------------|
| `inMin` | assumed input minimum |  
| `inMax` | assumed input maximum |  
| `outMin` | output minimum |  
| `outMax` | output maximum |  
| `clip` | nil (don't clip) \max (clip ceiling) \min (clip floor) \minmax (clip both - this is default). |  

```
(0..10).collect { |num| num.linlin(0, 10, -4.3, 100) };
(0..10).linlin(0, 10, -4.3, 100); // equivalent.
```



### `linexp`
map the receiver from an assumed linear input range (inMin..inMax) to an exponential output range (outMin..outMax). The output range must not include zero. If the input exceeds the input range, the following behaviours are specified by the clip argument.**Arguments:**

| Argument | Description |
|----------|-------------|
| `inMin` | assumed input minimum |  
| `inMax` | assumed input maximum |  
| `outMin` | output minimum |  
| `outMax` | output maximum |  
| `clip` | nil (don't clip) \max (clip ceiling) \min (clip floor) \minmax (clip both - this is default). |  

```
(0..10).collect { |num| num.linexp(0, 10, 4.3, 100) };
(0..10).linexp(0, 10, 4.3, 100); // equivalent.
```



### `explin`
map the receiver from an assumed exponential input range (inMin..inMax) to a linear output range (outMin..outMax). If the input exceeds the assumed input range. The input range must not include zero. If the input exceeds the input range, the following behaviours are specified by the clip argument.**Arguments:**

| Argument | Description |
|----------|-------------|
| `inMin` | assumed input minimum |  
| `inMax` | assumed input maximum |  
| `outMin` | output minimum |  
| `outMax` | output maximum |  
| `clip` | nil (don't clip) \max (clip ceiling) \min (clip floor) \minmax (clip both - this is default). |  

```
(1..10).collect { |num| num.explin(0.1, 10, -4.3, 100) };
(1..10).explin(0.1, 10, -4.3, 100); // equivalent.
```



### `expexp`
map the receiver from an assumed exponential input range (inMin..inMax) to an exponential output range (outMin..outMax). If the input exceeds the assumed input range. Both input range and output range must not include zero. If the input exceeds the input range, the following behaviours are specified by the clip argument.**Arguments:**

| Argument | Description |
|----------|-------------|
| `inMin` | assumed input minimum |  
| `inMax` | assumed input maximum |  
| `outMin` | output minimum |  
| `outMax` | output maximum |  
| `clip` | nil (don't clip) \max (clip ceiling) \min (clip floor) \minmax (clip both - this is default). |  

```
(1..10).collect { |num| num.expexp(0.1, 10, 4.3, 100) };
(1..10).expexp(0.1, 10, 4.3, 100); // equivalent.
```



### `lincurve`
map the receiver from an assumed linear input range (inMin..inMax) to an exponential curve output range (outMin..outMax). A curve is like the curve parameter in Env. Unlike with linexp, the output range may include zero. If the input exceeds the input range, the following behaviours are specified by the clip argument.**Arguments:**

| Argument | Description |
|----------|-------------|
| `inMin` | assumed input minimum |  
| `inMax` | assumed input maximum |  
| `outMin` | output minimum |  
| `outMax` | output maximum |  
| `curve` | 0 (linear) <0 (concave, negatively curved) >0 (convex, positively curved) |  
| `clip` | nil (don't clip) \max (clip ceiling) \min (clip floor) \minmax (clip both - this is default). |  

```
(0..10).collect { |num| num.lincurve(0, 10, -4.3, 100, -3) };
(0..10).lincurve(0, 10, -4.3, 100, -3); // equivalent.
```


```
// different curves:
(-4..4).do { |val|
    (0..100).collect(_.lincurve(0, 100, 0, 1, val)).plot
}
```



### `curvelin`
map the receiver from an assumed curve-exponential input range (inMin..inMax) to a linear output range (outMin..outMax). If the input exceeds the assumed input range. A curve is like the curve parameter in Env. Unlike with explin, the input range may include zero. If the input exceeds the input range, the following behaviours are specified by the clip argument.**Arguments:**

| Argument | Description |
|----------|-------------|
| `inMin` | assumed input minimum |  
| `inMax` | assumed input maximum |  
| `outMin` | output minimum |  
| `outMax` | output maximum |  
| `curve` | 0 (linear) <0 (concave, negatively curved) >0 (convex, positively curved) |  
| `clip` | nil (don't clip) \max (clip ceiling) \min (clip floor) \minmax (clip both - this is default). |  

```
(1..10).collect { |num| num.curvelin(0, 10, -4.3, 100, -3) };
(1..10).curvelin(0, 10, -4.3, 100, -3); // equivalent.
```


```
// different curves:
(-4..4).do { |val|
    (0..100).collect(_.curvelin(0, 100, 0, 1, val)).plot
}
```



### `bilin`
map the receiver from two assumed linear input ranges (inMin..inCenter) and (inCenter..inMax) to two linear output ranges (outMin..outCenter) and (outCenter..outMax). If the input exceeds the input range, the following behaviours are specified by the clip argument.**Arguments:**

| Argument | Description |
|----------|-------------|
| `inCenter` |  |  
| `inMin` | assumed input minimum |  
| `inMax` | assumed input maximum |  
| `outCenter` |  |  
| `outMin` | output minimum |  
| `outMax` | output maximum |  
| `clip` | nil (don't clip) \max (clip ceiling) \min (clip floor) \minmax (clip both - this is default). |  

```
var center = 0.5, ctlCenter;
w = Window("bilin", Rect(100, 100, 200, 100)).front;
a = Slider(w, Rect(20, 20, 150, 20)).value_(0.5);
b = Slider(w, Rect(20, 45, 150, 20)).value_(0.5);
b.action = { center = b.value };
a.mouseDownAction = { ctlCenter = a.value };
a.action = {
    b.value = a.value.bilin(ctlCenter, 0, 1, center, 0, 1);
};
```



### `biexp`
map the receiver from two assumed exponential input ranges (inMin..inCenter) and (inCenter..inMax) to two linear output ranges (outMin..outCenter) and (outCenter..outMax). The input range must not include zero. If the input exceeds the input range, the following behaviours are specified by the clip argument.**Arguments:**

| Argument | Description |
|----------|-------------|
| `inCenter` |  |  
| `inMin` | assumed input minimum |  
| `inMax` | assumed input maximum |  
| `outCenter` |  |  
| `outMin` | output minimum |  
| `outMax` | output maximum |  
| `clip` | nil (don't clip) \max (clip ceiling) \min (clip floor) \minmax (clip both - this is default). |  

```
// doesn't properly work yet.
(
var center = 0.5, ctlCenter;
w = Window("biexp", Rect(100, 100, 200, 100)).front;
a = Slider(w, Rect(20, 20, 150, 20)).value_(0.5);
b = Slider(w, Rect(20, 45, 150, 20)).value_(0.5);
b.action = { center = b.value };
a.mouseDownAction = { ctlCenter = a.value + 0.05 };
a.action = {
    b.value = (a.value + 0.1).biexp(ctlCenter, 0.1, 1.1, center, 0, 1);
};
)
```



### `lcurve`
map the receiver onto an L-curve.Uses the formula
```
a * (m * exp(x) * rTau + 1) / (n * exp(x) * rTau + 1)
```

This is used for smoothing values and limiting them to a range.
```
(0..1000).normalize(-10, 10).collect { |num| num.lcurve }.plot;
```



### `degrad`
**Returns:** converts degree to radian

### `raddeg`
**Returns:** converts radian to degree

### `midicps`
Convert MIDI note to cycles per second**Returns:** cycles per second

### `cpsmidi`
Convert cycles per second to MIDI note.**Returns:** midi note

### `midiratio`
Convert an interval in semitones to a ratio.**Returns:** a ratio

### `ratiomidi`
Convert a ratio to an interval in semitones.**Returns:** an interval in semitones

### `ampdb`
Convert a linear amplitude to decibels.

### `dbamp`
Convert a decibels to a linear amplitude.

### `octcps`
Convert decimal octaves to cycles per second.

### `cpsoct`
Convert cycles per second to decimal octaves.

### streams

### `storeOn`
stores this on the given stream

### `printOn`
prints this on the given stream

### random
Unless noted otherwise, the return value of all these methods will be an [Integer](../Classes/Integer.md) only when the receiver and all arguments are Integers as well.


> **Note:** Interval Notation Guide for this part:| Notation | Name | Inclusion | Meaning (Range) | 
| --- | --- | --- | --- || `[a, b]` | Closed interval | Includes both `a` and `b` | $a \leq x \leq b$ | | `(a, b)` | Open interval | Excludes both `a` and `b` | $a \lt x \lt b$ | | `[a, b)` | Half‑open interval (left‑closed) | Includes `a`, excludes `b` | $a \leq x \lt b$ | | `(a, b]` | Half‑open interval (right‑closed) | Excludes `a`, includes `b` | $a \lt x \leq b$ |



### `coin`
Let *x* be the receiver clipped to the range [0, 1]. With probability *x*, return true. With probability 1 - *x*, return false.

### `rand`
Returns a random number from a uniform distribution with the range [0,this), i.e., between 0 and this (including 0, not including this).

### `rand2`
Returns a random number from a uniform distribution with the range [-this, +this], i.e. between -this and +this (including -this and +this).

### `rrand`
Returns a random number from a uniform distribution with the range between `this` and `aNumber`.`aNumber` can be lower than `this`. If either `this` or `aNumber` is a [Float](../Classes/Float.md), the `aNumber` bound will be excluded from the range, and sclang returns a [float](../Classes/Float.md). If both `this` and `aNumber` are [Integer](../Classes/Integer.md), both bounds are included, and sclang returns an [integer](../Classes/Integer.md).

### `linrand`
Returns a random number from a linear distribution with the range [0, this). Histogram will approximate a diagonal line, hence the name. More formally, `.linrand` samples from a distribution over [0, 1) with a probability density function of 2(1 - x) and multiplies by `this`.Best explained visually:
```
{1.0.linrand}.dup(10000).plotHisto;
```



### `bilinrand`
Bilateral linearly distributed random number in the range (-this, +this). Like linrand, but adds a second straight line from `-this` to 0. Histogram will approach an isosceles triangle with its apex at x = 0. Formally like `.linrand`, but the probability density function is *also* supported in the range (-x, 0] by 2(1 + x).Best explained visually:
```
{1.0.bilinrand}.dup(10000).plotHisto;
```



### `sum3rand`
Returns a [Float](../Classes/Float.md) from the range [-this, this), distribution approximates a bell-like (Gaussian or normal) distribution.**Returns:** Always returns a [Float](../Classes/Float.md).Loosely approximates a Gaussian distribution by summing three uniform random generators. Equivalent to:
```
({ 1.0.rand }.dup(3).sum - 1.5) * 2/3 * this
```



### `exprand`
Returns a [Float](../Classes/Float.md) in the range [this, aNumber),  i.e. between this and aNumber (including this, not including aNumber),  drawn from a log-uniform distribution. Receiver (i.e., `this`) must not be zero. Note that the value is *not* drawn from an exponential distribution.**Returns:** Always returns a [Float](../Classes/Float.md).

### `gauss`
Returns a [Float](../Classes/Float.md) sampled from a Gaussian distribution with mean `this` and standard deviation `standardDeviation`. The range of the gaussian distribution is unbounded and thus may return +/-inf; consider using [clip](../Classes/SimpleNumber.md#-clip).**Arguments:**

| Argument | Description |
|----------|-------------|
| `standardDeviation` | The standard deviation. |  
**Returns:** Always returns a [Float](../Classes/Float.md).

### `partition`
randomly partition a number into parts of at least min size.**Arguments:**

| Argument | Description |
|----------|-------------|
| `parts` | number of parts |  
| `min` | the minimum size |  

```
75.partition(8, 3);
75.partition(75, 1);
```



### UGen Compatibility Methods
Some methods to ease the development of generic ugen code.


### `lag`, `lag2`, `lag3`, `lagud`, `lag2ud`, `lag3ud`, `slew`, `varlag`
**Returns:** `this`

### misc

### `isValidUGenInput`
**Returns:** false if receiver cannot be used in UGen.

### Special Functions
A variety of Special Functions are supplied by the Boost C++ library. The library's [online documentation](http://www.boost.org/doc/libs/1_66_0/libs/math/doc/html/special.html) serves as the primary reference for the following functions. The methods here match closely with those found in the source library, as do argument names.

Below you'll find descriptions of the functions and their bounds, but for visualizing the functions, have a look in [Tour-of-Special-Functions](../Guides/Tour-of-Special-Functions.md).

> **⚠️ Warning:** Many of the functions are only valid in certain numerical ranges. For the most part, error handling happens in the underlying boost functions. While these errors are often obtuse, you'll usually find a useful message at the end of the error regarding proper ranges and the erroneous value supplied. Refer to the online documentation for more detailed descriptions, and the [Tour-of-Special-Functions](../Guides/Tour-of-Special-Functions.md) for plots showing ranges and asymptotes.

### Number Series
Take a tour of [Number Series](../Guides/Tour-of-Special-Functions.md#number-series).


### `bernouliB2n`
Returns the (2*`n`)th Bernoulli number.Because all odd numbered Bernoulli numbers are zero (apart from B(1) which is -1/2) the interface will only return the even numbered Bernoulli numbers.

### `tangentT2n`
Returns a single tangent number at `i`. Also called a zag function.

### Gamma Functions
Take a tour of [Gamma Functions](../Guides/Tour-of-Special-Functions.md#gamma-functions).


### `tgamma`
Returns the "true gamma" of value `z`.

### `tgamma1pm1`
Returns `gamma(dz + 1) - 1`.

### `lgamma`
Returns the natural logarithm of the gamma function.

### `digamma`
Returns the digamma or psi function of `z`.Digamma is defined as the logarithmic derivative of the gamma function.

### `trigamma`
Returns the trigamma function of `z`.Trigamma is defined as the derivative of the digamma function.

### `polygamma`
Returns the polygamma function of `z`.Polygamma is defined as the `n`'th derivative of the digamma function.

### `tgammaRatio`
Returns the ratio of gamma functions `tgamma(a) / tgamma(b)`.

### `tgammaDeltaRatio`
Returns the ratio of gamma functions `tgamma(a) / tgamma(a+delta)`.

### `gammaP`
Returns the normalised lower incomplete gamma function.Requires `a` > 0 and `z` >= 0.

### `gammaQ`
Returns the normalised upper incomplete gamma function.Requires `a` > 0 and `z` >= 0.

### `tgammaLower`
Returns the full (non-normalised) lower incomplete gamma function.Requires `a` > 0 and `z` >= 0.

### `tgammaUpper`
Returns the full (non-normalised) upper incomplete gamma function.Requires `a` > 0 and `z` >= 0.

### `gammaPInv`
Returns a value such that `p = gamma_p(a, x)`.Requires `a` > 0 and 1 >= `p,q` >= 0.

### `gammaQInv`
Returns a value x such that `q = gamma_q(a, x)`.Requires `a` > 0 and 1 >= `p,q` >= 0.

### `gammaPInvA`
Returns a value such that `p = gamma_p(a, x)`.Requires `x` > 0 and 1 >= `p,q` >= 0.

### `gammaQInvA`
Returns a value x such that `q = gamma_q(a, x)`.Requires `x` > 0 and 1 >= `p,q` >= 0.

### `gammaPDerivative`
Implements the partial derivative with respect to x of the incomplete gamma function (lower).

### `gammaQDerivative`
Implements the partial derivative with respect to x of the incomplete gamma function (upper).

### Factorials and Binomial Coefficients
Take a tour of [Factorials and Binomial Coefficients](../Guides/Tour-of-Special-Functions.md#factorials-and-binomial-coefficients).


### `factorial`
Returns `i!`.> **⚠️ Warning:** `factorial` will overflow if `i > 170`

### `doubleFactorial`
Returns `i!!`.For **even** `i`, `i !! = i(i-2)(i-4)(i-6) ... (4)(2)`.For **odd** `i`, `i !! = i(i-2)(i-4)(i-6) ... (3)(1)`.

### `risingFactorial`
Returns the rising factorial of `x` and `i`:`x(x+1)(x+2)(x+3)...(x+i-1)`Both `x` and `i` can be negative as well as positive.

### `fallingFactorial`
Returns the falling factorial of `x` and `i`:`x(x-1)(x-2)(x-3)...(x-i+1)`This function is only defined for positive `i`. Argument `x` can be either positive or negative.

### `binomialCoefficient`
Requires `k` <= `n`.

### Beta Functions
Take a tour of [Beta Functions](../Guides/Tour-of-Special-Functions.md#beta-functions).


### `beta`
The beta function is defined by: `tgamma(a)*tgamma(b) / tgamma(a+b)`.

### `ibeta`
Returns the normalised incomplete beta function of `a`, `b` and `x`.Require 0 <= `x` <= 1, `a,b` >= 0, and in addition that not both `a` and `b` are zero.

### `ibetaC`
Returns the normalised complement of the incomplete beta function of `a`, `b` and `x`.Require 0 <= `x` <= 1, `a,b` >= 0, and in addition that not both `a` and `b` are zero.

### `betaFull`
Returns the full (non-normalised) incomplete beta function of `a`, `b` and `x`.Require 0 <= `x` <= 1, and `a,b` > 0.

### `betaFullC`
Returns the full (non-normalised) complement of the incomplete beta function of `a`, `b` and `x`.Require 0 <= `x` <= 1, and `a,b` > 0.

### `ibetaInv`
Returns a value `x` such that: `p = ibeta(a, b, x)`.Requires `a,b` > 0 and 0 <= `p` <= 1.

### `ibetaCInv`
Returns a value `x` such that: `q = ibetaC(a, b, x)`.Requires `a,b` > 0 and 0 <= `q` <= 1.

### `ibetaInvA`
Returns a value `a` such that: `p = ibeta(a, b, x)`.Requires `b` > 0, 0 < `x` < 1, and 0 <= `p` <= 1.

### `ibetaCInvA`
Returns a value `a` such that: `q = ibetaC(a, b, x)`.Requires `b` > 0, 0 < `x` < 1, and 0 <= `q` <= 1.

### `ibetaInvB`
Returns a value `b` such that: `p = ibeta(a, b, x)`.Requires `a` > 0, 0 < `x` < 1, and 0 <= `p` <= 1.

### `ibetaCInvB`
Returns a value `b` such that: `q = ibetaC(a, b, x)`.Requires `a` > 0, 0 < `x` < 1, and 0 <= `q` <= 1.

### `ibetaDerivative`
Returns the partial derivative with respect to `x` of the incomplete beta function `ibeta(a, b, x)`.

### Error Functions
Take a tour of [Error Functions](../Guides/Tour-of-Special-Functions.md#error-functions).


### `erf`
Returns the error function of `z`.

### `erfC`
Returns the complement of the error function of `z`.

### `erfInv`
Returns the inverse error function of `z`, that is a value `x` such that:`p = erf(x)`.

### `erfCInv`
Returns the inverse of the complement of the error function of `z`, that is a value `x` such that:`p = erfC(x)`

### Polynomials
Take a tour of [Polynomials](../Guides/Tour-of-Special-Functions.md#polynomials).


### `legendreP`
Returns the Legendre Polynomial of the first kind.Requires -1 <= `x` <= 1.

### `legendrePPrime`
Returns the derivatives of the Legendre polynomials.

### `legendrePZeros`
Since the Legendre polynomials are alternatively even and odd, only the non-negative zeros are returned. For the odd Legendre polynomials, the first zero is always zero. The rest of the zeros are returned in increasing order.

### `legendrePAssoc`
Returns the associated Legendre polynomial of the first kind.Requires -1 <= `x` <= 1.

### `legendreQ`
Returns the value of the Legendre polynomial that is the second solution to the Legendre differential equation.Requires -1 <= `x` <= 1.

### `laguerre`
Returns the value of the Laguerre Polynomial of order `n` at point `x`.

### `laguerreAssoc`
Returns the Associated Laguerre polynomial of degree of dgree `n` and order `m` at point `x`.

### `hermite`
Returns the value of the Hermite Polynomial of order `n` at point `x`.

### `chebyshevT`
Returns the Chebyshev polynomials of the first kind.

### `chebyshevU`
Returns the Chebyshev polynomials of the second kind.

### `chebyshevTPrime`
Returns the derivatives of the Chebyshev polynomials of the first kind.

### `chebyshevTZeros`
Returns the roots (zeros) of the `n`-th Chebyshev polynomial of the first kind.

### `sphericalHarmonic`
Returns the (`Complex`) value of the Spherical Harmonic.`theta` is taken as the polar (colatitudinal) coordinate within `[0, pi]`, and `phi` as the azimuthal (longitudinal) coordinate within `[0, 2pi]`.See boost documentation for further information, including a note about the Condon-Shortley phase term of `(-1)^m`.

### `sphericalHarmonicR`
Returns the real part of the Spherical Harmonic.

### `sphericalHarmonicI`
Returns the imaginary part of the Spherical Harmonic.

### Bessel Functions
Take a tour of [Bessel Functions](../Guides/Tour-of-Special-Functions.md#bessel-functions).


### `cylBesselJ`
Returns the result of the Bessel functions of the first kind.The functions return the result of `domain_error` whenever the result is undefined or complex. This occurs when `x < 0` and `v` is not an integer, or when `x == 0` and `v != 0`.

### `cylNeumann`
Returns the result of the Bessel functions of the second kind.The functions return the result of `domain_error` whenever the result is undefined or complex. This occurs when `x <= 0`.

### `cylBesselJZero`
Returns a single zero or root of the Bessel function of the first kind.`index` is a 1-based index of zero of the cylindrical Bessel function of order `v`.

### `cylNeumannZero`
Returns a single zero or root of the Neumann function (Bessel function of the second kind).`index` is a 1-based index of zero of the cylindrical Neumann function of order `v`.

### `cylBesselI`
Returns the result of the modified Bessel functions of the first kind.

### `cylBesselK`
Returns the result of the modified Bessel functions of the second kind.Requires `x > 0`.

### `sphBessel`
Returns the result of the spherical Bessel functions of the first kind.Requires `x` > 0.

### `sphNeumann`
Returns the result of the spherical Bessel functions of the first kind.Requires `x` > 0.

### `cylBesselJPrime`
Returns the first derivative with respect to x of the corresponding Bessel function.

### `cylNeumannPrime`
Returns the first derivative with respect to x of the corresponding Neumann function.Requires `x > 0`.

### `cylBesselIPrime`
Returns the first derivative with respect to x of the corresponding Bessel function.

### `cylBesselKPrime`
Returns the first derivative with respect to x of the corresponding Bessel function.Requires `x > 0`.

### `sphBesselPrime`
Returns the first derivative with respect to x of the corresponding Bessel function.Requires `x > 0`.

### `sphNeumannPrime`
Returns the first derivative with respect to x of the corresponding Neumann function.Requires `x > 0`.

### Hankel Functions
Take a tour of [Hankel Functions](../Guides/Tour-of-Special-Functions.md#hankel-functions).


### `cylHankel1`
Returns the result of the Hankel functions of the first kind.

### `cylHankel2`
Returns the result of the Hankel functions of the second kind.

### `sphHankel1`
Returns the result of the spherical Hankel functions of the first kind.

### `sphHankel2`
Returns the result of the spherical Hankel functions of the second kind.

### Airy Functions
Take a tour of [Airy Functions](../Guides/Tour-of-Special-Functions.md#airy-functions).


### `airyAi`
Returns the result of the Airy function Ai at `x`.

### `airyBi`
Returns the result of the Airy function Bi at `x`.

### `airyAiPrime`
Returns the derivative of the Airy function Ai at `x`.

### `airyBiPrime`
Returns the derivative of the Airy function Bi at `x`.

### `airyAiZero`
Returns the `m`th zero or root of the Airy Ai function. The Airy Ai function has an infinite number of zeros on the negative real axis.`m` is 1-based.

### `airyBiZero`
Returns the `m`th zero or root (1-based) of the Airy Bi function. The Airy Bi function has an infinite number of zeros on the negative real axis.`m` is 1-based.

### Elliptic Integrals
Take a tour of [Elliptic Integrals](../Guides/Tour-of-Special-Functions.md#elliptic-integrals).


### `ellintRf`
Returns Carlson's Elliptic Integral RF.Requires that `x,y >= 0`, with at most one of them zero, and that `z >= 0`.

### `ellintRd`
Returns Carlson's Elliptic Integral RD.Requires that `x,y >= 0`, with at most one of them zero, and that `z >= 0`.

### `ellintRj`
Returns Carlson's Elliptic Integral RJ.Requires that `x,y,z >= 0`, with at most one of them zero, and that `p != 0`.

### `ellintRc`
Returns Carlson's Elliptic Integral RC.Requires that `x >= 0`, with at most one of them zero, and that `y != 0`.

### `ellintRg`
Returns Carlson's Elliptic Integral RG.Requires that `x,y >= 0`.

### `ellint1`
Returns the incomplete elliptic integral of the first kind, Legendre form.Requires `-1 <= k <= 1`.

### `ellint1C`
Returns the complete elliptic integral of the first kind, Legendre form.Requires `-1 <= k <= 1`.

### `ellint2`
Returns the incomplete elliptic integral of the second kind, Legendre form.Requires `-1 <= k <= 1`.

### `ellint2C`
Returns the complete elliptic integral of the second kind, Legendre form.Requires `-1 <= k <= 1`.

### `ellint3`
Returns the incomplete elliptic integral of the third kind, Legendre form.Requires `-1 <= k <= 1` and `n < 1/sin^2(phi)`.

### `ellint3C`
Returns the complete elliptic integral of the third kind, Legendre form.Requires `-1 <= k <= 1` and `n < 1`.

### `ellintD`
Returns the incomplete elliptic integral **D(phi, k)**, Legendre form.Requires `-1 <= k <= 1`.

### `ellintDC`
Returns the complete elliptic integral **D(phi, k)**, Legendre form.Requires `-1 <= k <= 1`.

### `jacobiZeta`
Returns the result of the Jacobi Zeta Function.Requires `-1 <= k <= 1`.

### `heumanLambda`
Returns the result of the Heuman Lambda Function.Requires `-1 <= k <= 1`.

### Jacobi Elliptic Functions
Like all elliptic functions, these can be parameterised in a number of ways:

- In terms of a parameter `m`.
- In terms of the elliptic modulus `k` where `m = k^2`.
- In terms of the modular angle `α`, where `m = sin2α`.


This implementation takes the elliptic modulus `k` as the parameter. In addition the variable `u` is used to express an amplitude **φ**. All take the elliptic modulus as the first argument - this is for alignment with the [#Elliptic Integrals](#elliptic-integrals).

Take a tour of [Jacobi Elliptic Functions](../Guides/Tour-of-Special-Functions.md#jacobi-elliptic-functions).


### `jacobiCd`


### `jacobiCn`


### `jacobiCs`


### `jacobiDc`


### `jacobiDn`


### `jacobiDs`


### `jacobiNc`


### `jacobiNd`


### `jacobiNs`


### `jacobiSc`


### `jacobiSd`


### `jacobiSn`


### Zeta Functions
Take a tour of [Zeta Functions](../Guides/Tour-of-Special-Functions.md#zeta-functions).


### `zeta`
Returns the zeta function of `z`.Requires `z != 1`.

### Exponential Integrals
Take a tour of [Exponential Integrals](../Guides/Tour-of-Special-Functions.md#exponential-integrals).


### `expintEn`
Returns the exponential integral En of `z`.Requires that when `n == 1`, `z != 0`.

### `expintEi`
Returns the exponential integral of `z`.Requires `z != 0`.

### Basic Functions
Take a tour of [Basic Functions](../Guides/Tour-of-Special-Functions.md#basic-functions).


### `sinPi`
Returns `sin(x * π)`.

### `cosPi`
Returns `cos(x * π)`.

### `log1p`
Returns the natural logarithm of `x+1`.

### `expm1`
Returns `e^x - 1`.

### `cbrt`
Returns the cube root of `x`.

### `sqrt1pm1`
Returns `sqrt(1+x) - 1`.

### `powm1`
Returns `x^y - 1`.

### Sinus Cardinal (Sinc) and Hyperbolic Sinus Cardinal Functions
Take a tour of [Sinus Cardinal (Sinc) and Hyperbolic Sinus Cardinal Functions](../Guides/Tour-of-Special-Functions.md#sinus-cardinal-(sinc)-and-hyperbolic-sinus-cardinal-functions,-inverse-hyperbolic-functions).


### `sincPi`
Returns the Sinus Cardinal of `x`. Also known as the "sinc" function.`sincPi(x) = sin(x) / x`

### `sinhcPi`
Returns the Hyperbolic Sinus Cardinal of `x`.`sinhcPi(x) = sinh(x) / x`

### Inverse Hyperbolic Functions
Take a tour of [Inverse Hyperbolic Functions](../Guides/Tour-of-Special-Functions.md#sinus-cardinal-(sinc)-and-hyperbolic-sinus-cardinal-functions,-inverse-hyperbolic-functions).


### `asinh`
Returns the reciprocal of the hyperbolic sine function at `x`.

### `acosh`
Returns the reciprocal of the hyperbolic cosine function at `x`.Requires `x >= 1`.

### `atanh`
Returns the reciprocal of the hyperbolic sine function at `x`.Requires `-1 < x < 1`.

### Owen's T Function
Take a tour of [Owen's T Function](../Guides/Tour-of-Special-Functions.md#owen).


### `owensT`
Returns the Owens T function of `h` and `a`.



