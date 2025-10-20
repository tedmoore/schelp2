# NodeWatcher

*notify sc-lang side node objects of their server sided state*

**Related:** [Server-Command-Reference](../Reference/Server-Command-Reference.md), [Node](../Classes/Node.md), [DebugNodeWatcher](../Classes/DebugNodeWatcher.md)

**Categories:** Control, Server>Nodes

## Description

Node instances (Synths and Groups) can be registered with the NodeWatcher. It watches for server node status messages: n_go n_end n_off n_on
and sets the isPlaying and isRunning variables on the Node instance accordingly. A Node that ends is unregistered at that time.
In some cases this can be an invaluable service. The use of an independant object to maintain the state keeps the implementation of the Node classes simple. Note that server notification should be on. (this is default. see: aServer.notify)

```
// the most common use:
NodeWatcher.register(aNode);
```




## Class Methods



### `new`
Create a new instance listening to the server's address

### `newFrom`
Create a new instance listening to the server's address. If there is one present already return that one.

### `register`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `node` | Can be a Group or a Synth. The NodeWatcher is created internally. |  
| `assumePlaying` | If true, the node's **isPlaying** field is set to true. |  


### `unregister`
Remove the node from the list of nodes. This happens also when a node is freed.

## Instance Methods


### `start`
Add the OSCFunc to listen to the address.
### `stop`
Remove the OSCFunc to stop listen to the address.
## Examples


```
(
b = s.makeBundle(false, {
    a = Group.new(s);    // create a node object
    NodeWatcher.register(a); // register before creating on the server
});
)
a.isPlaying;
s.listSendBundle(nil, b);    // start the node on the server
a.isPlaying;
a.isRunning;
a.run(false);
a.isRunning;
s.freeAll;    // free all nodes
a.isPlaying;
a.isRunning;
```




