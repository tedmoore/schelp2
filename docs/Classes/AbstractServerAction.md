# AbstractServerAction

*register actions to be taken for a server*

**Related:** [Server](../Classes/Server.md), [ServerBoot](../Classes/ServerBoot.md), [ServerTree](../Classes/ServerTree.md), [ServerQuit](../Classes/ServerQuit.md)

**Categories:** Control

## Description

This is an **abstract superclass** for singletons like [ServerQuit](../Classes/ServerQuit.md), which provides a place for registering functions and objects for events that should happen when something happens in the server. No direct call to AbstractServerAction is required.

> **Note:** not fully working on Linux and windows. Setting the computer to sleep on these systems causes the actions to be called. As to date in Linux, JACK does not survive a sleep, it nevertheless behaves correctly for the time being.




## Class Methods

### `functionSelector`
Subclasses return specific function selectors for objects that implement this as interface. Selectors are:- doOnServerBoot - [ServerBoot](../Classes/ServerBoot.md)
- doOnServerQuit - [ServerQuit](../Classes/ServerQuit.md)
- doOnServerTree - [ServerTree](../Classes/ServerTree.md)
not for registry with a server, but analogous are:- doOnCmdPeriod - [CmdPeriod](../Classes/CmdPeriod.md)
- doOnStartUp - [StartUp](../Classes/StartUp.md)
- doOnShutDown - [ShutDown](../Classes/ShutDown.md)

### `add`
Add an action or object for registry.**Arguments:**

| Argument | Description |
|----------|-------------|
| `object` | Can either be a [Function](../Classes/Function.md) to be evaluated (as first arg the server is passed in), or an [Object](../Classes/Object.md) that implements the message returned by [#-functionSelector](#-functionselector). **One object is only registered once**, so that multiple additions don't cause multiple calls. |  
| `server` | Server for which to register. If the symbol **\default** is passed in, the action is called for the current default server. If the symbol **\all** is passed in, the action is called for all current servers. If server is nil, it is added to \all. |  

### `remove`
Remove an item or object from registry. If server is nil, remove from **all** key.
### `removeServer`
Remove all items that are registered for a given server.
## Examples


```supercollider
// ServerBoot
s.boot;
f = { |server| "------------The server '%' has booted.------------\n".postf(server) };
ServerBoot.add(f, \default);
s.quit; // quit the server and observe the post
s.boot;
ServerBoot.remove(f, \default); // remove it again
s.quit;
s.boot; // no post.
ServerBoot.add(f, Server.internal);
Server.internal.quit;
Server.internal.boot;
ServerBoot.removeAll; // clear all
```



```supercollider
// ServerQuit
s.boot;
f = { |server| "------------The server '%' has quit.------------\n".postf(server) };
ServerQuit.add(f, \default);
s.quit; // quit the server and observe the post
s.boot;
ServerQuit.remove(f, \default); // remove it again
s.quit; // no post.
ServerQuit.add(f, Server.internal);
Server.internal.boot;
Server.internal.quit;
ServerQuit.removeAll; // clear all
```



```supercollider
// ServerTree
s.quit;
f = { |server| "-------The server '%' has initialised tree.-------\n".postf(server) };
g = { |server| 10.do { Group(server).postln } };
ServerBoot.add(f, \default);
ServerTree.add(g, \default);
s.boot; // boot and see how the actions are evaluated in order
// "cmd-period" (or equivalent) resends the groups.

ServerBoot.removeAll; // clear all
ServerTree.removeAll; // clear all
```




