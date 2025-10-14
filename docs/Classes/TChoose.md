# TChoose

*Randomly select one of several inputs*

**Categories:** UGens>Triggers, UGens>Random

**Related:** [TWChoose](../Classes/TWChoose.md)

## Description

An output is selected randomly on receiving a trigger from an array of inputs.
TChoose returns a combination of [Select](../Classes/Select.md) and [TIRand](../Classes/TIRand.md).


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `trig` |  |  
| `array` |  |  

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
    TChoose.ar(Dust.ar(MouseX.kr(1, 1000, 1)), a) * 0.2

}.play;
)
```



> **Note:** all the ugens are continuously running. This may not be the most efficient way if each input is cpu-expensive.




