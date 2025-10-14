# TextField

*A view displaying editable text*

**Categories:** GUI>Views

## Description

A view displaying editable text.


## Class Methods



## Instance Methods


### Data
### `string`
 The text displayed in the view.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A String. |  

### `object`
 If [#-setBoth](#-setboth) is true, setting this variable also sets [#-string](#-string) to the value interpreted [as String](../Classes/Object.md#-asstring).**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | Any object, typically one which makes sense to display as a string, such as a Float. |  

### `setBoth`
 A variable stating whether setting [#-object](#-object) will also set [#-string](#-string).**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `value`
 Gets the same as [#-string](#-string), but when setting also sets [#-string](#-string) to the value interpreted [as String](../Classes/Object.md#-asstring) regardless of the [#-setBoth](#-setboth) flag.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | Any object, typically one which makes sense to display as a string, such as a Float. |  

### `valueAction`
 Sets [#-value](#-value) and triggers [#-action](#-action).

### Appearance
### `align`
 The alignment of the displayed text. See [gui_alignments](../Reference/gui_alignments.md) for possible values.
### `font`
 The font used to display the text.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Font. |  

### `stringColor`
 The color used to display the text.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  

### `background`
 Setting this variable colors the inside of the field under the text with the given color.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  


### Actions
### `action`
 The action object evaluated whenever the user changes the text.

### Drag and drop
### `defaultGetDrag`
**Returns:** The displayed [#-string](#-string).
### `defaultCanReceiveDrag`
**Returns:** Always true.
### `defaultReceiveDrag`
 Sets [#-valueAction](#-valueaction) to the current drag data.

## Examples


```supercollider
(
w = Window.new.front;
a = TextField(w, Rect(10, 10, 150, 20));
a.string = "hi there";
a.action = { |field| field.value.postln };
)

// does not do the action
a.value = "yo";
a.string = "oy";

a.valueAction_("this is not a pipe"); // does the action, if the value has changed
a.doAction; // evaluates the action with the content of the text field as an argument

a.background_(Color.grey);
a.stringColor_(Color.white);
a.align_(\center);
```




