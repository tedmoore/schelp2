# Tuning

*represents a musical tuning*

**Related:** [Scale](../Classes/Scale.md)

**Categories:** Tuning

## Description

Represents a musical tuning (e.g. equal temperament, just intonation, etc.). Used in conjunction with [Scale](../Classes/Scale.md) to generate pitch information.

```supercollider
t = Tuning.et12;
t.semitones;        // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
t.ratios;        // [1, 1.0594630943591, 1.1224620483089, 1.1892071150019, etc.]

Pbind(\scale, Scale.major(t), \degree, Pseq((0..7) ++ (6..0) ++ [\rest], 1), \dur, 0.25).play;

// use non-standard tuning
t = Tuning.just;
t.semitones;        // [0, 1.1173128526978, 2.0391000173077, 3.1564128700055, etc.]
t.ratios.collect(_.round(0.001));    // [1, 1.067, 1.125, 1.2, 1.25, 1.333, 1.406, 1.5, etc.]

Pbind(\scale, Scale.major(t), \degree, Pseq((0..7) ++ (6..0) ++ [\rest], 1), \dur, 0.25).play;
```



### Creation
**just, pythagorean, werckmeister, johnston, partch, wcAlpha, bp, etc.**

Creates a tuning from the library stored in `Tuning.all`. For a complete list of available tunings, execute


```supercollider
Tuning.directory
```





## Class Methods

### `et`
Creates an equal-tempered scale based on pitchesPerOctave.
### `choose`
Creates a random tuning from the library, constrained by size (which defaults to 12).
```supercollider
Scale.major(Tuning.choose).tuning.name;
```


### `new`
Creates a Tuning using some or all of the parameters as follows: **tuning** can be the name of a library tuning (in which case that tuning is returned); an array of floats representing the semitone values of the tuning (in which case pitchesPerOctave will be set to the size of the array regardless of the second parameter); or nil (in which case the default tuning for **pitchesPerOctave** will be returned). **octaveRatio** defaults to 2.0, but can be set differently for stretched or compressed tunings.
```supercollider
Tuning.new(\et12);    // standard equal temperament
// custom tuning
Tuning.new(#[0, 0.795, 2.251, 3.251, 4.036, 4.680, 5.915, 7.221, 8.013, 9.29, 9.930, 11.032]);
Tuning.new((0..11).collect(_ * (2.08 ** (1/12))), 2.08, "Stretched ET12");
```



## Instance Methods

### `semitones`
Returns an array of semitone values for the pitch set. [#-as](#-as)(Array) is equivalent; [#-as](#-as)(List) returns it as a list, etc.### `cents`
Returns a array of cent values for the pitch set.### `ratios`
Returns a tuned array of ratios for the pitch set.
## Examples

For examples of use, see the [Scale](../Classes/Scale.md) help file.

