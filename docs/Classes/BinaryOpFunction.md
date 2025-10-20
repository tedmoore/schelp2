# BinaryOpFunction

*represent a binary operation on a function*

**Categories:** Core

**Related:** [UnaryOpFunction](../Classes/UnaryOpFunction.md), [NAryOpFunction](../Classes/NAryOpFunction.md), [BinaryOpStream](../Classes/BinaryOpStream.md), [Pbinop](../Classes/Pbinop.md), [Overviews/Operators](../Overviews/Operators.md)

## Description

Operating on functions instead of numbers, what results is not a result of the calculation, but a structure that represents that calculation.


## Instance Methods


### `value`
Executes each of the operand functions and then performs the selector on the result.
### `valueArray`
the same as [#-value](#-value)
## Examples


```
// example
a = 5 + 7; // result is 12.
a = { b } + 7; // result is  a BinaryOpFunction
b = 5;
a.value; // now it is evaluated, and the result is calculated
b = 8;
a.value; // again, with a different value.
```



```
// sound example
(
var a = { 19.rand };
var b = { [5, 8, 9].choose };
var c = a + b;
fork {
    15.do {
        (instrument: \default, note: [c.value, a.value]).play;
        0.3.wait;
    }
}
)
```




