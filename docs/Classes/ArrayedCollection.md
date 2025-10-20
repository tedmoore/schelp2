# ArrayedCollection

**Categories:** Collections>Ordered

*Abstract superclass of Collections of fixed maximum size*

## Description

`ArrayedCollection` is an abstract class, a subclass of [SequenceableCollection](../Classes/SequenceableCollection.md) whose items are held in a vector of slots, indexable by a [SimpleNumber](../Classes/SimpleNumber.md) starting from 0. If a float is used as index, it will be truncated. Instances of `ArrayedCollection` have a fixed maximum size beyond which they may not grow.
Its principal subclasses are [Array](../Classes/Array.md) (for holding objects), and [RawArray](../Classes/RawArray.md), from which [Int8Array](../Classes/Int8Array.md), [FloatArray](../Classes/FloatArray.md), [Signal](../Classes/Signal.md) etc. inherit.


## Class Methods


### `newClear`
Creates a new instance with **indexedSize** indexable slots. The slots are filled with [Nil](../Classes/Nil.md), zero or something else appropriate to the type of indexable slots in the object.
```
Array.newClear(4).postln;
```



### `with`
Create a new ArrayedCollection whose slots are filled with the given arguments.
```
Array.with(7, 'eight', 9).postln;
```



### `series`
Fill an ArrayedCollection with an arithmetic series.
```
Array.series(5, 10, 2).postln;
```



### `geom`
Fill an ArrayedCollection with a geometric series.
```
Array.geom(5, 1, 3).postln;
```



### `iota`
Fills an ArrayedCollection with a counter. See [J-concepts-in-SC](../Guides/J-concepts-in-SC.md) for more examples.
```
Array.iota(2, 3);
Array.iota(2, 3, 4);
```



## Instance Methods


### `size`
Return the number of elements the ArrayedCollection.
### `maxSize`
Return the maximum number of elements the ArrayedCollection can hold. For example, [Array](../Classes/Array.md)s may initialise themselves with a larger capacity than the number of elements added.
```
[4, 5, 6].maxSize; // gosh
```


### `isRectangular`
Returns true if all nested sub arrays are the same size and all elements have the same depth. This is a requirement of several nested array algorithms and formats, notably multichannel audio files.Example:
```
[1, 2, 3].isRectangular // true
[[1, 2], [3, 4]].isRectangular // true

[1, 2, [3]].isRectangular // false
[[1, 2], [3]].isRectangular // false
[[1, 2], [3, [4, 5]]].isRectangular // false
```


### `at`
Returns the item at `index`, specified as an integer (or float) starting from `0`.
```
x = [1, 2, 3];
x.at(2); // returns 3
x[2];    // equivalent shorthand syntax
```

The `index` can also be an [Array](../Classes/Array.md) of indices to extract specified elements:
```
x = [10, 20, 30];

x.at([-1, 0, 1, 2, 3]); // returns [nil, 10, 20, 30, nil]
x.at((-1..3));          // same, as a range
x[(-1..3)];             // same as above

y = [0, 0, 2, 2, 1];
x[y];                   // returns [10, 10, 30, 30, 20]
```

Float indices are also supported with the following behavior:- Positive float indices are floored to the nearest lower integer.
- Negative float indices in the range (-1, 0) return the first item, `this.at(0)`.
- Out-of-range indices, `<= -1` or `>= this.size`, return `nil`.

```
x = [10, 20];

x.at(-1);   // returns nil
x.at(-0.9); // returns 10
x.at(-0.1); // returns 10
x.at(-0);   // returns 10
x.at(0);    // returns 10
x.at(1.1);  // returns 20
x.at(1.9);  // returns 20
x.at(2);    // returns nil
```

A sound example:
```
(
var pitches =  [43.0, 55.0, 58.86, 57.42, 67.0];
fork {
    pitches.size.do{ |i|
        {
            var freq = pitches[i].midicps;
            var env = Env.perc.ar(Done.freeSelf);
            SinOsc.ar(freq) * 0.1 * env
        }.play;
        0.2.wait
    }
}
)
```


