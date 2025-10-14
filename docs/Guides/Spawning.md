# "Spawning" and "TSpawning"

*The lack of the Spawn and TSpawn UGens and their various convienence classes*

**Categories:** Language>SC3 vs SC2

In SC2, Spawn and TSpawn were two of the most powerful and commonly used UGens. In SC3 the idea of a top level Synth in which everything is spawned is no longer valid. Synthesis is always running (at least as long as a server is) and new Synths can be created on the fly. This arrangement results in even greater flexibility than in SC2, but requires a slightly different approach.
In SC3 one can create Synths at any time simply by executing blocks of code.

```supercollider
// do this
(
x = SynthDef("Help-SynthDef", { arg out = 0;
    Out.ar(out, PinkNoise.ar(0.1))
}).play; // SynthDef-play returns a Synth object.
)

// then do this
(
SynthDef("help-Rand", { arg out = 0;
    Out.ar(
        out,
        FSinOsc.ar(
            Rand(200.0, 400.0), // frequency between 200 and 400 Hz
            0, Line.kr(0.2, 0, 1, doneAction: Done.freeSelf) // frees itself
        )
    )
}).play(s);
)

x.free;
```

Clocks, such as [SystemClock](../Classes/SystemClock.md), provide a way to schedule things at arbitrary points in the future. This is similar to `Synth.sched` in SC2.

```supercollider
(
SystemClock.sched(2.0, {
    "2.0 seconds later".postln; // this could be any code, including Synth creation
    nil // this means don't repeat
});
)
```

In SC3 time-based sequences of events can be implemented using Routines. A [Routine](../Classes/Routine.md) which yields a number can be scheduled using a clock:

```supercollider
(
var w, r;

w = Window.new("trem", Rect(512, 256, 360, 130));
w.front;

r = Routine({ arg time;
    60.do({ arg i;
        0.05.yield; // wait for 0.05 seconds
        {
            w.bounds = w.bounds.moveBy(10.rand2, 10.rand2);
            w.alpha = cos(i*0.1pi)*0.5+0.5;
        }.defer;
    });
    1.yield; // wait for 1 second before closing w
    w.close;
});

SystemClock.play(r);
)
```

Note that this implementation avoids one of the stranger aspects of the SC2 approach: The need to start a Synth to schedule time-based behavior, even if no audio is involved.
Both [SystemClock](../Classes/SystemClock.md) and [AppClock](../Classes/AppClock.md) (a less accurate version which can call Cocoa primitives) have only class methods. Thus one does not create instances of them. If you need to have an individual clock to manipulate (for instance to manipulate the tempi of different sequences of events) you can use [TempoClock](../Classes/TempoClock.md).
A simple SC2 Spawn example is shown below, followed by its translation into SC3 style code.

```supercollider
// This will not execute in SC3
(
Synth.play({
    Spawn.ar(
        { EnvGen.ar(Env.perc) * SinOsc.ar(440,0,0.1) },
        1, // one channels
        1 // new event every second
    )
})
)

// The same example in SC3 (will execute)
s.boot;
(
SynthDef("help-EnvGen",{ arg out = 0;
    Out.ar(
        out,
        EnvGen.kr(Env.perc,1.0,doneAction: Done.freeSelf) * SinOsc.ar(440,0,0.1)
    )
}).send(s);
)

(
r = Routine.new({ { Synth.new("help-EnvGen"); 1.yield; }.loop }); // loop every one second
SystemClock.play(r);
)
```

