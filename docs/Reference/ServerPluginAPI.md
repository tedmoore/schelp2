# Server Plugin API

*Reference for writing unit generators*

**Categories:** Internals

**Related:** [WritingUGens](../Guides/WritingUGens.md)


## Input rates
These four constants identify the calculation rates of inputs in SuperCollider.


**`calc_ScalarRate`**
: Initial rate. Conventionally known in the language as ".ir".

**`calc_BufRate`**
: Control rate. Conventionally known in the language as ".kr".

**`calc_FullRate`**
: Audio rate. Conventionally known in the language as ".ar".

**`calc_DemandRate`**
: Demand rate.





## UGen basics
These helper macros assume that there is a ugen object called `unit` in the local scope.


**`IN(index)`**
: A single block of audio-rate input as a float* at the given index. Index 0 is the first input to the ugen, index 1 the second input, and so forth.

**`IN0(index)`**
: A single sample of control-rate input as a float, at the given index.

**`OUT(index)`**
: A single block of audio-rate output as a float* at the given index.

**`OUT0(index)`**
: A single sample of control-rate input as a float, at the given index.

**`INRATE(index)`**
: Get the rate of a given input index. This will be one of the four rates.

**`INBUFLENGTH(index)`**
: Get the block size of a given input index.

**`SAMPLERATE`**
: Sample rate of the server in Hertz.

**`SAMPLEDUR`**
: Sample period of the server in seconds.

**`BUFLENGTH`**
: Length in samples of an audio buffer (that is, the number of samples in a control period).

**`BUFRATE`**
: Control rate of the server in Hertz.

**`BUFDUR`**
: Control period of the server in seconds.

**`FULLRATE`**
: 

**`FULLBUFLENGTH`**
: 





## Buffers

**`GET_BUF`**
: The recommended way to retrieve a buffer. Take the first input of this UGen and use it as a buffer number. This dumps a number of variables into the local scope:- `buf` - a pointer to the `SndBuf` instance
- `bufData` - the raw float data from the buffer
- `bufChannels` - the number of channels in the buffer
- `bufSamples` - the number of samples in the buffer
- `bufFrames` - the number of frames in the buffer
The buffer is locked using the `LOCK_SNDBUF` macro. Buffer lock operations are specific to supernova, and don't do anything in vanilla scsynth.

**`GET_BUF_SHARED`**
: Like `GET_BUF`, but the buffer is locked using `LOCK_SNDBUF_SHARED`.

**`SIMPLE_GET_BUF`**
: Like `GET_BUF`, but only creates the `buf` variable and does not lock the buffer.

**`SIMPLE_GET_BUF_EXCLUSIVE`**
: Like `SIMPLE_GET_BUF`, but locks the buffer with `LOCK_SNDBUF`.

**`SIMPLE_GET_BUF_SHARED`**
: Like `SIMPLE_GET_BUF`, but locks the buffer with `LOCK_SNDBUF_SHARED`.



The following macros are for use in supernova. They still exist in scsynth, but will have no effect.


```
ACQUIRE_BUS_AUDIO(index)
ACQUIRE_BUS_AUDIO_SHARED(index)
RELEASE_BUS_AUDIO(index)
RELEASE_BUS_AUDIO_SHARED(index)
LOCK_SNDBUF(buf)
LOCK_SNDBUF_SHARED(buf)
LOCK_SNDBUF2(buf1, buf2)
LOCK_SNDBUF2_SHARED(buf1, buf2)
LOCK_SNDBUF2_EXCLUSIVE_SHARED(buf1, buf2)
LOCK_SNDBUF2_SHARED_EXCLUSIVE(buf1, buf2)
ACQUIRE_SNDBUF(buf)
ACQUIRE_SNDBUF_SHARED(buf)
RELEASE_SNDBUF(buf)
RELEASE_SNDBUF_SHARED(buf)
ACQUIRE_BUS_CONTROL(index)
RELEASE_BUS_CONTROL(index)
```




## RGen
RGen is a pseudorandom number generator API. Most ugen developers are not interested in seeding their own RGens and would prefer to draw from a global RGen instance supplied by SuperCollider. This can be retrieved with the code:


```
RGen& rgen = *unit->mParent->mRGen;
```



**`uint32 RGen::trand()`**
: Return a uniformly distributed random 32-bit integer.

**`double RGen::drand()`**
: Return a uniformly distributed random double in [0,1).

