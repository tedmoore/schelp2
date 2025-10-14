# Object

*abstract superclass of all objects*

**Categories:** Core>Kernel, Language>OOP

**Related:** [Class](../Classes/Class.md), [Intro-to-Objects](../Guides/Intro-to-Objects.md), [Classes](../Reference/Classes.md)

## Description

Object is the root class of all other classes. All objects are indirect instances of class Object. We call the "receiver" the object the message is sent to: `receiver.method(argument)`.


## Class Methods


### `readArchive`
Read in an object from a text archive.
```supercollider
(
a = Array.fill(100, { 100.rand });
a.writeArchive(PathName.tmp ++ "myArray");
b = Object.readArchive(PathName.tmp ++ "myArray");
a == b; // true
)

/////////

// closed Function
(
f = { 1 + 2 };
f.writeArchive(PathName.tmp ++ "myFunc"); // succeeds
)
// open Function
(
var num;
num = 2;
f = { num + 2 };
f.writeArchive(PathName.tmp ++ "myFunc"); // fails
)
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `pathname` | A String containing the archive file's path. |  

### `new`
Create a new instance. The creation of new instances of any Object actually happens in this method (or with `newCopyArgs`) when it is called by a child class. See [WritingClasses](../Guides/WritingClasses.md).
### `newCopyArgs`
Creates a new instance and copies the arguments to the instance variables in the order that the variables were defined.Importantly, superclass constructors are NOT called, but the values are directly placed in the superclass's instance variables.
```supercollider
MyClass {
    var a, b, c;
    // Will copy arg1, arg2, arg3 to variables a, b, c.
    *new { |arg1, arg2, arg3| ^super.newCopyArgs(arg1, arg2, arg3) }
    *newKw { |arg1| ^super.newCopyArgs(arg1, c: 10) }
    value { ^[a, b, c] }
}
MyClass.new(1, 2, 3).value() == [1, 2, 3];
MyClass.newKw(1).value() == [1, nil, 10];
```

Example of inheritance.
```supercollider
Base {
    var a, b, c;
    *new { ^\didNotCallBase } // This is NEVER called
}

Derived : Base {
    var d, e, f;
    *new { |d, e, f| ^super.newCopyArgs(1, 2, 3, d, e, f) }
    *newKw { |d, e, f| ^super.newCopyArgs(c: 3, d: d, e: e, f: f) }
    value { ^[a, b, c, d, e, f] }
}

Derived.new(10, 11, 12).value() == [1, 2, 3, 10, 11, 12];
Derived.newKw(10, 11, 12).value() == [nil, nil, 3, 10, 11, 12];
```



## Instance Methods


### Class Membership
### `class`
Answer the class of the receiver.
```supercollider
5.class;
```


### `respondsTo`
Answer a [Boolean](../Classes/Boolean.md) whether the receiver understands the message selector or array of message selectors.
```supercollider
5.respondsTo('+'); // true
5.respondsTo('indexOf'); // false
5.respondsTo(['+', '-']); // true
5.respondsTo(['+', 'indexOf']); // false
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `aSymbol` | A selector name. Must be a [Symbol](../Classes/Symbol.md). |  

### `isKindOf`
Answer a Boolean indicating whether the receiver is a direct or indirect instance of aClass. Use of this message in code must be questioned, because it often indicates a missed opportunity to exploit object polymorphism.
```supercollider
5.isKindOf(Number); // true
5.isKindOf(String); // false
```


### `isMemberOf`
Answer a Boolean whether the receiver is a direct instance of aClass. Use of this message in code is almost always a design mistake.
```supercollider
5.isMemberOf(Number); // false
5.isMemberOf(Integer); // true
```



