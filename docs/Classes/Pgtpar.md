# Pgtpar

*embed event streams in parallel and put each in its own group, with time offset*

**Related:** [Pgpar](../Classes/Pgpar.md), [Ptpar](../Classes/Ptpar.md), [Pbus](../Classes/Pbus.md), [Pgroup](../Classes/Pgroup.md)

**Categories:** Streams-Patterns-Events>Patterns>Parallel

## Description

Similar to [Pgpar](../Classes/Pgpar.md) but with additional timing offsets.


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `list` | list of pairs of times and patterns or streams: [time, pat, time, pat ..].
> **Note:** times are in beats and depend on the tempo of the [TempoClock](../Classes/TempoClock.md) in use. |  
| `repeats` | repeat the whole pattern n times. |  

## Examples


```
// synthdef
(
SynthDef(\help_sinegrain,
    { |out = 0, freq = 440, sustain = 0.05|
        var env;
        env = EnvGen.kr(Env.perc(0.01, sustain, 0.2), doneAction: Done.freeSelf);
        Out.ar(out, SinOsc.ar(freq, 0, env))
}).add;
)

// pattern with different start times
(
x = Pbind(
    \instrument, \help_sinegrain,
    \degree, Pseq(#[0, 5, 4, 2, 1, 1, 3], inf),
    \dur, Pseq(#[0.25, 0.5, 1.0], inf),
    \scale, #[0, 3, 5, 9, 10]
);
a = Pbus(Pgtpar([0.0, x, 1.5, x, 2.25, x])).play;
)
s.plotTree;
a.stop;
```




