# Collection

*Abstract superclass of all collections*

**Related:** [List](../Classes/List.md), [Array](../Classes/Array.md), [Dictionary](../Classes/Dictionary.md), [Bag](../Classes/Bag.md), [Set](../Classes/Set.md), [SortedList](../Classes/SortedList.md)

**Categories:** Collections

## Description

Collection is an abstract class. You do not create direct instances of Collection. There are many types of Collections including [List](../Classes/List.md), [Array](../Classes/Array.md), [Dictionary](../Classes/Dictionary.md), [Bag](../Classes/Bag.md), [Set](../Classes/Set.md), [SortedList](../Classes/SortedList.md), etc. See [Collections](../Overviews/Collections.md) for a complete class tree.


## Class Methods


### `newFrom`
Creates a new Collection from another collection. This supports the interface for the method "as".
```
Array.newFrom(Set[4, 2, 1]);
Set.newFrom(Array[4, 2, 1]);
[1, 2, 3, 4, 3, 2].as(Set); // as(someClass) calls someClass.newFrom(this)
```



### `with`
Creates a new Collection from the args.
```
Array.with(4, 2, 1);
```



### `fill`
Creates a Collection of the given size, the elements of which are determined by evaluation the given function. The function is passed the index as an argument.
```
Array.fill(4, { |i| i * 2 });
Bag.fill(14, { |i| i.rand });
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `size` | The size of the collection which is returned. If nil, it returns an empty collection. If an array of sizes is given, the resulting collection has the appropriate dimensions (see: [#*fillND).](#*fillnd).)
```
Array.fill([2, 2, 3], { |i, j, k|  i * 100 + (j * 10) + k });
``` |  
| `function` | The function which is called for each new element - the index is passed in as a first argument. The function be anything that responds to the message "value".
```
Array.fill(10, { |i| 2 ** i });
Array.fill(10, Pxrand([0, 1, 2], inf).iter);
Array.fill(10, 7); // an object that doesn't respond with a new value is just repeatedly added.
``` |  


### `fill2D`
Creates a 2 dimensional Collection of the given sizes. The items are determined by evaluation of the supplied function. The function is passed row and column indexes as arguments. See [J-concepts-in-SC](../Guides/J-concepts-in-SC.md)
```
Array.fill2D(2, 4, 0);
Array.fill2D(3, 4, { |r, c| r*c+c });
```



### `fill3D`
Creates a 3 dimensional Collection of the given sizes. The items are determined by evaluation of the supplied function. The function is passed plane, row and column indexes as arguments. See [J-concepts-in-SC](../Guides/J-concepts-in-SC.md)
```
Array.fill3D(2, 3, 4, { |p, r, c| p });
```



### `fillND`
Creates a N dimensional Collection where N is the size of the array **dimensions**. The items are determined by evaluation of the supplied function. The function is passed N number of indexes as arguments. See [J-concepts-in-SC](../Guides/J-concepts-in-SC.md)
```
Array.fillND([4, 4], { |a, b| a+b });                // 2D
Array.fillND([4, 4, 4], { |a, b, c| a+b*c });        // 3D
Array.fillND([1, 2, 3, 4], { |a, b, c, d| b+d });    // 4D
```



## Instance Methods


### Accessing

### `size`
Answers the number of objects contained in the Collection.
```
List[1, 2, 3, 4].size;
```



### `isEmpty`
Answer whether the receiver contains no objects.
```
List[].isEmpty;
```



### Adding and Removing

### `add`
Add anObject to the receiver.
```
List[1, 2].add(3);
```



### `addAll`
Add all items in aCollection to the receiver.
```
List[1, 2].addAll(List[3, 4]);
```



### `remove`
Remove anObject from the receiver. Answers the removed object.
```
(
var a;
a = List[1, 2, 3, 4];
a.remove(3);
a;
)
```



### `removeAll`
Remove all items in aCollection from the receiver.
```
List[1, 2, 3, 4].removeAll(List[2, 3]);
```


> **Note:** that multiple items in the receiver will not necessarily be removed
```
~closet = [\hat, \hat, \hat, \coat, \coat, \shoe, \shoe];
~closet.removeAll([\hat, \coat, \shoe, \shoe]); // Doesn't empty the closet, just removes what we wanted to
```

See [#-removeEvery](#-removeevery) for a related method that removes all occurrences.



### `removeEvery`
Remove all occurrences of the items in aCollection from the receiver.
```
List[1, 2, 3, 2, 3, 2, 3, 4].removeEvery(List[2, 3]);
```



### `removeAllSuchThat`
Remove all items in the receiver for which function answers [True](../Classes/True.md). The function is passed two arguments, the item and an integer index. Answers the objects which have been removed.
```
(
var a;
a = List[1, 2, 3, 4];
a.removeAllSuchThat({ |item, i| item < 3 });
a;
)
```



### `putEach`
Put the values in the corresponding indices given by keys. If one of the two argument arrays is longer then it will wrap.
```
y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
y.putEach([4, 7], [\smelly, \head]);
y.putEach([2, 3, 5, 6], \wotsits);
```



### `atAll`
Return a collection of all the items for the keys.
```
y = [\a, \b, \c];
y.atAll([0, 2]);
```



### Testing

### `includes`
Answer whether anObject is contained in the receiver.
```
List[1, 2, 3, 4].includes(3);
```



### `includesEqual`
Answer whether anObject is contained in the receiver. In contrast to [#-includes](#-includes) this tests for equality - not identity.
```
List["a", "b", "c"].includesEqual("c");  // true
List["a", "b", "c"].includes("c");       // false
List[List[1, 2], List[3, 4]].includesEqual(List[3, 4]);  // true
List[List[1, 2], List[3, 4]].includes(List[3, 4]);       // false
```



### `includesAny`
Answer whether any item in aCollection is contained in the receiver.
```
List[1, 2, 3, 4].includesAny(List[4, 5]);
```



### `includesAll`
Answer whether all items in aCollection are contained in the receiver.
```
List[1, 2, 3, 4].includesAll(List[4, 5]);
```



### `matchItem`
Returns [True](../Classes/True.md) if this includes the **item**.See also [matchItem](../Reference/matchItem.md).

### Iteration

### `do`
Evaluates **function** for each item in the collection. The function is passed two arguments, the item and an integer index.
```
List[1, 2, 3, 4].do({ |item, i| item.postln });
```



### `collect`
Answer a new collection which consists of the results of **function** evaluated for each item in the collection. The function is passed two arguments, the item and an integer index.
```
List[1, 2, 3, 4].collect({ |item, i| item + 10 });
```

If you want to control what type of collection is returned, use [#-collectAs](#-collectas)(function, class).

### `select`
Answer a new collection which consists of all items in the receiver for which **function** answers [True](../Classes/True.md). The function is passed two arguments, the item and an integer index.
```
List[1, 2, 3, 4].select({ |item, i| item.even });
```

If you want to control what type of collection is returned, use [#-selectAs](#-selectas)(function, class).

### `reject`
Answer a new collection which consists of all items in the receiver for which **function** answers [False](../Classes/False.md). The function is passed two arguments, the item and an integer index.
```
List[1, 2, 3, 4].reject({ |item, i| item.even });
```

If you want to control what type of collection is returned, use [#-rejectAs](#-rejectas)(function, class).

### `detect`
Answer the first item in the receiver for which **function** answers [True](../Classes/True.md). The function is passed two arguments, the item and an integer index.
```
List[1, 2, 3, 4].detect({ |item, i| item.even });
```



### `detectLast`
Similar to [#-detect](#-detect), but performed in reverse order.
```
[2, 3, 4, 6, 8, 9, 10].detectLast({ arg item; item.odd }); // 9
["a", "b", "c"].detectLast({ arg item; item == "d" }); // nil
```



### `detectIndex`
Similar to [#-detect](#-detect) but returns the index instead of the item itself.
```
List[1, 2, 3, 4].detectIndex({ |item, i| item.even });
```



### `detectLastIndex`
Similar to [#-detectIndex](#-detectindex), but performed in reverse order.
```
[0, 1, 2, 3, 4].detectLastIndex({ arg item; item.odd }); // 3
["a", "b", "c"].detectLastIndex({ arg item; item == 0 }); // nil
```



### `lastForWhich`
Returns the last element of the collection for which the function is true. Synonym to [#-detectLast](#-detectlast).

### `lastIndexForWhich`
Returns the index of the last element of the collection for which the function is true. Synonym to [#-detectLastIndex](#-detectlastindex).

### `inject`
In functional programming, the operation known as a left fold. inject takes an initial value and a function and combines the elements of the collection by applying the function to the accumulated value and an element from the collection starting from the first element in the collection. The **function** takes two arguments and returns the new value. The accumulated value is initialized to **initialValue**.
```
[1, 2, 3, 4, 5].inject(0, _+_); // 15

