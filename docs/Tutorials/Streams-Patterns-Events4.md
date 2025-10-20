# Understanding Streams, Patterns and Events - Part 4

*Environment & Event*

**Related:** [Streams-Patterns-Events1](../Tutorials/Streams-Patterns-Events1.md), [Streams-Patterns-Events2](../Tutorials/Streams-Patterns-Events2.md), [Streams-Patterns-Events3](../Tutorials/Streams-Patterns-Events3.md), [Streams-Patterns-Events5](../Tutorials/Streams-Patterns-Events5.md), [Streams-Patterns-Events6](../Tutorials/Streams-Patterns-Events6.md), [Streams-Patterns-Events7](../Tutorials/Streams-Patterns-Events7.md)

**Categories:** Tutorials>Streams-Patterns-Events

The preceding sections showed how to use Streams and Patterns to generate complex sequences of values for a single parameter at a time.
This section covers Environments and Events, which are used to build a symbolic event framework for patterns, allowing you to control all aspects of a composition using patterns.

## Environment
An [Environment](../Classes/Environment.md) is an [IdentityDictionary](../Classes/IdentityDictionary.md) mapping [Symbol](../Classes/Symbol.md)s to values. There is always one current Environment which is stored in the `currentEnvironment` class variable of class [Object](../Classes/Object.md).

Symbol and value pairs may be put into the current Environment as follows:


```
currentEnvironment.put(\myvariable, 999);
```


and retrieved from the current Environment as follows:


```
currentEnvironment.at(\myvariable).postln;
```


The compiler provides a shorthand for the two constructs above.


```
~myvariable = 888;
```


is equivalent to:


```
currentEnvironment.put(\myvariable, 888);
```


and:


```
~myvariable.postln;
```


is equivalent to:


```
currentEnvironment.at(\myvariable).postln;
```




## Making an Environment
Environment has a class method **make** which can be used to create an [Environment](../Classes/Environment.md) and fill it with values. What **make** does is temporarily replace the current Environment with a new one, call your function where you fill the Environment with values, then it replaces the previous current Environment and returns you the new one.


```
(
var a;
a = Environment.make({
    ~a = 100;
    ~b = 200;
    ~c = 300;
});
a.postln;
)
```




## Using an Environment
The instance method **use** lets you temporarily replace the current [Environment](../Classes/Environment.md) with one you have made. The **use** method returns the result of your function instead of the Environment like **make** does.


```
(
var a;
a = Environment.make({
    ~a = 10;
    ~b = 200;
    ~c = 3000;
});
a.use({
    ~a + ~b + ~c
}).postln;
)
```


There is also a **use** class method for when you want to make and use the result from an [Environment](../Classes/Environment.md) directly.


```
(
var a;
a = Environment.use({
    ~a = 10;
    ~b = 200;
    ~c = 3000;
    ~a + ~b + ~c
}).postln;
)
```




## Calling Functions with arguments from the current Environment
It is possible to call a [Function](../Classes/Function.md) and have it look up any unspecified argument values from the current Environment. This is done with the **valueEnvir** and **valueArrayEnvir** methods. These methods will, for any unspecified argument value, look in the current Environment for a symbol with the same name as the argument. If the argument is not found then whatever the function defines as the default value for that argument is used.


```
(
var f;

// define a function
f = { arg x, y, z; [x, y, z].postln; };

Environment.use({
    ~x = 7;
    ~y = 8;
    ~z = 9;

    f.valueEnvir(1, 2, 3);    // all values supplied
    f.valueEnvir(1, 2);    // z is looked up in the current Environment
    f.valueEnvir(1);    // y and z are looked up in the current Environment
    f.valueEnvir;        // all arguments are looked up in the current Environment
    f.valueEnvir(z: 1);    // x and y are looked up in the current Environment
});
)
```


Here is a somewhat contrived example of how the Environment might be used to manufacture SynthDefs. Even though the three functions below have the freq, amp and pan args declared in different orders it does not matter, because valueEnvir looks them up in the environment.


```
(
var a, b, c, n;

n = 40;
a = { arg freq, amp, pan;
    Pan2.ar(SinOsc.ar(freq), pan, amp);
};
b = { arg amp, pan, freq;
    Pan2.ar(RLPF.ar(Saw.ar(freq), freq * 6, 0.1), pan, amp);
};
c = { arg pan, freq, amp;
    Pan2.ar(Resonz.ar(GrayNoise.ar, freq * 2, 0.1), pan, amp * 2);
};

Task({
    n.do({ arg i;
        SynthDef("Help-SPE4-EnvirDef-" ++ i.asString, { |out|
            var sound;
            Environment.use({
                    // set values in the environment
                ~freq = exprand(80, 600);
                ~amp = 0.1 + 0.3.rand;
                ~pan = 1.0.rand2;

                    // call a randomly chosen instrument function
                    // with values from the environment
                sound = [a,b,c].choose.valueEnvir;
            });
            sound = CombC.ar(sound, 0.2, 0.2, 3, 1, out);
            sound = sound * EnvGen.kr(
                Env.sine, doneAction: Done.freeSelf, timeScale: 1.0 + 6.0.rand, levelScale: 0.3
            );
            Out.ar(out, sound);
        }).send(s);
        0.02.wait;
    });
    loop({
        Synth( "Help-SPE4-EnvirDef-" ++ n.rand.asString );
        (0.5 + 2.0.rand).wait;
    });
}).play;
)
```




