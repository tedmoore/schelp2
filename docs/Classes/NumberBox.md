# NumberBox

*A view displaying a modifiable numerical value.*

**Categories:** GUI>Views

## Description

A view that displays a numerical value and allows to modify it by typing the value in, and incrementing or decrementing it using the keyboard, or mouse.
Using the keyboard, the value will change on each arrow key press by the amount defined by [#-step](#-step).
Mouse scrolling is performed by pressing a mouse button inside the view and dragging the mouse vertically. The value will change according to the mouse cursor movement, in steps defined by [#-scroll_step](#-scroll_step).
By default, holding down the Shift, Ctrl, or Alt key while incrementing or decrementing the value will multiply the steps by 100, 10, or 0.1 respectively, though you can customize this by setting [#-shift_scale](#-shift_scale), [#-ctrl_scale](#-ctrl_scale), or [#-alt_scale](#-alt_scale). Scrolling can be enabled or disabled by modifying the [#-scroll](#-scroll) variable.


## Class Methods



## Instance Methods


### Data
### `value`
 Numerical value between 0 and 1.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `valueAction`
 Sets [#-value](#-value) to the argument and triggers [#-action](#-action).
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

### `string`
 Text to be displayed instead of the numerical value. Setting [#-value](#-value) after this will display the value again.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A String. |  

### `object`
 If [#-setBoth](#-setboth) is true, setting this variable also sets [#-string](#-string) to the argument interpreted [as String](../Classes/Object.md#-asstring).**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | Any object, typically one which makes sense to display as a string, such as a Float. |  

### `setBoth`
 A variable stating whether setting [#-object](#-object) will also set [#-string](#-string).**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  


### Restrictions on data
### `clipLo`
 The lowest numerical value allowed. Trying to set a lower value will clip it to this.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `clipHi`
 The highest numerical value allowed. Trying to set a higher value will clip it to this.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `minDecimals`
 The minimum amount of decimal places displayed. If the value can be completely described with less decimal places, zeros will be appended until reaching this.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Integer. |  

### `maxDecimals`
 The maximum amount of decimal places displayed. The value will always be rounded to this amount of decimals.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Integer. |  

### `decimals`
 Sets both [#-minDecimals](#-mindecimals) and [#-maxDecimals](#-maxdecimals) to the argument.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Integer. |  


### Appearance
### `align`
 The alignment of the displayed value. See [gui_alignments](../Reference/gui_alignments.md) for possible values.
### `stringColor`
 The color used to display the value before it is ever changed by user interaction.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  

### `normalColor`
 The color used to display the value after is has been typed in.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  

### `typingColor`
 The color used to display the value while it is being typed in.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  


### Interaction
### `step`
 The amount by which the value will changed when [#-increment](#-increment) or [#-decrement](#-decrement) is called, or when related keys are pressed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `scroll_step`
 The amount by which the value will changed when scrolled using the mouse.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `shift_scale`
 The factor by which [#-step](#-step) or [#-scroll_step](#-scroll_step) is multiplied when incrementing or decrementing the value using keyboard or mouse while the Shift key is pressed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `ctrl_scale`
 The factor by which [#-step](#-step) or [#-scroll_step](#-scroll_step) is multiplied when incrementing or decrementing the value using keyboard or mouse while the Ctrl key is pressed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `alt_scale`
 The factor by which [#-step](#-step) or [#-scroll_step](#-scroll_step) is multiplied when incrementing or decrementing the value using keyboard or mouse while the Alt key is pressed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  


### Actions
### `action`
 The action object evaluated whenever the user changes the value by interacting with the view.
### `defaultKeyDownAction`
 Any key representing a character that can make part of a floating point number representation will initiated the editing of the value. Pressing Return (or Enter) will finish the editing and store the value typed in as a Float. Aside from that, this method implements the default effects of key presses as follows:| **Key** | **Effect** | 
| --- | --- || up arrow | increment | | down arrow | decrement | | right arrow | increment | | left arrow | decrement | 

### Drag and drop
### `defaultGetDrag`
**Returns:** The [#-value](#-value).
### `defaultCanReceiveDrag`
**Returns:** True if the current drag data is a number.
### `defaultReceiveDrag`
 Sets [#-valueAction](#-valueaction) to the current drag data.

## Examples


### Basic Example

```supercollider
(
    w = Window("NumberBox Example", Rect(100, 500, 400, 120));
    b =     NumberBox(w, Rect(150, 10, 100, 20));
    b.value = rrand(1, 15);
    b.action = { |numb| numb.value.postln };
    w.front
)
// try these one at time
b.value = rrand(1, 15) ;     // sets the value but does not perform the action
b.valueAction_(5);      // sets the value and performs the action
b.step_(0.1);           // change the increment/decrement size for the arrow keys
b.scroll_step = 10;    // change the increment/decrement size for the mosueScrolling

b.background_(Color.grey);          // change the background color of the box
b.typingColor_(Color(0.3, 1, 0.3));   // change the typing color for the box
b.normalColor_(Color.white);        // change the normal color for the box. won't change until next value change

b.stringColor = Color.red;
b.align = \center;

b.increment; // increment or decrement by step
b.decrement;
```




### Sound Example
Change frequency of a playing synth by step using arrow keys:


```supercollider
(
s.waitForBoot({

    n = { |freq = 220|
        var out;
        out = SinOsc.ar(freq, 0, 0.2);
        8.do{ out = AllpassN.ar(out, 0.2, 0.02+0.20.rand, 8) };
        out;
    }.play;

    w = Window("Use arrow keys to change the frequency by steps", Rect(100, 500, 500, 120));
    b = NumberBox(w, Rect(200, 10, 100, 20));
    b.value = 220;
    b.action = { |numb| n.set(\freq, numb.value) };
    b.step = 55; // make the step a fraction of the freq
    b.focus;
    w.front;

    CmdPeriod.doOnce({ w.close });

});
)
```