**`float RGen::frand()`**
: Random float in [0,1).

**`float RGen::frand0()`**
: Random float in [1,2).

**`float RGen::frand2()`**
: Random float in [-1,1).

**`float RGen::frand8()`**
: Random float in [-0.125,0.125).

**`float RGen::fcoin()`**
: Either -1 or +1.

**`float RGen::flinrand()`**
: Linearly distributed random float in [0,1), with a bias towards the 0 end.

**`float RGen::fbilinrand()`**
: Bilinearly distributed random float in (-1,1), with a bias towards 0.

**`float RGen::fsum3rand()`**
: A crude but fast approximation to a Gaussian distribution. Results are always in the range (-1,1). The variance is 1/6 and the standard deviation is 0.41.> *The formula is `(rand() + rand() + rand() - 1.5) * 2/3`, technically a shifted and stretched order-3 Irwin-Hall distribution.*

**`int32 RGen::irand(int32 scale)`**
: Random int in [0,scale).

**`int32 RGen::irand2(int32 scale)`**
: Random int in [-scale,+scale].

**`int32 RGen::ilinrand(int32 scale)`**
: Linearly distributed random int in [0,scale), with a bias towards the 0 end.

**`int32 RGen::ibilinrand(int32 scale)`**
: Bilinearly distributed random int in (-scale,scale), with a bias towards the 0.

**`double RGen::linrand()`**
: Linearly distributed random double in [0,1), with a bias towards the 0 end.

**`double RGen::bilinrand()`**
: Bilinearly distributed random double in (-1,1), with a bias towards 0.

**`double RGen::exprandrng(double lo, double hi)`**
: Exponentially distributed random double in [lo,hi).

**`double RGen::exprand(double scale)`**
: 

**`double RGen::biexprand(double scale)`**
: 

**`double RGen::exprand(double scale)`**
: 

**`double RGen::sum3rand(double scale)`**
: Double version of `RGen::fsum3rand`.





## Unary operators

**`bool sc_isnan(float/double x)`**
: Checks whether `x` is NaN. This is a legacy function, use `std::isnan` instead.

**`bool sc_isfinite(float/double x)`**
: Checks whether `x` is finite. This is a legacy function, use `std::isfinite` instead.

**`int32 sc_grayCode(int32 x)`**
: Convert binary to Gray code.



The following unary functions are available for both float32 and float64, and are the same as in sclang (minus the "sc_" prefixes):

- `sc_midicps`
- `sc_cpsmidi`
- `sc_midiratio`
- `sc_ratiomidi`
- `sc_octcps`
- `sc_cpsoct`
- `sc_ampdb`
- `sc_dbamp`
- `sc_cubed`
- `sc_sqrt`
- `sc_hanwindow`
- `sc_welwindow`
- `sc_triwindow`
- `sc_rectwindow`
- `sc_scurve`
- `sc_ramp`
- `sc_sign`
- `sc_distort`
- `sc_softclip`
- `sc_ceil`
- `sc_floor`
- `sc_reciprocal`
- `sc_frac`
- `sc_log2` (legacy -- use `std::log2(std::abs(x))`)
- `sc_log10` (legacy -- use `std::log10(std::abs(x))`)
- `sc_trunc` (legacy -- use `std::trunc`)


The following unary functions are available for both float32 and float64, but have no sclang equivalent:


**`zapgremlins(x)`**
: Replaces NaNs, infinities, very large and very small numbers (including denormals) with zero. This is useful in ugen feedback to safeguard from pathological behavior. (Note lack of sc_ prefix.)

**`sc_bitriwindow(x)`**
: Alternative to `sc_triwindow` using absolute value.

**`sc_scurve0(x)`**
: Same as `sc_scurve`, but assumes that `x` is in the interval [0, 1].

**`sc_distortneg(x)`**
: A one-sided distortion function. Same as `distort` for `x > 0`, and the identity function for `x <= 0`.

**`taylorsin(x)`**
: Taylor series approximation of `sin(x)` out to `x**9 / 9!`. (Note lack of sc_ prefix.)

**`sc_lg3interp(x1, a, b, c, d)`**
: Cubic Lagrange interpolator.

**`sc_CalcFeedback(delaytime, decaytime)`**
: Determines the feedback coefficient for a feedback comb filter with the given delay and decay times.

