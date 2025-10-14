# Score

*score of timed OSC commands*

**Related:** [Non-Realtime-Synthesis](../Guides/Non-Realtime-Synthesis.md)

**Categories:** Control, Server>NRT, External Control>OSC

## Description

Score encapsulates a list of timed OSC commands and provides some methods for using it, as well as support for the creation of binary OSC files for non-realtime synthesis. See [Non-Realtime-Synthesis](../Guides/Non-Realtime-Synthesis.md) for more details.
The list should be in the following format, with times in ascending order. Bundles are okay.

```supercollider
[
[beat1, [OSCcmd1]],
[beat2, [OSCcmd2], [OSCcmd3]],
...
[beat_n, [OSCcmdn]],
[beatToEndNRT, [\c_set, 0, 0]] // finish
]
```


For NRT synthesis the final event should a dummy event, after which synthesis will cease. It is thus important that this event be timed to allow previous events to complete.
Score scheduling defaults to [TempoClock](../Classes/TempoClock.md). A setting of `TempoClock.default.tempo = 1` (60 beats per minute), may be used to express score events in seconds if desired.


## Class Methods


### `new`
returns a new Score object with the supplied list.**Arguments:**

| Argument | Description |
|----------|-------------|
| `list` | can be an [Array](../Classes/Array.md), a [List](../Classes/List.md), or similar object. |  

