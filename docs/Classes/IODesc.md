# IODesc

*Description of SynthDesc input or output*

**Categories:** Server>Nodes

**Related:** [SynthDesc](../Classes/SynthDesc.md)

## Description

IODesc describes an input or output of a SynthDesc, as returned by [SynthDesc#-outputs](../Classes/SynthDesc.md#-outputs) and [SynthDesc#-inputs](../Classes/SynthDesc.md#-inputs)


## Class Methods



## Instance Methods


### `rate`
A [Symbol](../Classes/Symbol.md) for the rate.
### `numberOfChannels`
The number of channels.
### `startingChannel`
This can either be a [String](../Classes/String.md), a [Float](../Classes/Float.md) or an [UGen](../Classes/UGen.md).| String | The name of the control that provides the bus index | 
| --- | --- || Float | A hard-coded bus index | | UGen | The UGen providing the bus index | 
### `type`
The class of the input/output ugen, like [In](../Classes/In.md), [Out](../Classes/Out.md), [ReplaceOut](../Classes/ReplaceOut.md), etc.

