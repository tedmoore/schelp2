# Server

*Object representing a server application*

**Categories:** Server>Abstractions

**Related:** [Server-Guide](../Guides/Server-Guide.md), [MultiClient_Setups](../Guides/MultiClient_Setups.md), [ServerOptions](../Classes/ServerOptions.md), [Server-Architecture](../Reference/Server-Architecture.md), [Server-Command-Reference](../Reference/Server-Command-Reference.md), [ServerStatusWatcher](../Classes/ServerStatusWatcher.md), [AudioDeviceSelection](../Reference/AudioDeviceSelection.md)

## Description

A Server object is a representation of a server application. It is used to control scsynth (or supernova) from the SuperCollider language. (See [Server-Guide](../Guides/Server-Guide.md), as well as [ClientVsServer](../Guides/ClientVsServer.md) for more details on the distinction.) It forwards OSC messages and has a number of allocators that keep track of IDs for nodes, buses, and buffers.
The server application represented by a Server object might be running on the same machine as the sclang, or it may be running on a remote machine.
Most of a Server's options are controlled through its instance of ServerOptions. See the [ServerOptions](../Classes/ServerOptions.md) helpfile for more detail.
A server also holds an instance of a [Recorder](../Classes/Recorder.md) (for recording output into a file) and a [Volume](../Classes/Volume.md) (main output level).

> **Note:** By default, there is always one default server, which is stored in the interpreter variable 's'. E.g. you can boot the default server by calling `s.boot`



```
s.boot;
{ SinOsc.ar * 0.1 }.play(s); // play a synth on the server
```


The server application may be in three different states: running, not running, or unresponsive (for example while loading large files from disk).

```
s.serverRunning // returns true if it is true
```



> **Note:** If you get the message `"Mismatched sample rates are not supported."` it may be helpful to follow these steps:1. Set your device to the sample rate you want.
2. Check the device name in the boot posting of the server.
3. Set both sample rate and device (`s.options.sampleRate = …; s.options.device = "…"`).
4. Reboot the server: `s.reboot`.


