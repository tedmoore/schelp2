# JITGui

*a superclass for just in time interfaces*

**Categories:** JITLib>GUI, Live Coding

## Description

Proxies for synths, tasks and patterns as implemented in JITLib are extremely flexible. Having guis that represent their changeable states makes it easier to understand what is going on, especially when using multiple proxies together. JITGuis follow a special strategy described below.

### See also
- [EnvirGui](../Classes/EnvirGui.md),
- [TdefGui](../Classes/TdefGui.md), [TdefAllGui](../Classes/TdefAllGui.md), ([TaskProxyGui](../Classes/TaskProxyGui.md)) // TdefGui replaces obsolete TdefEditor
- [PdefGui](../Classes/PdefGui.md), [PdefAllGui](../Classes/PdefAllGui.md), ([TaskProxyAllGui](../Classes/TaskProxyAllGui.md)) // PdefGui replaces obsolete PdefEditor
- [NdefGui](../Classes/NdefGui.md), [MonitorGui](../Classes/MonitorGui.md), [NdefParamGui](../Classes/NdefParamGui.md) // replace NodeProxyEditor, ProxyMonitorGui
- [ProxyMixer](../Classes/ProxyMixer.md)
- [NdefMixer](../Classes/NdefMixer.md)





## Class Methods



### Creation
### `new`
Create a new JITGui that will be watching an object and displaying its state.
```supercollider
g = JITGui.new(nil, 0);        // make a JITGui
g.object = 123;                // its object gets shown asCompileString
g.object = (key: \otto);     // if the object understands .key, key gets shown as name
g.object = Pseq([1, 2, 3], inf);
g.close;
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `object` | the object to watch |  
| `numItems` | the number of display items to use, e.g. how many fields for text display, or how many sliders for single-number parameters. |  
| `parent` | a parent view on which to display. If nil, a new window is created; **parent** can also be an existing window or a composite view. |  
| `bounds` | a desired size and position where to display a JITGui. Can be nil, a [Point](../Classes/Point.md), or a [Rect](../Classes/Rect.md). JITGuis know their minimum size (**minSize**), and if bounds is nil, minSize is used. if bounds is a point or rect, it will be set to at least minSize. With a rect one can also supply a position where to display. If a point, shown size is the maximum of bounds and minSize. |  
| `makeSkip` | A flag whether to make a skipjack. (If the gui is on its own window, it typically uses one, if the JITGui is part of a larger gui, that gui may take care of updating.) |  
| `options` | a list of additional information, such as flags about optional buttons. (This is used in some subclasses.) |  



## Instance Methods


### Accessing Instance Variables

```supercollider
g.dump;
```


### `object`
the object to watch
### `numItems`
the number of display items to use, e.g. how many fields for text display, or how many sliders for single-number parameters.
### `parent`
a parent view on which the gui is displayed.
### `bounds`
the size and position of the JITGui
### `zone`
a [CompositeView](../Classes/CompositeView.md) inside the parent that holds the JITGui's views.
### `minSize`
a JITGuis calculates its own minimum size based on numItems and options.
### `defPos`
the default position where the JITGui is shown if it is in its own window.
### `skin`
(Appearance)the GUI skin to use. By default this is `GUI.skins.jit` .
### `font`
(Appearance)the font, also taken from JITGui.skin.
### `nameView`
(specific in the JITGui class)displays the object's key or name if available.
### `csView`
(specific in the JITGui class)displays the object's compileString.
### `prevState`
(common to all JITGuis)the last observed state which is kept around for comparison.
### `skipjack`
(common to all JITGuis)the skipjack that watches the object's state so it can be updated.
### `scroller`
(common to all JITGuis)an [EZScroller](../Classes/EZScroller.md) used for scrolling which of a list of items is shown. see e.g. [TdefGui](../Classes/TdefGui.md) for usage.
### `hasWindow`
(common to all JITGuis)a flag whether the JITGui has made its own window, and thus owns it.

### Instance Methods
### `object`
put an object in the gui - if the gui accepts it.
### `accepts`
test whether obj is a valid object to show in a JITGui. In **JITGui** itself, all objects are accepted, in the subclasses, **obj** can either be nil or a specific class, such as [Tdef](../Classes/Tdef.md), [Pdef](../Classes/Pdef.md), [Ndef](../Classes/Ndef.md)
### `name`
set the text of the [#-nameView](#-nameview) and the window (if it [#-hasWindow](#-haswindow))
### `getName`
ask the object its name, or return `'_anon_'`
### `winName`
return a suitable name for a window: "JITGui_objname"
### `moveTo`
if it has its own window, one can move it to some specific location.
### `close`
close its window.

### How JITGuis work
A JITGui watches the state of its object by calling its (the gui's) [#-getState](#-getstate) method at appropriate intervals (skipjack.dt). It compares the new state of the object with the previous state stored in [#-prevState](#-prevstate). When something has changed, only the gui elements concerned are updated.

Compare this with model-view-controller (MVC):

- MVC requires objects to make .changed calls in all the places where state may change, so its depandants will be informed; JITGui does not.
- MVC updates dependants instantly, while JITGui may take longer to update. For guis, very fast changes of settings (e.g. parameter automation) may produce some CPU load; with JITGuis, lazier display limits this worst-case load.
- Only the JITGui knows about its object, so there is no dependancy administration to take care of.



### 1 - Methods that subclasses should implement
You can write your own subclasses to JITGui very efficiently by implementing appropriate variants of the following methods in your class. For examples of these methods, see [TdefGui](../Classes/TdefGui.md), [EnvirGui](../Classes/EnvirGui.md), [NdefGui](../Classes/NdefGui.md).

### `setDefaults`
used to calculate the required onscreen size for the jitGui's zone. Should determine zone size based on [#-numItems](#-numitems) and options. also, [#-defPos](#-defpos) (where to show your jitGui by default) can be set here, and possibly modifications to the skin used.
### `accepts`
a test whether **obj** can be shown in the particular kind of JITGui. Subclasses of JITGui are made for special objects, e.g. Pdefs, so they should test whether obj is the right kind.
### `makeViews`
create all the views of the jitGui inside the zone.

### 2 - For updating the JITGui, overwrite these methods
### `getState`
ask the object for all aspects of its current state that will be displayed.
### `checkUpdate`
get the object's current state with [#-prevState](#-prevstate), compare it with prevState, update all gui elements that need to be changed, and store the new state as prevState. This method is called in the skipJack.

### 3 - More methods you may want to overwrite if required
### `calcBounds`
how to calculate the bounds for the zone in which to display
### `makeWindow`
how to make a window when no parent is given
### `makeZone`
how to initalize the zone within the parent window or view
### `getName`
a method for generating a name for the object.
### `winName`
a method for generating a name for the JITGui's window.
### `makeScroller`
Some objects may have more elements to display than the gui has slots, e.g. a [ProxySpace](../Classes/ProxySpace.md) can have more proxies than the mixer has numItems. Then, only [#-numItems](#-numitems) elements are shown, and the others can be scrolled to with [#-scroller](#-scroller) - an [EZScroller](../Classes/EZScroller.md) next to the slot elements. The makeScroller method should knows where in the zone to put the scroller.

## Examples


```supercollider
    // typically, only subclasses of JITGui are used,
    // so here are just some basic usage and layout tests

    // make its own window - defPos, minSize is used
