# OffsetOut

*Write a signal to a bus with sample accurate timing.*

**Related:** [Out](../Classes/Out.md), [ReplaceOut](../Classes/ReplaceOut.md), [XOut](../Classes/XOut.md)

**Categories:** UGens>InOut

## Description

Output signal to a bus, the sample offset within the bus is kept exactly; i.e. if the synth is scheduled to be started part way through a control cycle, OffsetOut will maintain the correct offset by buffering the output and delaying it until the exact time that the synth was scheduled for.
For achieving subsample accuracy see [SubsampleOffset](../Classes/SubsampleOffset.md)

> **Note:** Note that if you have an input to the synth, it will be coming in and its normal time, then mixed in your synth, and then delayed with the output. So you shouldn't use OffsetOut for effects or gating.


See the [Server-Architecture](../Reference/Server-Architecture.md) and [Bus](../Classes/Bus.md) helpfiles for more information on buses and how they are used.


## Class Methods


### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bus` | The index of the bus to write out to. The lowest numbers are written to the audio hardware. |  
| `channelsArray` | An Array of channels or single output to write out. You cannot change the size of this once a SynthDef has been built. |  

## Examples


```
(
SynthDef("help-OffsetOut",
    { |out = 0, freq = 440, dur = 0.05|
        var env;
        env = EnvGen.kr(Env.perc(0.01, dur, 0.2), doneAction: Done.freeSelf);
        OffsetOut.ar(out, SinOsc.ar(freq, 0, env))
}).send(s);

SynthDef("help-Out",
    { |out = 0, freq = 440, dur = 0.05|
        var env;
        env = EnvGen.kr(Env.perc(0.01, dur, 0.2), doneAction: Done.freeSelf);
        // compare to Out:
        Out.ar(out, SinOsc.ar(freq, 0, env))
}).send(s);
)


// these are in sync
(
Routine({
    loop {
        s.sendBundle(0.2, ["/s_new", "help-OffsetOut", -1]);
        0.01.wait;
    }
}).play;
)

// these are less reliably in sync and are placed at multiples of blocksize.
(
Routine({
    loop {
        s.sendBundle(0.2, ["/s_new", "help-Out", -1]);
        0.01.wait;
    }
}).play;
)



SynthDef("trig1", {
    var gate, tone;
    gate = Trig1.ar(1.0, t);
    tone = In.ar(10, 1); // tone comes in normally
    // but is then delayed when by the OffsetOut
    OffsetOut.ar(0,
        tone * EnvGen.ar(
                Env([0, 0.1, 0.1, 0], [0.01, 1.0, 0.01], [-4, 4], 2),
                gate, doneAction: Done.freeSelf
            )
    )
})
```




