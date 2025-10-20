# ContiguousBlock

*Represents a range of integer addresses*

**Categories:** Control

**Related:** [ContiguousBlockAllocator](../Classes/ContiguousBlockAllocator.md)

## Description

A ContiguousBlock is a range of addresses (generally integers >= 0) used in a [ContiguousBlockAllocator](../Classes/ContiguousBlockAllocator.md). ContiguousBlockAllocator is used in [Server](../Classes/Server.md) to manage buffer numbers and audio/control bus indices.
`ContiguousBlock(10, 2)` spans address indices 10 and 11.
Additionally, a ContiguousBlock may be marked as in use or free. See [#-used](#-used).


## Class Methods


### `new`
Returns a new instance.**Arguments:**

| Argument | Description |
|----------|-------------|
| `start` | The starting address of the block. |  
| `size` | The number of addresses after `start` to cover. Should be at least 1. |  


## Instance Methods


### `start`
The starting address of the block.
### `size`
The number of addresses covered in the block.
### `address`
A synonym for `start`.**Returns:** The starting address of the block.
### `lastAddress`
The last address covered within this block: `ContiguousBlock(10, 2).lastAddress` returns 11.
### `nextAddress`
The starting address immediately following this block. `ContiguousBlock(10, 2).lastAddress` returns 12, because an adjoining block following this block must begin at address 12.
### `used`
Boolean. `true` indicates that the block is in use, and `false` that it is available.
### `adjoins`
Answers `true` if this block touches or overlaps with the argument, and `false` if there is a gap between the two blocks.**Arguments:**

| Argument | Description |
|----------|-------------|
| `block` | A second `ContiguousBlock`. |  
**Returns:** Boolean.
### Operations

### `join`
Given two adjoining blocks, combines them into a single block. If the blocks do not adjoin, the result is `nil`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `block` | A second `ContiguousBlock`. |  
**Returns:** A new ContiguousBlock, spanning the full range of both input blocks.

### `split`
Divides a ContiguousBlock into two new blocks.**Arguments:**

| Argument | Description |
|----------|-------------|
| `span` | The size of the first new block. The remainder of the receiver block's size will be allocated to the second block. |  
**Returns:** There are three return cases:
**Receiver's size > span**
: Returns an array of two ContiguousBlocks, partitioning the original address space.

**Receiver's size == span**
: Returns an array with the original (identical) block and nil for the second partition.

**Receiver's size < span**
: Returns nil, because the original address space cannot be partitioned to be larger than itself.



## Examples


```
c = ContiguousBlock(10, 2);
d = ContiguousBlock(6, 3);
e = ContiguousBlock(6, 4);
f = ContiguousBlock(12, 1);
g = ContiguousBlock(14, 5);
h = ContiguousBlock(11, 4);


// .adjoins

c.adjoins(d)  // false: 6-8 then 10-11
c.adjoins(e)  // true: 6-9, 10-11
c.adjoins(f)  // true: 10-11, 12
c.adjoins(g)  // false: 10-11. 14-18
c.adjoins(h)  // true: overlap (10-11, 11-14)


// .join

// join 10-11 to 6-9, new block is 6-11
c.join(e)  // ContiguousBlock(6, 6, false)

c.join(d)  // nil because they don't adjoin


// .split

// g spans 14-18
// split(2) gives 14-15 for the first partition
// and 16-18 for the second
g.split(2)  // [ContiguousBlock(14, 2, false), ContiguousBlock(16, 3, false)]

c.split(2)  // [ContiguousBlock(10, 2, false), nil]

f.split(2)  // nil because 'f' isn't large enough
```




