# TWChoose

*Randomly select one of several inputs*

**Categories:** UGens>Triggers, UGens>Random

**Related:** [TChoose](../Classes/TChoose.md)

## Description

An output is selected randomly on receiving a trigger from an array of inputs.
the `weights` of this choice are determined from the weights array.
If `normalize` is set to 1 the weights are continuously normalized (this is an extra overhead) when using fixed values the `normalizeSum` method can be used to normalize the values.
TWChoose is a composite of [TWindex](../Classes/TWindex.md) and [Select](../Classes/Select.md).


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `trig` |  |  
| `array` |  |  
| `weights` |  |  
| `normalize` |  |  

## Examples


```supercollider
(
{
    var a;
    a = [
            SinOsc.ar,
            Saw.ar,
            Pulse.ar
        ];
    TWChoose.ar(Dust.ar(MouseX.kr(1, 1000, 1)), a, [0.99, 0.05, 0.05].normalizeSum) * 0.2

}.play;
)
```



> **Note:** all the ugens are continuously running. This may not be the most efficient way if each input is cpu-expensive.




