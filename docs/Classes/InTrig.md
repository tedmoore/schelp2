# InTrig

*Generate a trigger anytime a bus is set.*

**Categories:** UGens>InOut, UGens>Triggers

## Description

Any time the bus is "touched", ie. has its value set (using "/c_set" etc.), a single impulse trigger will be generated. Its amplitude is the value that the bus was set to.
If the bus is set [synchronously](../Classes/Bus.md#synchronous-control-bus-methods) no trigger will be generated.


## Class Methods


### `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bus` | The index of the bus to read in from. |  
| `numChannels` | The number of channels (i.e. adjacent buses) to read in. You cannot modulate this number by assigning it to an argument in a SynthDef. |  

## Examples


```
s = Server.local;
b = Bus.control(s, 1);

SynthDef("help-InTrig", { |out = 0, busnum = 0|
    var inTrig;
    inTrig = InTrig.kr(busnum);
    Out.ar(out,
        EnvGen.kr(Env.perc, gate: inTrig, levelScale: inTrig) * SinOsc.ar
    )
}).play(s, [\out, 0, \busnum, b.index]);


b.set(1.0);

b.value = 1.0;

b.value = 0.2;

b.value = 0.1;
```


compare with [In](../Classes/In.md) example.

