# Pdefn

*non event stream reference definition*

**Categories:** JITLib>Patterns, Live Coding

**Related:** [Pdef](../Classes/Pdef.md)

## Description

Pdefn provides an interface to its superclass [PatternProxy](../Classes/PatternProxy.md), keeping a reference to a stream that can be replaced while playing. One pattern may be used in many streams in different places. A change in the pattern definition propagates through all streams.
Pdef and Pdefn use separate global collections.

```supercollider
Pdefn(key)    // returns the instance
Pdefn(key, pat)    // defines the pattern and returns the instance, like Pdef, Tdef and Ndef.
```


It is very similar to [PatternProxy](../Classes/PatternProxy.md).
Pdefn can be used to store value patterns globally (for **event patterns**, see [Pdef](../Classes/Pdef.md)). Overview: [JITLib](../Overviews/JITLib.md)

### First Example

```supercollider
s.boot;

Pdefn(\x, Pbrown(0, 6, 0.1, inf));
Pbind(\note, Pdefn(\x), \dur, 0.3).play;
Pbind(\note, Pdefn(\x), \dur, 0.1, \ctranspose, 15).play;
// now change the definition
Pdefn(\x, Pseq([0, 3, 5, 7, 9, 11], inf));
Pdefn(\x, Pseq([0, 3, 3, 7], inf) + Pseq([0, [0, 3], [0, 5, 7]], inf));
```





## Class Methods


### `all`
A global [IdentityDictionary](../Classes/IdentityDictionary.md) with all proxies.

### Creation
### `new`
Store the pattern in a global dictionary under key, replacing its pattern with the new one. If the pattern is a **function**, Pdefn creates a [Prout](../Classes/Prout.md) with this function, passing in the envir, if given(see below).Using ***new(key)** you can access the pattern at that key (if none is given, a default silent event is created)**Arguments:**

| Argument | Description |
|----------|-------------|
| `key` | An identifier for the proxy. Usually, it is a [Symbol](../Classes/Symbol.md). The key transparently accesses the global [IdentityDictionary](../Classes/IdentityDictionary.md). |  
| `item` | An object for (re)defining the source of the proxy. If `nil`, the proxy is returned unmodified.
```supercollider
// pattern as an argument
Pdefn(\x, Pseq([1, 2, 5, 6, 7], inf));
Pdefn(\x); // omitting the second argument, we can access the proxy
Pdefn(\x).asStream.nextN(20); // ... play one event stream
Pdefn(\x).source.postcs; // ... and inspect the event pattern itself.


// function as an argument, create a new pattern each time it is called
Pdefn(\x, { Pseq({ 10.rand } ! 8) });
Pn(Pdefn(\x)).asStream.nextN(16);

// the function is called in the incoming event as current environment, so parameters can be passed:
Pdef(\stut, { Pdup(~dup ? 1, ~pattern) }); // we use here a Pdef (not a Pdefn!)
Pdefn(\y, Pdef(\stut) <> (pattern: Pdefn(\x), dup: Pseq([2, 2, 4, 3], inf))).asStream.nextN(16);
``` |  

