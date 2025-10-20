# Pattern Guide 03: What Is Pbind

*Pattern-based musical sequencing with Pbind and cousins*

**Related:** [A-Practical-Guide/PG_02_Basic_Vocabulary](../../Tutorials/A-Practical-Guide/PG_02_Basic_Vocabulary.md), [A-Practical-Guide/PG_04_Words_to_Phrases](../../Tutorials/A-Practical-Guide/PG_04_Words_to_Phrases.md)

**Categories:** Streams-Patterns-Events>A-Practical-Guide, Tutorials>Pattern-Guide


## What's that Pbind thing?
Some of the examples in the last tutorial played notes using Pbind, and you might be wondering how it works in general and what else you can do with it.

In the most general sense, [Pbind](../../Classes/Pbind.md) is just a way to give names to values coming out of the types of patterns we just saw. When you ask a Pbind stream for its next value, the result is an object called an [Event](../../Classes/Event.md). Like a [Dictionary](../../Classes/Dictionary.md) (which is a superclass of Event), an event is a set of "key-value pairs": each value is named by a key.


```
e = (freq: 440, dur: 0.5);    // an Event

e.at(\freq)        // access a value by name
e[\freq]
e.freq        // See IdentityDictionary help for more on this usage

e.put(\freq, 880);    // Change a value by name
e[\freq] = 660;
e.freq = 220;

e.put(\amp, 0.6);    // Add a new value into the event
e.put(\dur, nil);    // Remove a value
```


A Pbind is defined by a list of pairs: keys associated with the patterns that will supply the values for the events.

Things get interesting when the names associated with Pbind's sub-patterns are also [SynthDef](../../Classes/SynthDef.md) arguments. Then it becomes possible to play new Synths with Pbind, and feed their inputs with different values on each event.



## Building an event, one key at a time
We can look at the return values from a Pbind by calling `next` on the stream. Note that it's necessary to pass an empty event into *next*, so that Pbind has somewhere to put the values.


```
(
p = Pbind(
    \degree, Pseq(#[0, 0, 4, 4, 5, 5, 4], 1),
    \dur, Pseq(#[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1], 1)
).asStream;    // remember, you have to make a stream out of the pattern before using it
)

p.next(Event.new);    // shorter: p.next(())

// Output:
( 'degree': 0, 'dur': 0.5 )
( 'degree': 0, 'dur': 0.5 )
( 'degree': 4, 'dur': 0.5 )
( 'degree': 4, 'dur': 0.5 )
```


The return events show us what Pbind really does. Each time the next value is requested, it goes through each key-pattern pair and gets the next value from each pattern (actually streams, but Pbind makes streams out of the sub patterns internally). Each value gets put into the event, using the associated key.

For the first event, the first key is `'degree'` and the value is `0`. This is placed into the event before moving to the next pair: the event in transition contains `( 'degree': 0 )`. Then the next key supplies `0.5` for `'dur'`, and since there are no more pairs, the event is complete: `( 'degree': 0, 'dur': 0.5 )`.

// User does:


```
p.next(Event.new);
```


// SuperCollider processes:

1. `\degree` stream returns `0`
2. Put it in the Event: `( 'degree': 0 )`
3. `\dur` stream returns `0.5`
4. Put it in the Event: `( 'degree': 0, 'dur': 0.5 )`
5. Return the result event.



> **Note:** Dictionaries in SuperCollider are *unordered* collections. Even though Pbind processes its child streams in the order given, the results can display the keys and values in any order. This does not affect the behavior of playing Events, as we will soon see.




## Event, .play and event prototypes
So far we haven't seen anything that produces a note, just data processing: fetching values from patterns and stitching them together into events. The notes come from the difference between Events and regular Dictionaries: Events can do things when you `.play` them.


```
( 'degree': 0, 'dur': 0.5 ).play;
```


The action that the event will take is defined in an "event prototype." The prototype must include a function for the `'play'` key; this function is executed when `.play` is called on the event. Also, optionally the prototype can contain default values for a wide variety of parameters.

