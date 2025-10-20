# Pattern Guide 08: Event Types and Parameters

*Describes the event types defined in the default event, and the parameters they expect*

**Related:** [A-Practical-Guide/PG_07_Value_Conversions](../../Tutorials/A-Practical-Guide/PG_07_Value_Conversions.md), [A-Practical-Guide/PG_Cookbook01_Basic_Sequencing](../../Tutorials/A-Practical-Guide/PG_Cookbook01_Basic_Sequencing.md)

**Categories:** Streams-Patterns-Events>A-Practical-Guide, Tutorials>Pattern-Guide


## Event types
A common question is, "Which parameters have special meanings in Pbind?" Perhaps surprisingly, none of them do! That's because Pbind simply puts data into the result event; it doesn't care what the data are.

The event prototype used when playing the pattern defines the actions to take, and it is here that parameters are defined. Most patterns will play using the default event prototype ( `Event.default` ), so this is the source of the parameters that will most typically be used.

The default event prototype defines a number of "event types," each of which performs a different task. The `\type` key determines which action is taken, and the significant parameters depend on the event type.

There are a lot of event types! However, only a few are commonly used. The `\note` event type is by far the most typical. The others are auxiliary, and most useful when writing patterns to generate a [Score](../../Classes/Score.md) suitable for non-real-time rendering.

Before looking at the event types themselves, let's go over some standard parameters used across many event types. (Not every common parameter is used in every event type, but these turn up in lots of places.)



## Common parameters

### Timing control

**\delta**
: Number of **beats** until the next event. Calculated from `~dur * ~stretch`, if `\delta` is not given explicitly.

**\lag**
: Number of **seconds** to delay the event's server message(s).

**\timingOffset**
: Number of **beats** to delay the event's server message(s). In conjunction with [Quant](../../Classes/Quant.md), this allows control over the order of event preparation between different patterns in the client, without desynchronizing sonic events that should play together. [A-Practical-Guide/PG_06g_Data_Sharing](../../Tutorials/A-Practical-Guide/PG_06g_Data_Sharing.md) has an example of its use to pass data from a bass pattern to a chord pattern.

**\sustain**
: Number of beats to wait before releasing a Synth node on the server. The SynthDef must have a `gate` argument for the explicit release to be sent; otherwise, the pattern assumes the note will release itself using a timed envelope. `\sustain` is calculated from `~dur * ~legato * ~stretch` if not given directly.

**\sendGate**
: The default behavior for releasing a note is to look in the [SynthDesc](../../Classes/SynthDesc.md) for an argument called \gate. If it's present, the event will send a `node.set(\gate, 0)` message to the server. If not, no release will be sent; it's assumed that the SynthDef will release itself after a given length of time. `\sendGate` overrides this behavior: `true` means to force the release message to be sent, whether or not the argument exists, while `false` means to suppress the release message.It isn't typical use to override; nonetheless, for some special cases, it may be useful.

**\tempo**
: Optional. If a value is given (in beats per second), it will change the tempo of the TempoClock playing the pattern. Here, the note duration is constant but the clock's speed changes.
> **Note:** Changing the tempo will affect all patterns playing on the same clock.


```
Pbind(
    \curve, Pseg(Pseq([0, 1, 0], 1), 15),
    \degree, Pwhite(-7, 0, inf) + Pkey(\curve).linlin(0, 1, 0, 14).asInteger,
    \dur, 0.5,
    \tempo, Pkey(\curve).linlin(0, 1, 1, 10)
).play;
```






### Node control

**\addAction**
: How to add a synth or group node relative to the given `\group` in the event. See [Synth](../../Classes/Synth.md).

**\amp**
: Not formally defined as a special parameter, but this is typically used for Synth amplitude. The SynthDef should have an `amp` argument and use it to control volume. `\amp` is optionally calculated from `\db`.

**\id**
: The desired id(s) for newly created Nodes in this event. Normally this is `nil`, in which case the IDs will be obtained from `server.nextNodeID`.

**\instrument**
: The [SynthDef](../../Classes/SynthDef.md) name for which nodes will be created. Only one name should be given (unlike other arguments, which "multichannel expand" to create multiple nodes).

