# TwoWayIdentityDictionary

*associative collection mapping keys to values and back*

**Related:** [IdentityDictionary](../Classes/IdentityDictionary.md)

**Categories:** Collections>Unordered

## Description

Similar to [IdentityDictionary](../Classes/IdentityDictionary.md), but allows to go efficiently from element to key and back. The contents of a TwoWayIdentityDictionary are **unordered**. You must not depend on the order of items.


## Instance Methods

### `getID`
Find the key for a given object. If object is not element of the dictionary, it returns nil.
## Examples


```supercollider
a = TwoWayIdentityDictionary.new;
a.put(\test, 999);
a.put(["some", "strings"], 1200);
a.at(\test);
a.getID(999);
a.getID(1200);
a.getID(888); // nil
```




