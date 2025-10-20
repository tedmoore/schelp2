# ControlRate

*Server control rate.*

**Related:** [RadiansPerSample](../Classes/RadiansPerSample.md), [SampleDur](../Classes/SampleDur.md), [SampleRate](../Classes/SampleRate.md), [SubsampleOffset](../Classes/SubsampleOffset.md)

**Categories:** UGens>Info

## Description

Get the current control rate of the server.


## Class Methods


### `ir`
**Returns:** The current control rate of the server.equivalent to 1 / [ControlDur](../Classes/ControlDur.md)
## Examples


```
{ ControlRate.ir.poll }.play;
```


compare ControlRate (.kr) and [SampleRate](../Classes/SampleRate.md) (.ar)

```
( 
{
    var freq = 400;
    
    // pulses at control rate:
    (LFPulse.ar(ControlRate.ir, 0, 0.01, 2, -1) * [1, 0, 0, 0]) 
    
    // Sinewave at control rate:
    + (SinOsc.kr(freq) * [0, 1, 0, 0])
    
    // pulses at sample rate:
    + (LFPulse.ar(SampleRate.ir/2, 0, 0.1, 2, -1) * [0, 0, 1, 0]) 
    
    // Sinewave at sample rate:
    + (SinOsc.ar(freq) * [0, 0, 0, 1])
    
}.plot(0.01);
)
```


listen to difference:

```
(
{
    K2A.ar(SinOsc.kr(400, mul: [1, 0]))
         +  SinOsc.ar(400, mul: [0, 1])
}.scope
)
```


More about difference between .kr (control rate) and .ar (audio rate) can be found in [Mark_Polishook_tutorial/08_Rates](../Tutorials/Mark_Polishook_tutorial/08_Rates.md)
play a sine tone at control rate

```
{ SinOsc.ar(ControlRate.ir) * 0.1 }.play;
```




