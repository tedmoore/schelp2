# NumRunningSynths

*Number of currently running synths.*

**Related:** [NumAudioBuses](../Classes/NumAudioBuses.md), [NumControlBuses](../Classes/NumControlBuses.md), [NumBuffers](../Classes/NumBuffers.md), [NumInputBuses](../Classes/NumInputBuses.md), [NumOutputBuses](../Classes/NumOutputBuses.md)

**Categories:** UGens>Info

## Description

Number of currently running synths.


## Class Methods

### `ir`

## Examples


```supercollider
// example: frequency is derived from the number of synths running
(
SynthDef("numRunning", { |out|
    Out.ar(out, SinOsc.ar(NumRunningSynths.ir * 200 + 400, 0, 0.1));
}).add;
)

s.sendMsg("/s_new", "numRunning", -1, 0, 0);
s.sendMsg("/s_new", "numRunning", -1, 0, 0);
s.sendMsg("/s_new", "numRunning", -1, 0, 0);
s.sendMsg("/s_new", "numRunning", -1, 0, 0);
```




