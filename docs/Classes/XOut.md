# XOut

*Send signal to a bus, crossfading with previous contents.*

**Related:** [OffsetOut](../Classes/OffsetOut.md), [Out](../Classes/Out.md), [ReplaceOut](../Classes/ReplaceOut.md)

**Categories:** UGens>InOut

## Description

Send signal to a bus, crossfading with previous contents. `xfade` is a level for the crossfade between what is on the bus and what you are sending. The algorithm is equivalent to this:

```supercollider
bus_signal = (input_signal * xfade) + (bus_signal * (1 - xfade));
```


See the [Server-Architecture](../Reference/Server-Architecture.md) and [Bus](../Classes/Bus.md) helpfiles for more information on buses and how they are used.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bus` | The index of the bus to write out to. The lowest numbers are written to the audio hardware. |  
| `xfade` | Crossfade level. |  
| `channelsArray` | An Array of channels or single output to write out. You cannot change the size of this once a SynthDef has been built. |  

## Examples


```supercollider
(
SynthDef("help-SinOsc", { |freq = 440, out|
    Out.ar(out, SinOsc.ar(freq, 0, 0.1))
}).add;

SynthDef("help-XOut", { |out = 0, xFade = 1|
    var source;
        source = PinkNoise.ar(0.05);

        // write to the bus, crossfading with previous contents
        XOut.ar(out, xFade, source);

}).add;
)

Synth("help-SinOsc", [\freq, 500]);
a = Synth.tail(s, "help-XOut");


a.set(\xFade, 0.7);
a.set(\xFade, 0.4);
a.set(\xFade, 0.0);
```




