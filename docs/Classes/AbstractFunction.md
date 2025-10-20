# AbstractFunction

*An object which responds to a set of messages that represent mathematical functions*

**Categories:** Core>Kernel

**Related:** [UGen](../Classes/UGen.md), [Pattern](../Classes/Pattern.md), [Function](../Classes/Function.md), [Overviews/Operators](../Overviews/Operators.md)

## Description

An AbstractFunction is an object which responds to a set of messages that represent mathematical functions. Subclasses override a smaller set of messages to respond to the mathematical functions.
It provides a mechanism for functions that do not calculate values directly but instead compose structures for calculating (lazy evaluation).
Function, Pattern, Stream and UGen are subclasses of AbstractFunction. For example, if you multiply two UGens together the receiver responds by returning a new instance of class BinaryOpUGen which has the two operands as inputs.

```
{ var a, b; a = LFSaw.ar(220); b = LFPulse.ar(1442); [a, b, a * b] }.plot;
```


For an overview of common operators, see [Operators](../Overviews/Operators.md), for specific examples, see also e.g. [Function](../Classes/Function.md), [UGen](../Classes/UGen.md), [Pattern](../Classes/Pattern.md). To see which classes implement a specific method, see that method in the generated [Methods](../Overviews/Methods.md) overview.


## Instance Methods


### Unary Messages
The following messages return an object which represents a delayed unary operation, i.e. an operation on one object. For example, the reciprocal of a function will result in a new function that, when called, returns the reciprocal of the evaluation of the operand.

All of the following messages send the message composeUnaryOp to the receiver with the unary message selector as an argument. See [UnaryOpFunction](../Classes/UnaryOpFunction.md).


### `neg`

```
a = { 10.rand.postln }; b = a.neg; b.value;
// Patterns, Streams, UGens, and Proxies are AbstractFunctions, too:
a = Pgeom(1, 2, 5).neg; a.asStream.nextN(8);
{ a = LFNoise1.ar(1500); [a, a.neg] }.plot;
```



### `reciprocal`

```
a = { 10.rand.postln }; b = a.reciprocal; b.value;
a = Pgeom(1, 2, 5).reciprocal; a.asStream.nextN(8);
{ a = LFNoise1.ar(1500) + 2; [a, a.reciprocal] }.plot;
```



### `bitNot`
Bitwise integer negation.

### `abs`
Absolute value
```
a = { 10.rand - 10.rand }; b = a.abs; b.value;
a = Pseries(3, -1.8, inf).abs; a.asStream.nextN(8);
{ a = LFNoise1.ar(1500); [a, a.abs] }.plot;
```



### `asFloat`

```
a = { "123.471".scramble }; b = a.asFloat; b.value;
```



### `asInt`
Deprecated. Use `asInteger` instead.

### `asInteger`

```
a = { "123471".scramble }; b = a.asInteger; b.value;
```



### `ceil`, `floor`, `frac`

```
a = { 10.0.rand2.postln }; b = a.ceil; b.value;
a = { 10.0.rand2.postln }; b = a.floor; b.value;
a = Pgeom(1, 1.2, inf).ceil; a.asStream.nextN(8);
a = Pgeom(1, 1.2, inf).floor; a.asStream.nextN(8);
{ a = SinOsc.ar(150) * 1.5; [a, a.ceil, a.floor, a.frac] }.plot.superpose_(true);
```



### `sign`
Returns a function that returns -1 if receiver returns a negative number, 1 if positive, and 0 if zero.
```
a = { 10.0.rand2.postln }; b = a.sign; b.value;
{ a = LFNoise1.ar(1500) * 1.5; [a, a.sign] }.plot;
```



### `squared`

```
a = { |x| x + 1 }; b = a.squared; [a.value(1), b.value(1)];
a = Pseries(0, 1, inf).squared; a.asStream.nextN(8);
{ a = LFNoise1.ar(1500); [a, a.squared] }.plot;
```



