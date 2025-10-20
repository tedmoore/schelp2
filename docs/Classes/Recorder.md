# Recorder

*Write Audio to Harddisk*

**Categories:** Server>Abstractions

**Related:** [Server](../Classes/Server.md), [DiskOut](../Classes/DiskOut.md), [Non-Realtime-Synthesis](../Guides/Non-Realtime-Synthesis.md)

## Description

A Recorder allows you to write audio to harddisk, reading from a given bus and a certain number of channels, relative to a given node. A [Server](../Classes/Server.md) has one instance, which is accessible also through the [ScIDE](../Classes/ScIDE.md). You can use the server directly to record its output

```
(
{ SinOsc.ar(
    SinOsc.ar(
        XLine.kr(1, 100, 5)).exprange(*XLine.kr([20, 800], [7000, 200], 10)
    )
   ) * 0.1

}.play;
s.record(duration: 10);
)
```


This functionality is also available through the recording button on the server windows. Pressing it once calls record, and pressing it again calls stopRecording (see below). When doing so the file created will be in your recordings folder and be named for the current date and time. The default location of the recordings folder varies from platform to platform. Setting this variable allows you to change the default.

```
// find where the recordings are written to
thisProcess.platform.recordingsDir
```



> **Note:** By default, record creates the recording synth after the Server's default group and uses In.ar. Thus if you add nodes after the recording synth their output will not be captured. To avoid this, either use Node objects (which use the default node as their target) or (when using messaging style) use a target nodeID of 1.
```
s.sendMsg("/s_new", "default", s.nextNodeID, 1, 1);
```


For more detail on this subject see [Order-of-execution](../Guides/Order-of-execution.md), [default_group](../Reference/default_group.md), and [NodeMessaging](../Guides/NodeMessaging.md).
See [SoundFile](../Classes/SoundFile.md) for information on the various sample and header formats. Not all sample and header formats are compatible. Note that the sampling rate of the output file will be the same as that of the server app. This can be set using the Server's [ServerOptions](../Classes/ServerOptions.md).


## Class Methods


### `new`
Create a new instance for a given server.**Arguments:**

| Argument | Description |
|----------|-------------|
| `server` |  |  


## Instance Methods


### `prepareForRecord`
Allocates the necessary buffer, etc. for recording the server's output. (See `record` below.)**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` | a [String](../Classes/String.md) representing the path and name of the output file. If the directory does not exist, it will be created for you. (Note, however, that if this fails for any reason, recording will also fail.) |  
| `numChannels` | The number of output channels to record. |  
If you do not specify a path than a file will be created in your recordings folder (see the note above on this) called `SC_thisDateAndTime`. Changes to the header or sample format, or to the number of channels must be made **before** calling this.
### `record`
Starts or resumes recording the output.**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` | this is optional, and is passed to `prepareForRecord` (above). |  
| `bus` | The bus ([Bus](../Classes/Bus.md) object or integer bus index), the offset at which to start to count the number of channels. You can record any adjacent number of bus channels. |  
| `numChannels` | The number of output channels to record. |  
| `node` | The [Node](../Classes/Node.md) to record immediately after. By default, this is the default group 1. |  
| `duration` | If set, this limits recording to a given time in seconds.
> **Note:** The recording starts when the buffer has been allocated, and after the usually very short network latency. It will last for the `duration` exactly down to one server block size (64 samples). For scheduling the starting point of a recording precisely, call [#-prepareForRecord](#-prepareforrecord) first, and then call [#-record](#-record) a bundle (see [Server#-bind](../Classes/Server.md#-bind) and [Server#-sync](../Classes/Server.md#-sync)). |  
If you have not called prepareForRecord first (see above) then it will be invoked for you (but that adds a slight delay before recording starts for real).
```
r = Recorder(s);
{ GVerb.ar(Dust.ar(4)) }.play; // play on bus 64
r.record(numChannels: 2);
r.stopRecording;
```


### `pauseRecording`
Pauses recording. Can be resumed by executing record again, or by calling resumeRecording.
### `resumeRecording`
Start recording again.
### `stopRecording`
Stops recording, closes the file, and frees the associated resources.You must call this when finished recording or the output file will be unusable. Cmd-. while recording has the same effect.
### `filePrefix`
a string used as prefix for the path when recording. This can be used to separate the outputs of several recorders. The default is `"SC_"`.
### `numChannels`
a number of sound file channels that is used always when using this recorder, unless a different one is specified in the [#-record](#-record) method. When not set, we use [Server#-recChannels](../Classes/Server.md#-recchannels).
### `recHeaderFormat`
Get/set the header format (string) of the output file. The default is "wav". Must be called **before** prepareForRecord.
### `recSampleFormat`
Get/set the sample format (string) of the output file. The default is "float". Must be called **before** prepareForRecord.
### `recBufSize`
Get/set the size of the [Buffer](../Classes/Buffer.md) to use with the [DiskOut](../Classes/DiskOut.md) UGen. This must be a power of two. The default is the `sampleRate.nextPowerOfTwo` or the first power of two number of samples longer than one second. Must be called **before** prepareForRecord.
### `isRecording`
returns true if we are in the process of recording
### `paused`
returns true if recording is paused
### `duration`
returns the number of seconds we have been recording so far
### `path`
returns the path of the current recording
### `numFrames`
returns the number of frames of the recording buffer
### `notifyServer`
if set to true, it will send `changed` notifications to the server instance. This is used internally by the [Server](../Classes/Server.md) class.
### `server`
server to record from

## Examples

```
// something to record
(
SynthDef("bubbles", { |out|
    var f, sound;
    f = LFSaw.kr(0.4, 0, 24, LFSaw.kr([8, 7.23], 0, 3, 80)).midicps; // glissando function
    sound = CombN.ar(SinOsc.ar(f, 0, 0.04), 0.2, 0.2, 4); // echoing sine wave
    Out.ar(out, sound);
}).add;

SynthDef("tpulse", { |out = 0, freq = 700, sawFreq = 440.0|
    Out.ar(out, SyncSaw.ar(freq, sawFreq, 0.1))
}).add;

)

x = Synth.new("bubbles");

s.prepareForRecord; // if you want to start recording on a precise moment in time, you have to call this first.

s.record; // start recording. This can also be called directly, if it isn't imprtant when precisely you need to start.

s.pauseRecording; // pausable

s.record // start again

s.stopRecording; // this closes the file and deallocates the buffer recording node, etc.

x.free; // stop the synths

// look in your recordings folder and you'll find a file named for this date and time
```



```
// set location to your home folder (change user with your username)
thisProcess.platform.recordingsDir = "/home/user/";

// instantiate the Recorder
r = Recorder.new(s);

// record into a flac file
r.recHeaderFormat = "flac";

// default 'float' is incompatible with flac. set to 24bit:
r.recSampleFormat = "int24";

// set very obvious prefix for files
r.filePrefix = "SuperCollider_";

// start recording:
r.record;

// stop recording
r.stopRecording;
```