Pbind doesn't do much without an event prototype. Fortunately, you don't have to write the prototype on your own. There is a default event, accessed by `Event.default`, that includes functions for many different server-messaging tasks. If no specific action is requested, the normal action is to play a Synth. That's why playing a Pbind, as in the previous tutorial, with only `'degree'` and `'dur'` patterns produced notes: each event produces at least one synth by default, and the default event prototype knows how to convert scale degrees into frequencies and `'dur'` (duration) into note lengths.

When a pattern is played, an object called [EventStreamPlayer](../../Classes/EventStreamPlayer.md) is created. This object reads out the events one by one from the pattern's stream (using a given event prototype as the base), and calls `play` on each. The `'delta'` value in the event determines how many beats to wait until the next event. Play continues until the pattern stops producing events, or you call .stop on the EventStreamPlayer. (Note that calling `.stop` on the pattern does nothing. Patterns are stateless and cannot play or stop by themselves.)


> **Note:** **To sum up so far** : A Pbind's stream generates Events. When an Event is played, it does some work that usually makes noise on the server. This work is defined in an event prototype. The Event class provides a default event prototype that includes powerful options to create and manipulate objects on the server.



### Rests
Rests may be indicated in three ways.

- **Recommended**- *Rest:* An instance of [Rest](../../Classes/Rest.md) that marks the event as a rest.

- **Legacy**- *Symbol as pitch:* A symbol, such as **\rest**, **\r** or even the empty symbol **\**, in a key related to pitch (degree, note, midinote, freq) causes the event to be silent.
- *\type, \rest:* Setting the event's \type to \rest also silences the event.



A more complete discussion is found in the [Rest](../../Classes/Rest.md) help file.




### Useful Pbind variant: Pmono
Pbind plays separate notes by default. Sometimes, you might need a pattern to act more like a monophonic synthesizer, where it plays just one Synth node and changes its values with each event. If Pbind normally corresponds to `Synth.new` or `/s_new`, [Pmono](../../Classes/Pmono.md) corresponds to `aSynth.set` or `/n_set`.

Compare the sound of these patterns. Pbind produces an attack on every note, while Pmono glides from pitch to pitch.


```
p = Pbind(\degree, Pwhite(0, 7, inf), \dur, 0.25, \legato, 1).play;
p.stop;

p = Pmono(\default, \degree, Pwhite(0, 7, inf), \dur, 0.25).play;
p.stop;
```


Articulating phrases is possible with Pmono by chaining several Pmono patterns together in a row, or by using [PmonoArtic](../../Classes/PmonoArtic.md).





## Connecting Event values to SynthDef inputs
Most SynthDefs have [Control](../../Classes/Control.md) inputs, usually defined by arguments to the UGen function. For example, the default SynthDef (declared in Event.sc) defines five inputs: `out`, `freq`, `amp`, `pan` and `gate`.


```
SynthDef(\default, { arg out=0, freq=440, amp=0.1, pan=0, gate=1;
    var z;
    z = LPF.ar(
            Mix.new(VarSaw.ar(freq + [0, Rand(-0.4,0.0), Rand(0.0,0.4)], 0, 0.3)),
            XLine.kr(Rand(4000,5000), Rand(2500,3200), 1)
        ) * Linen.kr(gate, 0.01, 0.7, 0.3, 2);
    OffsetOut.ar(out, Pan2.ar(z, pan, amp));
}, [\ir]);
```


When an event plays a synth, any values stored in the event under the same name as a SynthDef input will be passed to the new synth. Compare the following:


```
// Similar to Synth(\default, [freq: 293.3333, amp: 0.2, pan: -0.7])
(freq: 293.3333, amp: 0.2, pan: -0.7).play;

// Similar to Synth(\default, [freq: 440, amp: 0.1, pan: 0.7])
(freq: 440, amp: 0.1, pan: 0.7).play;
```


