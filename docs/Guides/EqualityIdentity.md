# Identity and Equality in SuperCollider

*Distinction between reference equality ("identity", ===) and value equality ("equality", ==) in SuperCollider*

**Categories:** Tutorials

**Related:** [Event](../Classes/Event.md), [Float](../Classes/Float.md), [Intro-to-Objects](../Guides/Intro-to-Objects.md)

The distinction between identity and equality connects to wider issues in philosophy, logic, and computer science.> *For philosophical background see [Noonan/Curtis 2022](https://plato.stanford.edu/archives/fall2022/entries/identity/). What SuperCollider calls Identity and Equality roughly correspond to what philosophy calls "numeric identity" and "relative identity," respectively; and more precisely, to what computer science calls "reference equality" and "value equality," respectively. (E.g., [Miller/Goldman 2023](https://web.mit.edu/6.102/www/sp23/classes/10-equality/#reference_equality_vs_value_equality), accessed May 2025.)*
The present discussion is more narrowly concerned with an overview of how the distinction is understood in SuperCollider.

## Two objects that are equal to each other are not necessarily identical.

> **Note:** The word "object" here refers to *instances* of classes, not to the abstract class [Object](../Classes/Object.md). See [Intro-to-Objects](../Guides/Intro-to-Objects.md).


A factory may produce thousands of screwdrivers each day that are all *equal* to each other with respect to some specification; but each single screwdriver is *identical* only to itself (because it occupies this particular location at this particular time, or has a particular serial number stamped on it). Thus we can say that identity, the relation of an object to itself, is a stronger relation than equality, the relation of an object so some other object with respect to a common property.

Likewise, in SuperCollider, identity of objects created in sclang is accounted for through their location in memory.> *Exception: For primitives (such as numbers and symbols), an object's identity is tied directly to its value.*


```
a = [1,2,3];
b = [1,2,3];
a === a // -> true: identity as relation of an object (a) to itself.
a == a // -> true; identical objects are necessarily equal.
a === b // -> false; because a and b are distinct objects by virtue of their memory locations.
a == b // -> true; equal objects need not be identical.
```


In the above example, a and b were *different* instances of the [Array](../Classes/Array.md) class, each with their own memory address. You can query said address through the `.dump` method:


```
a.dump;
b.dump;
```


For newcomers to programming, it may be sufficient to be aware of this difference:

**The === (identity) and == (equality) methods are not interchangeable, and mean different things.**

In most cases, `==` behaves as "naively" expected. For instance,  from high school math, we expect `5 == 5.0` to return `true`; and it does.> *An important exception is floating-point arithmetics, where expressions like `0.1 * 3 == 0.3` may return false. However, this is not strictly speaking an issue with *equality*, but with floating-point representation (see [Float](../Classes/Float.md)).*

The behavior of `===`, on the other hand, depends more on lower-level implementation, and in some cases may at first seem counter-intuitive.

The following two examples illustrate the difference further with respect to two relevant use cases: Copying the contents of a variable rather than merely assigning it to another variable (a distinction fundamental to programming, not just in SuperCollider); and indexing into an instance of [IdentityDictionary](../Classes/IdentityDictionary.md) or [Event](../Classes/Event.md) (specific to SuperCollider).


### Where the distinction matters: Creating multiple instances from an object given in one variable using the .copy method
The above example assigned each variable to an instance of an array `[1,2,3]`, and demonstrated that the variables now point do distinct memory locations, hence their contents are not identical. However, when a variable is assigned to another *variable* rather than to an object instance, no new instance is created; instead, both variables will refer to the same object, at the same location in memory. This is relevant in practice when you want to modify a given list in multiple distinct ways, but that list only exists in one variable. The problem then becomes one of creating multiple equal but non-identical instances from just this one variable. The following example does not work as desired:


```
x = ['C', 'E', 'G']; // C major
y = x; // this will cause trouble in a moment.
z = x; // this too.
// x equals y and z at this point.
// now change last note in y to get a minor:
y[2] = 'A'; // -> ['C', 'E', 'A'] ... OK
//change first note in z to get e minor;
z[0] = 'B'; // -> ['B', 'E', 'A'] ... ; NOT what we wanted.
//why this didn't work as hoped:
x === y; // -> true: x and y point to the same List.
y === z; // as does z.
//We ended up modifying the original list twice,
//even though we wanted to keep the original x and
//get two distinct transformations from it...
```


Stacked fourths are nice, but we wanted to be boring here and just use triads. What we need to do is use the `.copy` method to create versions of the [Array](../Classes/Array.md) object referenced by `x` that are *equal but not identical to it*, so we can then modify them separately:


```
x = ['C', 'E', 'G']; //C major
y = x.copy;
z = x.copy;
x == y; // -> true
x === y; // -> false
// now change last note in y to get a minor:
y[2] = 'A'; // -> ['C', 'E', 'A'] ... OK
// change first note in z to get e minor;
z[0] = 'B'; // -> ['B', 'E', 'G'] ... OK
```


Thus, the distinction between equality and identity is implicit in such simple instructions such as "paint this screwdriver green, and that one red." (Computers just need to be told these things in more formal terms.)




### Where the distinction matters: Do not use Strings as keys for IdentityDictionary and Event.
In [Dictionary](../Classes/Dictionary.md) and its subclasses, the choice of lookup algorithm can impact performance. Using identity for this algorithm, as [IdentityDictionary](../Classes/IdentityDictionary.md) and [Event](../Classes/Event.md) do, is generally faster than usign equality, as [Dictionary](../Classes/Dictionary.md) does. Therefore when using [IdentityDictionary](../Classes/IdentityDictionary.md) and [Event](../Classes/Event.md) keys should not be [String](../Classes/String.md)s, but [Symbol](../Classes/Symbol.md)s. The following example demonstrates why:


```
"String" == "String"; // -> true
//what happens next may surprise you:
"String" === "String"; // -> false
//because each String object is a separate instance.

//Dictionary with a String key (works):
x = Dictionary.new();
x.put("String",1234);
x["String"] // -> 1234

//IdentityDictionary with a String key (won't work):
y = IdentityDictionary.new();
y.put("String",1234);
y["String"] // -> nil

//Event with a String key (wont'work):
z = (); //Shorthand for z = Event.new()
z.put("String", 1234) // -> ("String":1234)
z["String"] // -> nil
//... because the String instances are not identical!

//Symbols to the rescue:
z.put('Symbol', 5678) // -> ('Symbol':5678)
z['Symbol'] // -> 5678
```






## Implementation details

### Values with unique representations: Symbol, SimpleNumber, and more.
Why does [Symbol](../Classes/Symbol.md) work to index into an [IdentityDictionary](../Classes/IdentityDictionary.md), while [String](../Classes/String.md) does not? Because each [Symbol](../Classes/Symbol.md) has a **unique representation** such that `'symbol'` and `'symbol'`will always point to the same memory location, regardless of where they sit in the code. Thus, the instance that is passed to the argument of the `.at` method of the dictionary is *identical*, rather than just *equal*, to the instance that serves as the key argument to the dictionary.

Other examples of classes with unique representations are [SimpleNumber](../Classes/SimpleNumber.md) and its subclasses ([Integer](../Classes/Integer.md), [Float](../Classes/Float.md)): Each reference to a [Float](../Classes/Float.md) of a given value (say 1.234) points to one and the same instance. (Of course, this instance is not identical to floats of a different value, e.g. 1.23400001.)

As we have seen, this was *not* the case for [String](../Classes/String.md), where each occurrence of a [String](../Classes/String.md) in the code will create a *new* instance rather than pointing to an exiting instance of the same value. It is also generally *not* the case for [Collection](../Classes/Collection.md)s. We have already seen this for [Array](../Classes/Array.md)s; here is a similar example for [Set](../Classes/Set.md)s.


```
Set[1,2,3] === Set[1,2,3] // -> false
```





### Unless overridden by a subclass, checking for equality defaults to checking for identity.
Not all classes explicitly implement a `==` method. In that case, `==` simply defaults to `===`. An instance of this is [Function](../Classes/Function.md),> *The reason for this, at least for functions, lies ultimately in the undecideability of the "Halting Problem." See [Immermann2021](https://plato.stanford.edu/archives/win2021/entries/computability/#halpro).*where the following behavior may be surprising:


```
{1} == {1} // -> false!
```


To understand this behavior, we must know two things: First, instances of [Function](../Classes/Function.md) do not have unique representations, that is, like [String](../Classes/String.md) (mentioned above), each `{1}` expression in the code is assigned a separate instance. Thus `{1} === {1}` will return `false`. Second, *unlike* [String](../Classes/String.md), [Function](../Classes/Function.md) does not implement a `==` method, and therefore its `==` defaults to `===`.  `{1} == {1}` is thus really a question about whether the two functions designate the same object instance in memory,  i.e. whether `{1} === {1}`---which, as we just learned, returns `false`.





