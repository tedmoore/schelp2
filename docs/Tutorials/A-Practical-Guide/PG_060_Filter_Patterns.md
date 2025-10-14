# Pattern Guide 060: Filter Patterns

*Overview of patterns that modify the behavior of other patterns*

**Related:** [A-Practical-Guide/PG_05_Math_on_Patterns](../../Tutorials/A-Practical-Guide/PG_05_Math_on_Patterns.md), [A-Practical-Guide/PG_06a_Repetition_Contraint_Patterns](../../Tutorials/A-Practical-Guide/PG_06a_Repetition_Contraint_Patterns.md)

**Categories:** Streams-Patterns-Events>A-Practical-Guide, Tutorials>Pattern-Guide


## Filter patterns
Just like filter UGens modify an input signal, filter patterns modify the stream of values coming from a pattern.

We have already seen some operations that modify a stream of values: math operators (which render as [Punop](../../Classes/Punop.md), [Pbinop](../../Classes/Pbinop.md) or [Pnaryop](../../Classes/Pnaryop.md) patterns) and certain collection methods (mainly `collect`, `select` and `reject`). Filter pattern classes can do some other surprising and useful things.

All filter patterns take at least one source pattern, providing the values/events to be filtered. Some filter patterns are designed for value patterns, others for event patterns. A handful work equally well with both single values and events.

Following is a categorized overview. See the separate category documents for more detail.


### Repetition and Constraint patterns
[A-Practical-Guide/PG_06a_Repetition_Contraint_Patterns](../../Tutorials/A-Practical-Guide/PG_06a_Repetition_Contraint_Patterns.md)


**`Pclutch(pattern, connected)`**
: If the `connected` pattern is true, Pclutch returns the next value from `pattern`. If `connected` is false, the previous pattern value is repeated. It's like a clutch in a car: when engaged, the pattern moves forward; when disconnected, it stays where it is.

**`Pn(pattern, repeats)`**
: Embeds the source pattern `repeats` times: simple repetition. This also works on single values: `Pn(1, 5)` outputs the number 1 5 times.

**`Pdup(n, pattern)`**
: `n` and `pattern` are both patterns. Each value from `pattern` is repeated `n` times. If `n` is a pattern, each value can be repeated a different number of times.

**`Psubdivide(n, pattern)`**
: Like Pdup, except the pattern value is divided by the number of repeats (so that the total time for the repeat cycle is the duration value from the source pattern).

**`Pfin(count, pattern)`**
: Returns exactly `count` values from the source pattern, then stops.

**`Pconst(sum, pattern, tolerance)`**
: Output numbers until the sum reaches a predefined limit. The last output value is adjusted so that the sum matches the limit exactly.

**`Pfindur(dur, pattern, tolerance)`**
: Like Pconst, but applying the "constrain" behavior to the event's rhythmic values. The source pattern runs up to the specified duration, then stops. This is very useful if you know how long a musical behavior should go on, but the number of events to fill up that time is not known.

**`Psync(pattern, quant, maxdur, tolerance)`**
: Like Pfindur, but does not have a fixed duration limit. Instead, it plays until either it reaches `maxdur` (in which case it behaves like Pfindur, adjusting the last event so the total duration matches `maxdur`), or the pattern stops early and the last event is rounded up to the next integer multiple of quant.






### Time-based patterns
[A-Practical-Guide/PG_06b_Time_Based_Patterns](../../Tutorials/A-Practical-Guide/PG_06b_Time_Based_Patterns.md)


**`Ptime(repeats)`**
: Returns the amount of time elapsed since embedding.

**`Pstep(levels, durs, repeats)`**
: Repeat a `level` value for its corresponding duration, then move to the next.

**`Pseg(levels, durs, curves, repeats)`**
: Similar to Pstep, but interpolates to the next value instead of stepping abruptly at the end of the duration. Interpolation is linear by default, but any envelope segment curve can be used. `levels`, `durs` and `curves` should be patterns. Related: Use of [Env](../../Classes/Env.md) as a pattern.






### Adding values into event patterns (Or, "Pattern Composition")
[A-Practical-Guide/PG_06c_Composition_of_Patterns](../../Tutorials/A-Practical-Guide/PG_06c_Composition_of_Patterns.md)


**`Pbindf(pattern, pairs)`**
: Adds new key-value pairs onto a pre-existing Pbind-style pattern.

**`Pchain(patterns)`**
: Chains separate Pbind-style patterns together, so that all their key-value pairs go into the same event.






### Parallelizing event patterns
[A-Practical-Guide/PG_06d_Parallel_Patterns](../../Tutorials/A-Practical-Guide/PG_06d_Parallel_Patterns.md)


**`Ppar(list, repeats)`**
: Start each of the event patterns in the `list` at the same time. When the last one finishes, the Ppar also stops. If `repeats` > 1, all the subpatterns start over again from the beginning.

