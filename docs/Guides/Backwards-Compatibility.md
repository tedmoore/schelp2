# Backwards Compatibility

*Classes and methods that improve backwards compatibility with SC2 code*

**Categories:** Language>SC3 vs SC2

There are a number of classes and methods that have been added to allow for backwards compatibility with SC2 code. The most notable of these is `Synth.play`, which is basically a wrapper for `Function.play`.

```
{ SinOsc.ar(440, 0, 0.5) }.play; // creates an arbitrarily named SynthDef and a Synth to play it
Synth.play({ SinOsc.ar(440, 0, 0.5) }); // in SC3 just a wrapper for Function.play with fewer args
```

Both of these will create synth nodes on the default server. Note that neither requires the use of an `Out.ar` [UGen](../Classes/UGen.md); they simply output to the first audio bus. One can however add an [Out](../Classes/Out.md) to Function.play in order to specify.

```
Synth.play({ Out.ar(1, SinOsc.ar(440, 0, 0.5)) });
```

In general, one should be aware of this distinction when using this code. When copying such code for reuse with other SC3 classes (for example in a reusable [SynthDef](../Classes/SynthDef.md)), it will usually be necessary to add an `Out.ar`. Although useful for quick testing these methods are generally inferior to `SynthDef.play`, as the latter is more direct, requires no modifications for general reuse, has greater general flexibility and has slightly less overhead. (Although this is insignificant in most cases, it could be relevant when large numbers of defs or nodes are being created.)
Like `SynthDef.play`, `Function.play` returns a [Synth](../Classes/Synth.md) object which can then be messaged, etc. However, since `Function.play` creates an arbitrarily named [SynthDef](../Classes/SynthDef.md), one cannot reuse the resulting def, at least not without reading its name from the post window, or getting it from the [Synth](../Classes/Synth.md) object.

```
//The following examples are functionally equivalent
x = { arg freq = 440; Out.ar(1, SinOsc.ar(freq, 0, 0.5)) }.play(fadeTime: 0);
x.set(\freq, 880);        // you can set arguments
y = Synth.new(x.defName);    // get the arbitrary defname from x
x.free;
y.free;

x = SynthDef("backcompat-sine", { arg freq = 440; Out.ar(1, SinOsc.ar(freq, 0, 0.5)) }).play;
x.set(\freq, 880);
y = Synth.new("backcompat-sine");
x.free;
y.free;
```

`Function.play` is in general superior to both its SC2 equivalent and `Synth.play`. It has a number of significant features such as the ability to specify the output bus and fade times as arguments. See the [Function](../Classes/Function.md) helpfile for a more in-depth discussion.
A number of other classes and methods have also been added to improve compatibility. These are listed below. In general there are equivalent or better ways of doing the same things in SC3.
| Synth *play | use Function.play or SynthDef.play | 
| --- | --- || GetFileDialog | use [Dialog](../Classes/Dialog.md) | | GetStringDialog |  | | Synth *stop | use Server.freeAll | | Synth *isPlaying | Server.numSynths (this will include non-running nodes) | | Mix *ar *arFill | use Mix *new and *fill | | SimpleNumber.rgb |  | | Rawarray.write |  | 

