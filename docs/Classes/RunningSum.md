# RunningSum

*Running sum over n frames*

**Categories:** UGens>Analysis, UGens>Maths

## Description

A running sum over a user specified number of samples, useful for running RMS power windowing.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | Input signal |  
| `numsamp` | How many samples to take the running sum over (initialisation time only, not modulatable. default: 40) |  

## Examples


```
// distorts of course - would need scaling
{ RunningSum.ar(SoundIn.ar) }.play

// Running Average over x samples
(
{
    var x = 100;
    RunningSum.ar(LFSaw.ar, x) * (x.reciprocal)
 }.play
)
```



```
// RMS Power
(
{
    var input, numsamp;

    input = LFSaw.ar;
    numsamp = 30;

    (RunningSum.ar(input.squared, numsamp) / numsamp).sqrt
}.play
)
```



```
// shortcut in class
{ RunningSum.rms(SoundIn.ar) }.play
```



```
// play around
(
{
    var input, numsamp, power;
    numsamp = 500;
    input = SoundIn.ar;
    power = MouseX.kr(0.1, 4);

    (RunningSum.ar(input ** power, numsamp)/numsamp) ** (power.reciprocal)
}.play
)
```




