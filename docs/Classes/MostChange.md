# MostChange

*Output most changed.*

**Related:** [LeastChange](../Classes/LeastChange.md), [LastValue](../Classes/LastValue.md)

**Categories:** UGens>Maths

## Description

Given two inputs `a` and `b`, let `da[t] = abs(a[t] - a[t - 1])` and `db[t] = abs(b[t] - b[t - 1])`. Output `a[t]` if `da[t]` is larger, and output `b[t]` if `db[t]` is larger. If `da[t] == db[t]`, use whichever input was used last (assume `a` for the first sample of output).


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `a` | Input signal A. |  
| `b` | Input signal B. |  

## Examples


```
(
d = SynthDef("help-MostChange", { |out, amp = 1.0|
    var sound, in1, in2;
    in1 = LFNoise1.ar(800, amp);
    in2 = SinOsc.ar(800);
    sound = MostChange.ar(in1, in2) * 0.1;
    Out.ar(out, sound)
}).play;
)

d.set(\amp, 0.1);
d.set(\amp, 0);
d.set(\amp, 3);
d.free;

// the control that changed most is used for output:

(
d = SynthDef("help-MostChange", { |out, freq = 440|
    var sound, internalFreq;
    internalFreq = LFNoise0.ar(0.3, 300, 800);
    sound = SinOsc.ar(
            MostChange.kr(freq, internalFreq)
    );
    Out.ar(out, sound * 0.1)
}).play;
)

d.set(\freq, 800);
d.set(\freq, 800); // nothing changed
d.set(\freq, 900);
d.free;
```




