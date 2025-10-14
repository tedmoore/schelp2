# EnvirGui

*display the contents of an environment for editing*

**Categories:** JITLib>GUI, Live Coding

**Related:** [EZText](../Classes/EZText.md), [TdefGui](../Classes/TdefGui.md), [PdefGui](../Classes/PdefGui.md)

## Description

EnvirGui displays all keys and values of an environment, so one can change them flexibly. Single number get displayed with an [EZSlider](../Classes/EZSlider.md), pairs of numbers with an [EZRanger](../Classes/EZRanger.md), and anything else is shown as an [EZText](../Classes/EZText.md) (a text field).


## Class Methods


### Creation
### `new`
create a new EnvirGui NdefParamGui
```supercollider
// simple example
g = EnvirGui.new(nil, 5);    // empty with 5 slots
g.parent.alwaysOnTop_(true);
g.object_((a: 1, b: \werty, freq: [500, 2000]));    // put some things in
g.envir.put(\karl1, \otto1);                // one more
g.envir.put(\caesar, \julius);                // one more

g.envir.putAll((b: -12, r: 1, s: 2, t: 3, u: 4, v: 5))

g.object_((x: 2));    // put another object in

g.envir.putAll((b: -12, r: 1, s: 2, t: 3, u: 4, v: 5))

g.envir.removeAt(\b)
g.envir.removeAt(\r)
g.envir.removeAt(\s)
g.envir.removeAt(\t)
g.envir.removeAt(\u)
g.envir.removeAt(\v)
g.close;
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `object` | the envir to display |  
| `numItems` | the number of items to display. If an envir is given, and no num, num is envir.size. |  
| `parent` | the parent view to display in; if none is given, a new window is created. |  
| `bounds` | the bounds within which to display; if none is given, bounds are calculated. |  
| `makeSkip` | flag whether to make a skipjack to manage updates of the envirgui. |  
| `options` | configuration options |  



## Instance Methods


### Instance Variables
### `numItems`
how many envir items to display
### `envir`
the envir displayed - actually an alias for object.
### `zone`
the composite view the envirgui makes for itself
### `paramViews`
the paramViews that display the values:- Single numbers appear in an [EZSlider](../Classes/EZSlider.md),
- pairs of numbers will be shown in an [EZRanger](../Classes/EZRanger.md),
- all other values are shown as compileStrings in an [EZText](../Classes/EZText.md).
See [ParamView](../Classes/ParamView.md) for details.
### `specs`
a local dictionary of the specs used for display ranges of numerical parameters by the paramViews of this envirgui. See the [#-getSpec](#-getspec) method for details.
### `editKeys`
the keys of the currently displayed items in the dict.
### `keysRotation`
if the size of envir exceeds numItems, the keys displayed can be rotated: e.g. with 10 keys displayed on 5 paramViews, keysRotation 0 means show keys (0..4), keysRotation 2 means show keys (2..6), etc.**gui elements present if requested in options**
### `docBut`, `knowBut`, `parentBut`, `protoBut`


### Some Methods
### `object`
set the environment to show**Arguments:**

| Argument | Description |
|----------|-------------|
| `obj` | can be nil, a dictionary, an environment, or an event.
```supercollider
g = EnvirGui((freq: 120, \amp: 0.2, \pan: -0.5), 12, nil, bounds: Rect(20, 400, 220, 100));
g.object_((a: 1, b: [2, 3], c: \symbol, d: [4, 5, 6], f: { "boing".postln }))
``` |  

### `envir`
same as object_(obj)
### `name`
if in its own window, set the window's name
```supercollider
g.name_("Yoohoo");
```


### `getSpec`
For editing, numerical parameters need control specs for the ranges on the gui. These can be set locally in the EnvirGui, or global specs will be looked up. If no local or global specs exist for that parameter name, getSpec makes a usable guess for them. (With JITLibExtensions, one can also look up specs attached to an object such as a proxy.)
```supercollider
// inline example
g = EnvirGui.new; g.parent.alwaysOnTop_(true);
g.getSpec(\freq, 400);        // \freq exists as global spec, so use that
g.object_((freq: 150));

g.getSpec(\iFrek, 500);        // no global spec, so make a new one:
                // exponential from val * 0.05 to val * 20;
g.specs;            // and keep it here
g.envir.put(\iFrek, 500);
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `key` | the parameter name for which to find a spec |  
| `value` | the current value of that param, which is used when guessing specs. |  

### `putSpec`
add a spec for a given key, or (if it is a global key) override a global spec with a local one:
```supercollider
// set a desired range and warp:
g.putSpec(\iFrek, [10, 1000, \exp]);
g.putSpec(\freq, [10, 1000, \exp]);
g.specs;
g.putSpec(\freq, \freq);

// specs are remembered when object changes
g.putSpec(\freq, [10, 1000, \exp]);
g.object_((freq: 200, iFrek: 20));

// if needed, clear specs by hand when switching objects
g.specs.clear; g.object_((freq: 200, iFrek: 20));

g.close
```

**Keys with technical names can be replaced in the display with clearer names: method** replaceKeys the current list of keys to replace
### `addReplaceKey`
add a key to replace and its replacer key
### `removeReplaceKey`
remove a replacer key
### `showKeyFor`
show
```supercollider
e = (longFreq: 123, amp: 0.25);
g = EnvirGui(e); g.parent.alwaysOnTop_(true);

g.editKeys;
g.addReplaceKey(\longFreq, \freq1, [50, 500, \exp]);
g.viewForParam(\longFreq).visible_(false);
g.viewForParam(\freq1).visible_(true);

e.put(\z, 345);
e.put(\a, 34);

g.replaceKeys
g.removeReplaceKey(\longFreq)
```


### `highlight`
highlight the paramview at a given index, by color and optional prefix
```supercollider
g.highlight(0);
g.highlight(0, ">>_");
g.highlight(0, ">>_", Color.green(1, 0.6));
```


### `unhighlight`
remove highlighting at an index g.unhighlight(0);

### Some internal methods
### `setByKeys`
update the widgets for the current keys
### `showFields`
show (num) active fields, make others invisible.
### `useRanger`
set and get whether arrays of 2 number values should be displayed with EZRangers.**methods that make gui elements:**
### `makeViews`

### `makeOptionalViews`
the method that makes all views specified in the options
### `makeNameView`, `makeKnowBut`, `makeDocBut`, `makeClrBut`, `makeProtoBut`, `makeParentBut`
the methods that make the individual elements as specified**standard JITGui methods:**
### `accepts`, `setDefaults`, `getState`, `checkUpdate`, `updateButtons`



## Examples


```supercollider
    // Setting envir variables in a Tdef:
(
Tdef(\text).set(\note, [0, 2, 7], \dur, { [0.1, 0.2, 0.4].choose }, \pan, 0, \amp, 0.1);

w = Window("EZTexts", Rect(200, 400, 304, 120)).front;
w.addFlowLayout;

TdefGui(Tdef(\text), 0, parent: w);

e = EnvirGui(Tdef(\text).envir, 4, parent: w);

Tdef(\text, { |ev|
    var mydur;
    loop {
        mydur = ev.dur;
        (note: ev.note, dur: mydur, amp: ev.amp, pan: ev.pan).postln.play;
        mydur.wait;
    }
}).play;
)

    // or equivalently, use the built-in EnvirGui in TdefGui:
TdefGui(Tdef(\text), 8);

Tdef(\text).set(\yuhu, Prand([2, 3, 5, 8, 13], inf), \magic, [\abra, \cadabra]);

Tdef(\text).clear;
Tdef(\text).envir.clear;
```




