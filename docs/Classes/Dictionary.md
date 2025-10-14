# Dictionary

*associative collection mapping keys to values*

**Related:** [Environment](../Classes/Environment.md), [Event](../Classes/Event.md)

**Categories:** Collections>Unordered

## Description

A Dictionary is an associative collection mapping keys to values. Two keys match if they are **equal**. (i.e. == returns true.)
The contents of a Dictionary are **unordered**. You must not depend on the order of items in a Dictionary. You must only rely on equality for the keys. E.g. symbols and strings can both be used as keys because the matching is done by equality (==) and not by identity (===). For identity matching, where strings can not be used as keys, see: [IdentityDictionary](../Classes/IdentityDictionary.md) and [Event](../Classes/Event.md).

> **Note:** Setting `nil` as a value erases the key from the Dictionary. This means that `nil` itself can't be used as a Dictionary value.



```supercollider
d = Dictionary();
d.put(\a, 440);
d.keys; // Set[\a]
d.put(\a, nil); // removes the value 440
d.keys; // Set[]
```




## Class Methods

### `new`
Creates a Dictionary with an initial capacity for **n** key value mappings.
### `newFrom`
Creates a new Dictionary from another collection.
```supercollider
d = Dictionary.newFrom([\a, 1, \b, 2, \c, 4]);
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `aCollection` | any Object that responds to keysValuesDo (usually a List or an Array). |  
A new Dictionary can also be created from an array of [Association](../Classes/Association.md)s:
```supercollider
Dictionary.with(*[\a->1, \b->2, \c->3])
```

Or from a single Association like:
```supercollider
d = Dictionary[\a -> 1];
```



## Instance Methods


### Adding and Removing
### `add`
Add **anAssociation** to the Dictionary. If the key value pair already exists in the Dictionary, the key's value will be replaced.
```supercollider
(
d = Dictionary.new;
d.add(\monkey -> 0).postln;
d.add(\robot -> 1).postln;    // Add robot as a key with a value of 1
d.add(\monkey -> 2).postln;    // Replaces the value for the key monkey with 2
)
```


### `put`
Associate two objects and add them to the Dictionary.
```supercollider
d = Dictionary.new;
d.put("abc", 10);

// using an event:
d = ();
d.put("abc", 10);
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `key` | key to associate with object. This can be any objects, but is often a [Symbol](../Classes/Symbol.md). |  
| `value` | an object |  

### `removeAt`
Remove the key and the value associated with it from the Dictionary.
```supercollider
d = Dictionary[\monkey -> 99];
d.removeAt(\monkey);
```


