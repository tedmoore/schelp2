# Signal

*Sampled audio buffer*

**Related:** [Wavetable](../Classes/Wavetable.md)

**Categories:** Collections>Ordered

## Description

A Signal is a FloatArray that represents a sampled function of time buffer. Signals support math operations.


## Class Methods

### `sineFill`
Fill a Signal of the given size with a sum of sines at the given amplitudes and phases. The Signal will be normalized.
```supercollider
Signal.sineFill(1000, 1.0/[1, 2, 3, 4, 5, 6]).plot;
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `size` | the number of samples in the Signal. |  
| `amplitudes` | an Array of amplitudes for each harmonic beginning with the fundamental. |  
| `phases` | an Array of phases in radians for each harmonic beginning with the fundamental. |  

### `chebyFill`
Fill a Signal of the given size with a sum of Chebyshev polynomials at the given amplitudes. For eventual use in waveshaping by the Shaper ugen; see [Shaper](../Classes/Shaper.md) helpfile and [Buffer:cheby](../Classes/Buffer.md#-cheby) too.**Arguments:**

| Argument | Description |
|----------|-------------|
| `size` | the number of samples in the Signal. |  
| `amplitudes` | an [Array](../Classes/Array.md) of amplitudes for each Chebyshev polynomial beginning with order 1. |  
| `normalize` | a [Boolean](../Classes/Boolean.md) indicating whether to normalize the resulting Signal. If the zeroOffset argument is true, the normalization is done for use as a transfer function, using [normalizeTransfer](../Classes/Signal.md#-normalizetransfer), otherwise it just uses [normalize](../Classes/Signal.md#-normalize) to make the absolute peak value 1. Default is true. |  
| `zeroOffset` | a [Boolean](../Classes/Boolean.md) indicating whether to offset the middle of each polynomial to zero. If true, then a zero input will always result in a zero output when used as a [waveshaper](../Classes/Shaper.md). If false, then the "raw" (unshifted) Chebyshev polynomials are used. Default is false. |  

> **Note:** In previous versions, chebyFill always offset the curves to ensure the center value was zero. The zeroOffset argument was added in version 3.7, and the default behavior was changed, so that it no longer offsets.


```supercollider
Signal.chebyFill(1000, [1]).plot;

// shifted to avoid DC offset when waveshaping a zero signal
Signal.chebyFill(1000, [0, 1], zeroOffset: true).plot;

// normalized sum of (unshifted) Chebyshev polynomials (the default)
Signal.chebyFill(1000, [0, 1, 0, 0, 0, 1], normalize: true, zeroOffset: false).plot;

Signal.chebyFill(1000, [0, 0, 1]).plot;
Signal.chebyFill(1000, [0.3, -0.8, 1.1]).plot;


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
    var sigs = [
        Signal.chebyFill(256+1, amplitudes, normalize: true, zeroOffset: true),
        Signal.chebyFill(256+1, amplitudes, normalize: true, zeroOffset: false)
    ];
    b = sigs.collect{ |sig| Buffer.loadCollection(s, sig.asWavetableNoWrap) };
    s.sync;
    x = {
        var in = SinOsc.ar(100, 0, SinOsc.kr(0.1, 0, 0.5, 0.5));
        Shaper.ar(b, in) ++ LeakDC.ar(Shaper.ar(b[1], in))
    }.scope;
})
)
x.free; b.do(_.free); b = nil
```


### `hanningWindow`
Fill a Signal of the given size with a Hanning window.
```supercollider
Signal.hanningWindow(1024).plot;
Signal.hanningWindow(1024, 512).plot;
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `size` | the number of samples in the Signal. |  
| `pad` | the number of samples of the size that is zero padding. |  

### `hammingWindow`
Fill a Signal of the given size with a Hamming window.> **⚠️ Warning:** In versions of SuperCollider before 3.11, the implementation of `Signal.hammingWindow` had incorrect coefficients. To get the old behavior back, use `Signal.hammingWindow_old`.
```supercollider
Signal.hammingWindow(1024).plot;
Signal.hammingWindow(1024, 512).plot;
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `size` | the number of samples in the Signal. |  
| `pad` | the number of samples of the size that is zero padding. |  

### `welchWindow`
Fill a Signal of the given size with a Welch window.
```supercollider
Signal.welchWindow(1024).plot;
Signal.welchWindow(1024, 512).plot;
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `size` | the number of samples in the Signal. |  
| `pad` | the number of samples of the size that is zero padding. |  

