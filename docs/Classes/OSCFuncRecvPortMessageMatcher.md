# OSCFuncRecvPortMessageMatcher

*Matches incoming messages to responder funcs based on receive port*

**Categories:** External Control>OSC>Matchers

**Related:** [AbstractMessageMatcher](../Classes/AbstractMessageMatcher.md), [OSCFuncAddrMessageMatcher](../Classes/OSCFuncAddrMessageMatcher.md), [OSCFuncRecvPortMessageMatcher](../Classes/OSCFuncRecvPortMessageMatcher.md), [OSCFuncBothMessageMatcher](../Classes/OSCFuncBothMessageMatcher.md)

## Description

This is used by [OSCMessageDispatcher](../Classes/OSCMessageDispatcher.md) and [OSCMessagePatternDispatcher](../Classes/OSCMessagePatternDispatcher.md) to match incoming OSC messages to instances of [OSCFunc](../Classes/OSCFunc.md) or [OSCdef](../Classes/OSCdef.md) using receive port. This class is private, and generally users should not need to address instances directly.


## Class Methods

### `new`
Make a new instance.**Arguments:**

| Argument | Description |
|----------|-------------|
| `recvPort` | The receive port to attempt to match, in the form of an [Integer](../Classes/Integer.md). |  
| `func` | The [Function](../Classes/Function.md) to evaluate if a match is found. |  
**Returns:** An OSCFuncRecvPortMessageMatcher.

## Instance Methods

### `value`
Check to see if a message matches, and evaluate func if it does.**Arguments:**

| Argument | Description |
|----------|-------------|
| `msg` | The OSC message as an [Array](../Classes/Array.md) in the form `[OSCAddress, other args]`. |  
| `time` | A [Float](../Classes/Float.md) indicating the time the incoming message was sent. |  
| `addr` | A [NetAddr](../Classes/NetAddr.md) indicating the source of the message. |  
| `testRecvPort` | An [Integer](../Classes/Integer.md) indicating the port on which the message was received. |  