[1, 2, 3, 4, 5].inject(1, _*_); // 120

// same as .collect(_.squared)
[1, 2, 3, 4, 5].inject([], { |a, b| a ++ b.squared }); // [1, 4, 9, 16, 25]
[1, 2, 3, 4, 5].inject([], { |a, b| [b] ++ a ++ [b] }); // [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
[1, 2, 3, 4, 5].inject([], { |a, b| a ++ b ++ a });
[1, 2, 3, 4, 5].inject([], { |a, b| a ++ a ++ b });
```



### `injectr`
In functional programming, the operation known as a right fold. inject takes an initial value and a function and combines the elements of the collection by applying the function to the accumulated value and an element from the collection starting from the last element in the collection. The **function** takes two arguments and returns the new value. The accumulated value is initialized to **initialValue**.
```
[1, 2, 3, 4, 5].injectr([], _++_); // [5, 4, 3, 2, 1]

[1, 2, 3, 4, 5].inject([], _++_); // [1, 2, 3, 4, 5]
```



### `collectInPlace`
Iterate over the collection and replace each item with a new one, returned by the function. This can be useful when one wants to aviod creating a new array in memory. In most cases, it is better to use [#-collect](#-collect).
```
a = [1, 5, 3, 4];
a.collectInPlace { |x| 2 ** x };
a; // changed