### `rectWindow`
Fill a Signal of the given size with a rectangular window.
```supercollider
Signal.rectWindow(1024).plot;
Signal.rectWindow(1024, 512).plot;
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `size` | the number of samples in the Signal. |  
| `pad` | the number of samples of the size that is zero padding. |  

### `fftCosTable`
Fourier Transform: Fill a Signal with the cosine table needed by the FFT methods. See also the instance methods [fft](#fft) and [ifft](#ifft).
```supercollider
Signal.fftCosTable(512).plot;
```


### `hammingWindow_old`
This used to be `Signal.hammingWindow`, but the coefficients were incorrect (making it a different window in the generalized Hamming window family). It is provided to assist in porting code to 3.11 and later.

## Instance Methods

### `plot`
Plot the Signal in a window. The arguments are not required and if not given defaults will be used.
```supercollider
Signal.sineFill(512, [1]).plot;
Signal.sineFill(512, [1]).plot("Signal 1", Rect(50, 50, 150, 450));
```

For details, see [plot](../Reference/plot.md)### `play`
Loads the signal into a buffer on the server and plays it. Returns the buffer so you can free it again.
```supercollider
b = Signal.sineFill(512, [1]).play(true, 0.2);
b.free;    // free the buffer again.
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `loop` | A [Boolean](../Classes/Boolean.md) whether to loop the entire signal or play it once. Default is false. |  
| `mul` | volume at which to play it, 0.2 by default. |  
| `numChannels` | if the signal is an interleaved multichannel file, number of channels, default is 1. |  
| `server` | the server on which to load the signal into a buffer. |  
### `waveFill`
Fill the Signal with a function evaluated over an interval.**Arguments:**

| Argument | Description |
|----------|-------------|
| `function` | a function that should calculate the value of a sample.
```supercollider
(
a = Signal.newClear(256);
a.waveFill({ |x, old, i| sin(x) }, 0, 3pi);
a.waveFill({ |x, old, i| old * sin(11 * x + 0.3) }, 0, 3pi);
a.waveFill({ |x, old, i| old * (x % 4) }, 0, 3pi);

a.plot;
)
```

The function is called with three arguments:
**x**
: the value along the interval.

**old**
: the old value (if the signal is overwritten)

**i**
: the sample index.

As arguments, three values are passed to the function: the current input value (abscissa), the old value (if the signal is overwritten), and the index.
```supercollider
(
a = Signal.newClear(16);
a.waveFill({ |x, prev, i| [x, prev, i].postln; sin(x).max(0) }, 0, 3pi);
a.plot;
)
``` |  
| `start` | the starting value of the interval. |  
| `end` | the ending value of the interval. |  
### `asWavetable`
Convert the Signal into a Wavetable.
```supercollider
Signal.sineFill(512, [1]).asWavetable.plot;
```

### `fill`
Fill the Signal with a value.
```supercollider
Signal.newClear(512).fill(0.2).plot;
```

### `scale`
Scale the Signal by a factor **in place**.
```supercollider
a = Signal[1, 2, 3, 4];
a.scale(0.5); a;
```

### `offset`
Offset the Signal by a value **in place**.
```supercollider
a = Signal[1, 2, 3, 4];
a.offset(0.5); a;
```

### `peak`
Return the peak absolute value of a Signal.
```supercollider
Signal[1, 2, -3, 2.5].peak;
```

### `normalize`
Normalize the Signal **in place** such that the maximum absolute peak value is 1.
```supercollider
Signal[1, 2, -4, 2.5].normalize;
Signal[1, 2, -4, 2.5].normalize(0, 1);    // normalize only a range
```

### `normalizeTransfer`
Normalizes a transfer function so that the center value of the table is offset to zero and the absolute peak value is 1. Transfer functions are meant to be used in the [Shaper](../Classes/Shaper.md) ugen.
```supercollider
Signal[1, 2, 3, 2.5, 1].normalizeTransfer;
```

### `invert`
Invert the Signal **in place**.
```supercollider
a = Signal[1, 2, 3, 4];
a.invert(0.5); a;
```

### `reverse`
Reverse a subrange of the Signal **in place**.
```supercollider
a = Signal[1, 2, 3, 4];
a.reverse(1, 2); a;
```

### `fade`
Fade a subrange of the Signal **in place**.
```supercollider
a = Signal.fill(10, 1);
a.fade(0, 3);        // fade in
a.fade(6, 9, 1, 0);    // fade out
```

### `integral`
Return the integral of a signal.
```supercollider
Signal[1, 2, 3, 4].integral;
```

### `overDub`
Add a signal to myself starting at the index. If the other signal is too long only the first part is overdubbed.
```supercollider
a = Signal.fill(10, 100);
a.overDub(Signal[1, 2, 3, 4], 3);

        // run out of range
a = Signal.fill(10, 100);
a.overDub(Signal[1, 2, 3, 4], 8);

a = Signal.fill(10, 100);
a.overDub(Signal[1, 2, 3, 4], -4);

a = Signal.fill(10, 100);
a.overDub(Signal[1, 2, 3, 4], -1);

a = Signal.fill(10, 100);
a.overDub(Signal[1, 2, 3, 4], -2);

a = Signal.fill(4, 100);
a.overDub(Signal[1, 2, 3, 4, 5, 6, 7, 8], -2);
```

