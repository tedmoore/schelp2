# AnalogIn

*Read data from an analog input*

**Related:** [AnalogOut](../Classes/AnalogOut.md), [DigitalIn](../Classes/DigitalIn.md), [DigitalOut](../Classes/DigitalOut.md), [DigitalIO](../Classes/DigitalIO.md)

**Categories:** UGens>Bela

## Description

Read a DC-coupled analog input connected to a sensor (e.g.: a potentiometer or CV in).

> **Note:** This UGen only works on Bela




## Class Methods

### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `analogPin` | Analog pin number to read. Pin numbers begin at 0. This value can be modulated at audiorate. |  
| `mul` |  |  
| `add` |  |  

### `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `analogPin` | Analog pin number to read. Pin numbers begin at 0. |  
| `mul` |  |  
| `add` |  |  

## Examples


```supercollider
// modulate frequency of a sine oscillator

(
SynthDef("help-AnalogIn", { |out = 0|
    Out.ar(out,
      SinOsc.ar(AnalogIn.ar(0).exprange(200, 5000), 0, 0.1)
    )
}).play;
)
```




