# SparseArray

**Categories:** Collections>Ordered

*Array that stores duplicated values more efficiently*

## Description

A sparse array is a data structure that acts in exactly the same manner as an Array. However, data is represented differently in memory, in a way that makes it much more efficient to store very large arrays in which many values are the same.
Take for example an array consisting of a million zeroes, with a 1 appended to the end; SparseArray would compress this array by storing zero as a default value, and only explicitly storing the single value that differs, therefore offering a much more economical use of memory.
The benefits of using SparseArray typically arise when creating collections containing many millions of slots.


## Class Methods


### `newClear`
Create a new SparseArray of the specified **size**, with each slot's value being **default**.
```
g = SparseArray.newClear(20, 3);
g.postcs;
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `size` | Number of slots in the desired array. Note that slots are not explicitly created, so the speed of creation is not related to the array size. |  
| `default` | The default value, i.e. the value that all slots should take at first. |  


### `reduceArray`
Create a new SparseArray holding the same data as **array**.
```
a = [4, 7, 4, 4, 4, 4, 4, 4, 9, 9, 8];
g = SparseArray.reduceArray(a, 4);
g.postcs;
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `array` | Any [ArrayedCollection](../Classes/ArrayedCollection.md). |  
| `default` | The default value, i.e. the value that all slots should take at first. For best memory efficiency, you should supply the most common value found in the collection. |  


## Instance Methods


### `put`
Put a value at the desired index. This works just like all ArrayedCollection types. Behind the scenes the class will ensure the compact representation (deciding whether to store the value explicitly or implicitly).
```
g = SparseArray.newClear(10, 3);
g.put(4, \horse);
g.put(6, [4, 5, 6]);
g[1] = \hello; // Common compact notation
```


### `at`
Retrieve the value at index.
```
g = SparseArray.newClear(20, 3);
g.put(4, \horse);
g.at(4);
g[4];
```


### `asArray`
Convert to an ordinary [Array](../Classes/Array.md).
```
g = SparseArray.newClear(20, 3);
g.postcs;
g.asArray;
```


## Examples

Here we compare speed of Array vs SparseArray.

```
// Let's create a standard array, big but with only a couple of unusual values hidden in there
(
{
    a = { 10 }.dup(1000000);
    a[551] = 77;
    a[8722] = \foo;
}.bench
)
// Now a SparseArray made out of exactly the same data
(
{
    b = SparseArray.newClear(a.size, 10);
    b[551] = 77;
    b[8722] = \foo;
}.bench
)

// Alternatively you could make the SparseArray out of the existing array,
// although this is typically not as efficient as starting from scratch
// since the Array needs to be scanned directly.
(
{
    b = SparseArray.reduceArray(a, 10);
}.bench
)

// accessing:
{ 1000.do{ a[a.size.rand] == 60.rand } }.bench
{ 1000.do{ b[b.size.rand] == 60.rand } }.bench
// setting:
{ 1000.do{ a[a.size.rand] = 60.rand } }.bench
{ 1000.do{ b[b.size.rand] = 60.rand } }.bench
```




