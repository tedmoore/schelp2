# MultiSliderView

*A view displaying an array of sliders*

**Categories:** GUI>Views

## Description

MultiSliderView displays a collection of values, each represented by the position of one of the sliders placed side by side.
When clicking into the view, the value of the slider under the mouse pointer will be set. Whenever the mouse is moved with a mouse button pressed, the slider currently under the mouse pointer will be adjusted.
The last slider modified is considered to be the **current** one, i.e. the [#-index](#-index) method will return its index, and [#-currentValue](#-currentvalue) relates to its value.
The current slider is also considered to be the **selected** one. Selection can be extended to more than one slider by modifying [#-selectionSize](#-selectionsize). Whenever a different slider becomes the current one, the selection size shrinks back to 1. Note that the selection will only be visually indicated if [#-showIndex](#-showindex) is `true`.


## Class Methods



### `new`
 A new MultiSliderView is created empty, without any columns. [#-size](#-size) or [#-value](#-value) has to be set in order to create some columns. So if you want a specific number of sliders, then it is best to specify the [#-size](#-size) and set [#-elasticMode](#-elasticmode) to 1. Then you will get a MultiSliderView which distributes [#-size](#-size) amount of sliders over `bounds.width`, where the slider widths are at maximum [#-indexThumbSize](#-indexthumbsize) (default 12) and the [#-gap](#-gap) is adjusted accordingly.

## Instance Methods


### Data

### `size`
 The amount of sliders. When setting -size, if the new amount is larger then the current, new sliders will be added with the value of 0. In the opposite case, the value of sliders up to the new amount will be preserved, and the rest of the sliders will be removed.
> **Note:** **In Cocoa GUI:** Changing -size after the view has been drawn or after the [#-value](#-value) array has been set will lead to unexpected results. Instead, you should change the [#-value](#-value), if you need to change the contents of the view.

**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Integer. |  


### `value`
 Sets the values of the sliders to those of the elements of the argument.
> **Note:** If the amount of elements in the argument does not match [#-size](#-size), then makes [#-size](#-size) match before applying the new values.

**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An array of Floats. |  


### `valueAction`
 Sets [#-value](#-value) and triggers [#-action](#-action).

### `reference`
 The reference values in relation to which the values will be visually represented. The default for each slider is 0.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An array of Floats. |  


### `index`
 The index of the current slider, i.e. the first one in the selection.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Integer. |  


### `selectionSize`
 The amount of sliders in the selection (starting at [#-index](#-index)).

### `currentvalue`
 The value of the slider at [#-index](#-index)**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  


### Display

### `indexIsHorizontal`
 The orientation of the view: if true, the sliders are displayed in a horizontal order, otherwise in a vertical order.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  


### `elasticMode`
 If enabled (set to 1), the sliders from [#-startIndex](#-startindex) to the last one will be distributed so as to occupy the whole area of the view. The [#-gap](#-gap) variable will be ignored. The size of each slider in the direction of index will be maximally [#-indexThumbSize](#-indexthumbsize), or smaller in order for all the sliders to fit into the view.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | 0 (disabled) or 1 (enabled). |  


### `gap`
 The gap between the sliders in pixels when [#-elasticMode](#-elasticmode) is disabled.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Integer. |  


### `indexThumbSize`
 The size of the sliders in the direction of index in pixels . If [#-elasticMode](#-elasticmode) is enabled, this will be the maximum size, but the actual size might be smaller in order for all the sliders to fit into the view.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Integer. |  


### `valueThumbSize`
 The size of the slider handles in the direction of value in pixels (if drawn).**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Integer. |  


### `thumbSize`
 Sets both [#-indexThumbSize](#-indexthumbsize) and [#-valueThumbSize](#-valuethumbsize) to the argument.

### `startIndex`
 The index of the slider displayed at the left or top edge of the view (depending on whether [#-indexIsHorizontal](#-indexishorizontal) is true or false, respectively). Sliders with lower index than this will not be visible.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Integer. |  


### Appearance

### `showIndex`
 Whether the slider selection is visually indicated.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  


### `drawRects`
 Whether to draw the sliders.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  


### `drawLines`
 Whether to draw a line connecting the points that represent the [values](#-value) of the sliders, and a line connecting the points that represent the [references](#-reference).**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  


### `isFilled`
 If true, the sliders will have their area between the [#-reference](#-reference) and the [#-value](#-value) colored, and the area bounded by the lines connecting the reference and the value points will be colored as well.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  


### `strokeColor`
 The color used to draw the lines described in [#-drawLines](#-drawlines).**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  


### `fillColor`
 The color used to visualize the areas described in [#-isFilled](#-isfilled).**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  


### `colors`
 Sets [#-strokeColor](#-strokecolor) and [#-fillColor](#-fillcolor) to the two arguments, respectively.

### Interaction

### `editable`
 Whether the values can be edited using mouse or keyboard.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  


### `readOnly`
 The opposite if [#-editable](#-editable).**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  


### `step`
 If the argument is larger than 0, makes the MultiSliderView keep the values quantized to the nearest multiple of the argument.

### Actions

### `action`
 The action object evaluated whenever the user changes the value of a slider.

### `metaAction`
 The action object evaluated whenever the user changes the value of a slider while the Ctrl key is pressed.

### `defaultKeyDownAction`
 Implements the default effects of key presses as follows:| **Key** | **Effect** | 
| --- | --- || up arrow | increment -currentValue by -step | | down arrow | decrement -currentValue by -step | | right arrow | increment -index by 1 | | left arrow | decrement -index by 1 | 

### Drag and drop

### `defaultGetDrag`
**Returns:** a) If [#-selectionSize](#-selectionsize) is 0, returns [#-value](#-value). b) If [#-selectionSize](#-selectionsize) > 1, returns an Array with the values at the indexes in the selection. If [#-reference](#-reference) is not nil, returns an Array containing (a) or (b), and an Array of the corresponding reference values: `[[values], [references]]`.

### `defaultCanReceiveDrag`
**Returns:** True for any drag data, but the data should either be an Array of values (`[values]`), or an Array containg an Array of values and an Array of corresponding reference values (`[[values], [references]]`).

### `defaultReceiveDrag`
 If the drag data is in one of the acceptable forms (see [#-defaultCanReceiveDrag](#-defaultcanreceivedrag) above), sets [#-value](#-value) (and [#-reference](#-reference)) using that data.

## Examples


### Basic Examples

```
(
n = 20;
w = Window.new.front;
m = MultiSliderView(w, Rect(10, 10, n*13+2, 100)); // default thumbWidth is 13
m.value = Array.fill(n, { |v| v*0.05 }); // size is set automatically when you set the value
m.action = { |q|
    q.value.postln;
};
)
```


Looks like a candlestick graph:


```
(
var size;
size = 350 / 6;
w = Window.new;
w.view.decorator = FlowLayout(w.view.bounds);
m = MultiSliderView(w, Rect(0, 0, 350, 100));
m.value_(Array.fill(size, { 0.01 }));
m.isFilled_(true); // width in pixels of each stick
m.indexThumbSize_(2.0); // spacing on the value axis
m.gap_(4);
w.front;
)

// rotate the above graph
(
m.bounds_(Rect(0, 0, 100, 350));
m.indexIsHorizontal_(false);
)
```




### Interactive Example
A walk through all the graphic options:


```
(
n = 40;

w = Window("MultiSlider Options", Rect(200, Window.screenBounds.height-550, 600, 450));
f = {
    w.view.decorator = FlowLayout(w.view.bounds, 10@10, 10@2);
    m = MultiSliderView(w, Rect(0, 0, 580, 200)); // default thumbWidth is 13
    m.value = Array.fill(n, { |v| 0.5+((0.3*v).sin*0.25) });
    m.action = { |q|q.value.postln };
    
    StaticText(w, 380@18).string_("indexThumbSize or thumbSize");
    Slider(w, 580@10).action_({ |sl| m.indexThumbSize = sl.value*24 }).value_(0.5);
    StaticText(w, 380@18).string_("valueThumbSize");
    Slider(w, 580@10).action_({ |sl| m.valueThumbSize = sl.value*24 }).value_(0.5);
    StaticText(w, 580@18).string_("xOffset or gap");
    Slider(w, 580@10).action_({ |sl| m.xOffset = sl.value*50 });
    StaticText(w, 580@18).string_("startIndex");
    Slider(w, 580@10).action_({ |sl| m.startIndex = sl.value *m.size });
    
    CompositeView(w, 580@10); // spacer
    Button(w, 100@20).states_([["RESET", Color.red]])
        .action_({ w.view.removeAll; f.value });
    h = StaticText(w, 450@18).string_("").stringColor_(Color.yellow);
    Button(w, 100@20).states_([["elasticMode = 0"], ["elasticMode = 1", Color.white]])
        .action_({ |b| m.elasticMode = b.value });
    Button(w, 160@20).states_([["indexIsHorizontal = false"], ["indexIsHorizontal = true", Color.white]])
        .action_({ |b| m.indexIsHorizontal = b.value.booleanValue }).value_(1);
    Button(w, 120@20).states_([["isFilled = false"], ["isFilled = true", Color.white]])
        .action_({ |b| m.isFilled = b.value.booleanValue });
    Button(w, 120@20).states_([["drawRects = false"], ["drawRects = true", Color.white]])
        .action_({ |b| m.drawRects = b.value.booleanValue }).valueAction_(1);
    Button(w, 100@20).states_([["drawLines = false"], ["drawLines = true", Color.white]])
        .action_({ |b| m.drawLines = b.value.booleanValue });
    Button(w, 160@20).states_([["readOnly = false"], ["readOnly = true", Color.white]])
        .action_({ |b| m.readOnly = b.value.booleanValue });
    Button(w, 120@20).states_([["showIndex = false"], ["showIndex = true", Color.white]])
        .action_({ |b| m.showIndex = b.value.booleanValue });
    Button(w, 120@20).states_([["reference = nil"], ["reference filled", Color.white], ["reference random", Color.yellow]])
        .action_({ |b| 
            b.value.booleanValue.if({
                (b.value > 1).if(
                    { m.reference = Array.fill(n, { 1.0.rand }) },
                    { m.reference = Array.fill(m.size, { 0.5 }) }
                );
            }, { 
                q = m.value; m.reference = []; h.string = "reference can't be returned to nil presently. please hit RESET." 
            })
        });
    Button(w, 180@20).states_([["fillColor = Color.rand"]]).action_({ m.fillColor = Color.rand });
    Button(w, 180@20).states_([["strokeColor = Color.rand"]]).action_({ m.strokeColor = Color.rand });
    Button(w, 180@20).states_([["background = Color.rand"]]).action_({ m.background = Color.rand });
};
f.value;
w.front;
)
```




### Display a Sound File

```
(
// press shift to extend the selection
// use as waveView: scrubbing over the view returns index
// if showIndex(false) the view is not refreshed (faster);
// otherwise you can make a selection with shift - drag.
var size, file, maxval, minval;
size = 640;
a = Window("test", Rect(200, 140, 650, 150));
a.view.decorator = FlowLayout(a.view.bounds);
b = MultiSliderView(a, Rect(0, 0, size, 50));
b.readOnly_(true);
a.view.decorator.nextLine;

d = Array.new;
c = FloatArray.newClear(65493);

r = Slider(a, Rect(0, 0, size, 12));
r.action = { |ex| b.gap = (ex.value * 4) + 1 };

file = SoundFile.new;
file.openRead(ExampleFiles.child);
file.numFrames.postln;
file.readData(c);
// file.inspect;
file.close;
minval = 0;
maxval = 0;
f = Array.new;
d = Array.new;
c.do({ |fi, i|
    if(fi < minval, { minval = fi });
    if(fi > maxval, { maxval = fi });

    // f.postln;
    if(i % 256 == 0, {
        d = d.add((1 + maxval) * 0.5);
        f = f.add((1 + minval) * 0.5);

        minval = 0;
        maxval = 0;
    });
});

b.reference_(d); // this is used to draw the upper part of the table
b.value_(f);

r = Slider(a, Rect(0, 0, size, 12));
r.action = { |ex| b.startIndex = ex.value *f.size };

// b.enabled_(false);
b.action = { |xb| ("index: " ++ xb.index).postln };
b.drawLines_(true);
b.drawRects_(false);
b.isFilled_(true);
b.selectionSize_(10);
b.index_(10);
b.thumbSize_(1);
b.gap_(0);
b.colors_(Color.black, Color.blue(1.0, 1.0));
b.showIndex_(true);
a.front;

)
```




### Use as a Sequencer

```
(
var size;
size = 12;
s.waitForBoot({
    n = { |freq = 330| SinOsc.ar(freq, 0, 0.2) }.play;
    
    w = Window("test", Rect(200, 450, 10 + (size * 17), 10 + (size * 17)));
    w.view.decorator = FlowLayout(w.view.bounds);
    b = MultiSliderView(w, Rect(0, 0, size * 17, size * 17));
    b.value_(Array.fill(size, { |i| i/size }));
    b.background_(Color.rand);
    b.action = { |xb|
        n.set(\freq, 330+(1100*xb.value.at(xb.index)));
        ("index: " ++ xb.index ++" value: " ++ xb.value.at(xb.index)).postln };
    b.elasticMode_(1); // makes the squares fit evenly
    b.showIndex = true; // cursor mode
    b.readOnly = true;
    w.front;
    
    r = Routine({
        0.1.wait;
        30.do({ |i|
            b.index_(i%size);
            
            b.doAction;
            0.1.wait;
        });
        
        20.do({ |i|
            b.index_(b.size.rand);
            b.doAction;
            [0.1, 0.2].choose.wait;
        });
        1.wait;
        n.free;
        { w.close }.defer;
    });
    AppClock.play(r);
});
)
```






