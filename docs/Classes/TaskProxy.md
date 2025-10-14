# TaskProxy

*event stream reference*

**Categories:** JITLib>Patterns, Live Coding

**Related:** [Tdef](../Classes/Tdef.md)

## Description

Keeps a reference to a task (time pattern) that can be replaced while playing. It plays on when the old stream ended and a new stream is set and schedules the changes to the beat.


## Class Methods

### `new`
create a new instance with a function (the source). the source should be a **routine function** (see [Tdef](../Classes/Tdef.md)) or a **pattern** of time values.
### `default`
a default source, if none is given. the default is a loop that does nothing with a 1.0 beat wait time.
### `defaultQuant`
set the default quantization value for the class. (default: 1.0). can be a pair [quant, offset]

## Instance Methods

### `source`
set the source. If a quantization is given, schedule this change to the next beat the object is a **routine function**, which is evaluated in a protected way, so that failure will notify the proxy that it has stopped. The object can also be a **pattern** of time values.### `clear`
set the source to nil### `clock`
get or set the instance's default clock, used by [#-play](#-play) if no other clock is specified. Defaults to TempoClock.default.### `quant`
get or set the quantization value. can be a pair [quant, offset]### `condition`
provide a condition under which the pattern is switched when a new one is inserted. the stream value and a count is passed into the function. the methods **count_(n)** simply counts up to n and switches the pattern then### `reset`
switch the pattern immediately. (stuck conditions can be subverted by this)### `envir`
provide a default environment for the proxy. If given, it is used as an environment for the routine function. When set for the first time, the routine pattern is rebuilt.### `set`
set arguments in the environment. If there is none, it is created and the routine pattern is rebuilt.### `endless`
returns a [Prout](../Classes/Prout.md) that plays the proxy endlessly, replacing **nil** with a **default** value (1 s. wait time). This allows to create streams that idle on until a new pattern is inserted.
### a) using it as stream reference
### `source`
set the routine function / pattern (internally done by *new(key, obj)
### `embedInStream`
just like any stream, embeds itself in stream

### b) using it as EventStreamPlayer
### `play`
starts the TaskProxy and creates a player. if you want to play multiple instances, use **.playOnce(clock, protoEvent, quant)****Arguments:**

| Argument | Description |
|----------|-------------|
| `argClock` | which clock to use. if nil then use this instance's [#-clock](#-clock), which in turn defaults to TempoClock.default. |  
| `doReset` | A [Boolean](../Classes/Boolean.md) |  
| `quant` | can be an array of [quant, phase] |  

### `stop`
stops the player
### `player`
the current player (if the TaskProxy is simply used in other streams this is nil)
### `pause`, `resume`, `reset`
perform player method
### `isPlaying`
returns true if TaskProxy is running. if a TaskProxy is playing and its stream ends, it will schedule a stream for playing as soon as a new one is assigned to it.

## Examples


### a) using TaskProxy as a player

```supercollider
// create an empty Tdef and play it.
x = TaskProxy.new;
x.play;


x.source = { loop { "ggggggggggggggggg9999ggg999ggg999gg".scramble.postln; 0.5.wait } };


x.source = { loop { "---------////----------------------".scramble.postln; 0.25.wait } };
x.source = { loop { thisThread.seconds.postln; 1.wait } };
x.source = { loop { thisThread.seconds.postln; 1.01.wait } };

TempoClock.default.tempo = 2;

x.source = { "the end".postln };
x.source = { "one more".postln };
x.source = { 10.do { "ten more".scramble.postln; 0.25.wait } };
x.source = { loop { "many more".scramble.postln; 0.25.wait } };

TempoClock.default.tempo = 1;

x.stop;
x.play;
x.stop;
```



```supercollider
// sound example

(
// load a synthdef
s.boot;
SynthDef("pdef_grainlet",
    { |out = 0, freq = 440, sustain = 0.05|
        var env;
        env = EnvGen.kr(Env.perc(0.01, sustain, 0.3), doneAction: Done.freeSelf);
        Out.ar(out, SinOsc.ar(freq, 0, env))
    }).add;
)
x.play;

(
x.source = {
    loop {
        s.sendMsg("/s_new", "pdef_grainlet", -1, 0, 0, \freq, rrand(600, 640));
        0.1.wait;
    }
}
)

(
x.source = {
    var x;
    x = Pseries(300, 20, 100).loop.asStream;
    loop {
        s.sendMsg("/s_new", "pdef_grainlet", -1, 0, 0, \freq, x.next);
        0.05.wait;
    }
}
)

(
x.source = {
    var x;
    x = Plazy { Pseries(300 + 300.rand, 10 + 30.rand, 10 + 30.rand) }.loop.asStream;
    loop {
        s.sendMsg("/s_new", "pdef_grainlet", -1, 0, 0, \freq, x.next);
        0.05.wait;
    }
}
)

// metronome
(
y = TaskProxy {
    loop { s.sendMsg("/s_new", "pdef_grainlet", -1, 0, 0, \freq, 1500); 1.wait }
};
y.play;
)

// play ending stream once
(
x.source = {
    var x, dt;
    dt = [0.1, 0.125, 0.05].choose;
    x = Plazy { Pseries(1300 + 300.rand, 110 + 130.rand, 16) }.asStream;
    x.do { |item|
        s.sendMsg("/s_new", "pdef_grainlet", -1, 0, 0, \freq, item);
        dt.wait;
    }
}
)

... and so on ...

x.stop;
y.stop;
```




### b) embedding TaskProxy into other Tasks / Routines

```supercollider
(
#a, c = { TaskProxy.new } ! 2;
a.source = { "one".postln; 1.wait; "two".postln };
c.source = { var z; z = Synth(\default); 0.5.wait; z.release };
r = Task {
    "counting...".postln;
    2.wait;
    a.embedInStream;
    1.wait;
    c.embedInStream;
    "done.".postln;
};
)

r.play; // play a stream

c.source = { var z; z = Synth(\default, [\freq, 300]); 1.5.wait; z.release }; // change the def

r.reset;
r.play;

// of course TaskProxies can be used in other Tdefs:
(
b = TaskProxy.new;
b.source = {
    "counting...".postln;
    2.wait;
    a.embedInStream;
    1.wait;
    c.embedInStream;
    "done.".postln;
};
)
b.playOnce;

// if one wants to branch off a stream in a separate thread, asStream is used.
(
Routine {
    c.asStream.play;
    0.1.wait;
    c.asStream.play;
    0.1.wait;
    a.asStream.play;

}.play;
)
```






