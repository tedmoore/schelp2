# SequenceableCollection

*Abstract superclass of indexable collections*

**Categories:** Collections>Ordered

## Description

[SequenceableCollection](../Classes/SequenceableCollection.md) is a subclass of [Collection](../Classes/Collection.md) whose items can be indexed by a [SimpleNumber](../Classes/SimpleNumber.md). It has many useful subclasses; [Array](../Classes/Array.md) and [List](../Classes/List.md) are amongst the most commonly used.

### Indexing
In SuperCollider, an **index** is a number used to access items in the subclasses of [SequenceableCollection](../Classes/SequenceableCollection.md) such as arrays and lists. Indexing starts at `0`, so the first element of a collection is at index `0`, the second at index `1`, and so on. The item at a specific index is accessed using `.at(index)` method or its shortcut `[index]`. If using an index that is outside the bounds of the collection (too low or too high), SuperCollider returns `nil`.

Example:


```supercollider
a = [100, 200, 300];
a.at(0); // Returns 100 (the first item)
a[0]     // Same as above (syntactic sugar; shortcut)
a[2];    // Returns 300 (the third item)
a[5];    // Returns nil (the index is out of bounds)
```





## Class Methods


### `series`
Fill a SequenceableCollection with an arithmetic series.
```supercollider
Array.series(5, 10, 2);
```


### `geom`
Fill a SequenceableCollection with a geometric series.
```supercollider
Array.geom(5, 1, 3);
```


### `fib`
Fill a SequenceableCollection with a fibonacci series.
```supercollider
Array.fib(5);
Array.fib(5, 2, 32); // start from 32 with step 2.
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `size` | the number of values in the collection |  
| `a` | the starting step value |  
| `b` | the starting value |  

### `rand`
Fill a SequenceableCollection with random values in the range **minVal** to **maxVal**.
```supercollider
Array.rand(8, 1, 100);
```


### `rand2`
Fill a SequenceableCollection with random values in the range -**val** to +**val**.
```supercollider
Array.rand2(8, 100);
```


### `linrand`
Fill a SequenceableCollection with random values in the range **minVal** to **maxVal** with a linear distribution.
```supercollider
Array.linrand(8, 1, 100);
```


### `exprand`
Fill a SequenceableCollection with random values in the range **minVal** to **maxVal** with exponential distribution.
```supercollider
Array.exprand(8, 1, 100);
```


### `interpolation`
Fill a SequenceableCollection with the interpolated values between the **start** and **end** values.
```supercollider
Array.interpolation(5, 3.2, 20.5);
```



## Instance Methods

### `|@|`
synonym for [ArrayedCollection#-clipAt](../Classes/ArrayedCollection.md#-clipat) and [List#-clipAt](../Classes/List.md#-clipat).
```supercollider
[3, 4, 5]|@|6     // -> 5
List[3, 4, 5]|@|6 // -> 5
```

### `@@`
synonym for [ArrayedCollection#-wrapAt](../Classes/ArrayedCollection.md#-wrapat) and [List#-wrapAt](../Classes/List.md#-wrapat).
```supercollider
[3, 4, 5]@@6      // -> 3
[3, 4, 5]@@ -1    // -> 5
[3, 4, 5]@@[6, 8] // -> [3, 5]

