# Pbind

*combine several value patterns to one event stream by binding keys to values*

**Related:** [Pattern](../Classes/Pattern.md), [Event](../Classes/Event.md), [Pmono](../Classes/Pmono.md), [Rest](../Classes/Rest.md)

**Categories:** Streams-Patterns-Events>Patterns>Event

## Description

Pbind combines several value streams into one event stream. Each value stream is assigned to one or more keys in the resulting event stream. It specifies a stream of **Events** in terms of different patterns that are **bound** to different keys in the Event. The patterns bound to keys are referred to as *value patterns* and the Pbind itself is termed an event pattern.
The keys used in a Pbind are usually determined by [Event](../Classes/Event.md)'s default mechanism and the controls defined for the [SynthDef](../Classes/SynthDef.md) to be played. (See [#SynthDef and Event](#synthdef-and-event) below for a brief discussion of both in relation to Pbind.)


## Class Methods

### `new`
The arguments to Pbind are an alternating sequence of keys and patterns.
```supercollider
Pbind(\note, Pseq([0, 4, 7]), \amp, 0.1, \dur, 0.2).play
```

The message `new` converts keyword arguments into key value pairs, so that we can write:
```supercollider
Pbind(note: Pseq([0, 4, 7]), amp: 0.1, dur: 0.2).play
```

A pattern can also be bound to an array of keys. In this case, the pattern must specify a sequence whose elements are arrays with at least as many elements as there are keys.
```supercollider
Pbind([\note, \amp], Pseq([[0, 0.05],  [4, 0.5],  [7, 0.1]]), dur: 0.2).play
```



## Instance Methods

### `patternpairs`
The defined key value pairs mapping symbols to value patterns.
```supercollider
Pbind(x:7, y:Pseq([1, 2, 3])).patternpairs
```

### `embedInStream`
From within a [Stream](../Classes/Stream.md) like e.g. [Routine](../Classes/Routine.md), yield all events from this pattern before continuing. One pattern can be used to produce values for any number of independent streams.**Arguments:**

| Argument | Description |
|----------|-------------|
| `inevent` | An event that is passed into all substreams and is used by them to produce the output events.
```supercollider
a = Pbind(note: Pseq([0, 4, 7]), amp: 0.1, dur: 0.2);
r = Routine { |inevent| (note:9, dur: 1).yield;  a.embedInStream(inevent);  };
r.nextN(5, (x:7)); // passing in an event for the next 5 values from r, \x of 7 is passed through the Pbind stream
``` |  

## Examples


```supercollider
(
a = Pbind(
    x:    Pseq([1, 2, 3]),
    y:    Prand([100, 300, 200], inf),
    zzz:  99
);
x = a.asStream;
)

x.next(()); // pass in an event ()
x.next(());
x.next(());
x.next(()); // end: nil
```



```supercollider
// sound examples

// using the default synth def
Pbind(
    freq: Prand([300, 500, 231.2, 399.2], inf),
    dur:  0.1
).play;

Pbind(
    freq: Prand([300, 500, 231.2, 399.2], inf),
    dur:  Prand([0.1, 0.3], inf)
).play;

Pbind(
    freq: Prand([1, 1.2, 2, 2.5, 3, 4], inf) * 200,
    dur:  0.1
).play;
```


The keys can be specified as keyword arguments, as above, or as a sequence of keys to patterns provided as arguments. Additionally, when an array of keys is provided, the pattern with be unpacked into two streams (see following example). However, this does not work when using keyword arguments, and therefore must go before them. For historical reasons, you are more likely to see the sequence of keys to patterns rather than keyword arguments.

```supercollider
// Both of these do the same thing.
Pbind(a: Pseq([1, 2, 3]), dur: 1).trace.play
Pbind(\a, Pseq([1, 2, 3]), \dur, 1).trace.play


(
// a SynthDef
SynthDef(\test, {
    |out, freq = 440, amp = 0.1, nharms = 10, pan = 0, gate = 1|
    var audio = Blip.ar(freq, nharms, amp);
    var env = Linen.kr(gate, doneAction: Done.freeSelf);
    OffsetOut.ar(out, Pan2.ar(audio, pan, env));
}).add;
)

// Assignment to multiple keys using an Array.
// Must come before any keyword arguments.
Pbind(
    [\freq, \sustain], Ptuple([
                          Pseq((1..16) * 50, 4),
                          Pseq([1/10, 0.5, 1, 2], inf)
                       ]),
    instrument:        \test,
    nharms:            Pseq([4, 10, 40], inf),
    dur:               Pseq([1, 1, 2, 1]/10, inf),
).play
```



