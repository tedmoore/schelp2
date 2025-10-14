# InterplEnv

*envelope specification*

**Related:** [IEnvGen](../Classes/IEnvGen.md), [Env](../Classes/Env.md)

**Categories:** Control, Envelopes


> **Note:** Env fully supports all functionality of InterplEnv, InterplXYC, InterplPairs and InterplChord. These are now deprecated and will be removed in the future.


## Description

An InterplEnv is a specification for a segmented envelope. InterplEnvs can be used both server-side, by an [IEnvGen](../Classes/IEnvGen.md) within a SynthDef, and clientside, with methods such as at. An InterplEnv can have any number of segments. An InterplEnv can have several shapes for its segments.

### Differences between InterplEnv and Env
InterplEnvs do not have release or loop nodes. They are of a fixed duration. Mostly, it is meant to be used with IEnvGen, where 'times' are actually an **index into the envelope** shape.




## Class Methods



## Instance Methods



