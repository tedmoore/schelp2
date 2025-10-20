# SoundFile

*sclang soundfile data*

**Related:** [File](../Classes/File.md), [Buffer](../Classes/Buffer.md)

**Categories:** Files

## Description

The SoundFile class is used to check the size, format, channels etc. when the sclang client needs this information about a SoundFile. Soundfile data can be read and modified. Soundfile data can also be read and written incrementally, so with properly designed code, there is no restriction on the file size.
In most cases you will wish to send commands to the server to get it to load SoundFiles directly into Buffers. You will not need to use this class for this. See the [Buffer](../Classes/Buffer.md) helpfile.

```
(
// ExampleFiles helps locate audio files used in examples
p = ExampleFiles.child;
// peek at the path to see location and the format of a path
p.postln;

f = SoundFile.new;
f.openRead(p);
f.inspect;
f.close;
)
```


When reading a sound file, the headerFormat, sampleFormat, numChannels and numFrames variables will be set according to the file on disk.
When creating a new SoundFile, the format will be monophonic, 44.1 kHz, AIFF, floating-point by default. Users may override the defaults by passing the desired format strings to [SoundFile#*openWrite](../Classes/SoundFile.md#*openwrite), or by using [SoundFile#-headerFormat](../Classes/SoundFile.md#-headerformat), [SoundFile#-sampleFormat](../Classes/SoundFile.md#-sampleformat), [SoundFile#-numChannels](../Classes/SoundFile.md#-numchannels) and [SoundFile#-sampleRate](../Classes/SoundFile.md#-samplerate) *before* calling [SoundFile#-openWrite](../Classes/SoundFile.md#-openwrite).


## Class Methods


### `new`
Creates a new SoundFile instance.

### `writeArray`
Writes an array (or nested array) to a path as a sound file.**Arguments:**

| Argument | Description |
|----------|-------------|
| `array` | The data to write. Can be an array of numbers for a mono audio file, or an array of arrays-of-numbers for a multichannel audio file. Does not accept further nested arrays. Please note, that supercollider does not currently support very large arrays, roughly speaking, mono sound files longer than 45 mins at a sampling rate of 44100 will cause supercollider to fail silently. |  
| `pathName` | The path as a [String](../Classes/String.md). |  
| `headerFormat` | See [SoundFile#-headerFormat](../Classes/SoundFile.md#-headerformat). |  
| `sampleFormat` | See [SoundFile#-sampleFormat](../Classes/SoundFile.md#-sampleformat). |  
| `sampleRate` | A number, defaults to 44100. |  
**Returns:** The path if successful, or throws if unsuccessful.

### `openRead`
Try to open the audio file at the given path.**Arguments:**

| Argument | Description |
|----------|-------------|
| `pathName` | Full path to the sound file. Use [String#-standardizePath](../Classes/String.md#-standardizepath) to resolve home-folder shortcuts such as `~`. |  
**Returns:** A new SoundFile instance if successful, or `nil` if file open failed. User code should check for `nil` before doing anything with the SoundFile object.

### `openWrite`
Try to create an audio file at the given path. Note that there is no `numFrames` argument: the number of frames is counted after writing data into the file.**Arguments:**

| Argument | Description |
|----------|-------------|
| `pathName` | Full path to the sound file. Use [String#-standardizePath](../Classes/String.md#-standardizepath) to resolve home-folder shortcuts such as `~`. |  
| `headerFormat` | A string for the sound file format. Valid strings are listed at [SoundFile#-headerFormat](../Classes/SoundFile.md#-headerformat). If not given, the default `"AIFF"` is used. |  
| `sampleFormat` | A string for the sample format. Valid strings are listed at [SoundFile#-sampleFormat](../Classes/SoundFile.md#-sampleformat). If not given, the default `"float"` is used. |  
| `numChannels` | An integer number of channels (1 by default). |  
| `sampleRate` | An integer sample rate (44100 by default). |  
**Returns:** A new SoundFile instance if successful, or `nil` if file open failed. User code should check for `nil` before doing anything with the SoundFile object.

### `collect`
Returns an [Array](../Classes/Array.md) of SoundFile objects whose paths match the pattern. (The associated files are closed. These objects can be used to cue playback buffers)
```
SoundFile.collect("sounds/*").do { |f| f.path.postln };
```



### `use`
Reads the data of a SoundFile, evaluates the function (passing the file as argument) and closes it again.
```
SoundFile.use(ExampleFiles.child, { |f| f.inspect });
```



### `normalize`
Normalizes a soundfile to a level set by the user. The normalized audio will be written into a second file.Using this class method (SoundFile.normalize) will automatically open the source file for you. You may also [#-openRead](#-openread) the SoundFile yourself and call [#-normalize](#-normalize) on it. In that case, the source path is omitted because the file is already open.See instance method [#-normalize](#-normalize) for more information.

## Instance Methods


### Playback

### `cue`
Allocates a buffer and cues the SoundFile for playback. Returns an event parameterized to play that buffer. (See [NodeEvent](../Reference/NodeEvent.md) for a description of how events can be used to control running synths.) The event responds to **play**, **stop**, **pause**, **resume**, keeping the buffer open. The buffer is closed when the event is sent a **close** message.**Arguments:**

| Argument | Description |
|----------|-------------|
| `ev` | An [Event](../Classes/Event.md) can passed as an argument allowing playback to be customized using the following keys:| **key** | **default value** | **what it does** | 
| --- | --- | --- || bufferSize | 65536 | Must be a power of two (65536, 131072 or 262144 recommended) | | firstFrame | 0 | first frame to play | | lastFrame | nil | last frame to play (nil plays to end of file) | | out: | 0 | sets output bus | | server: | Server.default | which server | | group: | 1 | what target | | addAction: | 0 | head/tail/before/after | | amp: | 1 | amplitude | | instrument: | nil | if nil SoundFile:cue determines the SynthDef (one of diskIn1, diskIn2, ...diskIn16) | Where **bufferSize**, **firstFrame**, **lastFrame** are for buffer and playback position, and **out**, **server**, **group**, **addAction**, **amp** are synth parameters. Here is the default SynthDef used for stereo files:
```
SynthDef(\diskIn2, { |out, amp = 1, bufnum, sustainTime, atk = 0, rel = 0, gate = 1|
    var sig = VDiskIn.ar(2, bufnum, BufRateScale.kr(bufnum));
    var gateEnv = EnvGen.kr(Env([1, 1, 0], [sustainTime-rel, 0]));
    var env = EnvGen.kr(Env.asr(atk, 1, rel), gate * gateEnv, doneAction: Done.freeSelf);
    Out.ar(out, sig * env * amp)
});
```

The control **sustainTime** determines playback duration based on the firstFrame and lastFrame. The control **gate** allows early termination of the playback |  
| `playNow` | This is a [Boolean](../Classes/Boolean.md) that determines whether the file is to be played immediately after cueing.
```
f = SoundFile.collect("sounds/*");
e = f[1].cue;

e = f[1].cue((addAction: 2, group: 1));    // synth will play ahead of the default group
``` |  
| `closeWhenDone` | A flag to indicate whether the buffer will be closed after playback is finished. Default is False. |  


### Read/Write

### `openRead`
Read the header of a file. Answers a [Boolean](../Classes/Boolean.md) whether the read was successful. Sets the [#-numFrames](#-numframes), [#-numChannels](#-numchannels) and [#-sampleRate](#-samplerate). Does **not** set the [#-headerFormat](#-headerformat) and [#-sampleFormat](#-sampleformat).**Arguments:**

| Argument | Description |
|----------|-------------|
| `pathName` | a [String](../Classes/String.md) specifying the path name of the file to read. |  


### `readData`
Reads the sample data of the file into the raw array you supply. You must have already called [#-openRead](#-openread).When you reach EOF, the array's size will be 0. Checking the array size is an effective termination condition when looping through a sound file. See the method [#-channelPeaks](#-channelpeaks) for example.**Arguments:**

| Argument | Description |
|----------|-------------|
| `rawArray` | The raw array must be a [FloatArray](../Classes/FloatArray.md). Regardless of the sample format of the file, the array will be populated with floating point values. For integer formats, the floats will all be in the range -1..1.The size of the FloatArray determines the maximum number of single samples (not sample frames) that will be read. If there are not enough samples left in the file, the size of the array after the readData call will be less than the original size. |  


### `openWrite`
Write the header of a file. Answers a [Boolean](../Classes/Boolean.md) whether the write was successful.**Arguments:**

| Argument | Description |
|----------|-------------|
| `pathName` | a [String](../Classes/String.md) specifying the path name of the file to write. |  


### `writeData`
Writes the rawArray to the sample data of the file. You must have already called [#-openWrite](#-openwrite).**Arguments:**

| Argument | Description |
|----------|-------------|
| `rawArray` | The raw array must be a [FloatArray](../Classes/FloatArray.md) or [Signal](../Classes/Signal.md), with all values between -1 and 1 to avoid clipping during playback.
```
(
f = SoundFile.new.headerFormat_("AIFF").sampleFormat_("int16").numChannels_(1);
f.openWrite("sounds/sfwrite.aiff");
    // sawtooth
b = Signal.sineFill(100, (1..20).reciprocal);
    // write multiple cycles (441 * 100 = 1 sec worth)
441.do({ f.writeData(b) });
f.close;
)
``` |  


### `isOpen`
answers if the file is open.

### `close`
closes the file.

### `duration`
the duration in seconds of the file.

### Normalizing

### `normalize`
Normalizes a soundfile to a level set by the user. The normalized audio will be written into a second file.The normalizer may be used to convert a soundfile from one sample format to another (e.g., to take a floating point soundfile produced by SuperCollider and produce an int16 or int24 soundfile suitable for use in other applications).
> **Note:** While the normalizer is working, there is no feedback to the user. It will look like SuperCollider is hung, but it will eventually complete the operation. You can set `threaded:true` to get feedback but it will take slightly longer to complete.

**Arguments:**

| Argument | Description |
|----------|-------------|
| `outPath` | a path to the destination file. |  
| `newHeaderFormat` | the desired header format of the new file; if not specified, the header format of the source file will be used. |  
| `newSampleFormat` | the desired sample format of the new file; if not specified, the sample format of the source file will be used. |  
| `startFrame` | an index to the sample frame to start normalizing. |  
| `numFrames` | the number of sample frames to copy into the destination file (default nil, or entire soundfile). |  
| `maxAmp` | the desired maximum amplitude. Provide a floating point number or, if desired, an array to specify a different level for each channel. |  
| `linkChannels` | a [Boolean](../Classes/Boolean.md) specifying whether all channels should be scaled by the same amount. The default is **true**, meaning that the peak calculation will be based on the largest sample in any channel. If false, each channel's peak will be calculated independently and all channels will be scaled to maxAmp (this would alter the relative loudness of each channel). |  
| `chunkSize` | how many samples to read at once (default is 4194304, or 16 MB). |  
| `threaded` | if true, the normalization runs in a routine so that SC can respond (intermittently) while processing. Prevents macOS beachballing. |  


### Instance Variables

### `path`
Get the pathname of the file. This variable is set via the [#-openRead](#-openread) or [#-openWrite](#-openwrite) calls.

### `headerFormat`
This is a [String](../Classes/String.md) indicating the header format which was read by openRead and will be written by openWrite. In order to write a file with a certain header format you set this variable.
**read/write header formats:**
: | **header** | **description** | **filename extensions** | **notes** | 
| --- | --- | --- | --- || "AIFF" | Apple/SGI AIFF format | .aif, .aiff |  | | "WAV", "WAVE", "RIFF" | Microsoft WAV format | .wav, .wave |  | | "Sun", "NeXT" | Sun/NeXT AU format | .au, .snd |  | | "SD2" | Sound Designer 2 | .sd2 |  | | "IRCAM" | Berkeley/IRCAM/CARL | .sf |  | | "raw" | no header = raw data |  |  | | "MAT4" | Matlab (tm) V4.2 / GNU Octave 2.0 | .mat4 |  | | "MAT5" | Matlab (tm) V5.0 / GNU Octave 2.1 | .mat5 |  | | "PAF" | Ensoniq PARIS file format | .paf |  | | "SVX" | Amiga IFF / SVX8 / SV16 format | .svx |  | | "NIST" | Sphere NIST format | .nist, .sph |  | | "VOC" | VOC files | .voc |  | | "W64" | Sonic Foundry's 64 bit RIFF/WAV | .w64 | supports files larger than 4GB | | "PVF" | Portable Voice Format | .pvf |  | | "XI" | Fasttracker 2 Extended Instrument | .xm |  | | "HTK" | HMM Tool Kit format | .htk |  | | "SDS" | Midi Sample Dump Standard | .sds |  | | "AVR" | Audio Visual Research | .avr |  | | "FLAC" | FLAC lossless file format | .flac |  | | "CAF" | Core Audio File format | .caf | supports files larger than 4GB | | "RF64" | RF64 WAV format | .wav | supports files larger than 4GB | | "OGG" | Xiph OGG container | .ogg | use .ogg extension for the "vorbis" format (see below) | | "MPEG" | MPEG container | .mp1, .mp2, .mp3 | file extension depends on the format (see below) |

Additionally, a huge number of other formats are supported read only. Please note that WAV file support is limited to 4GB. For output of multiple channels or very long recordings we suggest to use RF64, W64, or CAF (on macOS).

### `sampleFormat`
A [String](../Classes/String.md) indicating the format of the sample data which was read by [#-openRead](#-openread) and will be written by [#-openWrite](#-openwrite). libsndfile determines which header formats support which sample formats. This information is detailed at [http://www.mega-nerd.com/libsndfile](http://www.mega-nerd.com/libsndfile) . The possible sample formats are:
**sample formats:**
: | **format** | **notes** | **supported headers** (partial list)  | 
| --- | --- | --- || "int8", "int16", "int24", "int32" | integer formats | "AIFF", "WAV", "RF64", "W64", "CAF", "FLAC"  | | "float" | floating-point format (won't clip above 0dB) | "AIFF", "WAV", "RF64", "W64", "CAF"  | | "mulaw", "alaw" | U-law and A-law encoding | "WAV", "W64"  | | "vorbis" | "Vorbis" compressed format | "OGG"  | | "mp1", "mp2", "mp3" | MPEG Layer I, II, and III compressed formats | "MPEG" (see **NOTE** below) |

Not all header formats support all sample formats.
> **Note:** Support for `MPEG` formats requires `libsndfile` library that supports it. This library is included in SuperCollider's macOS and Windows release builds version `3.13` and up. However, on platforms where system installation of libsndfile is used (e.g. Linux), or when building SC locally, MPEG support requires `libsndfile` version `1.1.0` or higher and that the library was built with the MPEG functionality enabled.

Currently there's no way to control the quality (bitrate) when writing OGG vorbis and MPEG files - the default bitrate set in libsndfile is used.

### `numFrames`
The number of sample frames in the file.

### `numChannels`
The number of channels in the file.

### `sampleRate`
The sample rate of the file.

## Examples


```
// Writing a sound file, long form:
// Set the format variables before calling 'openWrite'
// The Boolean answer from 'openWrite' tells you if it's safe to proceed
(
f = SoundFile(PathName.tmp +/+ "sf-help.wav");
f.headerFormat = "WAV";
f.sampleFormat = "int16";
if(f.openWrite) {
    f.writeData(Signal.sineFill(1024, [1]));
    f.close;
} {
    "Failed to open %".format(f.path).warn;
};
)

// Or, short form: Class method 'openWrite'
// f is nil if the file couldn't be opened
(
var p = PathName.tmp +/+ "sf-help.wav";
f = SoundFile.openWrite(p, "WAV", "int16");
if(f.notNil) {
    f.writeData(Signal.sineFill(1024, [1]));
    f.close;
} {
    "Failed to open %".format(p).warn;
};
)

// Reading the file
f = SoundFile.openRead(PathName.tmp +/+ "sf-help.wav");
f.sampleFormat;

// To get data, create a FloatArray or Signal first
d = FloatArray.newClear(f.numFrames);
f.readData(d);
d.plot;
f.close;

s.boot;

// It's a proper audio file -- server can load it
b = Buffer.read(s, PathName.tmp +/+ "sf-help.wav");

// It's a sinewave...
a = { (PlayBuf.ar(1, b, rate: 440 * 1024/44100, loop: 1) * 0.1).dup }.play;
a.free;

b.free;
File.delete(PathName.tmp +/+ "sf-help.wav");
```




