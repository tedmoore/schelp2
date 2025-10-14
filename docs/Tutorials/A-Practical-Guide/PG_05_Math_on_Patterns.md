# Pattern Guide 05: Math on Patterns

*Performing math and collection operations on patterns*

**Related:** [A-Practical-Guide/PG_04_Words_to_Phrases](../../Tutorials/A-Practical-Guide/PG_04_Words_to_Phrases.md), [A-Practical-Guide/PG_060_Filter_Patterns](../../Tutorials/A-Practical-Guide/PG_060_Filter_Patterns.md)

**Categories:** Streams-Patterns-Events>A-Practical-Guide, Tutorials>Pattern-Guide


## Math on patterns
Often, there is not a pattern that delivers exactly the desired result by itself. But, other operations can be applied to patterns, to manipulate one pattern's output and turn it into something else.

Some of these operations look like things you would do to an array, but there is a critical difference. Doing math on an array performs the operation on every array item all at once. By contrast, patterns are "lazy" -- they evaluate one value at the time, only when asked, and they only do as much as they need to do to deliver the next value. An operation on a pattern produces another pattern that remembers the work that is to be done. Making a stream out of the composite pattern creates the structure to perform the operation upon request.

For example, multiplying a pattern by a number produces a "binary operator pattern": [Pbinop](../../Classes/Pbinop.md). Looking at the Pbinop's variables reveals everything that is needed to reconstruct the operation on demand.


```supercollider
p = Pwhite(1, 5, inf) * 2;    // a Pbinop

p.operator    // == '*'
p.a        // == a Pwhite
p.b        // == 2
```


In other words, the multiplication here produces not the result of a single multiplication, but a template for an infinite stream of multiplications to follow.


### Math on patterns
Not only can patterns generate numbers, but they also support all the standard math operators: unary (abs, reciprocal, etc.), binary (+, -, *, /, **, min, max, etc.) and n-ary (clip, wrap, fold, linlin, linexp, etc.) operators are all valid with patterns.


```supercollider
// Random integers, 1-5
Pwhite(1, 5, inf).asStream.nextN(10);

// Random integers 1-5, multiplied by two gives even integers 2-10
(Pwhite(1, 5, inf) * 2).asStream.nextN(10);

// Random integers 1-5, multiplied by 1/4 gives multiples of 1/4 between 0.25 and 1.25
(Pwhite(1, 5, inf) * 0.25).asStream.nextN(10);

// Random integers 1-5, with the sign (positive or negative) randomly chosen
(Pwhite(1, 5, inf) * Prand(#[-1, 1], inf)).asStream.nextN(10);
```


If a binary operation occurs on two patterns, every time a value is requested from the resulting stream, both of the component streams are asked for a value, and the operator applies to those results. If either stream ends, the binary operator stream also ends.


```supercollider
// The resulting stream has two values, because the shorter operand stream has two values
(Pseq([10, 9, 8], 1) + Pseq([1, 2], 1)).do { |x| x.postln };
```


The binary operator adverb `.x` is supported with patterns. (See [Adverbs](../../Reference/Adverbs.md).) This adverb is like a nested loop: in `streamA +.x streamB`, the first value of streamA is added to every value of streamB in succession, then the second value of streamA is added to every streamB value, and so on. This is an easy way to transpose a pattern to different levels successively.


```supercollider
// Play a major-7th arpeggio, transposed to different scale degrees
// Pwhite is the transposer; Pseq is the chord
// The chord is like an "inner loop"
(
p = Pbind(
    \midinote, Pwhite(48, 72, inf) +.x Pseq(#[0, 4, 7, 11], 1),
    \dur, 0.125
).play;
)

p.stop;
```





### Collection operations on patterns
Some of the things you can do to arrays also work with patterns.


**`collect(func)`**
: Applies the function to each return value from the pattern. Good for generic transformations.

**`select(func)`**
: Preserve values from the output stream that pass the Boolean test; discard the rest.

