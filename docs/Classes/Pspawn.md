# Pspawn

*Spawns sub-patterns based on parameters in an event pattern*

**Related:** [Pspawner](../Classes/Pspawner.md), [Spawner](../Classes/Spawner.md)

**Categories:** Streams-Patterns-Events>Patterns>Parallel

## Description

Pspawn is a pattern-based version of [Pspawner](../Classes/Pspawner.md). Where Pspawner uses a Routine-style function to determine when and how to spawn child patterns into the result stream, Pspawn uses an event pattern to determine the actions to take.
Recommended to read the [Pspawner](../Classes/Pspawner.md) help file to become familiar with pattern spawning capabilities.

> **Note:** Important: There are two kinds of events involved in Pspawn:
****parent** events**
: which specify the pattern to embed, how to embed it (in parallel or sequence), and how long to wait until the next action;

****child** events**
: which produce the resulting notes (or take other actions on the server).


Of these, only the child events are returned to the event stream player during play. The parent events are used strictly internally to control spawning behavior. The parent and child event streams do not mix together. Thus pattern composition ([Pchain](../Classes/Pchain.md)) and parallelization ([Ppar](../Classes/Ppar.md)) may be used without special handling. It is up to the user to be aware of whether the parent or child stream should be subject to further manipulation, and put that manipulation in the right place. If it is to affect the child stream, it should enclose the entire Pspawn; for the parent stream, it should be inside Pspawn. (See the [#examples](#examples) below.)
Pspawn uses the following items in the parent pattern:

**method**
: The action to call on the spawner object. Currently supported: wait, seq, par, suspendAll.

**delta**
: How long to wait until the next action.

**dict**
: If 'pattern' is given as a symbol (see below), this is the dictionary in which the pattern will be looked up. If not specified, the [Pdef](../Classes/Pdef.md) collection will be used.

**pattern**
: If 'method' is seq or par, this is a pattern or function to be embedded, according to the following rules.


| **'pattern' in the event** | **Resulting behavior** | 
| --- | --- || A [Function](../Classes/Function.md) : `{ ... }` | The function should return a pattern; this pattern is spawned. | | A [Ref](../Classes/Ref.md) to a pattern: ``Pbind(...)` | The referenced pattern is spawned. | | A [Symbol](../Classes/Symbol.md) : `\scaleUp` | The pattern is looked up in the event's 'dict'. | 

### Using references to protect patterns from embedding
Normally, when a pattern appears inside another pattern, the subpattern is embedded in the main output stream. It is not visible to the outside world as a pattern in itself; only its values appear.


```supercollider
Pseq([Pwhite(0, 9, 5), Pwhite(10, 19, 5)], 1).asStream.all;
```


When using Pspawn, a sub pattern must be returned directly into the event. To accomplish this, every such pattern should be wrapped in a [Ref](../Classes/Ref.md) :


```supercollider
Pseq([`Pwhite(0, 9, 5), `Pwhite(10, 19, 5)], 1).asStream.all;
```


Hint: [Pfunc](../Classes/Pfunc.md) is another good way to wrap patterns, because it simply returns its result values without further embedding. See the first example.




## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `pattern` | An event pattern (typically [Pbind](../Classes/Pbind.md)) encapsulating the desired spawning behavior. Parameters in this event are described below. |  
| `spawnProtoEvent` | The event prototype against which the pattern is evaluated. Good for giving default values that should apply to all spawning (parent) events. |  

## Examples


```supercollider
// Play overlapping major scales, up and down
(
p = Pspawn(Pbind(
        // Pbind returned by Pfunc is not embedded, just placed in the event
        // So, it can be spawned
    \pattern, Pfunc { Pbind(\degree, Pseries(rrand(0, 10), #[-1, 1].choose, rrand(4, 10)), \dur, 0.125) },
    \delta, Pwhite(1, 5, inf) * 0.125,
    \method, \par
)).play;
)

p.stop;


// Same, using a dictionary of patterns, changing dur rhythm also
(
var    patternChoices = (
    up: { Pbind(\degree, Pseries(rrand(-4, 5), 1, rrand(4, 10)), \dur, 0.125) },
    down: { Pbind(\degree, Pseries(rrand(4, 11), -1, rrand(4, 10)), \dur, 0.125 * 4/3) }
);

p = Pspawn(Pbind(
    \pattern, Prand([\up, \down], inf),
    \delta, Pwhite(1, 5, inf) * 0.125,
    \method, \par
), (dict: patternChoices)).play;
)

p.stop;


// Using pattern composition (perhaps gratuitously) to build the parent events
(
var    patternChoices = (
    up: { Pbind(\degree, Pseries(rrand(-4, 5), 1, rrand(4, 10)), \dur, 0.125) },
    down: { Pbind(\degree, Pseries(rrand(4, 11), -1, rrand(4, 10)), \dur, 0.125 * 4/3) }
);

p = Pspawn(Pchain(
    Pbind(
        \pattern, Prand([\up, \down], inf),
        \method, \par
    ),
    Pbind(
        \delta, Pwhite(1, 5, inf) * 0.125
    )
), (dict: patternChoices)).play;
)

p.stop;


// Play parallel scales in the left channel and sequentially-arranged scales in the right
// This means parallelizing (Ppar) the child streams; thus Ppar surrounds a pair of Pspawns

// Handling of \pan is interesting: \pan needs to be a property of the patternChoices items
// It is NOT a property of the spawning events
// To reuse patternChoices, the Pspawns wrap the base patterns in a Pbindf, which adds new values
(
var    patternChoices = (
    up: { Pbind(\degree, Pseries(rrand(-4, 5), 1, rrand(4, 10)), \dur, 0.125) },
    down: { Pbind(\degree, Pseries(rrand(4, 11), -1, rrand(4, 10)), \dur, 0.125 * 4/3) }
);

p = Ppar([
    Pspawn(Pbind(
            // intermediate value
        \patternKey, Prand([\up, \down], inf),
            // pattern is selected and pan applied here
        \pattern, Pfunc { |ev| Pbindf(ev.dict[ev.patternKey].value, \pan, -1) },
        \delta, Pwhite(1, 5, inf) * 0.125,
        \method, \par
    ), (dict: patternChoices)),
    Pspawn(Pbind(
        \patternKey, Prand([\up, \down], inf),
        \pattern, Pfunc { |ev| Pbindf(ev.dict[ev.patternKey].value, \pan, 1) },
        \delta, Pwhite(1, 5, inf) * 0.125,
        \method, \seq
    ), (dict: patternChoices)),
]).play;
)

p.stop;
```




