# OSCdef

*OSC response reference definition*

**Categories:** External Control>OSC>Dispatchers

**Related:** [OSC_communication](../Guides/OSC_communication.md), [OSCFunc](../Classes/OSCFunc.md), [NetAddr](../Classes/NetAddr.md)

## Description

OSCdef provides a global reference to the functionality of its superclass [OSCFunc](../Classes/OSCFunc.md). Essentially it stores itself at a key within a global dictionary, allowing replacement at any time. Most methods are inherited from its superclass.


## Class Methods



### `all`
Get the global dictionary of all OSCdefs.**Returns:** An [IdentityDictionary](../Classes/IdentityDictionary.md).

### `new`
Create a new, enabled OSCdef. If an OSCdef already exists at this key, its parameters will be replaced with the ones provided (args for which nil is passed will use the old values).**Arguments:**

| Argument | Description |
|----------|-------------|
| `key` | The key at which to store this OSCdef in the global collection. Generally this will be a [Symbol](../Classes/Symbol.md). |  
| `func` | A [Function](../Classes/Function.md) or similar object which will respond to the incoming message. When evaluated it will be passed the following arguments:| msg | message as an [Array](../Classes/Array.md) in the form `[OSC address, args1, arg2, ...]` | 
| --- | --- || time | the time received (for messages) / the OSC bundle's timestamp (if the message was in a bundle) | | addr | a [NetAddr](../Classes/NetAddr.md) corresponding to the IP address of the **sender** | | recvPort | [Integer](../Classes/Integer.md) corresponding to the port on which the message was **received**. | |  
| `path` | A [Symbol](../Classes/Symbol.md) indicating the path of the OSC address of this object. Note that OSCdef demands OSC compliant addresses. If the path does not begin with a / one will be added automatically. |  
| `srcID` | An optional instance of [NetAddr](../Classes/NetAddr.md) indicating the IP address of the sender. If set this object will only respond to messages from that source. |  
| `recvPort` | An optional [Integer](../Classes/Integer.md) indicating the port on which messages will be received. If set this object will only respond to message received on that port. This method calls [Main#-openUDPPort](../Classes/Main.md#-openudpport) to ensure that the port is opened. |  
| `argTemplate` | An optional [Array](../Classes/Array.md) composed of instances of [Integer](../Classes/Integer.md) or [Function](../Classes/Function.md) (or objects which respond to the method [Methods#matchItem](../Overviews/Methods.md#matchitem)) used to match the arguments of an incoming OSC message. If a Function, it will be evaluated with the corresponding message arg as an argument, and should return a [Boolean](../Classes/Boolean.md) indicating whether the argument matches and this OSCdef should respond (providing all other arguments match). Template values of nil will match any incoming argument value. |  
| `dispatcher` | An optional instance of an appropriate subclass of [AbstractDispatcher](../Classes/AbstractDispatcher.md). This can be used to allow for customised dispatching. Normally this should not be needed. |  
**Returns:** An instance of OSCdef.

### `newMatching`
A convenience method to create a new, enabled OSCdef whose dispatcher will perform pattern matching on incoming OSC messages to see if their address patterns match this object's path.**Arguments:**

| Argument | Description |
|----------|-------------|
| `key` | The key at which to store this OSCdef in the global collection. Generally this will be a [Symbol](../Classes/Symbol.md). |  
| `func` | A [Function](../Classes/Function.md) or similar object which will respond to the incoming message. When evaluated it will be passed the arguments msg, time, addr, and recvPort, corresponding to the message as an [Array](../Classes/Array.md) [OSC address, args1, arg2, ...], the time that the message was sent, a [NetAddr](../Classes/NetAddr.md) corresponding to the IP address of the sender, and an [Integer](../Classes/Integer.md) corresponding to the port on which the message was received. |  
| `path` | A [Symbol](../Classes/Symbol.md) indicating the path of the OSC address of this object. Note that OSCdef demands OSC compliant addresses. If the path does not begin with a / one will be added automatically. Pattern matching will be applied to any incoming messages to see if they match this address. Note that according to the OSC spec, regular expression wildcards are only permitted in the incoming message's address pattern. Thus path should not contain wildcards. For more details on OSC pattern matching, see [http://opensoundcontrol.org/spec-1_0](http://opensoundcontrol.org/spec-1_0) |  
| `srcID` | An optional instance of [NetAddr](../Classes/NetAddr.md) indicating the IP address of the sender. If set this object will only respond to messages from that source. |  
| `recvPort` | An optional [Integer](../Classes/Integer.md) indicating the port on which messages will be received. |  
| `argTemplate` | An optional [Array](../Classes/Array.md) composed of instances of [Integer](../Classes/Integer.md) or [Function](../Classes/Function.md) (or objects which respond to the method [Methods#matchItem](../Overviews/Methods.md#matchitem)) used to match the arguments of an incoming OSC message. If a Function, it will be evaluated with the corresponding message arg as an argument, and should return a [Boolean](../Classes/Boolean.md) indicating whether the argument matches and this OSCFunc should respond (providing all other arguments match). Template values of nil will match any incoming argument value. |  
**Returns:** An instance of OSCdef.

### `freeAll`
Clears and deactivates all OSCdefs from the global collection.

## Instance Methods


### `key`
Get this OSCdef's key.**Returns:** Usually a [Symbol](../Classes/Symbol.md).
### `free`
Clears this OSCdef from the global collection and deactivates it.

## Timing in incoming bundles
The time argument indicates the time the message was sent plus, if given, the latency added to the bundle:


```
(
OSCdef(\x, { |msg, time|
    "reception time: %\nscheduling time: %\ndelta: %\n\n".postf(Main.elapsedTime, time, time - Main.elapsedTime)
}, \time);

n = NetAddr("127.0.0.1", 57120);
)

(
n.sendBundle(0.0, [\time]);
n.sendBundle(1.0, [\time]);
)
```



## Examples


```
n = NetAddr("127.0.0.1", 57120); // local machine

OSCdef(\test, { |msg, time, addr, recvPort| \unmatching.postln }, '/chat', n); // def style
OSCdef.newMatching(\test2, { |msg, time, addr, recvPort| \matching.postln }, '/chat', n); // path matching
OSCdef(\test3, { |msg, time, addr, recvPort| \oneShot.postln }, '/chat', n).oneShot; // once only


m = NetAddr("127.0.0.1", 57120); // loopback

m.sendMsg("/chat", "Hello App 1");
m.sendMsg("/chat", "Hello App 1"); // oneshot gone
m.sendMsg("/ch?t", "Hello App 1");
m.sendMsg("/*", "Hello App 1");
m.sendMsg("/chit", "Hello App 1"); // nothing

// Introspection

AbstractResponderFunc.allFuncProxies
AbstractResponderFunc.allEnabled
OSCdef(\test).disable;
AbstractResponderFunc.allDisabled

// change funcs
OSCdef(\test).enable;
OSCdef(\test, { |msg, time, addr, recvPort| 'Changed Unmatching'.postln }, '/chat', n); // replace at key \test
m.sendMsg("/chat", "Hello App 1");
OSCdef(\test).add(f = { \foo.postln }); // add another func
m.sendMsg("/chat", "Hello App 1");
OSCdef(\test).clear; // remove all functions
m.sendMsg("/chat", "Hello App 1");
OSCdef(\test).free;  // unregister OSCdef


//////// Use an argTemplate for finer grained matching

s.boot;
x = Synth(\default);
OSCdef(\watchForXEnd, { 'ended!'.postln }, '/n_end', s.addr, nil, [x.nodeID]).oneShot;
x.release(3);

// Args for which nil is passed will use the old values. While this facilitates swapping only parts of an OSCdef, such as the function, it also means you will have to free and recreate an OSCdef to remove parts.

OSCdef(\argtest, { |msg ... args| msg[1].postln }, '/hey', argTemplate: ['you']);
m.sendMsg("/hey", "you"); // oscdef will respond
m.sendMsg("/hey", "there"); // oscdef will not respond, filtered out by argTemplate

OSCdef(\argtest, argTemplate: nil); // this has no effect
m.sendMsg("/hey", "you"); // oscdef will respond
m.sendMsg("/hey", "there"); // oscdef will not respond, still filtered out by argTemplate

OSCdef(\argtest).free; // in order to get rid of the argTemplate, free the def...
OSCdef(\argtest, { |msg ... args| msg[1].postln }, '/hey'); // ... and recreate it.
m.sendMsg("/hey", "you"); // oscdef will respond
m.sendMsg("/hey", "there"); // oscdef will respond
```