// compare:
a = [1, 5, 3, 4];
a.collect { |x| 2 ** x };
a; // remains unchanged
```



### `collectCopy`
Like [#-collect](#-collect), but the collection is copied before iteration. This is recommended wherever the function may change the collection itself.
```
a = [1, 5, 2, 3, 4];
b = a.collectCopy { |x| if(x.even) { a.remove(x); "removed" } { x } };
a;
b;
```



### `any`
Answer whether **function** answers [True](../Classes/True.md) for any item in the receiver. The function is passed two arguments, the item and an integer index.
```
List[1, 2, 3, 4].any({ |item, i| item.even });
```



### `every`
Answer whether **function** answers [True](../Classes/True.md) for every item in the receiver. The function is passed two arguments, the item and an integer index.
```
List[1, 2, 3, 4].every({ |item, i| item.even });
```



### `count`
Answer the number of items for which **function** answers [True](../Classes/True.md). The function is passed two arguments, the item and an integer index.
```
List[1, 2, 3, 4].count({ |item, i| item.even });
```



### `occurrencesOf`
Answer the number of items in the receiver which are equal to anObject.
```
List[1, 2, 3, 3, 4, 3, 4, 3].occurrencesOf(3);
```



### `sum`
Answer the sum of the items in the collection.
```
[3, 6, 12, 24].sum // -> 45
```

This can be represented as:Optionally, a [Function](../Classes/Function.md) can be provided to be applied to each item in the collection before summing.**Arguments:**

| Argument | Description |
|----------|-------------|
| `function` | If provided, the [Function](../Classes/Function.md) is passed two arguments: the item and the iteration index.
```
[3, 6, 12, 24].sum { |item, i| i / (2 ** item) } // -> 0.016113460063934
```

The above code can be represented as:where $x_i$ is the function argument `item`. |  


### `product`
Answer the product of the items in the collection.
```
[3, 6, 12, 24].product // -> 5184
```

This can be represented as:Optionally, a [Function](../Classes/Function.md) can be provided to be applied to each item in the collection before multiplication.**Arguments:**

| Argument | Description |
|----------|-------------|
| `function` | If provided, the [Function](../Classes/Function.md) is passed two arguments: the item and the iteration index.
```
[3, 6, 12, 24].product { |item, i| item.sqrt ** i } // -> 3456.0
```

The above code can be represented as:where $x_i$ is the function argument `item`. |  


### `mean`
Answer the arithmetic mean of the items in the collection.
```
[3, 6, 12, 24].mean // -> 11.25
```

This can be represented as:Optionally, a [Function](../Classes/Function.md) can be provided to be applied to each item in the collection before multiplication.**Arguments:**

| Argument | Description |
|----------|-------------|
| `function` | If provided, the [Function](../Classes/Function.md) is passed two arguments: the item and the iteration index.
```
[3, 6, 12, 24].mean { |item, i| i / (item ** 2) } // -> 0.01171875
```

The above code can be represented as:where $x_i$ is the function argument `item`. |  


### `maxItem`
Answer the maximum of the results of **function** evaluated for each item in the receiver. The function is passed two arguments, the item and an integer index. If function is nil, then answer the maximum of all items in the receiver.
```
List[1, 2, 3, 4].maxItem({ |item, i| item + 10 });
```



### `minItem`
Answer the minimum of the results of **function** evaluated for each item in the receiver. The function is passed two arguments, the item and an integer index. If function is nil, then answer the minimum of all items in the receiver.
```
List[1, 2, 3, 4].minItem({ |item, i| item + 10 });
```



### `maxIndex`
Answer the index of the maximum of the results of **function** evaluated for each item in the receiver. The function is passed two arguments, the item and an integer index. If function is nil, then answer the maximum of all items in the receiver.
```
List[1, 2, 3, 4].maxIndex({ |item, i| item + 10 });
[3.2, 12.2, 13, 0.4].maxIndex;
```



### `minIndex`
Answer the index of the minimum of the results of **function** evaluated for each item in the receiver. The function is passed two arguments, the item and an integer index. If function is nil, then answer the minimum of all items in the receiver.
```
List[1, 2, 3, 4].minIndex({ |item, i| item + 10 });
List[3.2, 12.2, 13, 0.4].minIndex;
```



### `maxSizeAtDepth`
Returns the maximum size of all subcollections at a certain depth (dimension)**Arguments:**

| Argument | Description |
|----------|-------------|
| `rank` | The depth at which the size of the collection is measured
```
Set[Set[1, 2, 3], [Set[41, 52], 5, 6], 1, 2, 3].maxSizeAtDepth(2);
Set[Set[1, 2, 3], [Set[41, 52], 5, 6], 1, 2, 3].maxSizeAtDepth(1);
Set[Set[1, 2, 3], [Set[41, 52], 5, 6], 1, 2, 3].maxSizeAtDepth(0);
Set[].maxSizeAtDepth(0);
Set[[]].maxSizeAtDepth(0);
Set[[]].maxSizeAtDepth(1);
``` |  


### `maxDepth`
Returns the maximum depth of all subcollections.**Arguments:**

| Argument | Description |
|----------|-------------|
| `max` | Internally used only.
```
Set[Set[1, 2, 3], Set[Set[41, 52], 5, 6], 1, 2, 3].maxDepth
``` |  


### `iter`
Returns a [Routine](../Classes/Routine.md) that returns the elements one by one.
```
r = Set[10, 2, -3, -4].iter;
r.next;
r.next;
r.next;
r.next; // nil.
```



### Conversion

### `asBag`
Answer a [Bag](../Classes/Bag.md) to which all items in the receiver have been added.
```
List[1, 2, 3, 4].asBag;
```



### `asList`
Answer a [List](../Classes/List.md) to which all items in the receiver have been added.
```
Set[1, 2, 3, 4].asList;
```



### `asSet`
Answer a [Set](../Classes/Set.md) to which all items in the receiver have been added.
```
List[1, 2, 3, 4].asSet;
```



### `asSortedList`
Answer a [SortedList](../Classes/SortedList.md) to which all items in the receiver have been added.
```
List[2, 1, 4, 3].asSortedList;
```



### `asDict`
Answer a corresponding dictionary. This is part of the [Key-Value-Pairs](../Reference/Key-Value-Pairs.md) interface.**Arguments:**

| Argument | Description |
|----------|-------------|
| `mergeFunc` | Use this function to decide what to do with duplicate keys. |  
| `class` | The class of the dictionary to be returned. By default this is an [IdentityDictionary](../Classes/IdentityDictionary.md). |  


### `asAssociations`
Answer an array of [Association](../Classes/Association.md)s. If the first item of the list is already an associiation, return itself. This is part of the [Key-Value-Pairs](../Reference/Key-Value-Pairs.md) interface.**Arguments:**

| Argument | Description |
|----------|-------------|
| `class` | The class of the collection to be returned. By default this is an [Array](../Classes/Array.md). |  


### `asPairs`
Answer an array with alternating key value pairs, like `[\freq, 1848, \amp, 0.2]`. This is part of the [Key-Value-Pairs](../Reference/Key-Value-Pairs.md) interface.**Arguments:**

| Argument | Description |
|----------|-------------|
| `class` | The class of the collection to be returned. By default this is an [Array](../Classes/Array.md). |  


### `asEvent`
Answer an [Event](../Classes/Event.md): with the key value pairs. See [Key-Value-Pairs](../Reference/Key-Value-Pairs.md).

### `asDictWith`
used internally by `asDict`.

### `powerset`
Returns all possible combinations of the collection's elements.
```
Set[1, 2, 3].powerset;

