# OSCresponder

*client side network responder*

**Related:** [OSCFunc](../Classes/OSCFunc.md), [OSCdef](../Classes/OSCdef.md), [OSC_communication](../Guides/OSC_communication.md), [OSCresponderNode](../Classes/OSCresponderNode.md), [NetAddr](../Classes/NetAddr.md)

**Categories:** External Control>OSC


> **Note:** This class is deprecated and will be removed in a future version of SC. Use [OSCFunc](../Classes/OSCFunc.md) and [OSCdef](../Classes/OSCdef.md) instead. They are faster, safer, and have more logical argument order than the old responder classes, and they support pattern matching and custom listening ports. Use of the older classes OSCresponder, OSCresponderNode, and OSCpathResponder can be unsafe, since responders in user and class code can override each other unintentionally.


Register a function to be called upon receiving a specific command from a specific OSC address.
Other applications sending messages to SuperCollider should distinguish between sending messages to the server or the language. Server messages are documented in the [Server-Command-Reference](../Reference/Server-Command-Reference.md) and should be sent to the server's port - `s.addr.port` - which is **57110** by default. Messages sent to the server will not be processed by any OSCresponder in the language.
Messages from external clients that should be processed by OSCresponders must be sent to the language port, **57120** by default. Use `NetAddr.langPort` to confirm which port the SuperCollider language is listening on.
See [OSC_communication](../Guides/OSC_communication.md) for more details.

> **Note:** It is highly recommended to use [OSCresponderNode](../Classes/OSCresponderNode.md) or [OSCpathResponder](../Classes/OSCpathResponder.md) instead of OSCresponder directly. OSCresponders can overwrite each other, but OSCresponderNodes with the same address and command name can coexist peacefully.



## Class Methods



### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `addr` | The address the responder **receives from** (an instance of [NetAddr](../Classes/NetAddr.md), e.g. `Server.default.addr`). An address of nil will respond to messages from anywhere. An address with a port of nil will respond to messages from any port from that specific IP. |  
| `cmdName` | An OSC command eg. `'/done'`. |  
| `action` | A [Function](../Classes/Function.md) that will be evaluated when a cmd of that name is received from addr. arguments: time, theResponder, message, addr
> **Note:** OSCresponder evaluates its function in the system process. In order to access the application process (e.g. for GUI access) use { ... }.defer; within the action function, e.g., `{ |time, resp, msg| { gui.value_(msg[3]) }.defer }` |  

## Examples

see [OSCresponderNode](../Classes/OSCresponderNode.md).

