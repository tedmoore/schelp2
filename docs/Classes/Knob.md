# Knob

*A rotary controller view*

**Categories:** GUI>Views

**Related:** [Slider](../Classes/Slider.md), [Slider2D](../Classes/Slider2D.md)

## Description

Knob displays a value from 0.0 to 1.0 in rotary fashion, and allows to control it with either circular or linear mouse motion.
It also displays the deviation of the value from either 0.0 or 0.5, which you can choose using [#-centered](#-centered).
To switch between the mouse interaction modes, use [#-mode](#-mode).
The amount by which the value changes at interaction can be fine-tuned using [#-step](#-step), [#-keystep](#-keystep), [#-shift_scale](#-shift_scale), [#-ctrl_scale](#-ctrl_scale), and [#-alt_scale](#-alt_scale)


## Class Methods


### `defaultMode`
 The default [#-mode](#-mode) for newly created Knobs.

## Instance Methods


### Data
### `value`
 The displayed value.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Number in the range of 0.0 to 1.0. |  

### `valueAction`
 Sets the value and triggers [#-action](#-action).
### `increment`
 Increments the value by [#-keystep](#-keystep) multiplied by the argument.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Number. |  

### `decrement`
 Decrements the value by [#-keystep](#-keystep) multiplied by the argument.**Arguments:**

| Argument | Description |
|----------|-------------|
| `zoom` | A Number. |  


### Interaction
### `mode`
 The way value is controlled with respect to mouse movement after clicking on the view:- `\round` - value follows circular movement
- `\horiz` - value follows linear movement in horizontal direction
- `\vert` - value follows linear movement in vertical direction
 Defaults to `\round`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | One of the symbols listed above. |  

### `keystep`
 The amount by which the value is incremented/decremented when pressing a relevant key. Defaults to 0.01;**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Number. |  

### `step`
 The amount by which the value is incremented/decremented using the mouse in 'horizontal' and 'vertical' [modes](#-mode).**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Number. |  

### `shift_scale`
 The factor by which [#-step](#-step) or [#-keystep](#-keystep) is multiplied when used at mouse or keyboard interaction while the Shift key is pressed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `ctrl_scale`
 The factor by which [#-step](#-step) or [#-keystep](#-keystep) is multiplied when used at mouse or keyboard interaction while the Ctrl key is pressed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `alt_scale`
 The factor by which [#-step](#-step) or [#-keystep](#-keystep) is multiplied when used at mouse or keyboard interaction while the Alt key is pressed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  


### Appearance
### `centered`
 Whether the deviation of value will be displayed in relation to 0.0 or 0.5 (e.g. as in a panning controller);**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `color`
 The colors used by the Knob to draw the following elements:- the main Knob color
- the value indicator
- the deviation indicator
- the background of the deviation indicator
**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Array of four Colors in the order listed above. |  


### Actions
### `action`
 The action object evaluated whenever the user interacts with the Knob using the mouse or the keyboard.
### `defaultKeyDownAction`
 Implements the default effects of key presses as follows:| **Key** | **Effect** | 
| --- | --- || r | valueAction_(1.0.rand) | | n | valueAction_(0) | | x | valueAction_(1) | | c | valueAction_(0.5) | | ] | increment | | [ | decrement | | up arrow | increment | | down arrow | decrement | | right arrow | increment | | left arrow | decrement |  See also: [#-keystep](#-keystep), [#-shift_scale](#-shift_scale), [#-ctrl_scale](#-ctrl_scale), [#-alt_scale](#-alt_scale).

### Drag and drop
### `defaultGetDrag`
**Returns:** The [#-value](#-value).
### `defaultCanReceiveDrag`
**Returns:** True if the current drag data is a Number.
### `defaultReceiveDrag`
 Sets [#-valueAction](#-valueaction) to the current drag data.

## Examples


### Basic Example

```supercollider
(
var window, size = 32; // try different sizes - from 15 to 200 or more!
window = Window.new("Knob", Rect(640, 630, 270, 70)).front;
k = Knob.new(window, Rect(20, 10, size, size));
k.action_({ |v, x, y, m| postf("action func called: %\n", v.value) });
// k.color[1] = Color.gray(alpha: 0);
)

k.value
k.value = 0.25
k.valueAction = 0.125

// modes
k.mode = \vert;
k.mode = \horiz;
k.mode = \round; // default

k.visible
k.visible = false
k.visible = true
k.enabled = false
k.enabled_(true)
k.canFocus = false
k.canFocus = true
```




### Compare Mouse Modes

```supercollider
(
var view = View().layout_(
    HLayout(
        VLayout(Knob().mode_(\round), StaticText().string_("round")),
        VLayout(Knob().mode_(\vert), StaticText().string_("vert")),
        VLayout(Knob().mode_(\horiz), StaticText().string_("horiz"))
    )
);
view.front;
)
```




### Centered Mode
Center mode is useful for pan or eq gain control etc.


```supercollider
(
var window;
k = Knob.new(window, Rect(20, 10, 36, 36));
window = Window.new("Pan Knob", Rect(640, 630, 270, 70)).front;
k.action_({ |v, x, y, m| \pan.asSpec.map(v.value).postln })
//  .mode_(\horiz)
    .centered_(false)
    .value_(\pan.asSpec.unmap(0)); // 0.5
// k.color[1] = Color.gray(alpha: 0);
)
k.centered
k.centered = true
k.centered = false
```




### step
[#-step](#-step) only affects the 'horiz' and 'vert' modes:


```supercollider
(
var window, midispec;
k = Knob.new(window, Rect(20, 10, 32, 32));
midispec = [0, 127, 'linear', 1].asSpec;
window = Window.new("step Knob", Rect(640, 630, 270, 70)).front;
k.action_({ |v, x, y, m| midispec.map(v.value).postln })
       .value_(midispec.unmap(0));

k.mode = \vert;

)
k.step
k.step = 10/127 // step by 10

k.mode = \horiz;
k.mode = \round;
```




### mouseOverAction

```supercollider
(
var size = 28;
w = Window.new("Knobs", Rect(250, 500, 270, 70));
w.acceptsMouseOver = true; // must be true in parent window!
w.view.decorator = FlowLayout(w.view.bounds);
h = StaticText(w, 150 @ 10);
w.view.decorator.nextLine;
k = Array(8);
8.do({ |item, i|
    var knob;
    knob = Knob.new(w, size @ size)
        .action_({ |v, x, y, m| h.string = "val: " ++ v.value.asString })
        .mouseOverAction_({ |v, x, y| h.string = "val: " ++ v.value.asString });

    k = k.add(knob);
});
w.front
)
k[4].value
```




### Drag and Drop

```supercollider
(
var w, txt, size = 36;
w = Window.new("Knobs", Rect(400, 400, 250, 100)).front;
w.acceptsMouseOver = true;
w.view.decorator = FlowLayout(w.view.bounds).gap_(10 @ 10).margin_(10 @10);
txt = StaticText(w, 200 @ 14);
w.view.decorator.nextLine;

k = Knob(w, size @ size);
k.action = { |v, x, y|  v.value.postln; txt.string_("value: " ++ v.value) };
k.mouseOverAction = { |v| txt.string_("value: " ++ v.value) };

j = Knob(w, size @ size);
j.action = { |v, x, y|  j.value.postln; txt.string_("value: " ++ v.value) };
j.mouseOverAction = { txt.string_("value: " ++ j.value) };

n = NumberBox(w, 100 @ 20);
// n.setProperty(\boxColor, Color.grey(alpha: 0.0));
n.value = 0.0;
)

// customize drag and drop methods
k.canReceiveDragHandler
k.canReceiveDragHandler = false; // don't accept drops

k.canReceiveDragHandler = { View.currentDrag.isFloat }; // accept only if drag is float

k.receiveDragHandler = { ("value dropped in: " ++ View.currentDrag).postln }

k.receiveDragHandler = { k.valueAction = View.currentDrag.clip(0.0, 1.0) }

k.beginDragAction = { ("drag out -> " ++ k.value).postln }

k.beginDragAction = { k.value.asFloat }
```






