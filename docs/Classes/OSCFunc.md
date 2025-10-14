# OSCFunc

*Fast Responder for incoming Open Sound Control Messages*

**Categories:** External Control>OSC

**Related:** [OSC_communication](../Guides/OSC_communication.md), [OSCdef](../Classes/OSCdef.md), [NetAddr](../Classes/NetAddr.md)

## Description

OSCFunc (and its subclass [OSCdef](../Classes/OSCdef.md)) registers one or more functions to respond to an incoming OSC message which matches a specified OSC Address. Many of its methods are inherited from its superclass [AbstractResponderFunc](../Classes/AbstractResponderFunc.md). OSCFunc supports pattern matching of wildcards etc. in incoming messages. For efficiency reasons you must specify that an OSCFunc will employ pattern matching by creating it with the [#*newMatching](#*newmatching) method, or by passing a matching dispatcher to [#*new](#*new). For details on the Open Sound Control protocol, see [http://opensoundcontrol.org/spec-1_0.html](http://opensoundcontrol.org/spec-1_0.html)


## Class Methods


### `defaultDispatcher`
Get or set the default dispatcher object for OSCFuncs (this is what you get if you pass nil as the dispatcher argument to [#*new](#*new)). This object will decide if any of its registered OSCFuncs should respond to an incoming OSC message.**Returns:** By default this will be an [OSCMessageDispatcher](../Classes/OSCMessageDispatcher.md), but it can be set to any instance of an appropriate subclass of [AbstractDispatcher](../Classes/AbstractDispatcher.md).
### `defaultMatchingDispatcher`
Get or set the default matching dispatcher object for OSCFuncs (this is what you get if when you create an OSCFunc using [#*newMatching](#*newmatching)). This object will decide if any of its registered OSCFuncs should respond to an incoming OSC message using pattern matching.**Returns:** By default this will be an [OSCMessagePatternDispatcher](../Classes/OSCMessagePatternDispatcher.md), but it can be set to any instance of an appropriate subclass of [AbstractDispatcher](../Classes/AbstractDispatcher.md).
### `new`
Create a new, enabled OSCFunc.**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | A [Function](../Classes/Function.md) or similar object which will respond to the incoming message. When evaluated it will be passed the following arguments:| msg | message as an [Array](../Classes/Array.md) in the form `[OSC address, args1, arg2, ...]` | 
| --- | --- || time | the time received (for messages) / the time sent plus the latency (if the message was in a bundle) | | addr | a [NetAddr](../Classes/NetAddr.md) corresponding to the IP address of the **sender** | | recvPort | [Integer](../Classes/Integer.md) corresponding to the port on which the message was **received**. | |  
| `path` | A [Symbol](../Classes/Symbol.md) indicating the path of the OSC address of this object. Note that OSCFunc demands OSC compliant addresses. If the path does not begin with a / one will be added automatically. |  
| `srcID` | An optional instance of [NetAddr](../Classes/NetAddr.md) indicating the IP address of the sender. If set this object will only respond to messages from that source. |  
| `recvPort` | An optional [Integer](../Classes/Integer.md) indicating the port on which messages will be received. If set this object will only respond to message received on that port. This method calls [Main#-openUDPPort](../Classes/Main.md#-openudpport) to ensure that the port is opened. |  
| `argTemplate` | An optional [Array](../Classes/Array.md) composed of instances of [Integer](../Classes/Integer.md) or [Function](../Classes/Function.md) (or objects which respond to the method [Methods / matchItem ](../Overviews/Methods.md#matchitem)) used to match the arguments of an incoming OSC message. If a Function, it will be evaluated with the corresponding message arg as an argument, and should return a [Boolean](../Classes/Boolean.md) indicating whether the argument matches and this OSCFunc should respond (providing all other arguments match). Template values of nil will match any incoming argument value. |  
| `dispatcher` | An optional instance of an appropriate subclass of [AbstractDispatcher](../Classes/AbstractDispatcher.md). This can be used to allow for customised dispatching. Normally this should not be needed. |  
**Returns:** A new instance of OSCFunc.
### `newMatching`
A convenience method to create a new, enabled OSCFunc whose dispatcher will perform pattern matching on incoming OSC messages to see if their address patterns match this object's path.**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | A [Function](../Classes/Function.md) or similar object which will respond to the incoming message. When evaluated it will be passed the arguments msg, time, addr, and recvPort, corresponding to the message as an [Array](../Classes/Array.md) [OSCAddress, other args], the time that the message was sent, a [NetAddr](../Classes/NetAddr.md) corresponding to the IP address of the sender, and an [Integer](../Classes/Integer.md) corresponding to the port on which the message was received. |  
| `path` | A [Symbol](../Classes/Symbol.md) indicating the path of the OSC address of this object. Note that OSCFunc demands OSC compliant addresses. If the path does not begin with a / one will be added automatically. Pattern matching will be applied to any incoming messages to see if they match this address. Note that according to the OSC spec, regular expression wildcards are only permitted in the incoming message's address pattern. Thus path should not contain wildcards. For more details on OSC pattern matching, see [http://opensoundcontrol.org/spec-1_0](http://opensoundcontrol.org/spec-1_0) |  
| `srcID` | An optional instance of [NetAddr](../Classes/NetAddr.md) indicating the IP address of the sender. If set this object will only respond to messages from that source. |  
| `recvPort` | An optional [Integer](../Classes/Integer.md) indicating the port on which messages will be received. |  
| `argTemplate` | An optional [Array](../Classes/Array.md) composed of instances of [Integer](../Classes/Integer.md) or [Function](../Classes/Function.md) (or objects which respond to the method [Methods / matchItem ](../Overviews/Methods.md#matchitem)) used to match the arguments of an incoming OSC message. If a Function, it will be evaluated with the corresponding message arg as an argument, and should return a [Boolean](../Classes/Boolean.md) indicating whether the argument matches and this OSCFunc should respond (providing all other arguments match). Template values of nil will match any incoming argument value. |  
**Returns:** A new instance of OSCFunc.
### `trace`
A convenience method which dumps all incoming OSC messages.**Arguments:**

| Argument | Description |
|----------|-------------|
| `bool` | A [Boolean](../Classes/Boolean.md) indicating whether dumping is on or off. |  
| `hideStatusMsg` | A [Boolean](../Classes/Boolean.md) indicating whether server status messages are excluded from the dump or not. |  


## Instance Methods

### `path`
Get the path of this OSCFunc's OSC Address.**Returns:** A [String](../Classes/String.md)### `recvPort`
Get this OSCFunc's receiving port.**Returns:** An [Integer](../Classes/Integer.md)
## Examples


```supercollider
n = NetAddr("127.0.0.1", NetAddr.langPort); // local machine

OSCFunc.newMatching({ |msg, time, addr, recvPort| \matching.postln }, '/chat', n); // path matching
OSCFunc({ |msg, time, addr, recvPort| \oneShot.postln }, '/chat', n).oneShot; // once only
OSCdef(\test, { |msg, time, addr, recvPort| \unmatching.postln }, '/chat', n); // def style

m = NetAddr("127.0.0.1", NetAddr.langPort); // loopback

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

//////// Use an argTemplate for finer grained matching

s.boot;
x = Synth(\default);
OSCFunc({ 'ended!'.postln }, '/n_end', s.addr, nil, [x.nodeID]).oneShot;
x.release(3);
```




