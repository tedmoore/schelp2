# Pattern Guide 02: Basic Vocabulary

*Common patterns to generate streams of single values*

**Related:** [A-Practical-Guide/PG_01_Introduction](../../Tutorials/A-Practical-Guide/PG_01_Introduction.md), [A-Practical-Guide/PG_03_What_Is_Pbind](../../Tutorials/A-Practical-Guide/PG_03_What_Is_Pbind.md)

**Categories:** Streams-Patterns-Events>A-Practical-Guide, Tutorials>Pattern-Guide


## Basic Vocabulary: Generating values
Before getting to the really cool things patterns can do, we need to build up a basic vocabulary. We'll start with some words, then move into phrases in the next tutorial.

Some of the patterns will be demonstrated with a Pbind construct. This is a taste of things to come -- sequencing sonic events using patterns. Don't worry about how Pbind works just yet... all in good time.

Let's start with a very quick reference of some basic patterns. More complete descriptions follow this list. The list might seem long at first, but concentrate your attention on the patterns called "primary patterns". They are the most basic, and commonly used. 

Again, the purpose is to start learning the vocabulary of patterns -- like learning new words when studying a human language. You can always come back and look at the rest later.

For more information on any of these patterns, select the class name and use the help key for your editor to open its help file.



## Quick reference

### Primary Patterns

**`Pseq(list, repeats, offset)`**
: Play through the entire list `repeats` times. Like `list.do`.

**`Prand(list, repeats)`**
: Choose items from the list randomly (same as `list.choose`).

**`Pxrand(list, repeats)`**
: Choose randomly, but never repeat the same item twice in immediate succession.

**`Pshuf(list, repeats)`**
: Shuffle the list in random order, and use the same random order `repeats` times. Like `list.scramble`.

**`Pwrand(list, weights, repeats)`**
: Choose randomly, according to weighted probabilities (same as `list.wchoose(weights)`).

**`Pseries(start, step, length)`**
: Arithmetic series (addition).

**`Pgeom(start, grow, length)`**
: Geometric series (multiplication).

**`Pwhite(lo, hi, length)`**
: Random numbers, equal distribution ("white noise"). Like `rrand(lo, hi)` .

**`Pexprand(lo, hi, length)`**
: Random numbers, exponential distribution. Like `exprand(lo, hi)` .

**`Pbrown(lo, hi, step, length)`**
: Brownian motion, arithmetic scale (addition).

**`Pfunc(nextFunc, resetFunc)`**
: Get the stream values from a user-supplied function.

**`Pfuncn(func, repeats)`**
: Get values from the function, but stop after `repeats` items.

**`Prout(routineFunc)`**
: Use the function like a routine. The function should return values using `.yield` or `.embedInStream`.






### Additional List Patterns

**`Pser(list, repeats, offset)`**
: Play through the list as many times as needed, but output only `repeats` items.

**`Pslide(list, repeats, len, step, start, wrapAtEnd)`**
: Play overlapping segments from the list.

**`Pwalk(list, stepPattern, directionPattern, startPos)`**
: Random walk over the list.

**`Place(list, repeats, offset)`**
: Interlace any arrays found in the main list.

**`Ppatlace(list, repeats, offset)`**
: Interlace any patterns found in the main list.

**`Ptuple(list, repeats)`**
: Collect the list items into an array as the return value.






### Additional Random Number Generators

**`Pgbrown(lo, hi, step, length)`**
: Brownian motion, geometric scale (multiplication).

**`Pbeta(lo, hi, prob1, prob2, length)`**
: Beta distribution, where `prob1 = α` (alpha) and `prob2 = β` (beta).

**`Pcauchy(mean, spread, length)`**
: Cauchy distribution.

**`Pgauss(mean, dev, length)`**
: Guassian (normal) distribution.

**`Phprand(lo, hi, length)`**
: Returns the greater of two equal-distribution random numbers.

**`Plprand(lo, hi, length)`**
: Returns the lesser of two equal-distribution random numbers.

**`Pmeanrand(lo, hi, length)`**
: Returns the average of two equal-distribution random numbers, i.e., `(x + y) / 2`.

**`Ppoisson(mean, length)`**
: Poisson distribution.

**`Pprob(distribution, lo, hi, length, tableSize)`**
: Arbitrary distribution, based on a probability table.







## Functional descriptions of patterns

### List Patterns
The most obvious thing one would want to do with a pattern is to give it a list of values and have it read them out in order. You have a couple of choices, which differ in their handling of the `repeats` parameter.


**`Pseq(list, repeats, offset)`**
: Play through the entire list `repeats` times.

