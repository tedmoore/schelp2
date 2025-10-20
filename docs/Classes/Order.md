# Order

*an order of elements with a numerical index*

**Related:** [SparseArray](../Classes/SparseArray.md)

**Categories:** Collections>Ordered

## Description

Keeps elements in an order and allows to put them at arbitrary slots without having to allocate a large array.

> **Note:** [#-put](#-put) and [#-at](#-at) are slower than in [IdentityDictionary](../Classes/IdentityDictionary.md) / [PriorityQueue](../Classes/PriorityQueue.md), [#-do](#-do) is faster.




## Class Methods


### `new`
Create a new order.
```
g = Order.new;
g.put(7, 100); // put a value (100) at index 7
g.clear; // empty
```



### `newFromIndices`
Create a new order from given items and indices.

## Instance Methods


### `doRange`
Iterate over a range of the order's items.
### `pos`
Return the current write position.
## Examples


```
a = Order.new;

a[0] = \z;
a[0] = \y;
a[5] = \five;
a[4] = \four;

a[0] = \z;
a[5] = \five;
a[4] = \four;

a.indices;

a[9] = 100;
a.indices;
```




