# LibraryBase

*Abstract global storage class*

**Categories:** Collections

## Description

Base class for [Library](../Classes/Library.md) and [Archive](../Classes/Archive.md)
There is only one global instance: Archive.global, or Library.global, which is initialized automatically in the subclasses.


## Class Methods


### `global`
Subclass responsibility

### `clear`
Clear the dictionary

### `at`
Access the dictionary at a path with keys. The keys may be any object, but are usually [Symbol](../Classes/Symbol.md)s.

### `put`
Store an object in the dictionary at a path, given as a list of keys and the object to be stored as last argument. The keys may be any object, but are usually [Symbol](../Classes/Symbol.md)s.

### `atList`
Access the dictionary at a path, given as a list of keys. The keys may be any object, but are usually [Symbol](../Classes/Symbol.md)s.

### `putList`
Store an object in the dictionary at a path, given as a list of keys and the object to be stored as last argument. The keys may be any object, but are usually [Symbol](../Classes/Symbol.md)s.
## Examples


```
// an example from the subclass Library:

Library.put(\multi, \level, \addressing, \system, "i'm the thing you are putting in here");
Library.at(\multi, \level, \addressing, \system).postln;
Library.atList([\multi, \level, \addressing, \system]).postln;
```