### `cubed`

```
a = { |x| x + 1 }; b = a.cubed; [a.value(1), b.value(1)];
a = Pseries(0, 1, inf).cubed; a.asStream.nextN(8);
{ a = LFNoise1.ar(1500); [a, a.cubed] }.plot;
```



### `sqrt`

```
a = { |x| x + 1 }; b = a.sqrt; [a.value(1), b.value(1)];
a = Pseries(0, 1, inf).sqrt; a.asStream.nextN(8);
{ a = LFNoise1.ar(1500); [a, a.sqrt] }.plot;
```



### `exp`
Returns e to the power of this.
```
a = { |x| x + 1 }; b = a.exp; [a.value(1), b.value(1)];
a = Pseries(0, 0.25, inf).exp; a.asStream.nextN(8);
{ a = LFNoise1.ar(1500); [a, a.exp] }.plot;
```



### `midicps`
Converts midinote into cycles per seconds (Hz).
```
a = { |x, root = 60| x + root }; b = a.midicps; [a.value(9), b.value(9)];
a = Pseries(60, 1, inf).midicps; a.asStream.nextN(12);
{ a = LFNoise1.ar(1) * 5 + 60; Pulse.ar(a.round.midicps) * 0.1 }.play;
```



### `cpsmidi`
Converts cycles per seconds (Hz) into midinote.
```
a = { |x| #[440, 720, 801, 1020.2].at(x) }; b = a.cpsmidi; [a.value(3), b.value(3)];
a = Pseries(220, 220, inf).cpsmidi; a.asStream.nextN(12); // overtone series as midinotes
// follow but round to next midinote
{ a = Pitch.kr(SoundIn.ar).at(1); Pulse.ar(a.cpsmidi.round.midicps) * 0.1 }.play;
```



### `midiratio`


### `ratiomidi`


### `ampdb`


### `dbamp`


### `octcps`


### `cpsoct`


### `log`


### `log2`


### `log10`


### `sin`


### `cos`


### `tan`


### `asin`


### `acos`


### `atan`


### `sinh`


### `cosh`


### `tanh`


### `rand`


### `rand2`


### `linrand`


### `bilinrand`


### `sum3rand`


### `distort`


### `softclip`


### `coin`


### `even`


### `odd`


### `isPositive`


### `isNegative`


### `isStrictlyPositive`


### `rho`


### `theta`


### Binary Messages
The following messages return an object which represents a delayed binary operation, i.e. an operation between two objects. For example, adding two functions will result in a new function that, when called, adds the results of the evaluation of the two operands.

All of the following messages send the message composeBinaryOp to the receiver with the binary message selector and the second operand as arguments. See: [BinaryOpFunction](../Classes/BinaryOpFunction.md).

Examples:


```
// Add two functions:
x = { |x| x + 1000 } + { |x| x * 100 };
// Evaluate the result, passing in one argument
x.value(2); // posts 1202

// Either operand can be another object
// Add a number and a function:
x = 1871 + { |x| x * 12 };
x.value(12);

// keywords args are passed to each operand:
x = { |t, u| t + 1 } * { |t, u| u - 1 };
x.(t:2, u: 10) // 3 * 9
```



```
// Add two UGens
{ SinOsc.ar(440, 0, 0.2) + PinkNoise.ar(0.1); }.play
```



```
// Add two Patterns
(Pseq([1, 2, 3, 4]) + Prand([0, 0.1, -0.1], inf)).asStream.nextN(5);
```



```
// Add two NodeProxies
Ndef(\x, { SinOsc.ar(440, 0, 0.2) });
Ndef(\y, { PinkNoise.ar(0.1) });
Ndef(\z, Ndef(\x) + Ndef(\y)).play;
```



### `+`

```
({ |x| x.squared } + 3).value(2);
```



### `-`

```
({ |x| x.squared } - 3).value(2);
```



### `*`