**\group**
: The target node relative to which new node(s) will be created. Similar to `target` in `Synth(defName, args, target, addAction)`.

**\out**
: Generally used for the output bus of a [Synth](../../Classes/Synth.md). When using [Pbus](../../Classes/Pbus.md) or [Pfxb](../../Classes/Pfxb.md), an audio bus is allocated to isolate the pattern's signal. All events from the pattern receive the new bus number in the `\out` slot, and SynthDefs being played should use an `out` argument for the target of output UGens, e.g., `Out.ar(out, ...)` .






### User function hooks

**\finish**
: A function that will be executed after `play` has been called, but before event type processing. Use this to manipulate event data.

**\callback**
: A function that will be executed after the Event has finished all its work. The `callback` may be used for bookkeeping. Finished Events are expected to store new node IDs under `~id`; with the IDs, you can register functions to watch node status or set node controls, for instance. The function receives the finished event as its argument.







## Event Types

### Node control

**rest**
: As one would expect, a `\rest` does nothing except wait the required amount of time until the next event.

**note**
: This is the default event type, used when `\type` is not specified. It plays one or more Synth nodes on the server, with an automatic release after `\sustain` beats if the SynthDef has a `gate` argument.
**Standard Timing and Node control arguments**
: 

**sendGate**
: Override SynthDef behavior for the `gate` argument. If the SynthDef as `gate`, setting `sendGate = false` prevents the release message from being sent. Rarely used.

**strum**
: If multiple notes are produced (usually a chord, given by providing an array to one of the pitch parameters), `\strum` is the number of beats to delay each successive note onset. When using `\strum`, another key is active, `\strumEndsTogether`. If false (the default), each strummed node will play for its full duration and the releases will be staggered. If true, the releases will occur at the same time.
```
p = Pbind(
        // array is "multichannel expanded" into one Synth each
    \degree, #[2, 5, 8, 11, 13, 16],
    \octave, 3,
    \dur, 2,
    \sustain, 3,
        // non-zero strum staggers the entrances
    \strum, 0.12
).play(quant: 2);

p.stop;
```

**on**
: Start a Synth node (or nodes) without releasing. The node ID(s) are in the event's `~id` variable. Those IDs can be used with the off, set and kill event types.
**Standard Timing and Node control arguments**
: 

**(sendGate and strum parameters are not used)**
:

**off**
: Release server nodes nicely if possible. If the SynthDef has a `gate` argument, the gate will be set to `0` or a user-specified value. Otherwise, the nodes are brutally killed with `n_free`.
**Standard Timing control arguments**
: 

**hasGate**
: True or false, telling the event whether the SynthDef has a `gate` argument or not. The default is assumed true.

**id**
: The node ID(s) must be given explicitly.

**gate**
: By default, the gate will be set to `0`. Negative values trigger a "forced release" in EnvGen. See the [EnvGen](../../Classes/EnvGen.md) help file for details.

**kill**
: Immediately remove nodes using `n_free`.
**Standard Timing control arguments**
: 

**id**
: The node ID(s) must be given explicitly.

**set**
: Send new values to the control inputs of existing nodes.
**Standard Timing control arguments**
: 

**id**
: The node ID(s) must be given explicitly. This may be an integer ID or Synth/Group node object.



There are two ways to specify argument names: by *instrument* and by *argument array*.

- *By instrument* :
**instrument**
: The SynthDef name should be given again, so that the event knows which event values are relevant for the nodes.

**args**
: By default, the `\args` key contains the control names for the default synthdef. To take argument names from the instrument name, you must override this default with an empty array (or any non-collection object).
```
(
SynthDef(\event_set, { |freq = 440, gate = 1, amp = 0.1, lagTime = 0.1,
        ffreq = 2000, detune = 1.005, out = 0|
    var    sig = Saw.ar(Lag.kr(freq, lagTime) * [1, detune]).sum * amp
            * EnvGen.kr(Env.adsr, gate, doneAction: Done.freeSelf);
    Out.ar(out, sig ! 2);
}).add;
)

a = Synth(\event_set);

(
p = Pbind(
    \type, \set,
    \id, a,
    \instrument, \event_set,
    \args, #[],
    \freq, Pexprand(200, 600, inf),
    \dur, Pwhite(1, 5, inf) * 0.125
).play;
)

p.stop;
a.free;
```


