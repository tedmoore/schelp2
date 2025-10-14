# Pfunc

*Function pattern*

**Categories:** Streams-Patterns-Events>Patterns>Function

**Related:** [Pfuncn](../Classes/Pfuncn.md), [FuncStream](../Classes/FuncStream.md)

## Description

Returns a [Stream](../Classes/Stream.md) that returns values from the `nextFunc`. To return a pattern, see [Plazy](../Classes/Plazy.md).


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `nextFunc` | Stream function. In an event stream `nextFunc` receives the current [Event](../Classes/Event.md) as argument, and more generally the argument passed to the stream's `next` call. |  
| `resetFunc` | Function that is called when the stream is reset. `resetFunc` receives no arguments. |  

## Examples

Numeric stream examples

```supercollider
(
var a, x;
a = Pfunc({ exprand(0.1, 2.0) + #[1, 2, 3, 6].choose }, { \reset.postln });
x = a.asStream;
x.nextN(20).postln;
x.reset;
)

// with argument passed to nextFunc
(
x = Pfunc({ |inval| (10 ** inval.value) * rrand(1, 9) }).asStream;
[2, 3, 2].do { |i| x.next(i).postln };
x.nextN(5, (:0..)).postln;
)
```


Event stream (sound) examples:

```supercollider
(
SynthDef(\help_sinegrain,
    { |out = 0, freq = 440, sustain = 0.05|
        var env;
        env = EnvGen.kr(Env.perc(0.01, sustain, 0.2), doneAction: Done.freeSelf);
        Out.ar(out, SinOsc.ar(freq, 0, env))
    }).add;
)

(
var a;
a = Pfunc({ exprand(0.1, 0.3) + #[1, 2, 3, 6, 7].choose }).asStream;
{
    a.do { |val|
        Synth(\help_sinegrain, [\freq, val * 100 + 300]);
        0.02.wait;
    }
}.fork;
)
```


When an Event is played, if `\freq` is set then `\degree` is ignored (due to the `Event.default` machinery). In a chain of Patterns, a `Pfunc` can be used to delete a key from the Event stream; this can even be done inside a Pbind.

```supercollider
q = Pbind(\freq, 300, \dur, Pn(0.3, 2));
q.trace.play;

// Sound-wise ineffective modification of the incoming stream
p = Pbind(\degree, 6) <> q;
p.trace.play;

// Instead
p = Pbind(\degree, 6) <> Pfunc { |ev| ev.freq = nil } <> q;
p.trace.play;

// Alternatively
p = Pbind(\degree, Pfunc { |ev| ev.freq = nil; 6 }) <> q;
p.trace.play;

// Just setting a key to nil from a Pbind pair will end the stream
p = Pbind(\freq, nil, \degree, 6) <> q;
p.trace.play; // silent because it outputs no events
```




