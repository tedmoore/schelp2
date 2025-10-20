# Pexprand

*random values that follow a Exponential Distribution*

**Related:** [Pkey](../Classes/Pkey.md)

**Categories:** Streams-Patterns-Events>Patterns>Random


## Class Methods


### `new`

> **Note:** lo and hi should both be positive or negative (their range should not cross 0).

**Arguments:**

| Argument | Description |
|----------|-------------|
| `lo` | lower boundary of values. |  
| `hi` | upper boundary of values |  
| `length` | number of values produced. |  

## Examples


```
(
var a;
a = Pexprand.new(0.0001, 1, inf);
c = a.asStream.nextN(500);
// plot the values
c.plot(bounds: Rect(10, 10, 520, 380), discrete: true, parent: w);
// a histogram of the values
c.histo(500).plot(bounds: Rect(10, 410, 520, 380), parent: w);
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
a = Pexprand(0.0001, 1.0, inf).asStream;
{
    loop {
        Synth(\help_sinegrain, [\freq, a.next * 600 + 300]);
        0.02.wait;
    }
}.fork;
)
```




