# Understanding Streams, Patterns and Events - Part 1

*Streams & Routines*

**Related:** [Streams-Patterns-Events2](../Tutorials/Streams-Patterns-Events2.md), [Streams-Patterns-Events3](../Tutorials/Streams-Patterns-Events3.md), [Streams-Patterns-Events4](../Tutorials/Streams-Patterns-Events4.md), [Streams-Patterns-Events5](../Tutorials/Streams-Patterns-Events5.md), [Streams-Patterns-Events6](../Tutorials/Streams-Patterns-Events6.md), [Streams-Patterns-Events7](../Tutorials/Streams-Patterns-Events7.md)

**Categories:** Tutorials>Streams-Patterns-Events

The SuperCollider Pattern library provides a means of specifying dynamic structural transformations of musical processes. It provides similar capabilities as one finds in Nyquist, Elody, Siren, Kyma, HMSL, DMix, and Patchwork.
By using coroutines and streams rather than eager functional methods it is able to work in a lazy event by event method instead of the all-at-once method of Elody and Siren. It provides the kind of dynamic live control found in HMSL but with the more general event models of the others. In Nyquist and Siren certain transformation like Stretch and Transpose are specially coded into the framework. In SuperCollider Patterns, any parameter may have transformations applied to it. The only one treated specially is time, so that parallel streams can be merged.
In order to understand the framework, a number of concepts must be covered. These concepts are embodied in the classes for Streams, Patterns, and Events. You should learn these concepts in the order presented. The framework is built up in layers. If you skip ahead to get to the cool stuff first, you will have missed some important points.

## Streams
A stream represents a lazy sequence of values. The next value in the sequence is obtained by sending the message next to the stream object. The sequence can be restarted from the beginning by sending the message reset to the stream object. A stream can be of finite or infinite length. When a finite length stream has reached the end, it returns nil.

A stream can be any object that responds to the next and reset messages. Any object that responds to these messages can act as a stream. It happens that the class [Object](../Classes/Object.md) defines next and reset for all objects. In Object, both next and reset are defined to return `this`. Thus any object is by default a stream that represents an infinite sequence of itself.


```supercollider
7.next.postln;    // 7 responds to next by returning itself
```




## Stream and its subclasses
In addition to the default streams implemented by [Object](../Classes/Object.md), there is a class [Stream](../Classes/Stream.md) that provides more functionality such as math operations on streams and filtering of streams.

A generally useful subclass of Stream is the class [FuncStream](../Classes/FuncStream.md) which allows the user to provide functions to execute in response to next and reset. Here is a FuncStream that represents an infinite random sequence:


```supercollider
(
var a;
a = FuncStream.new({ #[1, 2, 3, 4].choose });
5.do({ a.next.postln; });    // print 5 values from the stream
)
```


Another useful subclass of Stream is [Routine](../Classes/Routine.md) which is a special kind of function that can act like a Stream. Routines are functions that can return a value from the middle and then be resumed from that point when called again. The yield message returns a value from the Routine. The next time the Routine is called it begins by returning from the yield and continues from that point. See the [Routine](../Classes/Routine.md) help file.

Here is a Routine that represents a finite sequence of values:


```supercollider
(
var a;
a = Routine.new({
        3.do({ arg i; i.yield; })
    });
4.do({ a.next.postln; });    // print 4 values from stream
)
```


and another:


```supercollider
(
var a;
a = Routine.new({
        3.do({ arg i;
            (i+1).do({ arg j; j.yield; })
        })
    });
8.do({ a.next.postln; });    // print 8 values from stream
)
```




## Math operations on Streams
Stream is a subclass of [AbstractFunction](../Classes/AbstractFunction.md) which means that one can do math operations on streams to produce other streams.

Applying a unary operator to a stream:


```supercollider
(
var a, b;
// a is a stream that counts from 0 to 9
a = Routine.new({
        10.do({ arg i; i.yield; })
    });
b = a.squared;    // stream b is a square of the stream a
12.do({ b.next.postln; });
)
```


Using a binary operator on a stream:


```supercollider
(
var a, b;
// a is a stream that counts from 0 to 9
a = Routine.new({
        10.do({ arg i; i.yield; })
    });
b = a + 100;    // add a constant value to stream a
12.do({ b.next.postln; });
)
```


Using a binary operator on two streams:


```supercollider
(
var a, b, c;
// a is a stream that counts from 0 to 9
a = Routine.new({
        10.do({ arg i; i.yield; })
    });
// b is a stream that counts from 100 to 280 by 20
b = Routine.new({
        forBy (100,280,20, { arg i; i.yield })
    });
c = a + b;    // add streams a and b
12.do({ c.next.postln; });
)
```




## Filtering operations on streams
Streams respond to the messages `collect`, `select`, and `reject` by returning a new [Stream](../Classes/Stream.md).

The `collect` message returns a stream that is modified by a function in the same way as the collect message sent to a [Collection](../Classes/Collection.md) returns a modified Collection.


```supercollider
(
var a, b;
// a is a stream that counts from 0 to 9
a = Routine.new({
        10.do({ arg i; i.yield; })
    });
// b is a stream that adds 100 to even values
b = a.collect({ arg item; if (item.even, { item + 100 },{ item }); });
6.do({ b.next.postln; });
)
```


The `select` message creates a stream that passes only items that return true from a user supplied function.


```supercollider
(
var a, b;
// a is a stream that counts from 0 to 9
a = Routine.new({
        10.do({ arg i; i.yield; })
    });
// b is a stream that only returns the odd values from stream a
b = a.select({ arg item; item.odd; });
6.do({ b.next.postln; });
)
```


The `reject` message creates a stream that passes only items that return false from a user supplied function.


```supercollider
(
var a, b;
// a is a stream that counts from 0 to 9
a = Routine.new({
        10.do({ arg i; i.yield; })
    });
// b is a stream that only returns the non-odd values from stream a
b = a.reject({ arg item; item.odd; });
6.do({ b.next.postln; });
)
```




## Making Music with Streams
Here is a sound example to show how you might use Streams to generate musical material.


```supercollider
(
    s = Server.local;
    SynthDef(\help_SPE1, { arg i_out=0, freq;
        var out;
        out = RLPF.ar(
            LFSaw.ar( freq, mul: EnvGen.kr( Env.perc, levelScale: 0.3, doneAction: Done.freeSelf )),
            LFNoise1.kr(1, 36, 110).midicps,
            0.1
        );
        // out = [out, DelayN.ar(out, 0.04, 0.04) ];
        4.do({ out = AllpassN.ar(out, 0.05, [0.05.rand, 0.05.rand], 4) });
        Out.ar( i_out, out );
    }).send(s);
)
(
// streams as a sequence of pitches
    var stream, dur;
    dur = 1/8;
    stream = Routine.new({
        loop({
            if (0.5.coin, {
                // run of fifths:
                24.yield;
                31.yield;
                36.yield;
                43.yield;
                48.yield;
                55.yield;
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
    Routine({
        loop({
            Synth(\help_SPE1, [ \freq, stream.next.midicps ] );
            dur.wait; // synonym for yield, used by .play to schedule next occurrence
        })
    }).play
)
```




## Optional:
More about Streams can be learned from the book A Little Smalltalk by Timothy Budd. He calls them Generators and shows how they can be used to solve problems like the "eight queens" problem etc.

To go to the next file: [Streams-Patterns-Events2](../Tutorials/Streams-Patterns-Events2.md)



