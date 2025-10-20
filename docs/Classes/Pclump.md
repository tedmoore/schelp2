# Pclump

*A pattern that takes another pattern and groups its values into arrays.*

**Related:** [SequenceableCollection#-clump](../Classes/SequenceableCollection#-clump.md)

**Categories:** Streams-Patterns-Events>Patterns>List

## Description

Groups the source pattern into arrays whose size is given by n. Similar to [SequenceableCollection#-clump](../Classes/SequenceableCollection.md#-clump).
E.g. If the source pattern has 5 elements and you choose a clump size of 2, the new pattern will return two arrays containing 2 elements and a final array containing 1 element.


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `n` | An integer, or a pattern that returns an integer. This integer will determine the size of the next clump. |  
| `pattern` | The pattern to be filtered. |  

## Examples


```
// This will give you the sequence: [1, 2] [3] nil
// Note that the last grouping is just the remainder of the pattern (in this case [3]).
x = Pclump(2, Pseq([1, 2, 3], 1)).asStream;
x.next;
x.next;
x.next;
```


Play some random chords:

```
Pbind(
  \degree, Pclump(Pseq([3, 3, 4, 2, 4, 2, 4], inf), Pseq([1, 3, 5, 7, 9], 8), inf),
  \dur, 1).play
```