### SynthDef and Event
The keys used in a Pbind are determined by the [SynthDef](../Classes/SynthDef.md) used and the structure of the extensive default mechanism provided by [Event](../Classes/Event.md). This section provides a brief review of both.

A [SynthDef](../Classes/SynthDef.md) assigns a name to an interconnection of unit generators to be run as a synth on a server. It also assigns **control names** to the synth's control inputs. In the following example the SynthDef \test has control inputs **out**, **freq**, **amp**, **nharms**, **pan**, and **gate**.


```supercollider
SynthDef(\test, { |out, freq = 440, amp = 0.1, nharms = 10, pan = 0, gate = 1|
    var audio = Blip.ar(freq, nharms, amp);
    var env = Linen.kr(gate, doneAction: Done.freeSelf);
    OffsetOut.ar(out, Pan2.ar(audio, pan, env));
}).add;
```


The SynthDef needs to be downloaded to the server upon which it is to be run. Use **.add** instead of .send to ensure that any patterns using this SynthDef have information about the available control inputs (see [SynthDesc](../Classes/SynthDesc.md)). Alternately, **.store** may be used to save the SynthDef to disk and add the SynthDesc to the library.

An [Event](../Classes/Event.md) is a Dictionary that specifies an action to be taken in response to **play** and a time increment to be returned in response to **delta**. Events can be written as a series of key value pairs enclosed in parentheses. Empty parentheses create an empty event.

By default, Events play synths on a server. Such *note events* use the following keys:


**instrument (\default)**
: The synthdef to be played

**variant (nil, optional)**
: The set of variant control defaults to use (see [SynthDef](../Classes/SynthDef.md))

**server (Server.default)**
: The server that plays the synth

**group (1)**
: The new synth's or the synth the new synth is placed before or after

**addAction (0)**
: How the synth is placed relative to the target specified by **group**
**0**
: head of group

**1**
: tail of group

**2**
: before group (could be a Synth)

**3**
: after group (could be a Synth)

**delta (function)**
: The time until the next event in a sequence of events, generally specified indirectly through **dur**



When the Event is played, it creates an OSC command to play a synth. It uses the name assigned to **instrument** to the select the SynthDef to be played. The SynthDef's control names (found in its [SynthDesc](../Classes/SynthDesc.md)) are looked up in the event and the corresponding values included in the command.

Playing a synth is the normal action taken by an Event. The default event structure defines several other event types that can perform a wide variety of server actions. See the [Event](../Classes/Event.md) help file for a list of event types.

There are a number of conventional names typically used to identify controls in a synth.


**out**
: output bus index

**in**
: input bus index (for filters, modulators, etc)

**gate**
: envelope gate (not level!) - should default to 1.0, deletes synth when released

**trig**
: envelope gate (not level!) - should default to 1.0, does not delete synth when released

**pan**
: panning position

**bufnum**
: buffer number (used in synths that utilize [PlayBuf](../Classes/PlayBuf.md), [DiskIn](../Classes/DiskIn.md), etc)

**sustain**
: duration of the synth

**amp**
: amplitude of the synth

**freq**
: base pitch of the synth



Event implements a layered specification scheme for some of these controls. In the following list, the first and leftmost name is the actual control name, names below and indented are more abstract ways to specify the control.


**delta**
: The time until the next event. Generally determined by:
**dur**
: The time until next event in a sequence of events

**stretch**
: Scales event timings (i.e. stretch == 2 => durations are twice as long)

**sustain**
: Duration of the synth, typically determined (in stretched time units) by:
**legato**
: The ratio of the synth's duration to the event's duration

**amp**
: synth amplitude (typically ranging from 0 to 1), often determined by
**db**
: Amplitude in decibels

**detunedFreq**
: actual "pitch" of a synth, determined by:
**freq + detune;**
: freq is determined by:
**(midinote + ctranspose).midicps * harmonic;**
: midinote is determined by:
**(note + gtranspose + root)/stepsPerOctave * octave * 12;**
: note is determined by:
**(degree + mtranspose).degreeToKey(scale, stepsPerOctave)**
:




```supercollider
(
// the SynthDef
SynthDef(\test, { |out, freq = 440, amp = 0.1, nharms = 10, pan = 0, gate = 1|
    var audio = Blip.ar(freq, nharms, amp);
    var env = Linen.kr(gate, doneAction: Done.freeSelf);
    OffsetOut.ar(out, Pan2.ar(audio, pan, env));
}).add;

// Events are written as parantheses enclosing key/value pairs
(instrument: \test).play;
(instrument: \test, freq: 20, nharms: 50).play;
)
```




