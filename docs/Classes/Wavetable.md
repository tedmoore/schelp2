# Wavetable

*sampled audio buffer in wavetable format*

**Related:** [Signal](../Classes/Signal.md)

**Categories:** Collections>Ordered

## Description

A Wavetable is a FloatArray in a special format used by SuperCollider's interpolating oscillators. Wavetables cannot be created by **new**.


## Class Methods

### `sineFill`
Fill a Wavetable of the given size with a sum of sines at the given amplitudes and phases. The Wavetable will be normalized.
```supercollider
Wavetable.sineFill(512, 1.0/[1, 2, 3, 4, 5, 6]).plot;
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `size` | must be a power of 2. |  
| `amplitudes` | an Array of amplitudes for each harmonic beginning with the fundamental. |  
| `phases` | an Array of phases in radians for each harmonic beginning with the fundamental. |  

### `chebyFill`
Fill a Wavetable of the given size with a sum of Chebyshev polynomials at the given amplitudes for use in waveshaping by the [Shaper](../Classes/Shaper.md) ugen.**Arguments:**

| Argument | Description |
|----------|-------------|
| `size` | must be a power of 2 plus 1, eventual wavetable is next power of two size up. |  
| `amplitudes` | an [Array](../Classes/Array.md) of amplitudes for each Chebyshev polynomial beginning with order 1. |  
| `normalize` | a [Boolean](../Classes/Boolean.md) indicating whether to normalize the resulting Wavetable. If the zeroOffset argument is true, the normalization is done for use as a transfer function, using [normalizeTransfer](../Classes/Signal.md#-normalizetransfer), otherwise it just uses [normalize](../Classes/Signal.md#-normalize) to make the absolute peak value 1. Default is true. |  
| `zeroOffset` | a [Boolean](../Classes/Boolean.md) indicating whether to offset the middle of each polynomial to zero. If true, then a zero input will always result in a zero output when used as a [waveshaper](../Classes/Shaper.md). If false, then the "raw" (unshifted) Chebyshev polynomials are used. Default is false. |  

> **Note:** In previous versions, chebyFill always offset the curves to ensure the center value was zero. The zeroOffset argument was added in version 3.7, and the default behavior was changed, so that it no longer offsets.


```supercollider
Wavetable.chebyFill(513, [1]).plot;

// shifted to avoid DC offset when waveshaping a zero signal
Wavetable.chebyFill(513, [0, 1], zeroOffset: true).plot;

// normalized sum of (unshifted) Chebyshev polynomials (the default)
Wavetable.chebyFill(513, [0, 1, 0, 0, 0, 1], normalize: true, zeroOffset: false).plot;

Wavetable.chebyFill(513, [0, 0, 1]).plot;
Wavetable.chebyFill(513, [0.3, -0.8, 1.1]).plot;


// This waveshaping example uses two buffers, one with zero offset and
// the other not.
//
// 1. The offset version gives zero output (DC free) when waveshaping an
// input signal with amplitude of zero (e.g. DC.ar(0)).
//
// 2. The non-offset version makes better use of the full (-1 to 1) range
// when waveshaping a varying signal with amplitude near 1, but (if even
// Chebyshev polynomial degrees are used) will have a DC offset when
// waveshaping a signal with amplitude of zero.
//
// 3. Wrapping the non-offset Shaper in a LeakDC (the third signal in the
// example) cancels out any DC offsets (third version), while making full use
// of the -1 to 1 range.
(
s.waitForBoot({
    var amplitudes = [0, 1, 1, -2, 1];
    var wavs = [
        Wavetable.chebyFill(256+1, amplitudes, normalize: true, zeroOffset: true),
        Wavetable.chebyFill(256+1, amplitudes, normalize: true, zeroOffset: false)
    ];
    b = wavs.collect{ |wav| Buffer.loadCollection(s, wav) };
    s.sync;
    x = {
        var in = SinOsc.ar(100, 0, SinOsc.kr(0.1, 0, 0.5, 0.5));
        Shaper.ar(b, in) ++ LeakDC.ar(Shaper.ar(b[1], in))
    }.scope;
})
)
x.free; b.do(_.free); b = nil;
```



## Instance Methods

### `plot`
Plot the Wavetable in a window. The arguments are not required and if not given defaults will be used.
```supercollider
Wavetable.sineFill(512, [0.5]).plot;
Wavetable.sineFill(512, [1]).plot("Table 1", Rect(50, 50, 150, 450));
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` | a String, the name of the window. |  
| `bounds` | a Rect giving the bounds of the window. |  
| `minval` | the minimum value in the plot. Defaults to the highest value in the data. |  
| `maxval` | the maximum value in the plot. Defaults to the lowest value in the data. |  
| `parent` | Either a [Window](../Classes/Window.md) or [View](../Classes/View.md) may be passed in - then the plot is embedded. Otherwise a new [Window](../Classes/Window.md) is created.
```supercollider
(
var w = Window("parent");
Wavetable.sineFill(512, 1.0/[1, 2, 3, 4, 5, 6]).plot(parent: w);
w.front
)
``` |  
### `asSignal`
Convert the Wavetable into a Signal.
```supercollider
Wavetable.sineFill(512, [1]).asSignal.plot;
```


### Advanced notes: wavetable format

```supercollider
Signal: [a0, a1, a2...]
Wavetable: [2*a0-a1, a1-a0, 2*a1-a2, a2-a1, 2*a2-a3, a3-a2...]
```


This strange format is not a standard linear interpolation (integer + frac), but for (integer part -1) and (1+frac)) due to some efficient maths for integer to float conversion in the underlying C code.



