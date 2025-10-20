# SynthDesc

*Description of a synth definition*

**Categories:** Server>Nodes

**Related:** [SynthDef](../Classes/SynthDef.md), [Synth](../Classes/Synth.md)

## Description

Contains a description of a [SynthDef](../Classes/SynthDef.md), including its name, control names and default values. Information is also stored on its outputs and inputs and whether it has a gate control.
SynthDescs are needed by the event stream system, so when using [Pbind](../Classes/Pbind.md), the instruments' default parameters are derived from the SynthDesc.

### Creation
SynthDescs are created by [SynthDescLib](../Classes/SynthDescLib.md), by reading a compiled synth def file.


```
SynthDescLib.global.read("synthdefs/default.scsyndef");
SynthDescLib.global.synthDescs.at(\default)
SynthDescLib.global.at(\default) // shortcut, same as line above
```


`aSynthDef.store` and `aSynthDef.add` also create a synthDesc in the global library.


**.store**
: saves a synthdef file on disk (like .load);

**.add**
: creates the synthDesc wholly in memory and sends the synthdef to registered servers.






```
(
SynthDef("test", { |out, freq, xFade|
    XOut.ar(out, xFade, SinOsc.ar(freq))
}).store
);
```


Browse the properties of SynthDescs:


```
SynthDescLib.global.browse;
```





## SynthDescs and SynthDef metadata
Metadata associated with a [SynthDef](../Classes/SynthDef.md) consists of an [Event](../Classes/Event.md) (a syntactically shorter form of an identity dictionary) containing information about the SynthDef that is useful to the client, and which cannot be inferred from the binary .scsyndef stream.

For example, by listing argument names and [ControlSpec](../Classes/ControlSpec.md)s under the 'specs' key in the event, the client can use the specs to build a [GUI](../Classes/GUI.md) allowing control over all the SynthDef's inputs, with sensible range mappings. (The "window" button in the SynthDescLib browser does exactly this -- any ControlSpecs listed in the metadata will be used for the corresponding synth input's slider.)

Currently only the 'specs' key is reserved. Other keys may be used as needed for specific applications. As the use of SynthDef metadata evolves, other keys may be standardized.


### Creation and access
Metadata are specified when creating a [SynthDef](../Classes/SynthDef.md). If the SynthDef is .store'd (or .add'd) into a SynthDescLib, the metadata become part of the SynthDesc as well. Thereafter, the metadata can be accessed through SynthDescLib:


```
SynthDescLib.global[\synthDefName].metadata
```





### Persistence and metadata plug-ins
Storing a SynthDef into the library with .store persists the SynthDef on disk. Metadata may also be persisted at the same time by using the appropriate metadata plug-in class. The plug-in is responsible for writing a separate metadata file into the synthdefs directory, and reading the file back at the same time that a SynthDesc is created for a .scsyndef file using SynthDesc.read or SynthDescLib.global.read.

The currently available plug-ins are:


**AbstractMDPlugin**
: A dummy plug-in, which writes no metadata, so that users who are not interested in metadata will not find extra files in the synthdefs directory.

**TextArchiveMDPlugin**
: Writes the metadata as a SuperCollider text archive -- metadata.writeArchive(path). This is the default. Metadata are written only if the SynthDef contains metadata.



Other plug-ins may be written at a later date, to support sharing metadata with applications in other languages using formats like JSON (JavaScript Object Notation) or XML.

You may specify a global default metadata plug-in as follows:


```
SynthDesc.mdPlugin = ... plug-in class name ...;
```


Metadata are not written when using `SynthDef().load(server)`. This is because SynthDesc exists to describe a SynthDef to the client, whereas SynthDef is really just an abstraction to create a [UGen](../Classes/UGen.md) graph for the server. Metadata are also not written for `SynthDef().add`, because in the normal case, nothing is persisted to disk. (If the SynthDef is very large and a disk file is required, then the metadata will persist along with the .scsyndef file.)




### Automatic population
You may write a function to populate entries into the metadata automatically, based on the SynthDesc object. This function executes when reading a SynthDesc from disk, when using .add, and before writing a metadata file (in .store).


```
SynthDesc.populateMetadataFunc = { |synthdesc|
    ... do work here ...
};
```





### Synchronization
Whenever a .scsyndef file is written, any existing metadata files will be deleted so that a new .scsyndef file will not exist on disk with out-of-date metadata.