### Accessing
### `size`
Different classes respond to this message differently. Object always returns 0.
### `rank`
Returns the number of dimensions the value has. A single value (scalar) has rank of zero. See [ArrayedCollection#-rank](../Classes/ArrayedCollection.md#-rank) for cases where this is useful.
### `shape`
For a multidimensional array, returns an array of the number of elements along each consecutive dimension, see [ArrayedCollection#-shape](../Classes/ArrayedCollection.md#-shape). For a scalar value (most objects) returns nil.

### Copying
### `copy`
Make a copy of the receiver. The implementation of this message depends on the object's class. In class Object, copy calls shallowCopy.
### `shallowCopy`
Makes a copy of the object. The copy's named and indexed instance variables refer to the same objects as the receiver.
### `deepCopy`
Recursively copies the object and all of the objects contained in the instance variables, and so on down the structure. This method works with cyclic graphs.
### `copyImmutable`
If object is immutable then return a shallow copy, else return receiver.

### Conversion
To convert an object of a certain class into a similar object of another class, Object provides a number of methods.

### `as`
Returns a similar new Object of a different class.
```supercollider
[1, 2, 3].as(Set);
Pwhite(0.0, 1.0, 10).as(Set);
```


### `asArray`
Returns an Array with the receiver, unless it is an Array already.
```supercollider
[1, 2, 3].asArray;
5.asArray;
```


### `asCompileString`
Returns a String that can be interpreted to reconstruct a copy of the receiver. For the complementary method, see [String#-interpret](../Classes/String.md#-interpret).
```supercollider
a = { 10.do { 10.postln } };
a.asCompileString.postcs;
a.postcs;
```


### `asInt`
Deprecated. Use `asInteger` instead.
### `cs`
Shorthand for [#-asCompileString](#-ascompilestring).
```supercollider
{ 10.do { 10.postln } }.cs;
"Strings don't post with surrounding quotes.".cs;
```



### Archiving
Object implements methods for writing and retrieving objects from disk. Note that you cannot archive instances of Thread and its subclasses (i.e. Routine), or open Functions (i.e., a Function which refers to variables from outside its own scope).

### `writeArchive`
Write an object to disk as a text archive.**Arguments:**

| Argument | Description |
|----------|-------------|
| `pathname` | A String containing the resulting file's path. |  


### Equality and Identity
### `==`
Answer whether the receiver equals anotherObject. The definition of equality depends on the class of the receiver. The default implementation in Object is to answer if the two objects are identical.
> **Note:** Whenever == is overridden in a class, hash should be overridden as well.


```supercollider
5.0 == 5; // true
5.0 === 5; // false
a = [1, 2, 3]; b = [1, 2, 3];
a == b; // equal
a === b; // not identical
"worth trying" == "worth trying"; // equal
```


### `===`
Answer whether the receiver is the exact same object as anotherObject.
```supercollider
5.0 === 5; // false
"worth trying" === "worth trying"; // not identical
'worth trying' === 'worth trying'; // identical (symbols are unique)
```


### `!=`
Answer whether the receiver does not equal anotherObject. The default implementation in Object is to determine '==' for the two operands and negate this result. (see below).
### `!==`
Answer whether the receiver is not identical to anotherObject.
### `|==|`
A lazy equality operator. For typical object types, `|==|` behaves the same as [Object#-==](../Classes/Object.md#-==). For [AbstractFunction](../Classes/AbstractFunction.md) and its subclasses (including [Pattern](../Classes/Pattern.md) and [UGen](../Classes/UGen.md)), it does not perform the equality check immediately, but rather composes an equality operation to be performed at the time of evaluating the resulting function or stream.
```supercollider
1 |==| 1  // true

Pseq([1], inf) == 1  // false (because "a Pseq" is not 1)

Pseq([1], inf) |==| 1  // a Pbinop

(Pseq([1], inf) |==| 1).asStream.next  // Pbinop evaluates to true
```


### `|!=|`
A lazy inequality operator, defined as `not(this |==| that)`. See [Object#-|==|](../Classes/Object.md#-|==|).
### `fuzzyEqual`
Returns the degree of equality between two objects with regard to a given precision. The compared objects must support `.max`, subtraction, and division.
```supercollider
5.0.fuzzyEqual(5.0, 0.5);  // 1.0 - full equality
5.25.fuzzyEqual(5.0, 0.5); // 0.5 - 50% equality
4.75.fuzzyEqual(5.0, 0.5); // 0.5 - 50% equality
5.9.fuzzyEqual(5.0, 0.5);  // 0.0 - no equality
```

Resolve to a Boolean within your precision threshold by checking whether the returned degree of equality is above `0.0`.
```supercollider
(
// Cartesian to Polar and back, accumulating precision error
var x = 3.0, y = 5.0;
var hypot = hypot(y, x);
var angle = atan2(y, x);
var polar = Polar(hypot, angle);
var xFromPolar = polar.asPoint.x;
var equalWithin = 1e-5;
postf(
    "Exactly equal? %\n"
    "Fuzzily equal? %\n",
    x == xFromPolar,
    fuzzyEqual(x, xFromPolar, equalWithin) > 0
);
[x, xFromPolar]
)
```

**Returns:** A [Float](../Classes/Float.md) in the range `0.0` to `1.0`.
### `compareObject`
Tests if two Objects (of the same class) are the same in a certain respect: It returns true if instVarNames are equal in both. If none are given, all instance variables are tested (see also: [#-instVarHash](#-instvarhash))
```supercollider
a = Pseq([1, 2, 3], inf); b = Pseq([100, 200, 300], inf);
a.compareObject(b, [\repeats]); // true
a.compareObject(b, [\list]); // false
```


### `hash`
Answer a code used to index into a hash table. This is used by Dictionary and Set and their subclasses to implement fast object lookup. Objects which are equal == should have the same hash values. Whenever == is overridden in a class, hash should be overridden as well.
```supercollider
a = "worth trying"; b = "worth trying";
a.hash;
b.hash;
```


### `identityHash`
Answer a code used to index into a hash table. This method is implemented by a primitive and is not overridden. Objects which are identical === should have the same hash values.
```supercollider
a = "worth trying"; b = "worth trying";
a.identityHash;
b.identityHash;
```


### `instVarHash`
Returns a combined hash value for the object's instance variables and the object's class. If none are given, all instance variables are tested (see also: [#-compareObject](#-compareobject)).
```supercollider
a = Pseq([1, 2, 3], inf); b = Pseq([100, 200, 300], inf);

a.instVarHash([\repeats]); // same
b.instVarHash([\repeats]);

a.instVarHash([\list]); // different
b.instVarHash([\list]);

a = Pseq([1, 2, 3], inf); b = Prand([1, 2, 3], inf);
a.instVarHash([\list]); // different
b.instVarHash([\list]);
```



### Testing
### `isNil`
Answer a Boolean indicating whether the receiver is nil.
### `notNil`
Answer a Boolean indicating whether the receiver is not nil.
### `isNumber`
Answer a Boolean indicating whether the receiver is an instance of Number.
### `isInteger`
Answer a Boolean indicating whether the receiver is an instance of Integer.
### `isFloat`
Answer a Boolean indicating whether the receiver is an instance of Float.
### `?`
If the receiver is nil then answer anObject, otherwise answer the receiver.
### `??`
If the receiver is nil, evaluate the [Function](../Classes/Function.md) and return the result.
### `!?`
If the receiver is not nil, evaluate the [Function](../Classes/Function.md) passing in the receiver as argument and return the result, otherwise return nil.
> **Note:** The function will be inlined if it contains no variables or arguments.

This method allow building up chains of actions to be performed on an object (possibly across several methods) without having to check if the object is nil or not. After all the desired actions are performed, [#-??](#-??) can be used to check if result the result is nil and supply a default value in that case.Examples:
```supercollider
x !? (_ * 3) ?? { "It was a nil, so I give a default value".postln; Point(1, 1) }
```

With `x = nil`, this will result in:But if `x = Point(3, 4)`, the result will be:Nested nil checks:
```supercollider
(
x = nil;
y = Point(3, 4);
z = Point(5, 6);
x !? { |x| y !? { |y| z !? { |z|  x.rho * y.rho * z.rho } } }
)
```

Results in `nil`
```supercollider
(
x = Point(1, 2);
y = Point(3, 4);
z = Point(5, 6);
x !? { |x| y !? { |y| z !? {  |z| x.rho * y.rho * z.rho } } }
)
```

Results in `87.321245982865`
### `pointsTo`
Returns true if receiver has a direct reference to obj.
```supercollider
a = 9;
b = [1, a, 6, 8];
c = [1, b, 5];
c.pointsTo(b); // true
c.pointsTo(a); // false
```


### `mutable`
Returns true if receiver is mutable.
```supercollider
a = #[1, 2, 3]; b = [1, 2, 3];
a.mutable; // false
b.mutable; // true
```


### `frozen`
Returns true if receiver is frozen.
### `switch`
Object implements a switch method which allows for conditional evaluation with multiple cases. These are implemented as pairs of test objects (tested using if this == test.value) and corresponding functions to be evaluated if true. In order for switch to be inlined (and thus be as efficient as nested if statements) the matching values must be literal Integers, Floats, Chars, Symbols and the functions must have no variables or arguments.
```supercollider
(
var x, z;
z = [0, 1, 1.1, 1.3, 1.5, 2];
switch (z.choose.postln,
    1,   { \no },
    1.1, { \wrong },
    1.3, { \wrong },
    1.5, { \wrong },
    2,   { \wrong },
    0,   { \true }
).postln;
)
```

or:
```supercollider
(
var x, z;
z = [0, 1, 1.1, 1.3, 1.5, 2];
x = switch (z.choose)
    { 1 }   { \no }
    { 1.1 } { \wrong }
    { 1.3 } { \wrong }
    { 1.5 } { \wrong }
    { 2 }   { \wrong }
    { 0 }   { \true };
x.postln;
)
```



### Messaging
Instead of directly sending a method to an object, a method may be invoked given a method selector only (a Symbol). The other arguments may be provided by passing them directly, from an environment. If it is not known whether the receiver implements the method, tryPerform only sends if it does. The messages `superPerform`, `superPerformList`; and `superPerformArgs` invoke the method of the superclass.

### `perform`
The selector argument must be a Symbol. Sends the method named by the selector with the given arguments to the receiver.If the first argument is an Array or List, this method behaves like `performMsg`. However, this usage is discouraged, and `performMsg` ought to be used instead.
### `performList`
The selector argument must be a Symbol. Sends the method named by the selector with the given arguments to the receiver. If the last argument is a List or an Array, then its elements are unpacked and passed as arguments.
```supercollider
a = { |a, b, c| postf("% plus % plus % is %\n", a, b, c, a + b + c); "" };
a.performList(\value, [1, 2, 3]);
```


### `performArgs`
Like [#-perform](#-perform), but allows you to pass a key-value array of keyword arguments. Useful in [#-doesNotUnderstand](#-doesnotunderstand) and other places where you might accept a variety of keyword arguments.**Arguments:**

| Argument | Description |
|----------|-------------|
| `selector` | A [Symbol](../Classes/Symbol.md) of the method name. |  
| `args` | An [Array](../Classes/Array.md) of the arguments. |  
| `kwargs` | An [Array](../Classes/Array.md) of keyword-argument pairs.Example
```supercollider
x.performArgs(\foo, [1, 2], [\bar, 10]);
// is equivalent to...
x.foo(1, 2, bar: 10);
``` |  

### `functionPerformList`
Call the function with the selector and argument list. This method is there for a uniform interface between [Method](../Classes/Method.md)s and [Function](../Classes/Function.md)s.
### `performMsg`
The argument must be a List or Array whose first element is a Symbol representing a method selector. The remaining elements are unpacked and passed as arguments to the method named by the selector.
```supercollider
a = { |a, b, c| postf("% plus % plus % is %\n", a, b, c, a + b + c); "" };
a.performMsg([\value, 1, 2, 3]);
```


### `performWithEnvir`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `selector` | A Symbol representing a method selector. |  
| `envir` | The remaining arguments derived from the environment and passed as arguments to the method named by the selector. |  

```supercollider
a = { |a, b, c| postf("% plus % plus % is %\n", a, b, c, a + b + c); "" };
a.performWithEnvir(\value, (a: 1, c: 3, d: 4, b: 2));
```


### `performKeyValuePairs`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `selector` | A Symbol representing a method selector. |  
| `pairs` | Array or List with key-value pairs. |  

```supercollider
a = { |a, b, c| postf("% plus % plus % is %\n", a, b, c, a + b + c); "" };
a.performKeyValuePairs(\value, [\a, 1, \b, 2, \c, 3, \d, 4]);
```


### `tryPerform`
Like 'perform', but tryPerform passes the method to the receiver only if the receiver understands the method name. If the receiver doesn't implement that method, the result is nil. Note that this does not catch errors like 'try' does (see Exception). If the receiver does have a matching method but that method throws an error, execution will halt. But, 'tryPerform' is faster than 'try'.
```supercollider
(a: 1, b: 2, c: 3).tryPerform(\keysValuesDo, { |key, value| [key, value].postln });

// Set does not understand keysValuesDo -- result is nil
Set[1, 2, 3].tryPerform(\keysValuesDo, { |key, value| [key, value].postln });

// Error occurs within keysValuesDo -- error is thrown back to halt execution
(a: 1, b: 2, c: 3).tryPerform(\keysValuesDo, { |key, value| [key, value].flippityblargh });

// keyword arguments are passed on
[1, 2, 3, 4].tryPerform(\pyramid, patternType: 1)
```


### `superPerform`
Like perform, superPerform calls a method, however it calls the method on the superclass. selector: A Symbol representing a method selector. args: Method arguments.
### `superPerformList`
Like performList, superPerformList calls a method, however it calls the method on the superclass. selector: A Symbol representing a method selector. args: Method arguments. If the last argument is a List or an Array, then its elements are unpacked and passed as arguments.
### `superPerformArgs`
Like performLArgs, superPerformArgs calls a method, however it calls the method on the superclass. selector: A Symbol representing a method selector. args: Method arguments. kwargs: Keyword arguments, are passed as key value pairs.
### `multiChannelPerform`
Perform selector with multichannel expansion. See also: [Multichannel-Expansion](../Guides/Multichannel-Expansion.md).**Arguments:**

| Argument | Description |
|----------|-------------|
| `selector` | A Symbol representing a method selector. |  
| `... args` | Method arguments which, if they contain an array, will call the method multiple times for each sub-element. |  

```supercollider
a = { |a, b, c| format("% plus % times % is %", a, b, c, a + b * c).quote };
a.multiChannelPerform(\value, [1, 10, 100, 1000], [2, 7, 9], [3, 7]);

["foo", "bar"].multiChannelPerform('++', ["l", "bro", "t"]);
```



### Unique Methods
Method definitions not yet implemented may be added to an Object instance.

### `addUniqueMethod`
Add a unique method.
```supercollider
a = 5;
a.addUniqueMethod(\sayHello, { |to| "hello " ++ to ++ ", I am 5" });
a.sayHello;
```


### `removeUniqueMethod`
Remove a unique method.
```supercollider
a.removeUniqueMethod(\sayHello);
a.sayHello;
```


### `removeUniqueMethods`
Remove all unique methods of an Object.

### Dependancy
### `addDependant`
Add aDependant to the receiver's list of dependants.
### `removeDependant`
Remove aDependant from the receiver's list of dependants.
### `dependants`
Returns an IdentitySet of all dependants of the receiver.
### `changed`
Notify the receiver's dependants that the receiver has changed. The object making the change should be passed as theChanger.
### `update`
An object upon which the receiver depends has changed. theChanged is the object that changed and theChanger is the object that made the change.
### `release`
Remove all dependants of the receiver. Any object that has had dependants added must be released in order for it or its dependants to get garbage collected.

### Error Support
Object implements a number of methods which throw instances of Error. A number of methods (e.g. doesNotUnderstand) are 'private' and do not normally need to be called directly in user code. Others, such as those documented below can be useful for purposes such as object oriented design (e.g. to define an abstract interface which will be implemented in subclasses) and deprecation of methods. The reserved keyword thisMethod can be used to refer to the enclosing method. See also Method and Function (for exception handling).

### `doesNotUnderstand`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `selector` | The method that was called. |  
| `... args` | An [Array](../Classes/Array.md) of arguments. |  
| `kwargs` | An [Array](../Classes/Array.md) of keyword argument pairs. |  

### `throw`
Throws the receiver as an Exception, which may or may not be caught and handled by any enclosing Function.
### `subclassResponsibility`
Throws a SubclassResponsibilityError. Use this to indicate that this method should be defined in all subclasses of the receiver.
```supercollider
someMethod {
    this.subclassResponsibility(thisMethod);
}
```


### `shouldNotImplement`
Throws a ShouldNotImplementError. Use this to indicate that this inherited method should not be defined or used in the receiver.
### `deprecated`
Throws a DeprecatedError. Use this to indicate that the enclosing method has been replaced by a better one (possibly in another class), and that it will likely be removed in the future. Unlike other errors, DeprecatedError only halts execution if `Error.debug == true`. In all cases it posts a warning indicating that the method is deprecated and what is the recommended alternative.
```supercollider
foo {
    this.deprecated(thisMethod, ThisOrSomeOtherObject.findMethod(\foo);
    ... // execution of this method will continue unless Error.debug == true
}

// For a class method:
*bar {
    this.deprecated(thisMethod, OtherClass.class.findMethod(\bar));
    ...
}
```



### Printing and Introspection
### `post`
Print a string representation of the receiver to the post window.
```supercollider
"hello".post; "hello".post; "";
```


### `postln`
Print a string representation of the receiver followed by a newline.
```supercollider
"hello".postln; "hello".postln; "";
```


### `postc`
Print a string representation of the receiver preceded by comments.
```supercollider
"hello".postc; "hello".postc; "";
```


### `postcln`
Print a string representation of the receiver preceded by comments, followed by a newline.
```supercollider
"hello".postcln; "hello".postcln; "";
```


### `postcs`
Print the compile string representation of the receiver, followed by a newline.
```supercollider
"hello".postcs; "hello".postcs; "";
```


### `dump`
Print a detailed low level representation of the receiver to the post window. Any object understands this method (this means metaclasses, classes and their instances). Note that in [List](../Classes/List.md) class, this method dumps the list's internal array.
```supercollider
Meta_Object.dump // the meta class of the class Object
```


```supercollider
Object.dump      // the class called Object
```


```supercollider
Object.new.dump  // an istance of the class Object
```

- The detailed low level information varies depending on the receiver.
- Some instance objects, especially unique objects, return the class name and value (also more data if necessary) of the dumped object:
**[Float](../Classes/Float.md)**
: ```supercollider
1.0.dump
```

64-bit version of SuperCollider returns:For the detals, see [Float#-dump](../Classes/Float.md#-dump)

**[Integer](../Classes/Integer.md)**
: ```supercollider
1.dump
```

**[Char](../Classes/Char.md)**
: ```supercollider
$1.dump
```

The integer between *Character* and *'1'* is the ASCII value of that character.

**[Symbol](../Classes/Symbol.md)**
: ```supercollider
\1.dump
```


- Some instances return more detailed information, such as- address in virtual memory (the hexadecimal number prefixed with 0x),
- *garbage collector color* (gc),
- *data format type* (fmt),
- *flags for immutablity, finalization and sanity information from the garbage collector* (flg),
- *size class* (set),
- and so on (the information on the second and subsequent lines varies depending on the class to which the instance belongs)
with the class name of the instance:
**[Array](../Classes/Array.md)**
: ```supercollider
[1, 2].dump;
```

**[List](../Classes/List.md)**
: ```supercollider
List[1, 2].dump;
```

**[Set](../Classes/Set.md)**
: ```supercollider
Set[1, 2].dump;
```




### System Information
### `gcInfo`
Posts garbage collector information in a table format.- flips: the number of times the GC "flipped", i.e. when it finished incremental scanning of all reachable objects
- collects: the number of partial collections performed
- nalloc: total number of allocations
- alloc: total allocation in bytes
- grey: the number of "grey" objects, i.e. objects that point to reachable objects and are not determined to be (un)reachable yet
Then for each size class: numer of black, white and free objects, total number of objects and the total set size.
```supercollider
flips 241  collects 689096   nalloc 40173511   alloc 322496998   grey 346541
0  bwf t sz:    882      0 368573   369455    2955640
1  bwf t sz:   6197    122 5702377   5708696   91339136
2  bwf t sz:    947      4 1500009   1500960   48030720
3  bwf t sz:   8056  65201 301800   375057   24003648
4  bwf t sz:   4047    145   3457     7649     979072
5  bwf t sz:    422      1    431      854     218624
6  bwf t sz:    124      2     72      198     101376
7  bwf t sz: 153504      1      0   153505   157189120
8  bwf t sz:     22      0      0       22      45056
9  bwf t sz:      5      0      0        5      20480
10  bwf t sz:      5      0      0        5      40960
12  bwf t sz:      2      0      0        2      65536
13  bwf t sz:      1      0      0        1      65536
19  bwf t sz:      1      0      3        4   16777216
tot bwf t sz: 174215  65476 7876722   8116413   341832120
```

You can also query the amount of free memory with `Object.totalFree` and dump the currently grey objects with `Object.dumpGrey`. More memory status methods are: largestFreeBlock, gcDumpSet, and gcSanity.

### Iteration
### `do`
Object evaluates the function with itself as an argument, returning the result. Different classes respond to this message differently.
```supercollider
f = { |x, i| [x, i].postln };
[1, 2, 3].do(f); // Array.do
10.do(f); // Integer.do
($Q).do(f); // Object.do
```


### `generate`
Object iterates by the message do, sent to the receiver. This method is used internally by list comprehensions.
### `dup`
Duplicates the receiver n times, returning an array of n copies. Different classes respond to this message differently. The shortcut "!" can be used in place.
```supercollider
8.dup(10);
8 ! 10; // same as above
x = [[1], [2], [3]].dup(5);
x[0] === x[1]; // false: copies receiver.
x[0][0] === x[1][0] // true: doesn't deepCopy receiver
{ 1.0.rand }.dup(5) // other objects respond differently to dup
```



### Scheduling
### `awake`
This method is called by a [Clock](../Classes/Clock.md) on which the object was scheduled when its scheduling time is up. It calls [#-next](#-next), passing on the scheduling time in beats as an argument.**Arguments:**

| Argument | Description |
|----------|-------------|
| `beats` | The scheduling time in beats. This is equal to the current logical time ([Thread#-beats](../Classes/Thread.md#-beats)). |  
| `seconds` | The scheduling time in seconds. This is equal to the current logical time ([Thread#-seconds](../Classes/Thread.md#-seconds)). |  
| `clock` | The clock on which the object was scheduled. |  


### Stream Support
### `next`
Does nothing; simply returns the object itself.
### `reset`
Does nothing; simply returns the object itself.

### Routine Support
Objects support the basic interface of Stream, just returning itself in response to the following messages: next, reset, stop, free, clear, removedFromScheduler, asStream.

### `yield`
Must be called from inside a Routine. Yields control to the calling thread. The receiver is the result passed to the calling thread's method. The result of yield will be the value passed to the Routine's next method the next time it is called.
### `yieldAndReset`
Must be called from inside a Routine. Yields control to the calling thread. The receiver is the result passed to the calling thread's method. The Routine is reset so that the next time it is called, it will start from the beginning. yieldAndReset never returns within the Routine.
### `alwaysYield`
Must be called from inside a Routine. Yields control to the calling thread. The receiver is the result passed to the calling thread's method. The Routine, when called subsequently will always yield the receiver until it is reset. alwaysYield never returns within the Routine.
### `embedInStream`
Yields the receiver
### `idle`
within a routine, return values (the receiver) until this time is over. (see also [Routine#-play](../Classes/Routine.md#-play)) Time is measured relative to the thread's clock.
```supercollider
a = Routine { 1.yield; 0.idle(3); 400.yield };
fork { loop { a.next.postln; 0.5.wait } };
```


### `iter`
Returns a [OneShotStream](../Classes/OneShotStream.md) with the receiver as return value.
```supercollider
a = 9.iter;
a.nextN(4);
```


### `cyc`
Embeds the receiver in the stream n times (default: inf), each time resetting it.
```supercollider
a = 9.cyc(2);
a.nextN(4);
```


### `fin`
Calls next with the receiver n times only (default: 1), yielding the result.
```supercollider
a = (10..0).iter.fin(2);
a.nextN(4);
```


### `repeat`
Repeatedly embeds the receiver in the stream using a Pn (may thus be used for patterns and other objects alike)
```supercollider
a = (0..3).iter.repeat(2);
a.nextN(9)
```


### `loop`
Indefinitely embeds the receiver in the stream
```supercollider
a = (0..3).iter.loop;
a.nextN(9)
```


### `nextN`
Returns an array with the results of calling [#-next](#-next) a given number of times**Arguments:**

| Argument | Description |
|----------|-------------|
| `n` | Number of message calls |  
| `inval` | argument passed to the next message
```supercollider
Routine { inf.do { |i| i.rand.yield } }.nextN(8)
``` |  

### `streamArg`
 Dependent on whether an object that is passed to a stream the object will behave differently: it may be embedded in the stream or used as stream directly. This method allows to switch between the two behaviors. For efficiency, the subclasses [Pattern](../Classes/Pattern.md) and [Stream](../Classes/Stream.md) implement this method simply as "asStream".**Arguments:**

| Argument | Description |
|----------|-------------|
| `embed` | If set to true, the object embeds itself into the stream (and thus return only once). If set to false, it returns itself forever. For simplicity, subclasses implement this method without this switch.
```supercollider
// embedding an event
a = (z: 77);
b = Pset(\y, 8, a.streamArg(true)).asStream;
c = Pset(\y, 8, a.streamArg(false)).asStream;
b.nextN(3, ()); // this ends
c.nextN(3, ()); // this loops

// embedding a pattern
a = Pbind(\note, Pseq([1, 2]));
b = Pset(\y, 8, a.streamArg(true)).asStream;
c = Pset(\y, 8, a.streamArg(false)).asStream;
b.nextN(3, ()); // this ends
c.nextN(3, ()); // this ends, too
``` |  

### `addFunc`

### `addFuncTo`

### `removeFunc`

### `removeFuncFrom`
The messages [Function#-addFunc](../Classes/Function.md#-addfunc) [Function#-addFuncTo](../Classes/Function.md#-addfuncto), [Function#-removeFunc](../Classes/Function.md#-removefunc), [Function#-removeFuncFrom](../Classes/Function.md#-removefuncfrom) are supported by Object.
### `instill`

### `obtain`
The messages [SequenceableCollection#-instill](../Classes/SequenceableCollection.md#-instill) and [SequenceableCollection#-obtain](../Classes/SequenceableCollection.md#-obtain), are supported by Object.

### Math Support
### `blend`
Lineraly interpolate between this and argument
```supercollider
blend(10, 100, 0.3);
blend([1, 2, 3], [1, 3, 4], 0.5);
blend((a: 6, b: 7), (a: 0, b: [1, 2], c: 9), 0.5);
```




