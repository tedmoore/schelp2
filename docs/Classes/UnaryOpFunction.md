# UnaryOpFunction

*represent a unary operation on a function*

**Related:** [UnaryOpStream](../Classes/UnaryOpStream.md), [Punop](../Classes/Punop.md), [BinaryOpFunction](../Classes/BinaryOpFunction.md), [NAryOpFunction](../Classes/NAryOpFunction.md), [Overviews/Operators](../Overviews/Operators.md)

**Categories:** Core

## Description

Operating on functions instead of numbers, what results is not a result of the calculation, but a structure that represents that calculation.

## Examples


```supercollider
a = 2.sqrt; // result is square root of two (approximate floating point).
a = { b }.sqrt; // result is  a UnaryOpFunction
b = 2;
a.value; // now it is evaluated, and the result is calculated
b = 9;
a.value; // again, with a different value.
```



```supercollider
// sound example
(
var a = { 19.rand };
var b = a.sqrt;
fork {
    15.do {
        (instrument: \default, note: [a.value, b.value]).play;
        0.3.wait;
    }
}
)
```




