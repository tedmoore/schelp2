# PureUGen

*Pure UGen*

**Categories:** UGens

**Related:** [UGen](../Classes/UGen.md)

## Description

A Pure UGen is a UGen, which does not access any shared resources like busses, buffers or random number generators. UGen classes which are derived from PureUGen are candidates for common subexpression elimination and dead code elimination passes during the SynthDef compilation.


## Instance Methods



