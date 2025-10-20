# Default Group

*An automatically created Group in sclang*

**Categories:** Server>Nodes

**Related:** [Group](../Classes/Group.md), [RootNode](../Classes/RootNode.md), [Node](../Classes/Node.md), [NodeMessaging](../Guides/NodeMessaging.md), [Order-of-execution](../Guides/Order-of-execution.md)

root node (id:0)default group (id:1)When a Server is booted, there is a top level group with an ID of 0 that defines the root of the tree. This is represented by a subclass of Group: [RootNode](../Classes/RootNode.md).
Separate from the root group is sclang's notion of a "default group," which is automatically created when the server is booted. You can access it with the method [Server#-defaultGroup](../Classes/Server.md#-defaultgroup). This group is the default enclosing group for all Nodes, i.e. it's what you get if you don't specify. In general, you should create new Nodes within the default group of a Server rather than in its RootNode. In a single-client setup, the default group will have an ID of 1.
Keep in mind that default groups are a client-side concept, and you are responsible for creating them if you're running scsynth from the command line or NRT mode, or developing an alternate client.> *When booting the server from the command line, you can create the default group manually with:
```
s.initTree;
```

*
This is the default target for all Nodes when using object style and is what you will get if you supply a [Server](../Classes/Server.md) as a target. If you don't specify a target or pass in nil, you will get the default group of the default Server.

```
s.boot;
a = Synth.new(\default); // creates a synth in the default group of the default Server
a.group; // note the Group ID
a.group == Server.default.defaultGroup;
// -> true
```

The default group serves an important purpose: It provides a predictable basic Node tree so that methods such as Server-scope, Server-record, etc. can function without running into order of execution problems. In the example below the scoping node will come after the default group.

```
s.boot;

{ SinOsc.ar(mul: 0.2) }.scope(1);

// watch the post window;
s.queryAllNodes;

// our SinOsc synth is within the default group (ID 1)
// the scope node comes after the default group, so no problems

s.quit;
```

Note that the default group is persistent: It is created in Server's `initTree` method (executed along with any code stored in its tree instance variable; see Server for more detail) and is recreated upon reboot, after pressing Cmd-., and after all nodes are freed. When using osc messages this means that a target node of id 1 can always be used:

```
s.sendMsg("/s_new", "snd", 1832,0,1); // add to head of group 1
```

The default group can be specifically freed, but there is generally no reason that one would want to do so.
In general one should add nodes to the default group rather than the RootNode unless one has a specific reason to do so (i.e. adding some new functionality such as recording and scoping which is dependent upon a predictable basic node order). When using object style the default group is the default target for all new nodes, so nodes will normally not be added to the RootNode unless that is explicitly specified. It is of course possible to do so, but it should only be done with a proper understanding of the issues involved.
For instance, if one were to place an 'effects' synth after the default group and call Server-record or Server-scope, the resulting recording or scope synths may not be correctly ordered:
default groupsource synth1source synth2recording syntheffects synthIn the above example the recording synth might not capture the output of the effects synth since it comes later in the node order.
A better method in this case is to create a group within the default group and place the effects synth after that.
default groupsource groupsource synth1source synth2effects synthrecording synth
## Default groups in multi-client setups
See [MultiClient_Setups](../Guides/MultiClient_Setups.md) for more info.

The default group mechanism is also used to separate clients in a multi-client setup. Every client registering with a server has its own individual default group. All nodes belonging to one client are in its default group and can be specifically addressed.

This keeps nodes cleanly separated by default, but a client also knows the default groups of all other clients. This is accessible via the method [Server#-defaultGroups](../Classes/Server.md#-defaultgroups), which is an array mapping client IDs to default groups.



