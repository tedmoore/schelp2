# FreeVerb2

*A two-channel reverb*

**Categories:** UGens>Reverbs

**Related:** [FreeVerb](../Classes/FreeVerb.md), [GVerb](../Classes/GVerb.md)

## Description

Coded from experiments with faust.


## Class Methods

### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | input signal channel 1. |  
| `in2` | input signal channel 2. |  
| `mix` | dry/wet balance. range 0..1. |  
| `room` | room size. rage 0..1. |  
| `damp` | Reverb HF damp. range 0..1. |  
| `mul` |  |  
| `add` |  |  
Valid parameter range from 0 to 1. Values outside this range are clipped by the UGen.
## Examples


```supercollider
s.boot;

// FreeVerb2 - demo synthdef
(
SynthDef(\FreeVerb2x2, { |out, mix = 0.25, room = 0.15, damp = 0.5, amp = 1.0|
    var signal;

    signal = In.ar(out, 2);

    ReplaceOut.ar(out,
        FreeVerb2.ar( // FreeVerb2 - true stereo UGen
            signal[0], // Left channel
            signal[1], // Right Channel
            mix, room, damp, amp
        )
    ); // same params as FreeVerb 1 chn version

}).add;
)

// 2ch source
(
a = SynthDef(\src2x2, { |out|
    Out.ar(out,
        Decay.ar(Impulse.ar(1), 0.25, LFCub.ar(1200, 0, 0.1)) ! 2
        +
        Pan2.ar(
            Decay.ar(Impulse.ar(1, pi), 0.1, WhiteNoise.ar(0.1)),
            LFNoise1.kr(0.5).range(-1, 1)
        )
    )
}).play
)

// kick it in
z = Synth(\FreeVerb2x2, [\outbus, 0], addAction: \addToTail)
// experiment with some settings
z.set(\room, 0.7)
z.set(\mix, 0.33)
z.set(\damp, 0.9)

// silence
[a, z].do(_.free)
```




