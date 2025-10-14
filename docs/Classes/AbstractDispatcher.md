# AbstractDispatcher

*Dispatches incoming messages to Functions*

**Categories:** External Control>Abstract Classes

**Related:** [AbstractWrappingDispatcher](../Classes/AbstractWrappingDispatcher.md), [OSCMessageDispatcher](../Classes/OSCMessageDispatcher.md), [OSCMessagePatternDispatcher](../Classes/OSCMessagePatternDispatcher.md), [MIDIMessageDispatcher](../Classes/MIDIMessageDispatcher.md), [OSCFunc](../Classes/OSCFunc.md), [OSCdef](../Classes/OSCdef.md), [MIDIFunc](../Classes/MIDIFunc.md), [MIDIdef](../Classes/MIDIdef.md), [AbstractResponderFunc](../Classes/AbstractResponderFunc.md)

## Description

Instances of AbstractDispatcher dispatch incoming messages (e.g. MIDI, OSC), to registered instances of [AbstractResponderFunc](../Classes/AbstractResponderFunc.md). There will be a default dispatcher for each message type, but one can have multiple dispatchers per type in order to implement custom dispatching for groups of ResponderFuncs. (The main example of this is OSC pattern matching with [OSCMessagePatternDispatcher](../Classes/OSCMessagePatternDispatcher.md).) Normally users do not need to access dispatcher instances directly.
Dispatchers must be registered at the appropriate central point (e.g. Main:recvOSCfunc for OSC messages). In this capacity their interfaces mimic [Function](../Classes/Function.md) and [FunctionList](../Classes/FunctionList.md).


## Class Methods


### `all`
Get a collection of all currently active dispatchers.**Returns:** An [IdentitySet](../Classes/IdentitySet.md).
### `new`
Make a new dispatcher.**Returns:** A new instance.

## Instance Methods

### `add`
Add a responder func to this dispatcher. Subclasses should override this to do any necessary bookkeeping. Generally this method should add this dispatcher as a dependant of the responder func, so that it can respond to any changes.**Arguments:**

| Argument | Description |
|----------|-------------|
| `funcProxy` | An instance of a subclass of [AbstractResponderFunc](../Classes/AbstractResponderFunc.md) to add. |  
### `remove`
Remove a responder func from this dispatcher.**Arguments:**

| Argument | Description |
|----------|-------------|
| `funcProxy` | An instance of a subclass of [AbstractResponderFunc](../Classes/AbstractResponderFunc.md) to remove. |  
### `value`
Evaluate an incoming message to see if it matches. Subclasses should override this message to take appropriate arguments. If a matching responder func is found, this method should call value on it, passing the message.### `valueArray`
As [value](#value) above, but with the arguments passed as a single [Array](../Classes/Array.md). This method is needed so that subclasses can work in FunctionLists in central message registration points such as Main:recvOSCMessage.**Arguments:**

| Argument | Description |
|----------|-------------|
| `args` | An [Array](../Classes/Array.md) containing the message and appropriate arguments. |  
### `register`
Register this dispatcher at the appropriate central point (e.g. Main:recvOSCfunc) to receive its message type. Subclasses should take care to not override any other registered objects. (So for example use Main:addOSCFunc for OSC messages rather than Main:recvOSCfunc_.) Generally speaking, dispatchers should register themselves automatically if needed when a responder func is added.### `unregister`
Remove this dispatcher from the appropriate central registration point, i.e. deactivate it. Generally speaking a dispatcher should unregister itself automatically when its last responder func is removed.### `free`
[unregister](#unregister) this dispatcher and remove it from [#*all](#*all). After this the dispatcher should be discarded.### `typeKey`
Subclasses should override this method to return a key indicating the type of message this dispatcher responds to, e.g. `'OSC matched'` or `'MIDI control'`.**Returns:** A [Symbol](../Classes/Symbol.md).### `update`
Subclasses should override this to do any necessary updating when a dispatchers responder funcs indicate they have changed via the standard dependancy mechanism. The default implementation does nothing.

