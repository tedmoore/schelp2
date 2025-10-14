# LFGauss

*Gaussian function oscillator*

**Categories:** UGens>Generators>Deterministic

## Description

A non-band-limited gaussian function oscillator.
`LFGauss` implements the formula:

where `x` in this context is the phase, which cycles in a range `-1` to `1` over the period **duration**. The Gaussian function in this form is a bell-shaped [apodization function](https://mathworld.wolfram.com/ApodizationFunction.html), making it convenient for use as an envelope.
Its minimum value occurs when the phase `x = -1` and `x = 1`, and its maximum occurs when `x = 0`.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `duration` | Duration of one cycle, in seconds. (Hint: **duration** `= 1/frequency`). Default: `1` |  
| `width` | The width of the bell curve (its standard deviation).Practically speaking, a **width** `<= 0.25` will give minimum values near, but not equal to, zero.The bell curve becomes broader with increasing **width**. Beyond roughly `>= 0.25` the function has the appearance of being truncated, or, when **loop** `= 1`, the cycles begin to "overlap". Default: `0.1` |  
| `iphase` | Initial offset phase offset in the range `[-1, 1]`. Default: 0 |  
| `loop` | If **loop** `> 0`, the function repeats. Otherwise, it calls **doneAction** after one cycle. Default: 1 |  
| `doneAction` | A `doneAction` value, which is evaluated at the end of a cycle (if **loop** `= 0`). `2` frees the synth. Default: `0` (continues running). See [Done / Actions ](../Classes/Done.md#actions) for more options. |  
By default, the maximum value of `LFGauss` is `1`. The minimum value will depend on the **width**, and can by inspected with [minval](#minval).The function can be mapped to a specified range with [range](#range), which can be useful when using `LFGauss` as an envelope that may need to span a range of, e.g., `[0, 1]`.See the examples below for understanding and manipulating the [#Min and max values, curve width](#min-and-max-values,-curve-width).

## Instance Methods

### `minval`
Returns the function's lowest value for the given **width** parameter, which is `exp(1.0 / (-2.0 * width^2))`.### `range`
Scales the output to the given range. This can be convenient when using `LFGauss` as an envelope (see [#examples](#examples) below).
```supercollider
// high width, curve minimum around is 0.25
{ LFGauss.ar(0.01, 0.6) }.plot;
// use .range to map the same function to a specified range
{ LFGauss.ar(0.01, 0.6).range(0, 2) }.plot;
```


## Examples


### Example plots

```supercollider
s.boot;

// a 0.1 second grain
{ LFGauss.ar(0.1, 0.12) }.plot(0.1);

// shift a half-cycle left
{ LFGauss.ar(0.1, 0.12, -1, loop: 0) }.plot(0.1);

// moving further away from the center
{ LFGauss.ar(0.1, 0.12, 2) }.plot(0.2);

// several grains
{ LFGauss.ar(0.065, 0.12, 0, loop: 1) }.plot(0.3);
```




### Min and max values, curve width
[minval](#minval) for a given **width** (assuming **iphase** `= 0`) is:

`minval = exp(-1.0 / (2.0 * squared(width)))`

**width** for a given [minval](#minval) is:

`width = sqrt(-1.0 / log(minval))`

**width** at half of the maximum value(`0.5`) is:

`(2 * sqrt(2 * log(2)) * width) = ca. 2.355 * width`


```supercollider
// minval for a width of 0.1:
(exp(1 / (-2.0 * squared(0.1)))) // 2e-22

// maximum width for a beginning at -60dB:
// we want the beginning small enough to avoid clicks
sqrt(-1 / (2 * log(-60.dbamp))) // 0.269

// minval for width of 0.25
(exp(1 / (-2.0 * squared(0.25)))).ampdb // -70dB

// maximum is always 1:
{ LFGauss.ar(0.1, XLine.kr(1, 0.03, 1), 0, loop: 1) }.plot(1);

// a gaussian curve in sclang:
(0..1000).normalize(-1, 1).collect(_.gaussCurve(1, 0, 0.1)).plot;

// rescale the function to the range 0..1
(
{
    var width = XLine.kr(0.04, 1.0, 1);
    var min = (exp(1.0 / (-2.0 * squared(width))));
    var gauss = LFGauss.ar(0.1, width, loop: 1);
    gauss.linlin(min, 1, 0, 1);
}.plot(1)
);

// range does the same implicitly
(
{
    var width = XLine.kr(0.04, 1.0, 1);
    LFGauss.ar(0.1, width, loop: 1).range(0, 1);
}.plot(1)
);
```




### Sound examples

```supercollider
// modulating duration
{ LFGauss.ar(XLine.kr(0.1, 0.001, 10), 0.03) * 0.2 }.play;

// modulating width, freq 60 Hz
{ LFGauss.ar(1/60, XLine.kr(0.1, 0.001, 10)) * 0.2 }.play;

// modulating both: x position is frequency, y is width factor.
// note the artefacts due to aliasing at high frequencies
{ LFGauss.ar(MouseX.kr(1/8000, 0.1, 1), MouseY.kr(0.001, 0.1, 1)) * 0.1 }.play;

// LFGauss as amplitude modulator
{ LFGauss.ar(MouseX.kr(1, 0.001, 1), 0.1) * SinOsc.ar(1000) * 0.1 }.play;

// modulate iphase
{ LFGauss.ar(0.001, 0.2, [0, MouseX.kr(-1, 1)]).sum * 0.2 }.scope;

// for very small width we are "approaching" a dirac function
{ LFGauss.ar(0.01, SampleDur.ir * MouseX.kr(10, 3000, 1)) * 0.2 }.play;

( // dur and width can be modulated at audio rate
{
    var dur = SinOsc.ar(MouseX.kr(2, 1000, 1) * [1, 1.1]).range(0.0006, 0.01);
    var width = SinOsc.ar(0.5 * [1, 1.1]).range(0.01, 0.3);
    LFGauss.ar(dur, width) * 0.2
}.play
)

( // several frequencies and widths combined
{
    var mod = LFGauss.ar(MouseX.kr(1, 0.07, 1), 1 * (MouseY.kr(1, 3) ** (-1..-6)));
    var carr = SinOsc.ar(200 * (1.3 ** (0..5)));
    (carr * mod).sum * 0.1
}.play
)

( // test spectrum
{
    var son = LeakDC.ar(LFGauss.ar(0.005, 0.2));
    BPF.ar(son * 3, MouseX.kr(60, 2000, 1), 0.05)
}.play
)
```




### Gabor Grain

> **Note:** The gaussian function doesn't start with `0` – it asymptotically approaches it at `-inf` and `inf`. When using it as an envelope, it has to start at some smaller value, and it has an offset for this value. You can remove this offset by explicitly setting the [range](#range), e.g. to `[0, 1]` (this is the default).



```supercollider
// first, visualize LFGauss as a granular envelope on a sine oscillator
(
var freq = 1000;
var ncycles = 10;
var width = 0.25;
var dur = ncycles / freq;
{
    var env = LFGauss.ar(dur, width, loop: 0, doneAction: Done.freeSelf).range;
    var son = FSinOsc.ar(freq, 0.5pi, env);
    son
}.plot(dur);
)

// ... now as a SynthDef
(
SynthDef(\gabor, { |out, i_freq = 440, i_sustain = 1, i_pan = 1, i_amp = 0.1, i_width = 0.25|
    var env = LFGauss.ar(i_sustain, i_width, loop: 0, doneAction: Done.freeSelf).range;
    var son = FSinOsc.ar(i_freq, 0.5pi, env);
    OffsetOut.ar(out, Pan2.ar(son, i_pan, i_amp));
}).add;
)

// modulating various parameters
(
Pdef(\x,
    Pbind(
        \instrument, \gabor,
        \freq, Pbrown(step: 0.01).linexp(0, 1, 100, 14000),
        \dur, Pbrown().linexp(0, 1, 0.004, 0.02),
        \legato, Pbrown(1, 3, 0.1, inf),
        \pan, Pwhite() * Pbrown()
    )
).play
)

// modulating width only
(
Pdef(\x,
    Pbind(
        \instrument, \gabor,
        \freq, 1000,
        \dur, 0.01,
        \width, Pseg(Pseq([0.25, 0.002], inf), 10, \exp),
        \legato, 2
    )
).play
)

// compare with sine grain:
// evaluate this SynthDef and re-run the above Pdefs
(
SynthDef(\gabor, { |out, i_freq = 440, i_sustain = 1, i_pan = 1, i_amp = 0.1, i_width = 0.25|
    var env = EnvGen.ar(Env.sine(i_sustain * i_width), doneAction: Done.freeSelf);
    var son = FSinOsc.ar(i_freq, 0.5pi, env);
    OffsetOut.ar(out, Pan2.ar(son, i_pan, i_amp));
}).add;
)
```