This leads to a key point: **The names that you use for patterns in Pbind should correspond to the arguments in the SynthDef being played**. The Pbind pattern names determine the names for values in the resulting Event, and those values are sent to the corresponding Synth control inputs.

The SynthDef to play is named by the `'instrument'` key. To play a pattern using a different Synth, simply name it in the pattern.


```
SynthDef(\harpsi, { |outbus = 0, freq = 440, amp = 0.1, gate = 1|
    var out;
    out = EnvGen.ar(Env.adsr, gate, doneAction: Done.freeSelf) * amp *
        Pulse.ar(freq, 0.25, 0.75);
    Out.ar(outbus, out ! 2);
}).add;    // see below for more on .add

p = Pbind(
        // Use \harpsi, not \default
    \instrument, \harpsi,
    \degree, Pseries(0, 1, 8),
    \dur, 0.25
).play;
```


It's actually an oversimplification to say that the Pbind names should always match up to SynthDef arguments.

- A Pbind can use some values in the event for intermediate calculations (see [A-Practical-Guide/PG_06g_Data_Sharing](../../Tutorials/A-Practical-Guide/PG_06g_Data_Sharing.md)). If these intermediate values have names not found in the SynthDef, they are not sent to the server. There is no requirement that every item in an Event must correspond to a SynthDef control.
- The default event prototype performs some automatic conversions. You might have noticed that the examples so far use `'degree'` to specify pitch, but the default SynthDef being played does not have a degree argument. It works because the default event converts degree into `'freq'`, which is an argument. The most important conversions are for pitch and timing. Timing is simple; pitch is more elaborate. See [A-Practical-Guide/PG_07_Value_Conversions](../../Tutorials/A-Practical-Guide/PG_07_Value_Conversions.md) for an explanation of these automatic calculations.


**Don't send or load SynthDefs; use .add or .store instead**

To send only the relevant values to the new Synth, the Event needs to know what controls exist in the SynthDef. This is done by a library of descriptors for SynthDefs; the descriptor is a [SynthDesc](../../Classes/SynthDesc.md), and the library is a [SynthDescLib](../../Classes/SynthDescLib.md). The normal methods -- `.send(s)`, `.load(s)` -- to communicate a SynthDef to the server do not enter it into the library. As a result, SynthDefs sent this way will not work properly with Pbind. Instead, use different methods that *store* the SynthDef into the library.


```
// Save into the library, write a .scsyndef file, and load it on the server
SynthDef(...).store;

// Save into the library and send the SynthDef to the server (no .scsyndef file)
// Make sure the server is booted before doing this
SynthDef(...).add;
```


.load(s) --> .store

.send(s) --> .add



## Rest events
Beginning with version 3.5, rests may be indicated using instances of [Rest](../../Classes/Rest.md).

- Rests may be given in any Pbind key-value pair. (Previously, rests could be indicated only in \type, \degree, \note, \midinote or \freq.)
- A rest has a value, e.g. `Rest(0.5)`, and will pass transparently through calculations.
- Addresses some problems with the former convention (to be discussed in brief below).


Ligeti's "touches bloquées" technique could be written this way (see [A-Practical-Guide/PG_06e_Language_Control](../../Tutorials/A-Practical-Guide/PG_06e_Language_Control.md) for an explanation of the conditional [Pif](../../Classes/Pif.md)):


```
(
// first, pitches ascending by 1-3 semitones, until 2 octaves are reached
var    pitches = Pseries(0, Pconst(24, Pwhite(1, 3, inf)), inf).asStream.all,
        // randomly block 1/3 of those
    mask = pitches.scramble[0 .. pitches.size div: 3];

p = Pbind(
    \arpeg, Pseq(pitches[ .. pitches.size - 2] ++ pitches.reverse[ .. pitches.size - 2], inf),
        // if the note is found in the mask array, replace it with Rest
        // then that note does not sound
    \note, Pif(Pfunc { |event| mask.includes(event[\arpeg]) }, Rest(0), Pkey(\arpeg)),
    \octave, 4,
    \dur, 0.125
).play;
)

p.stop;
```



