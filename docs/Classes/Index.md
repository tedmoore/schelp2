# Index

*Index into a table with a signal*

**Related:** [WrapIndex](../Classes/WrapIndex.md), [Shaper](../Classes/Shaper.md)

**Categories:** UGens>Buffer

## Description

Index into a table with a signal. The input signal value is truncated to an integer value and used as an index into the table. Out-of-range index values are clipped to the valid range.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bufnum` | Index of the buffer. |  
| `in` | The input signal. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```
// indexing into a fixed table
(
{
    SinOsc.ar(
        Index.kr(
            LocalBuf.newFrom([200, 300, 400, 500, 600, 800]),
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
        Index.kr(
            LocalBuf.newFrom([200, 300, 400, 500, 600, 800]),
            MouseX.kr(0, 7)
        ),
        0,
        0.5
    )
}.play;
)

(
// indexing into a changeable table
s = Server.local;
t = [200, 300, 400, 500, 600, 800];
b = Buffer(s, t.size, 1);

// alloc and set the values
s.listSendMsg(b.allocMsg(b.setnMsg(0, t)).postln);

SynthDef(\help_Index, { |out = 0, bufnum = 0|
    Out.ar(out,
        SinOsc.ar(
            Index.kr(
                bufnum,
                LFSaw.kr(2).range(0, 7)
            ),
            0,
            0.5
        )
    )
}).play(s, [\bufnum, b]);
)

b.setn(*[200, 300, 400, 500, 600, 800].scramble.postln - 30);


(
SynthDef(\help_Index, { |out = 0, bufnum = 0|
    Out.ar(out,
        SinOsc.ar(
            Index.kr(
                bufnum,
                MouseX.kr(0, BufFrames.ir(i_bufnum))
            ),
            0,
            0.5
        )
    )
}).play(s, [\bufnum, b]);
)

b.free;
```