**`reject(func)`**
: Discard values from the output stream that pass the test; return the rest to the user.
```supercollider
// Arbitrary/custom operation: Turn each number into a two-digit hex string
Pwhite(0, 255, 20).collect({ |x| x.asHexString(2) }).do { |x| x.postln };

// Keep odd numbers in the result (which is now less than 20 items)
Pwhite(0, 255, 20).select({ |x| x.odd }).do { |x| x.postln };

// Throw out odd numbers in the result
Pwhite(0, 255, 20).reject({ |x| x.odd }).do { |x| x.postln };
```

**`clump(n)`**
: Calling `.clump` on an array turns a flat array into a multilevel array. Similarly, `.clump` on a pattern gets *n* values from the pattern at once and returns all of them as an array. *n* can be a number or a numeric pattern.

**`flatten(levels)`**
: The reverse operation: if a pattern returns an array, its values will be output one by one.
```supercollider
// A flat stream becomes an array of 4-item arrays
Pwhite(0, 255, 20).clump(4).do { |x| x.postln };

    // a two-dimensional array
Array.fill(5, { Array.fill(4, { rrand(1, 5) }) });

    // a pattern reading that array in sequence
p = Pseq(Array.fill(5, { Array.fill(4, { rrand(1, 5) }) }), 1);

    // the pattern returns several arrays
p.do { |x| x.postln };

    // flattening the pattern returns a one-dimensional stream of numbers
p.flatten.do { |x| x.postln };
```

**`drop(n)`**
: Discard the first *n* values, and return whatever is left.
```supercollider
Pseries(1, 1, 20).drop(5).do { |x| x.postln };
```

**`differentiate`**
: Return the difference between successive values: second - first, third - second, and so on.
```supercollider
Array.geom(20, 1, 1.01).differentiate;
Pgeom(1, 1.01, 20).differentiate.do { |x| x.postln };
```






### Miscellaneous calculation patterns
These are some other numeric calculations that don't exactly fall in the category of math operators.


**`Pavaroh(pattern, aroh, avaroh, stepsPerOctave)`**
: Convert scale degrees to note numbers, with separate ascending and descending scale patterns. Originally written for Indian ragas, it also works well for the western melodic minor scale.

**`PdegreeToKey(pattern, scale, stepsPerOctave)`**
: Given a pattern yielding scale degrees, convert the degrees into note numbers according to the provided scale and steps per octave. This is done automatically when you use the `'degree'` event key, but there might be cases where you would want to do some further math on the note numbers, and it might be necessary to make the conversion explicit.

**`Pdiff(pattern)`**
: Returns the difference between the source stream's latest and previous values. Among other uses, this can measure whether a stream is ascending or descending. This is the underlying implementation of the `differentiate` method discussed just above.

**`Prorate(proportion, pattern)`**
: Splits up a number from `pattern` according to proportion(s) given by the `proportion` pattern. This is tricky to explain briefly; see the help file for some good examples.
```supercollider
// Swing notes with Prorate
(
p = Pbind(
    \degree, Pseries(4, Pwhite(-2, 2, inf).reject({ |x| x == 0 }), inf).fold(-7, 11),
    \dur, Prorate(0.6, 0.5)    // actually yields 0.3, 0.2, 0.3, 0.2...
).play;
)

p.stop;
```






### Calculations based on other event values
In a Pbind, normally the patterns for the various keys calculate independently. But it's possible for one or more child patterns to depend on the result of another pattern inside the same Pbind. This is done with [Pkey](../../Classes/Pkey.md), described in [A-Practical-Guide/PG_06g_Data_Sharing](../../Tutorials/A-Practical-Guide/PG_06g_Data_Sharing.md).

Previous: [A-Practical-Guide/PG_04_Words_to_Phrases](../../Tutorials/A-Practical-Guide/PG_04_Words_to_Phrases.md)

Next: [A-Practical-Guide/PG_060_Filter_Patterns](../../Tutorials/A-Practical-Guide/PG_060_Filter_Patterns.md)





