# Understanding Streams, Patterns and Events - Part 2

*Patterns Introduction*

**Related:** [Streams-Patterns-Events1](../Tutorials/Streams-Patterns-Events1.md), [Streams-Patterns-Events3](../Tutorials/Streams-Patterns-Events3.md), [Streams-Patterns-Events4](../Tutorials/Streams-Patterns-Events4.md), [Streams-Patterns-Events5](../Tutorials/Streams-Patterns-Events5.md), [Streams-Patterns-Events6](../Tutorials/Streams-Patterns-Events6.md), [Streams-Patterns-Events7](../Tutorials/Streams-Patterns-Events7.md)

**Categories:** Tutorials>Streams-Patterns-Events


## Patterns
Often one wants to be able to create multiple streams from a single stream specification. Patterns are just a way to make multiple Streams from a single specification, like a cookie cutter. A pattern can be any object that responds to the `asStream` message by creating a [Stream](../Classes/Stream.md). Once again there is a default implementation in class [Object](../Classes/Object.md) of asStream that simply returns the receiver as its own stream. Thus any object is by default a pattern that returns itself as a stream when sent the asStream message.


```supercollider
(
a = 7.asStream;
a.postln;
a.next.postln;
)
```




## Pattern and its subclasses
There is a class named [Pattern](../Classes/Pattern.md) that provides more functionality for the concept of a pattern.

A [Pfunc](../Classes/Pfunc.md) is a Pattern that returns a [FuncStream](../Classes/FuncStream.md). The same function arguments are supplied as are supplied to FuncStream.


```supercollider
(
var a, b;
a = Pfunc.new({ #[1, 2, 3, 4].choose });
b = a.asStream;            // make a stream from the pattern
5.do({ b.next.postln; });    // print 5 values from the stream
)
```


A [Prout](../Classes/Prout.md) is a Pattern that returns a [Routine](../Classes/Routine.md). The same function argument is supplied as is supplied to Routine.


```supercollider
(
var a, b, c;
a = Prout.new({
        3.do({ arg i; 3.rand.yield; })
    });
// make two streams from the pattern
b = a.asStream;
c = a.asStream;
4.do({ b.next.postln; });    // print 4 values from first stream
4.do({ c.next.postln; });    // print 4 values from second stream
)
```


A [Pseries](../Classes/Pseries.md) is a Pattern that generates an arithmetic series.


```supercollider
(
var a, b;
a = Pseries.new(10, 3, 8);    // stream starts at 10, steps by 3 and has length 8
b = a.asStream;
9.do({ b.next.postln; });    // print 9 values from stream
)
```


[Pgeom](../Classes/Pgeom.md) is a Pattern that generates a geometric series.


```supercollider
(
var a, b;
a = Pgeom.new(10, 3, 8);    // stream starts at 10, steps by factor of 3 and has length 8
b = a.asStream;
9.do({ b.next.postln; });    // print 9 values from stream
)
```




## Math operations on Patterns
Patterns also respond to math operators by returning patterns that respond to `asStream` with appropriately modified streams.

Applying a unary operator to a pattern


```supercollider
(
var a, b, c;
a = Pseries.new(0,1,10);    // a is a pattern whose stream counts from 0 to 9
b = a.squared;            // pattern b is a square of the pattern a
c = b.asStream;
12.do({ c.next.postln; });
)
```


Using a binary operator on a pattern


```supercollider
(
var a, b, c;
a = Pseries.new(0,1,10);    // a is a pattern whose stream counts from 0 to 9
b = a + 100;            // add a constant value to pattern a
c = b.asStream;
12.do({ c.next.postln; });
)
```




## Filtering operations on patterns
Patterns also respond to the messages `collect`, `select`, and `reject` by returning a new [Pattern](../Classes/Pattern.md).

The `collect` message returns a Pattern whose [Stream](../Classes/Stream.md) is modified by a function in the same way as the collect message sent to a Collection returns a modified Collection.


```supercollider
(
var a, b, c;
// a is a pattern whose stream counts from 0 to 9
a = Pseries.new(0,1,10);
// b is a pattern whose stream adds 100 to even values
b = a.collect({ arg item; if (item.even, { item + 100 },{ item }); });
c = b.asStream;
6.do({ c.next.postln; });
)
```


The `select` message creates a pattern whose stream passes only items that return true from a user supplied function.


```supercollider
(
var a, b, c;
// a is a pattern whose stream counts from 0 to 9
a = Pseries.new(0,1,10);
// b is a pattern whose stream only returns the odd values
b = a.select({ arg item; item.odd; });
c = b.asStream;
6.do({ c.next.postln; });
)
```


The `reject` message creates a pattern whose stream passes only items that return false from a user supplied function.


```supercollider
(
var a, b, c;
// a is a pattern whose stream counts from 0 to 9
a = Pseries.new(0,1,10);
// b is a pattern whose stream that only returns the non-odd values
b = a.reject({ arg item; item.odd; });
c = b.asStream;
6.do({ c.next.postln; });
)
```




## Making Music with Patterns
Here is a variation of the example given in part 1 that uses a [Pattern](../Classes/Pattern.md) to create two instances of the random melody stream.


```supercollider
(
    s = Server.local;
    SynthDef(\help_SPE2, { arg i_out=0, sustain=1, freq;
        var out;
        out = RLPF.ar(
            LFSaw.ar( freq ),
            LFNoise1.kr(1, 36, 110).midicps,
            0.1
        ) * EnvGen.kr( Env.perc, levelScale: 0.3,
            timeScale: sustain, doneAction: Done.freeSelf );
        //out = [out, DelayN.ar(out, 0.04, 0.04) ];
        4.do({ out = AllpassN.ar(out, 0.05, [0.05.rand, 0.05.rand], 4) });
        Out.ar( i_out, out );
    }).send(s);
)
(
// streams as a sequence of pitches
    var pattern, streams, dur, durDiff;
    dur = 1/7;
    durDiff = 3;
    pattern = Prout.new({
        loop({
            if (0.5.coin, {
                #[ 24,31,36,43,48,55 ].do({ arg fifth; fifth.yield });
            });
            rrand(2,5).do({
                // varying arpeggio
                60.yield;
                #[63,65].choose.yield;
                67.yield;
                #[70,72,74].choose.yield;
            });
            // random high melody
            rrand(3,9).do({ #[74,75,77,79,81].choose.yield });
        });
    });
    streams = [
        (pattern - Pfunc.new({ #[12, 7, 7, 0].choose })).midicps.asStream,
        pattern.midicps.asStream
    ];
    Routine({
        loop({
            Synth( \help_SPE2, [ \freq, streams.at(0).next, \sustain, dur * durDiff ] );
            durDiff.do({
                Synth( \help_SPE2, [ \freq, streams.at(1).next, \sustain, dur ] );
                dur.wait;
            });
        })
    }).play
)
```


To go to the next file: [Streams-Patterns-Events3](../Tutorials/Streams-Patterns-Events3.md)



