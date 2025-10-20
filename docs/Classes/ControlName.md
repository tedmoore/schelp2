# ControlName

*Object to store control information of SynthDef (used internally)*

**Related:** [SynthDesc](../Classes/SynthDesc.md), [SynthDef](../Classes/SynthDef.md)

**Categories:** UGens>Synth control

## Description

For an explicit creation of control names see: [NamedControl](../Classes/NamedControl.md), [Control](../Classes/Control.md)

## Examples


```
a = SynthDescLib.global; // the global library of SynthDescs
x = a.synthDescs.at(\default); // get the default SynthDesc
x.controls.do { |ctl| [\name, ctl.name, \defaultValue, ctl.defaultValue].postln }; "";
```



## Instance Methods


### `name`
The name of the control.**Returns:** a [Symbol](../Classes/Symbol.md)
### `index`
The index of the control.**Returns:** an [Integer](../Classes/Integer.md)
### `rate`
The rate of the control.**Returns:** a [Symbol](../Classes/Symbol.md) like `'audio'` or `'control'`
### `defaultValue`
Default value of this control. Will be an [Array](../Classes/Array.md) for multichannel controls.
### `numChannels`
The number of channels.**Returns:** an [Integer](../Classes/Integer.md)
### `spec`
The [ControlSpec](../Classes/ControlSpec.md) for this control. If set, it will be added to the specs metadata for the current SynthDef.at
```
(
d = SynthDef(\tone, { |out = 0, freq = 200|
    var sig;

    freq.spec = ControlSpec(20, 20000);
    sig = SinOsc.ar(freq);

    Out.ar(out, sig);
}).add;
)

d.specs.freq.postln;
```



