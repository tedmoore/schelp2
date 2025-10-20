# TdefAllGui

*see all Tdefs and their state*

**Categories:** JITLib>GUI, Live Coding

**Related:** [TdefGui](../Classes/TdefGui.md), [PdefGui](../Classes/PdefGui.md), [PdefAllGui](../Classes/PdefAllGui.md)

## Description

TdefAllGui uses [TdefGui](../Classes/TdefGui.md) views to display all Tdefs, or a selection.
Overview: [JITLib](../Overviews/JITLib.md)


## Class Methods


### Creation

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `numItems` | the maximum number of Pdefs that can be shown. |  
| `parent` | a parent view on which to display. If nil, a new window is created; **parent** can also be an existing window or a composite view. |  
| `bounds` | a desired size and position where to display a JITGui. can be nil, a [Point](../Classes/Point.md), or a [Rect](../Classes/Rect.md). JITGuis know their minimum size (**minSize**), and if bounds is nil, minSize is used. if bounds is a point or rect, it will be set to at least minSize. With a rect one can also supply a position where to display. If a point, shown size is the maximum of bounds and minSize. |  
| `makeSkip` | ///// Not Done Yet, but on the listA flag whether to make a skipjack. |  
| `options` | ///// Not Done Yet, but on the listthe only option for PdefAllGui will be [\makeEdit]. adding a "front" PdefGui that also shows the front Pdef's envir. |  


## Examples


```
(
Tdef(\a, { |e| 100.do { |i| i.postln; 0.5.wait } });
Tdef(\b, { |e| 100.do { |i| Tdef(\a).set(\otto, 8.rand); exprand(0.1, 3.0).wait } });
t = TdefAllGui(8);
)

    // if you have too many Tdefs, an ezscroller lets you select
"abcdefghijk".do { |ch| Tdef(ch.asSymbol) };

    // you can also filter which ones you see:
Tdef(\a_otti);
Tdef(\a_hannerl);
Tdef(\a_dede);

    // or better from gui
t.filtering_(true);
t.prefix_("a_");

    // if prefix is "", it will filter anything with "_" in it.
t.prefix_("");
t.filtering_(false);
```