List[3, 4, 5]@@6      // -> 3
List[3, 4, 5]@@ -1    // -> 5
List[3, 4, 5]@@[6, 8] // -> [3, 5]
```

### `@|@`
synonym for [ArrayedCollection#-foldAt](../Classes/ArrayedCollection.md#-foldat) and [List#-foldAt](../Classes/List.md#-foldat).
```supercollider
[3, 4, 5]@|@[6, 8]     // -> [5, 3]
List[3, 4, 5]@|@[6, 8] // -> [5, 3]
```

### `first`
Return the first element of the collection.
```supercollider
[3, 4, 5].first;
```

### `last`
Return the last element of the collection.
```supercollider
[3, 4, 5].last;
```

### `putFirst`, `putLast`
Place **item** at the first / last index in the collection. Note that if the collection is empty (and therefore has no indexed slots) the item will not be added.
```supercollider
[3, 4, 5].putFirst(100);
[3, 4, 5].putLast(100);
```

### `indexOf`
Return the index of an **item** in the collection, or nil if not found. Elements are checked for identity (not for equality).
```supercollider
[3, 4, 100, 5].indexOf(100);
[3, 4, \foo, \bar].indexOf(\foo);
```

### `indexOfEqual`
Return the index of something in the collection that equals the **item**, or nil if not found.
```supercollider
[3, 4, "foo", "bar"].indexOfEqual("foo");
```

### `indicesOfEqual`
Return an array of indices of things in the collection that equal the **item**, or nil if not found.
```supercollider
y = [7, 8, 7, 6, 5, 6, 7, 6, 7, 8, 9];
y.indicesOfEqual(7);
y.indicesOfEqual(5);
```

### `indexOfGreaterThan`
Return the first index containing an **item** which is greater than **item**.
```supercollider
y = List[10, 5, 77, 55, 12, 123];
y.indexOfGreaterThan(70);
```

### `selectIndices`
Return a new collection of same type as receiver which consists of all indices of those elements of the receiver for which function answers `true`. The function is passed two arguments, the item and an integer index.
```supercollider
#[a, b, c, g, h, h, j, h].selectIndices({ |item, i| item === \h })
```

If you want to control what type of collection is returned, use [#-selectIndicesAs](#-selectindicesas)### `selectIndicesAs`
Return a new collection of type *class* which consists of all indices of those elements of the receiver for which function answers `true`. The function is passed two arguments, the item and an integer index.
```supercollider
#[a, b, c, g, h, h, j, h].selectIndicesAs({ |item, i| item === \h }, Set)
```

### `rejectIndices`
Return a new collection of same type as receiver which consists of all indices of those elements of the receiver for which function answers `false`. The function is passed two arguments, the item and an integer index.
```supercollider
#[a, b, c, g, h, h, j, h].rejectIndices({ |item, i| item === \h })
```

If you want to control what type of collection is returned, use [#-rejectIndicesAs](#-rejectindicesas)### `rejectIndicesAs`
Return a new collection of type *class* which consists of all indices of those elements of the receiver for which function answers `false`. The function is passed two arguments, the item and an integer index.
```supercollider
#[a, b, c, g, h, h, j, h].rejectIndicesAs({ |item, i| item === \h }, Set)
```

### `find`
If the **sublist** exists in the receiver (in the specified order), at an offset greater than or equal to the initial **offset**, then return the starting index. The sublist must be of the same kind (class) as the list to search in. Elements are checked for equality (not for identity).
```supercollider
y = [7, 8, 7, 6, 5, 6, 7, 6, 7, 8, 9];
y.find([7, 6, 5]);
```

### `findAll`
Similar to [#-find](#-find) but returns an array of all the indices at which the sequence is found.
```supercollider
y = [7, 8, 7, 6, 5, 6, 7, 6, 7, 8, 9];
y.findAll([7, 6]);
```

### `indexIn`
Returns the closest index of the value in the collection (collection must be sorted).
```supercollider
[2, 3, 5, 6].indexIn(5.2);
```

### `indexInBetween`
Returns a linearly interpolated float index for the value (collection must be sorted). Inverse operation is [#-blendAt](#-blendat).
```supercollider
x = [2, 3, 5, 6].indexInBetween(5.2);
[2, 3, 5, 6].blendAt(x);
```

### `blendAt`
Returns a linearly interpolated value between the two closest indices. Inverse operation is [#-indexInBetween](#-indexinbetween).
```supercollider
x = [2, 5, 6].blendAt(0.4);
```

### `copyRange`
Return a new SequenceableCollection which is a copy of the indexed slots of the receiver from **start** to **end**. If **end** < **start**, an empty collection is returned.
```supercollider
(
var y, z;
z = [1, 2, 3, 4, 5];
y = z.copyRange(1, 3);
z.postln;
y.postln;
)
```

> **⚠️ Warning:** `x.copyRange(a, b)` is **not** equivalent to `x[a..b]`. The latter compiles to [ArrayedCollection#-copySeries](../Classes/ArrayedCollection.md#-copyseries), which has different behavior when **end** < **start**.### `copyToEnd`
Return a new SequenceableCollection which is a copy of the indexed slots of the receiver from **start** to the end of the collection. `x.copyToEnd(a)` can also be written as `x[a..]`### `copyFromStart`
Return a new SequenceableCollection which is a copy of the indexed slots of the receiver from the start of the collection to **end**. `x.copyFromStart(a)` can also be written as `x[..a]`### `remove`
Remove **item** from collection. Elements are checked for identity (not for equality).### `take`
Remove and return **item** from collection. The last item in the collection will move to occupy the vacated slot (and the collection size decreases by one). See also takeAt, defined for [ArrayedCollection#-takeAt](../Classes/ArrayedCollection.md#-takeat). Elements are checked for identity (not for equality).> **⚠️ Warning:** `take(item)` works on Arrays but not on Lists, because the internally called method `takeAt(item)` is not defined for Lists.
```supercollider
a = [11, 12, 13, 14, 15];
a.take(12);
a;
```

### `obtain`
Retrieve an element from a given index (like [SequenceableCollection#-at](../Classes/SequenceableCollection.md#-at)). This method is also implemented in [Object](../Classes/Object.md), so that you can use it in situations where you don't want to know if the receiver is a collection or not. See also: [SequenceableCollection#-instill](../Classes/SequenceableCollection.md#-instill)**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | The index at which to look for an element |  
| `default` | If index exceeds collection size, or receiver is nil, return this instead
```supercollider
(
a = [10, 20, 30];
b = [10, 20];
c = 7;
);

 // obtain third element, if outside bounds return 1
