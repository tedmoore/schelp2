# SynthDefs versus Synths

*The use of precompiled SynthDefs as opposed to always compiling on the fly*

**Categories:** Language>SC3 vs SC2

In SC2 `Synth.play` was the standard way to compile a *ugenGraphFunc* and play it. Each time you executed `Synth.play`, or Spawned a new event, that function was compiled anew. SC3 on the other hand, makes use of what are called SynthDefs. A [SynthDef](../Classes/SynthDef.md) takes a *ugenGraphFunc* and compiles it to a kind of bytecode (sort of like Java bytecode) which can be understood by the server app. The server reads the [SynthDef](../Classes/SynthDef.md) and creates a synth node based upon it.
SynthDefs can be precompiled and saved to disk. Any def saved in the synthdefs/ directory (or in any directory set in the environment variable SC_SYNTHDEF_PATH) will be loaded into memory by a local [Server](../Classes/Server.md) when it is booted. If the def being used in a new [Synth](../Classes/Synth.md) is already compiled and loaded, there is much less of a CPU spike when creating a new [Synth](../Classes/Synth.md) than there was in SC2.
SynthDefs can also be compiled and loaded into the [Server](../Classes/Server.md) without writing them to disk. This can be done while performing.
The downside of this is that precompiled SynthDefs lack some of the programmatic flexibility that was one of SC2's great strengths. Much of this flexibility is gained back however, through the ability to set and change arguments (which you build into your *ugenGraphFunc*), and through new UGens such as [Rand](../Classes/Rand.md) and [TRand](../Classes/TRand.md).
When maximum flexibility is required, it is still possible to compile and send SynthDefs 'on the fly', albeit with SC2-like CPU spikes and a small amount of messaging latency.
It is important to understand that creating and sending SynthDefs is *asynchronous*. This means that it is impossible to determine precisely how long it will take to compile and send a [SynthDef](../Classes/SynthDef.md), and thus when it will be available for creating new Synths. A simple way around this is to execute code in blocks, selecting them one at a time. More complicated is to use completion messages. `SynthDef.play` takes care of this for you, and returns a [Synth](../Classes/Synth.md) object which you can then manipulate. See the example below
Another important distinction is between Synth in SC2 and [Synth](../Classes/Synth.md) in SC3. The latter is a client-side object which represents a synth node on the server. Although it has some of the same methods, it does not function in the same way. There is no top level Synth in SC3, within which all scheduling and creation of other Synths occurs. There are only [Synth](../Classes/Synth.md) objects which represent synth nodes on the server. These can be created at any time, within any scope.
## Examples


```
s.boot;

// Compile a SynthDef and write it to disk
(
SynthDef("Help-SynthDef", { arg out = 0;
    Out.ar(out, PinkNoise.ar(0.1))
}).writeDefFile;
)

// Compile, write, and load it to the server
(
SynthDef("Help-SynthDef", { arg out = 0;
    Out.ar(out, PinkNoise.ar(0.1))
}).load(s);
)

// Load it to the server without writing to disk
(
SynthDef("Help-SynthDef", { arg out = 0;
    Out.ar(out, PinkNoise.ar(0.1))
}).send(s);
)

// Create a Synth with it
x = Synth.new("Help-SynthDef", s);
x.free;

// Shorthand method to compile and write a SynthDef, and then play it in a Synth when done.
// Look familiar?
(
x = SynthDef("Help-SynthDef", { arg out = 0;
    Out.ar(out, PinkNoise.ar(0.1))
}).play(s);
)
// The above only starts the new Synth after the def has been sent to the server.
// Note that SynthDef.play returns a Synth object!

x.set(\out, 1); // change one of the arguments
x.free;

// SynthDef with a parameter that will be randomly determined each time a new Synth is created
// (try it several times to hear the differences)
(
SynthDef("help-RandFreq", { arg out = 0;
    Out.ar(
        out,
        FSinOsc.ar(
            Rand(200.0, 400.0), // frequency between 200 and 400 Hz
            0, Line.kr(0.2, 0, 1, doneAction: Done.freeSelf)
        )
    )
}).play(s);
)
```




