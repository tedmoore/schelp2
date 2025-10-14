# Synth Definition File Format

*Description of Synth Definition file format used by SC synth server*

**Categories:** Server>Architecture

**Related:** [SynthDef](../Classes/SynthDef.md)

Synth definition files are read by the synth server and define collections of unit generators and their connections. These files are currently written by the SuperCollider language application, but theoretically could be written by any program. Such a program would need knowledge of the SC unit generators and their characteristics, such as number of inputs and outputs and available calculation rates. The code to write these files is open and available in the SuperCollider language app.
In the current SuperCollider 3.6 development version, there are two versions of SynthDef:
- **SynthDef** - The original SynthDef file format, backward compatible with .scsyndef files saved using earlier versions of SuperCollider.
- **SynthDef2** - A revised version that extends SynthDef's capacity.

This document describes SynthDef2's format. See [#Original SynthDef format](#original-synthdef-format) for the differences between SynthDef and SynthDef2.

## Basic types
All data is stored big endian. All integers, unless otherwise noted, are signed. All data is packed, not padded or aligned.


**int32**
: a 32 bit integer.

**int16**
: a 16 bit integer.

**int8**
: an 8 bit integer.

**float32**
: a 32 bit IEEE floating point number.

**pstring**
: a pascal format string: a byte (an **unsigned** int8) giving the length followed by that many bytes.





## File Format
a **synth-definition-file** is :

- int32 - four byte file type id containing the ASCII characters: "SCgf"
- int32 - file version, currently 2.
- int16 - number of synth definitions in this file (D).
- [ **synth-definition** ] * D


a **synth-definition** is :

- pstring - the name of the synth definition
- int32 - number of constants (K)
- [float32] * K - constant values
- int32 - number of parameters (P)
- [float32] * P - initial parameter values
- int32 - number of parameter names (N)
- [ **param-name** ] * N
- int32 - number of unit generators (U)
- [ **ugen-spec** ] * U
- int16 - number of variants (V)
- [ **variant-spec** ] * V


a **param-name** is :

- pstring - the name of the parameter
- int32 - its index in the parameter array


a **ugen-spec** is :

- pstring - the name of the SC unit generator class
- int8 - calculation rate
- int32 - number of inputs (I)
- int32 - number of outputs (O)
- int16 - special index
- [ **input-spec** ] * I
- [ **output-spec** ] * O


an **input-spec** is :

- int32 - index of unit generator or -1 for a constant
- if (unit generator index == -1) :- int32 - index of constant

- else :- int32 - index of unit generator output



an **output-spec** is :

- int8 - calculation rate


a **variant-spec** is :

- pstring - the name of the variant
- [float32] * P - variant initial parameter values




## File Format as Tree
added by Jonatan Liljedahl


### synth-definition-file
int32 - four byte file type id containing the ASCII characters: "SCgf"int32 - file version, currently 2.int16 - number of synth definitions in this file (D).[ **synth-definition** ] * Dpstring - the name of the synth definitionint32 - number of constants (K)[float32] * K - constant valuesint32 - number of parameters (P)[float32] * P - initial parameter valuesint32 - number of parameter names (N)[ **param-name** ] * Npstring - the name of the parameterint32 - its index in the parameter arrayint32 - number of unit generators (U)[ **ugen-spec** ] * Upstring - the name of the SC unit generator classint8 - calculation rateint32 - number of inputs (I)int32 - number of outputs (O)int16 - special index[ **input-spec** ] * Iint32 - index of unit generator or -1 for a constantif (unit generator index == -1)int32 - index of constantelseint32 - index of unit generator output[ **output-spec** ] * Oint8 - calculation rateint16 - number of variants (V)[ **variant-spec** ] * Vpstring - the name of the variant[float32] * P - variant initial parameter values




## Original SynthDef format
The original SynthDef format differs in that the following items are `int16` instead of `int32`.


> **Note:** The following list describes what has changed between SynthDef and SynthDef2. It is not a complete description of the original SynthDef file format.


- int32 - file version, currently 1. (This is *2* for the new format.)
- a **synth-definition** is :- int16 - number of constants (K)
- int16 - number of parameters (P)
- int16 - number of parameter names (N)
- int16 - number of unit generators (U)

- a **param-name** is :- int16 - its index in the parameter array

- a **ugen-spec** is :- int16 - number of inputs (I)
- int16 - number of outputs (O)

- an **input-spec** is :- int16 - index of unit generator or -1 for a constant
- int16 - index of constant
- int16 - index of unit generator output





## Glossary

**calculation rate**
: the rate that a computation is done. There are three rates numbered 0, 1, 2 as follows:
**0 = scalar rate**
: one sample is computed at initialization time only.

**1 = control rate**
: one sample is computed each control period.

**2 = audio rate**
: one sample is computed for each sample of audio output.

Outputs have their own calculation rate. This allows MultiOutUGens to have outputs at different rates. A one output unit generator's calculation rate should match that of its output.

**constant**
: a single floating point value that is used as a unit generator input.

**parameter**
: a value that can be externally controlled using server commands /s.new, /n.set, /n.setn, /n.fill, /n.map .

**parameter name**
: a string naming an index in the parameter array. This allows one to refer to the same semantic value such as 'freq' or 'pan' in different synths even though they exist at different offsets in their respective parameter arrays.

**special index**
: this value is used by some unit generators for a special purpose. For example, UnaryOpUGen and BinaryOpUGen use it to indicate which operator to perform. If not used it should be set to zero.

**synth**
: a collection of unit generators that execute together. A synth is a type of node.

**synth definition**
: a specification for creating synths.

**unit generator**
: a basic signal processing module with inputs and outputs. unit generators are connected together to form synths.





## Notes
Unit generators are listed in the order they will be executed. Inputs must refer to constants or previous unit generators. No feedback loops are allowed. Feedback must be accomplished via delay lines or through buses.


### For greatest efficiency:
Unit generators should be listed in an order that permits efficient reuse of connection buffers, which means that a depth first topological sort of the graph is preferable to breadth first.

There should be no duplicate values in the constants table.

copyright © 2002 James McCartney - converted to new help system 2010 by Jonatan Liljedahl, updated for version 2 by Scott Wilson 2011





