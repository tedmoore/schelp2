# jitlib_networking

*networked programming*

**Categories:** JITLib>Tutorials, Tutorials>JITLib

**Related:** [Overviews/JITLib](../../Overviews/JITLib.md)

*please note any problems, I'll try to add solutions here.*

## 1) using ProxySpace with more than one client, with separate bus spaces

> **Note:** if only one client is using a remote server, only step (a) and step (d) are relevant. The clientID argument can be left out then.



### before you start
remember to synchronize your system clocks. This can be done by:


**in macOS**
: SystemPreferences>Date&Time: set *"Set Date & Time automatically"* to true.

**in Linux**
: set the ntp clock



a local time server is better than the apple time server. if you cannot sync the time, you can set the server latency to `nil`. This will break the pattern's functionality though.




### a) boot the (remote) server and create a local model

```
s = Server("serverName", NetAddr(hostname, port));
s.options.maxLogins = 16; // or the maximum number of participants in the network
s.boot; // you cannot directly boot a remote server instance, but this initializes everything that is needed
```





**serverName**
: can be any name

**hostname**
: is an ip address, or if you have a name resolution, a network name

**port**
: the port on which the server is listening. default is 57110



see [Server](../../Classes/Server.md)




### b) from each client, initialize the default node and set notify to true:

```
s.boot; // this will initialize the tree and start notification

// if needed, a server window can be created:
s.makeWindow;
```





### c) now create a ProxySpace from the server:

```
p = ProxySpace.push(s);
```








