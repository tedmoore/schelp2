# NumChannels

*Ensures the number of output channels*

**Categories:** UGens>Multichannel

## Description

Ensures the output has the stated number of channels, regardless of the number of input channels.


## Class Methods

### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `input` | the audio signal |  
| `numChannels` | an integer |  
| `mixdown` | true/false, whether you want to mixdown or just use the first channel |  
Mono input is copied. Multi-channels clumped and if `mixdown` is true mixed down, else the first channel used.
## Examples


```supercollider
(
{
    NumChannels.ar(
        SinOsc.ar(100, 0, 0.2), // 1 becomes 2
        2)
}.play
)

(
{
    NumChannels.ar(
        SinOsc.ar([100, 200, 300], 0, 0.2), // 3 becomes 2
        2)
}.play
)

(
{
    NumChannels.ar(
        SinOsc.ar([100, 200, 300, 100], 0, 0.2), // 4 becomes 2

        2)
}.play
)
```