### Rests
See [Rest](../Classes/Rest.md) for a discussion of marking events as rests in Pbind.



### The Play Method
While the play method is actually defined in the class [Pattern](../Classes/Pattern.md), it is useful to review it here:


**play (clock, protoEvent, quant)**
: returns an [EventStreamPlayer](../Classes/EventStreamPlayer.md).

**clock**
: The clock that schedules the EventStreamPlayer, defaults to TempoClock.default. Patterns that change graphics must use [AppClock](../Classes/AppClock.md).

**protoEvent**
: The initial event modified by Pbind, defaults to Event.default.

**quant**
: A quantization value used by clock. When a number, the pattern will start at the next even multiple of that number. May also be a [Quant](../Classes/Quant.md), which specifies quantization, time position within that quantization, and a timingOffset. See [Quant](../Classes/Quant.md) for details.





### Realtime Control with EventStreamPlayer
The [EventStreamPlayer](../Classes/EventStreamPlayer.md) provides realtime control through **mute**, **unmute**, **stop**, **play** and **reset**.


```supercollider
(
SynthDef(\cfstring1, { |i_out, freq = 360, gate = 1, pan, amp = 0.1|
    var out, eg, fc, osc, a, b, w;
    fc = LinExp.kr(LFNoise1.kr(Rand(0.25, 0.4)), -1, 1, 500, 2000);
    osc = Mix.fill(8, { LFSaw.ar(freq * [Rand(0.99, 1.01), Rand(0.99, 1.01)], 0, amp) }).distort * 0.2;
    eg = EnvGen.kr(Env.asr(1, 1, 1), gate, doneAction: Done.freeSelf);
    out = eg * RLPF.ar(osc, fc, 0.1);
    #a, b = out;
    Out.ar(i_out, Mix.ar(PanAz.ar(4, [a, b], [pan, pan+0.3])));
}).add;

e = Pbind(
    \degree, Pseq((0..12), inf),
    \dur, 0.2,
    \instrument, \cfstring1
).play; // returns an EventStream
)

( // an interactive session
e.stop
e.play
e.reset

e.mute; // keeps playing, but replaces notes with rests

e.unmute;

e.reset; // reset the stream.
e.reset; // reset the stream.
e.reset; // reset the stream.
e.reset; // reset the stream.

e.pause; // will resume where paused.

e.play;

e.stop; // will reset before resume.

e.play;
)
```


In addition, the stream the EventStreamPlayer plays can be altered while it is running through the method **stream_(aStream)**.


```supercollider
(
e.stream = Pbind(
    \degree, Pseq([0, 1, 2, 4, 6, 3, 4, 8], inf),
    \dur, Prand([0.2, 0.4, 0.8], inf),
    \amp, 0.05, \octave, 5,
    \instrument, \cfstring1, \ctranspose, 0
).asStream;
)

(
e.stream = Pbind(
    \degree, Pseq([0, 1, 2, 4, 6, 3, 4, 8], inf),
    \dur, Prand([0.2, 0.4, 0.8], inf),
    \amp, 0.05, \octave, 5,
    \instrument, \cfstring1, \ctranspose, 0
).asStream;
)

(
e.stream = Pbind(
    \degree, Pxrand([0, 1, 2, 4, 6, 3, 5, 7, 8], inf),
    \dur, Prand([0.2, 0.4, 0.8], inf), \amp, 0.05,
    \octave, 5, \instrument, \cfstring1
).asStream;
)
```




### Additional arguments
Here is an example with more bindings. Here we have added a filter with cutoff and resonance arguments. You will need to hit command '.' before executing the next few pbind ex. without having them stack up. also, due to the synthdef's and synthdeclib, if the server is shut down you will have to reload the synthdef and re-read the synthdesclib.


```supercollider
(
SynthDef(\acid, { |out, freq = 1000, gate = 1, pan = 1, cut = 4000, rez = 0.8, amp = 1|
    Out.ar(out,
        Pan2.ar(
            RLPF.ar(
                Pulse.ar(freq, 0.05),
            cut, rez),
        pan) * EnvGen.kr(Env.linen(0.01, 1, 0.3), gate, amp, doneAction: Done.freeSelf);
    )
}).add;
)

(
Pbind(\instrument, \acid, \dur, Pseq([0.25, 0.5, 0.25], inf), \root, -12,
    \degree, Pseq([0, 3, 5, 7, 9, 11, 5, 1], inf), \pan, Pfunc({ 1.0.rand2 }),
    \cut, Pxrand([1000, 500, 2000, 300], inf), \rez, Pfunc({ 0.7.rand +0.3 }), \amp, 0.2).play;
)
```


