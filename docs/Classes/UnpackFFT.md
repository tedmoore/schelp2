# UnpackFFT

*Unpack an FFT chain into separate demand-rate FFT bin streams*

**Categories:** UGens>FFT, UGens>Demand

**Related:** [PackFFT](../Classes/PackFFT.md), [Unpack1FFT](../Classes/Unpack1FFT.md)

## Description

Takes an FFT chain and separates the magnitude and phase data into separate demand-rate streams, for arithmetic manipulation etc.
This is technically a demand-rate UGen. The actual "demand" is usually created by PackFFT later on in the graph, which requests the values in order to re-pack the data. This allows for processing to occur in between.
See also [PV_ChainUGen#-pvcollect](../Classes/PV_ChainUGen.md#-pvcollect), [PV_ChainUGen#-pvcalc](../Classes/PV_ChainUGen.md#-pvcalc), and [PV_ChainUGen#-pvcalc2](../Classes/PV_ChainUGen.md#-pvcalc2), which provide convenient ways to process audio in the frequency domain. The help for pvcollect includes notes on efficiency considerations.


## Class Methods



### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `chain` | FFT chain |  
| `bufsize` | FFT buffer size |  
| `frombin` | limiting analysis to the bins of interest |  
| `tobin` | limiting analysis to the bins of interest |  
**Returns:** A list from DC up to Nyquist of `[mag[0], phase[0], mag[1], phase[1], ... mag[nyquist], phase[nyquist]].`Note that you do have to decide your FFT buffer size in advance, since this determines how many values the UGen will output.
```
#magsphases = UnpackFFT(chain, bufsize)
```


## Examples


```
// This one just drags out various the values and posts them - a little bit pointless!
(
{
    var sig, chain, stream, windowStarts, fftSize;
    fftSize = 1024;

    sig = SinOsc.ar(LFDNoise3.kr(LFNoise0.kr(1) * 40 + 60) * 700 + 800);
    chain = FFT(LocalBuf(1, fftSize), sig);

    // a window start is indicated by a signal leaving the -1 bottom line
    windowStarts = chain > -1;

    // Using the frombin & tobin args makes it much more efficient, limiting analysis to the bins of interest
    stream = UnpackFFT(chain, fftSize, frombin: 0, tobin: 4);

    // Demand some data from the unpacker.
    // NOTE: At present, Demand.kr is unable to handle more than 32 inputs,
    // so using frombin & tobin to limit the number of bins is compulsory.

    Demand.kr(windowStarts, 0, stream).collect { |anunp, index|
        var label = if(index.even) { "Magnitude" } { "Phase" };
        label = label + (index / 2).floor;
        anunp.poll(windowStarts, label)
    };

    sig * 0.05
}.play
)

// simple frequency-domain manipulation, square-rooting the magnitudes AND phases.
(
x = {
    var sig, chain, magsphases, b;
    b = LocalBuf(1, 1024);
    sig = SinOsc.ar(LFDNoise3.kr(LFNoise0.kr(1) * 40 + 60) * 700 + 800);
    chain = FFT(b, sig);
    magsphases = UnpackFFT(chain, b.numFrames);
    magsphases = magsphases.collect(_.sqrt);
    chain = PackFFT(chain, b.numFrames, magsphases);
    IFFT(chain) * 0.1
}.play
)
```




