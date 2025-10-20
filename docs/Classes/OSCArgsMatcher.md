# OSCArgsMatcher

*Test for specific OSC arguments before evaluating a Function*

**Categories:** External Control>OSC>Matchers

**Related:** [OSCFunc](../Classes/OSCFunc.md), [OSC_communication](../Guides/OSC_communication.md)

## Description

OSCArgMatcher matches an argument template to a [Function](../Classes/Function.md) or similar object. When its value method is called, it evaluates the function if all of the arguments in its template pass a [matchItem](../Reference/matchItem.md) test. This is used by [OSCMessageDispatcher](../Classes/OSCMessageDispatcher.md) and [OSCMessagePatternDispatcher](../Classes/OSCMessagePatternDispatcher.md) to match incoming OSC messages to instances of [OSCFunc](../Classes/OSCFunc.md) or [OSCdef](../Classes/OSCdef.md) using sender address. This class is private, and generally users should not need to address instances directly.


## Class Methods


### `new`
Make a new OSCArgsMatcher**Arguments:**

| Argument | Description |
|----------|-------------|
| `argTemplate` | An [Array](../Classes/Array.md) comprising a template for determining if incoming arguments match. For each argument that you wish to test, you may include a constant (for exact matching), `nil` (indicating that all possible values and types will match), or a [Function](../Classes/Function.md) to test the incoming argument (see [matchItem](../Reference/matchItem.md) for examples). These should be in the same order as the items in the incoming OSC message, starting from index 1. (Index 0 is the OSC address.) |  
| `func` | A [Function](../Classes/Function.md) or similar object which will respond to the incoming message. When evaluated it will be passed the arguments msg, time, addr, and recvPort, corresponding to the message as an [Array](../Classes/Array.md) in the form `[OSCAddress, ...otherArgs]`, the time that the message was sent, a [NetAddr](../Classes/NetAddr.md) corresponding to the IP address of the sender, and an [Integer](../Classes/Integer.md) corresponding to the port on which the message was received. |  


## Instance Methods


### `value`
Test if an incoming message's arguments match, and if so evaluate this object's function. In normal usage (within an OSCFunc) this is done behind the scenes.**Arguments:**

| Argument | Description |
|----------|-------------|
| `testMsg` | An [Array](../Classes/Array.md) in the form `[OSCAddress, …msgArgs]`. |  
| `time` | The time that the message was sent as a [Float](../Classes/Float.md). |  
| `addr` | A [NetAddr](../Classes/NetAddr.md) corresponding to the IP address of the sender. |  
| `recvPort` | An [Integer](../Classes/Integer.md) corresponding to the port on which the message was received. |  

## Examples


```
// Basic example (standalone use)
m = OSCArgsMatcher([1, nil, 2], { 'matches!'.postln });
m.value(['/myAddress', 1, 3, 2], 0.0, NetAddr.localAddr, NetAddr.langPort); // matches!
```




