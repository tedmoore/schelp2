# CheckBox

*A view that toggles between two states.*

**Categories:** GUI>Views

## Description

A view that toggles between two states when clicked, displaying or hiding a check mark accordingly.


## Class Methods



## Instance Methods


### Data

### `value`
 Stating which of the two states the view is currently in, false meaning unchecked and true meaning checked. Default to false.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  


### `valueAction`
 Sets [#-value](#-value) and triggers [#-action](#-action).**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  


### `string`
 The text displayed next to the check mark.

### Actions

### `action`
 The action object evaluated whenever the user toggles the state.

### Drag and drop

### `defaultGetDrag`
**Returns:** The [#-value](#-value).

### `defaultCanReceiveDrag`
**Returns:** True if the current drag data is a Boolean.

### `defaultReceiveDrag`
 Sets [#-valueAction](#-valueaction) to the current drag data.

## Examples


```
(
var w = Window().front;
var c = CheckBox(w, Rect(10, 10, 50, 50), "test");
c.action_{ |v| v.value.postln };
)
```




