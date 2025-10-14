# Punop

*unary operator pattern*

**Related:** [Pbinop](../Classes/Pbinop.md), [Pnaryop](../Classes/Pnaryop.md), [UnaryOpFunction](../Classes/UnaryOpFunction.md), [Overviews/Operators](../Overviews/Operators.md)

**Categories:** Streams-Patterns-Events>Patterns>Math

## Description

Returns a stream that applies the unary operator to the stream values of the receiver. Usually, this is the result of applying a unary operator (i.e. a method with one argument) to a pattern.
Examples of unary operators are: squared, sqrt, sin, tan ...


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `operator` | operator to be applied |  
| `a` | a pattern (or compatible pattern input) |  

## Examples


```supercollider
(
var a;
a = Punop(\sqrt, Pseries(0, 1, 12));
a.asStream.all;
)

// this is the same as:
(
var a;
a = Pseries(0, 1, 12).sqrt;
a.asStream.all;
)

// some common cases:
Pseq([1, 2, 3]).squared;
Pseq([0.2, 0.5, 0.8]).coin;
Pwhite(-100, 100, inf).abs;



// sound example
(
SynthDef(\help_sinegrain,
    { |out = 0, freq = 440, sustain = 0.05, amp = 0.1|
        var env;
        env = EnvGen.kr(Env.perc(0.01, sustain, 0.2, amp), doneAction: Done.freeSelf);
        Out.ar(out, SinOsc.ar(freq, 0, env))
    }).add;
)

(
var a;
a = Pn(Punop(\sqrt, Pseries(0, 1, 12))).asStream;
{
    a.do { |val|
        Synth(\help_sinegrain, [\freq, a * 200 + 300].postln);
        0.5.wait;
    }
}.fork;
)

(
Pbind(
    \dur, 0.01,
    \instrument, \help_sinegrain,
    \note, Pn(Punop(\sqrt, Pseries(0, 1, 12)))
).play;
)


// these are the same as:

(
var a;
a = Pn(Pseries(0, 1, 12).sqrt).asStream;
{
    a.do { |val|
        Synth(\help_sinegrain, [\freq, a * 200 + 300].postln);
        0.05.wait;
    }
}.fork;
)

(
Pbind(
    \dur, 0.1,
    \instrument, \help_sinegrain,
    \note, Pn(Pseries(0, 1, 12).sqrt)
).play;
)
```




