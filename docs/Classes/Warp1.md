# Warp1

*Warp a buffer with a time pointer*

**Categories:** UGens>Buffer, UGens>Generators>Granular

## Description

Inspired by Chad Kirby's SuperCollider2 Warp1 class, which was inspired by Richard Karpen's sndwarp for CSound. A granular time stretcher and pitchshifter.


## Class Methods



### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `numChannels` | the number of channels in the soundfile used in bufnum. Must be a nonzero, positive integer. This is fixed when the SynthDef is compiled so cannot be assigned to a SynthDef argument. |  
| `bufnum` | the buffer number of a mono soundfile. |  
| `pointer` | the position in the buffer. The value should be between 0 and 1, with 0 being the beginning of the buffer, and 1 the end. |  
| `freqScale` | the amount of frequency shift. 1.0 is normal, 0.5 is one octave down, 2.0 is one octave up. Negative values play the soundfile backwards. |  
| `windowSize` | the size of each grain window. |  
| `envbufnum` | the buffer number containing a signal to use for the grain envelope. -1 uses a built-in Hanning envelope. |  
| `overlaps` | the number of overlapping windows. |  
| `windowRandRatio` | the amount of randomness to the windowing function. Must be between 0 (no randomness) to 1.0 (probably too random actually) |  
| `interp` | the interpolation method used for pitchshifting grains. 1 = no interpolation. 2 = linear.  4 = cubic interpolation (more computationally intensive). |  
| `mul` |  |  
| `add` |  |  

## Examples


```
s.boot;

(
b = Buffer.read(s, ExampleFiles.apollo11);
x = { |envbuf = -1|
    var pointer, pitch;
    // pointer - move from beginning to end of soundfile over 15 seconds
    pointer = LFSaw.ar(1/15).range(0, 1);
    // control pitch with MouseX
    pitch = MouseX.kr(0.5, 2);
    Warp1.ar(
        numChannels: 1,
        bufnum: b,
        pointer: pointer,
        freqScale: pitch,
        windowSize: 0.1,
        envbufnum: envbuf,
        overlaps: 8,
        windowRandRatio: 0.1,
        interp: 2
    )
}.play

)


(
// a custom envelope - not a very good one, but you can hear the difference
// between this and the default
var winenv = Env([0, 1, 0], [0.5, 0.5], [8, -8]);
z = Buffer.sendCollection(s, winenv.discretize, 1);
x.set(\envbuf, z);
)

// the default is -1
x.set(\envbuf, -1);

// relase and end
x.relase; z.free;
```



```
(
b.free;
b = Buffer.read(s, ExampleFiles.apollo11);
{
    var pointer = Phasor.ar(0, SampleDur.ir / BufDur.ir(b) * XLine.kr(1, 0.25, 20));
    var sound = Warp1.ar(1, b, pointer, 1, 0.3, -1, 16, Line.kr(0, 1, 40), 4);
    Pan2.ar(sound, pointer * 2 - 1, 0.25)
}.play
)
b.free;
```