### `putAll`
Add all items of each argument to the dictionary.
```supercollider
d = Dictionary.new;
d.putAll(Dictionary[\hello -> 9, \whello -> "world"], Dictionary["abd" -> 6]);
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `... dictionaries` | any Object that responds to keysValuesDo (usually a Dictionary). |  

### `putPairs`
Add all items to the dictionary, using them as key and value pairwise.
```supercollider
d = Dictionary.new;
d.putPairs([\hello, 10, \whello, "lord", "abc", 7]);
```



### Accessing
### `at`
Access the value associated with the key.
```supercollider
d = Dictionary[\robot -> 99];
d.at(\robot);    // Get the value associated with key
d[\robot];    // different syntax, same behaviour
d.at(\monkey);    // Key doesn't exist: return Nil
```


### `atFail`
Access the value associated with the key. If the key does not exist, return the result of `function`.
### `keys`
Return a [Set](../Classes/Set.md) of all keys.
```supercollider
d = Dictionary.newFrom([\hello, 9, \whello, "world"]);
d.keys;
```


### `values`
Return a [List](../Classes/List.md) of all values.
```supercollider
d = Dictionary.newFrom([\hello, 9, \whello, "world"]);
d.values;
```


### `atAll`
Return an [Array](../Classes/Array.md) of all values for the given keys.
```supercollider
d = Dictionary.newFrom([\hello, 9, \whello, "world", \z, 99, \c, 0.33]);
d.atAll([\hello, \z, \hello, \c, \whello]);
```


### `getPairs`
Return an [Array](../Classes/Array.md) with all keys and values pairwise.
```supercollider
d = Dictionary.newFrom([\hello, 9, \whello, 77, \z, 99]);
d.getPairs;
```

Note that, unlike [#-asPairs](#-aspairs), getPairs will return nil with an empty Dictionary.
```supercollider
d = Dictionary.new;
d.getPairs;
```


### `associationAt`
Access the [Association](../Classes/Association.md) that has the given key. Element is checked for equality (not identity).
```supercollider
d = Dictionary["robot" -> 99];
d.associationAt("robot");    // Get the value associated with key
```


### `findKeyForValue`
Try to find a given value and return its key. Element is checked for equality (not identity).
```supercollider
d = Dictionary.newFrom([\hello, 1, \whello, 77]);
d.findKeyForValue(1);
```


### `matchAt`
The dictionary's keys are used as conditions against which the arbitrary item is matched. See: [matchItem](../Reference/matchItem.md)Returns the associated value or nil if no key is matching the item.
> **Note:** if an item matches multiple criteria, the value returned is arbitrary. This is because a dictionary is an unordered collection. It's the user's responsibility to make sure that criteria are mutually exclusive.

- If the key is an object, the item will be matched by identity (if key === item, the value will be returned).
- If the key is a collection, the item is matched if it's contained in the collection.
- If the key is a function, the function is evaluated with the item as an argument and the item is matched if the function returns true.

```supercollider
(
d = Dictionary.newFrom([
    0, \zero,
    \abc, \alpha,
    [1, 2, 3, 5, 8, 13, 21], \fibonacci,
    { |x| try { x.even } }, \even // try is needed because argument might not be a number
    ]);
);

d.matchAt(0)    // matches both 'zero' and 'even', either may be returned
d.matchAt(1)
d.matchAt(2)    // matches both 'fibonacci' and 'even', either may be returned
d.matchAt(4)
d.matchAt(\abc)
```


### `trueAt`
Returns [True](../Classes/True.md) if the item's `booleanValue` at the key is `true`, otherwise `false`.
```supercollider
// using binary value equivalents
d = (x:1, y:0);
d.trueAt(\x)   // true
d.trueAt(\y)   // false
d.trueAt(\foo) // false

