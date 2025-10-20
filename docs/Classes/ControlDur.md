# ControlDur

*Duration of one block*

**Categories:** UGens>Info

**Related:** [ControlRate](../Classes/ControlRate.md)

## Description

Returns the current block duration of the server in seconds. Equivalent to 1 / [ControlRate](../Classes/ControlRate.md).


## Class Methods


### `ir`

## Examples


```
{ ControlDur.ir.poll }.play;

{ (1/ControlDur.ir).poll }.play;

{ ControlRate.ir.poll }.play;
```




