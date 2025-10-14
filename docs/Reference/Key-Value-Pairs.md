# Key Value Pairs

*An interface for translating between three common data structures: Dictionaries, Arrays of Associations and of Pairs*

**Categories:** Collections, Interfaces

**Related:** [IdentityDictionary](../Classes/IdentityDictionary.md), [Array](../Classes/Array.md), [Association](../Classes/Association.md)


## Motivation
There are three very similar ways to represent maps between keys and values, each of which have a specific purpose:

| key value pairs | common representation of arguments | `[\freq, 452, \amp, 0.2]` | 
| --- | --- | --- || collections of associations | ordering, array and collection methods | `[0 -> [1, 2, 3], 1 -> [2, 1]]` | | dictionaries: fast lookup | event compatibility | `(instrument: \sine, freq: 561)` | 
To make it easy to translate between these purposes and representations, there is a uniform set of methods:

| `asPairs` | returns an array of key value pairs | 
| --- | --- || `asAssociations` | returns an array of associations | | `asDict` | returns an IdentityDictionary. | 


## Examples

```supercollider
// the following all return [\freq, 452, \amp, 0.2]

[\freq, 452, \amp, 0.2].asPairs
[\freq -> 452, \amp -> 0.2].asPairs
(freq: 452, amp: 0.2).asPairs


// the following all return [\freq -> 452, \amp -> 0.2]

[\freq, 452, \amp, 0.2].asAssociations
[\freq -> 452, \amp -> 0.2].asAssociations
(freq: 452, amp: 0.2).asAssociations

// the following all return (freq: 452, amp: 0.2) or the equivalent IdentityDictionary

[\freq, 452, \amp, 0.2].asDict
[\freq -> 452, \amp -> 0.2].asDict
(freq: 452, amp: 0.2).asDict
```




## Mapping Parameters
The method `asDict` optionally takes a `mergeFunc` and a `class` argument.


```supercollider
 // IdentityDictionary[ (a -> 1), (c -> 3), (b -> 2) ]
[\a, 1, \a, 3, \b, 2, \c, 3, \c, 7].asDict;

//  IdentityDictionary[ (a -> 4), (c -> 10), (b -> 2) ]
[\a, 1, \a, 3, \b, 2, \c, 3, \c, 7].asDict({ |new, old| new + old })

// Dictionary[ (what -> was), (how -> wie), (and -> und), (this -> das) ]
["this", "das", "and", "und", "what", "was", "how", "wie"].asDict(class: Dictionary)

// Environment[ (a -> 1), (b -> 2) ]
[\a, 1, \b, 2].asDict(class: Environment)
```


The method `asEvent` is a shortcut:


```supercollider
[\freq, 100, \amp, 0.1].asEvent // ( 'amp': 0.1, 'freq': 100 )
```


The methods `asAssociations` and `asPairs` optionally take a `class` argument.


```supercollider
// SortedList[ (a -> 1871), (b -> 1848), (c -> 1789) ]
(c:1789, b:1848, a:1871).asAssociations(SortedList);

// LinkedList[ a, 1871, c, 1789, b, 1848 ]
(c:1789, b:1848, a:1871).asPairs(LinkedList);
```






