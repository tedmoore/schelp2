# FFT Overview

*Overview of the Fast Fourier Transform (FFT) UGens*

**Categories:** UGens>FFT

**Related:** [FFT](../Classes/FFT.md), [IFFT](../Classes/IFFT.md)


## FFT and IFFT
SuperCollider implements a number of UGens supporting Fast Fourier Transform (FFT) based processing. The most basic of these are FFT and IFFT (inverse-FFT) which convert data between the time and frequency domains:


```supercollider
chain = FFT(buffer, input)
```





```supercollider
output = IFFT(chain)
```


FFT requires a [Buffer](../Classes/Buffer.md) or [LocalBuf](../Classes/LocalBuf.md). The buffer's size must correspond to a power of 2, and must also be a multiple of the server's current [block size](../Classes/ServerOptions.md#-blocksize). The window size is equivalent to the buffer size, and the window [overlap defaults to 2 (hop = 0.5)](../Classes/FFT.md#*new). Both [FFT](../Classes/FFT.md) and [IFFT](../Classes/IFFT.md) use a sine window by default. Their combination efficiently becomes a Hanning window (i.e. raised sine, that is, sine squared).



## How FFT UGens communicate
[FFT](../Classes/FFT.md) stores spectral data in the buffer, in the following format:

| DC | nyquist | real 1f | imag 1f | real 2f | imag 2f | ... | real (N-1)f | imag (N-1)f | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
where `f` is the frequency corresponding to the window size, and `N` is the window size / 2.

The `FFT` UGen returns a signal (usually called **chain**) is constant at `-1`, only when a new FFT window starts, the signal equals the buffer number. This is how subsequent FFT UGens can write to that buffer and know when to do this. The FFT information is not in the chain signal, but in the buffer.


```supercollider
// the FFT return signal is -1, and for each starting window,
// it is the FFT buffer number

b = Buffer.alloc(s, 512); // allocate FFT buffer
b.bufnum; // note the buffer number

(
var dt = s.options.blockSize / s.sampleRate * 16; // plot 16 blocks
var min = -2, max = b.bufnum + 4;
// input is SoundIn, but we don't see this signal
{ FFT(b, SoundIn.ar) }.plot(dt, minval:min, maxval:max).plotMode_(\steps);
)

b.free; // free the buffer again
```




## Phase Vocoder UGens and Spectral Processing
In between an FFT and an IFFT one can chain together a number of Phase Vocoder UGens (i.e. `PV_...`) to manipulate blocks of spectral data before reconversion. The process of buffering the appropriate amount of audio, windowing, conversion, overlap-add, etc. is handled automatically.

See [#PV and FFT UGens in the Standard Library](#pv-and-fft-ugens-in-the-standard-library) for a list of UGens.


```supercollider
(
{
  var in, chain;
    in = WhiteNoise.ar(0.8);
    chain = FFT(LocalBuf(2048), in); // encode to frequency domain
    chain = PV_RandComb(chain, 0.95, Impulse.kr(0.4)); // process
    IFFT(chain) // decode to time domain
}.play;
)
```


In order to expand PV UGens for a multichannel input signal, an appropriate array of buffers must be provided (not a multichannel buffer):


```supercollider
(
{
  var in, chain;
    in = Ringz.ar(Impulse.ar([2, 3]), [700, 800], 0.1) * 5; // stereo input
    chain = FFT({ LocalBuf(2048) } ! 2, in); // array of two local buffers
    chain = PV_RandComb(chain, 0.95, Impulse.kr(0.4));
    IFFT(chain) // returns a stereo out
}.play;
)
```


For more examples, see [#Multichannel Expansion with FFT UGens](#multichannel-expansion-with-fft-ugens)


### Parallel FFT chains
PV UGens write their output data *in place*, i.e. back into the same buffer from which they read. PV UGens which require two buffers write their data into the first buffer, usually called 'bufferA'.


```supercollider
(
{
  var inA, chainA, inB, chainB, chain;
    inA = LFSaw.ar(MouseY.kr(100, 1000, 1), 0, 0.2);
    inB = Ringz.ar(Impulse.ar(MouseX.kr(1, 100, 1)), 700, 0.5);
    // make two parallel chains
    chainA = FFT(LocalBuf(2048), inA);
    chainB = FFT(LocalBuf(2048), inB);
    chain = PV_MagMul(chainA, chainB); // writes into bufferA
    IFFT(chain) * 0.1
}.play;
)

d.free;
```


A similar example using a soundfile:


```supercollider
// read the soundfile into a buffer
d = Buffer.read(s, ExampleFiles.child);

(
{
  var inA, chainA, inB, chainB, chain;
    inA = LFSaw.ar(100, 0, 0.2);
    inB = PlayBuf.ar(1, d, BufRateScale.kr(d), loop: 1);
    chainA = FFT(LocalBuf(2048), inA);
    chainB = FFT(LocalBuf(2048), inB);
    chain = PV_MagMul(chainA, chainB); // writes into bufferA
    IFFT(chain) * 0.1
}.play;
)

d.free;
```





### Copying FFT chains
Because each PV UGen overwrites the output of the previous one, it is necessary to copy the data to an additional buffer at the desired point in the chain in order to do parallel processing of input without using multiple FFT UGens. [PV_Copy](../Classes/PV_Copy.md) allows for this.


> **Note:** As of SC 3.7 instances of PV_Copy are added automatically where necessary for parallel processing. Existing code explicitly using PV_Copy should continue to work.



```supercollider
(
{
    var in, in2, chainA, chainB, chainC;
    var mod = LFNoise2.kr(2);
    in = Blip.ar(mod.exprange(4000, 2), 231);
    in2 = SinOsc.ar(mod.exprange(200, 4000));
    chainA = FFT(LocalBuf(2048), in);
    chainB = FFT(LocalBuf(2048), in2);
    chainC = PV_Copy(chainA, LocalBuf(2048));
    chainB = PV_MagMul(chainB, chainC);
    XFade2.ar(
        IFFT(chainA) * 0.4,
        IFFT(chainB) * 0.1,
        MouseX.kr(-1, 1)
    );
}.play
)
```


PV processes can also share a single FFT UGen to process a signal in parallel. In the following example, 'chain0' and 'chain1' share the same FFT UGen. SuperCollider automatically copies the FFT data from 'chain' into hidden LocalBufs inside the Synth. In the following example, if the [PV_PhaseShift](../Classes/PV_PhaseShift.md) UGen were operating directly on `chainA`, then the two [IFFT](../Classes/IFFT.md) units would produce the same signal, which, when added together, would reinforce each other. Instead, the sound is nearly silent -- proving that `chainB` is in a different buffer, even though the function does not explicitly create it.


```supercollider
(
x = { var inA, chainA, chainB;
    inA = LFClipNoise.ar(100);
    chainA = FFT(LocalBuf(2048, 1), inA);
    chainB = PV_PhaseShift(chainA, pi);
    // half-circle phase shift should result in an inverse signal
    // in practice, ultra-low frequencies sneak through
    // but you won't hear very much here
    IFFT(chainA) + IFFT(chainB);
}.play;
)
```





### Plotting magnitudes
Note that PV UGens convert as needed between cartesian (complex) and polar representations, therefore when using multiple PV UGens it may be impossible to know in which form the values will be at any given time. FFT produces complex output (see above). The following, however, returns a reliable magnitude plot:


```supercollider
c = Buffer.alloc(s,2048,1);

(
x = { var in, chain, chainB, chainC;
    in = WhiteNoise.ar;
    chain = FFT(c, in);
    0.01 * Pan2.ar(IFFT(chain));
}.play(s);
)

(
Routine({
    3.do{arg i;
        c.getToFloatArray(action: { arg array;
            var z, x;
            z = array.clump(2).flop;
            // Initially data is in complex form
            z = [Signal.newFrom(z[0]), Signal.newFrom(z[1])];
            x = Complex(z[0], z[1]);

            { x.magnitude.plot('Initial', Rect(200, 600-(200*i), 700, 200)) }.defer
        });
        0.1.wait;
}}).play
)

x.free;
```





### UGen access to FFT data
It is possible to manipulate the FFT data directly within a synth graph (if there doesn't already exist a PV UGen which will do what you want), using the methods pvcalc, pvcalc2, pvcollect. Here's an example which uses the methods [SequenceableCollection#-clump](../Classes/SequenceableCollection.md#-clump) and [SequenceableCollection#-flop](../Classes/SequenceableCollection.md#-flop) to rearrange the order of the spectral bins:


```supercollider
c = Buffer.read(s, ExampleFiles.child);

(
x = {
    var in, numFrames=2048, chain, v;
    in = PlayBuf.ar(1, c, loop: 1);
    chain = FFT(LocalBuf(numFrames), in);

    chain = chain.pvcalc(numFrames, {|mags, phases|
        /* Play with the mags and phases, then return them */
        [mags, phases].flop.clump(2).flop.flatten
    }, tobin: 250);

    0.5 * IFFT(chain).dup
}.play;
)
x.free; c.free;
```






## Multichannel Expansion with FFT UGens
Care must be taken when using multichannel expansion with FFT UGens, as they require separate buffers. Code such as this can be deceptive:


```supercollider
chain = FFT(bufnum, { WhiteNoise.ar(0.2) }.dup);
```


The above may seem to work, but does not. It does result in two FFT UGens, but as they both write to the same buffer, the second simply overwrites the data from the first, thus wasting CPU and accomplishing nothing.

When using multichannel expansion with FFT UGens it is necessary to ensure that each one writes to a different buffer. Here's an example of one way to do this:


```supercollider
(
SynthDef("help-multichannel FFT", { |out=0| // bufnum is an array
    var in, chain;
    in = [SinOsc.ar(200, 0, 0.2), WhiteNoise.ar(0.2)];
    chain = FFT(LocalBuf([2048, 2048]), in); // each FFT has a different buffer
    // now we can multichannel expand as normal
    chain = PV_BrickWall(chain, SinOsc.kr(-0.1));

    Out.ar(out, IFFT(chain));
}).play;
)

// or using global buffers

b = { Buffer.alloc(s, 2048, 1) }.dup;

(
SynthDef("help-multichannel FFT", { |out=0, bufnum= #[0, 1]| // bufnum is an array
    var in, chain;
    in = [SinOsc.ar(200, 0, 0.2), WhiteNoise.ar(0.2)];
    chain = FFT(bufnum, in); // each FFT has a different buffer
    // now we can multichannel expand as normal
    chain = PV_BrickWall(chain, SinOsc.kr(-0.1));

    Out.ar(out, IFFT(chain));
}).play(s,[\bufnum, b]);
)

b.free;
```


Note that dup on a UGen just makes a reference to that UGen, because UGen defines -copy to simply return the receiver. (See [UGen](../Classes/UGen.md) for more detail.)


```supercollider
a = SinOsc.ar;
a.dup[1] === a

true
```


Code like `IFFT(chain).dup` is found throughout the PV help files , and is just a convenient way to copy a mono signal to stereo, without further computation.

See also [Multichannel-Expansion](../Guides/Multichannel-Expansion.md).



## PV and FFT UGens in the Standard Library
The following PV UGens are included in the standard SC distribution:


**[FFT](../Classes/FFT.md)**
: Fast Fourier Transform

**[IFFT](../Classes/IFFT.md)**
: Inverse Fast Fourier Transform

**[PV_Add](../Classes/PV_Add.md)**
: complex addition

**[PV_BinScramble](../Classes/PV_BinScramble.md)**
: scramble bins

**[PV_BinShift](../Classes/PV_BinShift.md)**
: shift and stretch bin position

**[PV_BinWipe](../Classes/PV_BinWipe.md)**
: combine low and high bins from two inputs

**[PV_BrickWall](../Classes/PV_BrickWall.md)**
: zero bins

**[PV_ConformalMap](../Classes/PV_ConformalMap.md)**
: complex plane attack

**[PV_CopyPhase](../Classes/PV_CopyPhase.md)**
: copy magnitudes and phases

**[PV_Diffuser](../Classes/PV_Diffuser.md)**
: random phase shifting

**[PV_HainsworthFoote](../Classes/PV_HainsworthFoote.md)**
: onset detection

**[PV_JensenAndersen](../Classes/PV_JensenAndersen.md)**
: onset detection

**[PV_LocalMax](../Classes/PV_LocalMax.md)**
: pass bins which are a local maximum

**[PV_MagAbove](../Classes/PV_MagAbove.md)**
: pass bins above a threshold

**[PV_MagBelow](../Classes/PV_MagBelow.md)**
: pass bins below a threshold

**[PV_MagClip](../Classes/PV_MagClip.md)**
: clip bins to a threshold

**[PV_MagFreeze](../Classes/PV_MagFreeze.md)**
: freeze magnitudes

**[PV_MagMul](../Classes/PV_MagMul.md)**
: multiply magnitudes

**[PV_MagDiv](../Classes/PV_MagDiv.md)**
: division of magnitudes

**[PV_MagNoise](../Classes/PV_MagNoise.md)**
: multiply magnitudes by noise

**[PV_MagShift](../Classes/PV_MagShift.md)**
: shift and stretch magnitude bin position

**[PV_MagSmear](../Classes/PV_MagSmear.md)**
: average magnitudes across bins

**[PV_MagSquared](../Classes/PV_MagSquared.md)**
: square magnitudes

**[PV_Max](../Classes/PV_Max.md)**
: maximum magnitude

**[PV_Min](../Classes/PV_Min.md)**
: minimum magnitude

**[PV_Mul](../Classes/PV_Mul.md)**
: complex multiply

**[PV_PhaseShift](../Classes/PV_PhaseShift.md)**
: shift phase of all bins

**[PV_PhaseShift270](../Classes/PV_PhaseShift270.md)**
: shift phase by 270 degrees

**[PV_PhaseShift90](../Classes/PV_PhaseShift90.md)**
: shift phase by 90 degrees

**[PV_RandComb](../Classes/PV_RandComb.md)**
: pass random bins

**[PV_RandWipe](../Classes/PV_RandWipe.md)**
: crossfade in random bin order

**[PV_RectComb](../Classes/PV_RectComb.md)**
: make gaps in spectrum

**[PV_RectComb2](../Classes/PV_RectComb2.md)**
: make gaps in spectrum

**[UnpackFFT](../Classes/UnpackFFT.md), [PackFFT](../Classes/PackFFT.md), [Unpack1FFT](../Classes/Unpack1FFT.md)**
: "unpacking" components used in pvcalc, pvcalc2, pvcollect (can also be used on their own)



For a full list of FFT UGens, see **UGens>FFT** in the [Browse#UGens>FFT](../Browse.md#ugens>fft) page.