a.obtain(2, 1);
b.obtain(2, 1);
c.obtain(2, 1);
``` |  
### `instill`
Put an element at a given index (like [SequenceableCollection#-put](../Classes/SequenceableCollection.md#-put)). This method is also implemented in [Object](../Classes/Object.md), so that you can use it in situations where you don't want to know if the receiver is a collection or not. It will always return a new collection. See also: [SequenceableCollection#-obtain](../Classes/SequenceableCollection.md#-obtain)**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | The index at which to put the item |  
| `item` | The object to put into the new collection |  
| `default` | If the index exceeds the current collection's size, extend the collection with this element
```supercollider
(
a = [10, 20, 30, 40];
b = [10, 20];
c = 7;
);

a.instill(2, -1);
b.instill(2, -1);
c.instill(2, -1);
// providing a default value
c.instill(2, -1, 0);
``` |  
### `keep`
Keep the first **n** items of the array. If **n** is negative, keep the last -**n** items.
```supercollider
a = [1, 2, 3, 4, 5];
a.keep(3);
a.keep(-3);
```

### `drop`
Drop the first **n** items of the array. If **n** is negative, drop the last -**n** items.
```supercollider
a = [1, 2, 3, 4, 5];
a.drop(3);
a.drop(-3);
```

### `join`
Returns a [String](../Classes/String.md) formed by connecting all the elements of the receiver, with **joiner** inbetween. See also [String#-split](../Classes/String.md#-split) as the complementary operation.
```supercollider
["m", "ss", "ss", "pp", ""].join("i").postcs;
"mississippi".split("i").postcs;
```

### `flat`
Returns a collection from which all nesting has been flattened.
```supercollider
[[1, 2, 3], [[4, 5], [[6]]]].flat; // [1, 2, 3, 4, 5, 6]
[1, 2, [3, 4, [5, 6, [7, 8, [9, 0]]]]].flat; // [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
```

### `flatten`
Returns a collection from which **numLevels** of nesting has been flattened.**Arguments:**

| Argument | Description |
|----------|-------------|
| `numLevels` | Specifies how many levels downward (inward) to flatten. Zero returns the original.
```supercollider
a = [1, 2, [3, 4, [5, 6, [7, 8, [9, 0]]]]];
a.flatten(1); // [ 1, 2, 3, 4, [ 5, 6, [ 7, 8, [9, 0] ] ] ]
a.flatten(2); // [ 1, 2, 3, 4, 5, 6, [ 7, 8, [9, 0] ] ]
a.flatten(3); // [ 1, 2, 3, 4, 5, 6, 7, 8, [9, 0] ]
a.flatten(4); // [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
``` |  
### `flatten2`
A symmetric version of [#-flatten](#-flatten). For a negative `numLevels`, it flattens starting from the innermost arrays.**Arguments:**

| Argument | Description |
|----------|-------------|
| `numLevels` | Specifies how many levels downward (inward) or upward (outward) to flatten.
```supercollider
a = [1, 2, [3, 4, [5, 6, [7, 8, [9, 0]]]]];
a.flatten2(4);  // [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
a.flatten2(3);  // [ 1, 2, 3, 4, 5, 6, 7, 8, [9, 0] ]
a.flatten2(2);  // [ 1, 2, 3, 4, 5, 6, [ 7, 8, [9, 0] ] ]
a.flatten2(1);  // [ 1, 2, 3, 4, [ 5, 6, [ 7, 8, [9, 0] ] ] ]
a.flatten2(0);  // [ 1, 2, [ 3, 4, [ 5, 6, [ 7, 8, [9, 0] ] ] ] ]
a.flatten2(-1); // [ 1, 2, [ 3, 4, [ 5, 6, [7, 8, 9, 0] ] ] ]
a.flatten2(-2); // [ 1, 2, [ 3, 4, [5, 6, 7, 8, 9, 0] ] ]
a.flatten2(-3); // [ 1, 2, [3, 4, 5, 6, 7, 8, 9, 0] ]
a.flatten2(-4); // [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
``` |  
### `flatBelow`
Flatten all subarrays deeper than **level**.**Arguments:**

| Argument | Description |
|----------|-------------|
| `level` | Specifies from what level onward to flatten. level 0 is outermost, so flatBelow(0) is like flat.
```supercollider
a = [1, 2, [3, 4, [5, 6, [7, 8, [9, 0]]]]];
a.flatBelow(0); // [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
a.flatBelow(1); // [ 1, 2, [3, 4, 5, 6, 7, 8, 9, 0] ]
a.flatBelow(2); // [ 1, 2, [ 3, 4, [5, 6, 7, 8, 9, 0] ] ]

