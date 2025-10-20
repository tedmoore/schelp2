# Pair

*LISP-like two element cells*

**Categories:** Collections>Ordered

## Description


> **Note:** Implementation incomplete. See [J-concepts-in-SC](../Guides/J-concepts-in-SC.md) for similar functionality.


Most methods are inherited from the superclasses.


## Class Methods


### `new`
Return new instance.

### `newFrom`
Convert collection (e.g. arrays of arrays) to pairs.

## Instance Methods


### `size`
Return the size when linking across.
### `depth`
Return the size when linking down.
### `do`
Iterate over the two elements.
### `traverse`
Same like: [#-depthFirstPreOrderTraversal](#-depthfirstpreordertraversal)
### `depthFirstPreOrderTraversal`
Traverse the data structure first link down, then across (see [#examples](#examples)).
### `depthFirstPostOrderTraversal`
Traverse the data structure from bottom up (see [#examples](#examples)).
## Examples


```
a = Pair(Pair(Pair(1, 2), 4), Pair(5, 6));

a.size;
a.depth;
a.do { |x| x.postln };
a.traverse { |x| x.postln };
a.depthFirstPreOrderTraversal { |x| x.postln };
a.depthFirstPostOrderTraversal { |x| x.postln };


// alternative instantiations:

Pair.newFrom([1, [2, [[4, 5], 6]]]);

[1, [2, [[4, 5], 6]]].as(Pair); // equivalent.
```




