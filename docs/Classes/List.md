# List

*list of items of variable size*

**Related:** [Array](../Classes/Array.md)

**Categories:** Collections>Ordered

## Description

List is a subclass of SequenceableCollection with unlimited growth in size. Although not a subclass of [Array](../Classes/Array.md) or its superclass [ArrayedCollection](../Classes/ArrayedCollection.md) it uses an Array in its implementation and is in many cases interchangeable with one. (List implements many of the same methods as Array.)
Many of List's methods are inherited from [SequenceableCollection](../Classes/SequenceableCollection.md) or [Collection](../Classes/Collection.md) and are documented in those helpfiles.

### Size limitations of arrays and flexibility of lists in SuperCollider
Arrays have a fixed maximum size. Adding beyond that size, a new [Array](../Classes/Array.md) is created and returned. In order to be able to use it, the variable holding the old array can be reassigned to the new one. Threfore, the idiomatic way to add new item in [Array](../Classes/Array.md) is:


```supercollider
x = x.add(i);
```


Example:


```supercollider
// Create a new empty collections with size 3:
x = Array.new(3); 
y = Array.new(3); 
z = List.new(3);

// Try to add 7 items to the array and list.
// If the array exceeds maxSize, it will only
// grow to an internally specified max size.
( 
7.do { |i|
    x.add(i);
    y = y.add(i); // reassign array y on each add
    z.add(i);
};
)

// Attempt to access the 5th item:
x.at(4); // -> nil (out of bounds)
y.at(4); // -> 4
z.at(4); // -> 4

// x grew only to size 4
x.postln; // -> [ 0, 1, 2, 3 ]
y.postln; // -> [ 0, 1, 2, 3, 4, 5, 6 ]
z.postln; // -> List[ 0, 1, 2, 3, 4, 5, 6 ]
```


List has no size limitation and is thus more flexible, but has slightly more overhead:


```supercollider
(
// Create a new empty List with size: 3
x = List.new(3);

x.postln; // -> List[ ]

// Add numbers 0 to 4 to the List
5.do({ |i| x.add(i) });

// The list has been modified in-place with each added item
x.postln; // -> List[ 0, 1, 2, 3, 4 ]
)
```





## Class Methods

### `new`
Creates a List with the initial capacity given by **size**.
### `newClear`
Creates a List with the initial capacity given by **size** and slots filled with nil.
### `copyInstance`
Creates a List by copying **aList**'s array variable.
### `newUsing`
Creates a List using **anArray**.

## Instance Methods

### `asArray`
Returns a new [Array](../Classes/Array.md) based upon this List.### `array`
Returns the List's Array, allowing it to be manipulated directly. This should only be necessary for exotic manipulations not implemented in List or its superclasses.
```supercollider
(
x = List[1, 2, 3];
x.array.add("foo");
x.postln;
)
```

