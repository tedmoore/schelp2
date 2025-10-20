# BelaScopeOut

*Bela's Oscilloscope interface*

**Categories:** UGens>Bela

## Description


> **Note:** This UGen only works on Bela


This UGen effectively sends audio signals to Bela Oscilloscope, analogously to how [/Out](..//Classes/Out.md) writes to a bus. It can be used directly, or through [UGen#-belaScope](../Classes/UGen.md#-belascope), [Array#-belaScope](../Classes/Array.md#-belascope), [Bus#-belaScope](../Classes/Bus.md#-belascope), [Function#-belaScope](../Classes/Function.md#-belascope) and [Server#-belaScope](../Classes/Server.md#-belascope) convenience functions.


## Class Methods


### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `offset` | The Bela Oscilloscope's channel where to start writing. This is read only at construction time and thus it's not modulatable. |  
| `channelsArray` | An array of UGens to be scoped. |  


