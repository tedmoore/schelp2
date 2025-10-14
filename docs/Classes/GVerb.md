# GVerb

*A two-channel reverb*

**Categories:** UGens>Reverbs

**Related:** [FreeVerb](../Classes/FreeVerb.md), [FreeVerb2](../Classes/FreeVerb2.md)

## Description

A two-channel reverb [UGen](../Classes/UGen.md), based on the "GVerb" LADSPA effect by Juhana Sadeharju (kouhia at nic.funet.fi).

### Known issues
- There is a large CPU spike when the synth is instantiated while all the delay lines are zeroed out.
- Changes in roomsize result in pitch shifting and noise.





## Class Methods

### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | mono input. |  
| `roomsize` | in squared meters. |  
| `revtime` | in seconds. |  
| `damping` | 0 to 1, high frequency rolloff, 0 damps the reverb signal completely, 1 not at all. |  
| `inputbw` | 0 to 1, same as damping control, but on the input signal. |  
| `spread` | a control on the stereo spread and diffusion of the reverb signal. |  
| `drylevel` | amount of dry signal. |  
| `earlyreflevel` | amount of early reflection level. |  
| `taillevel` | amount of tail level. |  
| `maxroomsize` | to set the size of the delay lines. Defaults to roomsize + 1. |  
| `mul` |  |  
| `add` |  |  

## Examples


```supercollider
(
SynthDef(\test, { |out, roomsize, revtime, damping, inputbw, spread = 15, drylevel, earlylevel,
    taillevel|

    var a = Resonz.ar(
        Array.fill(4, { Dust.ar(2) }),
        1760 * [1, 2, 4, 8],
        0.01
    ).sum * 10;

    //    var a = SoundIn.ar(0);
    //    var a = PlayBuf.ar(1, 0);

    Out.ar(out,
        GVerb.ar(
            a,
            roomsize,
            revtime,
            damping,
            inputbw,
            spread,
            drylevel.dbamp,
            earlylevel.dbamp,
            taillevel.dbamp,
            roomsize, 0.3)
        + a
    )
}).add
)


s.scope(2);

// bathroom
a = Synth(\test, [\roomsize, 5, \revtime, 0.6, \damping, 0.62, \inputbw, 0.48, \drylevel -6, \earlylevel, -11, \taillevel, -13]);
a.free;

// living room
a = Synth(\test, [\roomsize, 16, \revtime, 1.24, \damping, 0.10, \inputbw, 0.95, \drylevel -3, \earlylevel, -15, \taillevel, -17]);
a.free;

// church
a = Synth(\test, [\roomsize, 80, \revtime, 4.85, \damping, 0.41, \inputbw, 0.19, \drylevel -3, \earlylevel, -9, \taillevel, -11]);
a.free;

// cathedral
a = Synth(\test, [\roomsize, 243, \revtime, 1, \damping, 0.1, \inputbw, 0.34, \drylevel -3, \earlylevel, -11, \taillevel, -9]);
a.free

// canyon
a = Synth(\test, [\roomsize, 300, \revtime, 103, \damping, 0.43, \inputbw, 0.51, \drylevel -5, \earlylevel, -26, \taillevel, -20]);
a.free;

s.quit;
```




