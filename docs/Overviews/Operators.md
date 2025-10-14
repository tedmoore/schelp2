# Operators

**Categories:** Language, Common methods

*common unary and binary operators*

**Related:** [Adverbs](../Reference/Adverbs.md)

SuperCollider supports operator overloading. Operators can thus be applied to a variety of different objects; Numbers, UGens, Collections, and so on. When operators are applied to UGens they result in [BinaryOpUGen](../Classes/BinaryOpUGen.md)s or [UnaryOpUGen](../Classes/UnaryOpUGen.md)s, through the methods of [AbstractFunction](../Classes/AbstractFunction.md).
This is a list of some of the common unary and binary operators that are implemented by several classes. See the specific classes for details and other operators.
You can see which classes implements a specific operator by clicking on the method name.

## Unary Operators
Unary operators may be written in two ways:


```supercollider
a.operator
operator(a)
```



### Arithmetics
### `neg`
Inversion.
```supercollider
{
    var a;
    a = FSinOsc.ar(300);
    [ a, a.neg ]
}.plot
```


### `reciprocal`
Reciprocal (1/x).
### `abs`
Absolute value.
### `floor`
Next lower integer.
```supercollider
{
    var a;
    a = Line.ar(-1, 1, 0.01);
    [ a, a.floor ]
}.plot
```


### `ceil`
Next higher integer.
```supercollider
{
    var a;
    a = Line.ar(-1, 1, 0.01);
    [ a, a.ceil ]
}.plot
```


### `frac`
Fractional part.
### `sign`
Sign function.**Returns:** -1 when a < 0, +1 when a > 0, 0 when a is 0
### `squared`
Squared value.**Returns:** `a*a`
### `cubed`
Cubed value.**Returns:** `a*a*a`
### `sqrt`
Square root.The definition of square root is extended for signals so that sqrt(a) when a<0 returns -sqrt(-a).
### `exp`
Exponential.



### Musical acoustics
### `midicps`
Convert MIDI note number to cycles per second.
```supercollider
{
    Saw.ar(Line.kr(24,108,10).midicps, 0.2)
}.play
```


### `cpsmidi`
Convert cycles per second to MIDI note.
### `midiratio`
Convert an interval in MIDI notes into a frequency ratio.
### `ratiomidi`
Convert a frequency ratio to an interval in MIDI notes.
### `dbamp`
Convert decibels to linear amplitude.
### `ampdb`
Convert linear amplitude to decibels.
### `octcps`
Convert decimal octaves to cycles per second.
### `cpsoct`
Convert cycles per second to decimal octaves.



### Random operators
See also [Randomness](../Guides/Randomness.md).

As with other operators, these work on a variety of receivers:


```supercollider
42.rand;
42.0.rand;
8.do { [0, 1, 2, 3, 4].rrand(5).postln; };
{ SinOsc.ar(110).bilinrand }.plot;

{ 10.rand2 }.dup(30).plot.plotMode_(\steps)
{ 10.0.rand2 }.dup(30).plot.plotMode_(\steps)
```





### Other
### `log`
Natural logarithm.
```supercollider
{
    var a, e;
    e = exp(1);
    a = Line.ar(e, 1/e, 0.01);
    a.log
}.plot
```


### `log2`
Base 2 logarithm.
### `log10`
Base 10 logarithm.
### `sin`
Sine.
### `cos`
Cosine.
### `tan`
Tangent.
### `asin`
Arcsine.
### `acos`
Arccosine.
### `atan`
Arctangent.
### `sinh`
Hyperbolic sine.
### `cosh`
Hyperbolic cosine.
### `tanh`
Hyperbolic tangent.
### `distort`
Nonlinear distortion.The formula used is :
```supercollider
x / (1 + abs(x))
```

Here is an example :
```supercollider
(
{
    var a;
    a = Line.ar(-4, 4, 0.01);
    a.distort
}.plot
)

{ FSinOsc.ar(500, 0.0, XLine.kr(0.1, 10, 10)).distort * 0.25 }.scope;
```


### `softclip`
Nonlinear distortion.Distortion with a perfectly linear region from -0.5 to +0.5
```supercollider
(
{
    var a;
    a = Line.ar(-2, 2, 0.01);
    a.softclip
}.plot
)


{ FSinOsc.ar(500,0.0, XLine.kr(0.1, 10, 10)).softclip * 0.25 }.scope(2);
```


