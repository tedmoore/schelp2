# UnaryOpUGen

*Apply a unary operation to the values of an input ugen*

**Categories:** UGens>Algebraic

**Related:** [BinaryOpUGen](../Classes/BinaryOpUGen.md), [UnaryOpFunction](../Classes/UnaryOpFunction.md), [Punop](../Classes/Punop.md), [Overviews/Operators](../Overviews/Operators.md)

## Description

UnaryOpUGens are created as the result of a unary operator applied to a [UGen](../Classes/UGen.md).

```supercollider
(SinOsc.ar(200).abs).dump;
(LFSaw.ar(200).sin).dump;
```


As in the examples given here, you don't usually need to instantiate UnaryOpUGen yourself.
The unary and binary operators are defined in [UGen](../Classes/UGen.md)'s superclass [AbstractFunction](../Classes/AbstractFunction.md), which creates the BinaryOpUGen as a result of the operation.
See [Operators](../Overviews/Operators.md) for an overview of common operators.


## Class Methods

### `new`
return a new instance that applies the operator `selector` to the ugen `a`**Arguments:**

| Argument | Description |
|----------|-------------|
| `selector` | The selector symbol for the unary operator |  
| `a` | operand |  

## Examples


```supercollider
a = WhiteNoise.ar; // a WhiteNoise
b = a.squared; // a UnaryOpUGen.
b.operator; // squared

// sound example

{ var a = LFSaw.ar(300).range(0, 2pi); a.sin * 0.1 }.play;

// Plotting the "abs" unary operator (via the server):

{ SinOsc.ar(300).abs }.plot
```




