# Tap

*Single tap into a delay line*

**Related:** [MultiTap](../Classes/MultiTap.md), [PlayBuf](../Classes/PlayBuf.md)

**Categories:** UGens>Buffer, UGens>Delays>Buffer

## Description

The Tap UGen allows a single tap at a delay into a buffer.
Tap uses the [PlayBuf](../Classes/PlayBuf.md) UGen internally


## Class Methods


### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bufnum` | The index of the buffer to use |  
| `numChannels` | Number of channels of the buffer |  
| `delaytime` | Tap delay; cannot be modulated |  

## Examples


```supercollider
// Create a buffer.
b = Buffer.alloc(s, s.sampleRate, 1); // enough space for one second of mono audio

// Write to the Buffer with BufWr, read using two Taps, one for each ear!
(
SynthDef(\helpTap, { |out, bufnum|
    var source, capture;

    source = SoundIn.ar(0); // use headphones to avoid feedback
    capture = BufWr.ar(source, bufnum, Phasor.ar(0, 1, 0, BufFrames.ir(bufnum), 1));

    Out.ar(out, Tap.ar(bufnum, 1, [0.1, 0.9])); // multichannel expansion, so one tap each ear
}).add;
)

x = Synth(\helpTap, [\bufnum, b]);

x.free;
```




