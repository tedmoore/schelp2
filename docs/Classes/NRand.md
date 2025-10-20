# NRand

*Sum of uniform distributions.*

**Related:** [ExpRand](../Classes/ExpRand.md), [IRand](../Classes/IRand.md), [LinRand](../Classes/LinRand.md), [Rand](../Classes/Rand.md), [TExpRand](../Classes/TExpRand.md), [TIRand](../Classes/TIRand.md), [TRand](../Classes/TRand.md)

**Categories:** UGens>Random

## Description

Generates a single random float value in a sum of `n` uniform distributions from `lo` to `hi` .


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `lo` | Lower limit of the output range. |  
| `hi` | Upper limit of the output range. |  
| `n` | | n = 1: | Uniform distribution - same as [Rand](../Classes/Rand.md). | 
| --- | --- || n = 2: | Triangular distribution. | | n = 3: | Smooth hump. | As `n` increases, distribution converges towards gaussian. |  

## Examples


```
(
SynthDef("help-NRand", { |out = 0, n = 0|
    Out.ar(out,
        FSinOsc.ar(
            NRand(1200.0, 4000.0, n),
            0, Line.kr(0.2, 0, 0.01, doneAction: Done.freeSelf))
    )
}).add;
)

(
n = 0;
Routine({
    inf.do({ |i|
        Synth.new("help-NRand", [\n, n]); 0.05.wait;
    })
}).play;
)

n = 1;
n = 2;
n = 4;
```




