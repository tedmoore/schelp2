# Bag

*Unordered collection of objects*

**Related:** [IdentityBag](../Classes/IdentityBag.md), [Set](../Classes/Set.md)

**Categories:** Collections>Unordered

## Description

A Bag is an unordered collection of objects. In some languages it is referred to as a counted set. A Bag keeps track of the number of times objects are inserted and requires that objects be removed the same number of times. There is only one instance of an object in a Bag even if the object has been added to the Bag multiple times (test is for **equality**)
Most of Bag's methods are inherited from Collection. The contents of a Bag are unordered. You must not depend on the order of items in a set.


## Class Methods


### `new`
Creates a Bag with an initial capacity for **n** objects.

## Instance Methods


### `contents`
Returns the dictionary that stores the objects in pairs (obj -> numberOfObjects)
```
Bag["a", "b", "c", "c"].contents;
```

**Returns:** [Dictionary](../Classes/Dictionary.md)
### `itemCount`
Count the number of **item**s.
```
Bag[1, 2, 2, 3, 300, 2].itemCount(2);
```


### Adding and Removing

### `add`
Add an object to the Bag. A Bag may contain multiple entries of the same object.
```
Bag[1, 2, 3].add(4).postln;

Bag[1, 2, 3].add(3).postln;

Bag["abc", "def", "ghi"].add("jkl").postln;

Bag["abc", "def", "ghi"].add("def").postln;
```



### `remove`
Remove an object from the Bag.
```
Bag[1, 2, 3].remove(3).postln;
```



### Iteration

### `do`
Evaluates **function** for each item in the Bag. The function is passed two arguments, the item and an integer index.
```
Bag[1, 2, 3, 300].do({ |item, i| item.postln });

Bag[1, 2, 2, 3, 300].do({ |item, i| item.postln });
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `function` | args to function: item, i |  


### `countsDo`
Evaluates **function** for each unique item in the Bag along with that item's count. The function is passed two arguments, the item, the quantity of that item in the Bag and an integer index.
```
Bag[1, 2, 3, 300].countsDo({ |item, count, i| [item, count].postln });

Bag[1, 2, 2, 3, 300].countsDo({ |item, count, i| [item, count].postln });
```



### Testing

### `includes`
Answer whether an object is contained in the Bag.
```
Bag[1, 2, 3, 4].includes(3);
```

**Returns:** [Boolean](../Classes/Boolean.md)

## Examples


### Difference between Bag and IdentityBag:

```
// the two strings are equal, but not identical
"something" == "something"; // true
"something" === "something" // false

a = Bag.new;
a.add("something");
a.add("something");
a.contents; // only one object in the bag really

a = IdentityBag.new;
a.add("something");
a.add("something");
a.contents; // two objects in the bag
```






