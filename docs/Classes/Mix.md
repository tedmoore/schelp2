# Mix

*Sum an array of channels.*

**Categories:** UGens>Multichannel

## Description

Mix will mix an array of channels down to a single channel or an array of arrays of channels down to a single array of channels. More information can be found under [Multichannel-Expansion](../Guides/Multichannel-Expansion.md).

> **Note:** Note that `Mix.ar` and `Mix.kr` in SC2 are equivalent to `Mix.new` in SC3, and that `Mix.arFill` and `Mix.krFill` are equivalent to `Mix.fill`.




## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `array` | The array of channels or arrays. |  

### `fill`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `n` | The size of array to create. |  
| `function` | The array filling function. |  
**Returns:** Returns: A newly created [UGen](../Classes/UGen.md) .
## Examples


```supercollider
s.boot;

{ Mix.new([PinkNoise.ar(0.1), FSinOsc.ar(801, 0.1), LFSaw.ar(40, 0.1)]) }.play

(
play({
    Mix.new(Array.fill(8, { SinOsc.ar(500 + 500.0.rand, 0, 0.05) }));
}))

(
play({
    Mix.fill(8, { SinOsc.ar(500 + 500.0.rand, 0, 0.05) });
}))
```