- *By argument names* :
**args**
: Provide a list of the Synth argument names as an array here, e.g. `[\freq, \amp, \pan]`. There is no need to provide the instrument name this way.
```
a = Synth(\event_set);

(
p = Pbind(
    \type, \set,
    \id, a,
    \args, #[\freq],
    \freq, Pexprand(200, 600, inf),
    \dur, Pwhite(1, 5, inf) * 0.125
).play;
)

p.stop;
a.free;
```





**monoNote**
: 

**monoOff**
: 

**monoSet**
: These event types are used internally by Pmono and PmonoArtic. They should not be used directly.






### Server control

**group**
: Create a new group (or groups).
**Standard Timing and Node control arguments**
: 

**id**
: (Optional) IDs for the new groups. If not specified, the new ID (for one group only) can be found in the event after `.play`. To create multiple groups, you must provide an array of IDs.

**bus**
: Set the value of a control bus, or contiguous control buses. This assumes that you already have the bus index.
**Standard Timing control arguments**
: 

**array**
: The value(s) to send to the bus(es). If it's only one value, it doesn't have to be an array.

**out**
: The first bus index to be set. A Bus object can be used.






### Buffer control
All of these buffer event types expect the buffer number to be provided. They will not automatically get a buffer number from the server's buffer allocator. A Buffer object is allowed -- you could create the Buffer first using `Buffer.alloc` or `Buffer.new` and then use this object in the control events. See also [#Event types with cleanup](#event-types-with-cleanup) below for other, user-friendlier Buffer control options.


**alloc**
: Allocate memory for a buffer on the server. Only one buffer may be allocated per event.
**Standard Timing control arguments**
: 

**bufnum, numchannels, numframes**
: See the [Buffer](../../Classes/Buffer.md) help file.

**free**
: Deallocate the buffer's memory on the server.
**Standard Timing control arguments**
: 

**bufnum**
: Buffer number to free (one only).

**gen**
: Generate wavetable data in the buffer, using one of the server's `b_gen` plug-ins. The [Buffer](../../Classes/Buffer.md) help file has more detail on the standard plug-ins.
**Standard Timing control arguments**
: 

**bufnum**
: 

**gencmd**
: The generator plug-in name: `\sine1`, `\sine2`, `\sine3`, `\cheby`.

**genflags**
: Three flags, associated with numbers: normalize = `1`, asWavetable = `2`, clearFirst = `4`. Add the numbers for the desired flags. Normally the flags are all true, adding up to `7`.

**genarray**
: Data parameters for the plug-in. See the [Server-Command-Reference](../../Reference/Server-Command-Reference.md) help file for details on the format for each plug-in.

**load**
: Allocate buffer memory in the server and load a sound file into it, using `b_allocRead`.
**Standard Timing control arguments**
: 

**bufnum**
: 

**filename**
: Path to disk file.

**frame**
: Starting frame to read (default `0`).

**numframes**
: Number of frames to read (default `0`, which loads the entire file).

**read**
: Read a sound file into a buffer already allocated on the server. This event type is good to cue a sound file for use with DiskIn.
**Standard Timing control arguments**
: 

**bufnum**
: 

**filename**
: Path to disk file.

**frame**
: Starting soundfile frame to read (default `0`).

**numframes**
: Number of frames to read (default `0`, which loads the entire file).

**bufpos**
: Starting buffer frame (default `0`).

**leaveOpen**
: `1` = leave the file open (for [DiskIn](../../Classes/DiskIn.md) use). `0` = close the disk file after reading. Default = `0`.






### Event types with cleanup
These event types uniquely have automatic cleanup event types associated with them. Playing one of these event types allocates a server resource. Later, the resource may be freed by changing the event type to the corresponding cleanup type and playing the event again. While the resource is active, the event can be used as a reference to the resource in other events or Synth messaging.


```
// create a buffer
b = (type: \allocRead, path: ExampleFiles.child).play;

a = { PlayBuf.ar(1, b, doneAction: Done.freeSelf) }.play;

// remove buffer
EventTypesWithCleanup.cleanup(b);
```