Some insights about common Server issues can be found on the FAQ [Server Issues](../Guides/UserFAQ.md#server-issues)


## Class Methods



### `new`
Create a new Server instance.**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` | a symbol; each Server object is stored in one global classvariable under its name. |  
| `addr` | an optional instance of [NetAddr](../Classes/NetAddr.md), providing host and port. The default is the localhost address using port 57110; the same as the local server. |  
| `options` | an optional instance of [ServerOptions](../Classes/ServerOptions.md). If `nil`, an instance of ServerOptions will be created, using the default values. |  
| `clientID` | an integer. In multi-client situations, every client can be given separate ranges for [Nodes](../Classes/Node.md), [Buffers](../Classes/Buffer.md), or [Busses](../Classes/Bus.md). In normal usage, the server will supply an ID automatically when a client registers for the [notifications](#-notify) so you should not need to supply one here. N.B. In multi-client situations, you will need to set the [ServerOptions#-maxLogins](../Classes/ServerOptions.md#-maxlogins) to at least the number of clients you wish to allow. This must be the same in the Server instances on every client. |  


### `remote`
Create a new Server instance corresponding to a server app running on a separate machine. This method assumes the remote app has been booted and starts listening immediately. You should not call [#-boot](#-boot) on an instance created using this method. [Server-Guide](../Guides/Server-Guide.md) and [MultiClient_Setups](../Guides/MultiClient_Setups.md) contain further information on this and multiclient usage.**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` | a symbol; each Server object is stored in one global classvariable under its name. |  
| `addr` | an optional instance of [NetAddr](../Classes/NetAddr.md), providing IP address of the remote machine and port the app is listening on. |  
| `options` | an optional instance of [ServerOptions](../Classes/ServerOptions.md). If `nil`, an instance of ServerOptions will be created, using the default values.
> **Note:** To enable remote connections you will need to change the option [ServerOptions#-bindAddress](../Classes/ServerOptions.md#-bindaddress) as the default value only allows connections from the local machine. `s.options.bindAddress = "0.0.0.0"` will allow connections from any address. |  
| `clientID` | an integer. In multi-client situations, every client can be given separate ranges for [Nodes](../Classes/Node.md), [Buffers](../Classes/Buffer.md), or [Busses](../Classes/Bus.md). In normal usage, the server will supply an ID automatically when a client registers for the [notifications](#-notify) so you should not need to supply one here. N.B. In multi-client situations, you will need to set the [ServerOptions#-maxLogins](../Classes/ServerOptions.md#-maxlogins) to at least the number of clients you wish to allow. This must be the same in the Server instances on every client.
```
// example usage:
// on machine running the server
(
s.options.bindAddress = "0.0.0.0"; // allow connections from any address
s.options.maxLogins = 2; // set to correct number of clients
s.boot;
)

// on remote machine connecting to server
(
o = ServerOptions.new;
o.maxLogins = 2;
t = Server.remote(\remote, NetAddr("192.168.0.130", 57110), o); // set to correct address and port
// info about returned client ID should be posted in the post window
t.makeWindow; // make a window for monitoring
)

// if you want to use the remote server without the need to explicitly pass it to e.g. Synth or Function -play, set it to be the default server:
//Server.default = t;

//otherwise, make some sound on the remote server 
{Resonz.ar(Saw.ar([100,101]), Line.kr(100,5000,10, doneAction: 2),mul: -12.dbamp)}.play(target: t); //use target to specify the remote server
``` |  


### `local`
get/set the local server, stored in classvar `local` (created already on initClass)

### `internal`
get/set the internal server, stored in classvar `internal` (created already on initClass) See: [Server-Guide](../Guides/Server-Guide.md)

### `default`
Get or set the default server. By default this is the local server (see above).Setting this will also assign it to the [Interpreter](../Classes/Interpreter.md) variable 's'.
```
// set the internal Server to be the default Server
Server.default = Server.internal;
s.postln; // internal
```



### Accessing all servers

### `all`
**Returns:** a [Set](../Classes/Set.md) containing all servers.
```
Server.all
```



### `allRunningServers`
**Returns:** a Set containing all running servers, according to the definition of [#-serverRunning](#-serverrunning).
```
Server.allRunningServers
```



### `allBootedServers`
**Returns:** a Set containing all booted servers, according to the definition of [#-hasBooted](#-hasbooted).

### `named`
**Returns:** An [IdentityDictionary](../Classes/IdentityDictionary.md) of all servers listed by their name
```
Server.named.at(\default)
```



### `quitAll`
quit all registered servers

### `killAll`
kill all the processes called "scsynth" and "supernova" in the system

### `freeAll`
free all nodes in all registered servers

### `hardFreeAll`
try to free all nodes in all registered servers, even if the server seems not to be running

### `sync_s`
If kept true (default), when the default server is changed, also the interpreter variable s is changed.
```
Server.default = Server(\alice, NetAddr("127.0.0.1", 57130));
s.postln; // see: it is alice.
```




### Switching the server application

### `supernova`
Switches the server program to supernova. Check [ParGroup](../Classes/ParGroup.md) how to make use of multicore hardware with the supernova server.

### `scsynth`
Switches the server program to scsynth. This is the default server.


## Instance Methods


### `sendMsg`
send an OSC-message to the server.
```
s.sendMsg("/s_new", "default", s.nextNodeID, 0, 1);
```


### `sendBundle`
send an OSC-bundle to the server.Since the network may have irregular performance, time allows for the bundle to be evaluated at a specified point in the future. Thus all messages are synchronous relative to each other, but delayed by a constant offset. If such a bundle arrives late, the server replies with a late message but still evaluates it.
```
s.sendBundle(0.2, ["/s_new", "default", x = s.nextNodeID, 0, 1], ["/n_set", x, "freq", 500]);
```


### `sendRaw`

### `listSendMsg`
as sendMsg, but takes an array as argument.
### `listSendBundle`
as sendBundle, but takes an array as argument.This allows you to collect messages in an array and then send them.
```
s.listSendBundle(0.2, [["/s_new", "default", x = s.nextNodeID, 0, 1],
    ["/n_set", x, "freq", 600]]);
```


### `sendSynthDef`
send a synthDef to the server that was written in a local directory
### `loadSynthDef`
load a synthDef that resides in the remote directory
### `loadDirectory`
load all the SynthDefs in the directory dir.**Arguments:**

| Argument | Description |
|----------|-------------|
| `dir` | a [String](../Classes/String.md) which is a valid path. |  
| `completionMsg` |  |  

### `nextNodeID`
get a unique nodeID.
### `nextPermNodeID`
get a permanent node ID. This node ID is in a reserved range and will be held until you explicitly free it.
### `freePermNodeID`
free a permanent node ID for later reuse.
### `wait`
this can be used within a [Routine](../Classes/Routine.md) to wait for a server reply
### `waitForBoot`
Evaluate "onComplete" as soon as the server has booted. This method will boot the server for you if it is not already running or booting. If the server is already running, "onComplete" is executed immediately.**Arguments:**

| Argument | Description |
|----------|-------------|
| `onComplete` | A function to evaluate after the server has booted successfully. |  
| `limit` | The number of times to check for a successful boot. (5 times/sec) |  
| `onFailure` | A function to evaluate after the server fails to boot. If onFailure is not given, an error message is posted. Providing a function suppresses the error message. If you want to supply a function and print the normal error message, make sure that your function returns "false," e.g. `s.waitForBoot(onFailure: { ... custom action...; false })`. |  
| `clock` | The default [Clock](../Classes/Clock.md) is [AppClock](../Classes/AppClock.md). Use [SystemClock](../Classes/SystemClock.md) or [TempoClock](../Classes/TempoClock.md) if time accuracy is important. |  
Refer to the discussion of [#-doWhenBooted](#-dowhenbooted).
### `doWhenBooted`
Evaluate "onComplete" as soon as the server has booted. This method assumes the server is being booted explicitly through a separate `boot` call. If the server is already running, "onComplete" is executed immediately.**Arguments:**

| Argument | Description |
|----------|-------------|
| `onComplete` | A function to evaluate after the server has booted successfully. |  
| `limit` | The number of times to check for a successful boot. |  
| `onFailure` | A function to evaluate after the server fails to boot. If onFailure is not given, an error message is posted. Providing a function suppresses the error message. If you want to supply a function and print the normal error message, make sure that your function returns "false," e.g. `s.doWhenBooted(onFailure: { ... custom action...; false })`. |  
| `clock` | The default [Clock](../Classes/Clock.md) is [AppClock](../Classes/AppClock.md). Use [SystemClock](../Classes/SystemClock.md) or [TempoClock](../Classes/TempoClock.md) if time accuracy is important. |  
To play with precise time control, the fourth argument clock should be set to a precise clock (see above), and then [GUI classes](../Overviews/GUI-Classes.md) should be wrapped in a `defer { ... }`.
```
(
t = TempoClock;
t.tempo = 1;

s.waitForBoot({
    var win, routine;
    defer {
        win = Window();
        win.background_(Color.grey(0, 0)).onClose_{ routine.stop }.front;
    };
    routine = fork {
        9.do { |i|
            1.wait;
            { win.background_(Color.rand) }.defer;
            i = if (i % 4 == 0) { 93 } { 81 };
            x = {
                SinOsc.ar(i.midicps) * Env.perc.ar(Done.freeSelf) * [0.1, -0.1]
            }.play
        };
        defer { win.close }
    }
}, clock: t)
)

t.tempo = 30/60
```


### `boot`
boot the remote server, create new allocators.**Arguments:**

| Argument | Description |
|----------|-------------|
| `startAliveThread` | If true, start a Routine to send a /status message to the server every so often. The interval between the messages is set by `theServer.aliveThreadPeriod = (seconds)`. The default period is 0.7. If false, /status will not be sent and the server's window will not update. |  
| `recover` | If true, create a new node ID allocator for the server, but use the old buffer and bus allocators. This is useful if the server process did not actually stop. In normal use, the default value "false" should be used. |  
| `onFailure` | In this method, the onFailure argument is for internal use only. If you wish to take specific actions when the server boots or fails to boot, it is recommended to use [#-waitForBoot](#-waitforboot) or [#-doWhenBooted](#-dowhenbooted). |  
You cannot boot a server app on a remote machine, but you can initialize the allocators by calling this message.
### `quit`
quit the server application
> **Note:** If the server is unresponsive at the time of calling this method, it will be forced to quit immediately.

**Arguments:**

| Argument | Description |
|----------|-------------|
| `onComplete` | A function that is called when quit has completed. |  
| `onFailure` | A function that is called when quit has failed. |  
| `watchShutDown` | a boolean to tell the server whether to watch status during shutdown. |  

### `reboot`
quit and restart the server application**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | a function that is called between quit and (re-)boot. |  
| `onFailure` | A function that is called when quit has failed. |  

### `freeAll`
free all nodes in this server
### `status`
query the server status
### `notify`
The server sends notifications, for example, if a node was created, a 'tr' message from a [SendTrig](../Classes/SendTrig.md), or a **/done** action. If `flag` is set to false, these messages will not be sent to this client. The default is true. If true the server will respond with a clientID (scsynth only) which can be useful in multi-client situations. If this is different from any previously received ID new allocators will be created. See [#Local vs. Remote Servers, Multi-client Configurations](#local-vs.-remote-servers,-multi-client-configurations) for more information.
### `ping`
measure the time between server and client, which may vary. the `func` is evaluated after `n` number of times and is passed the resulting maximum.
### `options`
Get or set this Server's [ServerOptions](../Classes/ServerOptions.md) object. Changes to options only take effect when the server is rebooted.
### `defaultGroup`
Return the default group on this Server for this client ID. This will be the same object as `server.defaultGroups[server.clientID]`.
### `defaultGroups`
Return an array mapping client IDs to their associated default groups as [Group](../Classes/Group.md) objects.
### `volume`
Get an instance of Volume that runs after the default group, or sets the Volume of the Server's output to level. Level is in db.
### `mute`
mute the server's output. This can also be toggled from the Server window with the 'm' key.
### `unmute`
unmute the server. This can also be toggled from the Server window with the 'm' key.
### `reorder`
Move the nodes in `nodeList` to the location specified by `target` and `addAction`, placing them there in the order indicated by nodeList.Any nodes which have already been freed will be skipped. Passing nil for target and addAction will result in the location being the head of the default group.
```
g = Group.new;
x = Array.fill(5, { Synth(\default) });
s.queryAllNodes;
s.reorder(x, g, \addToTail);
s.queryAllNodes;
```


### `inputBus`
Return a [Bus](../Classes/Bus.md) object that represents the input audio bus.
### `outputBus`
Return a [Bus](../Classes/Bus.md) object that represents the output audio bus.
### Information and debugging

### `dumpOSC`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `code` | | 0 | turn dumping OFF. | 
| --- | --- || 1 | print the parsed contents of the message. | | 2 | print the contents in hexadecimal. | | 3 | print both the parsed and hexadecimal representations of the contents. | 
> **Note:** `/status` messages won't be posted, when dumping is enabled |  


### `queryAllNodes`
Post a representation of this Server's current node tree to the post window. See [#-plotTree](#-plottree) for a graphical variant.Very helpful for debugging. For local servers, this uses g_dumpTree and for remote g_queryTree. See [Group](../Classes/Group.md) and [Server-Command-Reference](../Reference/Server-Command-Reference.md) for more info.
```
s.boot;
s.queryAllNodes; // note the root node (ID 0) and the default group (ID 1)
s.quit;
```



### `rtMemoryStatus`
Queries the server for the amount of currently free real-time memory**Arguments:**

| Argument | Description |
|----------|-------------|
| `action` | a Function that will be evaluated when the server responds, with the current amount of free RT memory and the size of largest continuous block (both in bytes) passed as arguments. The default action prints a message. |  


### `peakCPU`, `avgCPU`
Get peak and average CPU usage.

### `latency`
The current latency of the server. See [ServerTiming](../Guides/ServerTiming.md) for details.

### `sampleRate`
An integer representing the nominal sample rate of the server; in other words, the sample rate that was requested of the server when it was booted.

### `actualSampleRate`
A floating-point number representing the current hardware sample rate, which may drift.

### `numSynths`
Get number of running [Synth](../Classes/Synth.md)s.

### `numGroups`
Get the number of [Group](../Classes/Group.md)s.

### `numUGens`
Get the number of running [UGen](../Classes/UGen.md)s.

### `numSynthDefs`
Get number of loaded [SynthDef](../Classes/SynthDef.md)initions.

### `pid`
Get process ID of the running server (if not internal).

### `addr`
The network address of the server as a [NetAddr](../Classes/NetAddr.md).

### `maxNumClients`
If known, the maximum number of clients allowed on the server. Otherwise, the value of [ServerOptions#-maxLogins](../Classes/ServerOptions.md#-maxlogins), which is what will be requested after the server boots. This number is not guaranteed to be correct until [#-serverRunning](#-serverrunning) is `true`.

### `clientID`
The getter returns the client ID of this client on the remote process. `nil` until the server is running.The setter attempts to set the client ID of this client for the remote server process. Fails on invalid input or if the server is running. Valid inputs are in the range `[0..(this.maxNumClients-1)]`.

### `hasShmInterface`
Returns true if a [ServerShmInterface](../Classes/ServerShmInterface.md) is available. See also [Bus#Synchronous Control Bus Methods](../Classes/Bus.md#synchronous-control-bus-methods). The shared memory interface is initialized after first server boot.> **⚠️ Warning:** Currently, the shared memory interface treats server port as an unique identifier. In the rare case when there are multiple servers running on the same machine and listening on the same port, this leads to the shared memory interface of one of the servers being overwritten by the other.

### `serverBooting`
`true` if the server is booting, `false` otherwise.

### `hasBooted`
`true` if the server has booted. The server is not guaranteed to have a correct clientID, nor is it guaranteed that actions in [ServerTree](../Classes/ServerTree.md) will have run yet.

### `serverRunning`
`true` only if the server is fully ready. A server is fully ready once it has booted, received a reply to a `/notify` command, been given a client ID, and after the [ServerTree](../Classes/ServerTree.md) has run.

### `unresponsive`
`true` if the server is unresponsive (specifically, if it has failed to respond after [ServerOptions#-pingsBeforeConsideredDead](../Classes/ServerOptions.md#-pingsbeforeconsidereddead) ping attempts); `false` otherwise.

### `isLocal`
`true` if the server is running on the same machine as sclang, `false` otherwise.

### `remoteControlled`
`true` if the server is not being controlled by the machine on which it is running, `false` otherwise. This value is the same as `isLocal` unless explicitly set.

### `userSpecifiedClientID`
Deprecated in 3.9. Returns `false`. Server:clientID can now be set while a server is off, and is locked while the server is running. Thus, userSpecifiedClientID is no longer needed internally, and meaningless.

### Message Bundling
The server provides support for automatically bundling messages. This is quite convenient in object style and ensures synchronous execution. See also [Bundled-Messages](../Guides/Bundled-Messages.md)


### `makeBundle`
The Function `func` is evaluated, and all OSC messages generated by it are deferred and added to a bundle.**Arguments:**

| Argument | Description |
|----------|-------------|
| `time` | If set to nil or a number the bundle will be automatically sent and executed after the corresponding delay in seconds. If `time` is set to false the bundle will not be sent. |  
| `func` | The function to evaluate. |  
| `bundle` | allows you to pass in a preexisting bundle and continue adding to it. |  
**Returns:** The bundle so that it can be further used if needed.Calling `sync` inside func will split the bundle and wait for asynchronous actions to complete before continuing.If an error is encountered while evaluating `func` this method will throw an [Error](../Classes/Error.md) and stop message deferral.
```
s.boot;
(
// send a synth def to server
SynthDef("tpulse", { |out = 0, freq = 700, sawFreq = 440.0|
    Out.ar(out, SyncSaw.ar(freq, sawFreq, 0.1))
}).add;
)

// all OSC-commands generated in the function contained below will be added to a bundle
// and executed simultaneously after 2 seconds.
(
s.makeBundle(2.0, {
    x = Synth.new("tpulse");
    a = Bus.control.set(440);
    x.map(\freq, a);
});
)
x.free;

// don't send
(
b = s.makeBundle(false, {
    x = { PinkNoise.ar(0.1) * In.kr(0, 1) }.play;
});
)
// now pass b as a pre-existing bundle, and start both synths synchronously
(
s.makeBundle(nil, { // nil executes ASAP
    y = { SinOsc.kr(0.2).abs }.play(x, 0, 0, \addBefore); // sine envelope
}, b);
)
x.free; y.free;

// Throw an Error
(
try {
    s.makeBundle(nil, {
        s.farkermartin;
    });
} { |error|
    ("Look Ma, normal operations resume even though:\n" + error.errorString).postln;
    x = { FSinOsc.ar(440, 0, 0.2) }.play; // This works fine
}
)
x.free;

// use sync
(
s.makeBundle(nil, {
    b = Buffer.read(s, ExampleFiles.child);
    s.sync; // wait until load is done and then send the rest of the bundle
    x = { PlayBuf.ar(1, b) * 0.5 }.play;
});
)
x.free; b.free;
```



### `bind`
Just as in `makeBundle`, the Function `func` is evaluated, and all OSC messages generated by it are deferred and added to a bundle, which is sent to the server, using the server default latency.
```
(
s.bind {
    a = { |freq = 100| SinOsc.ar(freq, LFTri.ar(freq)) * 0.2 }.play;
    s.sync;
    a.set(\freq, 400);
}
)
```



### Shared Controls
The internal server has a number of shared control buses. Their values can be set or polled using the methods below.


### `getSharedControl`
get the current value of a shared control bus. num is the index of the bus to poll. This command is synchronous and only works with the internal server.

### `setSharedControl`
set the current value of a shared control bus to value. num is the index of the bus to set. This command is synchronous and only works with the internal server.

### `allocSharedControls`
set the number of shared control buses. Must be done before the internal server is booted. The default is 1024.

### Persistent Node Trees
The class [ServerTree](../Classes/ServerTree.md) can be used to store functions which will be evaluated after the server is booted, after all nodes are freed, and after cmd-. is pressed. This allows, for example, for one to create a persistent basic node structure. ServerTree is evaluated in the method initTree after the default group is created, so its existence can be relied upon.


### `initTree`
This method initializes the [default_group](../Reference/default_group.md) and runs [ServerTree](../Classes/ServerTree.md).This method is called automatically when you boot a Server from the language. N.B. If you started a server app from the command line you will have to call initTree manually if you need this functionality.
```
s.quit;
f = { Group.new(s.defaultGroup); "Other code can be evaluated too".postln };
ServerTree.add(f);
s.boot;
s.queryAllNodes; // note the group within the default group
ServerTree.remove(f);
```

[ServerBoot](../Classes/ServerBoot.md) and [ServerQuit](../Classes/ServerQuit.md) provide similar functionality at boot and quit times.

### GUI methods

### `makeGui`
Create and show the server window. The window responds to a number of keyboard shortcuts:| **key** | **action** | 
| --- | --- || `n` | Post a representation of this Server's current node tree to the post window. (See [#-queryAllNodes](#-queryallnodes)) | | `N` | As 'n' above but include controls. | | `l` | Show input/output level meters. (See [#-meter](#-meter)) | | `p` | Show graphical view of the node tree. (See [#-plotTree](#-plottree)) | | (space) | Boot server if not already booted. (See [#-boot](#-boot)) | | `s` | Show scope window. (See [#-scope](#-scope)) | | `f` | Show frequency analyzer window. (See [#-freqscope](#-freqscope)) | | `d` | Toggle dumping of OSC messages. | | `m` | Toggle mute. | | `0` | Reset volume to 0 db. | 

### `makeWindow`
On most platforms, this is equivalent to `makeGui`. If you are running SuperCollider on Emacs, it makes a server view composed of Emacs widgets.

### `scope`
Open a scope window showing the output of the Server. see [Stethoscope](../Classes/Stethoscope.md) for further details.**Arguments:**

| Argument | Description |
|----------|-------------|
| `numChannels` | the number of channels to be scoped out. The default is this server's options' numOutputBusChannels. |  
| `index` | the first channel to be output. The default is 0. |  
| `bufsize` | the size of the buffer for the ScopeView. The default is 4096. |  
| `zoom` | a zoom value for the scope's X-axis. Larger values show more. The default is 1. |  
| `rate` | whether to display audio or control rate buses (either \audio or \control) |  


### `freqscope`
Show frequency analyzer window.

### `meter`
Show input/output level meter by opening the singleton instance of [ServerMeter](../Classes/ServerMeter.md).
```
// Create a singleton ServerMeter, or bring the window to the front if it has already been created.
s.meter // -> a ServerMeter

// Query the current position of the ServerMeter window:
s.meter.position // -> Point(5.0, 277.0)

// Query the current bounds of the ServerMeter window:
s.meter.window.bounds // -> Rect(5.0, 277.0, 134.0, 230.0)

// Move the open ServerMeter to the specified position:
s.meter.position_(200@200) // -> a ServerMeter

// Retrieve the new position of the ServerMeter window:
s.meter.position // -> Point(200.0, 200.0)

// Retrieve the current bounds of the ServerMeter window:
s.meter.window.bounds // -> Rect(200.0, 200.0, 134.0, 230.0)
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `numIns` | the number of input channels. The default is nil and the number of input channels defined by `Server.local.options.numInputBusChannels` is used when using a local server. |  
| `numOuts` | the number of output channels. The default is nil and the number of output channels defined by `Server.local.options.numOutputBusChannels` is used when using a local server. |  
| `position` | the position of the meter window, i.e. the singleton instance of [ServerMeter](../Classes/ServerMeter.md). (See [ServerMeter#-position](../Classes/ServerMeter.md#-position).) The default is ``nil``, and the scope window will appear near the bottom-left side of the display: left: 5; bottom: 277. |  


### `plotTree`
Plot the node/group tree in a graphical format, similar to [#-queryAllNodes](#-queryallnodes). This creates a singleton window containing [NodeTreeView](../Classes/NodeTreeView.md).
> **Note:** To use multiple instances of [NodeTreeView](../Classes/NodeTreeView.md) per [Server](../Classes/Server.md) instance or workspace, refer to the [Examples in NodeTreeView Documentation](../Classes/NodeTreeView.md#examples).

This method returns an instance of [NodeTreeView](../Classes/NodeTreeView.md), which can also be accessed via [#-nodeTreeView](#-nodetreeview) method. Before version 3.14, this method returned an instance of the Server itself.
```
// start the SuperCollider server:
s.boot;

// Open a NodeTreeView window with a default refresh rate every 0.5 seconds:
s.plotTree;

// Close it:
s.nodeTreeView.close;
```


```
s.plotTree;

// Define and play a repeating pattern that generates a new synth every 0.4 seconds:
x = Pn((dur: 0.4, midinote: 69, amp: 0.1)).play;

/*
The NodeTreeView window dynamically displays active synth nodes.
Initially, it shows the first node, and upon each refresh, it retains the previous node while adding a new one.
This results in the display of one or two subsequent nodes at each interval.
*/

// stop updating plotTree:
s.nodeTreeView.stop;

// start updating plotTree:
s.nodeTreeView.start;

// stop the playback of the pattern:
x.stop;

s.nodeTreeView.close;
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `interval` | Polling interval.
```
(
s.waitForBoot {
    // Open a plotTree window with a refresh rate of 2 seconds:
    s.plotTree(2);

    // Define and play a repeating pattern that generates a new synth every 0.5 seconds:
    x = Pn((dur: 0.5, midinote: 69, amp: 0.1)).play;

    /*
    Since the plotTree window refreshes every 2 seconds,
    displaying only the most recent node,
    the first node will appear after a 2-second delay (once four notes have played),
    meaning only every fourth synth node is visible.
    */

    5.wait; // wait for 5 seconds.

    x.stop; // stop the playback of the pattern

    2.wait; // wait for 2 seconds.

    s.nodeTreeView.close; // close the plotTree window
}
)
``` |  
| `bounds` | The bounds of the `s.plotTree` window. A Rect specifying position and size of the window. The size does not include the border and title bar. Position is measured from the bottom-left corner of the screen in the same manner as `bounds` argument for [Window#*new](../Classes/Window.md#*new). The minimum size is 395 for width and 386 for height. Any values smaller than these will be automatically adjusted to the minimum values.
```
// Create plotTree window at the default position with default size:
s.plotTree;

// Move plotTree window to the defined position with defined size:
s.plotTree(2, Rect(200, 200, 100, 200));
// <- The size (width: 100; height: 200) is smaller than the minimum size, so the size will be adjusted.

s.plotTree; // brings the plotTree window to the front without changing its position or size.
``` |  


### `nodeTreeView`
An Instance of [NodeTreeView](../Classes/NodeTreeView.md) that is created by the [#-plotTree](#-plottree) method.

### `plotTreeView`
Plot the node/group tree graphically on a given view.**Arguments:**

| Argument | Description |
|----------|-------------|
| `interval` | Polling interval. |  
| `parent` | Parent view. |  
| `actionIfFail` | Function to be evaluated in case communication with the server cannot be established. |  
**Returns:** An Instance of [NodeTreeView](../Classes/NodeTreeView.md).

### Recording Support
The following methods are for convenience use. For recording with sample-accurate start and stop times you should make your own nodes. See the [DiskOut](../Classes/DiskOut.md) helpfile for more info. For non-realtime recording, see the [Non-Realtime-Synthesis](../Guides/Non-Realtime-Synthesis.md) helpfile.

This functionality is also available through the recording button on the server windows. Pressing it once calls record, and pressing it again calls stopRecording (see below). When doing so the file created will be in your recordings folder and be named for the current date and time. The default location of the recordings folder varies from platform to platform but is always stored in `thisProcess.platform.recordingsDir`. Setting this variable allows you to change the default.


> **Note:** record creates the recording synth after the Server's default group and uses In.ar. Thus if you add nodes after the recording synth their output will not be captured. To avoid this, either use Node objects (which use the default node as their target) or (when using messaging style) use a target nodeID of 1.
```
s.sendMsg("/s_new", "default", s.nextNodeID, 1, 1);
```


For more detail on this subject see [Order-of-execution](../Guides/Order-of-execution.md), [default_group](../Reference/default_group.md), and [NodeMessaging](../Guides/NodeMessaging.md).

See [SoundFile](../Classes/SoundFile.md) for information on the various sample and header formats. Not all sample and header formats are compatible. Note that the sampling rate of the output file will be the same as that of the server app. This can be set using the Server's [ServerOptions](../Classes/ServerOptions.md).

Example:


```
s.boot; // start the server

// something to record
(
SynthDef("bubbles", { |out|
    var f, sound;
    f = LFSaw.kr(0.4, 0, 24, LFSaw.kr([8, 7.23], 0, 3, 80)).midicps; // glissando function
    sound = CombN.ar(SinOsc.ar(f, 0, 0.04), 0.2, 0.2, 4); // echoing sine wave
    Out.ar(out, sound);
}).add;
)

x = Synth.new("bubbles");

s.prepareForRecord; // if you want to start recording at a precise moment in time, you have to call this first.

s.record;

s.pauseRecording; // pausable

s.record // start again

s.stopRecording; // this closes the file and deallocates the buffer recording node, etc.

x.free; // stop the synths

// look in your recordings folder and you'll find a file named for this date and time
```


The recording is done via an of [Recorder](../Classes/Recorder.md) - a server holds one instance implicitly.


### `prepareForRecord`
Allocates the necessary buffer, etc. for recording the server's output. (See `record` below.)**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` | a [String](../Classes/String.md) representing the path and name of the output file. If the directory does not exist, it will be created for you. (Note, however, that if this fails for any reason, the recording will also fail.) |  
| `numChannels` | a [String](../Classes/String.md) the number of output channels to record. |  
If you do not specify a path than a file will be created in your recordings folder (see the note above on this) called SC_thisDateAndTime. Changes to the header or sample format, or to the number of channels must be made **before** calling this.

### `record`
Starts or resumes recording the output.**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` | this is optional, and is passed to `prepareForRecord` (above). |  
| `bus` | the bus to record - defaults to 0 |  
| `numChannels` | the number of channels to record - defaults to 2 |  
| `node` | the node to record - defaults to server rootnode |  
| `duration` | duration to record - defaults to inf |  
If you have not called prepareForRecord first (see above) then it will be invoked for you (but that adds a slight delay before recording starts for real).

### `pauseRecording`
Pauses recording. Can be resumed by executing record again.

### `stopRecording`
Stops recording, closes the file, and frees the associated resources.You must call this when finished recording or the output file will be unusable. Cmd-. while recording has the same effect.

### `recChannels`
Get/set the number of channels (int) to record. By default this is set to 2 (stereo) but can be increased to record soundfiles with many more channels. Must be called **before** prepareForRecord.

### `recHeaderFormat`
Get/set the header format (string) of the output file. The default is "wav". Must be called **before** prepareForRecord.

### `recSampleFormat`
Get/set the sample format (string) of the output file. The default is "float" (32-bit). Common options include "int24" for 24-bit audio and "int16" for 16-bit audio. Must be called **before** prepareForRecord.

### `recBufSize`
Get/set the size of the [Buffer](../Classes/Buffer.md) to use with the [DiskOut](../Classes/DiskOut.md) UGen. This must be a power of two. The default is the `sampleRate.nextPowerOfTwo` or the first power of two number of samples longer than one second. Must be called **before** prepareForRecord.

### Asynchronous Commands
The server provides support for waiting on the completion of asynchronous OSC-commands such as reading or writing sound files. N.B. The following methods must be called from within a running [Routine](../Classes/Routine.md). Explicitly passing in a [Condition](../Classes/Condition.md) allows multiple elements to depend on different conditions. The examples below should make clear how all this works.


### `bootSync`
Boot the Server and wait until it has completed before resuming the thread.**Arguments:**

| Argument | Description |
|----------|-------------|
| `condition` | an optional instance of [Condition](../Classes/Condition.md) used for evaluating this. |  


### `sendMsgSync`
Send the following message to the server and wait until it has completed before resuming the thread.**Arguments:**

| Argument | Description |
|----------|-------------|
| `condition` | an optional instance of [Condition](../Classes/Condition.md) used for evaluating this. |  
| `... args` | one or more valid OSC messages. |  


### `sync`
Send a `/sync` message to the server, which will reply with the message `/synced` when all pending asynchronous commands have been completed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `condition` | an optional instance of [Condition](../Classes/Condition.md) used for evaluating this. |  
| `bundles` | one or more OSC messages which will be bundled before the sync message (thus ensuring that they will arrive before the /sync message). |  
| `latency` | allows for the message to be evaluated at a specific point in the future. |  
This may be slightly less safe than sendMsgSync under UDP on a wide area network, as packets may arrive out of order, but on a local network should be okay. Under TCP this should always be safe.
```
(
Routine.run {
    var c;

    // create a condition variable to control execution of the Routine
    c = Condition.new;

    s.bootSync(c);
    \BOOTED.postln;

    s.sendMsgSync(c, "/b_alloc", 0, 44100, 2);
    s.sendMsgSync(c, "/b_alloc", 1, 44100, 2);
    s.sendMsgSync(c, "/b_alloc", 2, 44100, 2);
    \b_alloc_DONE.postln;
};
)

(
Routine.run {
    var c;

    // create a condition variable to control execution of the Routine
    c = Condition.new;

    s.bootSync(c);
    \BOOTED.postln;

    s.sendMsg("/b_alloc", 0, 44100, 2);
    s.sendMsg("/b_alloc", 1, 44100, 2);
    s.sendMsg("/b_alloc", 2, 44100, 2);
    s.sync(c);
    \b_alloc_DONE.postln;
};
)
```



### Bela

### `belaScope`
Scope a number of channels from a Bus on this Server, to Bela's Oscilloscope (see [BelaScope](../Classes/BelaScope.md) for required setup). It is required that this Server is running on a Bela, and that it is thus capable of using BelaScope.**Arguments:**

| Argument | Description |
|----------|-------------|
| `scopeChannel` | Bela's oscilloscope channel to start scoping on. This has to be a non-negative number, and can't be changed after scoping starts. |  
| `index` | This server's bus index to scope. Defaults to 0. |  
| `numChannels` | Number of channels to send to BelaScope, starting from the index supplied. Defaults to 2, or to [ServerOptions#-numOutputBusChannels](../Classes/ServerOptions.md#-numoutputbuschannels) if index is 0. |  
**Returns:** A [Synth](../Classes/Synth.md), linking this Server's desired bus channels to BelaScope's bus.


