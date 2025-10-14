# Slider

*A view consisting of a sliding handle.*

**Categories:** GUI>Views

## Description

A view that allows setting a numerical value by means of moving a sliding handle. It can have horizontal or vertical orientation, meaning the direction in which the handle moves.


## Class Methods


### `new`
 When a new Slider is created, its [#-orientation](#-orientation) is determined by the initial size: if it is wider than high, the orientation will be horizontal, otherwise it will be vertical.

## Instance Methods


### Data
### `value`
 Numerical value between 0 and 1, represented by the handle position within the groove.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `valueAction`
 Sets [#-value](#-value) and triggers [#-action](#-action).
### `increment`
 Increments the value by [#-step](#-step) multiplied by 'factor'.**Arguments:**

| Argument | Description |
|----------|-------------|
| `factor` | Any number. |  

### `decrement`
 Decrements the value by [#-step](#-step) multiplied by 'factor'.**Arguments:**

| Argument | Description |
|----------|-------------|
| `factor` | Any number. |  


### Appearance
### `orientation`
 The orientation of the Slider - the direction in which the handle moves. The default value depends on the size of the view when created.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | One of the two Symbols: \horizontal or \vertical. |  

### `thumbSize`
 The size of the handle - its width or height, depending on [#-orientation](#-orientation).**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Integer amount of pixels. |  

### `background`
 The color of the background.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  

### `knobColor`
 The color of the handle.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  


### Interaction
### `step`
 The amount by which the value will changed when [#-increment](#-increment) or [#-decrement](#-decrement) is called, or when related keys are pressed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `pixelStep`
 The absolute amount by which the value would change if the handle moved by one pixel.**Returns:** A Float.
### `shift_scale`
 The factor by which [#-step](#-step) is multiplied when incrementing or decrementing the value by keyboard while the Shift key is pressed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `ctrl_scale`
 The factor by which [#-step](#-step) is multiplied when incrementing or decrementing the value by keyboard while the Ctrl key is pressed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `alt_scale`
 The factor by which [#-step](#-step) is multiplied when incrementing or decrementing the value by keyboard while the Alt key is pressed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  


### Actions
### `action`
 The action object evaluated whenever the user moves the handle.
### `defaultKeyDownAction`
 Implements the default effects of key presses as follows:| **Key** | **Effect** | 
| --- | --- || r | valueAction_(1.0.rand) | | n | valueAction_(0) | | x | valueAction_(1) | | c | valueAction_(0.5) | | ] | increment | | [ | decrement | | up arrow | increment | | down arrow | decrement | | right arrow | increment | | left arrow | decrement | 

### Drag and drop
### `defaultGetDrag`
**Returns:** The [#-value](#-value).
### `defaultCanReceiveDrag`
**Returns:** True if the current drag data is a number.
### `defaultReceiveDrag`
 Sets [#-valueAction](#-valueaction) to the current drag data.

## Examples


### Show the slider value in a NumberBox

```supercollider
(
w = Window.new.front;
c = NumberBox(w, Rect(20, 20, 150, 20));
a = Slider(w, Rect(20, 60, 150, 20))
    .action_({
        c.value_(a.value)
        });
a.action.value;
)

( // change the bounds to become vertical
w = Window.new.front;
c = NumberBox(w, Rect(20, 20, 150, 20));
a = Slider(w, Rect(200, 60, 20, 150))
    .action_({
        c.value_(a.value)
    });
a.action.value;
)
```




### Use a Spec to round and map the output range

```supercollider
(
w = Window.new.front;
b = ControlSpec(-50, 50, \linear, 0.01); // min, max, mapping, step
c = StaticText(w, Rect(20, 20, 150, 20)).align_(\center).background_(Color.rand);
a = Slider(w, Rect(20, 50, 150, 20))
    .focusColor_(Color.red(alpha: 0.2))
    .background_(Color.rand)
    .value_(0.5)
    .action_({
        c.string_(b.map(a.value).asString)
        // round the float so it will fit in the NumberBox
        });
a.action.value;
)
```




### Change the stepsize of the slider, selected via a PopUpMenu

```supercollider
(
w = Window.new.front;
a = ["0", "0.0625", "0.125", "0.25", "0.5", "1"];
b = Slider(w, Rect(20, 100, 100, 20))
    .action_({
        c.value_(b.value)
        }).background_(Color.rand);
d = PopUpMenu(w, Rect(20, 60, 100, 20))
    .items_(a)
    .action_({
        b.step_((a.at(d.value)).asFloat);
    });
StaticText(w, Rect(130, 60, 100, 20)).string_("change step");
c = NumberBox(w, Rect(20, 20, 100, 20));
)
```




### Use the slider view to accept key actions

```supercollider
( // select the slider, type something and watch the post window
w = Window.new;
c = Slider(w, Rect(0, 0, 100, 30));
c.keyDownAction = { |view, char, modifiers, unicode, keycode|
    [char, modifiers, unicode, keycode].postln
};
w.front;
)
```




### Adding functionality to a view by the method addAction
This is useful for adding things to existing frameworks that have action functions already.


```supercollider
(
w = Window.new("A Slider");
a = Slider.new(w, Rect(40, 10, 300, 30));
w.front
);

// now incrementally add some action to the slider
a.addAction({ |sl| sl.value.postln });
a.addAction({ |sl| w.view.background = Color.green(sl.value) });
a.addAction({ |sl| sl.background = Color.red(1 - sl.value) });

// adding and removing an action:
f = { |sl| "--------*******-------".postln };
a.addAction(f);
a.removeAction(f);

// or remove all, of course
a.action = nil;
```




### Use Slider for triggering sounds

```supercollider
(
s.waitForBoot({

    SynthDef(\pluck, { |out, freq = 55|
        Out.ar(out,
            Pluck.ar(WhiteNoise.ar(0.06),
                EnvGen.kr(Env.perc(0, 4), 1.0, doneAction: Done.freeSelf),
                freq.reciprocal,
                freq.reciprocal,
                10,
                coef: 0.1)
        );
    }).add;


    w = Window.new("Hold arrow keys to trigger sound",
        Rect(300, Window.screenBounds.height - 300, 400, 100)).front;
    a = Slider(w, Rect(50, 20, 300, 40)).value_(0.5).step_(0.05).focus
    .action_({
        // trigger a synth with varying frequencies
        Synth(\pluck, [\freq, 55 + (1100 * a.value)]);
        w.view.background_(Gradient(Color.rand, Color.rand));
    })
});
)
```




### Change background color of Window

```supercollider
(
w = Window("RGB fader", Rect(100, 500, 400, 400))
    .front;
f = { w.view.background_(Color.new(r.value, g.value, b.value, 1)) };
r = Slider(w, Rect(100, 140, 200, 20))
    .value_(0.5)
    .action_({ f.value });
g = Slider(w, Rect(100, 170, 200, 20))
    .value_(0.5)
    .action_({ f.value });
b = Slider(w, Rect(100, 200, 200, 20))
    .value_(0.5)
    .action_({ f.value });
f.value;
);
```