// generate the von neumann ordinals. (warning: only count to four at maximum!)
a = Set[];
a = a.powerset;
a = a.powerset;
a = a.powerset;

u = { |set| set.unify }; // union (count down)
n = { |set| set.powerset }; // powerset (count up)
a = Set[]; // empty set (zero)
n.(n.(a)); // two
u.(n.(n.(a))) == n.(a); // two - one == one
u.(u.(n.(n.(a)))) == u.(n.(a)); // two - two == one - one
```



### `flopDict`
Takes a collection of dictionaries and returns a single dictionary with arrays of all dictionaries' elements. If unbubble is [True](../Classes/True.md) (default), and if one element is singular, the array is replaced by this element.
```
[(degree: 7, x: 4), (degree: 8, x: 5), (degree: -2, dur: 2.5)].flopDict;
[(degree: 7, x: 4), (degree: 8, x: 5), (degree: -2, dur: 2.5)].flopDict(false);
```



### `histo`
Returns a histogram of the collection by counting the number of values that fall into each of the **steps** subdivisions (default: 100) between **min** and **max**. If not provided, **min** and **max** default to the smallest and largest value in the collection, respectively. If there are any values outside this range, it posts a note.See also: [Collection#-plotHisto](../Classes/Collection.md#-plothisto).
```
{ 1.0.linrand }.dup(10000).histo(1000).plot(discrete: true);
```


```
(
var data, steps = 15;
var minmax, range, binwidth;

data = { 15.0.rand + 3 }.dup(100);
minmax = [data.minItem, data.maxItem];
range = minmax[1] - minmax[0];
binwidth = range / steps;

data.histo(steps).plot(minval: 0)
.plotMode_(\steps)
.axisLabelY_("Occurrences")
.axisLabelX_("Bins")
.domainSpecs_(minmax.asSpec)
.domain_(binwidth * (0..steps-1) + data.minItem)
;
)
// or use Collection:-plotHisto for convenience
{ 15.0.rand + 3 }.dup(100).plotHisto(15);
```



### `invert`
Subtractively invert a collection about a value (default: sum of minimal and maximum value). It can be used to invert a pitch list about a given axis.
```
[0, 1, 4, 7].invert(0);
[0, 1, 2, 3].invert(1);
[3, 2, 9, 7].invert(11); // becomes [19, 20, 13, 15]
// if axis is nil, invert uses the registral center
[3, 2, 9, 7].invert; // becomes [8, 9, 2, 4]
// invert chords
[[0, 5, 7], [5, 7, 11], [6, 7, 9]].invert(5);
```



### Writing to streams

### `printOn`
Print a representation of the collection to a stream.

### `storeOn`
Write a compilable representation of the collection to a stream.

### `printItemsOn`
Print a comma separated compilable representation of the items in the collection to a stream.

### `storeItemsOn`
Write a comma separated compilable representation of the items in the collection to a stream.

### Set specific operations

### `sect`
Return the set theoretical intersection of this and **that**.
```
a = [1, 2, 3]; b = [2, 3, 4, 5];
sect(a, b);
```



### `union`
Return the set theoretical union of this and **that**.
```
a = [1, 2, 3]; b = [2, 3, 4, 5];
union(a, b);
```



### `difference`
Return the set of all items which are elements of this, but not of **that**.
```
a = [1, 2, 3]; b = [2, 3, 4, 5];
difference(a, b);
```



### `symmetricDifference`
Return the set of all items which are not elements of both this and **that**. this -- that
```
a = [1, 2, 3]; b = [2, 3, 4, 5];
symmetricDifference(a, b);
```



### `isSubsetOf`
Returns [True](../Classes/True.md) if all elements of this are also elements of **that**
```
a = [1, 2, 3, 4];
// a = List[1, 2, 3, 4];
// a = Set[1, 2, 3, 4];
// a = Interval(1, 4, 1);
// a = Bag[1, 2, 3, 4];
[1, 3].isSubsetOf(a); // true
[1, 5].isSubsetOf(a); // false
```

In mathematical notation, the last two lines of the above code are the equivalent to


