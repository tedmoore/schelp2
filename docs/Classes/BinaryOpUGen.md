# BinaryOpUGen

*Apply a binary operation to the values of an input UGen*

**Related:** [UnaryOpUGen](../Classes/UnaryOpUGen.md), [BinaryOpFunction](../Classes/BinaryOpFunction.md), [Pbinop](../Classes/Pbinop.md), [Overviews/Operators](../Overviews/Operators.md)

**Categories:** UGens>Algebraic

## Description

BinaryOpUGens are created as the result of a binary operator applied to a [UGen](../Classes/UGen.md).

```
(SinOsc.ar(200) * ClipNoise.ar).dump;
(SinOsc.ar(200).thresh(0.5)).dump;
```


The use of the binary operators `*` and `thresh` above each instantiate a BinaryOpUGen. The operators themselves (which are methods) are not to be confused with the resulting BinaryOpUGen (which is an object). The unary and binary operators are defined in [UGen](../Classes/UGen.md)'s superclass [AbstractFunction](../Classes/AbstractFunction.md), which creates the BinaryOpUGen as a result of the operation.
When operating on UGens instead of numbers, what results is not a result of the calculation, but a structure that represents that calculation. For the immediate operations on numbers, see for example [SimpleNumber](../Classes/SimpleNumber.md).
See [Operators](../Overviews/Operators.md) for an overview of common operators.


## Class Methods



### `new`
return a new instance that applies the operator `selector` to the UGens `a` and `b` normally, this is implicitly called when applying an operator to a [UGen](../Classes/UGen.md).**Arguments:**

| Argument | Description |
|----------|-------------|
| `selector` | The selector symbol for the binary operator |  
| `a` | left operand |  
| `b` | right operand |  
**Returns:** A new instance of BinaryOpUGen

## Instance Methods


## Examples


```
a = WhiteNoise.ar; // a WhiteNoise
b = a + 2; // a BinaryOpUGen.
b.operator; // +

// sound example
(
{
    var a = LFSaw.ar(300);
    var b = LFSaw.ar(329.1);
    a % b * 0.1
}.play;
)
```



### The comparison operators
The operators `>, >=, <, <=` are particularly useful for triggering. They should not be confused with their use in conditionals. Compare:


```
if(1 > 0) { "1 is greater than 0".postln }; // > returns a boolean
```


with


```
// trigger an envelope
(
{
    var trig;
    trig = SinOsc.ar(1) > 0.1;
    EnvGen.kr(Env.perc, trig, doneAction: Done.none) * SinOsc.ar(440, 0, 0.1)
}.play
) // > outputs 0 or 1
```


See [Operators](../Overviews/Operators.md) or the implementation of these in [AbstractFunction](../Classes/AbstractFunction.md) for more detail.

Since the equality operator (`==`) is used to distinguish objects including UGens, it cannot be used to create a BinaryOpUGen by application. Instead, to get a trigger value each time two signals are the same (instead of just finding out whether two UGens are the same), one can instantiate a BinaryOpUGen directly:


```
(
{
    var a = SinOsc.ar(1).round(0.1);
    var b = SinOsc.ar(1.2).round(0.1);
    BinaryOpUGen('==', a, b) * 0.1
}.play;
)
```






