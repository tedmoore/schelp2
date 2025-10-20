# Pconst

*constrain the sum of a value pattern*

**Related:** [Pfindur](../Classes/Pfindur.md), [Pfin](../Classes/Pfin.md), [Pfinval](../Classes/Pfinval.md)

**Categories:** Streams-Patterns-Events>Patterns>Repetition

## Description

Similar to [Pfindur](../Classes/Pfindur.md), but works with the value directly.

> **Note:** Be careful if this is used, directly or indirectly, for a note-length parameter! The difference may be very small and this could result in zombie nodes, due to a bug in [EnvGen](../Classes/EnvGen.md) for very short sustain times.




## Class Methods


### `new`
Embeds elements of the **pattern** into the stream until the sum comes close enough to **sum**. At that point, the difference between the specified sum and the actual running sum is embedded.
## Examples


```
(
var a, x;
a = Pconst(5, Prand([1, 2, 0.5, 0.1], inf));
x = a.asStream;
9.do({ x.next(Event.default).postln });
)


// Pconst used as a sequence of durations

(
SynthDef(\help_sinegrain,
    { |out = 0, freq = 440, sustain = 0.05|
        var env;
        env = EnvGen.kr(Env.perc(0.01, sustain, 0.2), doneAction: Done.freeSelf);
        Out.ar(out, SinOsc.ar(freq, 0, env))
    }).add;
)

(
Pn(
    Pbind(
        \dur, Pconst(1, Prand([1, 0.02, 0.2], inf)),
        \instrument, \help_sinegrain,
        \degree, Pseries(0, 1, inf),
        \octave, 6
    )
).play;
)
```