**`Pser(list, repeats, offset)`**
: Play through the list as many times as needed, but output only `repeats` items.
```supercollider
Pseq(#[1, 2, 3], 4).asStream.all;    // 12 items = 4 repeats * 3 items
Pser(#[1, 2, 3], 4).asStream.all;    // 4 items only
```

[Pseq](../../Classes/Pseq.md) is an obvious choice for streaming out known pitch and rhythm values.Before playing a Pbind pattern such as this, make sure the server is booted.
```supercollider
s.boot;

(
p = Pbind(
    \degree, Pseq(#[0, 0, 4, 4, 5, 5, 4], 1),
    \dur, Pseq(#[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1], 1)
).play;
)
```

To stop the examples in this file, use the "stop" keyboard shortcut (cmd-. on macOS, alt-. on Windows, check documentation for other editors). Or:
```supercollider
p.stop;
```

A variation, [Pslide](../../Classes/Pslide.md), plays overlapping segments of the input list.

**`Pslide(list, repeats, len, step, start, wrapAtEnd)`**
: Play overlapping segments from the list.
**`repeats`**
: number of segments

**`len`**
: length of each segment

**`step`**
: is how far to step the start of each segment from previous.

**`start`**
: what index to start at.

**`wrapAtEnd`**
: if true (default), indexing wraps around if goes past beginning or end. If false, the pattern stops if it hits a nil element or goes outside the list bounds.

If `step == 1`, then the first segment is at `start`, the second at `start + 1`, and so on.
```supercollider
Pslide(#[1, 2, 3, 4, 5, 6, 7, 8], 10, 3, 1, 0, false).asStream.all;

// or, to show the segments as separate arrays
Pslide(#[1, 2, 3, 4, 5, 6, 7, 8], 10, 3, 1, 0, false).clump(3).asStream.all;

// Flock of Seagulls!
(
p = Pbind(
    \degree, Pslide((-6, -4 .. 12), 8, 3, 1, 0),
    \dur, Pseq(#[0.1, 0.1, 0.2], inf),
    \sustain, 0.15
).play;
)
```






### Random-order list patterns

**`Prand(list, repeats)`**
: Choose items from the list randomly (same as `list.choose`).
```supercollider
// Prand: given scale degrees (pentatonic) with equal probability of each
(
p = Pbind(
    \degree, Prand([0, 1, 2, 4, 5], inf),
    \dur, 0.25
).play;
)
```

**`Pxrand(list, repeats)`**
: Choose randomly, but never repeat the same item twice in immediate succession.
```supercollider
// Pxrand: same as above but never repeats a pitch twice in a row
(
p = Pbind(
    \degree, Pxrand([0, 1, 2, 4, 5], inf),
    \dur, 0.25
).play;
)
```

**`Pshuf(list, repeats)`**
: Shuffle the list in random order, and use the same random order `repeats` times. Like `list.scramble`.
```supercollider
// Pshuf: randomly ordered once and repeated
(
p = Pbind(
    \degree, Pshuf([0, 1, 2, 4, 5], inf),
    \dur, 0.25
).play;
)
```

**`Pwrand(list, weights, repeats)`**
: Choose randomly, according to weighted probabilities (same as `list.wchoose(weights)`).
```supercollider
// Pwrand: these probabilities favor triadic notes from scale degrees
(
p = Pbind(
    \degree, Pwrand((0..7), [4, 1, 3, 1, 3, 2, 1].normalizeSum, inf),
    \dur, 0.25
).play;
)
```

**`Pwalk(list, stepPattern, directionPattern, startPos)`**
: Random walk over the list. This pattern is a bit more complicated; see its [help](../../Classes/Pwalk.md) file for details.






### Interlacing values and making arrays
These are opposing operations: interlacing means splitting arrays and merging them into a stream of single values, and arrays can be made out of single-value streams as well.


**`Place(list, repeats, offset)`**
: Take one from each item in the main array item in succession. Hard to explain, easier to see:
```supercollider
Place([0, [1, 2], [3, 4, 5]], 3).asStream.all;
--> [ 0, 1, 3, 0, 2, 4, 0, 1, 5 ]
```

If we turn this into a matrix and read vertically, the original arrays are clearly visible:
```supercollider
Place([0, [1, 2], [3, 4, 5]], 3).clump(3).do(_.postln);

[ 0, 1, 3 ]    // leftmost column: 0 from first Place item
[ 0, 2, 4 ]    // second column: alternates between 1 and 2, from second Place item
[ 0, 1, 5 ]    // third column: 3, 4, 5 from third Place item
```

**`Ppatlace(list, repeats, offset)`**
: Take one value from each sub-pattern in order.
```supercollider
// Hanon exercise
(
p = Pbind(
    \degree, Ppatlace([
        Pseries(0, 1, 8),    // first, third etc. notes
        Pseries(2, 1, 7)    // second, fourth etc. notes
    ], inf),
    \dur, 0.25
).play;
)
```

