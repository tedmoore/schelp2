# ExampleFiles

*A shortcut to example sounds bundled with SuperCollider*

**Categories:** Files

**Related:** [Buffer](../Classes/Buffer.md), [SoundFile](../Classes/SoundFile.md), [File](../Classes/File.md), [PathName](../Classes/PathName.md)

## Description

Provides a shortcut to the paths of example files which are bundled with SuperCollider and are located in [Platform#*resourceDir](../Classes/Platform.md#*resourcedir).

```
// instead of writing
Platform.resourceDir +/+ "sounds" +/+ "a11wlk01-44_1.aiff";
// one can write
ExampleFiles.apollo11;
```




## Class Methods


### `apollo11`
A radio recording from the Apollo 11 moon landing program where Bruce McCandless says *"Columbia, this is Houston. Over."*. For more information see [https://www.nasa.gov/history/alsj/a11/a11.mobility.html](https://www.nasa.gov/history/alsj/a11/a11.mobility.html) at the mark `110:25:41` (it seems to be the third repetition, though the pitch does not match).| Filename | `a11wlk01-44_1.aiff` | 
| --- | --- || Channels | 1 | | Samplerate | 44100 Hz | | Format | pcm_s16be | | Duration | 00:00:02.44 | **Returns:** The full path of `a11wlk01-44_1.aiff` as a [String](../Classes/String.md)Trivia time: Although the file in its current form was introduced on 2004-07-11 by Scott Wilson via commit `bc9a4d4fd8cdccd2b1c787010c776176c7993d2c`, its original version as a 11025 Hz mono file dates back to at least 2002-09-28 via the commit `f30d769ab6b8eb1f36027ed3a400efd3b829f43a` by James McCartney.This can be considered the "Hello world" audio sample of SuperCollider.

### `sinedPink`
A very short stereo sample which has 10 cycles of a 440Hz [SinOsc](../Classes/SinOsc.md) on its first channel and a [PinkNoise](../Classes/PinkNoise.md) on its second channel.| Filename | `SinedPink.aiff` | 
| --- | --- || Channels | 2 | | Samplerate | 44100 Hz | | Format | pcm_f32be | | Duration | 00:00:00.02 | **Returns:** The full path of `SinedPink.aiff` as a [String](../Classes/String.md)

### `child`
Allegedly a re-recording of [ExampleFiles#*apollo11](../Classes/ExampleFiles.md#*apollo11) performed by a child of a developer.| Filename | `a11wlk01.wav` | 
| --- | --- || Channels | 1 | | Samplerate | 44100 Hz | | Format | pcm_s16le | | Duration | 00:00:04.28 | **Returns:** The full path of `a11wlk01.wav` as a [String](../Classes/String.md)