**`sc_wrap1(x)`**
: Wrap `x` around ±1, wrapping only once.

**`sc_fold1(x)`**
: Fold `x` around ±1, folding only once.





## Binary operators

**`sc_wrap(in, lo, hi [, range])`**
: 

**`sc_fold(in, lo, hi [, range [, range2]])`**
: 

**`sc_pow(a, b)`**
: Compute `pow(a, b)`, retaining the sign of `a`.

**`sc_powi(x, unsigned int n)`**
: Compute `x^n`, not necessarily retaining the sign of `x`.

**`sc_hypotx(x, y)`**
: Compute `abs(x) + abs(y) - (min(abs(x), abs(y)) * (sqrt(2) - 1))`, the minimum distance one will have to travel from the origin to (x,y) using only orthogonal and diagonal movements.



The following functions are the same as in sclang (minus the "sc_" prefixes):

- `sc_mod(in, hi)` (floats, doubles, ints)
- `sc_round(x, quant)` (floats, doubles, ints)
- `sc_roundUp(x, quant)` (floats, doubles, ints)
- `sc_trunc(x, quant)` (floats, doubles, ints)
- `sc_gcd(a, b)` (ints, longs, floats)
- `sc_lcm(a, b)` (ints, longs, floats)
- `sc_bitAnd(a, b)` (ints)
- `sc_bitOr(a, b)` (ints)
- `sc_leftShift(a, b)` (ints)
- `sc_rightShift(a, b)` (ints)
- `sc_unsignedRightShift(a, b)` (ints)
- `sc_thresh(a, b)`
- `sc_clip2(a, b)`
- `sc_wrap2(a, b)`
- `sc_fold2(a, b)`
- `sc_excess(a, b)`
- `sc_scaleneg(a, b)`
- `sc_amclip(a, b)`
- `sc_ring1(a, b)`
- `sc_ring2(a, b)`
- `sc_ring3(a, b)`
- `sc_ring4(a, b)`
- `sc_difsqr(a, b)`
- `sc_sumsqr(a, b)`
- `sc_sqrsum(a, b)`
- `sc_sqrdif(a, b)`
- `sc_atan2(a, b)` (legacy -- use `std::atan2`)




## Constants
The following constants are doubles:

- `pi`
- `pi2` = pi/2
- `pi32` = 3pi/2
- `twopi` = 2pi
- `rtwopi` (1/2pi)
- `log001` = log(0.001)
- `log01` = log(0.01)
- `log1` = log(0.1)
- `rlog2` = 1/log(2)
- `sqrt2` = sqrt(2)
- `rsqrt2` = 1/sqrt(2)
- `truncDouble` = 3 * 2^51 (used to truncate precision)


The following constants are floats:

- `pi_f`
- `pi2_f`
- `pi32_f`
- `twopi_f`
- `sqrt2_f`
- `rsqrt2_f`
- `truncFloat` = 3 * 2^22 (used to truncate precision)




## Unroll macros
The macros in this section are legacy features. They are seen in many of SuperCollider's built-in ugens, and are intended to provide more efficient alternatives to the standard `for (int i = 0; i < inNumSamples; i++) { out[i] = in[i] }` loop. These efficiency savings are negligible on modern systems and use of these macros is not recommended, especially since they make debugging difficult.


**`LOOP(length, stmt)`**
: Execute code `stmt`, `length` times.

**`LOOP1(length, stmt)`**
: A faster drop-in alternative to `LOOP`, which assumes that `length > 0` so a branch instruction is saved.

**`LooP(length) stmt`**
: An alternative to LOOP/LOOP1 that is more debugger-friendly. The body of the loop comes after the call to `LooP`.

**`ZIN(index)`**
: Similar to `IN`, but subtracts 1 from the pointer to correct for off-by-one errors when using `LOOP` and `ZXP`.

**`ZOUT(index)`**
: Same as `OUT`, but subtracts 1 from the pointer to correct for off-by-one errors when using `LOOP` and `ZXP`.

**`ZIN0(index)`**
: Alias for `IN0`.

**`ZOUT0(index)`**
: Alias for `OUT0`.

**`ZXP(z)`**
: Pre-increment and dereference `z`.

**`ZX(z)`**
: Dereference `z`.

**`PZ(z)`**
: Pre-increment `z`.

**`ZP(z)`**
: Does nothing.

**`ZOFF`**
: Return 1.