## Event
The class [Event](../Classes/Event.md) is a subclass of [Environment](../Classes/Environment.md). Events are mappings of Symbols representing names of parameters for a musical event to their value. This lets you put any information you want into an event.

The class getter method **default** retrieves the default prototype event which has been initialized with values for many useful parameters. It represents only one possible event model. You are free to create your own, however it would be good to understand the one provided first so that you can see what can be done.

A prototype event is a default event which will be transformed by the streams returned by patterns. Compositions produced by event patterns are created entirely from transformations of copies of a single protoEvent.

> *It's all a part of the Big Note, but don't tell the pigs and ponies.*



## Value Patterns, Event Patterns and Pbind
The patterns discussed in parts 2 and 3 are known as "value patterns" because their streams return a single value for each call to **next**. Here we introduce "event patterns" which once turned into streams, return an [Event](../Classes/Event.md) for each call to **next**.

The class [Pbind](../Classes/Pbind.md) provides a bridge between value patterns and event patterns. It binds symbols in each event to values obtained from a pattern. Pbind takes arguments in pairs, the first of a pair being a [Symbol](../Classes/Symbol.md) and the second being a value [Pattern](../Classes/Pattern.md). Any object can act as a Pattern, so you can use constants as the pattern ( see `\amp` in the example below ).

The Pbind stream returns nil whenever the first one of its streams ends.


```
Pbind( \freq, Pseq([440,880]) ).play
```


An event stream is created for a Pattern by sending it the `asStream` message. What Pbind does is to produce a stream which puts the values for its symbols into the event, possibly overwriting previous bindings to those symbols:


```
t = Pbind( \freq, Pseq([440,880]) ).asStream;
t.next(Event.default);
t.next(Event.default);
t.next(Event.default);
```


When calling [Pattern#-play](../Classes/Pattern.md#-play) an [EventStreamPlayer](../Classes/EventStreamPlayer.md) is automatically generated which handles scheduling as well as passing the protoEvent into the event stream.



## EventStreamPlayer
The class [EventStreamPlayer](../Classes/EventStreamPlayer.md) is a subclass of [PauseStream](../Classes/PauseStream.md). A PauseStream is just a wrapper for a stream allowing to play, stop, start it, etc...

EventStreamPlayers are initialized using the event stream returned by Pbind-asStream, as well as with a protoEvent. The EventStreamPlayer passes in a **protoEvent**, at each call to **next** on the Pbind stream. The Pbind stream copies the event to pass down and back up the tree of pattern streams so that each stream can modify it.

An EventStreamPlayer is itself a stream which returns scalars (numbers) which are used by the clock to schedule its next invocation. At every call to EventStreamPlayer-next by the clock, the player gets its delta values by querying the Event after it has been returned by the Pbind stream traversal.



## Changes in SC3
In SC2, you called asEventStream on an Pattern and you'd get a stream which actually returned events.

In SC3, if you want an event stream proper you call asStream on the Event Pattern. This will give you a stream of events which you can then use to initialize an EventStreamPlayer object. You don't however need to worry about that because it is usually done for you in Pattern's play method. Also changed is that you do not pass in your protoEvent through the asStream method. It is passed in for you by the EventStreamPlayer at each call to next on the stream.

Here you can see what the stream returned from a Pbind looks like.


```
(
var pattern, stream;

    // bind Symbol xyz to values obtained from a pattern
pattern = Pbind(
    \xyz, Pseq([1, 2, 3])
);

    // create a stream of events for the Pbind pattern.
stream = pattern.asStream;

    // event Streams require a prototype event as input.
    // this example uses an empty Event as a prototype
4.do({ stream.next(Event.new).postln; });
)
```


Here is an example with more bindings.


```
(
var pattern, stream;

pattern = Pbind(
    \abc, Prand([6, 7, 8, 9], inf ),
    \xyz, Pseq([1, 2, 3], 2 ),
    \uuu, 999 // a constant represents an infinite sequence of itself
);

stream = pattern.asStream;

7.do({ stream.next(Event.new).postln; });
)
```


The ListPatterns discussed in part 3 can be put around Event Streams to create sequences of Event Streams.


```
(
var pattern, stream;
pattern =
    Pseq([
        Pbind( \abc, Pseq([1, 2, 3])),
        Pbind( \def, Pseq([4, 5, 6])),
        Pbind( \xyz, Pseq([7, 8, 9]))
    ]);
stream = pattern.asStream;
10.do({ stream.next(Event.new).postln; });
)

(
var pattern, stream;
pattern =
    Prand([
        Pbind( \abc, Pseq([1, 2, 3])),
        Pbind( \def, Pseq([4, 5, 6])),
        Pbind( \xyz, Pseq([7, 8, 9]))
    ], 3);
stream = pattern.asStream;
10.do({ stream.next(Event.new).postln; });
)
```


To go to the next file: [Streams-Patterns-Events5](../Tutorials/Streams-Patterns-Events5.md)