See the Pproto example in [A-Practical-Guide/PG_06f_Server_Control](../../Tutorials/A-Practical-Guide/PG_06f_Server_Control.md), showing how these can be used to clean up server objects at the end of a pattern.


**audioBus**
: Allocate an audio bus index from the server.
**channels**
: Number of channels to allocate.

**controlBus**
: Allocate a control bus index from the server.
**channels**
: Number of channels to allocate.

**buffer**
: Allocate a buffer number if not specified, and reserve the memory on the server.
**bufNum**
: (Optional) Buffer number. If not given, a free number will be obtained from the server.

**numBufs**
: Number of contiguous buffer numbers to reserve (default = `1`).

**numFrames**
: Number of frames.

**numChannels**
: Number of channels.

**allocRead**
: Read a disk file into server memory. The file is closed when finished.
**bufNum**
: (Optional) Buffer number. If not given, a free number will be obtained from the server.

**path**
: Path to the sound file on disk.

**firstFileFrame**
: Where to start reading in the file.

**numFrames**
: Number of frames. If not given, the whole file is read.

**cue**
: Cue a sound file (generally for use with DiskIn).
**bufNum**
: (Optional) Buffer number. If not given, a free number will be obtained from the server.

**path**
: Path to the sound file on disk.

**firstFileFrame**
: Where to start reading in the file.

**numFrames**
: Number of frames. If not given, the whole file is read.

**firstBufferFrame**
: Where in the buffer to start putting file data.

**leaveOpen**
: `1` = leave the file open (for [DiskIn](../../Classes/DiskIn.md) use). `0` = close the disk file after reading. Default = `0`.

**table**
: Fill a buffer with preset data. This uses `/b_setn` to transfer the data, so all of the data must fit into one datagram. It may take some experimentation to find the upper limit.
**bufNum**
: (Optional) Buffer number. If not given, a free number will be obtained from the server.

**amps**
: The values to put into the buffer. These should all be Floats.

**cheby**
: Generate a Chebyshev transfer function for waveshaping.
**bufNum**
: (Optional) Buffer number. If not given, a free number will be obtained from the server.

**numFrames**
: Number of frames, should be a power of 2.

**numChannels**
: Number of channels.

**genflags**
: Three flags, associated with numbers: normalize = `1`, asWavetable = `2`, clearFirst = `4`. Add the numbers for the desired flags. Normally the flags are all true, adding up to `7`.

**amps**
: The amplitude of each partial (i.e., polynomial coefficient).

**sine1**
: Mirrors the `sine1` method for [Buffer](../../Classes/Buffer.md), generating a wavetable with an integer-multiple harmonic spectrum using the given partial amplitudes.
**bufNum**
: (Optional) Buffer number. If not given, a free number will be obtained from the server.

**numFrames**
: Number of frames, should be a power of 2.

**numChannels**
: Number of channels.

**genflags**
: See above.

**amps**
: Array of amplitudes for each partial.

**sine2**
: Like **sine1**, but the frequency ratio of each partial is also given.
**Same arguments as sine1, plus:**
: 

**freqs**
: Array of frequencies for each partial. `1.0` is the fundamental frequency; its sine wave occupies the entire buffer duration.

**sine3**
: Like **sine2**, but the phase of each partial may also be provided.
**Same arguments as sine1, plus:**
: 

**phases**
: Array of phases for each partial, given in radians (0.0 - 2pi).






### MIDI output

**midi**
: Sends one of several types of MIDI messages to a MIDIOut object.
**Standard Timing control arguments (except timingOffset, which is not used)**
: 

**midicmd**
: The type of MIDI message to send. This also determines other arguments that should be present in the event.

**midiout**
: The MIDI out object, which connects to one of the MIDI devices listed in `MIDIClient.destinations`.

**chan**
: The MIDI channel number (0-15) on the device that should receive the message. This applies to all midicmds except the global ones ( **smpte**, **songPtr**, **sysex** ).




**Available midicmds:**
: **noteOn**
: Starts a note, and optionally stops it. If multiple frequencies are given, one noteOn/noteOff pair is sent for each, and `\strum` is also supported.
**chan**
: MIDI channel (0-15).

