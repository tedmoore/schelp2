# Pattern Guide Cookbook 08: Swing

*A filter pattern that turns equal rhythmic divisions into swung notes*

**Related:** [A-Practical-Guide/PG_Cookbook07_Rhythmic_Variations](../../Tutorials/A-Practical-Guide/PG_Cookbook07_Rhythmic_Variations.md), [A-Practical-Guide/PG_Ref01_Pattern_Internals](../../Tutorials/A-Practical-Guide/PG_Ref01_Pattern_Internals.md)

**Categories:** Streams-Patterns-Events>A-Practical-Guide, Tutorials>Pattern-Guide


## Converting equal divisions into "swing"
Most MIDI sequencers have a "swing" feature, which handles a note's timing differently depending on its metric position. A note in a stronger metric position is played on time; a note in a weaker position is delayed by some fraction of the beat.

In SuperCollider patterns, it's more convenient to express rhythm in terms of equal note durations. To mimic the swing-quantize behavior of conventional sequencers, it's helpful to have a way to modify the output events from a pattern so that the metrically-weaker notes sound later, without requiring the original pattern to be aware of the notes' metric positions.


### Requirements

**Parameter: Base rhythmic value**
: You should be able to swing any subdivision of the beat: 8th-, 16th-, quarter-notes. If this is 0.5 (8th-notes), then quarter notes will play unchanged.

**Parameter: Swing amount**
: Fraction of the base rhythm to delay the weaker notes. The actual delay time will be `base_value * swing_amount`.

**Weaker-positioned notes**
: The attack needs to be moved later, using the event's timingOffset (see [A-Practical-Guide/PG_08_Event_Types_and_Parameters#Timing control](../../Tutorials/A-Practical-Guide/PG_08_Event_Types_and_Parameters.md#timing-control)). Also, if the next note is in a stronger position, this note needs to be shorter by the same amount.

**Stronger-positioned notes**
: The attack will not be moved in time; but, if the next note is in a weaker position, this note needs to be slightly longer to compensate for the additional time between note onsets.

**Non-duple subdivisions**
: Swing typically assumes a beat will be divided into two notes. Treating triplets, quintuplets or other divisions by the same algorithm would produce confusing rhythms. So, we may also want a parameter `swingThreshold` to disable swing for notes that are too far away from the base rhythmic value.






### Implementation
[Pchain](../../Classes/Pchain.md) applies one pattern to the result of another pattern. So, if we can write a pattern that will modify the events coming from the source, Pchain will be an easy way to combine them.

The parameters noted above should be provided in the source pattern. Alternately, they may be given as an event at the end of Pchain's list of inputs. (Pchain, following the model of function composition, evaluates its patterns in reverse order. See [A-Practical-Guide/PG_06c_Composition_of_Patterns](../../Tutorials/A-Practical-Guide/PG_06c_Composition_of_Patterns.md).)

So... deep breath...


```
(
~swingify = Prout({ |ev|
    var now, nextTime = 0, thisShouldSwing, nextShouldSwing = false, adjust;
    while { ev.notNil } {
        // current time is what was "next" last time
        now = nextTime;
        nextTime = now + ev.delta;
        thisShouldSwing = nextShouldSwing;
        nextShouldSwing = ((nextTime absdif: nextTime.round(ev[\swingBase])) <= (ev[\swingThreshold] ? 0)) and: {
            (nextTime / ev[\swingBase]).round.asInteger.odd
        };
        adjust = ev[\swingBase] * ev[\swingAmount];
        // an odd number here means we're on an off-beat
        if(thisShouldSwing) {
            ev[\timingOffset] = (ev[\timingOffset] ? 0) + adjust;
            // if next note will not swing, this note needs to be shortened
            if(nextShouldSwing.not) {
                ev[\sustain] = ev.use { ~sustain.value } - adjust;
            };
        } {
            // if next note will swing, this note needs to be lengthened
            if(nextShouldSwing) {
                ev[\sustain] = ev.use { ~sustain.value } + adjust;
            };
        };
        ev = ev.yield;
    };
});
)
```





### Examples

```
p = Pbind(\degree, Pseries(0, 1, 8), \dur, 0.25);

p.play;  // straight 16ths

// swingBase: 0.25: Every other 16th-note is delayed
// swingAmount: 1/3: Off-beat notes will be delayed by 1/3 of a 16th-note
Pchain(~swingify, p, (swingBase: 0.25, swingAmount: 1/3)).play;

// note duration = twice swingBase, no swing (correct)
Pchain(~swingify, Pstretch(2, p), (swingBase: 0.25, swingAmount: 1/3)).play;

// hear the result of different swing amounts
(
Ppar([
    // 60% of a 16th-note
    Pchain(~swingify, p, (swingBase: 0.25, swingAmount: 0.6, pan: -1)),
    // 20% of a 16th-note
    Pchain(~swingify, p, (swingBase: 0.25, swingAmount: 0.2, pan: 1, octave: 6))
]).play;
)


(
q = Ppar([
    // walking bass (by a bass player who only chooses notes randomly)
    Pbind(
        \octave, 3,
        \degree, Pwhite(0, 7, inf),
        \dur, 0.5
    ),
    Pseq([
        Pchain(
            ~swingify,
            Pbind(
                \degree, Pseries(-7, 1, 15) +.x Pseq([0, 9], 1),
                \dur, Pwhite(1, 3, inf) * 0.25
            ),
            (swingBase: 0.25, swingAmount: 0.2)
        ),
        Pfuncn({ q.stop; Event.silent(1) }, 1)
    ])
]).play;
)
```


