# Pattern Guide 07: Value Conversions

*Describes the default event's conversions for pitch, rhythm and amplitude*

**Related:** [A-Practical-Guide/PG_06g_Data_Sharing](../../Tutorials/A-Practical-Guide/PG_06g_Data_Sharing.md), [A-Practical-Guide/PG_08_Event_Types_and_Parameters](../../Tutorials/A-Practical-Guide/PG_08_Event_Types_and_Parameters.md)

**Categories:** Streams-Patterns-Events>A-Practical-Guide, Tutorials>Pattern-Guide


## Pitch and rhythm conversions in the default event
Using the default event prototype, pitch and rhythm can be specified in Pbind at different levels depending on the musical requirement. The default event prototype includes logic to convert higher-level abstractions into the physical parameters that are useful for synthesis.

The descriptions below start with the ending value that will actually be used, following up with the other values that are used in the calculations: e.g., \delta is based on \dur and \stretch. The calculations may be bypassed by providing another value for the calculated item. If your pattern specifies `\delta` directly, `\dur` and `\stretch` are ignored.

Note also that there is no obligation to use these constructs. The default event prototype is not meant to enforce one model of pitch or rhythm over any other; it simply provides these options, which you may use if they suit the task, or ignore or override if your task calls for something else entirely.


### Timing conversions
Rhythm is based on `\delta` and `\sustain` event keys. Both of these can be calculated from higher-level abstractions: `\dur`, `\stretch` and `\legato`.


**delta**
: The number of beats until the next event. You can give the delta pattern directly, or the default event prototype can calculate it for you based on other values:
**dur**
: Duration of this event.

**stretch**
: A multiplier for duration: `delta = dur * stretch`.




**sustain**
: How many beats to hold this note. After `\sustain` beats, a release message will be sent to the synth node setting its `gate` control to `0`. Your SynthDef should use `gate` in an [EnvGen](../../Classes/EnvGen.md) based on a sustaining envelope (see [Env](../../Classes/Env.md)), and the EnvGen should have a `doneAction` ( [Done](../../Classes/Done.md) ) that releases the synth at the end. You can give the sustain pattern directly, or the default event prototype can calculate it for you based on:
**legato**
: A fraction of the event's duration for which the synth should sustain. `1.0` means this synth will release exactly at the onset of the next; `0.5` means the last half of the duration will be a rest. Values greater than `1.0` produce overlapping notes. `sustain = dur * legato * stretch`.






### Pitch conversions
Pitch handling in the default event is rich, with a large number of options. To use events, it is not necessary to understand all of those options. As the examples have shown, a note-playing pattern produces sensible results even specifying only `\degree`. The other parameters allow you to control how the event gets from `\degree` to the frequency that is finally passed to the new synth. The default event prototype includes reasonable defaults for all of these.

To go from the highest level of abstraction down:


**\degree**
: represents a scale degree. Fractional scale degrees support accidentals: adding `0.1` to an integer scale degree raises the corresponding chromatic note number by a semitone, and subtracting `0.1` lowers the chromatic note number. `0.2` raises or lowers by two semitones, and so on.

**\note**
: is a chromatic note index, calculated from `\degree` based on a `\scale` and modal transposition (`\mtranspose`, scale degrees to raise or lower the note). `\note` is in equal-tempered units of any number of steps to the octave ( `\stepsPerOctave` ).

**\midinote**
: is a 12ET conversion of `\note`, transposed into the right `\octave` and applying gamut transposition (`\gtranspose`, given in stepsPerOctave units). If `\stepsPerOctave` is anything other than `12`, the non-12ET units are scaled into 12 `\midinote` units per octave.

**\freq**
: is calculated from `\midinote` by `midicps`. A chromatic transposition in 12ET units ( `\ctranspose` ) is added.



Most note-playing SynthDefs use `freq` as an argument. If desired, they may use `midinote`, `note` or even `degree`.

To simplify into rules of thumb:

- If your material is organized around scales or modes, use `\degree`.- If the scale has different ascending and descending patterns, use `\note` in your Pbind, with the filter pattern [Pavaroh](../../Classes/Pavaroh.md).

- If your material is organized around equal divisions of the octave (not necessarily 12 divisions), use `\note` (and `\stepsPerOctave` for equal temperament other than 12 notes).
- If your material is organized around MIDI note numbers (or 12-tone equal temperament), `\midinote` will also work.
- If you prefer to give frequencies directly in Hz, use `\freq`.


Following is a complete description of all elements of the pitch system. Feel free to use the ones that are of interest, and ignore the rest.


**freq**
: Frequency in Hz. May be given directly, or calculated based on the following. Pitch may be expressed at any one of several levels. Only one need be used at a time. For instance, if you write pitch in terms of scale degrees, the note, MIDI note and frequency values are calculated automatically for you.
**ctranspose**
: Chromatic transposition, in 12ET units. Added to midinote.

**midinote**
: MIDI note number; 12 MIDI notes = one octave. This may be fractional if needed. Calculated based on:
**root**
: The scale root, given in 12ET MIDI note increments.

**octave**
: The octave number for `\note = 0`. The default is `5`, mapping note `0` onto MIDI note `60`.

**stepsPerOctave**
: How many `\note` units map onto the octave. Supports non-12ET temperaments.

**gtranspose**
: Non-12ET transposition, in `\note` units. Added to note.

**note**
: The note number, in any division of the octave. `0` is the scale root. Calculated based on:
**degree**
: Scale degree.

**scale**
: Mapping of scale degrees onto semitones. Major, for instance, is `[0, 2, 4, 5, 7, 9, 11]`.

**stepsPerOctave**
: (Same as above.)

**mtranspose**
: Modal transposition; added to degree.



See also the [Scale](../../Classes/Scale.md) class for a repository of scale configurations, and the possibility of non-ET tuning.


```supercollider
(
// approximate a major scale with a 19TET chromatic scale
p = Pbind(
    \scale, #[0, 3, 6, 8, 11, 14, 17],
    \stepsPerOctave, 19,
    \degree, Pwhite(0, 7, inf),
    \dur, 0.125,
    \legato, Pexprand(0.2, 6.0, inf)
).play;
)

p.stop;
```





### Amplitude conversion
Finally, you can specify amplitude as `\db` or `\amp`. If it's given as `\db`, the amplitude will be calculated automatically using `.dbamp`.

Previous: [A-Practical-Guide/PG_06g_Data_Sharing](../../Tutorials/A-Practical-Guide/PG_06g_Data_Sharing.md)

Next: [A-Practical-Guide/PG_08_Event_Types_and_Parameters](../../Tutorials/A-Practical-Guide/PG_08_Event_Types_and_Parameters.md)





