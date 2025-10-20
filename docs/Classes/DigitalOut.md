# DigitalOut

*Write data to a digital output*

**Related:** [AnalogIn](../Classes/AnalogIn.md), [AnalogOut](../Classes/AnalogOut.md), [DigitalIn](../Classes/DigitalIn.md), [DigitalIO](../Classes/DigitalIO.md)

**Categories:** UGens>Bela

## Description

Writes digital data to a digital output (e.g.: an LED or a trigger/gate output).

> **Note:** This UGen only works on Bela.



> **Note:** If you want to modulate the pin number, you should use the UGen [DigitalIO](../Classes/DigitalIO.md)




## Class Methods


### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `digitalPin` | Digital pin number to write to. Pin numbers begin at 0. This value cannot be modulated. |  
| `output` | Value to write out to the pin - the value will be 1 when the argument is larger than 0, otherwise 0. |  
| `mul` |  |  
| `add` |  |  


### `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `digitalPin` | Digital pin number to write to. Pin numbers begin at 0. This value cannot be modulated. |  
| `output` | Value to write out to the pin - the value will be 1 when the argument is larger than 0, otherwise 0. |  
| `mul` |  |  
| `add` |  |  

## Examples


```
// write a sine oscillator's output to a pin

(
SynthDef("help-DigitalOut", { |out = 0|
    DigitalOut.ar(0, SinOsc.ar(10));
}).play;
)
```




