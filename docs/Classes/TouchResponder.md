# TouchResponder

*allow functions to be registered to respond to MIDI aftertouch events*

**Related:** [MIDIFunc](../Classes/MIDIFunc.md), [MIDIdef](../Classes/MIDIdef.md), [MIDIResponder](../Classes/MIDIResponder.md), [CCResponder](../Classes/CCResponder.md)

**Categories:** External Control>MIDI

## Description


> **Note:** SC 3.5 added the [MIDIFunc](../Classes/MIDIFunc.md) and [MIDIdef](../Classes/MIDIdef.md) classes. These are faster, and aim to have a more convenient, logical and consistent interface, which shares a common design with [OSCFunc](../Classes/OSCFunc.md) and [OSCdef](../Classes/OSCdef.md). They also provide support for all MIDI message types.





## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `function` | A [Function](../Classes/Function.md) to be evaluated. Arguments passed to the function are: src, chan, value. |  
| `src` | The src number may be the system UID (obtained from `MIDIClient.sources[index].uid`) or the index of the source in the `MIDIClient.sources` array. nil matches all. |  
| `chan` | An [Integer](../Classes/Integer.md) between 0 and 15 that selects which MIDI channel to match. nil matches all. May also be a [Function](../Classes/Function.md) which will be evaluated to determine the match. eg: { |val| val < 2 } |  
| `value` | An [Integer](../Classes/Integer.md) between 0 and 127 to filter values. nil matches all. May also be a [Function](../Classes/Function.md) which will be evaluated to determine the match. eg: { |val| val < 50 } |  
| `install` | If true, install the responder automatically so it is active and ready to respond. If false, then it will be inactive. |  
| `swallowEvent` | If true, then if the midi event is matched, cease testing any further responders. Note that doing this will prevent any other responders of this type from responding, including ones added behind the scenes in classes. Note also that this functionality is sensitive to the order in which responders are added. |  


## Instance Methods


### `learn`
Wait for the next aftertouch message, reset self to match src, chan.
```
(
c = TouchResponder({ |src, chan, value|
        [src, chan, value].postln;
    });
    c.learn; // wait for the first touch message
)
TouchResponder.removeAll
```


## Examples


```
(
    c = TouchResponder({ |src, chan, val|
        [src, chan, val].postln;
        },
        nil, // any source
        nil, // any channel
        nil // any value
    )
)

c.remove
```



```
(
    c = TouchResponder({ |src, chan, val|
        [src, chan, val].postln;
        },
        nil, // any source
        nil, // any channel
        (50..90) // values within this range
    )
)

c.remove
```




