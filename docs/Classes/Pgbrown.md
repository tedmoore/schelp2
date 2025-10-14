# Pgbrown

*geometric brownian motion pattern*

**Related:** [BrownNoise](../Classes/BrownNoise.md), [Pbrown](../Classes/Pbrown.md)

**Categories:** Streams-Patterns-Events>Patterns>Random

## Description

Returns a stream that behaves like a geometric brownian motion.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `lo` | lower boundary of values. |  
| `hi` | upper boundary of values. |  
| `step` | maximum multiplication factor per step (omega) - the distribution is xrand2. |  
| `length` | number of values produced. |  

## Examples


```supercollider
(
var a, b;
a = Pgbrown(0.0, 1.0, 0.2, inf);
b = a.asStream;
7.do({ b.next.postln });
)


// sound example
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
a = Pgbrown(1.0, 2.0, 0.1, inf).asStream;
Routine({
    loop({
    Synth(\help_sinegrain, [\freq, a.next * 600 + 300]);
    0.02.wait;
    })
}).play;
)

// compare with normal brownian motion:

(
var a;
a = Pbrown(1.0, 2.0, 0.1, inf).asStream;
Routine({
    loop({
        Synth(\help_sinegrain, [\freq, a.next * 600 + 300]);
        0.02.wait;
    })
}).play;
)
```