### `default`
Default source, if none is given. The default is a Pattern that returns 1.0 (This is 1 and not 0 to avoid deadlocks when used as a duration pattern. In a sense, 1 is just as generic as 0).
### `removeAll`
Remove all proxies from the global dictionary ([#*all](#*all))
### `clear`
Clear all proxies, setting their source to silence.
### `all`
Set or return the environment ([IdentityDictionary](../Classes/IdentityDictionary.md)) that stores all Pdefns.


## Instance Methods


## Examples


### Pdefn in expressions

```supercollider
Pdefn(\c, Pdefn(\a) + Pdefn(\b));

t = Pdefn(\c).asStream; // create a stream from Pdefn(\c)

t.value; // default value for a Pdefn is 1, so that it is a good time value default.

Pdefn(\a, 100); // (re)define Pdefn(\a) as 100

t.value;

Pdefn(\b, Pseq([1, 2, 3], inf)); // (re)define Pdefn(\b) as Pseq([1, 2, 3], inf)

3.do { t.value.postln };

Pdefn(\c, Pdefn(\a) * Pdefn(\b) - Pdefn(\a)); // (re)define Pdefn(\c)

8.do { t.value.postln };

Pdefn(\a, Prand([1, 4, 2], inf)); // (re)define Pdefn(\a)
```




### Embedding Pdefn in other patterns

```supercollider
Pdefn(\x, Pseq([1, 2, 3], inf));

x = Pseq([0, 0, Pdefn(\x)], inf).asStream;

t = Task({ loop({ x.next.postln; 0.3.wait }) }).play;


Pdefn(\x, Pseq([55, 66, 77], inf));
Pdefn(\x, Pseq([55, 66, 77], 1));

t.stop;



// Pdefn can be accessed in multiple streams

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
Pdefn(\deg, Pseq([0, 3, 2], inf));

Pset(\instrument, \Pdefhelp,
    Ppar([
        Pbind(\degree, Pdefn(\deg), \pan, -0.8),
        Pbind(\degree, Pdefn(\deg), \dur, 1/3, \pan, 0.8)
])
).play;
)

Pdefn(\deg, Prand([0, 3, [1s, 4]], inf));

Pdefn(\deg, Pn(Pshuf([0, 3, 2, 7, 6], 2), inf));

(
Pdefn(\deg, Plazy { var pat;
    pat = [Pshuf([0, 3, 2, 7, 6], 2), Pseries(0, 1, 11), Pseries(11, -1, 11)].choose;
    Pn(pat, inf)
});
)
```




### Timing
When does the definition change?

If quant is set, the update is done at the next beat or whatever is specified:


```supercollider
Pdefn(\deg).quant = 4;
Pdefn(\deg, Pn(Pseries(0, 1, 8), inf));

Pdefn(\deg).quant = nil; // activate immediately again

(
Pdefn(\deg, {
    loop {
    5.do { |i|
        #[1, 3, 4].choose.yield;
        #[5, 0, 12].choose.yield;
        #[14, 3, 4].choose.do { |j| (i % j).postln.yield };
    }
    }
})
)
```




### update condition
In order to be able to switch to a new pattern under a certain condition, the instance variable **condition** can be set to a function that returns a boolean. Value and a count index are passed to the function. The condition is always valid for the **next pattern** inserted. For stuck conditions, the **reset** message can be used.

As counting up (such as *"every nth event, a swap can happen"*) is a common task, there is a method for this, called **count(n)**.


```supercollider
z = Pbind(\degree, Pdefn(\x, \), \dur, 0.25).play;
Pdefn(\x, Pseq((0..5), inf)).condition_({ |val, i| i.postln % 6 == 0 });
Pdefn(\x, Pseq((7..0), inf)).condition_({ |val, i| i.postln % 8 == 0 });


// the above is equvalent to:
Pdefn(\x, Pseq((7..0), inf)).count(8);
```




### Reset

```supercollider
// reset to change immediately:
Pdefn(\x).reset;

Pdefn(\x).stop;
```




### Functions as arguments to Pdefn

```supercollider
Pdefn(\deg, { loop { yield(0.1.rand.round(0.01) + [2, 3, 9].choose) } });

// equivalent to:

Pdefn(\deg, Prout { loop { yield(0.1.rand.round(0.01) + [2, 3, 9].choose) } });

// this is not exactly true, see below..
```




### The (inner) environment

```supercollider
// set() creates a local environment that overrides the outer currentEnvironment

Pdefn(\z).set(\a, 1, \b, 5);
(
Pdefn(\z, { |e|
    loop { yield((e.a + e.b) + 0.1.rand.round(0.01)) }
})
); // [1]

t = Pdefn(\z).asStream;

t.nextN(3);

(
Pdefn(\z, { |e|
    // (e.a + e.b) + 0.1.rand.round(0.01) 1
    Pseq([1, 2, e.a], 1)
})
);

Pdefn(\z, Pseq([1, 2, 3], 1));

e = Pdefn(\z).envir


Pdefn(\z).set(\a, 3);

t.next;

Pdefn(\z).set(\a, Pseq([1, 2, 3], inf));

t.reset;
t.nextN(3);

Pdefn(\z).envir; // post the envir



// if you want to keep using the currentEnvironment at the same time,
// assign the currentEnvironment to the envir's parent (or proto) field
// (this shouldn't be a proxy space of course.)

Pdefn(\z).envir.parent = currentEnvironment;
~a = 9;
~b = 10;

t.nextN(3);
```






