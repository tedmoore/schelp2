# PatternProxy

*stream reference*

**Categories:** JITLib>Patterns, Live Coding

**Related:** [Pdefn](../Classes/Pdefn.md)

## Description

Keeps a reference to a stream that can be replaced while playing. Multiple streams are thus handled without creating dependencies.


## Class Methods


### `new`
create a new instance with a pattern (the source). the pattern should be a *value pattern* (see [Pdefn](../Classes/Pdefn.md)).for event pattern proxy, see: [EventPatternProxy](../Classes/EventPatternProxy.md). instead of a pattern, a **function** can be passed in, creating a routine.
### `default`
a default source, if none is given. the default is 1.0 (it is not 0.0 in order to make it safe for durations)
### `defaultQuant`
set the default quantization value for the class. (default: nil)
### `defaultValue`
a default return value, if no source is given. the default is 1.0 (it is not 0.0 in order to make it safe for durations). This is used in [#-endless](#-endless).

## Instance Methods

### `asStream`
Return a [Stream](../Classes/Stream.md) from this pattern. One pattern proxy can be used to produce any number of independent streams.
```supercollider
a = PatternProxy.new;
a.source = Pgeom(1, Pwhite(1.01, 1.2), inf);
b = a.asStream; c = a.asStream;

b.next;
b.next;
b.next;

c.next; // c is independent from b
c.next;

a.source = Pgeom([1, 2, 3], Pwhite(1.01, 1.2), inf); // replace the source

b.next;
c.next;
```

### `embedInStream`
Given a [Stream](../Classes/Stream.md) like e.g. [Routine](../Classes/Routine.md), yield all values from the pattern in the proxy before continuing. One pattern proxy can be used to produce values for any number of independent streams.**Arguments:**

| Argument | Description |
|----------|-------------|
| `inval` | The inval is passed into all substreams and can be used to control how they behave from the outside. |  
| `embed` | See [Object#-streamArg](../Classes/Object.md#-streamarg) for explanation. |  
| `default` | Replacement for `nil` outputs of the source pattern. One use case is [#-endless](#-endless).
```supercollider
a = PatternProxy.new;
a.source = Pgeom(1, Pwhite(1.01, 1.2), 4);
r = Routine { loop { 2.yield; 3.yield; a.embedInStream } };
r.nextN(12); // the next 12 values from r
a.source = Pgeom([1, 2, 3], Pwhite(1.01, 1.2), inf); // replace the source
r.nextN(12); // the next 12 values from r
``` |  
### `source`
set the source. If a quantization is given, schedule this change to the next beat### `clear`
set the source to nil### `quant`
set or get the quantization value### `condition`
provide a condition under which the pattern is switched when a new one is inserted. the stream value and a count is passed into the function. the methods **count_(n)** simply counts up to n and switches the pattern then### `embedInStream`
just like any pattern, embeds itself in stream
### Methods implemented for subclasses
PatternProxy implements some methods for the benefits of its subclasses [Pdefn](../Classes/Pdefn.md) / [Pdef](../Classes/Pdef.md) / [Tdef](../Classes/Tdef.md) which are not useful for [PatternProxy](../Classes/PatternProxy.md) and [TaskProxy](../Classes/TaskProxy.md).

### `envir`
provide a default environment for the proxy. If given, it is used as an environment for the routine function. When set for the first time, the routine pattern is rebuilt.
### `set`
set arguments in the environment. If there is none, it is created and the pattern is rebuilt.
### `endless`
returns a Prout that plays the proxy endlessly, replacing **nil** with a **default** value (1). This allows to create streams that idle on until a new pattern is inserted.

## Examples


```supercollider
a = PatternProxy(Pseq([1, 2, 3], inf));

x = Pseq([0, 0, a], inf).asStream;

t = Task({ loop({ x.next.postln; 0.3.wait }) }).play;


a.source = Pseq([55, 66, 77], inf);
a.source = Pseq([55, 66, 77], 1);

t.stop;
```



```supercollider
// PatternProxy, like Pdefn can be accessed in multiple streams

(
SynthDef("Pdefhelp", { |out, freq, sustain = 1, amp = 1, pan|
    var env, u = 1;
    env = EnvGen.kr(Env.perc(0.03, sustain), 1, doneAction: Done.freeSelf);
    5.do { var d; d = exprand(0.01, 1); u = SinOsc.ar(d * 300, u, rrand(0.1, 1.2) * d, 1) };
    Out.ar(out, Pan2.ar(SinOsc.ar(u + 1 * freq, 0, amp * env), pan));

}).add;
s.boot;
)

(
x = PatternProxy.new;
x.source = Pseq([0, 3, 2], inf);

Pset(\instrument, \Pdefhelp,
    Ppar([
    Pbind(\degree, x),
    Pbind(\degree, x, \dur, 1/3)
])
).play;
)

x.source = Prand([0, 3, [1s, 4]], inf);

x.source = Pn(Pshuf([0, 3, 2, 7, 6], 2), inf);



// if quant is set, the update is done at the next beat or whatever is specified:

x.quant = 4;
x.source = Pn(Pseries(0, 1, 8), inf);

x.quant = nil; // reactivate immediacy

(
x.source = Prout {
    loop {
    4.do { |i|
        #[2, 3, 4].choose.yield;
        #[5, 0, 11].choose.yield;
        #[6, 3, 4].choose.do { |j| (i % j).yield };
    }
    }
}
)
```




