# MultiplexAnalogIn

*Read data from an analog input of the Bela board*

**Related:** [AnalogIn](../Classes/AnalogIn.md), [AnalogOut](../Classes/AnalogOut.md), [DigitalIn](../Classes/DigitalIn.md), [DigitalOut](../Classes/DigitalOut.md), [DigitalIO](../Classes/DigitalIO.md)

**Categories:** UGens>Bela

## Description

Reads analog data from a multiplexed analog input of the Bela board, with the additional Multiplexer board.

> **Note:** This UGen only works on Bela




## Class Methods

### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `analogPin` | Analog pin number to read. Pin numbers begin at 0. This value can be modulated at audiorate. |  
| `muxChannel` | Multiplex channel to read. Pin numbers begin at 0. This value can be modulated at audiorate. |  
| `mul` |  |  
| `add` |  |  

### `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `analogPin` | Analog pin number to read. Pin numbers begin at 0. |  
| `muxChannel` | Multiplex channel to read. Pin numbers begin at 0. |  
| `mul` |  |  
| `add` |  |  

## Examples


```supercollider
// modulate frequency of a sine oscillator

(
SynthDef("help-MultiplexAnalogIn", { |out = 0|
    Out.ar(out,
      SinOsc.ar(MultiplexAnalogIn.ar(0, 1).exprange(200, 5000), 0, 0.1)
    )
}).play;
)
```




