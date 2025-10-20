# Library

*keeping objects in a central place*

**Related:** [Archive](../Classes/Archive.md), [LibraryBase](../Classes/LibraryBase.md)

**Categories:** Collections

## Description

Library is a global MultiLevelIdentityDictionary. The Library can be used as a place to store data that you want globally accessible. It is an alternative to using class variables. It is a nice place to store menus, annotations, and commonly reusable functions.


## Class Methods



### `postTree`
Post a formatted description of the entire library.
```
Library.postTree;
```



### `put`
The last argument to put is the object being inserted:
```
Library.put(\multi, \level, \addressing, \system, "i'm the thing you are putting in here");
Library.at(\multi, \level, \addressing, \system).postln;
Library.atList([\multi, \level, \addressing, \system]).postln;
```



