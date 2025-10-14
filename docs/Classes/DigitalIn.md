# DigitalIn

*Read data from a digital input*

**Related:** [AnalogIn](../Classes/AnalogIn.md), [AnalogOut](../Classes/AnalogOut.md), [DigitalOut](../Classes/DigitalOut.md), [DigitalIO](../Classes/DigitalIO.md)

**Categories:** UGens>Bela

## Description

Reads digital data from a digital sensor input (e.g.: a button or trigger input).

> **Note:** This UGen only works on Bela.



> **Note:** If you want to modulate the pin number, you should use the UGen [DigitalIO](../Classes/DigitalIO.md)




## Class Methods

### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `digitalPin` | Digital pin number to read. Pin numbers begin at 0. This value cannot be modulated. |  
| `mul` |  |  
| `add` |  |  

### `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `digitalPin` | Digital pin number to read. Pin numbers begin at 0. This value cannot be modulated. |  
| `mul` |  |  
| `add` |  |  

## Examples


```supercollider
// turn on and off a sine oscillator

(
SynthDef("help-DigitalIn", { |out = 0|
    Out.ar(out,
      SinOsc.ar(500, 0, 0.1 * DigitalIn.ar(0))
    )
}).play;
)
```




