# UGen

*Abstract superclass of all unit generators*

**Categories:** UGens, Server>Abstractions

**Related:** [Browse#UGens](../Browse#UGens.md), [Tour_of_UGens](../Guides/Tour_of_UGens.md), [UGens-and-Synths](../Guides/UGens-and-Synths.md)

## Description

UGens represent calculations with signals. They are the basic building blocks of synth definitions on the server, and are used to generate or process both audio and control signals. The many subclasses of UGen are the client-side representations of unit generators, and are used to specify their parameters when constructing synth definitions (see [SynthDef](../Classes/SynthDef.md)).

### Interface
All UGens respond to one or more of the following class methods:

- `ar(arg1, arg2, ...)`
- `kr(arg1, arg2, ...)`
- `ir(arg1, arg2, ...)`


They return a new instance of UGen that calculates at audio/control rate or at initialization only (ir). Some UGens, like [Rand](../Classes/Rand.md), use the `*new` method instead. These methods are implemented in subclasses, where argument names and their meaning depend on the case.

If any argument is an array, they return an array of UGens (see: [Multichannel-Expansion](../Guides/Multichannel-Expansion.md)). If the combination of rates between arguments and ugen are not allowed, calling the methods will throw an error. This method adds the UGen to the current SynthDef, so it only fully works inside a UGen function.


```
{ Blip.ar(Blip.kr(4, 5, 500, 60), 59, 0.1) }.play;
```




### Documentation of mul and add arguments
A great number of UGens take arguments for `mul` and `add` in their `*ar` and `*kr` methods. Because these arguments are so ubiquitous, they are not general documented in the individual help files. Mul and add simply refer to a constant or signal by which to multiply the output of the UGen, and a constant or signal to add to the output of the UGen. (mul happens before add.) They thus correspond in many cases to scaling the amplitude of the UGen signal in the case of mul, and adding a constant or DC offset in the case of add. In most cases the defaults for mul and add are 1 and 0 respectively, and they are commonly implemented using a automatically generated [MulAdd](../Classes/MulAdd.md) UGen for efficiency. See also the `range` and `madd` methods below.




## Class Methods



### `buildSynthDef`
**Returns:** the SynthDef in which the UGen is situated.
```
{ UGen.buildSynthDef.dump; Silent.ar }.play;
```



### Internally used class methods

### `multiNew`
These methods are responsible for multichannel expansion. They call `*new1(rate, ...args)` for each parallel combination. Most `*ar / *kr` methods delegate to [#*multiNewList](#*multinewlist).**Arguments:**

| Argument | Description |
|----------|-------------|
| `... args` | The first argument is rate, then the rest of the arguments. `(rate, ...args)` |  


### `multiNewList`
See [#*multiNew](#*multinew).**Arguments:**

| Argument | Description |
|----------|-------------|
| `args` | An array where the first argument is rate, then the rest of the arguments. `([rate, ...args])` |  


### `new1`
This method returns a single instance of the UGen, not multichannel expanded. It is called inside multiNewList, whenever a new single instance is needed.

### `methodSelectorForRate`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `rate` | A [Symbol](../Classes/Symbol.md), `\audio, \control, \scalar` |  
**Returns:** An appropriate message selector ([Symbol](../Classes/Symbol.md) like `\ar, \kr, \ir`) for the given rate.

### `replaceZeroesWithSilence`
**Returns:** A new [Array](../Classes/Array.md), where every zero is replaced by a [Silent](../Classes/Silent.md) UGen.This is required internally sometimes for UGens like [Out](../Classes/Out.md).


## Instance Methods


### Convenience Methods

### `scope`
Displays the output of this UGen in an individual [Stethoscope](../Classes/Stethoscope.md) window.**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` | The name of the window |  
| `bufsize` | Buffer size |  
| `zoom` | Zoom factor |  

```
s.boot

{ Ringz.ar(PinkNoise.ar([0.1, 0.2]).scope(\pink), 2000, 1, 0.25) }.play; // multichannel works
s.scope; // can still separately scope the output of the server
```



### `poll`
Polls the output of this UGen every interval seconds, and posts the result.**Arguments:**

| Argument | Description |
|----------|-------------|
| `trig` | Trig frequency |  
| `label` | A symbol to label the output |  
| `trigid` | Numerical ID |  
The default trig is 10, which converts to 10 triggers per second (or every 0.1 seconds). See [Poll](../Classes/Poll.md) for more info on polling.
```
{ SinOsc.ar(LFNoise0.ar(2).range(420, 460).poll(label: \LFNoise), 0, 0.2) }.play;

// multichannel polling:
(
{
    var freqs = SinOsc.ar([0.2, 0.3]).range(420, 460);
    freqs.poll(label: [\freq1, \freq2]);
    SinOsc.ar(freqs, 0, 0.2);
}.play;
)
```



### `dpoll`
Like `poll`, only that `dpoll` is used for Demand ugens. See [Poll](../Classes/Poll.md) for more info on polling.

### `range`
Scales the output of this UGen to be within the range of `lo` and `hi`.Note that `range` expects the default output range, and thus should not be used in conjunction with mul and add arguments.
```
{ SinOsc.ar(SinOsc.ar(0.3).range(440, 660), 0, 0.5) * 0.1 }.play;
```



### `exprange`
Maps the output of this UGen exponentially to be within the range of `lo` and `hi` using a [LinExp](../Classes/LinExp.md) UGen.`lo` and `hi` should both be non-zero and have the same sign. Note that `exprange` expects the default output range, and thus should not be used in conjunction with mul and add arguments.
```
{ SinOsc.ar(SinOsc.ar(0.3).exprange(440, 6600), 0, 0.5) * 0.1 }.play;
```



### `curverange`
Scales the output of this UGen to be within the range of `lo` and `hi` using a curve factor of `curve`.Note that `curverange` expects the default output range, and thus should not be used in conjunction with mul and add arguments.
```
{ SinOsc.ar(SinOsc.ar(0.3).curverange(440, 660, -3), 0, 0.5) * 0.1 }.play;
```



### `unipolar`
Scales the output of this UGen to be between `(0..mul)` range (default 1).Note that `unipolar` expects the default output range, and thus should not be used in conjunction with mul and add arguments.
```
{ SinOsc.ar(300, 0, 0.5) * SinOsc.kr(2).unipolar * 0.1 }.play;
```



### `bipolar`
Scales the output of this UGen to be between `(-mul..mul)` range (default 1).Note that `bipolar` expects the default output range, and thus should not be used in conjunction with mul and add arguments.
```
{ SinOsc.ar(500 + LFPulse.ar(4).bipolar(40), 0, 0.5) * 0.1 }.play;
```



### `degrad`
Converts degrees to radians. This method multiplies the receiver's output by `pi/180`.

### `raddeg`
Converts radians to degrees. This method multiplies the receiver's output by `180/pi`.

### `clip`
Wraps the receiver in a [Clip](../Classes/Clip.md) UGen, clipping its output at `lo` and `hi`.

### `fold`
Wraps the receiver in a [Fold](../Classes/Fold.md) UGen, folding its output at `lo` and `hi`.

### `wrap`
Wraps the receiver in a [Wrap](../Classes/Wrap.md) UGen, wrapping its output at `lo` and `hi`.

### `blend`
Blends `this` with `that` by wrapping the receiver in an [XFade2](../Classes/XFade2.md) (if `this` or `that` are audio-rate UGens) or [LinXFade2](../Classes/LinXFade2.md) UGen.
> **Note:** The `blendFrac` argument is between 0 and 1



### `lag`
Wraps the receiver in a [Lag](../Classes/Lag.md) UGen, smoothing its output by `t1` seconds lagtime. If a second argument is given, it wraps it in a [LagUD](../Classes/LagUD.md) UGen.

### `lag2`
Wraps the receiver in a [Lag2](../Classes/Lag2.md) UGen, smoothing its output by `t1` seconds lagtime. If a second argument is given, it wraps it in a [Lag2UD](../Classes/Lag2UD.md) UGen.

### `lag3`
Wraps the receiver in a [Lag3](../Classes/Lag3.md) UGen, smoothing its output by `t1` seconds lagtime. If a second argument is given, it wraps it in a [Lag3UD](../Classes/Lag3UD.md) UGen.

### `lagud`
Wraps the receiver in a [LagUD](../Classes/LagUD.md) UGen, smoothing its output by `lagtimeU` and `lagtimeD`.

### `lag2ud`
Wraps the receiver in a [Lag2UD](../Classes/Lag2UD.md) UGen, smoothing its output by `lagtimeU` and `lagtimeD`.

### `lag3ud`
Wraps the receiver in a [Lag3UD](../Classes/Lag3UD.md) UGen, smoothing its output by `lagtimeU` and `lagtimeD`.

### `varlag`
Wraps the receiver in a [VarLag](../Classes/VarLag.md) UGen, smoothing its output by `time` seconds.

### `slew`
Wraps the receiver in a [Slew](../Classes/Slew.md) UGen, limiting the slope of its output.

### `degreeToKey`
Wraps the receiver in a [DegreeToKey](../Classes/DegreeToKey.md) UGen.

### `minNyquist`
Wraps the receiver in a `min` [BinaryOpUGen](../Classes/BinaryOpUGen.md), such that the lesser of the receiver's output and the Nyquist frequency is output. This can be useful to prevent aliasing.

### `snap`
Wraps the receiver so that its values are rounded within `margin` distance from a multiple of `resolution` to a multiple of resolution. By using `margin` and `strength` you can control when values will be rounded, and by how much. See [SimpleNumber#-snap](../Classes/SimpleNumber.md#-snap) for more details.This can be used to make control signals (e.g. from sensors) "snap" to defined resolution. Example:
```
s.boot;
x = { SinOsc.ar((Line.kr(0, 10, 10).snap(1, 0.3, 1) + 60).poll.midicps, 0, -24.dbamp) }.play
```



### `softRound`
Wraps the receiver so that its values are rounded outside of `margin` distance from a multiple of `resolution` to a multiple of resolution. By using `margin` and `strength` you can control when values will be rounded, and by how much. See [SimpleNumber#-softRound](../Classes/SimpleNumber.md#-softround) for more details.

### `linlin`
Wraps the receiver so that a linear input range is mapped to a linear output range.The clip argument can be one of the four:| `nil` | do not clip at outMin or outMax | 
| --- | --- || `\minmax` | clip at outMin or outMax | | `\min` | clip at outMin | | `\max` | clip at outMax | Example:
```
{ Line.ar(-1, 5, 0.1).linlin(0, 3, -1, 1) }.plot(0.1);

// modulate some values
(
{ Line.ar(-1, 5, 0.1).lincurve(SinOsc.ar(100), SinOsc.ar(130) + 3, -1, 1, clip: nil) }
    .plot(0.1, minval: -15, maxval: 5)
)
```



### `linexp`
Wraps the receiver so that a linear input range is mapped to an exponential output range.outMin and outMax must be nonzero and of the same sign. For clip argument, see `linlin` above.
```
{ Line.ar(-1, 5, 0.1).linexp(0, 3, 0.01, 1) }.plot(0.1);
```



### `explin`
Wraps the receiver so that an exponential input range is mapped to a linear output range.inMin and inMax must be nonzero and of the same sign. For clip argument, see `linlin` above.
```
{ Line.ar(1, 5, 0.1).explin(1, 3, -1, 1) }.plot(0.1);
```



### `expexp`
Wraps the receiver so that an exponential input range is mapped to an exponential output range.outMin, outMax, inMin and inMax must be nonzero and of the same sign. For clip argument, see `linlin` above.
```
{ Line.ar(1, 5, 0.1).expexp(1, 3, 0.01, 1) }.plot(0.1);
```



### `lincurve`
Wraps the receiver so that a linear input range is mapped to a curve-like exponential output range.outMin and outMax may be zero and of the different sign. For clip argument, see `linlin` above.
```
{ Line.ar(-1, 5, 0.1).lincurve(0, 3, -1, 1, curve: -4) }.plot(0.1);

// modulate the curve. Unlike with numbers and CurveSpec, the curve absolute value
// should not be much smaller than 0.5.
{ SinOsc.ar(100).lincurve(-1, 1, -1, 1, XLine.kr(-3, -100, 0.1)) * 0.1 }.plot(0.1);
```



### `curvelin`
Wraps the receiver so that a curve-like exponential input range is mapped to a linear output range.inMin and inMax may be zero and of the different sign. For clip argument, see `linlin` above.
```
{ Line.ar(-1, 5, 0.1).curvelin(0, 3, -1, 1, curve: -4) }.plot(0.1);
```



### `bilin`
Map the receiver from two assumed linear input ranges (inMin..inCenter) and (inCenter..inMax) to two linear output ranges (outMin..outCenter) and (outCenter..outMax). If the input exceeds the input range, the following behaviours are specified by the clip argument.**Arguments:**

| Argument | Description |
|----------|-------------|
| `inCenter` |  |  
| `inMin` | assumed input minimum |  
| `inMax` | assumed input maximum |  
| `outCenter` |  |  
| `outMin` | output minimum |  
| `outMax` | output maximum |  
| `clip` | nil (don't clip) \max (clip ceiling) \min (clip floor) \minmax (clip both - this is default). |  

```
{ Line.kr(0, 10, 0.1).bilin(1, 0, 10, 0.6, 0, 1) }.plot(0.1)
```



### `prune`
Limits the receiver range to one of the four clip modes, see `linlin` above.

### `checkBadValues`
Wraps the receiver in a [CheckBadValues](../Classes/CheckBadValues.md) UGen with the corresponding `id` and `post` flag.

### `if`
Outputs trueUGen when the receiver outputs 1, falseUGen when the receiver outputs 0. If the receiver outputs a value between 0 and 1, a mixture of both will be played.This is implemented as: `(this * (trueUGen - falseUGen)) + falseUGen)`Note that both trueUGen and falseUGen will be calculated regardless of whether they are output, so this may not be the most efficient approach.
```
// note different syntax in these two examples
{ if(LFNoise1.kr(1.0, 0.5, 0.5), SinOsc.ar, Saw.ar) * 0.1 }.play;

{ Trig1.ar(Dust.ar(3), 0.2).lag(0.1).if(FSinOsc.ar(440), FSinOsc.ar(880)) * 0.1 }.play;
```



### `binaryValue`
Outputs 1, representing true for positive, 0 representing false for negative or zero input values.

### `isPositive`
Outputs 1, representing true for positive or zero, 0 representing false for negative input values.

### `isStrictlyPositive`
Outputs 1, representing true for positive, 0 representing false for negative or zero input values.

### `isNegative`
Outputs 1, representing true for negative, 0 representing false for positive or zero input values.

### `|==|`
Outputs 1, representing true, when the receiver and argument signal coincide. Note that this may be ambivalent in many cases, because of floating point arithmetic. A special sign is needed, because `==` compares the UGen objects, and not the signal they produce.
```
// an example of floating point relevance for the |==| operator.
// the rounded signal will match at some point, but not the direct signal
(
{
    var a = Line.ar(0, 1, 0.008);
    var b = a |==| 0.5;
    var c = a.round(0.01) |==| 0.5;
    [a, Trig1.ar(b, 0.001), Trig1.ar(c, 0.001)]
}.plot
)
```



### `@`
Dynamic geometry support. Returns `Point(this, y)`.
```
{ (SinOsc.ar(1001) @ SinOsc.ar(1207)).rho }.scope;
```



### `asComplex`
Complex math support. Returns `Complex(this, 0.0)`.

### `dumpArgs`
Posts a list of the arguments for this UGen and their values.

### Other Instance Methods
The following methods and instance variables are largely used in the construction of synth definitions, synth descriptions (see [SynthDesc](../Classes/SynthDesc.md)), UGen class definitions, etc., and are usually not needed for general use. Users should not attempt to set any of these values in general code.


### `synthDef`
The SynthDef which contains the UGen.

### `inputs`
The array of inputs to the UGen.

### `rate`
The output rate of the UGen which is one of the [Symbol](../Classes/Symbol.md)s `\audio`, or `\control`.

### `signalRange`
**Returns:** A symbol indicating the signal range of the receiver. Either `\bipolar` or `\unipolar`.

### `numChannels`
**Returns:** The number of output channels.For a UGen, this will always be 1, but [Array](../Classes/Array.md) also implements this method, so multichannel expansion is supported. See [Multichannel-Expansion](../Guides/Multichannel-Expansion.md).

### `numInputs`
**Returns:** The number of inputs for this UGen.

### `numOutputs`
**Returns:** The number of outputs for this UGen.

### `name`
**Returns:** The Class name of the receiver as a [String](../Classes/String.md).

### `madd`
Wraps the receiver in a [MulAdd](../Classes/MulAdd.md) UGen.This is for the most part only used in UGen class definitions in order to allow efficient implementation of `mul` and `add` arguments.

### `isValidUGenInput`
**Returns:** true

### `asUGenInput`
**Returns:** the receiverThis method is implemented in a number of classes in order to allow objects like [Node](../Classes/Node.md)s, [Bus](../Classes/Bus.md)ses, and [Buffer](../Classes/Buffer.md)s to be passed directly as UGen inputs and [Synth](../Classes/Synth.md) args.

### `copy`
**Returns:** the receiver.Thus UGen-dup effectively returns a reference to the original and is a convenient way to copy a mono signal to multiple channels.
```
{ SinOsc.ar(Rand(200, 4000), 0, 0.2).dup }.plot // this is the same UGen
```

Function-dup evaluates that function multiple times, thus potentially returning distinct UGens.
```
{ { SinOsc.ar(Rand(200, 4000), 0, 0.2) }.dup }.plot // these are different UGens
```



### Internally used instance methods

### `methodSelectorForRate`
See [#*methodSelectorForRate](#*methodselectorforrate)

### `init`
By default, this method stores the inputs (e.g. the arguments to `*ar` and `*kr`) in the UGen.This may be overridden to do other initialisations, as long as the inputs are set correctly.

### Bela

### `belaScope`
Send this UGen's output to Bela's Oscilloscope (see [BelaScope](../Classes/BelaScope.md) for required setup)**Arguments:**

| Argument | Description |
|----------|-------------|
| `scopeChannel` | Bela's oscilloscope channel to start scoping on. This has to be a non-negative number, and can't be changed after scoping starts. |  
| `server` | The server on which BelaScope is running. If not specified, it looks for the first server for which BelaScope was already initialized. If none is found, it attempts to initialize a [BelaScope](../Classes/BelaScope.md) instance on [Server#*default](../Classes/Server.md#*default). |  
**Returns:** This UGen.