```
({ |x| x.squared } * { |x| x.squared }).value(2);
```



### `/`

```
({ |x| x.squared } / 4).value(2);
```



### `div`

```
({ |x| x.squared } div: 3).value(2);
```



### `%`

```
({ |x| x.squared } % 3).value(2);
```



### `**`

```
({ |x| x.squared } ** 3).value(2);
```



### `min`

```
({ |x| x.squared } min: 0).value(2);
```



### `max`

```
({ |x| x.squared } max: 0).value(2);
```



### `<`

```
({ |x| x.squared } < 3).value(2);
```



### `<=`

```
({ |x| x.squared } <= 3).value(2);
```



### `>`

```
({ |x| x.squared } > 3).value(2);
```



### `>=`

```
({ |x| x.squared } >= 3).value(2);
```



### `&`

```
a = { |min, max| ({ rrand(min, max) } ! 4).postln };
(a & a).value(0, 8);
```



### `|`

```
a = { |min, max| ({ rrand(min, max) } ! 4).postln };
(a | a).value(0, 8);
```



### `lcm`

```
a = { |min, max| rrand(min, max).postln };
(a lcm: a).value(0, 8);
```



### `gcd`

```
a = { |min, max| rrand(min, max).postln };
(a gcd: a).value(0, 8);
```



### `round`

```
a = { |max| max.rand.postln };
(a round: 0.5).value(1.0);
```



### `trunc`

```
a = { |max| max.rand.postln };
(a trunc: 2).value(10);
```



### `atan2`

```
a = { 1.0.rand2 };
a.atan2.dup(10);
```



### `hypot`

```
a = { 1.0.rand2 };
a.hypot.dup(10);
```



### `hypotApx`

```
a = { 1.0.rand2 };
a.hypotApx.dup(10);
```



### `>>`

```
a = { [2r10010, 2r101011, 2r11100].choose.postln };
b = a >> 2;
b.value.asBinaryDigits.join;
```



### `+>>`

```
a = { [2r10010, 2r101011, 2r11100].choose.postln };
b = a +>> 2;
b.value.asBinaryDigits.join;
```



### `ring1`
(a * b) + a
```
({ [5, 6, 2].choose.postln } ring1: { [2, -1, 3].choose.postln }).value

// UGens are also abstract functions
(
{ a = SinOsc.ar(335); b = SinOsc.ar(MouseX.kr(1, 1000, 1));
ring1(a, b) * 0.1 }.play;
)
```



### `ring2`
((a*b) + a + b)
```
({ [5, 6, 2].choose.postln } ring2: { [2, -1, 3].choose.postln }).value

(
{ a = SinOsc.ar(335); b = SinOsc.ar(MouseX.kr(1, 1000, 1));
ring2(a, b) * 0.1 }.play;
)
```



### `ring3`
(a * a * b)
```
({ [5, 6, 2].choose.postln } ring3: { [2, -1, 3].choose.postln }).value

(
{ a = SinOsc.ar(335); b = SinOsc.ar(MouseX.kr(1, 1000, 1));
ring3(a, b) * 0.1 }.play;
)
```



### `ring4`
((a*a *b) - (a*b*b))
```
({ [5, 6, 2].choose.postln } ring4: { [2, -1, 3].choose.postln }).value

(
{ a = SinOsc.ar(335); b = SinOsc.ar(MouseX.kr(1, 1000, 1));
ring4(a, b) * 0.1 }.play;
)
```



### `difsqr`
(a*a) - (b*b)
```
({ [5, 6, 2].choose.postln } difsqr: { [2, -1, 3].choose.postln }).value

(
{ a = SinOsc.ar(335); b = SinOsc.ar(MouseX.kr(1, 1000, 1));
difsqr(a, b) * 0.1 }.play;
)
```