### `isPositive`
Test if signal is >= 0.
### `isNegative`
Test if signal is < 0.
### `isStrictlyPositive`
Test if signal is > 0.




## Binary Operators
Three different syntaxes can be used for binary operators consisting of letters:


```supercollider
operator(a, b)

a operator: b

a.operator(b)
```


Operators consisting of symbols are written like this:


```supercollider
a + b
```



### Arithmetics
### `+`
Addition.
### `-`
Subtraction.
### `*`
Multiplication.
### `/`
Division.
### `%`
Modulo.
> **Note:** Uses floored division. Prior to SC 3.14, integer modulo would exhibit unexpected behavior for negative modulus; see [Integer#-modSeaside](../Classes/Integer.md#-modseaside).


### `**`
Exponentiation. Same as pow.
### `pow`
Exponentiation.
> **Note:** When used with UGens which produce a negative signal this function extends the usual definition of exponentiation and returns `neg(neg(a) ** b)`. This allows exponentiation of negative signal values by noninteger exponents.


### `lcm`
Least common multiple. This definition extends the usual definition and returns a negative number if **any of the operands** is negative. This makes it consistent with the lattice-theoretical interpretation and its idempotency, commutative, associative, absorption laws.Following the example of the programming language J (see: [J-concepts-in-SC](../Guides/J-concepts-in-SC.md)), lcm is analogous to logical **and** (see also: [http://www.jsoftware.com/papers/eem/gcd.htm](http://www.jsoftware.com/papers/eem/gcd.htm)).
```supercollider
lcm(4, 6);
lcm(1, 1); // and
lcm(1624, 26);
lcm(1624, -26);
lcm(-1624, -26);
lcm(513, gcd(513, 44)) // absorption law -> 513.
```


```supercollider
(
{
    var mx = MouseX.kr(-20, 20);
    var my = MouseY.kr(-20, 20);
    SinOsc.ar(SinOsc.kr(0.3) * 20 lcm: [mx, my] * 30 + 500) * 0.1
}.play;
)
```


### `gcd`
Greatest common divisor. This definition extends the usual definition and returns a negative number if **both operands** are negative. This makes it consistent with the lattice-theoretical interpretation and its idempotency, commutative, associative, absorption laws."greater" means "divisible by" in this interpretation, so `gcd(-1, -1)` returns a negative number. This is necessary to make the whole system consistent (fundamental law of arithmetics, idempotency and absorption laws would fail). See examples below.Following the example of the programming language J (see: [J-concepts-in-SC](../Guides/J-concepts-in-SC.md)), gcd is analogous to logical **or** (see also: [http://www.jsoftware.com/papers/eem/gcd.htm](http://www.jsoftware.com/papers/eem/gcd.htm)).
```supercollider
gcd(4, 6);
gcd(0, 1); // or
gcd(1024, 256);
gcd(1024, -256);
gcd(-1024, -256); // "greater" means "divisible by" in this case, so this returns a negative number.
gcd(-1024, lcm(-1024, 256)) // absorption law -> -1024.
gcd(66, 54) * lcm(66, 54) == (66 * 54); // true
```


```supercollider
(
{
    var mx = MouseX.kr(-200, 200);
    var my = MouseY.kr(-200, 200);
    SinOsc.ar(SinOsc.kr(0.3) * 20 gcd: [mx, my] * 30 + 500) * 0.1
}.play;
)
```

Here is an overview of how negative numbers are treated:
```supercollider
lcm(4, 6) // -> 12. "least multiple" interpreted as smallest in Z
lcm(4, -6) // -> -12 "least multiple" interpreted as smallest in Z
lcm(-4, -6) // -> -12 "least multiple" interpreted as smallest in Z

gcd(4, 6) // -> 2 "greatest divisor" interpreted as highest in Z
gcd(4, -6) // -> 2 "greatest divisor" is interpreted as highest in Z
gcd(-4, -6) // -> -2 "greatest divisor" is interpreted as *inverse* in Z. This is the only necessary asymmetry.
```





### Comparisons
### `<`
Less than.
### `<=`
Less than or equal.
### `>`
Greater than.With UGens, this can be useful for triggering purposes, among other things:
```supercollider
(
{ // trigger an envelope
    var trig;
    trig = SinOsc.ar(1) > 0;
    EnvGen.kr(Env.perc, trig, doneAction: Done.none)
            * SinOsc.ar(440, 0, 0.1)
}.play
)

// trigger a synth
(
SynthDef("help-EnvGen", { arg out=0;
    Out.ar(out,
        EnvGen.kr(Env.perc,1.0,doneAction: Done.freeSelf)
            * SinOsc.ar(440, 0, 0.1)
    )
}).add;

// This synth has no output. It only checks amplitude of input and looks for a transition from < 0.2
// to > 0.2

{ SendTrig.kr(Amplitude.kr(SoundIn.ar(0)) > 0.2) }.play;

// OSCFunc to trigger synth
OSCFunc({ "triggered".postln; Synth.new("help-EnvGen") },'/tr', s.addr);
)
```


### `>=`
Greater than or equal.
### `==`
Equal.
### `!=`
Not equal.
### `|==|`
"Lazy equality." See [Object#-|==|](../Classes/Object.md#-|==|).



### Other
### `<!`
Return first argument.
```supercollider
// this is useful when two UGens need to be called, but only one of their outputs is needed
(
{
    var a, b, c;
    a = Dseq([1, 2, 3, 4], inf).dpoll("a");
    b = Dseq([1955, 1952, 1823, 1452], inf).dpoll("b");
    c = (a <! b).dpoll("------> a <! b = "); // c only
    Duty.kr(0.4, 0, c);
    0.0
}.play
)
```


### `min`
Minimum.
```supercollider
{ // distorts and envelopes z
var z;
z = FSinOsc.ar(500);
z min: FSinOsc.ar(0.1);
}.play;
```


### `max`
Maximum.
```supercollider
{ // modulates and envelopes z
var z;
z = FSinOsc.ar(500);
z max: FSinOsc.ar(0.1);
}.play;
```


### `round`
Quantization by rounding. Rounds a to the nearest multiple of b.
### `trunc`
Quantization by truncation. Truncate a to a multiple of b.
### `hypot`
Hypotenuse. Returns the square root of the sum of the squares of a and b. Or equivalently, the distance from the origin to the point (x, y).In this example, hypot is used to calculate a doppler shift pitch and amplitude based on distance.
```supercollider
(
{
    var x, y, distance, velocity, pitchRatio, amplitude;
    // object travels 200 meters in 6 secs (=120kph) passing 10 meters
    // from the listener
    x = 10;
    y = LFSaw.kr(1/6, 0, 100);
    distance = hypot(x, y);
    velocity = Slope.kr(distance);
    pitchRatio = (344 - velocity) / 344;  // speed of sound is 344 meters/sec
    amplitude = 10 / distance.squared;
    FSinOsc.ar(1000 * pitchRatio, 0, amplitude)
}.play)
```

The next example uses the distance to modulate a delay line.
```supercollider
(
{
    var x, y, distance, velocity, pitchRatio, amplitude, motorSound;
    // object travels 200 meters in 6 secs (=120kph) passing 10 meters
    // from the listener
    x = 10;
    y = LFSaw.kr(1/6, 0, 100);
    distance = hypot(x, y);
    amplitude = 40 / distance.squared;
    motorSound = RLPF.ar(FSinOsc.ar(200, 0, LFPulse.ar(31.3, 0, 0.4)), 400, 0.3);
    DelayL.ar(motorSound, 110/344, distance/344, amplitude)
}.play)
```


### `hypotApx`
Hypotenuse approximation. Returns an approximation of the square root of the sum of the squares of x and y.The formula used is :
```supercollider
abs(x) + abs(y) - ((sqrt(2) - 1) * min(abs(x), abs(y)))
```

hypotApx is used to implement Complex method magnitudeApx. This should not be used for simulating a doppler shift because it is discontinuous. Use hypot.See also [#hypot](#hypot), [#atan2](#atan2).
### `atan2`
Returns the arctangent of y/x.OK, now we can add a pan to the [#hypot](#hypot) doppler examples by using atan2 to find the azimuth, or direction angle, of the sound source. Assume speakers at +/- 45 degrees and clip the direction to between those.
```supercollider
(
{
    var x, y, distance, velocity, pitchRatio, amplitude, azimuth, panValue;
    // object travels 200 meters in 6 secs (=120kph) passing 10 meters
    // from the listener
    x = 10;
    y = LFSaw.kr(1/6, 0, 100);
    distance = hypot(x, y);
    velocity = Slope.kr(distance);
    pitchRatio = (344 - velocity) / 344;  // speed of sound is 344 meters/sec
    amplitude = 10 / distance.squared;
    azimuth = atan2(y, x); // azimuth in radians
    panValue = (azimuth / 0.5pi).clip2(1);
    Pan2.ar(FSinOsc.ar(1000 * pitchRatio), panValue, amplitude)
}.play)

(
{
    var x, y, distance, velocity, pitchRatio, amplitude, motorSound,
            azimuth, panValue;
    // object travels 200 meters in 6 secs (=120kph) passing 10 meters
    // from the listener
    x = 10;
    y = LFSaw.kr(1/6, 0, 100);
    distance = hypot(x, y);
    amplitude = 40 / distance.squared;
    motorSound = RLPF.ar(FSinOsc.ar(200, 0, LFPulse.ar(31.3, 0, 0.4)), 400, 0.3);
    azimuth = atan2(y, x); // azimuth in radians
    panValue = (azimuth / 0.5pi).clip2(1); // make a value for Pan2 from azimuth
    Pan2.ar(DelayL.ar(motorSound, 110/344, distance/344), panValue, amplitude)
}.play)
```


### `ring1`
Ring modulation plus first source.Return the value of ((a*b) + a). This is more efficient than using separate unit generators for the multiply and add.See also [#*](#*), [#ring1](#ring1), [#ring2](#ring2), [#ring3](#ring3), [#ring4](#ring4).
```supercollider
{ (FSinOsc.ar(800) ring1: FSinOsc.ar(XLine.kr(200,500,5))) * 0.125 }.play;
```

same as :
```supercollider
(
{
    var a, b;
    a = FSinOsc.ar(800);
    b = FSinOsc.ar(XLine.kr(200,500,5));
    ((a * b) + a) * 0.125
}.play)
```

normal ring modulation:
```supercollider
(
{
    var a, b;
    a = FSinOsc.ar(800);
    b = FSinOsc.ar(XLine.kr(200,500,5));
    (a * b) * 0.125
}.play)
```


### `ring2`
Ring modulation plus both sources.Return the value of ((a*b) + a + b). This is more efficient than using separate unit generators for the multiply and adds.
```supercollider
{ (FSinOsc.ar(800) ring2: FSinOsc.ar(XLine.kr(200,500,5))) * 0.125 }.play;
```

same as :
```supercollider
(
{
    var a, b;
    a = FSinOsc.ar(800);
    b = FSinOsc.ar(XLine.kr(200,500,5));
    ((a * b) + a + b) * 0.125
}.play)
```


### `ring3`
Ring modulation variant.Return the value of (a*a *b). This is more efficient than using separate unit generators for each multiply.
```supercollider
{ (FSinOsc.ar(800) ring3: FSinOsc.ar(XLine.kr(200,500,5))) * 0.125 }.play;
```

same as :
```supercollider
(
{
    var a, b;
    a = FSinOsc.ar(800);
    b = FSinOsc.ar(XLine.kr(200,500,5));
    (a * a * b) * 0.125;
}.play)
```


### `ring4`
Ring modulation variant.Return the value of ((a*a *b) - (a*b*b)). This is more efficient than using separate unit generators for each operation.
```supercollider
{ (FSinOsc.ar(800) ring4: FSinOsc.ar(XLine.kr(200,500,5))) * 0.125 }.play;
```

same as :
```supercollider
(
{
    var a, b;
    a = FSinOsc.ar(800);
    b = FSinOsc.ar(XLine.kr(200,500,5));
    ((a * a * b) - (a * b * b)) * 0.125
}.play)
```


### `sumsqr`
Sum of squares.Return the value of (a*a) + (b*b). This is more efficient than using separate unit generators for each operation.
```supercollider
{ (FSinOsc.ar(800) sumsqr: FSinOsc.ar(XLine.kr(200,500,5))) * 0.125 }.play;
```

same as :
```supercollider
(
{
    var a, b;
    a = FSinOsc.ar(800);
    b = FSinOsc.ar(XLine.kr(200,500,5));
    ((a * a) + (b * b)) * 0.125
}.play)
```


### `difsqr`
Difference of squares.Return the value of (a*a) - (b*b). This is more efficient than using separate unit generators for each operation.
```supercollider
{ (FSinOsc.ar(800) difsqr: FSinOsc.ar(XLine.kr(200,500,5))) * 0.125 }.play;
```

same as :
```supercollider
(
{
    var a, b;
    a = FSinOsc.ar(800);
    b = FSinOsc.ar(XLine.kr(200,500,5));
    ((a * a) - (b * b)) * 0.125
}.play)
```


### `sqrsum`
Square of the sum.Return the value of (a + b)**2. This is more efficient than using separate unit generators for each operation.
```supercollider
{ (FSinOsc.ar(800) sqrsum: FSinOsc.ar(XLine.kr(200,500,5))) * 0.125 }.play;
```

same as :
```supercollider
(
{
    var a, b, c;
    a = FSinOsc.ar(800);
    b = FSinOsc.ar(XLine.kr(200,500,5));
    c = a + b;
    (c * c) * 0.125
}.play)
```


### `sqrdif`
Square of the difference.Return the value of (a - b)**2. This is more efficient than using separate unit generators for each operation.
```supercollider
{ (FSinOsc.ar(800) sqrdif: FSinOsc.ar(XLine.kr(200,500,5))) * 0.125 }.play;
```

same as :
```supercollider
(
{
    var a, b, c;
    a = FSinOsc.ar(800);
    b = FSinOsc.ar(XLine.kr(200,500,5));
    c = a - b;
    (c * c) * 0.125
}.play)
```


### `absdif`
Absolute value of the difference. `abs(a - b)`
```supercollider
(
{ // creates a rhythm
var mul = 0.2 absdif: FSinOsc.ar(2, 0, 0.5);
FSinOsc.ar(440, 0, mul);
}.play;
)
```


### `moddif`
On a circle, there are two distances between two points. This operator returns the smaller value of the two.
```supercollider
{ Line.ar(0, 4, 0.01).moddif(0) }.plot;
(
{
var mul = 0.2 moddif: FSinOsc.ar(2, 0, 0.5);
FSinOsc.ar(440, 0, mul);
}.play;
)
```


### `thresh`
Thresholding.0 when a < b, otherwise a.
```supercollider
{ LFNoise0.ar(50, 0.5) thresh: 0.45 }.play // a low-rent gate
```


### `amclip`
Two quadrant multiply.0 when b <= 0,  a*b when b > 0
```supercollider
{ WhiteNoise.ar.amclip(FSinOsc.kr(1,0.2)) }.play; // makes a sine envelope
```


### `scaleneg`
Scale negative part of input.a*b when a < 0, otherwise a.
```supercollider
{ FSinOsc.ar(500).scaleneg(Line.ar(1,-1,4)) }.play;
```


### `clip2`
Bilateral clipping.clips input wave a to +/- b
```supercollider
(
{
    var a;
    a = Line.ar(-2, 2, 0.01);
    a.clip2
}.plot
)

{ FSinOsc.ar(400).clip2(0.2) }.scope; // clipping distortion

{ FSinOsc.ar(1000).clip2(Line.kr(0,1,8)) }.scope;
```


### `wrap2`
Bilateral wrapping.wraps input wave to +/- b
```supercollider
(
{
    var a;
    a = Line.ar(-2, 2, 0.01);
    a.wrap2
}.plot
)

{ FSinOsc.ar(1000).wrap2(Line.kr(0,1.01,8)) }.scope;
```


### `fold2`
Bilateral folding.folds input wave a to +/- b
```supercollider
(
{
    var a;
    a = Line.ar(-2, 2, 0.01);
    a.fold2
}.plot
)


{ FSinOsc.ar(1000).fold2(Line.kr(0,1,8)) }.scope;
```


### `excess`
Residual of clipping.Returns the difference of the original signal and its clipped form: (a - clip2(a,b)).
```supercollider
(
{
    var a;
    a = Line.ar(-2, 2, 0.01);
    a.excess
}.plot
)

{ FSinOsc.ar(1000).excess(Line.kr(0,1,8)) }.play;
```






