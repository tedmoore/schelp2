# MultiOutUGen

*Superclass for all UGens with multiple outputs*

**Categories:** UGens>Base

**Related:** [OutputProxy](../Classes/OutputProxy.md)

## Description

This is a superclass for all UGens with multiple outputs. MultiOutUGen creates the [OutputProxy](../Classes/OutputProxy.md) ugens needed for the multiple outputs.


## Class Methods



## Instance Methods


### `initOutputs`
Create an array of OutputProxies for the outputs.**Arguments:**

| Argument | Description |
|----------|-------------|
| `numChannels` | Number of outputs. Must be a nonzero, positive integer. This is fixed when the SynthDef is compiled so cannot be assigned to a SynthDef argument. |  
| `rate` | The rate of the [OutputProxy](../Classes/OutputProxy.md). |  


