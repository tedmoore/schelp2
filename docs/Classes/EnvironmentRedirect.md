# EnvironmentRedirect

*Base class for environment redirects.*

**Categories:** JITLib>Environments, Collections>Unordered, Live Coding

**Related:** [Environment](../Classes/Environment.md)

## Description

EnvironmentRedirect behaves like an [Environment](../Classes/Environment.md) that redirects access (`put(key, val)`, or `~key`) and assignment (`at(key)`, or `~key = val`). It is used as a basis for classes like [LazyEnvir](../Classes/LazyEnvir.md) and [ProxySpace](../Classes/ProxySpace.md).


## Class Methods

### `new`
Create new environment redirect, if envir is passed, it is used as a basis.

### replacing Environment class methods
EnvironmentRedirect implements some of the interface of [Environment](../Classes/Environment.md)

### `push`, `pop`

### `make`, `use`

### `newFrom`



## Instance Methods

### `envir`
return or replace the source environment
```supercollider
e = LazyEnvir.new;
e.put(\x, 9);
e.envir; // look into the envir itself: for a LazyEnvir it contains instances of Maybe as placeholders
```


### redirecting objects
Overriding these methods, one can redirect where objects go when they are assigned to the space. This is done for example in [LazyEnvir](../Classes/LazyEnvir.md) and [ProxySpace](../Classes/ProxySpace.md).

### `at`, `removeAt`

### `put`

### `add`



### `dispatch`
A function or object that is called when the environment is modified. The key and the changed object are passed as arguments. When an object is removed from the environment, dispatch is called with its key and `nil`. Note that dispatch is called on removal only if the removed object existed.
```supercollider
e = LazyEnvir.new;
e.dispatch = { |key, val| "new values:".postln; [key, val].postln };
e.put(\x, 9);
e.removeAt(\x); // also runs dispatch, val is nil
e.removeAt(\y); // \y was not in e: dispatch not called
```



### Behaving like an Environment
EnvironmentRedirect implements some of the interface of [Environment](../Classes/Environment.md), which it can replace where needed.

### `push`, `pop`, `clear`, `choose`

### `make`, `use`

### `do`, `keysValuesDo`, `sortedKeysValuesDo`

### `putAll`

### `keysValuesArrayDo`

### `doFunctionPerform`

### `keys`, `values`, `findKeyForValue`

### `know`

### `doesNotUnderstand`


### Networking and forwarding assignment
EnvironmentRedirect and its subclasses can be used to dispatch assignment, e.g. over a network. To do this, a dispatch function can be supplied - see Public in **JITLibExtensions** quark. The following local methods can be used to avoid a recursive updating:

### `localPut`
Like `put`, but without calling the dispatch function.
### `localRemoveAt`
Like `removeAt`, but without calling the dispatch function.