// other kinds of objects
d = (num: 23.7, yes:true, no:false, sym:\foo);
d.trueAt(\num) // true
d.trueAt(\yes) // true
d.trueAt(\no)  // false
d.trueAt(\sym) // false
d.trueAt(\bar) // false (d[\bar] is nil)
```


### `falseAt`
Returns [True](../Classes/True.md) if the item's `booleanValue` at the key is `false`, otherwise `true`. See [#-trueAt](#-trueat) for examples.

### Testing
### `includes`
Returns true if the specified item is stored in the Dictionary as a value. Element is checked for equality (not for identity). For identity matching see subclasses: [IdentityDictionary](../Classes/IdentityDictionary.md) or [Event](../Classes/Event.md).
```supercollider
var d = Dictionary.newFrom([\a, "hey", \b, "hello"]);
d.includes("hey").postln; // -> true
```


### `includesKey`
Returns true if the specified item is stored in the Dictionary as a key. Element is checked for equality (not for identity). For identity matching see subclasses: [IdentityDictionary](../Classes/IdentityDictionary.md) or [Event](../Classes/Event.md).
```supercollider
var d = Dictionary.newFrom(["hey", 1, "hello", 2]);
d.includesKey("hey").postln; // -> true
```



### Iteration/Enumeration
Most methods for iteration work analogously to Dictionary's superclasses, see e.g. [Collection](../Classes/Collection.md).

### `do`, `collect`, `reject`, `select`

```supercollider
// do, collect, reject, select
d = Dictionary[\a -> "hello", \b -> "robot", \c -> [1, 2, 3]];
d.do { |item, i| [item, i].postln };
d.collect { |item| item + 100 };
d.reject { |item| item.size > 4 };
d.select { |item| item.size > 4 };
```


### `keysValuesDo`
Iterate over the associations, and evaluate the function for each, passing key and value as argument.
```supercollider
d = Dictionary[\a -> "hello", \b -> "robot", \c -> [1, 2, 3]];
d.keysValuesDo { |key, value| postln("the key: " ++ key ++ " the value: " ++ value) };
```


### `keysValuesChange`
Iterate over the associations, and evaluate the function for each, passing key and value as argument. Replace the value with the return value from the function (similar to [#-collect](#-collect), but modifies the dictionary **in place**).
```supercollider
d = Dictionary[\a -> "hello", \b -> "robot", \c -> [1, 2, 3]];
d.keysValuesChange { |key, value| "the key: " ++ key ++ " the value: " ++ value };
d;
```


### `keysDo`
Iterate over the associations, and evaluate the function for each, passing key as argument.
```supercollider
d = Dictionary[\a -> "hello", \b -> "robot", \c -> [1, 2, 3]];
d.keysDo { |key| postln("the key: " ++ key) };
```


### `associationsDo`
Iterate over the associations, and evaluate the function for each.
```supercollider
d = Dictionary[\a -> "hello", \b -> "robot", \c -> [1, 2, 3]];
d.associationsDo { |assoc| postln("the association: " ++ assoc) };
```


### `pairsDo`
Iterate over the associations, and evaluate the function for each, passing key and value as argument. Identical to [#-keysValuesDo](#-keysvaluesdo)
### `invert`
Return a new dictionary with all the values as keys and vice versa.
```supercollider
d = Dictionary[\a -> "hello", \b -> "robot", \c -> [1, 2, 3]];
d.invert;
```



### Other instance methods
### `order`
Return an array of keys which corresponds to the order of the values of the dictionary.
```supercollider
d = Dictionary[\a -> 5, \b -> 7, \c -> 1, \d -> 0];
d.order;
d.atAll(d.order);    // returns items in order
```


### `powerset`
Return the set of all subsets: here an array of all sub-dictionaries.
```supercollider
d = Dictionary[\a -> 5, \b -> 7, \c -> 1, \d -> 0];
d.powerset;
```


### `merge`
Combine two dictionaries into a new one by applying a function to each value. If **fill** is true (default: true), values missing from one of them are kept as they are.
```supercollider
d = Dictionary[\a -> 5, \b -> 7, \d -> 0];
e = Dictionary[\a -> 3, \b -> -3, \c -> 1];
merge(d, e, { |a, b| a + b });
merge(d, e, { |a, b| a + b }, false);
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `that` | another dictionary. |  
| `func` | a [Function](../Classes/Function.md). |  
| `fill` | a [Boolean](../Classes/Boolean.md). |  

