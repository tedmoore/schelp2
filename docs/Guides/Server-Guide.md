# Server Guide

*Using Server objects in different situations*

**Categories:** Server>Abstractions

**Related:** [Server](../Classes/Server.md), [ServerOptions](../Classes/ServerOptions.md), [Server-Architecture](../Reference/Server-Architecture.md), [Server-Command-Reference](../Reference/Server-Command-Reference.md), [MultiClient_Setups](../Guides/MultiClient_Setups.md)

## Description

A Server object is the client-side representation of a server app and is used to control the app from the SuperCollider language application. (See [ClientVsServer](../Guides/ClientVsServer.md) for more details on the distinction.) It forwards OSC messages and has a number of allocators that keep track of IDs for nodes, buses and buffers.
The server application is a commandline program, so all commands apart from OSC messages are UNIX commands.
The server application represented by a Server object might be running on the same machine as the client (in the same address space as the language application or separately; see below), or it may be running on a remote machine.
Most of a Server's options are contolled through its instance of ServerOptions. See the [ServerOptions](../Classes/ServerOptions.md) helpfile for more detail.

### Paths
Server apps running on the local machine have two UNIX environment variables: `SC_SYNTHDEF_PATH` and `SC_PLUGIN_PATH`. These indicate directories of synthdefs and ugen plugins that will be loaded at startup. These are in addition to the default synthdef/ and plugin/ directories which are hard-coded.

These can be set within SC using the getenv and setenv methods of class [String](../Classes/String.md).


```
// all defs in this directory will be loaded when a local server boots
"SC_SYNTHDEF_PATH".setenv("~/scwork/".standardizePath);
"echo $SC_SYNTHDEF_PATH".unixCmd;
```




### The default group
When a Server is booted there is a top level group with an ID of 0 that defines the root of the node tree. (This is represented by a subclass of [Group](../Classes/Group.md) : [RootNode](../Classes/RootNode.md).) If the server app was booted from within SCLang (as opposed to from the command line) the method `initTree` will be called automatically after booting. This will also create a [default_group](../Reference/default_group.md) with an ID of 1, which is the default group for all [Node](../Classes/Node.md)s when using object style. This provides a predictable basic node tree so that methods such as Server-scope, Server-record, etc. can function without running into order of execution problems.

The default group is persistent, i.e. it is recreated after a reboot, pressing cmd-., etc. See [RootNode](../Classes/RootNode.md) and [default_group](../Reference/default_group.md) for more information.


> **Note:** If a Server has been booted from the command line you must call `initTree` manually in order to initialize the default group, if you want it. See `initTree` below.




### Local vs. Internal
In general, when working with a single machine one will probably be using one of two Server objects which are created at startup and stored in the class variables [*local](../Classes/Server.md#*local) and [*internal](../Classes/Server.md#*internal). In SuperCollider.app (OSX), two GUI windows are created to control these. Use [-makeGui](../Classes/Server.md#-makegui) to create a GUI window manually.

The difference between the two is that the local server runs as a separate application with its own address space, and the internal server runs within the same space as the language/client app.

Both local and internal server supports [scoping](../Classes/Server.md#-scope) and [synchronous bus access](../Classes/Bus.md#synchronous-control-bus-methods).

The local server, and any other server apps running on your local machine, have the advantage that if the language app crashes, it (and thus possibly your piece) will continue to run. It is thus an inherently more robust arrangement. But note that even if the synths on the server continue to run, any language-side sequencing and control will terminate if the language app crashes.

At the current time, there is generally no benefit in using the internal server, but it remains for the purposes of backwards compatibility.



### The default Server
There is always a default Server, which is stored in the class variable `default`. Any [Synth](../Classes/Synth.md)s or [Group](../Classes/Group.md)s created without a target will be created on the default server. At startup this is set to be the local server (see above), but can be set to be any Server.



### Local vs. Remote Servers, Multi-client Configurations
Most of the time users work with a server app running on the same machine as the SC language client. It is possible to use a server running on a different machine via a network, providing you know the IP address and port of that server. The [*remote](../Classes/Server.md#*remote) method provides a convenient way to do this.


> **Note:** To enable remote connections you will need to change [ServerOptions#-bindAddress](../Classes/ServerOptions.md#-bindaddress) in the server's [ServerOptions](../Classes/ServerOptions.md) as the default value only allows connections from the local machine. `s.options.bindAddress = "0.0.0.0"` will allow connections from any address.


One common variant of this approach is multiple clients using the same server. If you wish to do this you will need to set the server's [ServerOptions#-maxLogins](../Classes/ServerOptions.md#-maxlogins) to at least the number of clients you wish to allow. When a client registers for [notifications](../Classes/Server.md#-notify) the server will supply a client ID. This also configures the allocators to avoid conflicts when allocating [Nodes](../Classes/Node.md), [Buffers](../Classes/Buffer.md), or [Busses](../Classes/Bus.md). For more info see [MultiClient_Setups](../Guides/MultiClient_Setups.md).

In order to use a remote server with tcp one should first boot the remote server using the `-t` option e.g. as follows:


```
// on machine running the server
(
s.options.protocol = \tcp; // set to use tcp
s.options.bindAddress = "0.0.0.0"; // allow connections from any address
s.options.maxLogins = 2; // set to correct number of clients
s.boot;
)
```


then run the following code:


```
// on remote machine connecting to server
(
o = ServerOptions.new;
o.protocol_(\tcp);
t = Server.remote(\remote, NetAddr("192.168.0.130", 57110), o); // set to correct address and port
t.addr.connect;
t.startAliveThread( 0 );
t.doWhenBooted({ "remote tcp server started".postln; t.notify; t.initTree });
)
```







