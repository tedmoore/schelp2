# DebugNodeWatcher

*watches a server address for debug-related messages*

**Related:** [Server-Command-Reference](../Reference/Server-Command-Reference.md), [Node](../Classes/Node.md), [NodeWatcher](../Classes/NodeWatcher.md)

**Categories:** Control, Server>Nodes

## Description

Posts when these messages are received from the server: n_go n_end n_off n_on
For debugging, it can be useful to see every node start and end. It doesn't require registration, reacts to each message.

## Examples


```supercollider
s.boot;

d = DebugNodeWatcher(s);
d.start;

y = Group.new;
y.run(false);
y.free;

d.stop;
```




