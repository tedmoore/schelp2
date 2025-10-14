# EventPatternProxy

*event stream reference*

**Categories:** JITLib>Patterns, Live Coding

**Related:** [Pdef](../Classes/Pdef.md)

## Description

Keeps a reference to a stream that can be replaced while in use.


## Class Methods

### `new`
create a new instance with a pattern (the source). The pattern should be an *event pattern* (see [Pdef](../Classes/Pdef.md))
### `default`
a default source, if none is given. the default is a Pbind with resting notes of 1.0 beat duration.
### `defaultQuant`
set the default quantization value for the class.

## Instance Methods

### `source`
set the source (a pattern). If a quantization is given, schedule this change to the next beat (**pattern_**(..) is equivalent)### `clear`
set the source to nil and stop playing### `clock`
get or set the instance's default clock, used by [play](#play) if no other clock is specified. Defaults to TempoClock.default.### `quant`
get or set the quantization value. can be an array [quant, phase, offset, outset]### `fadeTime`
when the synthdefs that are used contain an `\amp` control, the patterns are replaced by crossfading the previous with the new over this time (in beats)### `envir`
provide a default event for the Pdef. It is used to filter the incoming stream before it is passed to the source pattern. This is similar to [NodeProxy#-nodeMap](../Classes/NodeProxy.md#-nodemap). When set for the first time, the pattern is rebuilt.### `set`
set arguments in the default event. If there is none, it is created and the pattern is rebuilt.
### a) using as stream reference
### `embedInStream`
Given a [Stream](../Classes/Stream.md) like e.g. [Routine](../Classes/Routine.md), yield all values from the pattern in the proxy before continuing. One pattern proxy can be used to produce values for any number of independent streams.**Arguments:**

| Argument | Description |
|----------|-------------|
| `inval` | The inval is an [Event](../Classes/Event.md) and is passed into all substreams. It can be used to control how they behave from the outside. |  
| `embed` | See [Object#-streamArg](../Classes/Object.md#-streamarg) for explanation. |  
| `default` | Replacement for `nil` outputs of the source pattern. One use case is [endless](#endless).
```supercollider
a = EventPatternProxy.new;
a.source = Pbind(\freq, Pgeom(100, Pwhite(1.01, 1.2), 4));
r = Routine { |inval| loop { a.embedInStream(inval) } };
r.nextN(12, ()); // the next 12 values from r
a.source = Pbind(\freq, Pgeom([100, 200], Pwhite(1.01, 1.2), 4)); // replace the source
r.nextN(12, ()); // the next 12 values from r
``` |  


### b) using as EventStreamPlayer
### `play`
starts the EventPatternProxy and creates a player. if you want to play multiple instances, use [fork](#fork).**Arguments:**

| Argument | Description |
|----------|-------------|
| `argClock` | play on a certain clock, e.g. a [TempoClock](../Classes/TempoClock.md). If nil uses this instance's [clock](#clock), which in turn defaults to TempoClock.default. |  
| `protoEvent` | an event to be used as a first input to the chain |  
| `quant` | can be an array of [quant, phase, offset, outset], or an instance of [Quant](../Classes/Quant.md). |  
| `doReset` | if set to true, play will restart the stream if already running (a [Boolean](../Classes/Boolean.md)).
```supercollider
// using a protoEvent
Pdef(\x, Pbind(\dur, 0.1));
Pdef(\x).trace.play(protoEvent: (freq: 1000));
```


```supercollider
// using a different clock: here a Scheduler
Pdef(\x, Pbind(\dur, Pwhite(0.1, 0.2, inf), \count, Pseries()));
a = Scheduler(TempoClock.default);
Pdef(\x).trace.play(a);
a.advance(0.2);
``` |  

### `stop`
stops the player
### `player`
the current player (if the Pdef is simply used in other streams this is `nil`)
### `pause`, `resume`, `reset`
perform player method
### `isPlaying`
returns true if Pdef is running. if a Pdef is playing and its stream ends, it will schedule a stream for playing as soon as a new one is assigned to it.

## Examples


### a) embedding EventPatternProxy in streams

```supercollider
(
SynthDef("Pdefhelp", {
    arg out, freq, sustain = 1, amp = 0.1, pan;
    var env, u = 1;
    env = EnvGen.kr(Env.perc(0.03, sustain), 1, doneAction: Done.freeSelf);
    5.do { var d; d = exprand(0.01, 1); u = SinOsc.ar(d * 300, u, rrand(0.1, 1.2) * d, 1) };
    Out.ar(out, Pan2.ar(SinOsc.ar(u + 1 * freq, 0, amp * env), pan));
}).add;
)
s.boot;

#a, b, c, m = { EventPatternProxy.new } ! 4;

m.play;
m.source = Pbind(\instrument, \Pdefhelp, \dur, 1, \degree, 16, \legato, 0.1);

a.source = Pbind(\instrument, \Pdefhelp, \dur, 0.25, \degree, Pseq(#[0, 5, 4, 3]));
b.source = Pbind(\instrument, \Pdefhelp, \dur, 0.125, \degree, Pseq(#[7, 8, 7, 8]));
c.source = Pbind(\instrument, \Pdefhelp, \dur, 0.25, \degree, Pseq(#[0, 1, 2], 2));

x = Pseq([a, b, c], inf).play;


c.source = Pbind(\instrument, \Pdefhelp, \dur, 0.25, \degree, Pseq(#[4, 3, 1, 2]*3));


// infinite loops are scheduled (to ths clock's next beat by default) and released:

a.source = Pbind(\instrument, \Pdefhelp, \dur, 0.753, \degree, Pseq(#[0, 5, 4, 3, 2], inf));
a.source = Pbind(\instrument, \Pdefhelp, \dur, 0.125, \degree, Pseq(#[0, 5, 4, 3] + 1, 1));
a.source = Pbind(\instrument, \Pdefhelp, \dur, 0.25, \degree, Pseq(#[0, 5, 4, 3] - 1, 1));

a.source = Pbind(\instrument, \Pdefhelp, \dur, 0.125, \degree, Pseq(#[0, 5] - 1, 1));
a.source = Pbind(\instrument, \Pdefhelp, \dur, 0.753, \degree, Pshuf(#[0, 5, 4, 3, 2], inf));

x.stop;
m.stop;

// EventPatternProxy can be used in multiple patterns

(
x = Ppar([
    Pbindf(Pn(a, inf),
        \gtranspose, Pdup(8, Pseq(#[0, 2, 0, 3], inf))
    ),
    Pbindf(Pn(a, inf),
        \gtranspose, Pdup(8, Pseq(#[7, 4, 0, 3], inf)),
        \dur, 0.6
    ),
    Pbindf(Pn(a, inf),
        \degree, Pseq(#[0, 5, 4, 3, 2, 3, 2], 1)
    )
]).play;
)

a.source = Pbind(\instrument, \Pdefhelp, \dur, 0.1, \degree, Pseq(#[0, 1, 0, 1, 2], inf));

a.source = Pbind(\instrument, \Pdefhelp, \dur, 0.2, \degree, Pseq([0, 4], inf));

a.source = Pbind(\instrument, \Pdefhelp, \dur, 0.2, \degree, Pseq([0, 4, Prand([6, 8b], 2)], inf));

a.source = Pbind(\instrument, \Pdefhelp, \dur, 0.1, \degree, Pseq(#[0, 1b, 1, 2b, 2, 3, 4b, 4, 5], inf));

a.set(\detune, -50); // set environment
a.set(\detune, 0);

x.stop;
```




### b) playing EventPatternProxy

```supercollider
s.boot;

(
// load a synthdef
SynthDef("gpdef", {
    arg out = 0, freq = 440, sustain = 0.05, amp = 0.1, pan;
    var env;
    env = EnvGen.kr(Env.perc(0.01, sustain), doneAction: Done.freeSelf) * amp;
    Out.ar(out, Pan2.ar(SinOsc.ar(freq, 0, env), pan))
}).add;
)

#x, y = { EventPatternProxy.new } ! 2;

x.play; // play them. A silent resting pattern is used.
y.play;

// assign various patterns to it:

x.source = Pbind(\dur, 0.25, \instrument, \gpdef);
x.source = Pbind(\dur, 0.25, \degree, Pseq([3, 4, 5b, 6], inf), \instrument, \gpdef);
x.source = Pbind(\dur, 0.25, \degree, Pseq([3, 4, 5b, 6]+1, inf), \instrument, \gpdef);
y.source = Pbind(\dur, 0.25, \degree, Pseq([3, 4, 5b, 6]-1, inf), \instrument, \gpdef);
y.source = Pbind(\dur, 0.25, \degree, Pseq([3, 4, 5b]-2, inf), \instrument, \gpdef);

// using fadeTime:

y.fadeTime = 8.0;
y.source = Pbind(\dur, 0.125, \degree, Pseq([3, 4, 5b, 6]+4.rand, inf), \instrument, \gpdef);
y.source = Pbind(\dur, 0.25, \degree, Pseq([3, 4, 5b, 6]-2, inf), \instrument, \gpdef);

(
x.source = Pbind(
    \dur, 1 / 6,
    \degree, Pseq([3, 4, Prand([8, 2, 3, 9, 10], 1) - 5, 6]+1, inf),
    \instrument, \gpdef
)
)

(
x.source = Pbind(
    \dur, 0.25,
    \degree, Pseq([3, 4, Prand([8, 2, 3, 9, 10], 1), 6], inf),
    \instrument, \gpdef
)
)

x.stop;

// tempo change
TempoClock.default.tempo = 1.3;
y.source = Pbind(\dur, 0.25, \degree, Pseq([3, 4, 5, 6]+1, inf), \instrument, \gpdef);

// drop in ending patterns

x.play;
x.fadeTime = nil;

x.source = Pbind(\dur, 0.25, \degree, Pseq([3, [7, 4], 5, 6]-2), \instrument, \gpdef);
x.source = Pbind(\dur, 0.125, \degree, Pseq([3, [7, 4], 5, 4]-3), \instrument, \gpdef);
x.source = Pbind(\dur, 0.35, \degree, Pseq([3, [7, 4], 5, 4, 3]-3), \instrument, \gpdef);
x.source = Pbind(\dur, 0.25, \degree, Pshuf([3, [7, 4], 5, 6]-2), \instrument, \gpdef);


TempoClock.default.tempo = 1.0;
x.stop;
y.stop;
```