### `clipAt`
Similar to [#-at](#-at), but guarantees that any value for index is valid by clipping values outside the collection's bounds. Values greater than `size - 1` are clipped to that last index, and values below `0` (negative) are clipped to 0. The index can also be an array of indices to extract the specified elements. [SequenceableCollection#-|@|](../Classes/SequenceableCollection.md#-|@|) is its syntactic shortcut.
```
a = [1, 2, 3]
a.clipAt(2) // same as at
a.clipAt(3) // clips
a.clipAt([-1, 3, 1]) // array of indices
a|@|3 //syntactic shortcut
```


### `wrapAt`
Similar to [#-at](#-at), but guarantees that any value for index is valid by wrapping values outside the collection's bounds. If the index exceeds `size - 1`, it wraps back around to `0`. Similarly, if the index is below `0` (negative), it wraps to access elements from the end of the collection. `this.wrapAt(index)` is equivalent to `this.at(index mod: size)`, ensuring the index is always within the valid range of the collection. The index can also be an array of indices to extract the specified elements. [SequenceableCollection#-@@](../Classes/SequenceableCollection.md#-@@) is its syntactic shortcut.
```
a = [1, 2, 3]
a.wrapAt(2) // same as at
a.wrapAt(3) // wraps
a.wrapAt([-1, 3, 1]) // array of indices
a@@3 //syntactic shortcut

(
var pitches =  [43.0, 55.0, 58.86, 57.42, 67.0];
fork {
    32.do{ |i|
        {
            var freq = pitches.wrapAt(i).midicps;
            var env = Env.perc.ar(Done.freeSelf);
            SinOsc.ar(freq) * 0.1 * env
        }.play;
        0.2.wait
    }
}
)
```


### `foldAt`
Similar to [#-at](#-at), but guarantees that any value for index is valid by reflecting values outside the collection's bounds. Values greater than `size - 1` are reflected back toward lower indices. Similarly, if the index is below `0` (negative), it folds in the opposite direction. This creates a symmetrical mapping of any index within the collection's boundaries. The index can also be an array of indices to extract the specified elements. [SequenceableCollection#-@|@](../Classes/SequenceableCollection.md#-@|@) is its syntactic shortcut.
```
a = [1, 2, 3]
a.foldAt(2) // same as at
a.foldAt(3) // folds back
a.foldAt([-1, 3, 1]) // array of indices
a@|@3 //syntactic shortcut

(
var pitches =  [43.0, 55.0, 58.86, 57.42, 67.0];
fork {
    32.do{ |i|
        {
            var freq = pitches.foldAt(i).midicps;
            var env = Env.perc.ar(Done.freeSelf);
            SinOsc.ar(freq) * 0.1 * env
        }.play;
        0.2.wait
    }
}
)
```


### `plot`
Plot values in a GUI window. See [plot](../Reference/plot.md) for more details. When the receiver contains `nil` items, the plot fails with an error.
### `swap`
Swap the values at indices i and j, both specified as integers starting from 0.
```
[1, 2, 3].swap(0, 2).postln;
```


### `put`
Put **item** at **index** starting from 0, replacing what is there. **index** can be an array of indices. If a float is used as index, it will be truncated.Example:
```
x = [1, 2, 3];
y = x.put(0, 150); // -> [150, 2, 3]
z = x.put([0, 1], 150); // [150, 150, 3]
```


### `clipPut`
Same as [#-put](#-put), but values for **index** greater than the [ArrayedCollection](../Classes/ArrayedCollection.md) instance size minus one will be clipped to `size - 1`, which is the last index.
### `wrapPut`
Same as [#-put](#-put), but values for **index** greater than the [ArrayedCollection](../Classes/ArrayedCollection.md) instance size minus one will be wrapped around to 0.
### `foldPut`
Same as [#-put](#-put), but values for **index** greater than the [ArrayedCollection](../Classes/ArrayedCollection.md) instance size minus one will be folded back.
### `putEach`
Put the **values** in the corresponding indices given by **keys**. If one of the two argument arrays is longer then it will wrap.
```
y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
y.putEach([4, 7], [\smelly, \head]);
y.putEach([2, 3, 5, 6], \wotsits);
```


### `indexOf`
Return the first index containing an item which matches **item**. Elements are checked for identity (not for equality).
```
y = [\the, \symbol, \collection, \contains, \my, \symbol];
y.indexOf(\symbol);
```


### `includes`
Return a boolean indicating whether the collection contains anything matching **item**. Elements are checked for identity (not for equality).
```
y = [\the, \symbol, \collection, \contains, \my, \symbol];
y.includes(\symbol);
y.includes(\solipsism);
```


### `indexOfGreaterThan`
Return the first index containing an item which is greater than **item**.
```
y = [10, 5, 77, 55, 12, 123];
y.indexOfGreaterThan(70);
```


### `removeAt`
Remove and return the item at **index**, specified as an integer or a float starting from 0, shrinking the size of the ArrayedCollection.
```
y = [1, 2, 3, 4];

y.removeAt(1);
y.postln; // returns [1, 3, 4]

y.removeAt(0.5)
y.postln; // returns [3, 4]
```


### `takeAt`
Similar to [#-removeAt](#-removeat), but does not maintain the order of the items following the one that was removed. Instead, the last item is placed into the position of the removed item and the array's size decreases by one.
```
y = [1, 2, 3, 4, 5];
y.takeAt(1);
y.postln;
```


### `takeThese`
Removes all items in the receiver for which the **func** answers true. The function is passed two arguments, the item and an integer index. Note that order is not preserved. See [#-takeAt](#-takeat).
```
y = [1, 2, 3, 4];
y.takeThese({ |item, index| item.odd });    // remove odd items
y.postln;
```


### `add`
Adds an item to an ArrayedCollection if there is space. This method may return a new ArrayedCollection. For this reason, you should always assign the result of add to a variable - never depend on `add` changing the receiver.
```
(
// z and y are the same object
var y, z;
z = [1, 2, 3];
y = z.add(4);
z.postln;
y.postln;
)

(
// in this case a new object is returned
var y, z;
z = [1, 2, 3, 4];
y = z.add(5);
z.postln;
y.postln;
)
```


### `addAll`
Adds all the elements of aCollection to the contents of the receiver. This method may return a new ArrayedCollection. For this reason, you should always assign the result of `addAll` to a variable - never depend on add changing the receiver.
```
(
// in this case a new object is returned
var y, z;
z = [1, 2, 3, 4];
y = z.addAll([7, 8, 9]);
z.postln;
y.postln;
)
```


### `extend`
Extends the object to match **size** by adding a number of **item**s. If **size** is less than receiver size then truncate. This method may return a new ArrayedCollection. For this reason, you should always assign the result of `extend` to a variable - never depend on add changing the receiver.
```
(
var y, z;
z = [1, 2, 3, 4];
y = z.extend(10, 9);        // fill up with 9 until the size equals 10
z.postln;
y.postln;
)
```


### `fill`
Inserts the item into the contents of the receiver.
> **Note:** the difference between this and [Collection's *fill](../Classes/Collection.md#*fill).


```
(
var z;
z = [1, 2, 3, 4];
z.fill(4).postln;
z.fill([1, 2, 3, 4]).postln;
)
```


### `insert`
Inserts the item into the contents of the receiver at the specified index, which is an integer starting from 0.  This method may return a new ArrayedCollection.  For this reason, you should always assign the result of `insert` to a variable - never depend on add changing the receiver.
```
// In this case, a new object is returned  
// because adding a new item would exceed the fixed maximum size of 4, 
// which is set at the instantiation of the array z and 
// cannot be changed at a later stage.
// (By default, an array initialized with a size between 1 and 4 
// retains a maximum size of 4):
z = [1, 2, 3, 4]; // -> [1, 2, 3, 4]
y = z.insert(1, 999); // -> [1, 999, 2, 3, 4]
z // -> [1, 2, 3, 4]
y // -> [1, 999, 2, 3, 4]
(z == y) // -> false
(z === y) // -> false

// In this case, the same object is returned 
// because the new number of elements does not exceed 
// the number of elements at instantiation:
z = [1, 2, 3]; // -> [1, 2, 3]
y = z.insert(1, 999); // -> [1, 999, 2, 3]
z; // -> [1, 999, 2, 3]
y; // -> [1, 999, 2, 3]
(z == y); // -> true
(z === y); // -> true
```


### `boundedInsert`
Changes the receiver but maintains its size, therefore unlike `.insert` it is not necessary to reassign the result of `.boundedInsert`.
```
// .boundedInsert never returns a new object  
// because inserting a new item never exceeds the maxSize.  
z = [1, 2, 3, 4];            // -> [1, 2, 3, 4]
y = z.boundedInsert(1, 999); // -> [1, 999, 2, 3]
z;                           // -> [1, 999, 2, 3]
y;                           // -> [1, 999, 2, 3]
z == y;                      // -> true
(z === y);                   // -> true
y = y.boundedInsert(20, \a); // -> [1, 999, 2, a]
z = z.boundedInsert(-2, \b); // -> [b, 1, 999, 2]
```


### `move`
Moves an item from one position to another. – Both `fromIndex` and `toIndex` arguments are specified as integers starting from 0.
```
[10, 20, 1000, 40, 50].move(2, 0) // move 1000 to index 0
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `fromIndex` | The position in the array from which the element is removed. |  
| `toIndex` | The position in the array before which the element is inserted again. |  

### `addFirst`
Inserts the item before the contents of the receiver, possibly returning a new collection.
```
(
// in this case a new object is returned
var y, z;
z = [1, 2, 3, 4];
y = z.addFirst(999);
z.postln;
y.postln;
)
```


### `pop`
Remove and return the last element of the ArrayedCollection.
```
(
var z;
z = [1, 2, 3, 4];
z.pop.postln;
z.postln;
)
```


### `grow`
Increase the size of the ArrayedCollection by **sizeIncrease** number of slots, possibly returning a new collection.
### `growClear`
Increase the size of the ArrayedCollection by **sizeIncrease** number of slots, returning a new collection with [Nil](../Classes/Nil.md)s in the added slots.
```
// Compare:
[4, 5, 6].grow(5);
[4, 5, 6].growClear(5);
```


### `copyRange`
Return a new [ArrayedCollection](../Classes/ArrayedCollection.md) which is a copy of the indexed slots of the receiver from **start** to **end**. – Both start and end are specified as integers starting from 0. If **end** < **start**, an empty ArrayedCollection is returned.
```
(
var x, y;
x = [1, 2, 3, 4, 5];
y = x.copyRange(1, 3);
x.postln;
y.postln;
)
```

> **⚠️ Warning:** `x.copyRange(a, b)` is **not** equivalent to `x[a..b]`. The latter compiles to [#-copySeries](#-copyseries), which has different behavior when **end** < **start**. See [NOTE](#copyrange_copyseries) in [#-copySeries](#-copyseries).
### `copySeries`
Return a new [ArrayedCollection](../Classes/ArrayedCollection.md) consisting of the values starting at **first**, then every step of the distance between **first** and **second**, up until **last**. – All indices (first, second, last) are specified as integers starting from 0. If **second** is `nil`, a step of 1 or -1 is used as appropriate.`x.copySeries(a, nil, c)` is equivalent to `x[a..c]`, and `x.copySeries(a, b, c)` is equivalent to `x[a, b..c]`
```
(
var x, y;
x = [1, 2, 3, 4, 5, 6];
y = x.copySeries(0, 2, 5);
x.postln;
y.postln;
)
```


> **Note:** <a id="copyRange_copySeries"></a>If the intent is to copy *forward*, and you are calculating start and end indices such that `end` may be less than `start`, `copyRange` is not recommended. In this case, `copySeries` or the shortcut syntax `x[a..b]` is recommended because it will adapt to use a positive or negative step as needed.
```
a = Array.series(10, 0, 1);

/* case 1 */
a[0..2];  // [0, 1, 2]
a.copySeries(0, 1, 2);  // [0, 1, 2]
a.copySeries(0, nil, 2);  // [0, 1, 2]
a.copyRange(0, 2);  // [0, 1, 2]

/* case 2 */
a[2..0];  // [2, 1, 0]
a.copySeries(2, 1, 0);  // [2, 1, 0]
a.copySeries(2, nil, 0);  // [2, 1, 0]
a.copyRange(2, 0);  // []
```


### `seriesFill`
Fill the receiver with an arithmetic progression. The first element will be **start**, the second **start + step**, the third **start + step + step** ...
```
(
var y;
y = Array.newClear(15);
y.seriesFill(5, 3);
y.postln;
)
```


### `putSeries`
Put **value** at every index starting at **first**, then every step of the distance between **first** and **second**, up until **last**. – All indices (first, second, last) are specified as integers starting from 0. `x.putSeries(a, b, c, val)` can also be written as `x[a, b..c] = val`
```
(
var y, z;
z = [1, 2, 3, 4, 5, 6];
y = z.putSeries(0, 2, 5, "foo");
y.postln;
)
```


### `++`
Concatenate the contents of the two collections into a new ArrayedCollection.
```
(
var y, z;
z = [1, 2, 3, 4];
y = z ++ [7, 8, 9];
z.postln;
y.postln;
)
```


### `reverse`
Return a new ArrayedCollection whose elements are reversed.
```
(
var y, z;
z = [1, 2, 3, 4];
y = z.reverse;
z.postln;
y.postln;
)
```


### `do`
Iterate over the elements in order, calling the function for each element. The function is passed two arguments, the element and an index.
```
['a', 'b', 'c'].do({ |item, i| [i, item].postln });
```


### `reverseDo`
Iterate over the elements in reverse order, calling the function for each element. The function is passed two arguments, the element and an index.
```
['a', 'b', 'c'].reverseDo({ |item, i| [i, item].postln });
```


### `collect`
Answer a new collection which consists of the results of function evaluated for each item in the collection. The function is passed two arguments, the item and an integer index. See [Collection](../Classes/Collection.md) helpfile for examples.
### `deepCollect`
The same as [#-collect](#-collect), but can look inside sub-arrays up to the specified **depth**.
```
a = [99, [4, 6, 5], [[32]]];
a.deepCollect(1, { |item| item.isArray }).postln;
a.deepCollect(2, { |item| item.isArray }).postln;
a.deepCollect(3, { |item| item.isArray }).postln;
```


### `windex`
Interprets the array as a list of probabilities which should sum to 1.0 and returns a random index value based on those probabilities. The random index is taken from the receiver's index, starting from 0.
```
(
Array.fill(10, {
    [0.1, 0.6, 0.3].windex;
}).postln;
)
```


### `normalizeSum`
Returns the Array resulting from :
```
(this / this.sum)
```

so that the array will sum to 1.0.This is useful for using with windex or wchoose.
```
[1, 2, 3].normalizeSum.postln;
```


### `normalize`
Returns a new Array with the receiver items normalized between **min** and **max**.
```
[1, 2, 3].normalize;            // default min = 0, max = 1
[1, 2, 3].normalize(-20, 10);
```


### `perfectShuffle`
Returns a copy of the receiver with its items split into two equal halves, then reconstructed by interleaving the two halves.
> **Note:** the size of the collection should be even, otherwise the item directly in the middle of the collection will be lost in the shuffle.


```
(
var y, z;
z = [1, 2, 3, 4, 5, 6];
y = z.perfectShuffle;
z.postln;
y.postln;
)
```


### `performInPlace`
Performs a method in place, within a certain region [from..to], returning the same array.
```
a = (0..10);
a.performInPlace(\normalizeSum, 3, 6);
```


### `rank`
Returns the number of dimensions of the collection. `rank` inspects the size of the left-most elements of sub-arrays only, i.e. it's assumed that the collection [#-isRectangular](#-isrectangular), so subarrays of mismatched sizes may not return an expected result. A single value has a rank of `0`. An empty array has a rank of `1`.
```
0.rank // 0
[].rank // 1
[4, 7, 6, 8].rank // 1
[[4, 7], [6, 8]].rank // 2
[1 ,2, [3, 4]].rank // 1, this array is not rectangular and returns a meaningless value.
```


### `shape`
Returns an array describing the dimension of each nested array. Requires [#-isRectangular](#-isrectangular) as a precondition.
```
[4, 7, 6, 8].shape // [4]
[[4, 7], [6, 8]].shape // [2, 2]
[[[4, 7]], [[6, 8]]].shape // [2, 1, 2]
[1, 2, [3, 4]].shape // [3], this array is not rectangular and returns a meaningless value.
```


### `reshape`
For a multidimensional array, rearranges the data using the desired number of elements along each dimension. The data may be extended using [Array#-wrapExtend](../Classes/Array.md#-wrapextend) if needed. This will always return a rectangular array, see [#-isRectangular](#-isrectangular).
```
a = [4, 7, 6, 8];
a.reshape(2, 2);
a.reshape(2, 3);
```


### `find`
Finds the starting index of a number of elements contained in the array. This method expects a collection as an argument. So for finding only one element, have a look at [SequenceableCollection#-indexOfEqual](../Classes/SequenceableCollection.md#-indexofequal). Elements are checked for equality (not for identity).
```
a = (0..10);
a.find([4, 5, 6]);
```


### `replace`
Return a new array in which a number of elements have been replaced by another. Elements are checked for equality (not for identity).
```
a = (0..10) ++ (0..10);
a.replace([4, 5, 6], 100);
a.replace([4, 5, 6], [1734, 1985, 1860]);
```

this method is inherited by [String](../Classes/String.md) :
```
a = "hello world";
a.replace("world", "word");
```


### `asRandomTable`
Return an integral table that can be used to generate random numbers with a specified distribution. (see [Randomness](../Guides/Randomness.md) helpfile for a more detailed example)
```
(
a = (0..100) ++ (100..50) / 100; // distribution
a = a.asRandomTable;
)
```


### `tableRand`
Returns a new random number from a random table.
```
(
a = (0..100) ++ (100..50) / 100; // distribution
a = a.asRandomTable;
20.do { a.tableRand.postln };
)
```


### `msgSize`
Return the size of an osc message in bytes
```
a = ["/s_new", "default", -1, "freq", 440];
a.msgSize;
```


### `bundleSize`
Return the size of an osc bundle in bytes
```
a = [["/s_new", "default", -1, "freq", 440], ["/s_new", "default", -1, "freq", 220]];
a.bundleSize;
```


### `asciiPlot`
For an ArrayedCollection containing numbers (e.g. audio data) this renders a plot in the post window using asterisks and spaces (works best if you use a monospace font in your post window).
```
a = (0, pi/10 .. 5pi).collect{ |val| val.sin };
a.asciiPlot;
```