### `newFromFile`
as [#*new](#*new), but reads the list in from a text file.**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` | a [String](../Classes/String.md) indicating the path of the file. The file must contain a valid SC expression. |  

### `play`
as [#*new](#*new) but immediately plays it. (See also the instance method below.)**Arguments:**

| Argument | Description |
|----------|-------------|
| `list` | the list. |  
| `server` | If no value is supplied it will play on the default [Server](../Classes/Server.md). |  

### `playFromFile`
as [#*play](#*play), but reads the list from a file.
### `write`
a convenience method to create a binary OSC file for NRT synthesis. Does not create an instance.**Arguments:**

| Argument | Description |
|----------|-------------|
| `list` | the list. |  
| `oscFilePath` | a [String](../Classes/String.md) containing the desired path of the OSC file. |  
| `clock` | Use clock as a tempo base. `TempoClock.default` is used if clock is nil. |  

### `writeFromFile`
as [#*write](#*write) but reads the list from a file.**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` | a path to a file with a list. |  
| `oscFilePath` | a [String](../Classes/String.md) containing the desired path of the OSC file. |  
| `clock` | Use clock as a tempo base. `TempoClock.default` is used if clock is nil. |  

### `recordNRT`
a convenience method to synthesize **list** in non-realtime. This method writes an OSC file to **oscFilePath** (you have to do your own cleanup if desired) and then starts a server app to synthesize it. For details on valid headerFormats and sampleFormats see [SoundFile](../Classes/SoundFile.md). Use `TempoClock.default` as a tempo base. Does not return an instance.**Arguments:**

| Argument | Description |
|----------|-------------|
| `list` | the list. |  
| `oscFilePath` | the path to which the binary OSC file will be written. |  
| `outputFilePath` | the path of the resultant soundfile. |  
| `inputFilePath` | an optional path for an input soundfile. |  
| `sampleRate` | the sample rate at which synthesis will occur. |  
| `headerFormat` | the header format of the output file. The default is 'AIFF'. |  
| `sampleFormat` | the sample format of the output file. The default is 'int16'. |  
| `options` | an instance of [ServerOptions](../Classes/ServerOptions.md). If not supplied the options of the default [Server](../Classes/Server.md) will be used. |  
| `completionString` |  |  
| `duration` |  |  
| `action` | A function to be evaluated once the NRT server has finished rendering its score. |  


## Instance Methods

### `play`
play the list on **server**, use **clock** as a tempo base and quantize start time to **quant**. If **server** is nil, then on the default server. `TempoClock.default` if **clock** is nil. now if **quant** is 0.### `stop`
stop playing.### `write`
create a binary OSC file for NRT synthesis from the list. Use **clock** as a tempo base. `TempoClock.default` if **clock** is nil.### `score`
get or set the list.### `add`
adds bundle to the list.### `addSystemSynthDefs`
Some code requires a number of SynthDefs that are assumed to exist on the server ([SystemSynthDefs](../Classes/SystemSynthDefs.md)). When booting a server in realtime mode, they are sent automatically. In non-realtime mode, they need to be added to the score explicitly:
```supercollider
x = Score.new;
x.addSystemSynthDefs;
x.score
```

### `sort`
sort the score time order. This is recommended to do **before recordNRT or write** when you are not sure about the packet order.### `recordNRT`
synthesize the score in non-realtime. For details of the arguments see [#*recordNRT](#*recordnrt) above.### `saveToFile`
save the score list as a text file to **path**.
## Examples


### NRT Examples

```supercollider
// A sample synthDef
// Here we use store instead of add to store the compiled synthdef in Platform.defaultTempDir +/+ "synthdefs/"
// and make it available to the NRT server
(
SynthDef("helpscore", { |out, freq = 440|
    Out.ar(out,
        SinOsc.ar(freq, 0, 0.2) * Line.kr(1, 0, 0.5, doneAction: Done.freeSelf)
    )
}).store;
)

// write a sample file for testing
(
var f, g;
TempoClock.default.tempo = 1;
g = [
    [0.1, [\s_new, \helpscore, 1000, 0, 0, \freq, 440]],
    [0.2, [\s_new, \helpscore, 1001, 0, 0, \freq, 660]],
    [0.3, [\s_new, \helpscore, 1002, 0, 0, \freq, 220]],
    [1, [\c_set, 0, 0]] // finish
    ];
f = File(Platform.defaultTempDir +/+ "score-test", "w");
f.write(g.asCompileString);
f.close;
)

// convert it to a binary OSC file for use with NRT
Score.writeFromFile(Platform.defaultTempDir +/+ "score-test", Platform.defaultTempDir +/+ "test.osc");
```


From the command line, the file can then be rendered from within the build directory:


```supercollider
scsynth -N test.osc _ test.aif 44100 AIFF int16 -o 1
```


Score also provides methods to do all this more directly:


```supercollider
(
var f, o;
g = [
    [0.1, [\s_new, \helpscore, 1000, 0, 0, \freq, 440]],
    [0.2, [\s_new, \helpscore, 1001, 0, 0, \freq, 660],
        [\s_new, \helpscore, 1002, 0, 0, \freq, 880]],
    [0.3, [\s_new, \helpscore, 1003, 0, 0, \freq, 220]],
    [1, [\c_set, 0, 0]] // finish
    ];
o = ServerOptions.new.numOutputBusChannels = 1; // mono output
Score.recordNRT(g, Platform.defaultTempDir +/+ "help-oscFile", Platform.defaultTempDir +/+ "helpNRT.aiff", options: o); // synthesize
)
```




### Real-time Examples

```supercollider
s.boot; // boot the default server

// A sample synthDef
(
SynthDef("helpscore", { |out, freq = 440|
    Out.ar(out,
        SinOsc.ar(freq, 0, 0.2) * Line.kr(1, 0, 0.5, doneAction: Done.freeSelf)
    )
}).store;
)

// write a sample file for testing
(
var f, g;
TempoClock.default.tempo = 1;
g = [
    [0.1, [\s_new, \helpscore, 1000, 0, 0, \freq, 440]],
    [0.2, [\s_new, \helpscore, 1001, 0, 0, \freq, 660],
        [\s_new, \helpscore, 1002, 0, 0, \freq, 880]],
    [0.3, [\s_new, \helpscore, 1003, 0, 0, \freq, 220]],
    [1, [\c_set, 0, 0]] // finish
    ];
f = File(Platform.defaultTempDir +/+ "score-test", "w");
f.write(g.asCompileString);
f.close;
)

z = Score.newFromFile(Platform.defaultTempDir +/+ "score-test");

// play it on the default server
z.play;

// change the list
(
x = [
[0.0, [\s_new, \helpscore, 1000, 0, 0, \freq, 1413]],
[0.1, [\s_new, \helpscore, 1001, 0, 0, \freq, 712]],
[0.2, [\s_new, \helpscore, 1002, 0, 0, \freq, 417]],
[0.3, [\s_new, \helpscore, 1003, 0, 0, \freq, 1238]],
[0.4, [\s_new, \helpscore, 1004, 0, 0, \freq, 996]],
[0.5, [\s_new, \helpscore, 1005, 0, 0, \freq, 1320]],
[0.6, [\s_new, \helpscore, 1006, 0, 0, \freq, 864]],
[0.7, [\s_new, \helpscore, 1007, 0, 0, \freq, 1033]],
[0.8, [\s_new, \helpscore, 1008, 0, 0, \freq, 1693]],
[0.9, [\s_new, \helpscore, 1009, 0, 0, \freq, 410]],
[1.0, [\s_new, \helpscore, 1010, 0, 0, \freq, 1349]],
[1.1, [\s_new, \helpscore, 1011, 0, 0, \freq, 1449]],
[1.2, [\s_new, \helpscore, 1012, 0, 0, \freq, 1603]],
[1.3, [\s_new, \helpscore, 1013, 0, 0, \freq, 333]],
[1.4, [\s_new, \helpscore, 1014, 0, 0, \freq, 678]],
[1.5, [\s_new, \helpscore, 1015, 0, 0, \freq, 503]],
[1.6, [\s_new, \helpscore, 1016, 0, 0, \freq, 820]],
[1.7, [\s_new, \helpscore, 1017, 0, 0, \freq, 1599]],
[1.8, [\s_new, \helpscore, 1018, 0, 0, \freq, 968]],
[1.9, [\s_new, \helpscore, 1019, 0, 0, \freq, 1347]],
[2.0, [\c_set, 0, 0]] // finish
];

z.score_(x);
)

// play it
z.play;

// play and stop after one second
(
z.play;
SystemClock.sched(1.0, { z.stop });
)
```




### creating Score from a pattern

```supercollider
(
SynthDef("helpscore", { |out, freq = 440|
    Out.ar(out,
        SinOsc.ar(freq, 0, 0.2) * Line.kr(1, 0, 0.5, doneAction: Done.freeSelf)
    )
}).store;
)

// new pattern
(
p = Pbind(
    \instrument, \helpscore,
    \dur, Prand([0.3, 0.5], inf),
    \freq, Prand([200, 300, 500], inf)
);
)

// make a score from the pattern, 4 beats long
z = p.asScore(4.0);
z.score.postcs;
z.play;

// rendering a pattern to sound file directly:
// render the pattern to wav (4 beats)
p.render(Platform.defaultTempDir +/+ "asScore-Help.wav", 4.0);
```






