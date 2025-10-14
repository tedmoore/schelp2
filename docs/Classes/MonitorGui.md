# MonitorGui

*display and control a Monitor*

**Categories:** JITLib>GUI, Live Coding

**Related:** [NodeProxy](../Classes/NodeProxy.md), [Ndef](../Classes/Ndef.md), [JITGui](../Classes/JITGui.md), [NdefGui](../Classes/NdefGui.md)

## Description

MonitorGui displays the state of a [NodeProxy](../Classes/NodeProxy.md)'s [Monitor](../Classes/Monitor.md). It is used in [NdefGui](../Classes/NdefGui.md), [ProxyMixer](../Classes/ProxyMixer.md), and [NdefMixer](../Classes/NdefMixer.md).

### First examples

```supercollider
s.boot;
Ndef(\a).ar;
Ndef(\k).kr;

    // make a MonitorGui with all bells and whistles
m = MonitorGui.new(bounds: 500@40, options: [\name, \level, \fade]);

    // when it has a kr proxy, it is visible, but disabled
m.object_(Ndef(\k));
    // with an ar proxy, it is enabled
m.object_(Ndef(\a));


    // show its play state
Ndef(\a).play
    // and volume
Ndef(\a).vol_(0.25);

    // NOTE: shift-clicking the play button opens a playN dialog!

Ndef(\a).stop;
Ndef(\a).play(0);
```





## Class Methods



### Creation
### `new`

```supercollider
g = MonitorGui(Ndef(\a));    // barebones
(
w = Window.new.front;
w.addFlowLayout;
g = MonitorGui(Ndef(\a), w, 300@40);
)

    // bounds
MonitorGui.new(Ndef(\a), bounds: Rect(100, 100, 400, 30))
MonitorGui.new(Ndef(\a), bounds: 400@24)

    // level name and numerical value
MonitorGui.new(Ndef(\a), options: [\level])

    // a nameView and a fadeTime setter box
MonitorGui.new(Ndef(\a), options: [\name, \fade])

    // all of 'em
MonitorGui.new(Ndef(\a), options: [\level, \name, \fade])
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `object` | the nodeproxy whose monitor state will be shown, or nil. |  
| `parent` | a parent view where MonitorGui is to be shown. If nil, a window is made. |  
| `bounds` | bounds where the view (or window) will be shown. |  
| `makeSkip` | a flag whether to create and start a [SkipJack](../Classes/SkipJack.md) for auto-updating. |  
| `options` | an array of symbols for options of what to display. |  



### Class Variables
### `lastOutBus`
the highest outbus number to allow. Default is 99.


## Instance Methods


### Instance Variables
### `config`
some information on what to display
### `ampSl`
an [EZSlider](../Classes/EZSlider.md) for [Monitor](../Classes/Monitor.md) volume
### `playBut`
a play button. Shift-click opens a dialog window for playN output routing by code
### `setOutBox`
a numberbox to set output routing
### `fadeBox`
a numberbox for setting monitor fadeTime.

### Some Methods
**Making various gui elements:**

### `makeViews`

### `makeVol`

### `makeNameView`

### `makePlayOut`

### `makeFade`
**Standard JITGui methods:**
### `setDefaults`
create default layout sizes
### `accepts`
accepts nil or NodeProxy
### `getState`
get the object's current state
### `checkUpdate`
compare previous state with current state, and update gui elements.


