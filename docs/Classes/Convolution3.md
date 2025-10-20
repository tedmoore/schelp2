# Convolution3

*Time based convolver.*

**Related:** [Convolution](../Classes/Convolution.md), [Convolution2](../Classes/Convolution2.md), [Convolution2L](../Classes/Convolution2L.md)

**Categories:** UGens>Convolution

## Description

Strict convolution with fixed kernel which can be updated using a trigger signal. The convolution is performed in the time domain.

> **Note:** Doing convolution in time domain is highly inefficient, and probably only useful for either very short kernel sizes, or for control rate signals. See [Convolution2](../Classes/Convolution2.md) and [Convolution2L](../Classes/Convolution2L.md) for more efficient convolution UGens.




## Class Methods



### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | processing target |  
| `kernel` | buffer index for the fixed kernel, may be modulated in combination with the trigger |  
| `trigger` | update the kernel on a change from <=0 to >0 |  
| `framesize` | maximum size of the buffer containing the kernel |  
| `mul` |  |  
| `add` |  |  


