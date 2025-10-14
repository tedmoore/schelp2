# ContiguousBlockAllocator

*for better handling of dynamic allocation*

**Related:** [Server](../Classes/Server.md), [PowerOfTwoAllocator](../Classes/PowerOfTwoAllocator.md), [MultiClient_Setups](../Guides/MultiClient_Setups.md)

**Categories:** Control

## Description

The default allocator used in servers to allocate bus numbers and buffer numbers. Compared to its predecessor, [PowerOfTwoAllocator](../Classes/PowerOfTwoAllocator.md), it can reserve a block of numbers at the beginning of its range, and it can offset its entire range of numbers to support multiple clientIDs.


## Class Methods

### `new`
Create a new allocator with *size* slots. You may block off the first *pos* slots (the server's audioBusAllocator does this to reserve the hardware input and output buses).

## Instance Methods


### Public interface
### `alloc`
Return the starting index of a free block that is *n* slots wide. The default is 1 slot.Note that the returned address is not guaranteed to be the lowest possible address that can satisfy the requested size. It should be adjacent to a previously allocated block, however (to minimize fragmentation of the address space).
### `free`
Free a previously allocated block starting at *address*.
### `reserve`
Mark a specific range of addresses as used so that the alloc method will not return any addresses within that range. 
### `findAvailable`
Given an integer width of a desired block, find and return a `ContiguousBlock` object whose `start` is the beginning address of the block and whose `size` is the width. This method only queries the allocator; it does not change the state. If you obtain an address using `findAvailable`, there is no guarantee that a later call will not return the same address. So, in general, use [alloc](#alloc) to request an address. (`alloc` calls `findAvailable` and then `reserve`.)This method could be considered "half-private": It may be useful for queries, but in general, you can get everything you need from [alloc](#alloc), [free](#free) and [reserve](#reserve).

### Status and debugging
You may query these state variables, but it is not recommended to change them outside of the public interface.

### `debug`
 Post internal state of allocator for debugging.
### `size`
 The number of id numbers it can allocate.
### `pos`
 The allocator's offset for a reserved block (e.g. for hardware input and output buses).
### `addrOffset`
 The offset of the allocator's address range, which is used to accomodate multiple clientIDs.
### `top`
 The address of the last empty block.

## Examples


```supercollider
c = ContiguousBlockAllocator(10);
c.alloc(5);  // 0 = first available
c.alloc(2);  // 5
c.alloc(4);  // nil -- no block of 4 available

c.free(1);  // no-op: nothing at 1 to free

c.free(0);

c.alloc(3);  // 0: tries to reuse previously-freed space first

c.alloc(3);  // 7


// Adjacency
c = ContiguousBlockAllocator(24);

// reserve every 4th
(0, 4 .. 23).do { |i| c.reserve(i) };

10.do { c.findAvailable(1).postln };
```


In the last line of the second example, `findAvailable` may locate any of indices 1, 5, 9, 13, or 17. (21 would not be used until a suitable block could not be found in the other empty spaces.) If you were to allocate a single address, then the empty block of three would always be reduced to an empty block of two (instead of dividing the empty space in half and having two empty single-address blocks).
It may be surprising that the algorithm does not favor lower-index blocks, but if two addresses A and B have been previously used and freed, there is no inherent reason to prefer A if A < B.

