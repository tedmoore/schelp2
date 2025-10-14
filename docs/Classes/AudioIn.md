# AudioIn

*Read audio input.*

**Related:** [In](../Classes/In.md), [SoundIn](../Classes/SoundIn.md)

**Categories:** UGens>InOut

## Description

Reads audio from the sound input hardware.

> **Note:** This is provided for backwards compatibility with SC2 code. For normal use [SoundIn](../Classes/SoundIn.md), which has bus numbers beginning at 0, as AudioIn may be deprecated and removed at some point in the future.




## Class Methods

### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `channel` | Input channel number to read. Channel numbers begin at 1. |  
| `mul` |  |  
| `add` |  |  

## Examples

Patching input to output

```supercollider
// patching input to output

// beware of the feedback

(
ServerOptions.inDevices.postln;    //  post available audio input devices
s.meter;    // display level meters for monitoring
SynthDef(\helpAudioIn, { |out|
    var input = AudioIn.ar(1); // first input
    // delay output to tame feedback in case of microphones are configured:
    Out.ar(out, CombN.ar(input * -25.dbamp, 0.5, 0.5, 0.001))
}).play
)
```




