# RangeSlider

*A view consisting of a sliding extendable handle*

**Categories:** GUI>Views

## Description

A view that allows setting two numerical values between 0 and 1, represented by the two ends of a movable and extendable handle. It can have horizontal or vertical orientation, meaning the direction in which the handle moves and extends.
Dragging the mouse pointer on either end of the range moves the end by itself. Dragging in the middle of the range moves the whole range without changing its size.


## Class Methods


### `new`
 When a new RangeSlider is created, its [#-orientation](#-orientation) is determined by the initial size: if it is wider than high, the orientation will be horizontal, otherwise it will be vertical.

## Instance Methods


### Data
### `lo`
 The low end of the range. If you attempt to set it higher then the current [#-hi](#-hi), -hi will be set instead, and -lo will become the old -hi. When setting -lo the value will always be clipped to the range between 0 and 1.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float between 0 and 1. |  

### `hi`
 The high end of the range. If you attempt to set it lower then the current [#-lo](#-lo), -lo will be set instead, and -hi will become the old -lo. When setting -hi the value will always be clipped to the range between 0 and 1.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float between 0 and 1. |  

### `activeLo`
 Sets [#-lo](#-lo) to the argument and triggers [#-action](#-action).
### `activeHi`
 Sets [#-hi](#-hi) to the argument and triggers [#-action](#-action).
### `range`
 The difference between [#-hi](#-hi) and [#-lo](#-lo). Setting -range will set -hi to -lo + -range.
### `activeRange`
 Sets [#-range](#-range) to the argument and triggers [#-action](#-action).
### `setSpan`
 Sets [#-lo](#-lo) and [#-hi](#-hi) to each of the arguments, respectively.
### `setSpanActive`
 Calls [#-setSpan](#-setspan), forwarding the arguments, and triggers [#-action](#-action).
### `setDeviation`
 Sets [#-lo](#-lo) and [#-hi](#-hi) according to their deviation and their average instead of their absolute values.**Arguments:**

| Argument | Description |
|----------|-------------|
| `deviation` | A Float determining the absolute deviation of -lo and -hi from their average. |  
| `average` | A Float determining the average of -lo and -hi. |  

### `increment`
 Increments both [#-lo](#-lo) and [#-hi](#-hi) by [#-step](#-step) multiplied by 'factor'.**Arguments:**

| Argument | Description |
|----------|-------------|
| `factor` | A Float. |  

### `decrement`
 Decrements both [#-lo](#-lo) and [#-hi](#-hi) by [#-step](#-step) multiplied by 'factor'.**Arguments:**

| Argument | Description |
|----------|-------------|
| `factor` | A Float. |  


### Appearance
### `orientation`
 The orientation of the RangeSlider - the direction in which the handle moves and is extendable. The default value depends on the size of the view when created.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | One of the two Symbols: \horizontal or \vertical. |  

### `knobColor`
 The color of the handle.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  


### Interaction
### `step`
 The amount by which the range will change when [#-increment](#-increment) or [#-decrement](#-decrement) is called, or when related keys are pressed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `pixelStep`
 The absolute amount by which the range would change if the handle moved by one pixel.**Returns:** A Float.
### `shift_scale`
 The factor by which [#-step](#-step) is multiplied when incrementing or decrementing the range by keyboard while the Shift key is pressed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `ctrl_scale`
 The factor by which [#-step](#-step) is multiplied when incrementing or decrementing the range by keyboard while the Ctrl key is pressed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `alt_scale`
 The factor by which [#-step](#-step) is multiplied when incrementing or decrementing the range by keyboard while the Alt key is pressed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  


### Actions
### `action`
 The action object evaluated whenever the user changes the position or size of the handle.
### `defaultKeyDownAction`
 Implements the default effects of key presses as follows:| **Key** | **Effect** | 
| --- | --- || a | lo_(0), hi_(1), and triggers action | | n | lo_(0), hi_(0), and triggers action | | x | lo_(1), hi_(1), and triggers action | | c | lo_(0.5), hi_(0.5), and triggers action | | up arrow | increment | | down arrow | decrement | | right arrow | increment | | left arrow | decrement | 

### Drag and drop
### `defaultGetDrag`
**Returns:** A Point of which the x and y coordinates are set to [#-lo](#-lo) and [#-hi](#-hi), respectively.
### `defaultCanReceiveDrag`
**Returns:** True if the current drag data is a Point.
### `defaultReceiveDrag`
 Sets [#-lo](#-lo) and [#-hi](#-hi) to the two coordinates of the Point stored as the current drag data, respectively, and triggers the [#-action](#-action).

## Examples


### Basic examples

```supercollider
(
w = Window.new.front;
a = RangeSlider(w, Rect(20, 80, 120, 30))
    .lo_(0.2)
    .range_(0.4)
    .action_({ |slider|
        [\sliderLOW, slider.lo, \sliderHI, slider.hi].postln;
    });
)
```



```supercollider
(
w = Window.new.front;
a = RangeSlider(w, Rect(20, 80, 120, 30))
    .lo_(0.2)
    .hi_(0.8)
    .action_({ |slider|
        b.activeLo_(slider.lo); // this will trigger the action of b (and set it's value)
        b.hi_(slider.hi);
    });
b = RangeSlider(w, Rect(220, 80, 20, 130))
    .lo_(0.2)
    .hi_(0.8)
    .knobColor_(HiliteGradient(Color.grey, Color.white, \h))
    .action_({ |slider|
        [\sliderLOW, slider.lo, \sliderHI, slider.hi].postln;
    });
)
```




### Use of setDeviation

```supercollider
(
w = Window("setDeviation", Rect(300, 300, 300, 150));
a = RangeSlider(w, Rect(10, 10, 200, 30))
    .lo_(0)
    .hi_(1);
b = Slider(w, Rect(10, 50, 200, 30))
    .action_(
        { |me|
            a.setDeviation(c.value, b.value);
        });
c = Slider(w, Rect(10, 100, 200, 30))
    .action_(
        { |me|
            a.setDeviation(c.value, b.value);
        }
    );
c.valueAction = 0.2;
w.front;
)
```




### Sound example
Shape a bandpass filter.

In Cocoa GUI, hold down the Ctrl key to move the whole range; in other GUI kits you can simply click within the range and drag it.


```supercollider
(
s.waitForBoot({
    a = { |freq = 1800, bw = 0.2|
        var r;
        BBandPass.ar(WhiteNoise.ar(0.3), freq, bw);
    }.play;

    w = Window("2DSlider", Rect(100, Window.screenBounds.height-400, 400, 50));
    t = RangeSlider(w, Rect(10, 10, 380, 30))
            .lo_(0.4)
            .hi_(0.6)
            .action_({ |sl|
                a.set(\freq, 1800*(sl.lo+sl.lo)+10, \bw, (sl.hi-sl.lo).abs+0.01);
            });
    t.doAction;

    w.front;
    CmdPeriod.doOnce({ w.close });
})
)
```






