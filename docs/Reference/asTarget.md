# asTarget

*Convert to a valid Node Target*

**Categories:** Server>Nodes

**Related:** [Node](../Classes/Node.md)


### `asTarget`
The classes listed below implement the method `asTarget`. This is used widely in the [Node](../Classes/Node.md) classes ( [Group](../Classes/Group.md) and [Synth](../Classes/Synth.md) ) to convert non-Node objects to an appropriate target. This allows nil and instances of [Server](../Classes/Server.md) to be used as targets. This can be useful when writing classes which create nodes internally, but in most cases there should be little need to call asTarget in normal use.For an updated list of which classes that implements `asTarget`, see asTarget in [Methods#asTarget](../Overviews/Methods.md#astarget)
**[Node#-asTarget](../Classes/Node.md#-astarget)**
: Returns the instance of Node itself. The subclasses of Node (Synth and Group) are valid targets and require no conversion.

**[Server#-asTarget](../Classes/Server.md#-astarget)**
: Returns a [Group](../Classes/Group.md) object representing the [default_group](../Reference/default_group.md) of this instance of Server. Note that this object may not be identical with other objects representing the default group, but will be equivalent.
```
s = Server.default;
g = s.asTarget;     // the default group of s
h = s.defaultGroup; // and again
g == h;             // true
g === h;            // false
```

**[Nil#-asTarget](../Classes/Nil.md#-astarget)**
: Returns a [Group](../Classes/Group.md) object representing the [default_group](../Reference/default_group.md) of the current default [Server](../Classes/Server.md).
```
s = Server.default;
g = nil.asTarget;
g == s.defaultGroup; // true
```

**[Integer#-asTarget](../Classes/Integer.md#-astarget)**
: Returns a [Group](../Classes/Group.md) object representing a group node on the current default Server with this Integer as its node ID number.
> **Note:** Although this can be convenient in some cases, it does not create the corresponding node on the default server, nor does it check to make sure that it exists. As well it does not directly access the server's NodeIDAllocator, so duplication of node IDs is possible. For these reasons this method should be used with care. When not dealing with the default Server, Group-basicNew is safer and simpler, as otherwise one needs to set the server instance variable to ensure correct targeting.


```
/////// Showing the problems

s = Server.default;
s.boot;
g = s.nextNodeID.asTarget;
x = Synth.head(g, "default");   // but g doesn't exist on the server
s.sendMsg(*g.addToHeadMsg);     // now it's sent to the default server, in the default group
x = Synth.head(g, "default");   // now this works
x.free; g.free;

// if not using the default Server Integer-asTarget can be problematic

Server.default = Server.local;
Server.default.boot;            // quit the default server
i = Server.internal; i.boot;
g = i.nextNodeID.asTarget;
i.sendMsg(*g.addToHeadMsg);     // seems to work, but...
x = Synth.head(g, "default");   // oops, this goes to the default server, so Group not Found
g.server == Server.default;     // true, so that's the problem
g.server = i;
x = Synth.head(g, "default");   // now to the right place
x.free; g.free;
```


```
/////// A more practical example

s = Server.default;
s.boot;
s.sendMsg(\g_new, x = s.nextNodeID);
// ...

// now if we need to use Node objects for some reason
y = Synth.head(x.asTarget, "default");

// this is simpler than Group.basicNew(s, x);, providing you're using the default server:
z = Synth.head(Group.basicNew(s, x), "default");

y.free; z.free; x.asTarget.free;
```