// to set the level below which to flatten from the deepest level up,
// one can use coll.maxDepth. E.g. to flatten only the innermost level:
a.flatBelow((a.maxDepth - 1) - 1);
// for lowest two levels:
a.flatBelow((a.maxDepth - 1) - 2);
``` |  
### `flop`
Invert rows and columns in a two dimensional Collection (turn inside out). See also: [Function](../Classes/Function.md).
```supercollider
[[1, 2, 3], [4, 5, 6]].flop;
[[1, 2, 3], [4, 5, 6], [7, 8]].flop; // shorter array wraps
[].flop; // result is always 2-d.
```

Note that the innermost arrays are not copied:
```supercollider
a = [1, 2];
x = [[[a, 5], [a, 10]], [[a, 50, 60]]].flop;
a[0] = pi;
x // pi is everywhere
```

### `flopWith`
Flop with a user defined function. Can be used to collect over several collections in parallel.
```supercollider
[[1, 2, 3], [4, 5, 6]].flopWith(_+_);
[[1, 2, 3], 1, [7, 8]].flopWith{ |a, b, c| a+b+c }; // shorter array wraps

// typical use case (pseudocode)
[synths, buffers].flopWith{ |a, b| a.set(\buf, b) }
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | A function taking as many arguments as elements in the array. |  
### `flopTogether`
Invert rows and columns in a an array of dimensional Collections (turn inside out), so that they all match up in size, but remain separated.
```supercollider
(
a = flopTogether(
    [[1, 2, 3], [4, 5, 6, 7, 8]] * 100,
    [[1, 2, 3], [4, 5, 6], [7, 8]],
    [1000]
)
);

a.collect(_.size); // sizes are the same
a.collect(_.shape) // shapes can be different
```

### `flopDeep`
Fold dimensions in a multi-dimensional Collection (turn inside out).**Arguments:**

| Argument | Description |
|----------|-------------|
| `rank` | The depth (dimension) from which the array is inverted inside-out.
```supercollider
[[1, 2, 3], [[41, 52], 5, 6]].flopDeep(2);
[[1, 2, 3], [[41, 52], 5, 6]].flopDeep(1);
[[1, 2, 3], [[41, 52], 5, 6]].flopDeep(0);
[[1, 2, 3], [[41, 52], 5, 6]].flopDeep; // without argument, flop from the deepest level

[[[10, 100, 1000], 2, 3], [[41, 52], 5, 6]].flopDeep(2); // shorter array wraps
[].flopDeep(1); // result is always one dimension higher.
[[]].flopDeep(4);
```


> **Note:** Note that, just like in flop, the innermost arrays (deeper than rank) are not copied.


```supercollider
a = [1, 2];
x = [[[a, 5], [a, 10]], [[a, 50, 60]]].flopDeep(1);
a[0] = pi;
x // pi is everywhere
``` |  
### `maxSizeAtDepth`
Returns the maximum size of all subarrays at a certain depth (dimension)**Arguments:**

| Argument | Description |
|----------|-------------|
| `rank` | The depth at which the size of the arrays is measured
```supercollider
[[1, 2, 3], [[41, 52], 5, 6], 1, 2, 3].maxSizeAtDepth(2);
[[1, 2, 3], [[41, 52], 5, 6], 1, 2, 3].maxSizeAtDepth(1);
[[1, 2, 3], [[41, 52], 5, 6], 1, 2, 3].maxSizeAtDepth(0);
[].maxSizeAtDepth(0);
[[]].maxSizeAtDepth(0);
[[]].maxSizeAtDepth(1);
``` |  
### `maxDepth`
Returns the maximum depth of all subarrays.**Arguments:**

| Argument | Description |
|----------|-------------|
| `max` | Internally used only.
```supercollider
[[1, 2, 3], [[41, 52], 5, 6], 1, 2, 3].maxDepth
``` |  
### `isSeries`
Returns true if the collection is an arithmetic series.**Arguments:**