### `blend`
Blend two dictionaries into a new one by interpolating each value. If **fill** is true (default: true), values missing from one of them are kept as they are.
```supercollider
d = Dictionary[\a -> 5, \b -> 7, \d -> 0];
e = Dictionary[\a -> 3, \b -> -3, \c -> 1];
blend(d, e, 0.3);
blend(d, e, 0.3, false);

d = Dictionary[\a -> 500, \b -> 0.001];
e = Dictionary[\a -> 300, \b -> 0.1];
blend(d, e, 0.3, specs: (a: \freq, b: \rq));
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `that` | another dictionary. |  
| `blend` | the blend ratio as a [Float](../Classes/Float.md) between 0.0 and 1.0. |  
| `fill` | a [Boolean](../Classes/Boolean.md). |  
| `specs` | a dictionary of [Spec](../Classes/Spec.md)s that are applied to each before blending. |  

### `asSortedArray`
Return the values in a sorted array of key value pairs. Sorted by key.
```supercollider
d = Dictionary[\a -> 5, \b -> 7, \c -> 1, \d -> 0];
d.asSortedArray;
```


### `asDict`
If no arguments are passed, return itself. This is part of the [Key-Value-Pairs](../Reference/Key-Value-Pairs.md) interface.**Arguments:**

| Argument | Description |
|----------|-------------|
| `mergeFunc` | This argument is not used, but exists to make the method compatible with [Collection#-asDict](../Classes/Collection.md#-asdict). |  
| `class` | A dictionary class to convert to, if given (conversion is done via `newFrom`). |  

### `asPairs`
Return the values in an array of alternating key value pairs, like `[\freq, 1848, \amp, 0.2]`. This is part of the [Key-Value-Pairs](../Reference/Key-Value-Pairs.md) interface.**Arguments:**

| Argument | Description |
|----------|-------------|
| `class` | The class of the collection to be returned. By default this is an [Array](../Classes/Array.md). |  

```supercollider
d = Dictionary[\a -> 5, \b -> 7, \c -> 1, \d -> 0];
d.asPairs;
```

Note that, unlike [#-getPairs](#-getpairs), asPairs will return an empty Array with an empty Dictionary.
```supercollider
d = Dictionary.new;
d.asPairs;
```


### `asKeyValuePairs`
See [#-asPairs](#-aspairs).
### `embedInStream`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `event` | The inval, usually in an event stream. See also [Event](../Classes/Event.md).If the event is not nil, yields a copy, adding all the elements of the receiver event (this leaves the receiver unchanged). If it is nil, return the receiver.Because this pattern is mostly used in the context of events, the following code examples use the shortcut for the subclass [Event](../Classes/Event.md) instead of the Dictionary.
```supercollider
a = (note: 2);
b = (note: [3, 5]);
Pseq([a, b]).play;
```

If a key "embedInStream" is given, use this function instead. The behaviour of the event can be configured easily this way.The arguments event (the receiver) and inevent (the inevent) are passed to the function.
> **Note:** In infinite patterns, you **must** call yield or embedInStream in the function, otherwise it will loop forever.


```supercollider
(
a = (
    pattern: Pbind(\note, Pgeom(1, 1.1, { 20.rand }), \dur, 0.05),
    embedInStream: { |event, inevent| event[\pattern].embedInStream(inevent) }
);
b = (note: [3, 5]);
c = (freq: 402, dur: 0.3);
Prand([a, b, c], inf).trace.play;
)

// change the events while playing
c[\freq] = [900, 1002, 1102];
c[\freq] = [200, 101, 1102];
```

A generator for dictionaries:
```supercollider
(
d = (
    a: 5, b: 7, c: 1,
    rout: Routine { |inval|
        inf.do { |i|
            var event = d.copy.put(\count, i);
            inval = event.embedInStream(inval);
        }
    }
);
)

// draw new values
d.rout.((z: 999));
d.rout.((z: 1, a: 0));
d.rout.(());
``` |  



## Overview

### The Difference between Dictionary, IdentityDictionary, Environment, and Event
Often, the subclass [Event](../Classes/Event.md) is used as an IdentityDictionary, because there is a syntactical shortcut:


```supercollider
a = (foo: 7);    // return a new Event.
a.put(\foo, 2.718);
a.at(\foo);
a[\foo] = 3.5;    // different syntax for put
```


Event, Environment and IdentityDictionary differ mainly insofar from Dictionary as the **keys** are taken to be identical (===) objects (see IdentityDictionary), instead of equal (==) objects. By consequence, the subclasses are also faster for indexing. Apart from this, the subclasses add specific functionality only.


```supercollider
// preliminary identity and equality of strings and symbols
"hello" == "hello";    // true, but
"hello" === "hello";    // false. However:
\hello === \hello;    // true

// compare: Dictionary will only store one "hello"
Dictionary["hello" -> 0, "hello" -> 1]; // Dictionary[(hello -> 1)]
// while Event will store both "hello" because they are not identical
("hello": 0, "hello": 1); // ("hello": 1, "hello": 0)

// for symbols as keys, Dictionary and Event show the same behaviour:
Dictionary[\hello -> 1, \hello -> 0]; // Dictionary[(hello -> 0)]
(\hello: 1, \hello: 0); // ('hello': 0)
```








