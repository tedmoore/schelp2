# NetAddr

*network address*

**Related:** [OSCFunc](../Classes/OSCFunc.md)

**Categories:** Control, External Control>OSC


## Class Methods



### `new`
create new net address.
> **Note:** To send messages internally, loopback IP is used: "127.0.0.1"

**Arguments:**

| Argument | Description |
|----------|-------------|
| `hostname` | a [String](../Classes/String.md), either an IP number (e.g. "192.168.34.56") or a hostname such as "otherHost.local". |  
| `port` | a port number, like 57110. |  


### `fromIP`
create new net address using an integer IP number.

### `langPort`
Get the port sclang is currently listening on (may change after a recompile).

### `localIP`
Get the local IP address as a String.**Arguments:**

| Argument | Description |
|----------|-------------|
| `network` | An optional IP string to select a particular network. This might be necessary if your machine is connected to multiple networks. Typically, you would use the IP address of the router, but it can really be any address within the network. |  


### `localEndPoint`
Get a NetAddr with the local IP address and a user provided port number.**Arguments:**

| Argument | Description |
|----------|-------------|
| `port` | The port number. If omitted, the sclang port is used. |  
| `network` | An optional IP string to select a particular network. See also [#*localIP](#*localip). |  


### `localAddr`
Get a NetAddr which corresponds to localhost and the port sclang is listening on.

### `disconnectAll`
close all TCP connections.

### `broadcastFlag`
Get or set the broadcast flag (whether or not broadcast messages can be sent).

### `localIPs`
Get all local IP addresses (NICs) on this computer.**Arguments:**

| Argument | Description |
|----------|-------------|
| `family` | A Symbol that specifies the desired address family.| `all` | all addresses | 
| --- | --- || `ipv4` | only IPv4 addresses | | `ipv6` | only IPv6 addresses | |  
**Returns:** An [Array](../Classes/Array.md) containing all local IP addresses of the desired family.

### `matchLangIP`
Test an IP address to see if it matches any local IP address. See also [#*localIPs](#*localips).**Arguments:**

| Argument | Description |
|----------|-------------|
| `ipstring` | A [String](../Classes/String.md) to test containing an IP number in dot decimal notation (e.g. "192.168.34.56"). |  
**Returns:** A [Boolean](../Classes/Boolean.md) indicating whether a match was found.

### `connections`
**Returns:** A copy of the [IdentityDictionary](../Classes/IdentityDictionary.md) with all open TCP connections.

## Instance Methods


### `sendMsg`
Convert the argument list to an OSC message and send it to the NetAddr without a timestamp. The first argument is the OSC address, and the remaining arguments are the arguments in the OSC message. If you leave off the initial "/" in the OSC address, one will be prepended. The technical details of how sclang objects are converted to OSC messages is given in the [OSC_communication](../Guides/OSC_communication.md) helpfile.
```
n = NetAddr("localhost", 12345);
n = s.addr;

// Example sending symbols, integers, and a float
n.sendMsg('/s_new', \default, 2000, 0, s.defaultGroup.nodeID, \freq, 60.midicps);

// The initial forward slash can be omitted
n.sendMsg(\n_set, 2000, \gate, 0);

// Using the performList syntax, you can use an array to store an OSC message
~msg = [\n_set, 2000, \gate, 0];
n.sendMsg(*~msg);
```


### `sendBundle`
send a bundle with timestamp to the addr.
### `sendRaw`
send a raw message without timestamp to the addr.
### `connect`
open TCP connection.**Arguments:**

| Argument | Description |
|----------|-------------|
| `disconnectHandler` | called when the connection is closed (either by the client or by the server). |  

### `disconnect`
close TCP connection.
### `ip`
returns the ip number (as a [String](../Classes/String.md)).
```
n = NetAddr("localhost", 57110);
n.ip;
```


### `isLocal`
Test if this NetAddr ip number matches that of one of this hosts NICs, or the loopback address.**Returns:** A [Boolean](../Classes/Boolean.md).
## Examples


```
n = NetAddr("127.0.0.1", 57120); // 57120 is sclang default port
r = OSCFunc({ |msg, time| [time, msg].postln }, '/good/news', n);

n.sendMsg("/good/news", "you", "not you");
n.sendMsg("/good/news", 1, 1.3, 77);


n.sendBundle(0.2, ["/good/news", 1, 1.3, 77]);

r.free;
n.disconnect;

// note that different NetAddr objects with the same port and ip are independent.

r = OSCFunc({ "message arrived".postln }, '/x');

n = NetAddr("127.0.0.1", 57120);
n.sendMsg("/x")


u = NetAddr("127.0.0.1", 57120);
u.sendMsg("/x");

n.disconnect

u.sendMsg("/x");

r.free;
u.disconnect;
```




