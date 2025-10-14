# AbstractResponderFunc

*Abstract superclass of responder func objects*

**Categories:** External Control>Abstract Classes

**Related:** [OSCFunc](../Classes/OSCFunc.md), [OSCdef](../Classes/OSCdef.md), [MIDIFunc](../Classes/MIDIFunc.md), [MIDIdef](../Classes/MIDIdef.md), [AbstractDispatcher](../Classes/AbstractDispatcher.md)

## Description

AbstractResponderFunc is the abstract superclass of responder funcs, which are classes which register one or more functions to respond to a particular type of input. It provides some common functionality such as introspection. Its two main subclasses are [OSCFunc](../Classes/OSCFunc.md), and [MIDIFunc](../Classes/MIDIFunc.md). By default responder funcs do not persist beyond Cmd-. (see [permanent](#permanent) below).
Instances will register with a dispatcher (an instance of a subclass of [AbstractDispatcher](../Classes/AbstractDispatcher.md)), which will actually dispatch incoming messages to an instance's Function(s).


## Class Methods


### `allFuncProxies`
Get all current instances of this classes concrete subclasses, sorted by type.**Returns:** An [IdentityDictionary](../Classes/IdentityDictionary.md).
### `allEnabled`
As allFuncProxies above, but only return those instances currently listening for input.**Returns:** An [IdentityDictionary](../Classes/IdentityDictionary.md).
### `allDisabled`
As allFuncProxies above, but only return those instances currently not listening for input.**Returns:** An [IdentityDictionary](../Classes/IdentityDictionary.md).

## Instance Methods

### `func`
Get or set this objects response function.**Returns:** The getter returns a [Function](../Classes/Function.md) or similar object.### `srcID`
Get this object's source.**Returns:** The return type will depend on subclass. For [OSCFunc](../Classes/OSCFunc.md) this will be a [NetAddr](../Classes/NetAddr.md), for [MIDIFunc](../Classes/MIDIFunc.md) a UID. This can be nil, which indicates that the object will respond to any source.### `enabled`
Check if this object is currently responding to incoming messages.**Returns:** A [Boolean](../Classes/Boolean.md).### `dispatcher`
et this object's dispatcher. This is the object which matches incoming messages with responder funcs. Instances can use custom dispatchers to support arbitrary matching schemes.**Returns:** An instance of an appropriate subclass of [AbstractDispatcher](../Classes/AbstractDispatcher.md). (The return type will depend on subclass.)### `permanent`
Get or set whether this responder func is persists when the user executes Cmd-. If false this will be disabled and removed from the global lists. The default is false.**Arguments:**

| Argument | Description |
|----------|-------------|
| `bool` | A [Boolean](../Classes/Boolean.md) indicating if this object is permanent. |  
**Returns:** The getter returns a [Boolean](../Classes/Boolean.md).### `enable`
Enable this object to receive incoming messages. This is done automatically at creation time.### `disable`
Stop this object from receiving incoming messages.### `add`
Add a new function to the list of functions which will be executed when this object receives an incoming message.**Arguments:**

| Argument | Description |
|----------|-------------|
| `newFunc` | A [Function](../Classes/Function.md) or similar object to be added. |  
### `remove`
Remove a function from the list of functions which will be executed when this object receives an incoming message.**Arguments:**

| Argument | Description |
|----------|-------------|
| `removeFunc` | The [Function](../Classes/Function.md) to be removed. |  
### `gui`
Open a subclass specific GUI. (Not yet implemented)**Returns:** The GUI object.### `oneShot`
Indicate that this object should execute only once and then free itself.### `fix`
A synonym for [permanent](#permanent)### `free`
Disable this object and remove it from the global lists. This should be done when you are finished using this object.### `clear`
Remove all active functions from this object's function list.
## Examples

See [OSCFunc](../Classes/OSCFunc.md) and [MIDIFunc](../Classes/MIDIFunc.md).