### Reading
When reading a SynthDesc, metadata files will be checked and one will be read, regardless of format. (Even if the default SynthDesc.mdPlugin is different from the file format on disk, the disk file will be read using the appropriate plug-in anyway.)

There should be only one metadata file at a time. However, in the case of conflicts, the default SynthDesc.mdPlugin will be preferred. The file extension identifies the format.




### Metadata Examples

```
s.boot;

d = SynthDef(\mdDemo, { |out, freq, cutoff, volume, gate = 1|
    var    sig = LPF.ar(Saw.ar(freq, volume), cutoff),
        env = EnvGen.kr(Env.adsr, gate, doneAction: Done.freeSelf);
    Out.ar(out, (sig * env) ! 2)
}).add;

SynthDescLib.global[\mdDemo].makeWindow;

// Note in the resulting window that Freq has a slider, but Cutoff and Volume do not.
// This is because there are no global specs for the argument names 'cutoff' and 'volume'.


// Same SynthDef, but adding metadata
// \freq and \amp exist in the global ControlSpec collection -- Spec.specs
// They are converted to real ControlSpecs using .asSpec

d = SynthDef(\mdDemo, { |out, freq, cutoff, volume, gate = 1|
    var    sig = LPF.ar(Saw.ar(freq, volume), cutoff),
        env = EnvGen.kr(Env.adsr, gate, doneAction: Done.freeSelf);
    Out.ar(out, (sig * env) ! 2)
}, metadata: (specs: (cutoff: \freq, volume: \amp))).add;

SynthDescLib.global[\mdDemo].makeWindow;

// Now cutoff has a slider for frequency and volume has amplitude scaling


// Store the SynthDef along with metadata
d.store(mdPlugin: TextArchiveMDPlugin);

"ls %mdDemo.*".format(SynthDef.synthDefDir.escapeChar($ )).unixCmd;

// In addition to .scsyndef, there's also .txarcmeta - "text archive metadata"

// Load a fresh SynthDesc from disk for it
// The SynthDesc.read interface is a bit weird - e will be a dictionary holding the SynthDesc
e = SynthDesc.read(SynthDef.synthDefDir ++ "mdDemo.scsyndef");

// Metadata have been successfully read from disk!
// You could even do the above after recompiling and the MD would be there
e[\mdDemo].metadata

e[\mdDemo].makeWindow;
```






## Class Methods



### `read`
Adds all synthDescs in a path to a dict. You should not use this method or *readFile to read SynthDescs into a SynthDescLib. Use [SynthDescLib#read](../Classes/SynthDescLib.md#read) or [SynthDescLib#readStream](../Classes/SynthDescLib.md#readstream) instead.

## Instance Methods


### `name`
**Returns:** the name of the SynthDef
### `controls`
**Returns:** an array of instances of [ControlName](../Classes/ControlName.md), each of which have the following fields: name, index, rate, defaultValue
```
SynthDescLib.global.at(\default).controlNames.postln;
```


### `controlDict`
An [IdentityDictionary](../Classes/IdentityDictionary.md) of the [ControlName](../Classes/ControlName.md)'s, indexed by name. This can be used for fast lookup of control index by name, for example to set a specific element of a multichannel control.
### `controlNames`
**Returns:** an array of Strings with the names of controls
### `outputs`
**Returns:** an array of [IODesc](../Classes/IODesc.md) that describes the available outputs.
### `inputs`
**Returns:** an array of [IODesc](../Classes/IODesc.md) that describes the available inputs.
### `hasGate`
is true if the Synthdef has a gate input
### `canFreeSynth`
is true if the [Synth](../Classes/Synth.md) can free itself (via some means, usually a doneAction)This can be used to decide if to remove a Synth directly via free-message.
```
SynthDescLib.global.at(\default).canFreeSynth;
```


### `outputData`
Returns an array of events with information about any UGens that write to a bus (such as [Out](../Classes/Out.md) etc.). This includes the rate and number of channels of the UGen. If its first input is a control, also the corresponding control name is provided.
```
a = SynthDef(\x, { |out, freq = 440| Out.ar(out, SinOsc.ar(freq)) }).add;
a.desc.outputData;
a = SynthDef(\x, { |out, freq = 440| Out.ar(out + 7, SinOsc.ar(freq)) }).add; // no controlName in this case
a.desc.outputData;
```


### `msgFunc`
the function which is used to create an array of arguments for playing a synth def in patterns
```
SynthDescLib.global.synthDescs.at(\default).msgFunc.postcs;
```