The [ListPattern](../Classes/ListPattern.md)s can be put around Event Streams to create sequences of Event Streams.


```supercollider
(
Pseq([
    Pbind(\instrument, \acid, \dur, Pseq([0.25, 0.5, 0.25], 4), \root, -24,
        \degree, Pseq([0, 3, 5, 7, 9, 11, 5, 1], inf), \pan, Pfunc({ 1.0.rand2 }),
        \cut, Pxrand([1000, 500, 2000, 300], inf), \rez, Pfunc({ 0.7.rand +0.3 }), \amp, 0.2),

    Pbind(\instrument, \acid, \dur, Pseq([0.25], 6), \root, -24, \degree, Pseq([18, 17, 11, 9], inf),
        \pan, Pfunc({ 1.0.rand2 }), \cut, 1500, \rez, Pfunc({ 0.7.rand +0.3 }), \amp, 0.16)

], inf).play;
)
```


'Pseq' in the above ex. can be any pattern object:


```supercollider
(
Prand([
    Pbind(\instrument, \acid, \dur, Pseq([0.25, 0.5, 0.25], 4), \root, -24,
        \degree, Pseq([0, 3, 5, 7, 9, 11, 5, 1], inf), \pan, Pfunc({ 1.0.rand2 }),
        \cut, Pxrand([1000, 500, 2000, 300], inf), \rez, Pfunc({ 0.7.rand +0.3 }),
        \amp, 0.2),

    Pbind(\instrument, \acid, \dur, Pseq([0.25], 6), \root, -24, \degree, Pseq([18, 17, 11, 9], inf),
        \pan, Pfunc({ 1.0.rand2 }), \cut, 1500, \rez, Pfunc({ 0.7.rand +0.3 }), \amp, 0.16)

], inf).play;
)
```




### Multichannel Expansion
If we supply an array for **any** argument, the synth node will automatically replicate to handle the additional arguments.

The only **exception** to this is: `\instrument` and `\dur`. For the general schema, see also: [Multichannel-Expansion](../Guides/Multichannel-Expansion.md).


```supercollider
// When we provide the 'root' argument an array, we should hear a chord.
// the synth def is defined above
(
Pbind(
    \instrument, \acid, \dur, Pseq([0.25, 0.5, 0.25], inf),
    \root, [-24, -17], // expand root
    \degree, Pseq([0, 3, 5, 7, 9, 11, 5, 1], inf),
    \pan, Pfunc { 1.0.rand2 },
    \cut, Pxrand([1000, 500, 2000, 300], inf),
    \rez, Pfunc { 0.7.rand + 0.3 },
    \amp, 0.2).play;
);

// multiple arrays are correlated in parallel, the shorter one wraps:
(
Pbind(
    \instrument, \acid,
    \dur, Pseq([0.25, 0.5, 0.25], inf),
    \root, [-24, -17], // expand root ...
    \degree, Pseq([0, 3, 5, 7, 9, 11, 5, 1], inf) + [0, 6, 9], // ... and expand degrees
    \pan, Pfunc { 1.0.rand2 },
    \cut, Pxrand([1000, 500, 2000, 300], inf),
    \rez, Pfunc { 0.7.rand + 0.3 },
    \amp, 0.2).play;
);
```



> **Note:** In Pbind, you can’t have arrays of patterns, but only patterns that **return** arrays.



```supercollider
// so this does not expand:
Pbind(\degree, [Pseq([0, 2, 3], inf), Pseq([2, 4, 5, 6], inf)]).play;

// but this does:
Pbind(\degree, Pseq([[0, 2], [2, 4], [3, 5], [0, 6]], inf)).play;
```



```supercollider
// transform an array of patterns into a pattern that returns arrays, use Ptuple:
a = [Pseq([1, 2, 3], inf), Prand([100, 299, 399], inf), Pseries(0, 6, inf)];
b = Ptuple(a);
b.asStream.nextN(8)
```



```supercollider
Pbind(\degree, Ptuple([Pseq([0, 2, 3], inf), Pseq([2, 4, 5, 6], inf)])).play;
```



```supercollider
// an example: instead of \degree, [p1, p2] you write \degree, Ptuple([p1, p2])
(
Pdef(\x,
    Pbind(
        \instrument, \test,
        \legato, 0.2,
        \degree, Ptuple([0, Pwalk(Scale.hijaz.degrees, Prand([1, -1], inf))]),
        \scale, Scale.hijaz,
        \strum, 0.05
    )
).play;
)
```




