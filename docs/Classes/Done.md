# Done

*Monitors another UGen to see when it is finished*

**Related:** [UGen](../Classes/UGen.md), [FreeSelfWhenDone](../Classes/FreeSelfWhenDone.md), [PauseSelfWhenDone](../Classes/PauseSelfWhenDone.md)

**Categories:** UGens>Synth control, Server>Nodes

## Description

Some UGens set a 'done' flag when they are finished playing. This UGen echoes that flag when it is set to track a particular UGen.
The UGens trackable by Done are:
- [PlayBuf](../Classes/PlayBuf.md)
- [RecordBuf](../Classes/RecordBuf.md)
- [Line](../Classes/Line.md)
- [XLine](../Classes/XLine.md)
- [EnvGen](../Classes/EnvGen.md)
- [Linen](../Classes/Linen.md)
- [BufRd](../Classes/BufRd.md)
- [BufWr](../Classes/BufWr.md)
- [Dbufrd](../Classes/Dbufrd.md)
- [Dbufwr](../Classes/Dbufwr.md)
- [DiskIn](../Classes/DiskIn.md)
- [VDiskIn](../Classes/VDiskIn.md)
- [Demand](../Classes/Demand.md)



## Actions
A number of UGens implement doneActions. These allow one to optionally free or pause the enclosing synth and other related nodes when the UGen is finished. You can use the constants in this class to name doneActions, which can be clearer than using the number codes alone. The available doneActions are as follows:

| name | value | description | 
| --- | --- | --- || none | 0 | do nothing when the UGen is finished | | pauseSelf | 1 | pause the enclosing synth, but do not free it | | freeSelf | 2 | free the enclosing synth | | freeSelfAndPrev | 3 | free both this synth and the preceding node | | freeSelfAndNext | 4 | free both this synth and the following node | | freeSelfAndFreeAllInPrev | 5 | free this synth; if the preceding node is a group then do g_freeAll on it, else free it | | freeSelfAndFreeAllInNext | 6 | free this synth; if the following node is a group then do g_freeAll on it, else free it | | freeSelfToHead | 7 | free this synth and all preceding nodes in this group | | freeSelfToTail | 8 | free this synth and all following nodes in this group | | freeSelfPausePrev | 9 | free this synth and pause the preceding node | | freeSelfPauseNext | 10 | free this synth and pause the following node | | freeSelfAndDeepFreePrev | 11 | free this synth and if the preceding node is a group then do g_deepFree on it, else free it | | freeSelfAndDeepFreeNext | 12 | free this synth and if the following node is a group then do g_deepFree on it, else free it | | freeAllInGroup | 13 | free this synth and all other nodes in this group (before and after) | | freeGroup | 14 | free the enclosing group and all nodes within it (including this synth) | | freeSelfResumeNext | 15 | free this synth and resume the following node | 
For information on `freeAll` and `deepFree`, see [Group](../Classes/Group.md) and [Server-Command-Reference](../Reference/Server-Command-Reference.md).



## Alternatives
Another way to free a synth when some UGen is done playing is to use [FreeSelfWhenDone](../Classes/FreeSelfWhenDone.md), or [FreeSelf](../Classes/FreeSelf.md) in combination with [Done](../Classes/Done.md). For example, this can be used to delay the freeing to let reverb tails fade out, etc.



## Class Methods


### `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `src` | The UGen to monitor |  

## Examples

The 'done' flag can be used to trigger other things in the same synth:

```supercollider
(
SynthDef("Done-help", { |out, t_trig|
    var line, a, b;

    line = Line.kr(1, 0, 1);

    a = SinOsc.ar(440, 0, 0.1*line); // sound fading out
    b = WhiteNoise.ar(Done.kr(line)*0.1); // noise starts at end of line

    Out.ar(out, Pan2.ar(a+b));
}).add;
)

Synth("Done-help"); // note that this synth doesn't have it's own doneAction, so you'll need to manually deallocate it
```


The 'done' flag can be used to trigger a delayed freeing of the current synth, which is not possible by using doneActions alone:

```supercollider
play {
    var env = Line.kr(1, 0, 2);
    var sig = PinkNoise.ar(env);
    FreeSelf.kr(TDelay.kr(Done.kr(env), 3));
    GVerb.ar(sig, 70, 7);
}
```




