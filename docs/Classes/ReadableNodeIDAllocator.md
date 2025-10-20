# ReadableNodeIDAllocator

*an allocator for nodeIDs with human-readable ownership*

**Categories:** Control

**Related:** [Server](../Classes/Server.md), [MultiClient_Setups](../Guides/MultiClient_Setups.md)

## Description

In multi-client setups, it is useful to know which client created which nodeIDs on a shared server. ReadableNodeIDAllocator provides that facility by using a decimal prefix based on the clientID.

```
// default server uses a ReadableNodeIDAllocator
s.nodeAllocator;
s.nodeAllocator.userID; // its userID is
s.clientID

// which creates this defaultGroup 1
s.defaultGroup;
s.defaultGroupID;
// and temp nodes begin with 1000 ...
3.do { s.nextNodeID.postln };


// make a dummy server with different clientID
r = Server(\remote4, s.addr, s.options, clientID: 4);
// defaultGroup begins with 400000 ... prefix and ends with 1
r.defaultGroup;
r.defaultGroupID;
// and temp nodes begin with 400001000 ...
3.do { r.nextNodeID.postln };
```




## Class Methods


### `new`
make a new instance for given clientID, offset for lowest temporary id, and**Arguments:**

| Argument | Description |
|----------|-------------|
| `clientID` | the clientID for which to create an offset/prefix |  
| `lowestTempID` | the offset for the lowest temporary id |  
| `numClients` | the number of clients for which to split the number range
```
// make an allocator with id 11
a = ReadableNodeIDAllocator(11, 1000, 12);
// begins with 1100000 ... prefix
3.do { a.alloc.postln };
``` |  


## Instance Methods


### `clientID`
the clientID for which to create an offset/prefix
### `numClients`
the number of clients for which to split the number range
### `lowestTempID`
the offset from where temporary nodeID begin
### `idOffset`
the offset from where nodeID range begins
### `maxPermID`
the highest permanent nodeID
### `numIDs`
the number of IDs before the allocator will wrap
### `alloc`
allocate next temporary nodeID
### `allocPerm`
allocate next permanent nodeID
### `freePerm`
free a permanent nodeID**Arguments:**

| Argument | Description |
|----------|-------------|
| `id` |  |  

### `isPerm`
test whether num is in the allocator's range of permanent numbers**Arguments:**

| Argument | Description |
|----------|-------------|
| `num` |  |  

### `reset`
reset allocator to initial state

