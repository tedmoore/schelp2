# Pattern Guide 06c: Composition of Patterns

*Making multiple event patterns act as one*

**Related:** [A-Practical-Guide/PG_06b_Time_Based_Patterns](../../Tutorials/A-Practical-Guide/PG_06b_Time_Based_Patterns.md), [A-Practical-Guide/PG_06d_Parallel_Patterns](../../Tutorials/A-Practical-Guide/PG_06d_Parallel_Patterns.md)

**Categories:** Streams-Patterns-Events>A-Practical-Guide, Tutorials>Pattern-Guide


## Adding values to a base event pattern (Or, "Pattern Composition")
One way to use patterns is to write everything into the pattern up front. This has the advantage of clarity and ease of understanding. Another way is to modularize the behavior by creating smaller, simpler patterns and combining their results into single events that have keys and values from all the component patterns.

This is related to the computer science concept of "function composition," in which a complex calculation can be written not as a single large function, but as several smaller functions that are then chained together into a single function. Since Functions are normal objects in SuperCollider, it's easy to do an operation on a function that returns a composite function (which may then be used like any other function). [http://en.wikipedia.org/wiki/Function_composition_(computer_science)](http://en.wikipedia.org/wiki/Function_composition_(computer_science))

In mathematics, the `·` operator represents function composition.


```
f(x) = x + 1
g(x) = x * 2

g · f = g(f(x)) = (x + 1) * 2
```


`g · f` means to evaluate `f` first, then pass its result to `g`. The `·` operator is written as `<>` in SuperCollider.


```
f = { |x| x + 1 };
g = { |x| x * 2 };

h = (g <> f);
--> a Function

h.value(1);
--> 4    // == (1+1) * 2

(f <> g).value(1)
--> 3    // == (1*2) + 1

// g · f == g(f(x)) -- f is evaluated first, and its result is passed to g
g.value(f.value(1));
--> 4
```


Event patterns can be similarly composed.


**`Pbindf(pattern, pairs)`**
: Adds new key-value pairs onto a pre-existing Pbind-style pattern. `Pbindf(Pbind(\a, patternA), \b, patternB, \c, patternC)` gets the same result as `Pbind(\a, patternA, \b, patternB, \c, patternC)` .

**`Pchain(patterns)`**
: Chains separate Pbind-style patterns together, so that all their key-value pairs go into the same event. For example, if one part of your code creates a Pbind instance `a = Pbind(\a, patternA)` and another part creates `b = Pbind(\b, patternB, \c, patternC)`, you could append `\b` and `\c` into the `\a` result using `Pchain(b, a)` . The subpatterns evaluate in reverse order, in keeping with function composition notation.For musical purposes, you could have one part of your code create a pattern defining rhythm and another part defining pitch material, then combine them with [Pchain](../../Classes/Pchain.md).
```
~rhythm = Pbind(
    \dur, Pwrand(#[0.125, 0.25, 0.5], #[0.3, 0.5, 0.2], inf),
    \legato, Pwrand(#[0.1, 0.6, 1.01], #[0.1, 0.3, 0.6], inf)
);
~melody = Pbind(
    \degree, Pwhite(-4, 11, inf)
);

p = Pchain(~melody, ~rhythm).play;
p.stop;
```

That in itself has some good potential for algorithmic composition. Introducing [EventPatternProxy](../../Classes/EventPatternProxy.md) into the mix makes it possible to swap different melody and rhythm components in and out on the fly, with no interruption. We can even change the type of pattern ( [Pbind](../../Classes/Pbind.md), [Pmono](../../Classes/Pmono.md), [PmonoArtic](../../Classes/PmonoArtic.md) ) with no ill effect.
```
~rhythm = EventPatternProxy(Pbind(
    \dur, Pwrand(#[0.125, 0.25, 0.5], #[0.3, 0.5, 0.2], inf),
    \legato, Pwrand(#[0.1, 0.6, 1.01], #[0.1, 0.3, 0.6], inf)
));

~melody = EventPatternProxy(Pbind(
    \degree, Pwhite(-4, 11, inf)
));

p = Pchain(~melody, ~rhythm).play;

~melody.source = PmonoArtic(\default, \degree, Pseries(4, Prand(#[-1, 1], inf), inf).fold(-4, 11));

~melody.source = Pbind(\degree, Pseries(4, Pwrand(#[-2, -1, 1, 2], #[0.3, 0.2, 0.2, 0.3], inf), inf).fold(-4, 11));

p.stop;
```




### Pset and cousins
A group of pattern classes allow single event keys to be overwritten, or one addition or multiplication to be performed. [Pkey](../../Classes/Pkey.md), in combination with the [Pchain](../../Classes/Pchain.md) or [Pbindf](../../Classes/Pbindf.md) "pattern composition" classes, can do everything the following classes can do (though this alternate notation may be more convenient in certain cases).


**`Pset(name, value, pattern)`**
: Get one event from `pattern`, and then put the next value from the `value` pattern into the `name` key. If the source pattern specifies a value for the same name, the value from the source will be replaced with the new one.

**`Padd(name, value, pattern)`**
: After getting the next event, replace the `name` value with its existing value `+` the next number from `value`.

**`Pmul(name, value, pattern)`**
: After getting the next event, replace the `name` value with its existing value `*` the next number from `value`.



These patterns remain in the library mainly for reasons of backward compatibility, since their behavior can be replicated easily using [Pbindf](../../Classes/Pbindf.md).

| `Pset(name, value, pattern)` | `Pbindf(pattern, name, value)` | 
| --- | --- || `Padd(name, value, pattern)` | `Pbindf(pattern, name, Pkey(name) + value)` | | `Pmul(name, value, pattern)` | `Pbindf(pattern, name, Pkey(name) * value)` | 
The patterns [Psetpre](../../Classes/Psetpre.md), [Paddpre](../../Classes/Paddpre.md), and [Pmulpre](../../Classes/Pmulpre.md) reverse the order of evaluation. [Pchain](../../Classes/Pchain.md) is able to duplicate this functionality.


**`Psetpre(name, value, pattern)`**
: Get the next `value` and put it into the event prototype before evaluating `pattern`.



| `Psetpre(name, value, pattern)` | `Pchain(pattern, Pbind(name, value))` | 
| --- | --- || `Paddpre(name, value, pattern)` | `Pchain(pattern, Pbind(name, Pkey(name) + value))` | 
Similar for `Pmulpre`.

A third group -- [Psetp](../../Classes/Psetp.md), [Paddp](../../Classes/Paddp.md), [Pmulp](../../Classes/Pmulp.md) -- behave slightly differently, nesting pattern evaluation.

Previous: [A-Practical-Guide/PG_06b_Time_Based_Patterns](../../Tutorials/A-Practical-Guide/PG_06b_Time_Based_Patterns.md)

Next: [A-Practical-Guide/PG_06d_Parallel_Patterns](../../Tutorials/A-Practical-Guide/PG_06d_Parallel_Patterns.md)





