# Non-Realtime Synthesis (NRT)

*Non-realtime synthesis with binary files of OSC commands*

**Categories:** Server>NRT, External Control>OSC

**Related:** [Score](../Classes/Score.md)


## Realtime vs. Non-Realtime Synthesis
When you boot a SuperCollider server (scsynth, or supernova on supported systems) normally, it runs in *realtime* mode:

- The server is constantly processing audio, at a rate determined by the hardware sample rate.
- The server receives OSC commands over a network interface, and processes them either at the next available opportunity, or at a time specified by a timestamp.
- The server can also send OSC messages back to the client.


If the server starts with the -N switch, it runs in *non-realtime* (NRT) mode:

- The server processes audio as fast as possible, or as slow as necessary, depending only on workload. There is no attempt to synchronize with any other time reference.
- The server takes commands only from a file of OSC commands (a "score"), prepared in advance.
- There is no network connection and no interaction with the process while it is running.


**When to use NRT mode:** If the audio processing can be arranged fully in advance, and you need "faster-than-light" processing (or the processing is too heavy to complete in real time), NRT may be appropriate.

**When not to use NRT mode:** If you need to interact with the server process at specific times, NRT is not appropriate. For instance, if your code makes decisions about upcoming events based on data received from [SendReply](../Classes/SendReply.md), [Bus#-get](../Classes/Bus.md#-get) (`/c_get`) or [Buffer#-get](../Classes/Buffer.md#-get) (`/b_get`), or node notification messages, these data will not be available in NRT mode.



## Basic usage of Score
It is recommended to use a [Score](../Classes/Score.md) object to run NRT processes. A Score object:

- prepares the binary OSC file for you, in the correct format;
- manages NRT server processes;
- can optionally play the Score, or portions of it, in real time for testing.



```supercollider
(
var server = Server(\nrt,
    options: ServerOptions.new
    .numOutputBusChannels_(2)
    .numInputBusChannels_(2)
);

a = Score([
    [0.0, ['/d_recv',
        SynthDef(\NRTsine, { |out, freq = 440|
            Out.ar(out, SinOsc.ar(freq, 0, 0.2).dup)
        }).asBytes
    ]],
    [0.0, (x = Synth.basicNew(\NRTsine, server, 1000)).newMsg(args: [freq: 400])],
    [1.0, x.freeMsg]
]);

a.recordNRT(
    outputFilePath: "~/nrt-help.wav".standardizePath,
    headerFormat: "wav",
    sampleFormat: "int16",
    options: server.options,
    duration: 1,
    action: { "done".postln }
);

server.remove;
)
```



### Timed messages
A new Score object needs a list of commands, with times.

Each command is an array, e.g. `['/n_set', 1000, 'gate', 0]`.

Each command is bound to a time by placing it in another array, with the time (a floating point number, in beats) first:


```supercollider
[143.2647423, ['/n_set', 1000, 'gate', 0]]
```



> **Note:** Times are adjusted for the clock's tempo. [Score#*new](../Classes/Score.md#*new) allows you to specify a [TempoClock](../Classes/TempoClock.md); if you don't, then `TempoClock.default` will be used.


Server abstraction objects (Synth, Group, Buffer etc.) include methods to give you the OSC message. So, a Score may frequently include idioms such as:

- Create a group: `[time, Group.basicNew(server).newMsg]`
- Create a synth: `[time, Synth.basicNew(\defname, server).newMsg(target, args: [...])]`
- Read a buffer from disk: `[time, Buffer(server).allocReadMsg(path)]`



> **Note:** Normal usage of [Synth](../Classes/Synth.md) or [Buffer](../Classes/Buffer.md) communicates immediately with the server: `Synth.new(...)` transmits `/s_new`; `Buffer.alloc(server, ...)` sends `/b_alloc`. To build a NRT score, create the object as a placeholder (no immediate communication) and then ask a placeholder for the message: [Synth#*basicNew](../Classes/Synth.md#*basicnew) and [Synth#-newMsg](../Classes/Synth.md#-newmsg), or [Buffer#*new](../Classes/Buffer.md#*new) and [Buffer#-allocMsg](../Classes/Buffer.md#-allocmsg) or [Buffer#-allocReadMsg](../Classes/Buffer.md#-allocreadmsg). There is no need for a bus-allocation message simmilar to [Buffer#-allocMsg](../Classes/Buffer.md#-allocmsg). If you have only used realtime synthesis, this code style is unfamiliar, but it's worth practicing.(The result of, e.g., `newMsg` is already the array representing the message. So it is sufficient for each Score item to be an array containing the time and method call. The subarray should be explicit only when writing the message by hand.)


Consult help files for the server abstraction classes for additional "...Msg" methods.

If you save the result of `Synth.basicNew(...)` in a variable, then you can free it later using either [Node#-freeMsg](../Classes/Node.md#-freemsg) or [Node#-releaseMsg](../Classes/Node.md#-releasemsg), e.g.:


```supercollider
[1.0, (x = Synth.basicNew(\default, server)).newMsg(args: [freq: 200])],
[2.0, x.releaseMsg]
```


For [SynthDef](../Classes/SynthDef.md), there is no `addMsg` or `recvMsg` method. Add SynthDefs into the Score as follows:


```supercollider
[0.0, ['/d_recv', SynthDef(...).asBytes]]
```


Very large SynthDefs will need to be written to disk and *not* rendered as OSC messages in the Score. The SuperCollider language client limits the size of a single OSC message to 65516 bytes. If a SynthDef exceeds this limit, creation of the Score object will fail with the error message `ERROR: makeSynthMsgWithTags: buffer overflow`. Resolve this error message as follows:


```supercollider
(
SynthDef(\veryLarge, {
    // ... very large UGen graph...
}).writeDefFile;
)

(
x = Score([
    // Do NOT put a \d_recv message for \veryLarge here!
    // Allow the NRT server to read it from the disk file.
    ...
]);
)
```





### Rendering a Score using 'recordNRT'
To render the Score, use the [Score#-recordNRT](../Classes/Score.md#-recordnrt) method. Here is a rough template, followed by an explanation of the `recordNRT` parameters.


```supercollider
(
a = Score(...);

a.recordNRT(
    oscFilePath: ,
    outputFilePath: ,
    inputFilePath: ,
    sampleRate: ,
    headerFormat: ,
    sampleFormat: ,
    options: ,
    completionString: ,
    duration: ,
    action:
);
)
```



**oscFilePath**
: Recommended to omit (leave as `nil`). Score will generate a temporary filename for you.

**outputFilePath**
: The output audio file that you want (full path).

**inputFilePath**
: Optional. If you provide an existing audio file, its contents will stream to the NRT server's hardware input buses.

**sampleRate**
: Output file sample rate.

**headerFormat**
: See [SoundFile#-headerFormat](../Classes/SoundFile.md#-headerformat).

**sampleFormat**
: See [SoundFile#-sampleFormat](../Classes/SoundFile.md#-sampleformat).

**options**
: An instance of [ServerOptions](../Classes/ServerOptions.md). In particular, this is important to set the desired number of output channels, e.g. `ServerOptions.new.numOutputBusChannels_(2)`.

**completionString**
: Undocumented. No apparent purpose.

**duration**
: The desired total length of the output file, in seconds.

**action**
: A function to evaluate when rendering is complete.



Of these, `outputFilePath`, `options` and `duration` are particularly important. Make sure you specify at least these.


> **Note:** NRT processing continues until the last timestamp in the score file. If you specify a `duration` for recordNRT, Score will automatically append a dummy command at the end of the score, with the given timestamp, ensuring that the output file will be at least this long.


If you are repeatedly rendering NRT scores, you can set `Score.options = ServerOptions.new...` and `recordNRT` will use this set of server options by default.




### Score files
`recordNRT` allows you optionally to specify the path to the binary OSC score file. This is useful if you want to keep the file for archival purposes, or to delete the file in `recordNRT`'s action function.

If you do not give a path, `recordNRT` will generate one for you in the system's temporary file location. These files are not automatically deleted after rendering. Some systems may automatically clean up old temporary files after some time. Otherwise, you can take it into your own hands:


```supercollider
var oscPath = PathName.tmp +/+ "mytempscore";

x = Score([ ... ]);

x.recordNRT(oscFilePath: oscPath, ..., action: {
    File.delete(oscPath)
});
```





### Using system SynthDefs
Some code requires a number of SynthDefs that are assumed to exist on the server ([SystemSynthDefs](../Classes/SystemSynthDefs.md)). When booting a server in realtime mode, they are sent automatically. In non-realtime mode, they need to be added to the score explicitly:


```supercollider
x = Score.new;
x.addSystemSynthDefs;
```





### Server instance
If you want to use server abstraction objects (e.g. Synth, Group, Buffer), you might also want them to allocate node IDs or buffer and bus numbers for you. [Synth#*basicNew](../Classes/Synth.md#*basicnew) and [Buffer#*new](../Classes/Buffer.md#*new) use the server's allocators if you don't supply an ID (leave it nil). However, if you accidentally use the default server, any IDs you allocate for NRT will be marked as allocated in the default, realtime server. To avoid this, you can create a separate Server instance, just for producing the Score, and then remove the instance after rendering. This is a client-only object; you don't need to boot it.

It is technically incorrect to use the default server `s` for Score generation, but for quick and dirty uses, it may be acceptable. The examples in this document demonstrate the use of a dedicated Server object as a best practice. Following this best practice is likely to avoid problems in which NRT Score generation affect the default server instance; however, in common usage, such problems might not be severe. "At the user's own risk."




### Server resources
A NRT server is *a separate server process* from any other. Every time you run a Score, it launches a brand-new server process. Each new server starts with a blank slate. In particular, any SynthDefs you have added or Buffers you have loaded are not automatically available to the new server.

Therefore, your Score must include instructions to prepare these resources.

It is a very common mistake to load a buffer into a realtime server, and then run a non-realtime server, and find that resources are not available. For instance, this example adds a SynthDef in the normal way (added in memory only), and the SynthDef is not automatically transferred to the NRT server.


```supercollider
// Incorrect
(
SynthDef(\NRTsine, { |out, freq = 440|
    Out.ar(out, SinOsc.ar(freq, 0, 0.2).dup)
}).add;
)

(
var server = Server(\nrt,
    options: ServerOptions.new
    .numOutputBusChannels_(2)
    .numInputBusChannels_(2)
);

a = Score([
    [0.0, (x = Synth.basicNew(\NRTsine, server, 1000)).newMsg(args: [freq: 400])],
    [1.0, x.freeMsg]
]);

a.recordNRT(
    outputFilePath: PathName.tmp +/+ "nrt-help-fail.wav",
    headerFormat: "wav",
    sampleFormat: "int16",
    options: server.options,
    duration: 1,
    action: { "done".postln }
);

server.remove;
)
```




```supercollider
File.delete(PathName.tmp +/+ "nrt-help-fail.wav");
```



> **Note:** Another common technique to transmit SynthDefs to an NRT server is to use [SynthDef#-writeDefFile](../Classes/SynthDef.md#-writedeffile) to avoid this problem. This works by writing the SynthDef into the default SynthDef directory; then, the NRT server reads SynthDefs from the default location when it starts up. This approach is perfectly valid, but has the disadvantage of leaving `.scsyndef` files on disk that you might not need later. For that reason, this document demonstrates how to make SynthDefs available to NRT servers without using disk files.


The good news is that a NRT server does not have to wait for "heavy" operations like receiving SynthDefs or loading buffers. Commands that are considered asynchronous in a realtime server behave as synchronous commands in NRT. So, you can simply front-load your Score with all the SynthDefs and Buffers, at time 0.0, and then start the audio processing also at time 0.0. (However, you might need a slight offset for the audio processing because `sort` may not know which entries at time 0.0 must come first.) The following examples demonstrate.





## Examples

### Algorithmic generation of Synth messages
The preceding example, for simplicity, adds only one synth. Another approach is to create the initial Score with "setup" messages, and add further Synth messages for notes.


```supercollider
(
var server = Server(\nrt,
    options: ServerOptions.new
    .numOutputBusChannels_(2)
    .numInputBusChannels_(2)
),
defaultGroup = Group.basicNew(server);

var time = 0;

x = Score([
    [0.0, ['/d_recv',
        SynthDef(\singrain, { |out, freq = 440, time = 0.1, amp = 0.1|
            var eg = EnvGen.kr(Env.perc(0.01, time), doneAction: 2),
            sig = SinOsc.ar(freq) * amp;
            Out.ar(out, (sig * eg).dup);
        }).asBytes
    ]],
    [0.0, defaultGroup.newMsg]
]);

100.do {
    x.add([time, Synth.basicNew(\singrain, server)
        .newMsg(g, [freq: exprand(200, 800), time: exprand(0.1, 1.0)])
    ]);
    time = time + exprand(0.02, 0.25)
};

x.recordNRT(
    outputFilePath: "~/nrt.wav".standardizePath,
    sampleRate: 44100,
    headerFormat: "wav",
    sampleFormat: "int16",
    options: server.options,
    duration: x.endTime + 1
);

server.remove;
)
```





### NRT processing of an audio file
Applying a custom effect to a very long audio file is an especially good use of NRT: create a Score that defines an effect SynthDef and runs it for the duration of of the input file. You can use `recordNRT`'s input file parameter to pipe the source audio to the NRT server's hardware inputs, and read it with [SoundIn](../Classes/SoundIn.md).

The example audio file is not very long, but processing here is almost instantaneous.


```supercollider
(
var server,
inputFile = SoundFile.openRead(ExampleFiles.child);

inputFile.close;  // doesn't need to stay open; we just need the stats

server = Server(\nrt,
    options: ServerOptions.new
    .numOutputBusChannels_(2)
    .numInputBusChannels_(inputFile.numChannels)
);

x = Score([
    [0.0, ['/d_recv',
        SynthDef(\fft, {
            var in = SoundIn.ar([0]),
            fft = FFT(LocalBuf(1024, 1), in);
            fft = PV_MagFreeze(fft, ToggleFF.kr(Dust.kr(12)));
            Out.ar(0, IFFT(fft).dup)
        }).asBytes
    ]],
    [0.0, Synth.basicNew(\fft, server).newMsg]
]);

x.recordNRT(
    outputFilePath: "~/nrt.wav".standardizePath,
    inputFilePath: inputFile.path,
    sampleRate: 44100,
    headerFormat: "wav",
    sampleFormat: "int16",
    options: server.options,
    duration: inputFile.duration
);

server.remove;
)
```





### Generating NRT scores from patterns
Event patterns can be converted into Scores by `asScore`. (Note that `asScore` internally creates a Server instance to use for allocators. So, it is not necessary for this example to create a Server.)

First, a simple example using the default SynthDef. Note that the default SynthDef is not stored to disk by default, so it is necessary to include it in the score. The slight time offset in `asScore` is necessary to be sure that the SynthDef message comes first.


```supercollider
(
x = Pbind(
    \freq, Pexprand(200, 800, inf),
    \dur, Pexprand(0.8, 1.25, inf) * Pgeom(0.01, 1.0143978590819, 400),
    \legato, 3,
).asScore(10, timeOffset: 0.001);

x.add([0.0, [\d_recv, SynthDescLib.global[\default].def.asBytes]]);
x.sort;

x.recordNRT(
    outputFilePath: "~/nrt.wav".standardizePath,
    sampleRate: 44100,
    headerFormat: "wav",
    sampleFormat: "int16",
    options: ServerOptions.new.numOutputBusChannels_(2),
    duration: 10
);
)
```


To use Buffers and Buses, it is recommended to avoid conflicts with real-time server instances by creating a Server object just for the non-realtime process. It is not necessary to boot this server, only to use its allocators. After rendering, you may safely `remove` the server instance.


```supercollider
(
var server = Server(\nrt,
    options: ServerOptions.new
    .numOutputBusChannels_(2)
    .numInputBusChannels_(2)
),
def = SynthDef(\buf1, { |out, bufnum, rate = 1, time = 0.1, start = 0, amp = 0.1|
    var eg = EnvGen.kr(Env.perc(0.01, time), doneAction: 2),
    sig = PlayBuf.ar(1, bufnum, rate, startPos: start);
    Out.ar(out, (sig * (eg * amp)).dup);
}),
// the pattern needs a placeholder for the buffer
buf = Buffer.new(server, 0, 1);

def.add;  // the pattern needs the def in the SynthDescLib

x = Pbind(
    \instrument, \buf1,
    \bufnum, buf,
    \rate, Pexprand(0.5, 2, inf),
    \start, Pwhite(0, 50000, inf),
    \time, 0.1,
    \dur, Pexprand(0.05, 0.5, inf),
    \legato, 3,
).asScore(duration: 20, timeOffset: 0.001);

// the score also needs the def and buffer
x.add([0.0, [\d_recv, def.asBytes]]);
x.add([0.0, buf.allocReadMsg(ExampleFiles.child)]);
x.sort;

x.recordNRT(
    outputFilePath: "~/nrt.wav".standardizePath,
    sampleRate: 44100,
    headerFormat: "wav",
    sampleFormat: "int16",
    options: server.options,
    duration: 20
);

server.remove;
)
```


See also [Pproto](../Classes/Pproto.md) for another way to initialize buffers and other resources within a pattern object. Not every type of resource is supported in `Pproto`, but for typical cases, it may be more convenient than the above approach.




### Analysis using a Non-Realtime server
An NRT server may also be used to extract analytical data from a sound file. The main issues are:


**Suppressing audio file output**
: In macOS and Linux environments, use `/dev/null` for the output file path. In Windows, use `NUL`.

**Retrieving analytical data.**
: The easiest way is to allocate a buffer at the beginning of the NRT score, and use BufWr to fill the buffer. At the end of the score, write the buffer into a temporary file. Then you can use SoundFile on the language side to access the data. See the example.




```supercollider
// Example: Extract onsets into a buffer.

(
fork {
    var server = Server(\nrt,
        options: ServerOptions.new
        .numOutputBusChannels_(2)
        .numInputBusChannels_(2)
    );
    var resultbuf, resultpath, oscpath, score, dur, sf, cond, size, data;

    // get duration
    sf = SoundFile.openRead(ExampleFiles.child);
    dur = sf.duration;
    sf.close;

    resultpath = PathName.tmp +/+ UniqueID.next ++ ".wav";
    oscpath = PathName.tmp +/+ UniqueID.next ++ ".osc";

    score = Score([
        [0, (resultbuf = Buffer.new(server, 1000, 1, 0)).allocMsg],
        [0, [\d_recv, SynthDef(\onsets, {
            var sig = SoundIn.ar(0), // will come from NRT input file
            fft = FFT(LocalBuf(512, 1), sig),
            trig = Onsets.kr(fft),
            // count the triggers: this is the index to save the data into resultbuf
            i = PulseCount.kr(trig),
            // count time in seconds
            timer = Sweep.ar(1);
            // 'i' must be audio-rate for BufWr.ar
            BufWr.ar(timer, resultbuf, K2A.ar(i), loop: 0);
            BufWr.kr(i, resultbuf, DC.kr(0), 0);  // # of points in index 0
        }).asBytes]],
        [0, Synth.basicNew(\onsets, server, 1000).newMsg],
        [dur, resultbuf.writeMsg(resultpath, headerFormat: "wav", sampleFormat: "float")]
    ]);

    cond = Condition.new;

    // osc file path, output path, input path - input is soundfile to analyze
    score.recordNRT(oscpath, "/dev/null", sf.path, sampleRate: sf.sampleRate,
        options: ServerOptions.new
            .verbosity_(-1)
            .numInputBusChannels_(sf.numChannels)
            .numOutputBusChannels_(sf.numChannels)
            .sampleRate_(sf.sampleRate),
        action: { cond.unhang }  // this re-awakens the process after NRT is finished
    );
    cond.hang;  // wait for completion

    sf = SoundFile.openRead(resultpath);
    // get the size: one frame at the start
    sf.readData(size = FloatArray.newClear(1));
    size = size[0];
    // now the rest of the data
    sf.readData(data = FloatArray.newClear(size));
    sf.close;

    File.delete(oscpath);
    File.delete(resultpath);
    server.remove;

    data.postln;  // these are your onsets!
};
)
```






## OSC file format
If, for some reason, you need to write the OSC command file yourself without using Score, the general method is:

1. Open a file for writing: `File(path, "w")`.
2. For each OSC command:1. Create the command as an array, and save it in a variable such as `cmd`.
2. Convert to binary: `cmd = cmd.asRawOSC;`
3. Write the byte size as an integer: `file.write(cmd.size);`
4. Write the binary command: `file.write(cmd);`




```supercollider
f = File(PathName.tmp +/+ "Cmds.osc", "w");

// start a sine oscillator at 0.2 seconds.
c = [0.2, [\s_new, \default, 1001, 0, 0]].asRawOSC;
f.write(c.size); // each bundle is preceded by a 32 bit size.
f.write(c); // write the bundle data.

// stop sine oscillator at 3.0 seconds.
c = [3.0, [\n_free, 1001]].asRawOSC;
f.write(c.size);
f.write(c);

// scsynth stops processing immediately after the last command, so here is
// a do-nothing command to mark the end of the command stream.
c = [3.2, [0]].asRawOSC;
f.write(c.size);
f.write(c);

f.close;

// after rendering, always remember to clean up your mess:
File.delete(PathName.tmp +/+ "Cmds.osc");
```




## Bus allocation and synth/LFO mapping
In this example, a control bus and LFO map is used to have various affects on the source sound.


```supercollider
(
var nrtserver = Server(\nrt,
    options: ServerOptions.new
    .numOutputBusChannels_(2)
    .numInputBusChannels_(2)
);

//control bus allocation
var bus = Bus.control(nrtserver, 2);
var lfo, sine;

//LFO
SynthDef.new(\lfo, {|out, freq=100|
    Out.kr(out, LFNoise0.kr(freq).exprange(20.0,1000))
}).load;

lfo = Synth.basicNew(\lfo, server: nrtserver);

SynthDef.new(\NRTsine, {|out=0, freq=440|
    Out.ar(out, SinOsc.ar(freq, 0, 0.2).dup)
}).load;

sine = Synth.basicNew(\NRTsine, server: nrtserver);

a = Score([
    [0.0, lfo.newMsg(args:[\out, bus])],
    [0.0, sine.newMsg],
    [0.0, sine.mapMsg(\freq, bus)],
]);

a.recordNRT(
    outputFilePath: "~/nrtbus-help.wav".standardizePath,
    headerFormat: "wav",
    sampleFormat: "int16",
    options: nrtserver.options,
    duration: 1,
    action: { "done".postln }
);

nrtserver.remove;
)
```






