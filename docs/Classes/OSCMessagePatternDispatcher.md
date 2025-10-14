# OSCMessagePatternDispatcher

*The default pattern matching dispatcher for OSCFunc and OSCdef.*

**Categories:** External Control>OSC>Dispatchers

**Related:** [OSCFunc](../Classes/OSCFunc.md), [OSCdef](../Classes/OSCdef.md), [AbstractWrappingDispatcher](../Classes/AbstractWrappingDispatcher.md), [AbstractDispatcher](../Classes/AbstractDispatcher.md), [AbstractMessageMatcher](../Classes/AbstractMessageMatcher.md), [OSCMessageDispatcher](../Classes/OSCMessageDispatcher.md), [OSCFuncAddrMessageMatcher](../Classes/OSCFuncAddrMessageMatcher.md), [OSCFuncRecvPortMessageMatcher](../Classes/OSCFuncRecvPortMessageMatcher.md), [OSCFuncBothMessageMatcher](../Classes/OSCFuncBothMessageMatcher.md), [OSC_communication](../Guides/OSC_communication.md)

## Description

OSCMessageDispatcher dispatches incoming OSC messages to matching functions, using pattern matching to see if regular expressions wildcards in the incoming message's address pattern match one of this dispatcher's OSCFuncs' paths. Normally users should not have to create or message instances of this class directly. For details on OSC pattern matching, see [http://opensoundcontrol.org/spec-1_0](http://opensoundcontrol.org/spec-1_0)


## Class Methods


## Instance Methods

### `value`
Attempt to match an incoming OSC message with this dispatcher's responder funcs, and evaluate their functions for all matches found.**Arguments:**

| Argument | Description |
|----------|-------------|
| `msg` | The OSC message as an [Array](../Classes/Array.md) in the form `[OSCAddress, other args]`. |  
| `time` | A [Float](../Classes/Float.md) indicating the time the incoming message was sent. |  
| `addr` | A [NetAddr](../Classes/NetAddr.md) indicating the source of the message. |  
| `recvPort` | An [Integer](../Classes/Integer.md) indicating the port on which the message was received. |  
### `typeKey`
Returns `'OSC unmatched'`.**Returns:** A [Symbol](../Classes/Symbol.md).

