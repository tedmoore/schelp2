# Adverbs for Binary Operators

*modify behaviour of binary operators*

**Categories:** Language, Collections

**Related:** [SequenceableCollection](../Classes/SequenceableCollection.md), [Stream](../Classes/Stream.md)

Adverbs are a third argument passed to binary operators that modifies how they iterate over [SequenceableCollection](../Classes/SequenceableCollection.md)s or [Stream](../Classes/Stream.md)s. The idea for adverbs is taken from the J programming language which is a successor of APL.

## Adverbs and SequenceableCollections
Normally when you add two arrays like this:


```
[10, 20, 30, 40, 50] + [1, 2, 3]
```


You get this result:


```
[ 11, 22, 33, 41, 52 ]
```


A new array is created which is the length of the longer array and items from each array are added together by wrapped indexing.

Using adverbs can change this behavior. Adverbs are symbols and they follow a '.' (dot) after the binary operator. Adverbs can be applied to all binary operators.


### adverb 's'
The first adverb is 's' which means 'short'. The add operation now returns the shorter of the two arrays.


```
[10, 20, 30, 40, 50] +.s [1, 2, 3]
```


returns:


```
[ 11, 22, 33 ]
```





### adverb 'f'
Another adverb is 'f' which uses folded indexing instead of wrapped:


```
[10, 20, 30, 40, 50] +.f [1, 2, 3]
```


returns:


```
[ 11, 22, 33, 42, 51 ]
```





### adverb 't'
The table adverb 't' makes an array of arrays where each item in the first array is added to the whole second array and the resulting arrays are collected.


```
[10, 20, 30, 40, 50] +.t [1, 2, 3]
```


returns:


```
[ [ 11, 12, 13 ], [ 21, 22, 23 ], [ 31, 32, 33 ], [ 41, 42, 43 ], [ 51, 52, 53 ] ]
```





### adverb 'x'
The cross adverb 'x' is like table, except that the result is a flat array:


```
[10, 20, 30, 40, 50] +.x [1, 2, 3]
```


returns:


```
[ 11, 12, 13, 21, 22, 23, 31, 32, 33, 41, 42, 43, 51, 52, 53 ]
```






## Adverbs and Streams
There is currently one adverb defined for streams. This is the cross adverb, 'x'.

Normally when you add two streams like this:


```
p = (Pseq([10, 20]) + Pseq([1, 2, 3])).asStream;
Array.fill(3, { p.next });
```


you get this:


```
[ 11, 22, nil ]
```


The items are paired sequentially and the stream ends when the earliest stream ends.

The cross adverb allows you to pair each item in the first stream with every item in the second stream.


```
p = (Pseq([10, 20]) +.x Pseq([1, 2, 3])).asStream;
Array.fill(7, { p.next });
```


the result is:


```
[ 11, 12, 13, 21, 22, 23, nil ]
```


You can string these together. Every item in the left stream operand is "ornamented" by the right stream operand.


```
p = (Pseq([100, 200]) +.x Pseq([10, 20, 30]) +.x Pseq([1, 2, 3, 4])).asStream;
Array.fill(25, { p.next });

[ 111, 112, 113, 114, 121, 122, 123, 124, 131, 132, 133, 134,
  211, 212, 213, 214, 221, 222, 223, 224, 231, 232, 233, 234, nil ]
```


Sound example:


```
Pbind(\dur, 0.17, \degree, Pwhite(0, 6) +.x Pseq([[0, 2, 4], 1, [0, 2], 3])).trace.play
```






