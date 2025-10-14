# Splay

*Splay spreads an array of channels across the stereo field*

**Categories:** UGens>Multichannel>Panners

**Related:** [SplayAz](../Classes/SplayAz.md), [SplayZ](../Classes/SplayZ.md), [LevelComp](../Classes/LevelComp.md), [Level_Compensation](../Guides/Level_Compensation.md)

## Description

Splay spreads an array of channels across the stereo field. Optional arguments are spread and center, and equal power levelCompensation. The formula for the stereo position is ((0 .. (n - 1)) * (2 / (n - 1)) - 1) * spread + center


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `inArray` | The array of channels to be distributed over the two stereo pairs |  
| `spread` | For spread = 0, all channels end up in the centre, for 1, they have maximum distribution |  
| `level` | An amplitude multiplier for all channels |  
| `center` | Shift the centre of the distribution. |  
| `levelComp` | a flag or numeric value:- `true` : maintain equal power, keeping overall loudness the same.
- `false` : off / no level change,
- float between `0.0` and `1.0` : smooth tuning of levelComp factor:- `0.0` is none -> factor 1
- `0.5` is equal power -> factor (1/n).squared
- `1.0` is equal amplitude -> factor (1/n) |  

### `arFill`
In analogy to Mix:arFill, this method takes a function that produces the channels. The counting index is passed to it.**Arguments:**

| Argument | Description |
|----------|-------------|
| `n` | Number of channels |  
| `function` | Function to return each channel |  
| `spread` | For spread = 0, all channels end up in the centre, for 1, they have maximum distribution |  
| `level` | An amplitude multiplier for all channels |  
| `center` | Shift the centre of the distribution. |  
| `levelComp` | see above |  

## Examples

Basic usage:

```supercollider
// splay 10 chans of sound into 2
(
x = { |spread = 1, level = 0.2, center = 0.0|
    var numchans = 10;
    Splay.ar(
        SinOsc.ar({ |i| LFNoise2.kr(1).exprange(200, 4000) } ! numchans),
        spread,
        level,
        center
        // use levelComp default true
    );
}.play;
)

s.meter;
s.scope;

// change settings dynamically:

x.set(\spread, 1,   \center, 0);   // full stereo
x.set(\spread, 0.5, \center, 0);   // less wide
x.set(\spread, 0,   \center, 0);   // mono center
x.set(\spread, 0.5, \center, 0.5); // spread from center to right
x.set(\spread, 0,   \center, -1);  // all left
x.set(\spread, 1,   \center, 0);   // full stereo

// A similar example written with arFill:
(
x = { |spread = 1, level = 0.2, center = 0.0|
    var numchans = 10;
    Splay.arFill(numchans,
        { |i| SinOsc.ar(LFNoise2.kr(rrand(10, 20), 200, i + 3 * 100))  },
        spread,
        level,
        center
    );
}.play;
)
```




> **Note:** levelComp new takes multiple input options: true, false as before for rough equal power level compensation, and newly added: a float between 0 and 1. This is to offer more choices for level compensation, such as equal maximum amplitude.


For a full discussion, see [LevelComp](../Classes/LevelComp.md); here is an overview of the levelComp variants:

```supercollider
// default is equal power comp: level / (numchans.sqrt)
Splay.ar(ins, spread, level, center); // true is default
// write it explicitly for clarity
Splay.ar(ins, spread, level, center, levelComp: true);
// or do equal power as float levelComp
Splay.ar(ins, spread, level, center, levelComp: 0.5); //

// maximum peak safety by equal amplitude comp: level / numchans
Splay.ar(ins, spread, level, center, levelComp: 1);
// or calculate by hand:
Splay.ar(ins, spread, level / ins.size, center, levelComp: false);

// no compensation, just tune level by hand
Splay.ar(ins, spread, level, center, levelComp: false);
Splay.ar(ins, spread, level, center, levelComp: 0);

// levelComp by float: level / numchans.pow(levelComp),
// so 0.0 is no compensation: level / 1;
//    0.5 is equal power : level / (numchans.sqrt)
//    1.0 is equal amplitude : level / (numchans)
// can be used to tune e.g. between equal power and equal amp:
Splay.ar(ins, spread, level, center, levelComp: 0.75);
```




