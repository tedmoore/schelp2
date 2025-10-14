# Pfset

*Insert an environment into the event prototype before evaluating the supplied pattern*

**Related:** [Pset](../Classes/Pset.md)

**Categories:** Streams-Patterns-Events>Patterns>Data Sharing

## Description

Good for setting default values or loading server objects.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | Use environment variable syntax (e.g., `~x = 0`) to store values in the internal environment. These values are copied into the event prototype before running the supplied pattern. |  
| `pattern` | An event pattern (such as [Pbind](../Classes/Pbind.md)). |  
| `cleanupFunc` | Optional. A function to evaluate when the pattern is stopped, or when the supplied pattern runs out of values. For example, if you loaded a [Buffer](../Classes/Buffer.md) in the initializer function, you could free it in the `cleanupFunc`. |  

## Examples


```supercollider
(
var a, b;
a = Pfset({
    ~legato = 0.3;
    ~detune = rrand(0, 30);
}, Pbind(\dur, 0.5));
x = a.asStream;
9.do({ x.next(Event.new).postln });
)
```


Pfset does not override values placed into the event by the inner pattern:

```supercollider
(
var a, b;
a = Pfset({
    ~dur = 0.3;
}, Pbind(\dur, 0.5));
x = a.asStream;
9.do({ x.next(Event.new).postln });
)
```


Sound example

```supercollider
(
SynthDef(\sinegrain,
    { |out = 0, freq = 440, sustain = 0.02|
        var env;
        env = EnvGen.kr(Env.perc(0.001, sustain), 1, doneAction: Done.freeSelf);
        Out.ar(out, SinOsc.ar(freq, 0, env * 0.1))
    }).add;
)

(
a = Pbind(\dur, 0.5, \instrument, \sinegrain, \x, Pfunc { rrand(500, 600) });
a = Pfset({ ~freq = { ~x.postln * 2 }; ~legato = 3 }, a);
a.play;
)
```




