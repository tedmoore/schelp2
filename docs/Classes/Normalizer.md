# Normalizer

*Flattens dynamics.*

**Related:** [Amplitude](../Classes/Amplitude.md), [Compander](../Classes/Compander.md), [CompanderD](../Classes/CompanderD.md), [Limiter](../Classes/Limiter.md)

**Categories:** UGens>Dynamics

## Description

Normalizes the input amplitude to the given level. Normalizer will not overshoot like [Compander](../Classes/Compander.md) will, but it needs to look ahead in the audio. Thus there is a delay equal to twice the value of the `dur` parameter.


## Class Methods


### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The signal to be processed. |  
| `level` | The peak output amplitude level to which to normalize the input. |  
| `dur` | Also called lookAheadTime. The buffer delay time. Shorter times will produce smaller delays and quicker transient response times, but may introduce amplitude modulation artifacts. This parameter cannot be modulated. |  

## Examples


```
(
// example signal to process
{
    var z;
    z = Decay2.ar(
        Impulse.ar(8, LFSaw.kr(0.25, -0.6, 0.7)),
        0.001, 0.3, FSinOsc.ar(500));
    z * 0.8
}.play
)

(
{
    var z;
    z = Decay2.ar(
        Impulse.ar(8, LFSaw.kr(0.25, -0.6, 0.7)),
        0.001, 0.3, FSinOsc.ar(500));
    [z, Normalizer.ar(z, 0.4, 0.01)] * 0.5
}.play
)
```