Note that the above example uses a precompiled [SynthDef](../Classes/SynthDef.md). This results in a lower CPU spike when Synths are created than SC2-style Spawning. It is possible to create SynthDefs on the fly, if this is necessary, but a great deal of variation can be achieved with arguments, or with UGens such as [Rand](../Classes/Rand.md) and [TRand](../Classes/TRand.md). See the section [SC3vsSC2#SynthDefsVsSynths](../Overviews/SC3vsSC2.md#synthdefsvssynths) for more detail.

```supercollider
// SynthDefs on the fly
s.boot;
(
t = TempoClock.new;
r = Routine.new({
    10.do({
        // could be done with an argument instead of a new def, but proves the point
        SynthDef("help-EnvGen" ++ i, { arg out = 0;
            Out.ar(
                out,
                EnvGen.kr(Env.perc, 1.0, doneAction: Done.freeSelf)
                * SinOsc.ar(100 + (100 * t.elapsedBeats), 0, 0.1)
            )
        }).play(s);
        1.yield;
    });
}).play(t); // Note the alternative syntax: Routine.play(aClock)
)
```

Note the alternative syntax for playing a Routine. `aClock.play(aRoutine)` and `aRoutine.play(aClock)` are functionally equivalent. The two make different things more or less convenient, like sending messages to the [Routine](../Classes/Routine.md) or [Clock](../Classes/Clock.md). (See the play helpfile for a more detailed discussion.) For instance:

```supercollider
(
// this, that and the other
r = Routine.new({var i = 0; { ("this: " ++ i).postln; i = i + 1; 1.yield; }.loop });
q = Routine.new({var i = 0; { ("that: " ++ i).postln; i = i + 1; 1.yield; }.loop });
t = Routine.new({var i = 0; { ("the other: " ++ i).postln; i = i + 1; 1.yield; }.loop });
)

SystemClock.play(r);    // start this
SystemClock.play(q);    // start that
SystemClock.play(t);    // start the other

r.stop;            // stop this but not that or the other
q.reset;        // reset that while playing

c = TempoClock.new;    // make a TempoClock
r.reset;        // have to reset this because it's stopped
c.play(r);        // play this in the new clock; starts from the beginning
c.tempo = 16;        // increase the tempo of this

SystemClock.clear;    // clear EVERYTHING scheduled in the SystemClock; so that and the other
            // but not this

c.clear;        // clear everything scheduled in c, i.e. this
c.play(r);        // since it wasn't stopped, we don't have to reset this
            // and it picks up where it left off

c.stop;            // stop c, destroy its scheduler, and release its OS thread
```

For convenience pauseable scheduling can be implemented with a [Task](../Classes/Task.md). `Task.new` takes two arguments, a function and a clock, and creates it's own [Routine](../Classes/Routine.md). If you don't specify a clock, it will create a [TempoClock](../Classes/TempoClock.md) for you. Since you don't have to explicitly create a [Clock](../Classes/Clock.md) or [Routine](../Classes/Routine.md), use of [Task](../Classes/Task.md) can result in code that is a little more compact.

```supercollider
(
t = Task.new({
    inf.do({ arg i;
        i.postln;
        0.5.wait
    });
});
)

t.start;        // Start it
t.stop;            // Stop it
t.start;        // Start again from the beginning
t.reset;        // Reset on the fly
t.stop;            // Stop again
t.resume;        // Restart from where you left off
t.clock.tempo = 0.25;    // Get the Task's clock and change the tempo. This works since the
            // default is a TempoClock.
t.pause;        // Same as t.stop
```

TSpawn's functionality can be replicated with [SendTrig](../Classes/SendTrig.md) and [OSCFunc](../Classes/OSCFunc.md). See their individual helpfiles for details on their arguments and functionality.

```supercollider
s.boot;
(
// this Synth will send a trigger to the client app
SynthDef("help-SendTrig", {
    SendTrig.kr(
        Dust.kr(1.0), // trigger could be anything, e.g. Amplitude.kr(SoundIn.ar(0) > 0.5)
        0, 0.9
    );
}).send(s);
)

(
// this receives the trigger on the client side and 'Spawns' a new Synth on the server
OSCFunc({
    SynthDef("help-EnvGen", { arg out = 0;
        Out.ar(
            out,
            EnvGen.kr(Env.perc, 1.0, doneAction: Done.freeSelf)
            * SinOsc.ar(440, 0, 0.1)
        )
    }).play(s);
}, '/tr', s.addr);

// Start 'spawning'
Synth("help-SendTrig");
)
```



