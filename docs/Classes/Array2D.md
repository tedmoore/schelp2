# Array2D

*two-dimensional array*

**Related:** [Array](../Classes/Array.md)

**Categories:** Collections>Ordered

## Description

Represents a two-dimensional array of data. The number of rows and columns is fixed.

> **Note:** It is possible to implement a similar behaviour using an "array-of-arrays" - see the examples towards the bottom of this page for comparison.




## Class Methods


### `new`
Create an array of the specified size.
```
a = Array2D.new(3, 4);
a[2, 2] = 1;
a.postln
```



### `fromArray`
Build an Array2D from the supplied array.
```
a = Array2D.fromArray(3, 4, [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4]);
a[2, 2] = 1;
a.postln
```



## Instance Methods


### `at`
Get a value from the array.
```
a.at(2, 3);
a[2, 3];
```


### `put`
Put a value into the array.
```
a.put(2, 3, 72);
a[2, 3] = 72;
```


### `colsDo`
Iterate over the columns. Each column will be passed to **func** in turn.
```
a.colsDo(_.postln);
```


### `rowsDo`
Iterate over the rows. Each row will be passed to **func** in turn.
```
a.rowsDo(_.postln);
```


### `colAt`
Retrieve a single column.
```
a.colAt(2);
```


### `rowAt`
Retrieve a single row.
```
a.rowAt(2);
```


### `asArray`
Return a flat array containing the elements.
```
a.postln;
a.asArray.postln;
```

**Returns:** [Array](../Classes/Array.md)
## Examples


```
// "a" is an array-of-arrays
a = { { 100.0.rand }.dup(100) }.dup(100);
// "b" is an equivalent Array2D, made using the "fromArray" class method
b = Array2D.fromArray(100, 100, a.flat);

// Accessing
a[15][22]
b[15, 22]

// Speed comparison 1: random access
bench { 100.do(a[100.rand][100.rand]) }
bench { 100.do(b[100.rand, 100.rand]) }

// Speed comparison 2: iteration
bench { 100.do(a.do { |row| row.do { |item| item * 2 } }) }
bench { 100.do(b.do { |item| item * 2 }) }
```




