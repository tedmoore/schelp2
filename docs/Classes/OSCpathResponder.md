# OSCpathResponder

*client side network responder*

**Related:** [OSCFunc](../Classes/OSCFunc.md), [OSCdef](../Classes/OSCdef.md), [OSC_communication](../Guides/OSC_communication.md), [OSCresponderNode](../Classes/OSCresponderNode.md)

**Categories:** External Control>OSC

## Description


> **Note:** This class is deprecated and will be removed in a future version of SC. Use [OSCFunc](../Classes/OSCFunc.md) and [OSCdef](../Classes/OSCdef.md) instead. They are faster, safer, and have more logical argument order than the old responder classes, and they support pattern matching and custom listening ports. Use of the older classes OSCresponder, OSCresponderNode, and OSCpathResponder can be unsafe, since responders in user and class code can override each other unintentionally.The replacement for path matching is to be found in the template argument of OSCFunc and OSCDef (see example below).


Register a function to be called upon receiving a command with a specific path.
Other applications sending messages to SuperCollider should distinguish between sending messages to the server or the language. Server messages are documented in the [Server-Command-Reference](../Reference/Server-Command-Reference.md) and should be sent to the server's port - `s.addr.port` - which is **57110** by default. Messages sent to the server will not be processed by any [OSCresponder](../Classes/OSCresponder.md) in the language.
Messages from external clients that should be processed by OSCresponders must be sent to the language port, **57120** by default. Use `NetAddr.langPort` to confirm which port the SuperCollider language is listening on.
See [OSC_communication](../Guides/OSC_communication.md) for more details.

### Command paths
OSC commands sometimes include additional parameters to specify the right responder.

For example `/tr` commands, which are generated on the server by the [SendTrig](../Classes/SendTrig.md) UGen create an OSC packet consisting of: `[/tr, nodeID, triggerID, value]`. This array actually specifies the source of value: `[/tr, nodeID, triggerID]`. We will refer to that array as a command path.

To create an OSCpathResponder for a specific trigger, the **cmdName** parameter is simply replaced by the complete command path.



### Path defaults
Any element of the command path array can be set to nil to create a responder that will handle multiple command paths.

For example, setting the commandpath: `['/tr', nil, triggerID]` makes a responder that responds to `/tr` messages from any Synth but with a specific triggerID.




## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `addr` | An instance of [NetAddr](../Classes/NetAddr.md), usually obtained from your server: server-addr. An address of nil will respond to messages from anywhere. |  
| `cmdPath` | A command path, such as ['\c_set', bus index]. |  
| `action` | A [Function](../Classes/Function.md) that will be evaluated when a cmd of that name is received from addr. arguments: time, theResponder, message
> **Note:** OSCresponderNode evaluates its function in the system process. In order to access the application process (e.g. for GUI access) use { ... }.defer; within the action function, e.g., `{ |time, resp, msg| { gui.value_(msg[3]) }.defer }` |  

## Examples


```supercollider
s.boot;

(
    var commandpath, response, aSynth, nodeID, triggerID;
    triggerID = 1;
    aSynth = { |freq = 1, triggerID = 1|
        SendTrig.kr(SinOsc.kr(freq), triggerID, 666)
    }.play;
    nodeID = aSynth.nodeID;
    commandpath = ['/tr', nodeID, triggerID];
    response = { |time, responder, message| message.postln };

    o = OSCpathResponder(s.addr, commandpath, response);
    o.add;
)

// switch on and off:
o.remove;
o.add;


// this can be written now conveniently and efficiently with OSCFunc.
// the argTemplate is like the "path" of OSCpathResponder, but without the OSC-path itself.
(
    var commandpath, response, aSynth, nodeID, triggerID;
    triggerID = 1;
    aSynth = { |freq = 1, triggerID = 1|
        SendTrig.kr(SinOsc.kr(freq), triggerID, 666)
    }.play;
    nodeID = aSynth.nodeID;
    commandpath = [nodeID, triggerID];
    response = { |message| message.postln };

    o = OSCFunc(response, '/tr', s.addr, argTemplate: commandpath);

)

// an OSCFunc is removed with cmd-Period.
// in order to switch it on and off programmatically:
o.remove;
o.add;
```




