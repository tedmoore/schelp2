# Pdict

*pattern that embeds patterns from a dictionary*

**Categories:** JITLib>Patterns, Live Coding

**Related:** [Pbind](../Classes/Pbind.md)

## Description

A general purpose lookup stream.

## Examples


```supercollider
SynthDescLib.read;

(
e = (
    a: Pbind(\dur, 0.1, \degree, Pseq([0, 5, 4, 3, 2])),
    b: Pbind(\dur, 0.06, \degree, Pseq([7, 8, 7, 8])),
    c: Pbind(\dur, 0.3, \degree, Pseq([0, 1, 2], 2))
);

x = Pdict(e, Pseq([
            \a, \b,
            Prand([\a, \c])
        ], 4)
    );
x.play;
)
```




