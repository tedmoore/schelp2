# Set

*a set according to equality*

**Related:** [IdentitySet](../Classes/IdentitySet.md), [List](../Classes/List.md), [Dictionary](../Classes/Dictionary.md)

**Categories:** Collections>Unordered

## Description

An instance of the class `Set` (a set) is a collection of objects, in which no two elements are equal. Most of its methods are inherited from `Collection`. The contents of a set are unordered; therefore, code must not rely on the order of elements in a set. For an ordered variant, see [OrderedIdentitySet](../Classes/OrderedIdentitySet.md); for multisets (i.e., sets in which distinct elements can be equal, but that remain unordered), see [Bag](../Classes/Bag.md).

> **Note:** Currently, a set cannot contain `nil` as an element. Attempting to add `nil` will result in a runtime error: This restriction exists because `nil` is internally used as a sentinel value to represent unoccupied slots in hash-based collections. As a result, this limitation also applies to Set’s subclasses.




## Instance Methods


### Adding and Removing
### `add`
Add an Object to the Set. An object which is equal to an object already in the Set will not be added.
```supercollider
Set[1, 2, 3].add(4).postln;
Set[1, 2, 3].add(3).postln;
Set["abc", "def", "ghi"].add("jkl").postln;
Set["abc", "def", "ghi"].add("def").postln;
```


### `remove`
Remove an Object from the Set. Element is checked for equality (not for identity).
```supercollider
Set[1, 2, 3].remove(3).postln;
```



### Testing
### `includes`
Returns true if the specified item is present in the Set. Elements are checked for equality (not for identity).
```supercollider
Set[1, 2, 3].includes(2).postln;
```


### `findMatch`
Returns the item, if it is present in the set. Otherwise returns nil. Element is checked for equality (not for identity).
```supercollider
Set[1, 2, 3].findMatch(3).postln;
```



### Iteration
### `do`
Evaluates function for each item in the Set. The function is passed two arguments, the item and an integer index.
```supercollider
Set[1, 2, 3, 300].do({ |item, i| item.postln });
```


### `keyAt`
Returns the object at the internal **index**. This index is not deterministic.

### Set specific operations
### `sect`, `&`
Return the set theoretical intersection of this and **that**. The function will search for objects occurring in both sets and return a new set containing those. Elements are checked for equality (not for identity).
```supercollider
a = Set[1, 2, 3]; b = Set[2, 3, 4, 5];
sect(a, b);
a & b // shorter syntax
```


### `union`, `|`
Return the set theoretical union of this and **that**. The function combines the two sets into one without duplicates. Elements are checked for equality (not for identity).
```supercollider
a = Set[1, 2, 3]; b = Set[2, 3, 4, 5];
union(a, b);
a | b // shorter syntax
```


### `difference`, `-`
Return the set of all items which are elements of this, but not of **that**. Elements are checked for equality (not for identity).
```supercollider
a = Set[1, 2, 3]; b = Set[2, 3, 4, 5];
difference(a, b);
a - b // shorter syntax
```


### `symmetricDifference`, `--`
Return the set of all items which are not elements of both this and **that**. Elements are checked for equality (not for identity).
```supercollider
a = Set[1, 2, 3]; b = Set[2, 3, 4, 5];
symmetricDifference(a, b);
a -- b // shorter syntax
```


### `isSubsetOf`
Returns true if all elements of this are also elements of **that**. Elements are checked for equality (not for identity). Since Set is an unordered collection, order doesn't matter in this comparison.
```supercollider
a = Set[1, 2, 3, 4];
Set[1, 2].isSubsetOf(a); // true
Set[1, 5].isSubsetOf(a); // false
```



## Examples


```supercollider
a = Set[1, 2, 3, 4];
b = a.powerset; // set of all parts
a.isSubsetOf(b); // false: no set is ever part of itself.
b.asArray.reduce(\union) == a; // true parts may not contain other elements that original
b.asArray.reduce(\difference).isEmpty; // true.
```



```supercollider
// you can use Set to efficiently remove duplicates from an array:

a = [1, 2, 3, 4, 3, 5, 5, 2, 2, 1];
a.as(Set);        // convert to set
a.as(Set).as(Array);    // and convert back
```