**midinote**
: Note number to trigger. This may be calculated from the standard pitch hierarchy described in [A-Practical-Guide/PG_07_Value_Conversions](../../Tutorials/A-Practical-Guide/PG_07_Value_Conversions.md) (with the exception that only 12TET can be supported).

**amp**
: `MIDI velocity = amp * 127`.

**sustain**
: How many beats to wait before sending the corresponding note off message. If not given directly, it's calculated as `~sustain = ~dur * ~legato * ~stretch` (just like the standard `\note` event type).

**hasGate**
: Normally true. If false, the note off message will not be sent.

**noteOff**
: Send an explicit note off message (useful if **hasGate** is set false in the note on event).
**chan**
: MIDI channel (0-15).

**midinote**
: Note number.

**amp**
: Release velocity (supported by some synthesizers).

**allNotesOff**
: "Panic" message, kills all notes on the channel.
**chan**
: MIDI channel (0-15).

**control**
: Continuous controller message.
**chan**
: MIDI channel (0-15).

**ctlNum**
: Controller number to receive the new value.

**control**
: New value (0-127).

**bend**
: Pitch bend message.
**chan**
: MIDI channel (0-15).

**val**
: New value (0-16383). 8191 is centered.

**touch**
: Aftertouch message.
**chan**
: MIDI channel (0-15).

**val**
: New value (0-127).

**polyTouch**
: Poly aftertouch message (not supported by all synthesizers).
**chan**
: MIDI channel (0-15).

**midinote**
: Note number to get the new after touch value. As in note on, it may be calculated from the standard pitch hierarchy.

**polyTouch**
: New value (0-127).

**program**
: Program change message.
**chan**
: MIDI channel (0-15).

**progNum**
: Program number (0-127).

**smpte**
: Send MIDI Time Code messages.
**Arguments**
: frames, seconds, minutes, hours, frameRate

**songPtr**
: Song pointer message.
**songPtr**
: Pointer value (0-16383).

**sysex**
: System exclusive messages.
**array**
: An [Int8Array](../../Classes/Int8Array.md) with the sysex bytes in order.
> **Note:** Very important: Arrays normally multi-channel expand in patterns. So, you must wrap the Int8Array inside another array to prevent this. Write `[Int8Array[...]]`, not just `Int8Array[...]`.






### Miscellaneous

**composite**
: Perform any number of event types, given as ~types. You should ensure that parameters are compatible. It is possible, using `\composite`, to play a synth and send MIDI for the same pitches. It is not possible to use one frequency for the synth and a different one for MIDI, in the same event (you would need two different events for that case).
**types**
: An array of Symbols, listing the Event types to be performed.


```
MIDIClient.init;
m = MIDIOut(0);

// should play a synth *and* an external MIDI note simultaneously
(type: \composite, types: [\note, \midi], midiout: m, degree: 0, dur: 3).play;
```

**phrase**
: See [JITLib/recursive_phrasing](../../Tutorials/JITLib/recursive_phrasing.md).

**setProperties**
: Set variables belonging to a given object. One possible use is to control a GUI using a pattern.
**receiver**
: The object to be modified.

**args**
: The list of variable names to set in the receiver. The receiver should have a setter method -- variableName_ -- for each of these. New values will be looked up in the event.


```
// Visualize Brownian motion
w = Window("Brownian motion", Rect(10, 100, 500, 50));
x = Slider(w, Rect(10, 15, 480, 20));
w.front;

p = Pbind(
    \type, \setProperties,
    \receiver, x,
        // this means, call x.value_() on every event
    \args, [\value],
        // and look for the value under \value
    \value, Pbrown(0, 1, 0.1, inf),
    \delta, 0.1
).play;

p.stop;
```



Previous: [A-Practical-Guide/PG_07_Value_Conversions](../../Tutorials/A-Practical-Guide/PG_07_Value_Conversions.md)

Next: [A-Practical-Guide/PG_Cookbook01_Basic_Sequencing](../../Tutorials/A-Practical-Guide/PG_Cookbook01_Basic_Sequencing.md)





