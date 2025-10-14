# Collections

*A hierarchical overview of Collection subclasses*

**Categories:** Collections

**Related:** [Collection](../Classes/Collection.md)

SuperCollider has a rich hierarchy of Collection subclasses, detailed below. Subclasses of a given class are indented (sub-lists) relative to the class. Classes labelled "abstract" are not for direct use, but classes lower down the tree may inherit methods from them. For this reason it is important to consult the helpfiles of classes farther up the tree in order to get a complete list of available methods.

## Hierarchy


### Notes

**[List](../Classes/List.md)**
: is an expandable [SequenceableCollection](../Classes/SequenceableCollection.md) (compare to [ArrayedCollection](../Classes/ArrayedCollection.md) and [Array](../Classes/Array.md)).

**[Array](../Classes/Array.md)**
: is more efficient than [List](../Classes/List.md).

**[SparseArray](../Classes/SparseArray.md)**
: is an array of elements optimized for huge gaps between them.

**[TwoWayIdentityDictionary](../Classes/TwoWayIdentityDictionary.md)**
: is similar to [IdentityDictionary](../Classes/IdentityDictionary.md) and allows easy searching by both key and value. It is faster than [IdentityDictionary](../Classes/IdentityDictionary.md) on reverse lookup, but with more memory overhead.

**[Environment](../Classes/Environment.md)**
: is an [IdentityDictionary](../Classes/IdentityDictionary.md), one of which is always current; useful for creating sets of persistent variables.

**[Event](../Classes/Event.md)**
: is a dictionary mapping names of musical parameters to their values.

**[IdentitySet](../Classes/IdentitySet.md)**
: is an unordered collection of unidentical objects (compare to [Set](../Classes/Set.md)).