### `sumsqr`
(a*a) + (b*b)
```
({ [5, 6, 2].choose.postln } sumsqr: { [2, -1, 3].choose.postln }).value

(
{ a = SinOsc.ar(335); b = SinOsc.ar(MouseX.kr(1, 1000, 1));
sumsqr(a, b) * 0.1 }.play;
)
```



### `sqrdif`
(a - b) ** 2
```
({ [5, 6, 2].choose.postln } sqrdif: { [2, -1, 3].choose.postln }).value

(
{ a = SinOsc.ar(335); b = SinOsc.ar(MouseX.kr(1, 1000, 1));
ring4(a, b) * 0.1 }.play;
)
```



### `sqrsum`
(a + b) ** 2
```
({ [5, 6, 2].choose.postln } sqrsum: { [2, -1, 3].choose.postln }).value

(
{ a = SinOsc.ar(335); b = SinOsc.ar(MouseX.kr(1, 1000, 1));
sqrsum(a, b) * 0.1 }.play;
)
```



### `absdif`
(a - b).abs
```
({ [5, 6, 2].choose.postln } absdif: { [2, -1, 3].choose.postln }).value

(
{ a = SinOsc.ar(335); b = SinOsc.ar(MouseX.kr(1, 1000, 1));
absdif(a, b) * 0.1 }.play;
)
```



### `moddif`
absolute difference in modulo arithmetics.

### `amclip`
0 when b <= 0, a*b when b > 0

### `scaleneg`
a * b when a < 0, otherwise a.

### `clip2`
clips receiver to +/- aNumber

### `excess`
Returns the difference of the receiver and its clipped form.

### `<!`


### `rrand`

```
a = { |x| sin(x) } rrand: { |x| sin(x) *  -1 };
(0..1000).normalize(0, 5pi).collect(a).plot;

(
{ a = SinOsc.ar(335); b = SinOsc.ar(MouseX.kr(1, 1000, 1));
rrand(a, b) * 0.1 }.play;
)
```



### `exprand`


### `rotate`


### `dist`


### `bitAnd`


### `bitOr`


### `bitXor`


### `bitHammingDistance`


### `@`


### Messages with more arguments (n-ary Operators)
The following messages return an object which represents a delayed n-ary operation, i.e. an operation between several objects (often three). For example, rescaling a function with linlin will result in a new function that, when called, scales the results of the evaluation of all operands.

All of the following messages send the message `composeNAryOp` to the receiver with the binary message selector and the other operands as arguments. See [NAryOpFunction](../Classes/NAryOpFunction.md).


### `clip`


### `wrap`


### `fold`


### `blend`


### `linlin`


### `linexp`


### `explin`


### `expexp`


### other

### `applyTo`
Interface that allows us to combine selectors (Symbols) and Functions. Sends valueArray(args) to this.
```
// example:

f = [{ |a, b| a * b * 100.rand }, { |a, b| sin(a) * sin(b) }, '*', '/'];
f.choose.postcs.applyTo(3, 4);

// this is used in SequenceableCollection reduce:
(1..10).reduce('+');
(1..10).reduce({ |a, b| a * b * 1.0.rand });
```



### `asUGenInput`
**Returns:** the result of sending the value(for) message to this.
```
// example:
(
var f, g, product;
f = { SinOsc.ar(400) };
g = { LFPulse.kr(8) };
product = f * g * 0.1;
{ Pan2.ar(product, SinOsc.kr(0.3)) }.play;
)
```



### `sampled`
Sample a function.
```
// sample a function
f = { |x| sin(3*x)*cos(8*x) }
f.plotGraph(from: 0, to: 2);
f.sampled(10, 0, 2).plotGraph(from: 0, to: 2);
f.sampled(80, 0, 2).plotGraph(from: 0, to: 2);

// on complicated functions a sampled function is less cpy heavy.
f = { |x| 60.collect{ 2**((x-rrand(0.0, 1.0))) }.sum/60 };
f.plotGraph(from: 0, to: 1);
g = f.sampled(200);
g.plotGraph(from: 0, to: 1);
{ 200.collect{ f.(rand(0.0, 1.0)) } }.bench;
{ 200.collect{ g.(rand(0.0, 1.0)) } }.bench;
```



