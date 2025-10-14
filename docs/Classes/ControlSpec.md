# ControlSpec

*numerical input specification*

**Related:** [Warp](../Classes/Warp.md)

**Categories:** Control, Spec

## Description

The original, and most common spec (see [Spec](../Classes/Spec.md)). A ControlSpec is used by GUI sliders and knobs to specify the range and curve of the controls. ControlSpec may be used in many ways to map from linear 0..1 range to your desired range and back.
The most common way to create a ControlSpec is by

```supercollider
anObject.asSpec // the object may be an array or a symbol
```




## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `minval` | The minimum value of the range. |  
| `maxval` | The maximium value of the range. |  
| `warp` | a [Warp](../Classes/Warp.md), a symbol (e.g. \lin or \exponential: Default value is \lin), or something else that returns a Warp when sent the message .asWarp. A CurveWarp is defined by a number. |  
| `step` | The smallest possible increment. |  
| `default` | The default value. |  
| `units` | The units, e.g. "hz". Used by some gui's as a unit label. |  
| `grid` |  |  


## Instance Methods

### `map`
Maps and constrains a **value** between 0 and 1 to the range between minval and maxval.### `unmap`
Maps and constrains a **value** between minval and maxval to the range between 0 and 1.
```supercollider
g = ControlSpec(0.01, 2000, \exp, 0.1, 220, "Hz");
g.map(0.5); // convert from [0..1] to [0.01..2000]
g.unmap(1000); // convert from [0.01..2000] to [0..1]

// fore and back translation should be close to identical:
g.unmap(g.map(0.5));
```

### `clipLo`
The lower of maxval and minval.### `clipHi`
The higher of maxval and minval.### `constrain`
Returns `value.asFloat.clip(clipLo, clipHi).round(step)`.### `range`
Returns `maxval - minval`.### `guessNumberStep`
Used for EZ GUI classes for guessing a sensible **step** if none is specified.### `gridClass`
Returns the [AbstractGridLines](../Classes/AbstractGridLines.md) subclass corresponding to the current spec, in particular its warp behavior.### `grid`
Get/set an instance of the [AbstractGridLines](../Classes/AbstractGridLines.md) subclass that describes the range and warp behavior of the current spec, e.g. for use by [DrawGrid](../Classes/DrawGrid.md) for drawing grids in [Plotter](../Classes/Plotter.md).
## Examples


```supercollider
g = ControlSpec(0.01, 2000, \exp, 0.1, 220, "Hz");

// or alternatively

[0.001, 2000, \exp, 0.1, 220, "hz"].asSpec;

// or add it to the ControlSpec.specs IdentityDictionary:

ControlSpec.specs[\myFreq] = ControlSpec(0.01, 2000, \exp, 0.01, 440, units: "Hz");
```



```supercollider
// array is used as arguments to ControlSpec.new(minval, maxval, warp, step, default)
[300, 3000, \exponential, 100].asSpec.dump
Instance of ControlSpec {    (0313FC08, gc = 00, fmt = 00, flg = 00, set = 03)
  instance variables [6]
    minval : Integer 300
    maxval : Integer 3000
    warp : Symbol 'exponential'
    step : Integer 100
    default : Integer 300
}

// partially specified ...
[-48, 48].asSpec.dump
Instance of ControlSpec {    (0313FF18, gc = 00, fmt = 00, flg = 00, set = 03)
  instance variables [6]
    minval : Integer -48
    maxval : Integer 48
    warp : Symbol 'linear'
    step : Float 0
    default : Integer -48
}

// a Symbol
\freq.asSpec.dump
Instance of ControlSpec {    (180F4910, gc = 3C, fmt = 00, flg = 00, set = 03)
  instance variables [8]
    minval : Integer 20
    maxval : Integer 20000
    warp : instance of ExponentialWarp (17FEDB30, size = 1, set = 1)
    step : Integer 0
    default : Integer 440
    units : " Hz"
    clipLo : Integer 20
    clipHi : Integer 20000
}


// nil becomes a default ControlSpec
nil.asSpec.dump
Instance of ControlSpec {    (0313FF18, gc = 00, fmt = 00, flg = 00, set = 03)
  instance variables [6]
    minval : Float 0
    maxval : Float 1
    warp : Symbol 'linear'
    step : Float 0
    default : Float 0
}
```



```supercollider
// make a frequency spec with an exponential range from 20 to 20000,
// give it a rounding of 30 (Hz)
a = \freq.asSpec;
a.step = 100;

// equivalent:
a = [20, 20000, 'exp', 100, 440].asSpec;
a.dump;

a.constrain(800); // make sure it is in range and round it.
a.constrain(803); // make sure it is in range and round it.

a.map(0.5);
a.map(0.0); // returns min
a.map(1.5); // exceeds the area: clip, returns max

a.unmap(4000);
a.unmap(22.0);
```



```supercollider
// like in envelopes, a CurveWarp is created by a number:

a = [0, 1, -4].asSpec;
a.map(0.5);
a.unmap(0.99);
a.map((0..10).normalize).plot;

// look at different distributions:
(
var invals = (0..10).normalize;
(-4..4).do { |curve|
    var a = [0, 1, curve].asSpec;
    a.map(invals).plot;
}
);
```



```supercollider
// using spec for sliders:
(
var w, c, d;
w = Window.new("control", Rect(128, 64, 340, 160));
w.front;
c = Slider.new(w, Rect(10, 10, 300, 30));
d = StaticText.new(w, Rect(10, 40, 300, 30));
c.action = {
    d.string = "unmapped value"
    + c.value.round(0.01)
    + "......"
    + "mapped value"
    + a.map(c.value)
};
)
```



```supercollider
// ControlSpec-map can also be used to map ugens
(
var spec;
spec = [100, 18000, \exp].asSpec;
{
    var freq, osc;
    osc = SinOsc.kr(0.1).range(0, 1);
    freq = spec.map(osc);

    freq.dump; // BinaryOpUGen

    SinOsc.ar(
        freq.poll
    )
}.play
)
```