Swing should not apply to triplets. Note that the rhythmic value 1/6 introduces floating-point rounding error, so we need to raise the threshold slightly. `(1/6)+(1/6)+(1/6)` is within 0.05 of an eighth-note, but `1/6` is not, causing triplet notes to pass through unchanged.


```
// swing threshold: throw a few triplets in
(
Pchain(
    ~swingify,
    Pbind(
        \degree, Pseries(-7, 1, 15),
        \dur, Pwrand([Pn(0.25, 2), Pn(1/6, 3)], [0.7, 0.3], inf)
    ),
    (swingBase: 0.25, swingAmount: 0.2, swingThreshold: 0.05)
).play;
)
```





### Explanation
We need to measure the current metric position against some reference point. The most logical is the time when the pattern started processing. [Prout](../../Classes/Prout.md) allows variables to persist for the entire length of its stream (unlike [Pfunc](../../Classes/Pfunc.md)).


```
(
~swingify = Prout({ |ev|
    var now, nextTime = 0, thisShouldSwing, nextShouldSwing = false, adjust;
```


~~

If the source event is nil, errors will follow, so we should stop looping in that case.


```
    while { ev.notNil } {
```


~~

`now` is what the next time *was*. The time of the next event simply adds `ev.delta`.


```
        now = nextTime;
        nextTime = now + ev.delta;
```


~~

As discussed above, there are two factors to decide whether or not this note should be delayed:


**Is it close enough to the base rhythm grid?**
: Round the current time to the grid, and the difference between the actual and rounded times must be less than the threshold: `(now absdif: now.round(ev[\swingBase])) <= (ev[\swingThreshold] ? 0)`.

**Is it in a weaker metrical position?**
: Dividing by the base value yields an even number for stronger positions, and odd for weaker positions: `(now / ev[\swingBase]).round.asInteger.odd`.



There's room also for a slight optimization. In the previous event, we decided whether the next event would need to swing or not. Now, in the current event, we are processing what used to be "next." So we can just copy the old value of `nextShouldSwing` from last time, instead of redoing the calculation. (Note that this requires `nextShouldSwing = false` in the beginning -- because `now` is always 0 for the first event, and consequently can never swing.)


```
        // current this time is what was "next" last time
        thisShouldSwing = nextShouldSwing;
        nextShouldSwing = ((nextTime absdif: now.round(ev[\swingBase])) <= (ev[\swingThreshold] ? 0)) and: {
            (nextTime / ev[\swingBase]).round.asInteger.odd
        };
        adjust = ev[\swingBase] * ev[\swingAmount];
```


~~

Naming the variables appropriately makes the subsequent "if" block almost self-explanatory. Two notes:

- The event's `timingOffset` may be nonzero, in which case, it would be wrong to overwrite. We need to *adjust* the timing offset: +.
- The original `sustain` value may be calculated from `dur` and `legato`. That calculation is done by the `~sustain` function, which must be executed from within the event ([Environment#-use](../../Classes/Environment.md#-use)).



```
        if(thisShouldSwing) {
            ev[\timingOffset] = (ev[\timingOffset] ? 0) + adjust;
            // if next note will not swing, this note needs to be shortened
            if(nextShouldSwing.not) {
                ev[\sustain] = ev.use { ~sustain.value } - adjust;
            };
        } {
            // if next note will swing, this note needs to be lengthened
            if(nextShouldSwing) {
                ev[\sustain] = ev.use { ~sustain.value } + adjust;
            };
        };
```


~~

`yield` is a bit of a funny method. It doesn't return its result right away. It passes the yielded value to whichever block of code called `next` on the stream, and then pauses. Then, the next time `next` is called, the `yield` method returns, taking its value from `next`'s argument. Here, that will be the event currently being processed, so we need to reassign it to `ev` and loop back.

This is the normal, correct way to handle input values from `next` within routines.


```
        ev = ev.yield;
    };
});
)
```


Previous: [A-Practical-Guide/PG_Cookbook07_Rhythmic_Variations](../../Tutorials/A-Practical-Guide/PG_Cookbook07_Rhythmic_Variations.md)

Next: [A-Practical-Guide/PG_Ref01_Pattern_Internals](../../Tutorials/A-Practical-Guide/PG_Ref01_Pattern_Internals.md)