### Experimenting with Patterns
Using [Pdef](../Classes/Pdef.md) (provided by [JITLib](../Overviews/JITLib.md)) makes it easy to replace patterns on the fly:


```supercollider
(
Pdef(\buckyball).play;
)

(
Pdef(\buckyball, Pbind(\instrument, \acid, \dur, Pseq([0.25, 0.5, 0.25], inf), \root, [-24, -17],
    \degree, Pseq([0, 3, 5, 7, 9, 11, [5, 17], 1], inf), \pan, Pfunc({ [1.0.rand2, 1.0.rand2] }),
    \cut, Pxrand([1000, 500, 2000, 300], inf), \rez, Pfunc({ 0.7.rand +0.3 }), \amp, [0.15, 0.22]));
)
(
Pdef(\buckyball, Pbind(\instrument, \acid, \dur, Pseq([0.25, 0.5, 0.25], inf), \root, [-24, -17],
    \degree, Pseq([0b, 3b, 5b, 7b, 9b, 11b, 5b, 0b], inf), \pan, Pfunc({ 1.0.rand2 }), // notice the flats
    \cut, Pxrand([1000, 500, 2000, 300], inf), \rez, Pfunc({ 0.7.rand +0.3 }), \amp, 0.2));
)

// stop the Pdef
Pdef(\buckyball).stop;

// start the Pdef
Pdef(\buckyball).resume;

// removing the Pdef
Pdef.remove(\buckyball);
```




### Sending to effects
Assignment to effect processors can be achieved by setting the 'out' argument to the desired efx's input bus. The effect Synth must also be created. Synth.new is one way of doing this.


```supercollider
(
// efx synthdef- dig the timing on the delay and the pbind. :-P
SynthDef(\pbindefx, { |out, in, time1 = 0.25, time2 = 0.5|
    var audio, efx;
    audio = In.ar([20, 21], 2);
    efx = CombN.ar(audio, 0.5, [time1, time2], 10, 1, audio);
    Out.ar(out, efx);
}).add;

// create efx synth
a = Synth.after(1, \pbindefx);

// if you don't like the beats change to 0.4, 0.24
// a.set(\time1, 0.4, \time2, 0.24);

SynthDef(\acid, { |out, freq = 1000, gate = 1, pan = 0, cut = 4000, rez = 0.8, amp = 1|
    Out.ar(out,
        Pan2.ar(
            RLPF.ar(
                Pulse.ar(freq, 0.05),
            cut, rez),
        pan) * EnvGen.kr(Env.linen(0.02, 1, 0.3), gate, amp, doneAction: Done.freeSelf);
    )
}).add;
)

(
Pbind(\instrument, \acid, \out, 20, \dur, Pseq([0.25, 0.5, 0.25], inf), \root, [-24, -17],
    \degree, Pseq([0, 3, 5, 7, 9, 11, 5, 1], inf), \pan, Pfunc({ 1.0.rand2 }),
    \cut, Pxrand([1000, 500, 2000, 300], inf), \rez, Pfunc({ 0.7.rand +0.3 }), \amp, 0.12).play;
)
```




### Additional examples

```supercollider
(
SynthDef(\berlinb, { |out = 0, freq = 80, amp = 0.01, pan = 0, gate = 1|
    var synth, env;
    env = Decay2.kr(gate, 0.05, 8, 0.0003);
    synth = RLPF.ar(
        LFPulse.ar(freq, 0, SinOsc.kr(0.12, [0, 0.5pi], 0.48, 0.5)),
        freq * SinOsc.kr(0.21, 0, 18, 20),
        0.07
    );
    #a, b = synth*env;
    DetectSilence.ar(a, 0.1, doneAction: Done.freeSelf);
    Out.ar(out, amp * Mix.ar(PanAz.ar(4, [a, b], [pan, pan+1])));
}).add;
)

(
f = Pbind(
    \degree, Pseq([0, 1, 2, 4, 6, 3, 4, 8], inf),
    \dur, 0.5, \octave, 3, \instrument, \berlinb
).play;
)

(
f.stream = Pbind(
    \degree, Pseq([0, 1, 2, 4, 6, 3, 4, 8], inf),
    \dur, 0.5, \octave, [2, 1],
    \instrument, \berlinb,
    \pan, Pfunc({ 1.0.rand2 })
).asStream;
)
```






