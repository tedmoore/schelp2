# StackNumberAllocator

*consecutive number allocator*

**Categories:** Control

**Related:** [ContiguousBlockAllocator](../Classes/ContiguousBlockAllocator.md), [PowerOfTwoAllocator](../Classes/PowerOfTwoAllocator.md)

## Description

Number allocator within a specified range.


## Class Methods

### `new`
make a new instance, with lo and hi values.**Arguments:**

| Argument | Description |
|----------|-------------|
| `lo` | initial value |  
| `hi` | maximum |  


## Instance Methods

### `init`
Reset allocator to its initial state.### `alloc`
Allocate next number. After hi value returns nil.### `free`
Set the next value of the allocator to the arbitrary `inIndex` (could be any object). Then continue with the counter.**Arguments:**

| Argument | Description |
|----------|-------------|
| `inIndex` |  |  

## Examples


```supercollider
o = StackNumberAllocator(0, 100);
o.alloc // return the next value (evaluate multiple times)

o.init // reset counter
o.alloc // 0

o.free(2000) // returns the StackNumberAllocator itself - sets the next value to 2000
o.alloc // 2000
o.free("foo") // you can set the next value to any Object, not just integers
o.alloc // "foo"
o.alloc // allocator resumes counting where it left off before we called .free
```




