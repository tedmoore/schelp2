# DelTapRd

**Categories:** UGens>Buffer, UGens>Delays

*Tap a delay line from a DelTapWr UGen*

**Related:** [DelTapWr](../Classes/DelTapWr.md)

## Description

Tap a delay line from a [DelTapWr](../Classes/DelTapWr.md) UGen.

> **Note:** If you run a `DelTapRd.ar` and a `DelTapWr.ar` in tandem, keep in mind that they read and write in blocks equal to the server's block size. If the delay time is greater than the buffer size minus a block, the write and read heads might interfere in unintended ways. Use a slightly larger buffer if this happens.




## Class Methods



### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `buffer` | buffer where DelTapWr has written signal. Max delay time is based on buffer size. |  
| `phase` | the current phase of the DelTapWr UGen. This is the output of DelTapWr. |  
| `delTime` | A delay time in seconds. |  
| `interp` | the kind of interpolation to be used. 1 is none, 2 is linear, 4 is cubic. (The numbers one, two, and *four* correspond to the number of consecutive samples needed to compute each type of interpolation.) Any other values for this argument will silently default to no interpolation. |  
| `mul` |  |  
| `add` |  |  

## Examples

See [DelTapWr#examples](../Classes/DelTapWr.md#examples) for examples.

