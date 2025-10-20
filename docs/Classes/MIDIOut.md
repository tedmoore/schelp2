# MIDIOut

*send MIDI messages*

**Related:** [MIDIClient](../Classes/MIDIClient.md), [MIDIIn](../Classes/MIDIIn.md), [MIDI](../Guides/MIDI.md), [UsingMIDI](../Guides/UsingMIDI.md), [Overviews/MidiPatterns](../Overviews/MidiPatterns.md)

**Categories:** External Control>MIDI

## Description

a MIDIOut is bound to a specific [MIDIEndPoint](../Classes/MIDIEndPoint.md) as defined by the operating system.
Linux users, or any users who require cross-platform compatibility with Linux, should read [#Linux specific: Connecting and disconnecting ports](#linux-specific:-connecting-and-disconnecting-ports) carefully.


## Class Methods



### `new`
Create a new MIDIOut instance. Note that this method is not safe for cross-platform usage with Linux, because the meaning of the `port` argument is different. See [#Linux specific: Connecting and disconnecting ports](#linux-specific:-connecting-and-disconnecting-ports) for details.**Arguments:**

| Argument | Description |
|----------|-------------|
| `port` | **macOS, Windows**
: The index of the MIDIEndPoint in the `MIDIClient.destinations` array.

**Linux**
: The output port number. `MIDIEndPoint("SuperCollider", "out0")` is port 0; `"out1"` is port 1. In Linux, this argument has no connection at all to `MIDIClient.destinations`. |  
| `uid` | **macOS / Windows**
: uid is optional; if specified, it should be the uid of that port ie. MIDIClient.destinations[port].uid. If you don't provide a uid, the correct uid will be filled in for you (easier).

**Linux**
: using the uid is optional as described below. |  


### `newByName`
Searches for the MIDI output device, by a name found in the `MIDIClient.destinations` array. This is safer then depending on the index which will change if your studio setup changes. It is also Linux compatible.
```
// list connected out ports with names:
MIDIClient.init;
MIDIClient.destinations;
```



### `findPort`
Searches for a connected MIDIEndPoint by name.
```
// list connected out ports with names:
MIDIClient.init;
MIDIClient.destinations;
```



### `connect`, `disconnect`
Linux only. MacOS does not need to connect. On Linux it is an optional feature (see below).

## Instance Methods


### `sysex`
Sends a sysex command represented as an [Int8Array](../Classes/Int8Array.md) to the device.
> **Note:** The method call should contain a full sysex message. In other words, it should start with 0xF0 (240 or -16) and end with 0xF7 (247 or -9).

**Arguments:**

| Argument | Description |
|----------|-------------|
| `packet` | An Int8Array of data bytes to be sent.
```
m = MIDIOut(0);

m.sysex(Int8Array[0xF0, 1, 2, 3, 0xF7]);  // OK!

m.sysex(Int8Array[1, 2, 3]);  // not OK
``` |  

### `latency`
This sets the latency with which a midi event is sent out. Per default, this is set to 0.2, in order to be equal to the Server.latency.
> **Note:** On Linux, there seems to be an ALSA or kernel bug if the latency is larger than 0, for some Linux kernels. If MIDIOut does not seem to work, set the latency to 0.


## Examples


```
MIDIClient.init;

m = MIDIOut(0);  // Linux users: MIDIOut(0, MIDIClient.destinations[0].uid)
m.noteOn(16, 60, 60);
m.noteOn(16, 61, 60);
m.noteOff(16, 61, 60);
m.allNotesOff(16);


MIDIIn.connect; // 1 port midi interface
MIDIIn.sysex = { |uid, packet| [uid, packet].postln };
MIDIIn.sysrt = { |src, chan, val|  [src, chan, val].postln };
MIDIIn.smpte = { |src, chan, val|  [src, chan, val].postln };

m.sysex(Int8Array[0xF0, 0, 0, 27, 11, 0, 0xF7])

m.smpte(24, 16)
m.midiClock
m.start
m.continue
m.stop
```



### Using patterns for sending MIDI events
See [MidiPatterns](../Overviews/MidiPatterns.md) for details!


```
MIDIClient.init;
m = MIDIOut(0);  // Linux users: MIDIOut(0, MIDIClient.destinations[0].uid)

// Simplest way for sending \note-type events to MIDI
// define a Pattern of note-events:
a = Pbind(degree: Prand([1, 2, 3, [0, 5]], inf));

// chain a \midi-type event into the pattern and play it (see link::Classes/Pchain::)
// this will also take care of noteOffs. 
(a <> (type: \midi, midiout: m)).play;

// a tidier way to do the same, where we specify the type of midi commands we want to send:
a = Pbind(midicmd: \noteOn, degree: Prand([1, 2, 3, [0, 5]], inf));
(a <> (type: \midi, midiout: m)).play;
//again, noteOffs are taken care off by default (but this can be turned off).

//other selected midicmds:
// for bend messages: 
b = Pbind(midicmd: \bend, val: Pwhite(0,16383));
(b <> (type: \midi, midiout: m)).play;

// for CC messages: 
c = Pbind(midicmd: \control, control: Pwhite(0,127), ctlNum: 0);
(c <> (type: \midi, midiout: m)).play;
```


See [A-Practical-Guide/PG_08_Event_Types_and_Parameters#MIDI output](../Tutorials/A-Practical-Guide/PG_08_Event_Types_and_Parameters.md#midi-output) for a list of midi commands supported by the 'midi' event type.



### Linux specific: Connecting and disconnecting ports
In Linux, the MIDIOut architecture is different from other operating systems.

In macOS and Windows, a MIDIOut instance is bound to a specific destination MIDI device.

SuperCollider in Linux uses the ALSA MIDI layer. ALSA MIDI applications send messages out through a "virtual output port," which is one of the members of `MIDIClient.sources`.


```
MIDIClient.init;
```



At this point, creating `MIDIOut(0)` tells SuperCollider that this MIDIOut object should direct messages to `MIDIEndPoint("SuperCollider", "out0")`. (It seems strange, if you think of SuperCollider sending messages to this MIDI *source*. It is more accurate to think of SuperCollider sending messages *through* this port. The port is, then, a source for the rest of the system.)

A `MIDIOut(0)` object, then, will not reach any destinations by default. The user needs to connect destination devices to the virtual source port, using either a graphical tool such as Qjackctl, or by MIDIOut's `connect` method.


```
m = MIDIOut(0);  // use virtual source port "out0"
m.connect(1);  // connect to MIDIClient.destinations[1]
```


> **⚠️ Warning:** The `port` argument to [MIDIOut#*new](../Classes/MIDIOut.md#*new) has an entirely different meaning in Linux, compared to macOS and Windows. If user code calls this method *and* cross-platform compatibility is needed, it is the user's responsibility to handle Linux separately. User code can check the platform using `thisProcess.platform.name` (which returns one of `\osx`, `\linux` or `\windows`). Or, for compatibility, use [#*newByName](#*newbyname) instead.
[MIDIOut#*new](../Classes/MIDIOut.md#*new) optionally takes a second argument, for the uid of the MIDI destination device. If the uid is non-zero, then: 1/ all connections in the ALSA MIDI patchbay are ignored, and 2/ individual messages will be sent directly to the specified device.

[MIDIOut#*newByName](../Classes/MIDIOut.md#*newbyname) locates a device by name and populates the uid in the new MIDIOut object. After successful completion, a MIDIOut object created using this method will have a non-zero uid.


> **Note:** A non-zero uid (whether specified in `MIDIOut.new`, found by `MIDIOut.newByName`, or set manually later) does not create or use any ALSA MIDI connections. It is not a "connection" at all; rather, it is a parameter that causes outgoing MIDI messages to bypass ALSA MIDI connections and go directly to one specific device. Because it is not a connection, there is nothing to show in MIDI patchbay interfaces; users should not expect to see connections for these MIDIOut objects.Also, because a uid bypasses patchbay connections, it is meaningless to specify a uid and use `.connect` at the same time. A single MIDIOut object should not do both at once. (It does not break anything, but the patchbay connections are ignored.)


**Compatibility**

- `MIDIOut.newByName("device", "port")` -- Should be compatible on all systems.
- `MIDIOut(index)` -- macOS, Windows (`index` is the device's index in `MIDIClient.destinations`). Note that this usage is *not* compatible with Linux! macOS and Windows users should not expect Linux users to be able to run this style of connection.
- `MIDIOut(0, MIDIClient.destinations[index].uid)` -- Linux only (`index` is the device's index in `MIDIClient.destinations`).




### macOS specific: Sending MIDI to other applications
Open the Audio MIDI Setup application. Double-click on IAC Driver and check "device is online".

reinitialize:

MIDIClient.init(numIns, numOuts)

The IAC Bus will now appear in MIDIClient.destinations. It will appear first, which means that any code that you have written that addresses the first physical bus as 0 will now have to be changed.

For this reason, it is always safer to find the port by name :


```
MIDIOut.newByName("RemoteSL IN", "Port 1");
```


The IAC Bus will now also appear to other applications.

MIDIMonitor (freeware) can be very useful for troubleshooting:

[http://www.snoize.com/MIDIMonitor/](http://www.snoize.com/MIDIMonitor/)



### Sysex example
a machinedrum manual say sysex commands should be formatted like this...


```
$f0,$00,$20,$3c,$02,$00,command,...,$f7
```


and to set the tempo the machinedrum expects this command...


```
$61 | Set tempo ID
%0aaaaaaa | Upper bits
%0bbbbbbb | Lower bits
$f7 | SYSEX end
Note: Tempo = %aaaaaaabbbbbbb / 24, max 300 BPM, min 30 BPM
```


so to create and send a valid set tempo sysex command from SuperCollider to this machinedrum do...


```
MIDIClient.init;
m = MIDIOut(0);  // Linux users: MIDIOut(0, MIDIClient.destinations[0].uid)
m.sysex(Int8Array[0xf0, 0x00, 0x20, 0x3c, 0x02, 0x00, 0x61, 21, 54, 0xf7]);
```


This will set the tempo to 114.23 bpm. One can calculate the upper and lower 7bit values like this...


```
(
var bpm, val, upper, lower;
bpm = 114.23;
val = (bpm*24).round.asInteger;
upper = val&2r11111110000000>>7;
lower = val&2r00000001111111;
[upper, lower].postln;
)
```


where the resulting 21 and 54 are the same as 2r0010101 and 2r0110110 in binary notation.



