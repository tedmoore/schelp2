# SharedOut

*Write to a shared control bus.*

**Related:** [SharedIn](../Classes/SharedIn.md)

**Categories:** UGens>InOut

## Description

> **⚠️ Warning:** SharedIn has been deprecated. Synchronous access to busses on local servers is possible via [Bus#-getSynchronous](../Classes/Bus.md#-getsynchronous) and [Bus#-setSynchronous](../Classes/Bus.md#-setsynchronous)
Reads from a control bus shared between the internal server and the SC client. Control rate only. Reading from a shared control bus on the client is synchronous. When not using the internal server use the get method of Bus (or /c_get in messaging style) or [SendTrig](../Classes/SendTrig.md) with an [OSCFunc](../Classes/OSCFunc.md).


## Class Methods

### `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bus` | The index of the shared control bus to write to. |  
| `channelsArray` | An Array of channels or single output to write out. You cannot change the size of this once a SynthDef has been built. |  

## Examples


```supercollider
(
// only works with the internal server
s = Server.internal;
s.boot;
)

(
SynthDef("help-SharedOut", {
    SharedOut.kr(0, SinOsc.kr(0.2));
}).add;
)

(
s.sendMsg(\s_new, "help-SharedOut", x = s.nextNodeID, 0, 1);
s.sendMsg(\n_trace, x);

// poll the shared control bus
Routine({
    30.do({
        s.getSharedControl(0).postln;
        0.2.wait;
    });
}).play;
)


s.quit;
```




