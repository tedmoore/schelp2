# IndexL

*Index into a table with a signal, linear interpolated*

**Categories:** UGens>Buffer

**Related:** [Index](../Classes/Index.md), [IndexInBetween](../Classes/IndexInBetween.md)

## Description

The input signal value is used as an index into the table, with linear interpolation. Out of range index values are clipped to the valid range.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bufnum` | index of the buffer. |  
| `in` | the input signal. |  

## Examples


```supercollider
// indexing into a fixed table
(
{
    SinOsc.ar(
        IndexL.kr(
            LocalBuf.newFrom([200, 300, 400, 500, 600, 800].scramble),
            LFSaw.kr(2.0).range(0, 7)
        ),
        0,
        0.5
    )
}.play;
)

// with mouse control
(
{
    SinOsc.ar(
        IndexL.kr(
            LocalBuf.newFrom([200, 300, 400, 500, 600, 800].scramble),
            MouseX.kr(0, 7)
        ),
        0,
        0.5
    )
}.play;
)

(
// indexing into a changeable table
t = [200, 300, 400, 500, 600, 800];
b = Buffer(s, t.size, 1);

// alloc and set the values
s.listSendMsg(b.allocMsg(b.setnMsg(0, t)).postln);

SynthDef(\help_index, { |out = 0, bufnum = 0|
    Out.ar(out,
        SinOsc.ar(
            IndexL.kr(
                bufnum,
                LFSaw.kr(2).range(0, BufFrames.kr(bufnum))
            ),
            0,
            0.5
        )
    )
}).play(s, [\bufnum, b]);
)

b.setn(*[200, 300, 400, 500, 600, 800].scramble.postln - 30);


(
SynthDef(\help_index, { |out = 0, bufnum = 0|
    Out.ar(out,
        SinOsc.ar(
            IndexL.kr(
                bufnum,
                MouseX.kr(0, BufFrames.ir(bufnum))
            ),
            0,
            0.5
        )
    )
}).play(s, [\bufnum, b]);
)

b.free;
```