**`Ptpar(list, repeats)`**
: Here, the list consists of `[timeOffset0, pattern0, timeOffset1, pattern1...]` . Each pattern starts after the number of beats given as its time offset. The patterns can start at different times relative to each other.

**`Pgpar(list, repeats)`**
: Like Ppar, but it creates a separate group for each subpattern.

**`Pgtpar(list, repeats)`**
: This is supposed to be like Ptpar with separate groups for the sub patterns, but the class is currently broken.

**`Pspawner(routineFunc)`**
: The function is used to make a routine. A Spawner object gets passed into this routine, and this object is used to add or remove streams to/from the parallel stream. New patterns can be added in sequence or in parallel.

**`Pspawn(pattern, spawnProtoEvent)`**
: Supports most of the features of Pspawner, but uses a pattern to control the [Spawner](../../Classes/Spawner.md) object instead of a routine function.






### Language control methods
[A-Practical-Guide/PG_06e_Language_Control](../../Tutorials/A-Practical-Guide/PG_06e_Language_Control.md)

Some patterns mimic language-style control methods: conditionals ( [Pif](../../Classes/Pif.md) ), loops ( [Pwhile](../../Classes/Pwhile.md) ) and error cleanup ( [Pprotect](../../Classes/Pprotect.md) ).


**`Pif(condition, iftrue, iffalse, default)`**
: Evaluates a pattern `condition` that returns true or false. Then, one value is taken from the true or false branch before going back to evaluate the condition again. The `default` value or pattern comes into play when the true or false branch stops producing values (returns nil). If the `default` is not given, Pif returns control to the parent upon nil from either branch.

**`Pseed(randSeed, pattern)`**
: Random number generators depend on seed values; setting a specific seed produces a repeatable stream of pseudorandom numbers. Pseed sets the random seed before embedding `pattern`, effectively restarting the random number generator at the start of the pattern.

**`Pprotect(pattern, func)`**
: Like the `protect` error handling method, if an error occurs while getting the next value from the pattern, the function will be evaluated before the error interrupts execution.

**`Ptrace(pattern, key, printStream, prefix)`**
: For debugging, Ptrace prints every return value. Is your pattern really doing what you think? This will tell you. A Ptrace is created automatically by the `trace` message: `aPattern.trace(key, printStream, prefix)` --> `Ptrace(aPattern, key, printStream, prefix)`.

**`Pwhile(func, pattern)`**
: Like [Conditional-Execution#while](../../Reference/Conditional-Execution.md#while) as long as the function evaluates to true, the pattern is embedded. The function is checked once at the beginning and thereafter when the pattern comes to an end. If it's applied to an infinite pattern, there's no looping because the pattern never gives control back.






### Server control methods
[A-Practical-Guide/PG_06f_Server_Control](../../Tutorials/A-Practical-Guide/PG_06f_Server_Control.md)


**`Pbus(pattern, dur, fadeTime, numChannels, rate)`**
: Creates a private group and bus for the synths played by the pattern. The group and bus are released when the pattern stops. Useful for isolating signals from different patterns.

**`Pgroup(pattern)`**
: Creates a private group (without private bus) for the pattern's synths.

**`Pfx(pattern, fxname, pairs)`**
: 

**`Pfxb(pattern, fxname, pairs)`**
: Both of these patterns play an effect synth at the tail of the target group. This synth should read from the bus identified by the `out` argument, and write the processed signal onto the same bus using either [ReplaceOut](../../Classes/ReplaceOut.md) or [XOut](../../Classes/XOut.md). Pfx uses whatever bus and group are specified in the incoming event. Pfxb allocates a separate bus and group for the effect and the pattern.

**`Pproto(makeFunction, pattern, cleanupFunc)`**
: Allocate resources on the server and add references to them into the event prototype used to play `pattern`. When the pattern stops (or is stopped), the resources can be removed automatically.






### Data sharing
[A-Practical-Guide/PG_06g_Data_Sharing](../../Tutorials/A-Practical-Guide/PG_06g_Data_Sharing.md)


**`Pkey(key)`**
: Read the `key` in the input event, making previously-calculated values available for other streams.

**`Penvir(envir, pattern, independent)`**
: Run the pattern inside a given environment.

**`Pfset(func, pattern)`**
: Assign default values into the input event before getting each result event out of the given pattern.

**`Plambda(pattern, scope)`**
: Creates a "function scope" into which values are assigned using [Plet](../../Classes/Plet.md), and from which values are retrieved with [Pget](../../Classes/Pget.md). Pget is somewhat like [Pkey](../../Classes/Pkey.md), except that its scope is strictly internal, hidden from the caller. With Pkey, the source values remain present in the event returned to the caller.



Previous: [A-Practical-Guide/PG_05_Math_on_Patterns](../../Tutorials/A-Practical-Guide/PG_05_Math_on_Patterns.md)

Next: [A-Practical-Guide/PG_06a_Repetition_Contraint_Patterns](../../Tutorials/A-Practical-Guide/PG_06a_Repetition_Contraint_Patterns.md)