> **Note:** In 3.9, it is no longer supported to use the Rest class in patterns. All rests need to have a value, e.g. `Rest(0)`. Rest objects now support math operators. That is, you can now write `Pseq([1, 2, Rest(0)], inf) * 2` *and* `[1, 2, Rest(0)] * 2`. (Prior to 3.9, the former usage was supported, but only in Pbind, and the latter usage was not supported at all.)


The older convention for rests is to set the `\freq` key to a [Symbol](../../Classes/Symbol.md). Commonly this is `\rest`, but a backslash by itself is enough to suppress the note on the server. (This usage is still supported, but not recommended because it is limited to pitch-related keys only.)

If it's the `\freq` key that determines whether the event as a rest or not, why does it work to use it with `\note`? As noted, keys like `\degree`, `\note`, and `\midinote` are automatically converted into frequency. The math operations that perform the conversion preserve Symbols intact -- e.g., `\rest + 1 == \rest` . So the `\rest` value is passed all the way through the chain of conversions so that `\freq` in the event ends up receiving `\rest`.

Note that it doesn't matter if the SynthDef has a `freq` argument. It's the event, on the *client* side, that looks to this key to determine whether to play the note or not. If it is a rest, the server is not involved at all.



## Writing SynthDefs for patterns
SynthDefs should have a couple of specific features to work well with patterns.


### Synths should release themselves
The default event prototype relies on the synth to remove itself from the server when it's finished. This can be done in several ways:

- (Most typical) A gated envelope with a releasing `doneAction` ( >= 2) in the envelope generator (see [Done](../../Classes/Done.md) for a complete list). The `\harpsi` SynthDef above uses this technique. A gated envelope specifies a release node or uses one of the predefined sustaining envelope types: `Env.asr`, `Env.adsr`, `Env.dadsr`. The [Env](../../Classes/Env.md) help file offers more detail on gated envelopes.
- `Linen.kr`, which is a shortcut for `EnvGen.kr(Env([0, susLevel, 0], [attackTime, releaseTime], \lin, releaseNode: 1), gate, doneAction: [2 or higher])`. The default SynthDef uses this. The `doneAction` should be at least 2 to release the node.
> **Note:** If the release is controlled by a gate, the gate must be represented by the synth argument `gate`; standard event prototypes expect to be able to control the synth's release using this argument. Also, make sure the gate's default value is greater than 0. Otherwise, the envelope will never start and you will both hear nothing and watch synths pile up on the server.


- Fixed-duration envelopes (no gate).





### Argument name prefixes
One other subtle point about synth argument names. In a SynthDef, argument names can have the prefix `t_` to indicate a "trigger control," or `i_` for an "initial rate" control (meaning that it holds the value set when the Synth is first played). This is described in [SynthDef](../../Classes/SynthDef.md) help. Pbind and its cousins should leave out the prefixes, e.g.:


```
(
SynthDef(\trig_demo, { |out, freq = 440, gate = 1, t_trig = 1|    // t_trig here
    var    env = Decay2.kr(t_trig, 0.01, 0.1),
        sig = SinOsc.ar(freq, 0, env)
            * Linen.kr(gate, 0.01, 0.1, 0.1, doneAction: Done.freeSelf);
    Out.ar(out, sig ! 2)
}).add;
)

(
p = Pmono(\trig_demo,
    \freq, Pexprand(200, 800, inf),
    \trig, 1,    // note that this is NOT t_trig -- just \trig
    \delta, 0.125
).play;
)

p.stop;
```


Previous: [A-Practical-Guide/PG_02_Basic_Vocabulary](../../Tutorials/A-Practical-Guide/PG_02_Basic_Vocabulary.md)

Next: [A-Practical-Guide/PG_04_Words_to_Phrases](../../Tutorials/A-Practical-Guide/PG_04_Words_to_Phrases.md)





