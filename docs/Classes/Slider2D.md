# Slider2D

*A view with a handle movable in two dimensions.*

**Categories:** GUI>Views

## Description

A view that allows setting two numerical values represented by the horizontal and vertical position of a handle movable in two dimensions.
The values are always within the range between 0 and 1. Scaling the output and input values to your needs can easily be achieved by using a [ControlSpec](../Classes/ControlSpec.md) with its [-map](../Classes/ControlSpec.md#-map) and [-unmap](../Classes/ControlSpec.md#-unmap) methods.
The [step](#step) variable determines the amount by which the values will change when the handle is controlled using the keyboard. By default, holding down the Shift, Ctrl, or Alt key will multiply this amount by 100, 10, or 0.1 respectively, though you can customize this by setting [#-shift_scale](#-shift_scale), [#-ctrl_scale](#-ctrl_scale), or [#-alt_scale](#-alt_scale).
Drag and drop gives and accepts a [Point](../Classes/Point.md) of which the two coordinates represent the two values of the Slider2D.


## Class Methods



## Instance Methods


### Data
### `x`
 The value represented by the horizontal position of the handle. It will always be clipped to the range between 0 and 1.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `y`
 The value represented by the vertical position of the handle. It will always be clipped to the range between 0 and 1.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `activex`
 Sets [x](#x) and triggers the [action](#action).
### `activey`
 Sets [y](#y) and triggers the [action](#action).
### `setXY`
 Sets [x](#x) and [y](#y) to the two arguments.
### `setXYActive`
 Sets [x](#x) and [y](#y) to the two arguments, and triggers the [action](#action).
### `incrementX`
 Increments [x](#x) by [step](#step) multiplied by `factor`.
### `decrementX`
 Decrements [x](#x) by [step](#step) multiplied by `factor`.
### `incrementY`
 Increments [y](#y) by [step](#step) multiplied by `factor`.
### `decrementY`
 Decrements [y](#y) by [step](#step) multiplied by `factor`.

### Appearance
### `knobColor`
 The color of the handle.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  

### `thumbSize`
 The size of the handle.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Integer amount of pixels. |  


### Interaction
### `step`
 The amount by which [x](#x) or [y](#y) will change when incremented or decremented, either by calling relevant methods, or when related keys are pressed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `pixelStepX`
 The absolute amount by which [x](#x) would change if the handle moved horizontally by one pixel.**Returns:** A Float.
### `pixelStepY`
 The absolute amount by which [y](#y) would change if the handle moved vertically by one pixel.**Returns:** A Float.
### `shift_scale`
 The factor by which [step](#step) is multiplied when incrementing or decrementing the values by keyboard while the Shift key is pressed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `ctrl_scale`
 The factor by which [step](#step) is multiplied when incrementing or decrementing the values by keyboard while the Ctrl key is pressed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `alt_scale`
 The factor by which [step](#step) is multiplied when incrementing or decrementing the values by keyboard while the Alt key is pressed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  


### Actions
### `action`
 The action object evaluated whenever the user changes the position or size of the handle.
### `defaultKeyDownAction`
 Implements the default effects of key presses as follows:| **Key** | **Effect** | 
| --- | --- || r | x_(1.rand), y_(1.rand), and triggers action | | n | x_(0), y_(0), and triggers action | | x | x_(1), y_(1), and triggers action | | c | x_(0.5), y_(0.5), and triggers action | | up arrow | incrementY | | down arrow | decrementY | | right arrow | incrementX | | left arrow | decrementX | 

### Drag and drop
### `defaultGetDrag`
**Returns:** A Point of which the x and y coordinates are set to [x](#x) and [y](#y), respectively.
### `defaultCanReceiveDrag`
**Returns:** True if the current drag data is a Point.
### `defaultReceiveDrag`
 Sets [x](#x) and [y](#y) to the two coordinates of the Point stored as the current drag data, respectively, and triggers the [action](#action).

## Examples


```supercollider
(
w = Window("Slider2D", Rect(100, 100, 140, 140));
t = Slider2D(w, Rect(20, 20, 80, 80))
        .x_(0.5) // initial location of x
        .y_(1)   // initial location of y
        .action_({ |sl|
            [\sliderX, sl.x, \sliderY, sl.y].postln;
        });
w.front;
)

t.x        // get the x loc
t.x_(0.25) // set the x loc
```


Drag an drop Points

```supercollider
(
w = Window("Slider2D", Rect(100, 100, 500, 300));
w.view.decorator = FlowLayout(w.view.bounds);
t = Slider2D(w, Rect(20, 20, 280, 280))
        .x_(0.5) // initial location of x
        .y_(1)   // initial location of y
        .background_(Color.rand)
        .action_({ |sl|
            [\sliderX, sl.x, \sliderY, sl.y].postln;
        });
t.step_(0.01);

n = CompositeView.new(w, 200@300);
n.decorator = FlowLayout(n.bounds);

v = { |i| DragBoth.new(n, Rect(0, i * 20, 200, 20)).background_(Color.rand).align_(\center) }.dup(5);

StaticText.new(n, 200@150).string_("hold down cmd and drag points from the slider to the drag slots, or reverse").stringColor_(Color.white);

w.front;
)
```


Shape a Sound

```supercollider
(
s.waitForBoot({
    a = { |mod = 0.05, index = 0.05|
            var r, out, out2;
            r = Saw.ar(8, 0.03);
            out = PMOsc.ar(
                440,
                660 * mod, 3 * index, 0,
                Lag.ar(r, 0.01, 1));
            [out, Delay1.ar(out)];
    }.play;

    w = Window("Slider2D", Rect(100, Window.screenBounds.height - 400, 300, 300));
    w.view.decorator = FlowLayout(w.view.bounds);
    t = Slider2D(w, Rect(0, 0, 292, 292))
            .y_(0.05)
            .x_(0.05)
            .background_(Color.rand)
            .knobColor_(Color.rand)
            .action_({ |sl|
                a.set(\mod, sl.x, \index, sl.y);
            });
    w.front;
    CmdPeriod.doOnce({ w.close });
})
)
```




