# PdefGui

*a line of editing controls for a Pdef, and optionally its envir*

**Categories:** JITLib>GUI, Live Coding

**Related:** [PdefAllGui](../Classes/PdefAllGui.md), [TdefGui](../Classes/TdefGui.md), [TdefAllGui](../Classes/TdefAllGui.md), [EnvirGui](../Classes/EnvirGui.md)

## Description

A gui showing the [Pdef](../Classes/Pdef.md)'s name, playing state, source state, and envir state. Optionally, its envir can also be edited.

### First example

```
g = PdefGui();            // make a PdefGui
g.object = Pdef(\a);        // show when a Pdef is put in
Pdef(\a, Pbind(\note, 12));     // show whether it has a source
Pdef(\a).play;             // show whether playing, stopped, or ended, and pausable
Pdef(\a).set(\dur, 0.25);     // show whether the Pdef has an envir
g.close;

g = PdefGui(Pdef(\a), 3);    // with an envirgui for 3 items
Pdef(\a).set(\lofreq, [1, 10], \str, "someString", \oops, \oneSymbolTooMany);
Pdef(\a).clear;
Pdef(\a).envir.clear;
g.close;

(                // put it in an existing window - margin is 0@0
w = Window("my win", Rect(200, 200, 300, 200)).front;
w.addFlowLayout;
PdefGui(Pdef(\a), 0, w);
PdefGui(Pdef(\a), 3, w);
)
```




### Details on the GUI elements

**name button**
: when selected, typing the delete key will delete its Pdef.

**play/stop button**
: indicates whether the Pdef is playing:| " >" | if stopped, | 
| --- | --- || " _" | if playing and active, | | " |" | if it is playing, but the stream has ended. |

**pause/resume button**
: only visible if one can pause or resume the Pdef, i.e. while it is playing.| "paus" | shown when you can pause it, | 
| --- | --- || "rsum" | shown when you can resume it. |

**src button**
: opens a document to edit the source (function) of the Pdef.| green | a source exists, | 
| --- | --- || white | the source is nil. |

**env button**
: opens a document to edit the environment of the Pdef, which is where one can keep all variables the Pdef uses for easy access.| green | the Pdef has an envir, | 
| --- | --- || white | the envir is nil. |






## Class Methods


### Creation Methods

### `new`
Create a new [JITGui](../Classes/JITGui.md) that will be watching an object and display its state.**Arguments:**

| Argument | Description |
|----------|-------------|
| `object` | the object to watch |  
| `numItems` | the number of display items to use, e.g. how many fields for text, or how many EZSliders for single-number parameters. |  
| `parent` | a parent view on which to display. If nil, a new window is created; **parent** can also be an existing window or a composite view. |  
| `bounds` | a desired size and position where to display a JITGui. can be nil, a [Point](../Classes/Point.md), or a [Rect](../Classes/Rect.md). JITGuis know their minimum size (**minSize**), and if bounds is nil, minSize is used. if bounds is a [Point](../Classes/Point.md) or [Rect](../Classes/Rect.md), it will be set to at least minSize. With a rect one can also supply a position where to display. If a point, shown size is the maximum of bounds and minSize. |  
| `makeSkip` | A flag whether to make a skipjack. |  
| `options` | a list of additional information, e.g. flags about optional buttons. (this is used is some subclasses) |  



## Instance Methods


### `object`
a [Pdef](../Classes/Pdef.md), or nil
### `numItems`
the number of items in the envirGui
### `parent`
the parent view
### `bounds`
the bounds of the [#-zone](#-zone)
### `zone`
the [CompositeView](../Classes/CompositeView.md) within which the PdefGui is shown
### `nameBut`, `playBut`, `pauseBut`, `srcBut`, `envBut`
the buttons
### `envirGui`
the gui for the Pdef's envir - nil if numItems is 0.
### `object`
put an object in the gui.
### `moveTo`
(if the jitGui is in its own window)move it to some specific location.
### `clear`
(if the jitGui is in its own window)set the PdefGui's object to nil
### `close`
(if the jitGui is in its own window)and close its window.
### Internal methods

### `srcString`
a compileString that recreates the Pdef.
```
// assume g from above is still there
g.srcString;
```



### `editString`
a compileString that recreates the Pdef's envir at edKey.

### `editStrings`
a compileString that recreates the Pdef's envir at edKeys.**Arguments:**

| Argument | Description |
|----------|-------------|
| `edKeys` | Default value is nil.
```
// assume g from above is still there
g.editString;
Pdef(\a).set(\foo, \bar);
g.editString(\foo);

g.editStrings;
``` |  


### `getUsedKeys`
the keys in use in the envir
```
g.getUsedKeys;
```



### `openDoc`
open a document with some strings at some location
```
g.openDoc(g.editStrings);
```



### `makeEnvirGui`
make an envirGui within zone - called internally.

## Examples


```
Pdef(\a, Pbind(\freq, Prand((1..16) * 55, inf)));
Pdef(\a).play;
t = PdefGui(Pdef(\a), 4);
Pdef(\a).set(\dur, 0.125, \amp, 0.05);

Pdef(\a).stop;
Pdef(\a).play;
Pdef(\a).pause;
Pdef(\a).resume;

t.object_(nil);
t.object_(Pdef(\a));

(
w = Window("put it in a selfmade window").front;
w.addFlowLayout;
w.view.decorator.shift(50, 50);
PdefGui(Pdef(\a), 12, w);
)

Pdef(\b, Pbind(\note, Pxrand((0..7), inf), \dur, 0.125));
Pdef(\b).play;
PdefGui(Pdef(\b));

    // see all Pdefs:
PdefAllGui(16);
```