### `plotGraph`
Sample the function with n points, in the range [from, to], and plot it in a Plotter. Returns a [Plotter](../Classes/Plotter.md).**Arguments:**

| Argument | Description |
|----------|-------------|
| `n` | Number of values displayed in the plot window (500 by default). |  
| `from` | Minimum value passed to the function. |  
| `to` | Maximum value passed to the function. |  
| `name` | See [plot](../Reference/plot.md) |  
| `bounds` | See [plot](../Reference/plot.md) |  
| `discrete` | See [plot](../Reference/plot.md) |  
| `numChannels` | See [plot](../Reference/plot.md) |  
| `minval` | See [plot](../Reference/plot.md) |  
| `maxval` | See [plot](../Reference/plot.md) |  
| `separately` | See [plot](../Reference/plot.md) |  
| `parent` | See [plot](../Reference/plot.md) |  
**Returns:** a [Plotter](../Classes/Plotter.md)
```
// plot x.squared transfer function with x between -1 and 1.
// here the x-axis shows n, the number of points
{ |x| x.squared }.plotGraph(n: 200, from: -1, to: 1);

// as plotGraph returns a Plotter, you can apply a domain spec to show x value on the x-axis
{ |x| x.squared }.plotGraph(n: 200, from: -1, to: 1).domainSpecs_([-1, 1, \lin].asSpec).refresh;
```



### Function Composition
The composition operator `<>` is used to perform function chaining (function composition), whereby $f \cdot g = f(g(x))$. Note that different subclasses like [Pattern](../Classes/Pattern.md) or [UGen](../Classes/UGen.md) have their own composition scheme analogous to the one of AbstractFunction itself.


```
// compose a function that will return an array of random length
a = { |n| { 16.rand } ! n } <> { rrand(4, 8) };
a.value;
// compose a function from a that selects only odd values
b = { |x| x.select(_.odd) } <> a;
b.value;

// call arguments are passed to the first (rightmost) function:
a = { |n| { 16.rand } ! n } <> { |n| n + 2 };
a.value(3);
```



> **Note:** The comparison operators `<`, `<=`, `>` and `>=` automatically perform function composition, as does `*` in the example above.Equality comparisons have two possible meanings: to compare the objects as they exist right now, or a composite operator that will evaluate the operands in the future and check the equality of those results. Both are needed at different times, and are supported by different operators: `==` for an immediate equality check (which always returns a Boolean result), or `|==|` for a "lazy" equality operator to be performed later.



```
f = { 2.rand };  // a function

// eager (immediate) equality
// false: the function as itself is not the same as '1'
g = (f == 1);

g.value;  // still false

// lazy equality
g = (f |==| 1);  // a BinaryOpFunction

g.value;  // true or false, depending on f's result
```



## Examples


```
// examples

a = { 1.0.rand } + 8;
a.value;


y = { 8 } + { 1.0.rand };
y.value;
```



```
// arguments are passed into both functions

y = { |x = 0| x } + { 1.0.rand };
y.value(10);


y = { |x = 0| x * 3 } + { |x = 0| x + 1.0.rand };
y.value(10);

y.postcs;

y = { |x = 0| x * 3 } + { |x = 0| x + 1.0.rand } * { |x = 0| [50, 100].choose + x } + 1.0;
y.value(10);
```



```
// environments can be used as a lookup with valueEnvir:

(
Environment.use {
    ~y = 10;
    ~x = 2;
    ~z = { |x = 8| x } + { |y = 0| y + 1.0.rand };
    ~z.valueEnvir;
}
)
```



```
// n-ary operators:

a = blend({ 3.0.rand }, { 1000.rand }, { |frac| frac });
a.value(0.5);

a.value((0, 0.06..1)); // creates a range of values..
```




