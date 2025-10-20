# Unpack1FFT

*Unpack a single value (magnitude or phase) from an FFT chain*

**Categories:** UGens>FFT, UGens>Demand

**Related:** [PackFFT](../Classes/PackFFT.md), [UnpackFFT](../Classes/UnpackFFT.md), [FFT-Overview](../Guides/FFT-Overview.md)

Unpack1FFT(chain, bufsize, binindex, whichmeasure = 0)
## Description

Takes an FFT chain and extracts a single scalar value as a demand-rate stream. To call it, a "demander" is needed, which fires whenever the FFT chain fires - this is normally achieved using [PackFFT](../Classes/PackFFT.md) but can also be done using [Demand](../Classes/Demand.md).

> **Note:** This UGen is commonly not used directly. Its main purpose is as a component in [PV_ChainUGen#-pvcollect](../Classes/PV_ChainUGen.md#-pvcollect), [PV_ChainUGen#-pvcalc](../Classes/PV_ChainUGen.md#-pvcalc), and [PV_ChainUGen#-pvcalc2](../Classes/PV_ChainUGen.md#-pvcalc2) processes. You're welcome to use it on its own - the example below shows how.




## Class Methods



### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `chain` | an FFT chain |  
| `bufsize` | the size of the expected input FFT frames |  
| `binindex` | the integer index of the bin you want to query |  
| `whichmeasure` | 0 for magnitude and 1 for phase. None of these arguments can be modulated. |  

```
// Let's extract the DC component - i.e. the magnitude at binindex zero.
(
{
    var sig, chain, stream, windowStarts, demand;
    var fftsize = 1024;

    sig = SinOsc.ar(LFDNoise3.kr(LFNoise0.kr(1) * 40 + 60) * 700 + 800);

    chain = FFT(LocalBuf(fftsize), sig);
    stream = Unpack1FFT(chain, bufsize: fftsize, binindex: 0, whichmeasure: 0);

    // each time an FFT window starts, the unpacker returns a new value
    windowStarts = chain > -1;
    demand = Demand.kr(windowStarts, 0, stream);
    demand.poll(windowStarts);

    sig * 0.05
}.play
)
```



