# Main

**Categories:** Core>Kernel

*The concrete instance of Process*

**Related:** [StartUp](../Classes/StartUp.md)

## Description

Main is the concrete instance of [Process](../Classes/Process.md) (the runtime environment for the virtual machine and interpreter). Main overrides some methods of Process. There are two methods of interest. One is named startup and is called after the class library has been compiled. The other is called shutdown which gets called when the library gets re-compiled.

### `thisProcess`
The singleton instance of Main is available through the special keyword thisProcess. For example, to find out what platform you're on:
```
thisProcess.platform;    // --> e.g. "an OSXPlatform", "a LinuxPlatform", ...
```




## Class Methods


### SuperCollider version
These class methods tell you which version of SuperCollider you are running and whether that version complies to your required minimum / maximum settings:


### `version`
**Returns:** the current version as a human readable string

### `versionAtLeast`
Returns `true` if we are running version maj.min.patch or newer, false otherwise. If `min` and/or `patch` are `nil`, they will be treated as wildcards. The tweak part of the version is completely ignored.**Arguments:**

| Argument | Description |
|----------|-------------|
| `maj` | Major version number as Integer. |  
| `min` | Minor version number as Integer, or `nil`. |  
| `patch` | Patch version number as Integer, or `nil`.
```
Main.versionAtLeast(3, 10, 4);
``` |  


### `versionAtMost`
Returns `true` if we are running version maj.min.patch or older, false otherwise. If `min` and/or `patch` are `nil`, they will be treated as wildcards. The tweak part of the version is completely ignored.**Arguments:**

| Argument | Description |
|----------|-------------|
| `maj` | Major version number as Integer. |  
| `min` | Minor version number as Integer, or `nil`. |  
| `patch` | Patch version number as Integer, or `nil`.
```
Main.versionAtMost(3, 13, 9);
``` |  


### `scVersionMajor`
**Returns:** major version number as Integer

### `scVersionMinor`
**Returns:** minor version number as Integer

### `scVersionPatch`
**Returns:** patch version number as Integer

### `scVersionTweak`
The "tweak" version is typically only used to distinguish pre-release versions of SC from proper releases. It may be empty.**Returns:** tweak version as a String

### `scVersionPostfix`
Deprecated. Use `scVersionPatch` and `scVersionTweak` instead.


## Instance Methods


### `startup`
Called after the class library has been compiled.This calls the superclass' startup, which among other things initializes the [AppClock](../Classes/AppClock.md) and the top-level [Environment](../Classes/Environment.md).Main's startup then stores Server.default in the interpreter variable s, sets the platform default's [GUI](../Classes/GUI.md) kit, calls a [Platform](../Classes/Platform.md) specific startup method (for example, OSXPlatform's startup opens the server windows), and finally invokes StartUp.run.To add your own startup functionalities, you could either edit the special startup-file (discussed in [StartupFile](../Reference/StartupFile.md)), or use StartUp.add as discussed in the [StartUp](../Classes/StartUp.md) help file.
### `shutdown`
Called after SuperCollider is quit or the class library is about to be re-compiled.This will quit all audio [Server](../Classes/Server.md) instances, perform a platform specific shutdown (e.g. the HID subsystem is released), finally Process' shutdown method is called, resulting in successive calls to UI.shutdown, NetAddr.disconnectAll, File.closeAll, and Archive.write. To register your own shutdown code, use a call like this:
```
ShutDown.add({ "Good bye!!".postln });
```


### `run`
Override this to do whatever you want, e. g. add a class extension file like this to the class library:
```
+ Main {
    run { "myPatch.rtf".load }
}
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `newFunc` | A [Function](../Classes/Function.md) or similar object to be set. When evaluated, this function will be passed the arguments time, replyAddr, and message, corresponding to the time the message was sent, the [NetAddr](../Classes/NetAddr.md) of the sender, and the message itself as an [Array](../Classes/Array.md). |  

### `addOSCRecvFunc`
Register a [Function](../Classes/Function.md) to be evaluated whenever SuperCollider language (the client) receives an OSC message. This will not overwrite any previously registered functions.**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | A [Function](../Classes/Function.md) or similar object to be added. When evaluated, this function will be passed the arguments msg, time, replyAddr, and recvPort, corresponding to the message itself as an [Array](../Classes/Array.md), the time the message was sent, the [NetAddr](../Classes/NetAddr.md) of the sender, and the port on which the message was received. Note that this order differs from that used by the deprecated method [#-recvOSCfunc](#-recvoscfunc).
```
// post all incoming traffic except the server status messages
// basically the same as OSCFunc.trace
(
f = { |msg, time, replyAddr, recvPort|
    if(msg[0] != '/status.reply') {
        "At time %s received message % from % on port%\n".postf(time, msg, replyAddr, recvPort)
    }
};
thisProcess.addOSCRecvFunc(f);
);

// stop posting.
thisProcess.removeOSCRecvFunc(f);
``` |  

### `removeOSCRecvFunc`
Remove a [Function](../Classes/Function.md) from the list of those evaluated whenever SuperCollider language (the client) receives an OSC message. This will leave any other registered functions in place.**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | A [Function](../Classes/Function.md) or similar object to be removed. |  

### `replaceOSCRecvFunc`
Replace a [Function](../Classes/Function.md) in the list of those evaluated whenever SuperCollider language (the client) receives an OSC message with a different one. This will leave any other registered functions in place.**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | The [Function](../Classes/Function.md) or similar object to be replaced. |  
| `newFunc` | A [Function](../Classes/Function.md) or similar object to be replace the one being removed. When evaluated, this function will be passed the arguments time, replyAddr, recvPort, and message, corresponding to the time the message was sent, the [NetAddr](../Classes/NetAddr.md) of the sender, the port on which the message was received, and the message itself as an [Array](../Classes/Array.md). |  

### `openUDPPort`
Attempt to open a new UDP port for receiving OSC traffic. If another application has already bound to the requested port this will fail. Once opened, ports remain bound until SC is recompiled.If the port was already opened by SC it will return true directly without trying to open the port again.**Arguments:**

| Argument | Description |
|----------|-------------|
| `portNum` | An [Integer](../Classes/Integer.md) indicating the port to attempt to bind. |  
| `type` | An [Symbol](../Classes/Symbol.md) \osc or \raw, indicating which type of messages to expect. \osc will receive callbacks at `Main:recvOSCmessage`, \raw will receive callbacks at `Main:recvRawMessage`. |  
**Returns:** A [Boolean](../Classes/Boolean.md) indicating whether the attempt was successful.
```
thisProcess.openUDPPort(3000); // will return true or false.
thisProcess.openPorts; // returns all open ports
```


### `openPorts`
Get a collection of all active UDP ports, including the main sclang port `NetAddr.langPort`.**Returns:** A [Set](../Classes/Set.md).
### `pid`
**Returns:** The operating system's pid (process ID) for the process.
### `recompile`
Recompiles the class library.
### `platform`
Get the current [Platform](../Classes/Platform.md)
### `argv`
Get the command-line arguments passed to sclang.

