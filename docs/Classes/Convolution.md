# Convolution

*Real-time convolver.*

**Related:** [Convolution2](../Classes/Convolution2.md), [Convolution2L](../Classes/Convolution2L.md), [Convolution3](../Classes/Convolution3.md)

**Categories:** UGens>FFT, UGens>Convolution

## Description

Strict convolution of two continuously changing inputs. Also see [Convolution2](../Classes/Convolution2.md) for a cheaper CPU cost alternative for the case of a fixed kernel which can be changed with a trigger message.
See also [http://www.dspguide.com/ch18.htm](http://www.dspguide.com/ch18.htm) by Steven W. Smith.


## Class Methods

### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | Processing target. |  
| `kernel` | Processing kernel. |  
| `framesize` | Size of FFT frame, must be a power of two (512, 1024, 2048, 4096 are standard choices). Convolution uses twice this number internally. Note that the convolution gets progressively more expensive to run for higher powers! The maximum value you can use is 2^16 = 16384. (This upper limit is half of "SC_FFT_MAXSIZE" defined in the SC source code.) Larger convolutions than this can be done using [PartConv](../Classes/PartConv.md). |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```supercollider
(

{
    var input, kernel;

    input = SoundIn.ar(0);
    kernel = Mix.ar(LFSaw.ar([300, 500, 800, 1000] * MouseX.kr(1.0, 2.0), 0, 1.0));

    // must have power of two framesize
    Convolution.ar(input, kernel, 1024, 0.5)
}.play;

)

(
// must have power of two framesize- FFT size will be sorted by Convolution to be double this
// maximum is currently a = 8192 for FFT of size 16384

a = 2048;
s = Server.local;

// kernel buffer
g = Buffer.alloc(s, a, 1);
)

(

// random impulse response

g.set(0, 1.0);

100.do({ |i| g.set(a.rand, 1.0.rand) });


{
    var input, kernel;

    input = SoundIn.ar(0);
    kernel = PlayBuf.ar(1, g.bufnum, BufRateScale.kr(g.bufnum), 1, 0, 1);

    Convolution.ar(input, kernel, 2 * a, 0.5)
}.play;

)
```




