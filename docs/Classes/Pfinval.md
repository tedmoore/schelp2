# Pfinval

*limit number of items embedded in a stream*

**Related:** [Pfindur](../Classes/Pfindur.md), [Pfin](../Classes/Pfin.md), [Pconst](../Classes/Pconst.md)

**Categories:** Streams-Patterns-Events>Patterns>Repetition

## Description


> **Note:** Pfinval is not appropriate for wrapping [Pmono](../Classes/Pmono.md), [Pfx](../Classes/Pfx.md) etc. For these types of event patterns, you should use [Pfin](../Classes/Pfin.md).




## Class Methods

### `new`
Embeds **count** elements of the **pattern** into the stream.
## Examples


```supercollider
(
var a, b;
a = Pfinval(5, Pseq(#[1, 2, 3], inf));
b = a.asStream;
9.do({ b.next.postln });
)


// Pfinval used as a sequence of pitches

(
SynthDef(\help_sinegrain,
    { |out = 0, freq = 440, sustain = 0.05|
        var env;
        env = EnvGen.kr(Env.perc(0.01, sustain, 0.2), doneAction: Done.freeSelf);
        Out.ar(out, SinOsc.ar(freq, 0, env))
    }).add;
)

(
var c, b;
c = Pn(Pfinval({ rrand(3, 5) }, Pseq([1, 2, 3, 4, 5, 6], inf)*4+65), inf);
b = c.asStream;
Routine({
    loop({
        Synth(\help_sinegrain, [\freq, b.next.midicps]);
        0.12.wait;
    })
}).play;
)
```