### `array`
Sets the List's Array.### `at`
Return the item at **index**. See [SequenceableCollection#Indexing](../Classes/SequenceableCollection.md#indexing).. Accepts either a single index or an array of indices, in which case an Array of elements is returned. [Array](../Classes/Array.md) is its syntactic shortcut.
```supercollider
x = List[1, 2, 3] //-> [1, 2, 3]

// Retrieve the value at index 1:
x.at(1) //-> 2
// Equivalent shorthand syntax:
x[1] //-> 2

// An index can also be retrieved from an array (returns not a list, but an array):
y = [0, 0, 2, 2, 1] //-> [0, 0, 2, 2, 1]
x[y]; //-> [1, 1, 3, 3, 2]

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
Similar to [at](#at), but guarantees that any value for index is valid by clipping values outside the collection's bounds. Values greater than `size - 1` are clipped to that last index, and values below `0` (negative) are clipped to 0. When passed an array of indices, returns a new Array containing the elements at the specified positions. [SequenceableCollection#-|@|](../Classes/SequenceableCollection.md#-|@|) is its syntactic shortcut.
```supercollider
a = List[1, 2, 3]
a.clipAt(2) // same as at
a.clipAt(3) // clips
a.clipAt([-1, 3, 1]) // array of indices (returns not a list, but an array)
a|@|3 //syntactic shortcut
```

### `wrapAt`
Similar to [at](#at), but guarantees that any value for index is valid by wrapping values outside the collection's bounds. If the index exceeds `size - 1`, it wraps back around to `0`. Similarly, if the index is below `0` (negative), it wraps to access elements from the end of the collection. `this.wrapAt(index)` is equivalent to `this.at(index mod: size)`, ensuring the index is always within the valid range of the collection. The index can also be an array of indices to extract the specified elements. [SequenceableCollection#-@@](../Classes/SequenceableCollection.md#-@@) is its syntactic shortcut.
```supercollider
a = List[1, 2, 3]
a.wrapAt(2) // same as at
a.wrapAt(3) // wraps
a.wrapAt([-1, 3, 1]) // array of indices (returns not a list, but an array)
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
Similar to [at](#at), but guarantees that any value for index is valid by reflecting values outside the collection's bounds. Values greater than `size - 1` are reflected back toward lower indices. Similarly, if the index is below `0` (negative), it folds in the opposite direction. This creates a symmetrical mapping of any index within the collection's boundaries. The index can also be an array of indices to extract the specified elements. [SequenceableCollection#-@|@](../Classes/SequenceableCollection.md#-@|@) is its syntactic shortcut.
```supercollider
a = List[1, 2, 3]
a.foldAt(2) // same as at
a.foldAt(3) // folds back
a.foldAt([-1, 3, 1]) // array of indices (returns not a list, but an array)
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

### `put`
Put **item** at **index**, replacing what is there. See [SequenceableCollection#Indexing](../Classes/SequenceableCollection.md#indexing)..### `clipPut`
Same as [put](#put), but values for **index** greater than the [List](../Classes/List.md) instance size minus one will be clipped to `size - 1`, which is the last index.### `wrapPut`
Same as [put](#put), but values for **index** greater than the [List](../Classes/List.md) instance size minus one will be wrapped around to 0.### `foldPut`
Same as [put](#put), but values for **index** greater than the [List](../Classes/List.md) instance size minus one will be folded back.### `add`
Adds an **item** to the end of the List.### `addFirst`
Inserts the **item** at the beginning of the List.### `insert`
Inserts the **item** into the contents of the [List](../Classes/List.md) at the indicated **index**.
```supercollider
x = List[1, 2, 3, 4]; // -> List[1, 2, 3, 4]
x.insert(0, 999); // -> List[999, 1, 2, 3, 4]
x; // -> List[999, 1, 2, 3, 4]
```

### `boundedInsert`
Same as [insert](#insert), but removes the receiver's last element before inserting **item**. This changes the receiver but maintains its size.
```supercollider
x = List[1, 2, 3, 4]; // -> List[1, 2, 3, 4]
x.boundedInsert(1, 999); // -> List[1, 999, 2, 3]
x; // -> List[1, 999, 2, 3]
x.boundedInsert(20, \a); // -> List[1, 999, 2, a]
x.boundedInsert(-2, \b); // -> List[b, 1, 999, 2]
```

### `pop`
Remove and return the last element of the List.### `grow`
Increase the size of the List by **sizeIncrease** number of slots.### `removeAt`
Remove and return the item at **index**, shrinking the size of the List. See [SequenceableCollection#Indexing](../Classes/SequenceableCollection.md#indexing)..
```supercollider
y = List[1, 2, 3];
y.removeAt(1);
y.postln;
```

### `fill`
Inserts the item into the contents of the receiver, possibly returning a new collection.
> **Note:** the difference between this and [Collection's *fill](../Classes/Collection.md#*fill).


```supercollider
(
var z;
z = List[1, 2, 3, 4];
z.fill(4).postln;
z.fill([1, 2, 3, 4]).postln;
)
```

### `do`
Iterate over the elements in order, calling the function for each element. The function is passed two arguments, the element and an index.
```supercollider
List['a', 'b', 'c'].do({ |item, i| [i, item].postln });
```

### `reverseDo`
Iterate over the elements in reverse order, calling the function for each element. The function is passed two arguments, the element and an index.
```supercollider
List['a', 'b', 'c'].reverseDo({ |item, i| [i, item].postln });
```

### `pairsDo`
Calls function for each subsequent pair of elements in the List. The function is passed the two elements and an index.
```supercollider
List[1, 2, 3, 4, 5, 6].pairsDo({ |a, b| [a, b].postln });
```

### `copyRange`
Return a new List which is a copy of the indexed slots of the receiver from start to end. See [SequenceableCollection#Indexing](../Classes/SequenceableCollection.md#indexing)..
```supercollider
(
var y, z;
z = List[1, 2, 3, 4, 5];
y = z.copyRange(1, 3);
z.postln;
y.postln;
)
```

### `copySeries`
Return a new List consisting of the values starting at **first**, then every step of the distance between **first** and **second**, up until **last**. See [SequenceableCollection#Indexing](../Classes/SequenceableCollection.md#indexing)..
```supercollider
(
var y, z;
z = List[1, 2, 3, 4, 5, 6];
y = z.copySeries(0, 2, 5);
y.postln;
)
```

### `putSeries`
Put **value** at every index starting at **first**, then every step of the distance between **first** and **second**, up until **last**. See [SequenceableCollection#Indexing](../Classes/SequenceableCollection.md#indexing)..
```supercollider
(
var y, z;
z = List[1, 2, 3, 4, 5, 6];
y = z.putSeries(0, 2, 5, "foo");
y.postln;
)
```

### `reverse`
Return a new List whose elements are reversed.
```supercollider
(
var y, z;
z = List[1, 2, 3, 4];
y = z.reverse;
z.postln;
y.postln;
)
```

### `scramble`
Returns a new List whose elements have been scrambled. The receiver is unchanged.
```supercollider
List[1, 2, 3, 4, 5, 6].scramble.postln;
```

### `mirror`
Return a new List which is the receiver made into a palindrome. The receiver is unchanged.
```supercollider
List[1, 2, 3, 4].mirror.postln;
```

### `mirror1`
Return a new List which is the receiver made into a palindrome with the last element removed. This is useful if the list will be repeated cyclically, the first element will not get played twice. The receiver is unchanged.
```supercollider
List[1, 2, 3, 4].mirror1.postln;
```

### `mirror2`
Return a new List which is the receiver concatenated with a reversal of itself. The center element is duplicated. The receiver is unchanged.
```supercollider
List[1, 2, 3, 4].mirror2.postln;
```

### `stutter`
Return a new List whose elements are repeated **n** times. The receiver is unchanged.
> **Note:** It is recommended to use `dupEach` instead. This method is retained for backwards compatibility.


```supercollider
List[1, 2, 3].stutter(2).postln;
```

### `dupEach`
Return a new List whose elements are repeated **n** times. The receiver is unchanged.
```supercollider
List[1, 2, 3].dupEach(2).postln;
```

### `rotate`
Return a new List whose elements are in rotated order. Negative **n** values rotate left, positive **n** values rotate right. The receiver is unchanged.
```supercollider
List[1, 2, 3, 4, 5].rotate(1).postln;
List[1, 2, 3, 4, 5].rotate(-1).postln;
List[1, 2, 3, 4, 5].rotate(3).postln;
```

### `pyramid`
Return a new List whose elements have been reordered via one of 10 "counting" algorithms. The algorithms are numbered 1 through 10. Run the examples to see the algorithms.
```supercollider
List[1, 2, 3, 4].pyramid(1).postln;

(
10.do({ |i|
    List[1, 2, 3, 4].pyramid(i + 1).postcs;
});
)
```

### `lace`
Returns a new List whose elements are interlaced sequences of the elements of the receiver's subcollections, up to size **length**. The receiver is unchanged.
```supercollider
(
x = List[[1, 2, 3], 6, List["foo", 'bar']];
y = x.lace(12);
x.postln;
y.postln;
)
```

### `permute`
Returns a new List whose elements are the **nthPermutation** of the elements of the receiver. The receiver is unchanged.
```supercollider
(
x = List[1, 2, 3];
6.do({ |i| x.permute(i).postln });
)
```

### `wrapExtend`
Returns a new List whose elements are repeated sequences of the receiver, up to size **length**. The receiver is unchanged.
```supercollider
(
x = List[1, 2, 3, "foo", 'bar'];
y = x.wrapExtend(9);
x.postln;
y.postln;
)
```

### `foldExtend`
Same as [wrapExtend](#wrapextend) but the sequences fold back on the list elements.
```supercollider
(
x = List[1, 2, "foo"];
y = x.foldExtend(9);
x.postln;
y.postln;
)
```

### `slide`
Return a new List whose elements are repeated subsequences from the receiver. Easier to demonstrate than explain.
```supercollider
List[1, 2, 3, 4, 5, 6].slide(3, 1).postcs;
List[1, 2, 3, 4, 5, 6].slide(3, 2).postcs;
List[1, 2, 3, 4, 5, 6].slide(4, 1).postcs;
```

### `dump`
Dump the List's Array.### `clear`
Replace the List's Array with a new empty one.