g = JITGui(Ndef(\a));

    // make its own window, specific size
g = JITGui(Ndef(\a), bounds: 390@20);

    // provide full bounds
g = JITGui(Ndef(\a), bounds: Rect(200, 500, 390, 24));

    // extent is 0@0: minSize x, y is used
g = JITGui(Ndef(\a), bounds: Rect(200, 500, 0, 0));
g = JITGui(Ndef(\a), bounds: Rect(200, 500, 0, 50));
g = JITGui(Ndef(\a), bounds: Rect(200, 500, 500, 0));


(    // put a JITGui in an existing window:
w = Window().front;
g = JITGui(Ndef(\a), 0, w, bounds: 300@48);
)

(    // 5 lines high
w = Window().front;
g = JITGui(Ndef(\a), 5, w);
)

(    // recommended: use a FlowLayout.
w = Window().front;
w.addFlowLayout;
EZSlider(w, 300@100, \test, []);
g = JITGui(Ndef(\a), 0, w, bounds: 300@40);
)

// test changing color schemes for JITguis
// this scheme is admittedly ugly but different

GUI.skins.put(\jit, (
    fontSpecs:         ["Inconsolata", 12],
    fontColor:         Color.white,
    background:     Color(0.2, 0.85, 0.7, 0.5),
    foreground:        Color.grey(0.1),
    onColor:        Color(0.5, 0, 0.5),
    onColor2:       Color(0.0, 0.5, 0.5),
    offColor:        Color.grey(0.2, 0.5),
    hiliteColor:    Color.green(1.0, 0.5),
    gap:            0 @ 0,
    margin:         2@2,
    buttonHeight:    18,
    headHeight:     24)
);

// make some JITGuis to check
n = NdefGui(Ndef(\a));
Ndef(\a, { SinOsc.ar(\freq.kr(250)) });
Ndef(\a).clear;
n = NdefMixer(s);

TdefAllGui();
Tdef(\a).set(\amp, 0.25);
TdefGui(Tdef(\a), 5);

EnvirGui((a: 123));
```




