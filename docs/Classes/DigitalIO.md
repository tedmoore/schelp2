# DigitalIO

*Read or write data to a digital pin*

**Related:** [AnalogIn](../Classes/AnalogIn.md), [AnalogOut](../Classes/AnalogOut.md), [DigitalIn](../Classes/DigitalIn.md), [DigitalOut](../Classes/DigitalOut.md)

**Categories:** UGens>Bela

## Description

Reads or writes digital data from or to a digital pin. The pin number of this UGen can be modulated, as well as its I/O mode, which allows to tri-state the pin.

> **Note:** This UGen only works on Bela.



> **Note:** If you do not need to change the pin mode or the pin, you should use the UGen [DigitalIn](../Classes/DigitalIn.md) or [DigitalOut](../Classes/DigitalOut.md)




## Class Methods

### `ar`
The output of this UGen is always the last value read when the digital pin was an input.**Arguments:**

| Argument | Description |
|----------|-------------|
| `digitalPin` | Digital pin number to write to. Pin numbers begin at 0. This value can be modulated at audiorate. |  
| `output` | Value to write out to the pin - the value will be 1 when the argument is larger than 0, otherwise 0. This value can be modulated at audio rate. |  
| `pinMode` | Value to write out to the pin - the pin will be an input when the argument is smaller than 0.5, otherwise an output. This value can be modulated at audiorate. |  
| `mul` |  |  
| `add` |  |  

### `kr`
The output of this UGen is always the last value read when the digital pin was an input.**Arguments:**

| Argument | Description |
|----------|-------------|
| `digitalPin` | Digital pin number to write to. Pin numbers begin at 0. |  
| `output` | Value to write out to the pin - the value will be 1 when the argument is larger than 0, otherwise 0. |  
| `pinMode` | Value to write out to the pin - the pin will be an input when the argument is smaller than 0.5, otherwise an output. |  
| `mul` |  |  
| `add` |  |  

## Examples


```supercollider
// write a sine oscillator's output to a pin, and read the pin value at other times

(
SynthDef("help-DigitalIO", { |out = 0|
    DigitalIO.ar(0, SinOsc.ar(10), LFPulse.kr(0.1)).poll;
}).play;
)
```




