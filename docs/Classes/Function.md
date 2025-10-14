# Function

*Implements a function*

**Categories:** Core>Kernel

**Related:** [Functions](../Reference/Functions.md), [AbstractFunction](../Classes/AbstractFunction.md), [FunctionDef](../Classes/FunctionDef.md)

This document deals with the usage of Function objects.  For a more general introduction and documentation of syntax, see [Functions](../Reference/Functions.md).
## Description

A Function is a reference to a FunctionDef and its defining context Frame. When a FunctionDef is encountered in your code it is pushed on the stack as a Function. A Function can be evaluated by using the 'value' method.
Because it inherits from AbstractFunction, Functions respond to math operations by creating a new Function.

```supercollider
// example
(
var a, b, c;
a = { [100, 200, 300].choose };    // a Function
b = { 10.rand + 1 };    // another Function
c = a + b;     // c is a Function.
c.value.postln;    // evaluate c and print the result
)
```


See [AbstractFunction#Function Composition](../Classes/AbstractFunction.md#function-composition) for function composition examples.
Because Functions are such an important concept, here some examples from related programming languages with functions as first class objects:

```supercollider
// returning the first argument itself:
{ |x| x }.value(1) // SuperCollider
[:x | x ] value: 1 // Smalltalk
((lambda (x) x) 1) // Lisp
```



### Related Keywords
### `thisFunction`
The global pseudo-variable `thisFunction` always evaluates to the current enclosing Function.
> **Note:** Be aware that `thisFunction` may refer to different functions depending on function inlining. See [Conditional-Execution#Optimization through inline expansion](../Reference/Conditional-Execution.md#optimization-through-inline-expansion).

See also: [thisFunctionDef](../Classes/FunctionDef.md#.thisfunctiondef)



## Class Methods



## Instance Methods


### Access
### `def`
Get the definition (FunctionDef) of the Function.
### `isClosed`
returns true if the function is closed, i.e. has no external references and can thus be converted to a compile string safely.

### Evaluation
### `value`
Evaluates the FunctionDef referred to by the Function. The Function is passed the args given.
```supercollider
 // different way of expressing the same:
{ |a, b| a * b }.value(3, 10);
{ |a, b| a * b }.value(a: 3, b: 10); // keyword arguments
{ |a, b| a * b }.(3, 10); // short syntax: "value" can be dropped.
```

Default arguments can be omitted in the call:
```supercollider
{ |a=3, b=10| a * b }.value; // use default arguments only
{ |a=3, b=10| a * b }.value(2); // only set the first argument (a)
{ |a=3, b=10| a * b }.value(b: 100); // set the second argument (b) without the first
```

The results of functions composed with operators distribute the keyword arguments to each of the operands.
```supercollider
f = { |a, b=1| a ** b } * { |a, c = 0| a + c };
f.value(1); // default arguments for b and c
f.value(1, b:2); // explicitly specify a (the other function warns)
(b:2.5).use { f.valueEnvir(2) } // to avoid the warnings, you can use valueEnvir (see below)
```


### `valueArray`
Evaluates the FunctionDef referred to by the Function. If the last argument is an Array or List, then it is unpacked and appended to the other arguments (if any) to the Function. If the last argument is not an Array or List then this is the same as the 'value' method.
```supercollider
{ |a, b, c| ((a * b) + c).postln }.valueArray([3, 10, 7]);

{ |a, b, c, d| [a, b, c, d].postln }.valueArray([1, 2, 3]);

{ |a, b, c, d| [a, b, c, d].postln }.valueArray(9, [1, 2, 3]);

{ |a, b, c, d| [a, b, c, d].postln }.valueArray(9, 10, [1, 2, 3]);
```

A common syntactic shortcut:
```supercollider
{ |a, b, c| ((a * b) + c).postln }.value(*[3, 10, 7]);
```


### `valueEnvir`
As value above. Unsupplied argument names are looked up in the current Environment.
```supercollider
(
Environment.use({
~a = 3;
~b = 10;
{ |a, b| (a * b).postln }.valueEnvir;
});
)

// or syntactically shorter using an Event:

(a:3, b:10).use { { |a, b| (a * b).postln }.valueEnvir };
```


### `valueArrayEnvir`
Evaluates the FunctionDef referred to by the Function. If the last argument is an Array or List, then it is unpacked and appended to the other arguments (if any) to the Function. If the last argument is not an Array or List then this is the same as the 'value' method. Unsupplied argument names are looked up in the current Environment.
### `valueWithEnvir`
Evaluate the function, using arguments from the supplied environment. This is slightly faster than valueEnvir and does not require replacing the currentEnvironment.
```supercollider
(
e = Environment.make({ ~a = 3; ~b = 10 });
{ |a, b| (a * b) }.valueWithEnvir(e);
)
```


### `functionPerformList`
For Function, this behaves the same as valueArray(arglist). It is used where Functions and other objects should behave differently to value, such as in the object prototyping implementation of Environment.
### `performWithEnvir`

```supercollider
a = { |a, b, c| postf("% plus % plus % is %\n", a, b, c, a + b + c); "" };
a.performWithEnvir(\value, (a: 1, c: 3, d: 4, b: 2));
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `selector` | A Symbol representing a method selector. |  
| `envir` | The remaining arguments derived from the environment and passed as arguments to the method named by the selector. |  

### `performKeyValuePairs`

```supercollider
a = { |a, b, c| postf("% plus % plus % is %\n", a, b, c, a + b + c); "" };
a.performKeyValuePairs(\value, [\a, 1, \b, 2, \c, 3, \d, 4]);
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `selector` | A Symbol representing a method selector. |  
| `pairs` | Array or List with key-value pairs. |  

### `loop`
Repeat this function. Useful with Task and Clocks.
```supercollider
t = Task({ { "I'm loopy".postln; 1.wait }.loop });
t.start;
t.stop;
```


### `defer`
Delay the evaluation of this Function by `delta` in seconds on AppClock.This is equivalent to `AppClock.sched(0, function)` unless `delta` is `nil`. In that case the function is only scheduled if current code is not running on AppClock, otherwise the function is evaluated immediately.
```supercollider
{ "2 seconds have passed.".postln }.defer(2);

(
{ "chicken".postln }.defer(0); // schedules on the AppClock
{ "egg".postln }.defer // evaluates immediately
)

(
fork { // schedules on a TempoClock
    { "chicken".postln }.defer // schedules on the AppClock
};
{ "egg".postln }.defer // evaluates immediately
)
```


### `dup`
Return an Array consisting of the results of n evaluations of this Function.
```supercollider
x = { 4.rand }.dup(4);
x.postln;
```


### `!`
equivalent to dup(n)
```supercollider
x = { 4.rand } ! 4;
x.postln;
```


### `sum`
return the sum of n values produced.
```supercollider
{ 4.rand }.sum(8);
```


### `choose`
evaluates the function. This makes it polymorphic to SequenceableCollection, Bag and Set.
```supercollider
[{ 100.rand }, [20, 30, 40]].collect(_.choose);
```


### `bench`
Returns the amount of time this function takes to evaluate. print is a boolean indicating whether the result is posted. The default is true.
```supercollider
{ 1000000.do({ 1.0.rand }) }.bench;
```


### `fork`
Returns a Routine using the receiver as it's function, and plays it in a TempoClock.
```supercollider
{ 4.do({ "Threading...".postln; 1.wait }) }.fork;
```


### `forkIfNeeded`
If needed, creates a new Routine to evaluate the function in, if the message is called within a routine already, it simply evaluates it.
```supercollider
f = { 4.do({ "Threading...".postln; 1.wait }) };
f.forkIfNeeded;
{ "we are now in a routine".postln; 1.wait; f.forkIfNeeded }.fork;
```


### `block`
Break from a loop. Calls the receiver with an argument which is a function that returns from the method block. To exit the loop, call .value on the function passed in. You can pass a value to this function and that value will be returned from the block method.
```supercollider
block { |break|
    100.do { |i|
        i.postln;
        if (i == 7) { break.value(999) }
    };
}
```


### `thunk`
Return a Thunk, which is an unevaluated value that can be used in calculations
```supercollider
x = thunk { 4.rand };
x.value;
x.value;
```


### `flop`
Return a function that, when evaluated with nested arguments, does multichannel expansion by evaluating the receiver function for each channel. A flopped function responds like the "map" function in languages like Lisp. The new function always returns an array.
```supercollider
// multichannel expansion for if, here to protect from division by zero:
f = { |a, b| if(b != 0) { a / b } { 0 } }.flop;
f.value([1, 2, 3, 4], [0, 10, 1000]); //  -> [0, 0.2, 0.003, 0]
f.value(2, 4); // [0.5] (always returns an array)

// strings don't expand
f = { |a, b| a + b }.flop;
f.("hello", ["world", "algorithm"]); // -> [hello world, hello algorithm]
f.("hello", "world"); // -> [hello world]
```


### `flop1`
Same as [#flop](#flop), return only an array if the arguments also contains an array. This can be used to implement [Multichannel-Expansion](../Guides/Multichannel-Expansion.md).
```supercollider
// multichannel expansion for if, here to protect from division by zero:
f = { |a, b| if(b != 0) { a / b } { 0 } }.flop1;
f.value([1, 2, 3, 4], [0, 10, 1000]); //  -> [0, 0.2, 0.003, 0]
f.value([2], 4); // -> [0.5]
f.value(2, 4); // -> 0.5

// strings don't expand, like in flop
f = { |a, b| a + b }.flop1;
f.("hello", ["world", "algorithm"]); // -> [hello world, hello algorithm]
f.("hello", "world"); // -> hello world
```


### `envirFlop`
This method is kept for backward compatibility. Use `flop` instead.
### `inEnvir`
returns an "environment-safe" function. See Environment for more details. Note that the function returned takes no keyword arguments.
```supercollider
e = (a: "get it", b: "didn't");
f = { ~b + ~a + "..." }.inEnvir(e);
f.value;

f = { |how = "", end = "..."| how + ~b + ~a + end }.inEnvir(e); // doesn't work with keyword arguments
f.value(how: "really"); // WARNING: keyword arg 'how' not found in call to function (see inEnvirWithArgs).



// a use case: defer is usually called in the call environment
// prints nil because ~a is read from topEnvironment, not e
e = (a: "got it", f: { { ~a.postln }.defer(0.5) });
e.use { e.f };

// prints "got it" because { ~a.postln } is now bound to the e environment
e = (a: "got it", f: { { ~a.postln }.inEnvir.defer(0.5) });
e.use { e.f };
```


### `inEnvirWithArgs`
Like [#inEnvir](#inenvir), but returns a function which takes keyword arguments. Building this function makes a call to the interpreter and is less efficient than inEnvir
```supercollider
e = (a: "get it", b: "didn't");
f = { |how = "", end = "..."| how + ~b + ~a + end }.inEnvirWithArgs(e);
f.value(how: "I really", end: "done!");
```


### `case`
Function implements a case method which allows for conditional evaluation with multiple cases. Since the receiver represents the first case this can be simply written as pairs of test functions and corresponding functions to be evaluated if true. Unlike Object-switch, this is inlined and is therefore just as efficient as nested if statements.
```supercollider
(
var i, x, z;
z = [0, 1, 1.1, 1.3, 1.5, 2];
i = z.choose;
x = case
    { i == 1 }   { \no }
    { i == 1.1 } { \wrong }
    { i == 1.3 } { \wrong }
    { i == 1.5 } { \wrong }
    { i == 2 }   { \wrong }
    { i == 0 }   { \true };
x.postln;
)
```


### `matchItem`
Interface shared with other classes that implements pattern matching. See also: matchItem. Function.matchItem evaluates the function with the item as argument, expecting a Boolean as reply.See also [matchItem](../Reference/matchItem.md).
```supercollider
{ |x| x > 5 }.matchItem(6); // true
```


### `performDegreeToKey`
use a function as a conversion from scale degree to note number. See also SequenceableCollection and Scale
```supercollider
// a strange mapping
(
var f = { |degree, stepsPerOctave, acc|
    (1.8 ** (degree % stepsPerOctave) + acc).postln
};
Pbind(
    \scale, f,
    \degree, Pseq([0, 1, 2b, 3s, 4s, 6, 14, [0, 2, 4], [1, 3, 6]], inf)
).play
)
```



### Exception Handling
For the following two methods a return ^ inside of the receiver itself cannot be caught. Returns in methods called by the receiver are OK.

See also [#Exception Handling Examples](#exception-handling-examples) and [Exception](../Classes/Exception.md) for more information on how to handle exceptions.

### `try`
Executes the receiver. If an exception is thrown the catch function handler is executed with the error as an argument. handler itself can rethrow the error if desired.
### `protect`
Executes the receiver. The cleanup function handler is executed with an error as an argument, or nil if there was no error. The error continues to be in effect.

### Scheduling
### `awake`
This method is called by a [Clock](../Classes/Clock.md) on which the function was scheduled when its scheduling time is up. It calls [value](#value), passing on the scheduling time in beats as an argument.**Arguments:**

| Argument | Description |
|----------|-------------|
| `beats` | The scheduling time in beats. This is equal to the current logical time ([Thread#-beats](../Classes/Thread.md#-beats)). |  
| `seconds` | The scheduling time in seconds. This is equal to the current logical time ([Thread#-seconds](../Classes/Thread.md#-seconds)). |  
| `clock` | The clock on which the object was scheduled. |  
**Returns:** The value returned by the function's [value](#value). A caller clock uses this value to reschedule the function.
```supercollider
// Runs every 2 seconds
AppClock.play({ "And again".postln; 2 });
```



### Audio
### `play`
Play a Synth from UGens returned by the function. The function arguments become controls that can be set afterwards.This works as follows: play wraps the UGens in a SynthDef and sends it to the target. When this asynchronous command is completed, it creates one synth from this definition.**Arguments:**

| Argument | Description |
|----------|-------------|
| `target` | A Node, Server, or Nil. A Server will be converted to the default group of that server. Nil will be converted to the default group of the default Server. |  
| `outbus` | A bus number that determines the output channel. This is equivalent to `Out.ar(outbus, signal)`. The default is 0. |  
| `fadeTime` | Crossfade time for attack and release of the synth. The default is 0.02 seconds, which is just enough to avoid a click. |  
| `addAction` | The add action for the synth. For a list of valid addActions see [Synth](../Classes/Synth.md) |  
| `args` | An array of key value pairs of control names and control values which are used when starting the synth.
> **Note:** Some UGens are added in this process.- an [Out](../Classes/Out.md) UGen for playing the audio to the first audio busses. If the function returns an Out UGen, this is omitted.
- an envelope with a `\gate` control for releasing and crossfading. If the function provides its own releasable envelope, this is omitted.


```supercollider
x = { |freq = 440| SinOsc.ar(freq, 0, 0.3) }.play; // this returns a Synth object;
x.set(\freq, 880); // note you can set the freq argument
x.defName; // the name of the resulting SynthDef
x.release(4); // fadeout over 4 seconds
```

Many of the examples make use of the Function.play syntax. Note that reusing such code in a SynthDef requires the addition of an Out ugen.
```supercollider
// the following two lines produce equivalent results
{ SinOsc.ar(440, 0, 0.3) }.play(fadeTime: 0.0);
SynthDef(\help_FuncPlay, { Out.ar(0, SinOsc.ar(440, 0, 0.3)) }).play;
```

Function.play is often more convenient than SynthDef.play, particularly for short examples and quick testing. The latter does have some additional options, such as lagtimes for controls, etc. Where reuse and maximum flexibility are of greater importance, SynthDef and its various methods are usually the better choice. |  

### `scope`
As play above, and calls Server-scope to open a scope window in which to view the output.
```supercollider
{ FSinOsc.ar(440, 0, 0.3) }.scope(1)
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `numChannels` | The number of channels to display in the scope window, starting from outbus. It automatically reflects the number of channels. |  
| `outbus` | The output bus to play the audio out on. This is equivalent to Out.ar(outbus, theoutput). The default is 0. |  
| `fadeTime` | A fadein time. The default is 0.05 seconds, which is just enough to avoid a click. |  
| `bufsize` | The size of the buffer for the ScopeView. The default is 4096. |  
| `zoom` | A zoom value for the scope's X axis. Larger values show more. The default is 1. |  
| `bounds` | The bounds of the `Window` in which the scope is embedded. A Rect specifying position and size of the window. The size does not include the border and title bar. Position is measured from the bottom-left corner of the screen (this is different than [View#-bounds](../Classes/View.md#-bounds)). The default is nil and the scope window will be in the centre of the display. |  

### `plot`

> **Note:** See [plot](../Reference/plot.md) for a general reference on plotting

Calculates duration in seconds worth of the output of this function asynchronously, and plots it in a GUI window. Unlike play and scope it will not work with explicit Out UGens, so your function should return a UGen or an Array of them. The plot will be calculated in realtime.
```supercollider
{ SinOsc.ar(440) }.plot(0.01, bounds: Window.screenBounds);

{ { |i| SinOsc.ar(1 + i) }.dup(7) }.plot(1);
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `duration` | The duration of the function to plot in seconds. The default is 0.01. |  
| `target` | The server, synth or group where the signal is picked up. See [asTarget](../Reference/asTarget.md).
```supercollider
(
var synth = { Out.ar(99, SinOsc.ar([300, 700])) }.play;
{ In.ar(99, 2) }.plot(0.02, synth);
)
``` |  
| `bounds` | An instance of Rect or Point indicating the bounds of the plot window. |  
| `minval` | the minimum value in the plot. If not specified, the signal's minimum is used. |  
| `maxval` | the maximum value in the plot. If not specified, the signal's maximum is used. |  
| `separately` | If set to `true`, for multichannel signals use separate value display ranges, unless minval or maxval is specified already. |  
| `parent` | Either a [Window](../Classes/Window.md) or [View](../Classes/View.md) may be passed in - then the plot is embedded. Otherwise a new [Window](../Classes/Window.md) is created.
```supercollider
(
var w = Window("The parent of a plotter").front;
{ SinOsc.ar }.plot(0.01, parent: w)
)
``` |  

### `asBuffer`
Calculates duration in seconds worth of the output of this function asynchronously, and returns it in a [Buffer](../Classes/Buffer.md) of the number of channels. This method immediately returns a buffer, which takes `duration` seconds to become filled with data asynchronously. Then the action function is called.**Arguments:**

| Argument | Description |
|----------|-------------|
| `duration` | The duration of the function to plot in seconds. The default is 0.01. |  
| `target` | The synth or group after which the synth runs (see [asTarget](../Reference/asTarget.md)). The default is the default group of `Server.default`. |  
| `action` | A function that is called when the buffer is filled. It is passed the buffer as argument. |  
| `fadeTime` | A fade in and out time in seconds. Only when greater than zero, an envelope is applied to the signal to avoid clicks (default: 0). |  

```supercollider
// record a buffer
b = { Blip.ar(XLine.kr(10000, 4, 3) * [1, 1.2], 20) * 0.1 }.asBuffer(3, fadeTime: 0.1)
b.plot; // after 3 seconds, you can see it.
// play the soundfile back
{ PlayBuf.ar(b.numChannels, b, LFNoise2.kr(2 ! 8).exprange(0.15, 1), loop: 1).sum }.play;
```


### `loadToFloatArray`
Write a UGen function to a file and then load it into a FloatArray.**Arguments:**

| Argument | Description |
|----------|-------------|
| `duration` | Amount of data to record in seconds |  
| `target` | A server, synth, or group where to place the synth that plays the function |  
| `action` | A function to call when writing is finished.
```supercollider
// get some data from the synth audio
{ SinOsc.ar + GrayNoise.ar(0.1) }.loadToFloatArray(0.01, action: { |array| a = array });
a.postln;
a.plot;

// place it after some other node:
z = { WhiteNoise.ar * 0.1 }.play; // play some noise
{ BPF.ar(In.ar(0), 7000, 0.01) * 10 }.loadToFloatArray(0.01, z, action: { |array| a = array });
a.postln;
``` |  

### `getToFloatArray`
Stream the function audio values to the client using a series of getn messages and put the results into a FloatArray.**Arguments:**

| Argument | Description |
|----------|-------------|
| `duration` | Amount of data to record in seconds |  
| `target` | A server, synth, or group where to place the synth that plays the function |  
| `action` | A function to call when writing is finished. |  
| `wait` | The amount of time in seconds to wait between sending getn messages. Longer times are safer. The default is 0.01 seconds which seems reliable under normal circumstances. A setting of 0 is not recommended. |  
| `timeout` | The amount of time in seconds after which to post a warning if all replies have not yet been received. the default is 3. |  
For a discussion of the difference between getToFloatArray and loadToFloatArray, see [Buffer#-getToFloatArray](../Classes/Buffer.md#-gettofloatarray) and [Buffer#-loadToFloatArray](../Classes/Buffer.md#-loadtofloatarray).
```supercollider
// get some data from the synth audio

{ SinOsc.ar + GrayNoise.ar(0.1) }.getToFloatArray(0.01, action: { |array| a = array });
a.postln;
a.plot;
```



### Conversion
### `asSynthDef`
Returns a SynthDef based on this Function, adding a Linen and an Out ugen if needed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `rates` | An Array of rates and lagtimes for the function's arguments (see SynthDef for more details). |  
| `prependArgs` | arguments |  
| `outClass` | The class of the output ugen as a symbol. The default is \Out. |  
| `fadeTime` | a fadein time. The default is 0. |  
| `name` | the name of the SynthDef |  

### `asDefName`
Performs asSynthDef (see above), sends the resulting def to the local server and returns the SynthDefs name. This is asynchronous.
```supercollider
x = { SinOsc.ar(440, 0, 0.3) }.asDefName; // this must complete first
y = Synth(x);
```


### `asRoutine`
Returns a Routine using this as its func argument.
### `r`
Returns a Routine using this as its func argument.
```supercollider
a = r { 5.do { |i| i.rand.yield } };
a.nextN(8);
```


### `p`
Returns a Prout using this as its func argument.
```supercollider
a = p { 5.do { |i| i.rand.yield } };
x = a.asStream;
x.nextN(8);
```

This is useful for using ListComprehensions in Patterns:
```supercollider
Pbind(\degree, p { :[x, y].postln, x<-(0..10), y<-(0..10), (x + y).isPrime }, \dur, 0.3).play;
```



### Bela
### `belaScope`
Like [Function#-scope](../Classes/Function.md#-scope), plays and scopes this Function, but using Bela's Oscilloscope (see [BelaScope](../Classes/BelaScope.md) for required setup). This Function's output bus is monitored right after the generated Synth.**Arguments:**

| Argument | Description |
|----------|-------------|
| `scopeChannel` | Bela's oscilloscope channel to start scoping on. This has to be a non-negative number, and can't be changed after scoping starts. |  
| `target` | A Node, Server, or Nil. A Server will be converted to the default group of that server. Nil will be converted to the default group of the default Server.
> **Note:** this Function's play target needs to be on a Server that supports BelaScope |  
| `numChannels` | Number of channels to scope, from this Function's output channels. Defaults to this Function's output channels. |  
| `outbus` |  |  
| `fadeTime` |  |  
| `addAction` |  |  
| `args` | See [Function#-scope](../Classes/Function.md#-scope) |  
**Returns:** Like [Function#-play](../Classes/Function.md#-play), a Synth playing this function. When that synth is freed, so will be its monitor.

## Examples


### Exception Handling Examples

```supercollider
// no exception handler
value { 8.zorg; \didnt_continue.postln }

try { 8.zorg } { |error| error.postln; \cleanup.postln }; \continued.postln;

protect { 8.zorg } { |error| error.postln }; \didnt_continue.postln;
```



```supercollider
try { 123.postln; 456.throw; 789.postln } { |error| [\catch, error].postln };

try { 123.postln; 789.postln } { |error| [\catch, error].postln };

try { 123.postln; nil.throw; 789.postln } { |error| [\catch, error].postln };

protect { 123.postln; 456.throw; 789.postln } { |error| [\onExit, error].postln };

protect { 123.postln; 789.postln } { |error| [\onExit, error].postln };

(
try {
    protect { 123.postln; 456.throw; 789.postln } { |error| [\onExit, error].postln };
} { |error| [\catch, error].postln };
)

value { 123.postln; 456.throw; 789.postln }

value { 123.postln; Error("what happened?").throw; 789.postln }
```



```supercollider
(
a = [\aaa, \bbb, \ccc, \ddd];
a[1].postln;
a[\x].postln;
a[2].postln;
)

(
try {
    a = [\aaa, \bbb, \ccc, \ddd];
    a[1].postln;
    a[\x].postln;
    a[2].postln;
} { |error| \caught.postln; error.dump }
)

(
try {
    a = [\aaa, \bbb, \ccc, \ddd];
    a[1].postln;
    a[\x].postln;
    a[2].postln;
} { |error| \caught.postln; error.dump; error.throw }
)

(
protect {
    a = [\aaa, \bbb, \ccc, \ddd];
    a[1].postln;
    a[\x].postln;
    a[2].postln;
} { |error| \caught.postln; error.dump }
)
```






