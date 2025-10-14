# AnalogOut

*Write data to an analog output*

**Related:** [AnalogIn](../Classes/AnalogIn.md), [DigitalIn](../Classes/DigitalIn.md), [DigitalOut](../Classes/DigitalOut.md), [DigitalIO](../Classes/DigitalIO.md)

**Categories:** UGens>Bela

## Description

Writes an output to a DC-coupled analog output (e.g.: CV out).

> **Note:** This UGen only works on Bela




## Class Methods

### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `analogPin` | Analog pin number to read. Pin numbers begin at 0. This value can be modulated at audiorate. |  
| `output` | Value to write out to the pin. |  
| `mul` |  |  
| `add` |  |  

### `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `analogPin` | Analog pin number to read. Pin numbers begin at 0. |  
| `output` | Value to write out to the pin. |  
| `mul` |  |  
| `add` |  |  

## Examples


```supercollider
// write a sine oscillator's output to a pin

(
SynthDef("help-AnalogOut", { |out = 0|
    AnalogOut.ar(0, SinOsc.ar(10));
}).play;
)
```




