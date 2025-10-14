# PdefAllGui

*see all Pdefs and their state*

**Categories:** JITLib>GUI, Live Coding

**Related:** [TdefAllGui](../Classes/TdefAllGui.md), [PdefGui](../Classes/PdefGui.md)

## Description

PdefAllGui uses [PdefGui](../Classes/PdefGui.md) views to display all Pdefs, or a selection. Overview: [JITLib](../Overviews/JITLib.md)


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


```supercollider
(
Pdef(\a, { |e| 100.do { |i| i.postln; 0.5.wait } });
Pdef(\b, { |e| 100.do { |i| Pdef(\a).set(\otto, 8.rand); exprand(0.1, 3.0).wait } });
t = PdefAllGui(8);
)

    // if you have too many Pdefs, an ezscroller lets you select
"abcdefghijk".do { |ch| Pdef(ch.asSymbol) };

    // you can also filter which ones you see:
Pdef(\a_otti);
Pdef(\a_annerl);
Pdef(\a_bebe);

    // or better from gui
t.prefix_("a_");
t.filtering_(true);

    // if prefix is "", it will filter anything with "_" in it.
t.prefix_("");
t.filtering_(false);
```




