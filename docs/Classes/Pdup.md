# Pdup

*repeat input stream values*

**Related:** [Pn](../Classes/Pn.md), [Pattern#-dup](../Classes/Pattern#-dup.md)

**Categories:** Streams-Patterns-Events>Patterns>Repetition

## Description

repeat each element n times.

```supercollider
(
var a, b;
a = Pdup(2, Pwhite(-1.0, 1.0));
x = a.asStream;
8.do { x.next.postln };
)
```


This is also a response to [Pattern#-dup](../Classes/Pattern.md#-dup)


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `n` | The number of repeats for each new element. n may be a pattern, so the number of times can vary each iteration. |  
| `pattern` | the pattern to repeat. |  

## Examples


```supercollider
// the first argument can be a pattern, too:
(
var a, b;
a = Pdup(Prand([1, 2, 5], inf), Pwhite(-1.0, 1.0)); // repeat either once, twice, or five times
x = a.asStream;
20.do { x.next.postln };
)

// using event patterns:
(
SynthDef(\help_sinegrain,
    { |out = 0, freq = 440, sustain = 0.05|
        var env;
                env = Env.perc(0.01, sustain, 0.2).kr(doneAction: Done.freeSelf);
        Out.ar(out, SinOsc.ar(freq, 0.5pi, env))
}).add;
)

(
a = Pbind(
    \instrument, \help_sinegrain,
    \note, Pxrand([0, 5, 7, 9], inf),
    \dur, 0.05,
    \sustain, 0.1
);
Pdup(Pseq([1, 2, 3, 4], inf), a).trace.play;
)


// Pdup used as a sequence of pitches

(
c = Pdup(3, Pxrand([1, 2, 3], inf) * 4 + 65);
x = c.asStream;
Routine {
    loop {
        Synth(\help_sinegrain, [\freq, x.next.midicps]);
        0.12.wait;
    }
}.play;
)


// Voss algorithm for pink noise
// note that pattern.dupEach(n) is a synonym for Pdup(n, pattern)
a = Pwhite();
c = (2 ** (0..10)).sum { |n| a.dupEach(n) };
c.asStream.nextN(1000).plot


// Voss-McCartney algorithm: balance calculation for realtime use
a = Pwhite();
c = (2 ** (0..10)).sum { |n| a.dupEach(n.div(2).fin(1)) ++ a.dupEach(n) };
c.asStream.nextN(1000).plot
```




