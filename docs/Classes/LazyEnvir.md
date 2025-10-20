# LazyEnvir

*lazy environment*

**Categories:** JITLib>Environments, Live Coding, Collections>Unordered

**Related:** [Maybe](../Classes/Maybe.md), [Fdef](../Classes/Fdef.md), [Environment](../Classes/Environment.md), [ProxySpace](../Classes/ProxySpace.md), [Overviews/JITLib](../Overviews/JITLib.md)

## Description

Environment with deferred evaluation and default values.
Consequently, calculations can be done with nonexisting objects which can then be assigned later. Per default, a LazyEnvir returns instances of [Maybe](../Classes/Maybe.md). See also [Fdef](../Classes/Fdef.md).

> **Note:** While the method put is treated as transparent and implicitly creates a placeholder, all other methods, like at, collect, do, etc. pass the placeholder. In order to retrieve the object itself, use .source - in order to reduce it to a value, use: value



```
e = LazyEnvir.new;
e.use { ~x = ~y + ~z };
e.at(\x);
e.at(\x).source; // the source is a binary operation (addition on the placeholders)
e.use { ~y = 5; ~z = 7 };
e.at(\x).value; // the value is 12
```




## Instance Methods


### `put`
Sets the value of the reference at key.
### `at`
Returns a reference to the object at key.
```
l = LazyEnvir.push;

// default objects are created on access
~a;
~a.value; // defaults to nil

// operations on placeholders
(
~c = ~a + ~b;

~c.value; // doesn't fail, instead returns nil
)

// variables can be assigned later
(
~a = 800;
~b = { 1.0.rand };

~c.value;
)

// variables can be exchanged later
(
~b = { 1000.rand };
~c.value;
)
```


### `copy`
Copies the environment into a new one, with each placeholder being copied as well.
### `localPut`, `localRemoveAt`
Sets the value of the key directly. This method is mainly used internally.
### `proxyClass`
Specify what placeholder object the environment uses by supplying a class name ([Symbol](../Classes/Symbol.md)). The default is a [Maybe](../Classes/Maybe.md). Any object that responds to the methods source, source_ and clear can be a placeholder.
```
// making a pattern space using LazyEnvir

a = LazyEnvir.new;
a.proxyClass = \PatternProxy;

a.push;

~x = Pseq([1, 2, 30], 1);
~y = Pseq([~x], inf);

z = ~y.asStream;

z.next;
z.next;
z.next;
~x = Pseq([100, 2, 300], 1);
z.next;
z.next;
z.next;

a.pop;
```


### `removeAt`
Removes the placeholder from the environment and clears it.
### `makeProxy`
Returns a new placeholder object. This is used internally and can be overridden to implement other lazy environments.