### `overWrite`
Write a signal to myself starting at the index. If the other signal is too long only the first part is overdubbed.
```supercollider
a = Signal.fill(10, 100);
a.overWrite(Signal[1, 2, 3, 4], 3);

        // run out of range
a = Signal.fill(10, 100);
a.overWrite(Signal[1, 2, 3, 4], 8);

a = Signal.fill(10, 100);
a.overWrite(Signal[1, 2, 3, 4], -4);

a = Signal.fill(10, 100);
a.overWrite(Signal[1, 2, 3, 4], -1);

a = Signal.fill(10, 100);
a.overWrite(Signal[1, 2, 3, 4], -2);

a = Signal.fill(4, 100);
a.overWrite(Signal[1, 2, 3, 4, 5, 6, 7, 8], -2);
```

### `blend`
Blend two signals by some proportion.
```supercollider
Signal[1, 2, 3, 4].blend(Signal[5, 5, 5, 0], 0);
Signal[1, 2, 3, 4].blend(Signal[5, 5, 5, 0], 0.2);
Signal[1, 2, 3, 4].blend(Signal[5, 5, 5, 0], 0.4);
Signal[1, 2, 3, 4].blend(Signal[5, 5, 5, 0], 1);
Signal[1, 2, 3, 4].blend(Signal[5, 5, 5, 0], 2);
```


### Fourier Transform
### `fft`
Perform an FFT on a real and imaginary signal in place. See also the class method [#*fftCosTable](#*fftcostable).
```supercollider
(
var size = 512;
var real, imag, cosTable, frqAmpPhs, complex;

// Create a signal of sine partials:
// partial freqs, amps, and phases
frqAmpPhs = [
    // 0 Hz (DC), amp: 1, phase pi/2 (cosine)
    [0, 1, 0.5pi],
    // other partials, various amp and phase
    [8], [13, 0.25], [21, 0.25], [55, 0.5, 0.5pi],
    // nyquist, amp: 1, phase pi/2 (cosine)
    [size/2, 1, 0.5pi]
];
real = Signal.newClear(size);
real.sineFill2(frqAmpPhs);

imag = Signal.newClear(size); // zeros
cosTable = Signal.fftCosTable(size);

// Perform fft
complex = fft(real, imag, cosTable);

// Plot signals and spectrum
[
    real,
    imag,
    (complex.magnitude) / size
]
.plot("fft", Window.screenBounds.insetBy(*200!2))
.axisLabelX_(["Signal (real, samples)", "Signal (imaginary, samples)", "FFT spectrum (bins)"])
.axisLabelY_(["Amplitude", "Amplitude", "Magnitude"])
.plotMode_([\linear, \linear, \steps]);
)
```


### `ifft`
Perform an inverse FFT on a real and imaginary signal in place. See also the class method [#*fftCosTable](#*fftcostable).
```supercollider
(
var real, imag, cosTable, complex, ifft;
var size = 512;

// Create a signal of sine partials, add noise
real = Signal.newClear(size);
real.sineFill2([[8], [13, 0.5], [21, 0.25], [55, 0.125, 0.5pi]]);
real.overDub(Signal.fill(size, { 0.2.bilinrand }));

imag = Signal.newClear(size); // zeros
cosTable = Signal.fftCosTable(size);

// Perform fft & ifft
complex = fft(real, imag, cosTable).postln;
ifft = complex.real.ifft(complex.imag, cosTable);

// Plot input and output
[
    real,
    ifft.real
]
.plot("fft -> ifft", Window.screenBounds.insetBy(*200!2))
.axisLabelX_(["Real signal (samples)", "Restored signal (samples)"])
.axisLabelY_("Amplitude");
)
```



### Unary Messages
Signal will respond to unary operators by returning a new Signal.


```supercollider
x = Signal.sineFill(512, [0, 0, 0, 1]);
[x, x.neg, x.abs, x.sign, x.squared, x.cubed, x.asin.normalize, x.exp.normalize, x.distort].flop.flat
    .plot(numChannels: 9);
```


### `neg`, `abs`, `sign`, `squared`, `cubed`, `sqrt`, `exp`, `log`, `log2`, `log10`, `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `sinh`, `cosh`, `tanh`, `distort`, `softclip`, `isPositive`, `isNegative`, `isStrictlyPositive`


### Binary Messages
Signal will respond to binary operators by returning a new Signal.


```supercollider
(
x = Signal.fill(512, { rrand(0.0, 1.0) });
y = Signal.fill(512, { |i| (i * pi / 64).sin });
[x, y, (x + y) * 0.5, x * y, min(x, y), max(x, y)].flop.flat
    .plot(numChannels: 6);
)
```




### `thresh`
Thresholding replaces every value < threshold with 0.
> **Note:** Before SuperCollider 3.13 this function was implemented incorrectly, evaluating the square of provided threshold. This behavior is now fixed, but note that older code might give different results.


### `+`, `-`, `*`, `/`, `div`, `pow`, `mod`, `min`, `max`, `ring1`, `ring2`, `ring3`, `ring4`, `difsqr`, `sumsqr`, `sqrdif`, `absdif`, `amclip`, `scaleneg`, `clip2`, `wrap2`, `excess`

### `%`, `**`

### `<!`



