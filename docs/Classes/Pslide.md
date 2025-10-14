# Pslide

*slide over a list of values and embed them*

**Related:** [Ptuple](../Classes/Ptuple.md)

**Categories:** Streams-Patterns-Events>Patterns>List


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `list` |  |  
| `repeats` | number of segments. |  
| `len` | length of each segment. |  
| `step` | how far to step the start of each segment from previous. step can be negative. |  
| `start` | what index to start at. |  
| `wrapAtEnd` | if true (default), indexing wraps around if goes past beginning or end. If false, the pattern stops if it hits a nil element or goes outside the list bounds. |  

## Examples


```supercollider
(
var a, b;
a = Pslide([1, 2, 3, 4, 5], inf, 3, 1, 0);
x = a.asStream;
13.do({ x.next.postln });
)

// Pslide used as a sequence of pitches:

(
SynthDef(\help_sinegrain,
    { |out = 0, freq = 440, sustain = 0.05|
        var env;
        env = EnvGen.kr(Env.perc(0.01, sustain, 0.2), doneAction: Done.freeSelf);
        Out.ar(out, SinOsc.ar(freq, 0, env))
    }).add;
)

(
c = Pslide(#[1, 2, 3, 4, 5], inf, 3, 1, 0) * 3 + 67;
x = c.asStream;
Routine({
    loop({
        Synth(\help_sinegrain, [\freq, x.next.midicps]);
        0.17.wait;
    })
}).play;
)
```




