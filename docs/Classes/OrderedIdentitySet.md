# OrderedIdentitySet

*a set according to identity*

**Related:** [IdentitySet](../Classes/IdentitySet.md), [List](../Classes/List.md), [Dictionary](../Classes/Dictionary.md)

**Categories:** Collections>Ordered

## Description

An OrderedIdentitySet is a collection of objects, no two of which are the same object (aka. "identical"). Most of its methods are inherited. (see [Collection](../Classes/Collection.md) and [Set](../Classes/Set.md) classes). Unlike [IdentitySet](../Classes/IdentitySet.md), contents of an OrderedIdentitySet are ordered.


## Instance Methods

### `do`
Evaluates **function** for each item in the OrderedIdentitySet. You may depend on the order of items. The function is passed two arguments, the item and an integer index.
```supercollider
OrderedIdentitySet[1, 2, 3, 300].do { |item, i| item.postln };
```



