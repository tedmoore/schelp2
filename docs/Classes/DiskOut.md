# DiskOut

*Record to a soundfile to disk.*

**Related:** [RecordBuf](../Classes/RecordBuf.md), [DiskIn](../Classes/DiskIn.md), [VDiskIn](../Classes/VDiskIn.md)

**Categories:** UGens>InOut, UGens>Buffer

## Description

Record to a soundfile to disk. Uses a [Buffer](../Classes/Buffer.md).
See [RecordBuf](../Classes/RecordBuf.md) for recording into a buffer in memory.

### Disk recording procedure
Recording to disk involves several steps, which should be taken in the right order. [Server#-record](../Classes/Server.md#-record) performs these steps for you. To record arbitrary buses using DiskOut explicitly, make sure to do the following:

1. Define a DiskOut [SynthDef](../Classes/SynthDef.md), as shown in the example below.
2. Allocate a [Buffer](../Classes/Buffer.md) for recording.- The buffer size should be a power of two.
- A duration of at least one second is recommended: `s.sampleRate.nextPowerOfTwo`.
- Do not allocate the buffer inside the SynthDef.
- Keep the buffer in a variable.

3. Specify the file path and recording format using [Buffer#-write](../Classes/Buffer.md#-write), with the `leaveOpen` flag set to `true`. This is the only way to set the file path and recording format.
4. Create a [Synth](../Classes/Synth.md) node to run the DiskOut UGen.
5. When recording is finished, stop the DiskOut synth.
6. Close the buffer: `b.close`. This step updates the recorded file's audio header. Without it, the file will be unusable.
7. Free the buffer: `b.free`.


These steps are illustrated in the Examples section. In general, only the "Object Style" approach is needed. ("Messaging Style" is provided as a historical reference, but it isn't needed for typical use.)




## Class Methods


### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bufnum` | The number of the buffer to write to (prepared with /b-write or Buffer.write)
> **Note:** The Buffer's numFrames must be a power of two and is recommended to be at least 65536 -- preferably 131072 or 262144. Smaller buffer sizes mean more frequent disk access, which can cause glitches. |  
| `channelsArray` | The Array of channels to write to the file.
> **Note:** The number of channels in the buffer and the channelsArray must be the same, otherwise DiskOut will fail silently (and not write anything to your file). |  
**Returns:** The number of frames written to disk.

## Instance Methods


## Examples


```supercollider
s.boot; // start the server
(
// something to record
SynthDef("bubbles", { |out|
    var f, zout;
    f = LFSaw.kr(0.4, 0, 24, LFSaw.kr([8, 7.23], 0, 3, 80)).midicps; // glissando function
    zout = CombN.ar(SinOsc.ar(f, 0, 0.04), 0.2, 0.2, 4); // echoing sine wave
    Out.ar(out, zout)
}).add;

// this will record to the disk
SynthDef("help-Diskout", { |bufnum|
    DiskOut.ar(bufnum, In.ar(0, 2));
}).add;

// this will play it back
SynthDef("help-Diskin-2chan", { |out, bufnum = 0|
    Out.ar(out, DiskIn.ar(2, bufnum))
}).add;
)
```



### Object Style

```supercollider
// start something to record
x = Synth("bubbles");

// allocate a disk i/o buffer
b = Buffer.alloc(s, 65536, 2);

// create an output file for this buffer, leave it open
b.write("~/diskouttest.wav".standardizePath, "wav", "int16", 0, 0, true);
// create the diskout node; making sure it comes after the source
d = Synth.tail(nil, "help-Diskout", ["bufnum", b]);
// stop recording
d.free;
// stop the bubbles
x.free;
// close the buffer and the soundfile
b.close;
// free the buffer
b.free;

// play it back
(
x = Synth.basicNew("help-Diskin-2chan");
m = { |buf| x.addToHeadMsg(nil, [\bufnum, buf]) };

b = Buffer.cueSoundFile(s, "~/diskouttest.wav".standardizePath, 0, 2, completionMessage: m);
)
x.free; b.close; b.free; // cleanup
```




### Messaging Style

```supercollider
// The same thing done in Messaging Style (less overhead but without the convenience of objects)
// This does nothing different from the Messaging Style example.
// If any of the following is confusing, stick to Object Style
// and ignore this part.

// start something to record
s.sendMsg("/s_new", "bubbles", 2003, 1, 1);

// allocate a disk i/o buffer
s.sendMsg("/b_alloc", 0, 65536, 2); // Buffer number is 0

// create an output file for this buffer, leave it open
s.sendMsg("/b_write", 0, "~/diskouttest.wav".standardizePath, "wav", "int16", 0, 0, 1);

// create the diskout node
s.sendMsg("/s_new", "help-Diskout", 2004, 3, 2003, "bufnum", 0);

s.sendMsg("/n_free", 2004); // stop recording
s.sendMsg("/n_free", 2003); // stop the bubbles

s.sendMsg("/b_close", 0); // close the file.
s.sendMsg("/b_free", 0);
```






