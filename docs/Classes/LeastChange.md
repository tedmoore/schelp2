# LeastChange

*Output least changed*

**Related:** [MostChange](../Classes/MostChange.md), [LastValue](../Classes/LastValue.md)

**Categories:** UGens>Maths

## Description

Given two inputs `a` and `b`, let `da[t] = abs(a[t] - a[t - 1])` and `db[t] = abs(b[t] - b[t - 1])`. Output `a[t]` if `da[t]` is smaller, and output `b[t]` if `db[t]` is smaller. If `da[t] == db[t]`, use whichever input was used last (assume `a` for the first sample of output).


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `a` | Input signal A. |  
| `b` | Input signal B. |  

## Examples


```supercollider
(
d = { |amp = 1.0|
    var in1, in2;
    in1 = LFNoise0.ar(800, amp);
    in2 = SinOsc.ar(800);
    LeastChange.ar(in1, in2) * 0.1;
}.play;
)

d.set(\amp, 0.1);
d.set(\amp, 0);
d.set(\amp, 3);
d.free;
```


the control that changed least is used as output:

```supercollider
(
d = { |freq = 440|
    var internalFreq;
    internalFreq = LFNoise0.ar(0.3, 300, 800);
    SinOsc.ar(
        LeastChange.kr(freq, internalFreq) // two sources of change: one external, one internal
    ) * 0.1
}.play
);

d.set(\freq, 800);
d.set(\freq, 900);
d.free;
```