| Argument | Description |
|----------|-------------|
| `step` | Step size to look for. If none is given, any step size will match.
```supercollider
[0, 1, 2, 3, 4, 5].isSeries; // true
[1.5, 2.5, 3.5, 4.5, 5.5, 6.5].isSeries; // true
[0, 1, 4, 5].isSeries; // false
[0, 3, 6, 9, 12, 15].isSeries; // true
[0, 3, 6, 9, 12, 15].isSeries(1); // false
[2] // true
[] // true (empty sequence)
``` |  
### `resamp0`
Returns a new Collection of the desired length, with values resampled evenly-spaced from the receiver without interpolation.
```supercollider
[1, 2, 3, 4].resamp0(12);
[1, 2, 3, 4].resamp0(2);
```

### `resamp1`
Returns a new Collection of the desired length, with values resampled evenly-spaced from the receiver with linear interpolation.
```supercollider
[1, 2, 3, 4].resamp1(12);
[1, 2, 3, 4].resamp1(3);
```

### `choose`
Choose an element from the collection at random.
```supercollider
[1, 2, 3, 4].choose;
```

### `wchoose`
Choose an element from the collection at random using a list of probabilities or weights. The weights must sum to 1.0.
```supercollider
[1, 2, 3, 4].wchoose([0.1, 0.2, 0.3, 0.4]);
```

