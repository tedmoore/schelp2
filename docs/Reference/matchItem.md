# matchItem

**Categories:** Common methods

*test if object fulfils a constraint*

Implemented by: [Object](../Classes/Object.md), [Collection](../Classes/Collection.md), [Nil](../Classes/Nil.md), [Function](../Classes/Function.md)
### `matchItem`
matchItem(item) may be passed to different objects that behave as constraints. More Objects may be conceived to implement matchItem to extend the interface.See also: [Dictionary#-matchAt](../Classes/Dictionary.md#-matchat).
## Object-matchItem
Test if **item** is identical to **object**.


```supercollider
a = [1, 2, 3, "wort", "1", [pi, 2pi]];
a.any { |x| x.matchItem(3) }; // true
a.any { |x| x.matchItem(5) }; // false
a.any { |x| x.matchItem("wort") }; // false, because "wort" == "wort" but not identical.
```




## Collection-matchItem
Test if **item** is included in **collection**.


```supercollider
a = [1, 2, 3, "wort", "1", [pi, 2pi]];
a.any { |x| x.matchItem(pi) }; // true
```




## Nil-matchItem
returns true ([Nil](../Classes/Nil.md) serves as a "joker", a stand-in for anything).


```supercollider
a = [nil, 1, 2, 3, "wort", "1", [pi, 2pi]];
a.any { |x| x.matchItem(10000.rand) }; // true always
```




## Function-matchItem
Test **item** by passing it to a function which should return a [Boolean](../Classes/Boolean.md).


```supercollider
a = [10, 20, 30, { |item| item.isPrime }];
a.any { |x| x.matchItem(3) }; // true
a.any { |x| x.matchItem(4) }; // false
a.any { |x| x.matchItem(10) }; // true
```






