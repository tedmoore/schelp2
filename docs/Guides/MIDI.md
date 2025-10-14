# MIDI

*about MIDI*

**Related:** [UsingMIDI](../Guides/UsingMIDI.md), [MIDIFunc](../Classes/MIDIFunc.md), [MIDIdef](../Classes/MIDIdef.md)

**Categories:** External Control>MIDI


## Practical usage overview
Begin with the [UsingMIDI](../Guides/UsingMIDI.md) help file.


### Receiving MIDI input
[MIDIFunc](../Classes/MIDIFunc.md) and [MIDIdef](../Classes/MIDIdef.md) are the standard, recommended way to receive MIDI note on/off, controller, pitch bend, aftertouch, poly-touch and program change messages.


> **Note:** **IMPORTANT:** Before MIDI can be received, SuperCollider needs to be told to connect to the MIDI subsystem and connect to the available devices.
```supercollider
MIDIClient.init;
MIDIIn.connectAll;
```

You need to do this once after launching SuperCollider, or recompiling the class library.


There are some examples in the wild using the MIDIIn class directly to receive MIDI. This is not recommended for normal use. The exceptions are sysex (system exclusive) and sysrt (MIDI clock) messages, which are currently supported only by MIDIIn. See the example below.




### Sending MIDI output
See the [MIDIOut](../Classes/MIDIOut.md) help file for details.





## Summary of MIDI classes

**[MIDIClient](../Classes/MIDIClient.md)**
: This class connects to the operating system's MIDI layer, and obtains the lists of available MIDI sources and destinations. The information about the hardware is stored in `MIDIClient.sources` and `MIDIClient.destinations` as [MIDIEndPoint](../Classes/MIDIEndPoint.md) objects. MIDIClient must be initialized before MIDI can be received. See the note above.

**[MIDIFunc](../Classes/MIDIFunc.md)**
: The optimal way to receive the most typical MIDI messages: note on/off, controller, pitch bend, aftertouch, poly-touch and program change.

**[MIDIdef](../Classes/MIDIdef.md)**
: Related to [MIDIFunc](../Classes/MIDIFunc.md), this class keeps several MIDIFunc objects in global storage, by name. Especially helpful for live or interactive use.

**[MIDIOut](../Classes/MIDIOut.md)**
: Supports MIDI output to hardware ports or inter-application MIDI buses.

**[MIDIEndPoint](../Classes/MIDIEndPoint.md)**
: Represents a MIDI port published by the operating system. It contains a device name, port name and unique identifier (uid).

**[MIDIIn](../Classes/MIDIIn.md)**
: The lowest-level MIDI input class. MIDIFunc and MIDIdef use this class so that you don't have to. It is strongly recommended to avoid using this class directly.




## Examples

MIDI input:

```supercollider
(
MIDIClient.init;
MIDIIn.connectAll;
m = MIDIFunc.noteOn({ |vel, num|
    "note % @ velocity %\n".postf(num, vel);
});
)

// when finished
m.free;
```


MIDI output:

```supercollider
(
MIDIClient.init;
m = MIDIOut(0, MIDIClient.destinations.at(0).uid);
m.noteOn(0, 60, 60);
)
```


Receiving system exclusive messages:

```supercollider
~sysexFunc = { |uid, data|
    // 'data' holds the sysex packet as 8-bit integers
};
MIDIIn.addFuncTo(\sysex, ~sysexFunc);

// when finished
MIDIIn.removeFuncFrom(\sysex, ~sysexFunc);
```