That's also a taste of things to come: Patterns can be nested.

**`Ptuple(list, repeats)`**
: Get one value from each item in the array, and return all of them as an array of values.
```supercollider
// Chords
// \degree receives [7, 9, 4], then [6, 7, 4] successively, expanded to chords on the server
(
p = Pbind(
    \degree, Ptuple([
        Pseries(7, -1, 8),
        Pseq([9, 7, 7, 7, 4, 4, 2, 2], 1),
        Pseq([4, 4, 4, 2, 2, 0, 0, -3], 1)
    ], 1),
    \dur, 1
).play;
)
```






### Arithmetic and geometric series
Now, let's move to patterns that produce values mathematically, without using a predefined list.


**`Pseries(start, step, length)`**
: Arithmetic series, successively adding `step` to the starting value, returning a total of `length` items.

**`Pgeom(start, grow, length)`**
: Geometric series, successively multiplying the current value by `grow`.
```supercollider
// Use Pseries for a scale and Pgeom for an accelerando
(
p = Pbind(
    \degree, Pseries(-7, 1, 15),
    \dur, Pgeom(0.5, 0.89140193218427, 15)
).play;
)
```

**Third-party extension alert** : If you want an arithmetic or geometric series to start at one number and end at another specific number, the step size/multiplier must be calculated from the endpoints and the number of items desired. The **ddwPatterns** quark includes a convenience method, `fromEndpoints`, for both Pseries and Pgeom that performs this calculation. It's necessary to give an exact number of repeats, at least two and less than infinity.
```supercollider
p = Pgeom.fromEndpoints(0.5, 0.1, 15);    // error if ddwPatterns not installed
p.postcs;
```

Prints:
```supercollider
Pgeom(0.5, 0.89140193218427, 15)
```






### Random numbers and probability distributions

**`Pwhite(lo, hi, length)`**
: Produces `length` random numbers with equal distribution ('white' refers to white noise).

**`Pexprand(lo, hi, length)`**
: Same, but the random numbers have an exponential distribution, favoring lower numbers. This is good for frequencies, and also durations (because you need more notes with a shorter duration to balance the weight of longer notes).

**`Pbrown(lo, hi, step, length)`**
: Brownian motion. Each value adds a random `step` to the previous value, where the `step` has an equal distribution between `-step` and `+step`.

**`Pgbrown(lo, hi, step, length)`**
: Brownian motion on a geometric scale. Each value multiplies a random `step` factor to the previous value.

**`Pbeta(lo, hi, prob1, prob2, length)`**
: Beta distribution, where `prob1 = α` (alpha) and `prob2 = β` (beta).

**`Pcauchy(mean, spread, length)`**
: Cauchy distribution.

**`Pgauss(mean, dev, length)`**
: Gaussian (normal) distribution.

**`Phprand(lo, hi, length)`**
: Returns the greater of two equal-distribution random numbers.

**`Plprand(lo, hi, length)`**
: Returns the lesser of two equal-distribution random numbers.

**`Pmeanrand(lo, hi, length)`**
: Returns the average of two equal-distribution random numbers, i.e., `(x + y) / 2`.

**`Ppoisson(mean, length)`**
: Poisson distribution.

**`Pprob(distribution, lo, hi, length, tableSize)`**
: Given an array of relative probabilities across the desired range (a histogram) representing an arbitrary distribution, generates random numbers corresponding to that distribution.



To see a distribution, make a histogram out of it.


```supercollider
Pmeanrand(0.0, 1.0, inf).asStream.nextN(10000).histo(200, 0.0, 1.0).plot;
```





### Catchall Patterns
Not everything is pre-written as a pattern class. These patterns let you embed custom logic.


**`Pfunc(nextFunc, resetFunc)`**
: The next value is the return value from evaluating `nextFunc`. If `.reset` is called on a stream made from this pattern, `resetFunc` is evaluated. The stream will run indefinitely until `nextFunc` returns `nil`.

**`Pfuncn(func, repeats)`**
: Like Pfunc, output values come from evaluating the function. Pfuncn, however, returns exactly `repeats` values and then stops. The default number of repeats is 1.

**`Prout(routineFunc)`**
: Use the `routineFunc` in a routine. The stream's output values are whatever this function `.yield`s. Prout ends when it yields `nil`.



Next, we'll look at the central pattern for audio sequencing: [Pbind](../../Classes/Pbind.md).

Previous: [A-Practical-Guide/PG_01_Introduction](../../Tutorials/A-Practical-Guide/PG_01_Introduction.md)

Next: [A-Practical-Guide/PG_03_What_Is_Pbind](../../Tutorials/A-Practical-Guide/PG_03_What_Is_Pbind.md)





