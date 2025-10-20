# RingNumberAllocator

*cyclic number allocator within a specified range*

**Categories:** Undocumented classes

**Related:** [ContiguousBlockAllocator](../Classes/ContiguousBlockAllocator.md), [PowerOfTwoAllocator](../Classes/PowerOfTwoAllocator.md), [StackNumberAllocator](../Classes/StackNumberAllocator.md)

## Description

Continuously cycles through the range of numbers, starting over from the beginning once the end of the range is reached.


## Class Methods


### `new`
make a new instance, with lo and hi values.**Arguments:**

| Argument | Description |
|----------|-------------|
| `lo` | initial value |  
| `hi` | maximum |  


## Instance Methods


### `alloc`
Allocate next number. After hi value returns lo.**Returns:** (describe returnvalue here)
### `init`
Reset allocator to its initial state.
## Examples


```
a = RingNumberAllocator.new(3, 5)
7.do {a.alloc.post } // 3453453
a.init
a.alloc // 3
```




