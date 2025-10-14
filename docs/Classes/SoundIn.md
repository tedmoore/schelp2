# SoundIn

*Read audio from hardware inputs*

**Categories:** UGens>InOut

**Related:** [In](../Classes/In.md), [ServerOptions](../Classes/ServerOptions.md)

## Description

SoundIn is a convenience UGen to read audio from the input of your computer or soundcard. It is a wrapper [UGen](../Classes/UGen.md) based on [In](../Classes/In.md), which offsets the index such that 0 will always correspond to the first input regardless of the number of inputs present.

> **Note:** On Intel based Macs, reading the built-in microphone or input may require creating an aggregate device in AudioMIDI Setup.`"open -a 'Audio MIDI Setup'".unixCmd; // execute this to launch it`




## Class Methods

### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bus` | the channel (or array of channels) to read in. These start at 0, which will correspond to the first audio input. |  
| `mul` |  |  
| `add` |  |  

## Examples


```supercollider
// world's most expensive patchcord (use headphones to avoid feedback)
{ SoundIn.ar(0) }.play;

// stereo version
{ SoundIn.ar([0, 1]) }.play;

// scope input; silent output
{ Amplitude.kr(SoundIn.ar(0)) }.scope;
```