### `wchoosen`
Choose an element from the collection at random using a list of probabilities or weights. The weights are derived from a function or an array of any size, and their sum is automatically normalized to 1.0. If the weights are shorter than the collection, the remaining weights are assumed to be zero. If the weights are longer, the exceeding weights are ignored. A weight defined as a function is first called with the collection as the argument. Because the provided weights are normalized on every call, it is less efficient than using [#-wchoose](#-wchoose) with pre-normalized weights.
```supercollider
// weights are a non-normalized array
10.collect { [1, 2, 3, 4].wchoosen([10, 18, 3, 2]) }
// weights are a non-normalized too short
10.collect { [1, 2, 3, 4].wchoosen([10, 18]) }
// weights contain functions
10.collect {  [1, 2, 3, 4].wchoosen([1, 1, { 15.rand }, 1]) }
// weights contains streams
10.collect { [1, 2, 3, 4].wchoosen([1, 1, Pseries(0,1).asStream, 1]) };
// weights is a function
10.collect { [1, 2, 3, 4].wchoosen({ |list| list.collect { |x| if(x.even) { 1 } { 2 } }  }) };
// weights is nil: behave like choose
10.collect { [1, 2, 3, 4].wchoosen };
```

### `sort`
Sort the contents of the collection using the comparison function argument. The function should take two elements as arguments and return true if the first argument should be sorted before the second argument. If the function is nil, the following default function is used. { |a, b| a <= b }
```supercollider
[6, 2, 1, 7, 5].sort;
[6, 2, 1, 7, 5].sort({ |a, b| a > b }); // reverse sort
```

### `sortBy`
Sort the contents of the collection using the key **key**, which is assumed to be found inside each element of the receiver.
```supercollider
(
a = [
    Dictionary[\a->5, \b->1, \c->62],
    Dictionary[\a->2, \b->9, \c->65],
    Dictionary[\a->8, \b->5, \c->68],
    Dictionary[\a->1, \b->3, \c->61],
    Dictionary[\a->6, \b->7, \c->63]
]
)
a.sortBy(\b);
a.sortBy(\c);
```

### `order`
Return an array of indices that would sort the collection into order. **function** is treated the same way as for the [#-sort](#-sort) method.
```supercollider
[6, 2, 1, 7, 5].order;
```

### `swap`
Swap two elements in the collection at indices **i** and **j**.### `pairsDo`
Calls function for each subsequent pair of elements in the SequentialCollection. The function is passed the two elements and an index.
```supercollider
[1, 2, 3, 4, 5].pairsDo({ |a, b| [a, b].postln });
```

### `doAdjacentPairs`
Calls function for every adjacent pair of elements in the SequenceableCollection. The function is passed the two adjacent elements and an index.
```supercollider
[1, 2, 3, 4, 5].doAdjacentPairs({ |a, b| [a, b].postln });
```

### `separate`
Separates the collection into sub-collections by calling the function for each adjacent pair of elements. If the function returns true, then a separation is made between the elements.
```supercollider
[1, 2, 3, 5, 6, 8, 10].separate({ |a, b| (b - a) > 1 }).postcs;
```

### `clump`
Separates the collection into sub-collections by separating every groupSize elements.
```supercollider
[1, 2, 3, 4, 5, 6, 7, 8].clump(3).postcs;
```

### `clumps`
Separates the collection into sub-collections by separating elements into groupings whose size is given by integers in the groupSizeList.
```supercollider
[1, 2, 3, 4, 5, 6, 7, 8].clumps([1, 2]).postcs;
```

### `curdle`
Separates the collection into sub-collections by randomly separating elements according to the given probability.
```supercollider
[1, 2, 3, 4, 5, 6, 7, 8].curdle(0.3).postcs;
```

### `integrate`
Returns a collection with the incremental sums of all elements.
```supercollider
[3, 4, 1, 1].integrate;
```

### `differentiate`
Returns a collection with the pairwise difference between all elements.
```supercollider
[3, 4, 1, 1].differentiate;
```

### `reduce`
Applies the method named by operator to the first and second elements of the collection, and then applies the method to the result and to the third element of the collection, then applies the method to the result and to the fourth element of the collection, and so on, until the end of the array.If the collection contains only one element, it is returned as the result. If the collection is empty, returns `nil`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `operator` | May be a [Function](../Classes/Function.md) (taking two or three arguments) or a [Symbol](../Classes/Symbol.md) (method selector).
```supercollider
[3, 4, 5, 6].reduce('*'); // this is the same as [3, 4, 5, 6].product
[3, 4, 5, 6].reduce(\lcm); // Lowest common multiple of the whole set of numbers
["d", "e", (0..9), "h"].reduce('++'); // concatenation
[3, 4, 5, 6].reduce({ |a, b| sin(a) * sin(b) }); // product of sines
``` |  
| `adverb` | An optional adverb to be used together with the operator (see [Adverbs](../Reference/Adverbs.md)). If the operator is a functions, the adverb is passed as a third argument.
```supercollider
// compare:
[1, 2] *.x [10, 20, 30]
[[1, 2], [10, 20, 30]].reduce('*', 'x')
[[1, 2], [10, 20, 30], [1000, 2000]].reduce('+', 'x') // but you can combine more
``` |  
### `convertDigits`
Returns an integer resulting from interpreting the elements as digits to a given base (default 10). See also asDigits in [Integer#-asDigits](../Classes/Integer.md#-asdigits) for the complementary method.
```supercollider
[1, 0, 0, 0].convertDigits;
[1, 0, 0, 0].convertDigits(2);
[1, 0, 0, 0].convertDigits(3);
```

### `hammingDistance`
Returns the count of array elements that are not equal in identical positions. [http://en.wikipedia.org/wiki/Hamming_distance](http://en.wikipedia.org/wiki/Hamming_distance)The collections are not wrapped - if one array is shorter than the other, the difference in size should be included in the count.
```supercollider
[0, 0, 0, 1, 1, 1, 0, 1, 0, 0].hammingDistance([0, 0, 1, 1, 0, 0, 0, 0, 1, 1]);
"SuperMan".hammingDistance("SuperCollider");
```


### Fuzzy comparisons
With fuzzy comparisons, the arrays do not need to match exactly. We can check how similar they are, and make decisions based on that. This is the magic behind autocorrection.

### `editDistance`
Returns the minimum number of changes to modify this `SequenceableCollection` into the other `SequenceableCollection`. A change can be: an addition, a deletion, or a substitution. This is known as the Levenshtein Distance and is implemented in SuperCollider using the Wagner–Fischer algorithm.The default comparison uses **identity** - see [Object#-==](../Classes/Object.md#-==) and [Object#-===](../Classes/Object.md#-===)Where both arrays are raw arrays (String, Int16Array, Int32Array, FloatArray etc., or any derived classes), like comparing two strings, a faster primitive will be used to calculate the distance.
```supercollider
"hello".editDistance("hallo"); // 1 (substitution)
"hello".editDistance("hell"); // 1 (deletion)
"hello".editDistance("helloo"); // 1 (addition)
"hello".editDistance("hllo"); // 1 (removal)
"hello".editDistance("haldo"); // 2 (substitutions)
```

In cases where the arrays are of different types, it will fall back to a slower, non-primitive implementation.
```supercollider
// String vs Array
"hello".editDistance([$h, $e, $l, $l, $o]);
```

For cases that require comparisons other than identity, the optional `compareFunc` can be given to compare elements. This function will be passed two arguments, representing a single element from each array to compare, and this function must return a boolean as to whether or not the elements are equal.
```supercollider
// Using compareFunc for case insensitive comparisons
"HeLLO".editDistance("HELLO", { |a, b|
    a.toLower == b.toLower;
});
```


> **Note:** Specifying a `compareFunc` will bypass the primitive and may take significantly longer to execute for larger arrays.

**Arguments:**

| Argument | Description |
|----------|-------------|
| `other` | The `SequenceableCollection` to compare against |  
| `compareFunc` | An optional comparison function to use for each element. It will be provided two arguments, and the function must return a boolean as to whether or not they are the same. Default value is `nil`, which will use **identity** (not equality) to compare elements.
```supercollider
[1, 2, 3, 4].editDistance([2, 3, 4, 5], { |a, b|
    a == b;
});
``` |  

### `similarity`
Returns a value between 0 and 1 representing the percentage similarity between this `SequenceableCollection` and the other `SequenceableCollection`.A value of 1 means they are exactly the same, a value of 0 means they are completely different. This is calculated based on the [#-editDistance](#-editdistance)
```supercollider
"hello".similarity("hello"); // 1
"hello".similarity("asdf"); // 0
"word".similarity("wodr"); // 0.5
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `other` | The `SequenceableCollection` to compare against |  
| `compareFunc` | An optional compareFunc to be used to calculate the edit distance (see [#-editDistance](#-editdistance)) |  




### Math Support - Unary Messages
All of the following messages send the message [#-performUnaryOp](#-performunaryop) to the receiver with the unary message selector as an argument.

### `neg`, `reciprocal`, `bitNot`, `abs`, `asFloat`, `ceil`, `floor`, `frac`, `sign`, `squared`, `cubed`, `sqrt`, `exp`, `midicps`, `cpsmidi`, `midiratio`, `ratiomidi`, `ampdb`, `dbamp`, `octcps`, `cpsoct`, `log`, `log2`, `log10`, `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `sinh`, `cosh`, `tanh`, `rand`, `rand2`, `linrand`, `bilinrand`, `sum3rand`, `distort`, `softclip`, `coin`, `even`, `odd`, `isPositive`, `isNegative`, `isStrictlyPositive`, `real`, `imag`, `magnitude`, `magnitudeApx`, `phase`, `angle`, `rho`, `theta`, `asFloat`, `asInteger`

### `performUnaryOp`
Creates a new collection of the results of applying the selector to all elements in the receiver.
```supercollider
[1, 2, 3, 4].neg;
[1, 2, 3, 4].reciprocal;
```



### Math Support - Binary Messages
All of the following messages send the message [#-performBinaryOp](#-performbinaryop) to the receiver with the binary message selector and the second operand as arguments.

### `+`, `-`, `*`, `/`, `div`, `min`, `max`, `<`, `<=`, `>`, `>=`, `bitXor`, `lcm`, `gcd`, `round`, `trunc`, `atan2`, `hypot`, `ring1`, `ring2`, `ring3`, `ring4`, `difsqr`, `sumsqr`, `sqrdif`, `absdif`, `amclip`, `scaleneg`, `clip2`, `excess`, `rrand`, `exprand`

### `%`, `**`, `&`, `|`, `>>`, `+>>`, `<!`

### `modSeaside`
Pre-3.14 modulo with unexpected behavior for negative integer modulus; see [Integer#-modSeaside](../Classes/Integer.md#-modseaside). Calling `modSeaside` on a non-integer operand will fall back to `mod` behavior; see [Float#-modSeaside](../Classes/Float.md#-modseaside).
### `performBinaryOp`
Creates a new collection of the results of applying the selector with the operand to all elements in the receiver. If the operand is a collection then elements of that collection are paired with elements of the receiver.
```supercollider
([1, 2, 3, 4] * 10);
([1, 2, 3, 4] * [4, 5, 6, 7]);
```



### Math Support - Special Functions
A variety of Special Functions are supplied by the Boost C++ library. The library's [online documentation](http://www.boost.org/doc/libs/1_66_0/libs/math/doc/html/special.html) serves as the primary reference for the following functions. The methods here match closely with those found in the source library, as do argument names.

Below you'll find descriptions of the functions and their bounds, but for visualizing the functions, have a look in [Tour-of-Special-Functions](../Guides/Tour-of-Special-Functions.md).


> **Note:** The following methods are documented slightly clearer in [SimpleNumber#Special Functions](../Classes/SimpleNumber.md#special-functions) using functional notation. As of this writing, a bug in the help file formatting misleadingly documents the methods in receiver notation (methods preceded by `.`), but should be read to suggests the usage: `foo([a], [b])`. The equivalent receiver notation is: `[a].foo([b])`. Note that those methods with only one argument erroneously omit that argument from the argument list; each element in the collection is implicitly passed as the method's argument, e.g. `foo([a])` or `[a].foo`


> **⚠️ Warning:** Many of the functions are only valid in certain numerical ranges. For the most part, error handling happens in the underlying boost functions. While these errors are often obtuse, you'll usually find a useful message at the end of the error regarding proper ranges and the erroneous value supplied. Refer to the online documentation for more detailed descriptions, and the [Tour-of-Special-Functions](../Guides/Tour-of-Special-Functions.md) for plots showing ranges and asymptotes.




























































































































### Multichannel wrappers
All of the following messages are performed on the elements of this collection, using [Object#-multiChannelPerform](../Classes/Object.md#-multichannelperform).

The result depends on the objects in the collection, but the main use case is for [UGen](../Classes/UGen.md)s.

See also [Multichannel-Expansion](../Guides/Multichannel-Expansion.md)

### `clip`, `wrap`, `fold`, `prune`, `linlin`, `linexp`, `explin`, `expexp`, `lincurve`, `curvelin`, `bilin`, `biexp`, `range`, `exprange`, `unipolar`, `bipolar`, `lag`, `lag2`, `lag3`, `lagud`, `lag2ud`, `lag3ud`, `varlag`, `slew`, `blend`, `checkBadValues`
Calls `this.multiChannelPerform(selector, *args)` where selector is the name of the message.
### `multichannelExpandRef`
This method is called internally on inputs to UGens that take multidimensional arrays, like [Klank](../Classes/Klank.md) and it allows proper multichannel expansion even in those cases. For SequenceableCollection, this returns the collection itself, assuming that it contains already a number of Refs. See [Ref](../Classes/Ref.md) for the corresponding method implementation.**Arguments:**

| Argument | Description |
|----------|-------------|
| `rank` | The depth at which the list is expanded. For instance the Klank spec has a rank of 2. For more examples, see [SequenceableCollection#-flopDeep](../Classes/SequenceableCollection.md#-flopdeep)
```supercollider
`([[[100, 200], 500], nil, [[[0.01, 0.3], 0.8]]]).multichannelExpandRef(2);
[`[[100, 200], nil, [0.2, 0.8]], `[[130, 202], nil, [0.2, 0.5]]].multichannelExpandRef(2);
``` |  


### Rhythm-lists
### `convertRhythm`
Convert a rhythm-list to durations.supports a variation of Mikael Laurson's rhythm list RTM-notation.> *see Laurson and Kuuskankare's 2003, "From RTM-notation to ENP-score-notation" [http://jim2003.agglo-montbeliard.fr/articles/laurson.pdf](http://jim2003.agglo-montbeliard.fr/articles/laurson.pdf)*The method converts a collection of the form `[beat-count, [rtm-list], repeats]` to a [List](../Classes/List.md) of [Float](../Classes/Float.md)s. A negative integer within the rtm-list equates to a value tied over to the duration following. The method is recursive in that any subdivision within the rtm-list can itself be a nested convertRhythm collection (see example below). The repeats integer has a default value of 1.If the divisions in the rtm-list are events, the event durations are interpreted as relative durations, and a list of events is returned.
```supercollider
// using numbers as score
[3, [1, 2, 1], 1].convertRhythm; // List[0.75, 1.5, 0.75]
[2, [1, 3, [1, [2, 1, 1, 1]], 1, 3], 1].convertRhythm;
[2, [1, [1, [2, 1, 1, 1]]], 1].convertRhythm;
[2, [1, [1, [2, 1, 1, 1]]], 2].convertRhythm; // repeat
[2, [1, [1, [2, 1, 1, -1]]], 2].convertRhythm; // negative value is tied over.

// sound example
Pbind(\degree, Pseries(0, 1, inf), \dur, Pseq([2, [1, [1, [2, 1, 1, -1]]], 2].convertRhythm)).play;
```



### Starting system processes

### `unixCmd`
Executes a system command **asynchronously**. This object should be an array of strings where the first string is the path to the executable to be run and all other strings are passed as arguments to the executable. This method starts the process directly without using a shell.If you want to run a command using a shell, use [String#-unixCmd](../Classes/String.md#-unixcmd).**Arguments:**

| Argument | Description |
|----------|-------------|
| `action` | A [Function](../Classes/Function.md) that is called when the process has exited. It is passed two arguments: the exit code and pid of the exited process. |  
| `postOutput` | A [Boolean](../Classes/Boolean.md) that controls whether or not the output of the process is displayed in the post window. |  
**Returns:** An [Integer](../Classes/Integer.md) - the pid of the newly created process. Use [Integer#-pidRunning](../Classes/Integer.md#-pidrunning) to test if a process is alive.Example:
```supercollider
["ls", "/"].unixCmd;
```


### `unixCmdGetStdOut`
Similar to [#-unixCmd](#-unixcmd) except that the stdout of the process is returned (**synchronously**) rather than sent to the post window. This object should be an array of strings where the first string is the path to the executable to be run and all other strings are passed as arguments to the executable. This method starts the process directly without using a shell.
```supercollider
~listing = ["ls", "/"].unixCmdGetStdOut; // Grab
~listing.reverse.as(Array).dupEach.join.postln; // Mangle
```





