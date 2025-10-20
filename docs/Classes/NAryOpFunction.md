# NAryOpFunction

*represent a n-ary operation on a function*

**Categories:** Core

**Related:** [BinaryOpFunction](../Classes/BinaryOpFunction.md), [UnaryOpFunction](../Classes/UnaryOpFunction.md), [NAryOpStream](../Classes/NAryOpStream.md), [Pnaryop](../Classes/Pnaryop.md), [Overviews/Operators](../Overviews/Operators.md)

## Description

Operating on functions instead of numbers, what results is not a result of the calculation, but a structure that represents that calculation.

## Examples


```
// example
a = 0.8.linexp(0, 1, 40, 20000); // map (0..1) to exponentially to human frequency hearing range
a = { b }.linexp(0, 1, 40, 20000); // result is  a NAryOpFunction
b = 0.1;
a.value; // now it is evaluated, and the result is calculated
b = 0.5;
a.value; // again, with a different value.
```



```
// sound example
(
var a = { 1.0.rand };
var b = a.linexp(0, 1, 40, 20000);
fork {
    15.do {
        (instrument: \default, freq: b.value).play;
        0.3.wait;
    }
}
)
```




