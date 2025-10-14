# Event types

*Different ways that an Event can "play"*

**Categories:** Streams-Patterns-Events>Events

**Related:** [Event](../Classes/Event.md)

An [Event](../Classes/Event.md) responds to a `play` message by evaluating ~play in the event, and the default behaviour of ~play is determined by the value of ~type.> *To see how event types are normally invoked, here is a slightly simplified version of the default definition of ~play as defined in the Event class:`{ ~eventTypes[~type].value(server); }`The function uses the value of ~type to select a function from the Dictionary held in ~eventTypes.*

```supercollider
a = (play: { ~word.scramble.postln }, word: "hello word");
a.play;

a = (type: \note, freq: [1310, 1321]); // choosing a play function by specifying type
a.play;
```

The collection of eventTypes can be readily extended using [*addEventType](../Classes/Event.md#*addeventtype):

```supercollider
Event.addEventType(\test, { "Your word is: ".post; ~word.scramble.postln });
(type: \test, word: "annahme").play;
```


## Currently existing event types:

> **Note:** this documentation is incomplete.



**note**
: Instantiate a synth on the server, with specified arguments, and later to free it. The choice of [SynthDef](../Classes/SynthDef.md) is specified using the \instrument key. This event type is what `Event.default` returns.`(degree: [0, 5, 7, 11]).play;`Actually plays this event type:`(type: \note, degree: [0, 5, 7, 11], instrument: \default).play;`

**set**
: used to set parameters of some already-running node(s).
```supercollider
a = (degree: 3, sustain: 40).play;
fork { 10.do { (type: \set, id: a[\id], \degree: [0, 5, 8, 11].choose).play; 0.3.wait } };
```

(See also: note in [Pmono](../Classes/Pmono.md) helpfile)

**group**
: creates a new group optional parameters:| ~id | node ID, or node object | 
| --- | --- || ~group | outer group id or object | | ~addAction / ~lag / ~timingOffset | determine how and when the group is created | Example:
```supercollider
(type: \group, id: 2).play                    // create a group with nodeID 2
(type: \note, freq: 500, group: 2).play        // play a synth in that group
```

**midi**
: send note parameters to midi device parameters:| ~midicmd | A Symbol, for the MIDI command to issue | 
| --- | --- || ~midiout | A MIDIOut object | | ~chan | The MIDI channel number (0-15) | See [A-Practical-Guide/PG_08_Event_Types_and_Parameters#MIDI output](../Tutorials/A-Practical-Guide/PG_08_Event_Types_and_Parameters.md#midi-output) for details on available midicmds.

**on**
: play synth, ~id must be specified

**off**
: release synth (or free if no gate)

**kill**
: free synth

**rest**
: do nothing for a specified amount of time

**composite**
: perform any number of event types, given as ~types
```supercollider
MIDIClient.init;
m = MIDIOut(0);

// should play a synth *and* an external MIDI note simultaneously
(type: \composite, types: [\note, \midi], midiout: m, degree: 0, dur: 3).play;
```

**bus**
: write ~array to control buses starting at ~out

**audioBus**
: allocate ~channels consecutive audio buses

**controlBus**
: allocate ~channels consecutive control buses

**alloc**
: allocate ~bufnum with ~numframes and ~numchannels

**allocRead**
: load a file from ~path, starting at ~firstFileFrame, reading ~numFrames sample frames

**cue**
: cue a file for DiskIn, with ~bufferSize frames

**free**
: free ~bufnum

**gen**
: send ~gencmd to ~bufnum

**load**
: load ~filename starting at ~frame into ~bufnum

**read**
: 

**table**
: load ~amps directly into a buffer

**sine1**
: generate a buffer from ~amps

**sine2**
: generate a buffer from ~freqs, ~amps

**sine3**
: generate a buffer from ~freqs, ~amps, ~phases

**cheby**
: generate a waveshape buffer from ~amps

**setProperties**
: sends setter messages to ~receiver for each key in ~args that has a nonNil value in the Event.

**tree**
: creates a tree of groups. ~tree can be an array of nodeIDs, and may contain associations to further nested arrays.

**phrase**
: instead of playing a single synth from a SynthDef with ~instrument, it looks up a Pdef and plays a cluster of sounds.




### Some event types are used internally, e.g.:

**monoNote**
: used by Pmono

**monoSet**
: used by Pmono

**monoOff**
: used by Pmono









