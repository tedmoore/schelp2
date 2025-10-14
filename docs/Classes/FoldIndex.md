# FoldIndex

*Index into a table with a signal.*

**Related:** [Index](../Classes/Index.md), [Shaper](../Classes/Shaper.md)

**Categories:** UGens>Buffer

## Description

The input signal value is truncated to an integer value and used as an index into the table. Out-of-range index values are folded into the valid range.


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


```supercollider
// indexing into a table
(
{
    var buf = LocalBuf.newFrom([200, 300, 400, 500, 600, 800]);
    var freq = FoldIndex.kr(buf, MouseX.kr(0, BufFrames.ir(buf) * 3));
    SinOsc.ar(freq) * 0.1
}.play;
)

// the same using a global buffer
(
t = [200, 300, 400, 500, 600, 800];
b = Buffer(s, t.size, 1);

// alloc and set the values
s.listSendMsg(b.allocMsg(b.setnMsg(0, t)).postln);

SynthDef(\help_Index, { |out = 0, bufnum = 0|
    Out.ar(out,
        SinOsc.ar(
            FoldIndex.kr(
                bufnum,
                MouseX.kr(0, BufFrames.ir(bufnum) * 3)
            ),
            0,
            0.5
        )
    )
}).play(s, [\bufnum, b.bufnum]);
)
```




