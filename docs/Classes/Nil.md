# Nil

**Categories:** Core

*Represents uninitialized data*

## Description

Nil has a single instance named `nil` and is used to represent uninitialized data, bad values, or terminal values such as end-of-stream. Internally, `nil` also serves as a sentinel value, used to mark empty or unoccupied slots in hash-based data structures such as `Set`, and its subclasses. Because of this internal role, `nil`—despite being a valid object—cannot be stored as an element in `Set` or any of its subclasses. Attempting to do so will result in a runtime error. See the [Set](../Classes/Set.md) for more information.

> **Note:** Take note that `Nil` is a class and not the special value `nil`. Comparing `Nil` and `nil` will return false. In normal use, you should not need to use this class directly; use `nil`.
```
Nil.isNil;    // false
Nil == nil;   // false
Nil === nil;  // false
```




## Instance Methods


### `isNil`
Answers true because this is nil. In class [Object](../Classes/Object.md) this message is defined to answer false.
```
[1, 2, nil, 3].collect(_.isNil);
```


### `notNil`
Answer false. In class [Object](../Classes/Object.md) this message answers true.
```
[1, 2, nil, 3].collect(_.notNil);
```


### `?`
return first non-nil argument. Since this IS nil then return anObject. In class [Object](../Classes/Object.md), ? is defined to answer the receiver.
```
[1, 2, nil, 3].collect { |x| x ? -1 }; // replace nil by -1
```


### `??`
If the receiver is nil, evaluate the function and return the result. Since this IS nil, then evaluate the function and return the result. In class [Object](../Classes/Object.md), ?? is defined to answer the receiver.
```
[nil, 2, nil, 3].collect { |x| x ?? { 100.rand } }; // replace nil by a random number
```


### `booleanValue`
Returns false.
```
[1, 2, nil, 3].collect(_.booleanValue);
// compare:
[true, false, false, true].collect(_.binaryValue);
```


### `rate`
Returns nil.
### `numChannels`
Returns nil.
### `isPlaying`
Returns false.
### `dependants`
Returns an empty IdentitySet.
### `awake`
Returns nil.
### `nextTimeOnGrid`
Returns clock.nextTimeOnGrid.
### `asQuant`
Returns Quant.default.
### `matchItem`
Returns true.See also [matchItem](../Reference/matchItem.md).
```
[3, 2, 1].select(nil.matchItem(_))); // returns all
// compare:
[3, 2, 1].select([1, -1, 2].matchItem(_))); // returns only those in the key collection
```


### `asCollection`
Returns empty array.
### `get`
Returns prevVal.
### `asSpec`
Returns the default ControlSpec
### `handleError`
Either report error or inspect error and halt execution.
### `push`
Executes function.
### `appendStream`
Returns stream.
### Dependancy
All the messages for the Dependancy protocol (See class [Object](../Classes/Object.md)) are defined in class Nil to do nothing. This eliminates the need to check for nil when sending dependancy messages.


### Other Methods
Many other messages are defined in class Nil to do nothing. This eliminates the need to check for nil.


### Generic Collectors
There are a number of methods that can be applied to nil so that variables do not need to be initialized. Nil is just the "ground" (default case) from which the rest is bootstrapped.


### `add`
Returns an array with the value. This makes it unnecessary to initialize when adding to a variable.
```
x = nil;
x = x.add(8);  // returns an array
x = x.add(7); // appends to the array
```



### `addAll`
Returns an array with all the values. This makes it unnecessary to initialize when adding to a variable.
```
x = nil;
x = x.addAll([0, 2, 1, 2]);  // returns an array
x = x.addAll(7); // single objects are converted
```



### `remove`
For nil, it just returns nil. This makes it unnecessary to initialize when removing from a variable and adding to it again.
```
x = nil;
x.remove(1); // stays nil, returns nil
x = x.addAll([0, 2, 1, 2]);  // returns an array
x.remove(1); // returns 1
x;
```



### `++`
Returns an array with all the values. This makes it unnecessary to initialize when adding to a variable.
```
x = nil;
x = x ++ [7, 8, 9]; // returns the receiver
x = x ++ [3, 0, 1, 2]; // adds to the array
```



### `addFunc`
Returns a function or a FunctionList. This method is used to add multiple functions to already existing ones.
```
f = nil;
f = f.addFunc { "----------****".scramble };
f = f.addFunc { 1.0.rand };
f.value;
```



### `removeFunc`
This method is used to remove multiple functions from already existing ones. For Nil, it just returns itself.
```
f = { 1.0.rand };
g = { "you have produced a random value".postln };
f = f.addFunc(g);
f.value;
f.removeFunc(g);
f.value;
```



### `transformEvent`
This method is used to operate on events which are passed through the system as an argument.
```
// for Nil: return the argument unmodified (an event).
nil.transformEvent((x: 8));
// for Dictionary (and thus for Event): add to the argument.
(y: 100, z: 1).transformEvent((x: 8));
// for Association: add the association to the event
(\a -> \x).transformEvent((x: 8));
// for Function: use the function receive the event as argument.
{ |event| event.use { ~x = ~x + 1 }; event }.transformEvent((x: 8));
```




