# ProxySynthDef

*synth def that wraps ugen graph*

**Categories:** JITLib>NodeProxy

**Related:** [NodeProxy](../Classes/NodeProxy.md)

## Description

(used internally by [NodeProxy](../Classes/NodeProxy.md))
for inner workings see [JITLib/jitlib_fading](../Tutorials/JITLib/jitlib_fading.md)


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` | like in [SynthDef](../Classes/SynthDef.md). todo: add variants. |  
| `func` | like in [SynthDef](../Classes/SynthDef.md). todo: add variants. |  
| `rates` | like in [SynthDef](../Classes/SynthDef.md). todo: add variants. |  
| `prependArgs` | like in [SynthDef](../Classes/SynthDef.md). todo: add variants. |  
| `makeFadeEnv` | if true it constructs a fader envelope and adds controls for gate and fadeTime |  
| `channelOffset` | a constant offset that is added to the out number |  
| `chanConstraint` | max numChannels for the synthdef. If ugenfunc returns a larger array, it wraps |  
| `rateConstraint` | a symbol like \audio, \control or \scalar. |  

### `sampleAccurate`
always use [OffsetOut](../Classes/OffsetOut.md), if set to true (default: false)
## Examples


```supercollider
a = ProxySynthDef("xtest", { SinOsc.ar(400) * 0.1 });

a.add;

x = Synth("xtest");
x.release;


/*

    if the resulting number of channels is larger than a given channelConstraint,
    it behaves according to the rate: audio rate signals are wrapped around
    a smaller channel size, control rate signals are not (the exceeding channels are left out)

*/
```




