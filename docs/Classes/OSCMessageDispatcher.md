# OSCMessageDispatcher

*The default dispatcher class for OSCFunc and OSCdef.*

**Categories:** External Control>OSC>Dispatchers

**Related:** [OSCFunc](../Classes/OSCFunc.md), [OSCdef](../Classes/OSCdef.md), [AbstractWrappingDispatcher](../Classes/AbstractWrappingDispatcher.md), [AbstractDispatcher](../Classes/AbstractDispatcher.md), [AbstractMessageMatcher](../Classes/AbstractMessageMatcher.md), [OSCMessagePatternDispatcher](../Classes/OSCMessagePatternDispatcher.md), [OSCFuncAddrMessageMatcher](../Classes/OSCFuncAddrMessageMatcher.md), [OSCFuncRecvPortMessageMatcher](../Classes/OSCFuncRecvPortMessageMatcher.md), [OSCFuncBothMessageMatcher](../Classes/OSCFuncBothMessageMatcher.md), [OSC_communication](../Guides/OSC_communication.md)

## Description

OSCMessageDispatcher dispatches incoming OSC messages to matching functions. Normally users should not have to create or message instances of this class directly.


## Class Methods


## Instance Methods

### `wrapFunc`
Called internally to wrap functions in message matcher objects, if needed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `funcProxy` | An instance of [OSCFunc](../Classes/OSCFunc.md) or [OSCdef](../Classes/OSCdef.md) whose function(s) are to be wrapped. |  
### `getKeysForFuncProxy`
Get the keys at which a responder func's functions are stored in this dispatcher's active dictionary. The keys will be an OSC path.**Arguments:**

| Argument | Description |
|----------|-------------|
| `funcProxy` | The [OSCFunc](../Classes/OSCFunc.md) or [OSCdef](../Classes/OSCdef.md) whose keys should be returned. |  
**Returns:** An [Array](../Classes/Array.md) containing the funcProxy's path as a [Symbol](../Classes/Symbol.md).### `value`
Attempt to match an incoming OSC message with this dispatcher's responder funcs, and evaluate their functions for all matches found.**Arguments:**

| Argument | Description |
|----------|-------------|
| `msg` | The OSC message as an [Array](../Classes/Array.md) in the form `[OSCAddress, other args]`. |  
| `time` | A [Float](../Classes/Float.md) indicating the time the incoming message was sent. |  
| `addr` | A [NetAddr](../Classes/NetAddr.md) indicating the source of the message. |  
| `recvPort` | An [Integer](../Classes/Integer.md) indicating the port on which the message was received. |  
### `register`
Adds this dispatcher to thisProcess.recvOSCfunc.### `unregister`
Removes this dispatcher from thisProcess.recvOSCfunc.### `typeKey`
Returns `'OSC unmatched'`.**Returns:** A [Symbol](../Classes/Symbol.md).

