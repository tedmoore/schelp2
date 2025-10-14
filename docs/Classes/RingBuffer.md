# RingBuffer

*Fixed size ringbuffer*

**Categories:** Collections>Ordered

**Related:** [LinkedList](../Classes/LinkedList.md)

## Description

A circular buffer that holds a fixed-size collection. Can be used as a queue.


## Class Methods

### `new`
Create a new buffer.**Arguments:**

| Argument | Description |
|----------|-------------|
| `size` | Initial size. The collection will be able to hold one minus this number of values. |  
| `collectionClass` | Defaults to the [Array](../Classes/Array.md) class. |  


## Instance Methods

### `array`
The collection.### `readPos`
Current read position.### `writePos`
Current write position.### `maxSize`
Maximum capacity.### `size`
Alias of [#-readable](#-readable).### `readable`
Number of readble items.### `writable`
Number of writable items.### `add`
Add value and increase [#-writePos](#-writepos). Do nothing if no items can be written.### `pop`
Return next readable item and increase [#-readPos](#-readpos). Return `nil` if no items can be read.### `overwrite`
Add value and increase [#-writePos](#-writepos) by overwriting oldest readable item.### `do`
Iterate over the currently readable items.
## Examples


```supercollider
r = RingBuffer(4);
r.add(\one);
r.add(\two);
r.add(\three);
r.readable;
r.do{ |x| x.postln };


r = RingBuffer(12, Int16Array);
r.writable.do{ |i| r.add(i + 1 * 100) };
r.array;
r.readable;  // 11
r.writable;  // 0 = full
r.pop;
r.pop;
r.pop;
r.readable;  // 8
r.writable;  // 3


(
var num = 100;
var m = MultiSliderView().elasticMode_(1).size_(num).front;
var r = RingBuffer(num + 1, DoubleArray);
Routine({
    while { m.isClosed.not } {
        if(r.writable == 0, { r.pop });
        r.add(sin(thisThread.seconds).abs);
        r.do{ |v, i|
            m.index = i;
            m.currentvalue = v;
        };
        (1/60).wait;
    }
}).play(AppClock);
)
```




