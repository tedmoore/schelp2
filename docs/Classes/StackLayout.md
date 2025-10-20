# StackLayout

*A layout that stacks views on top of each other*

**Categories:** GUI>Layout

**Related:** [HLayout](../Classes/HLayout.md), [VLayout](../Classes/VLayout.md), [GridLayout](../Classes/GridLayout.md), [GUI-Layout-Management](../Guides/GUI-Layout-Management.md)

## Description

StackLayout manages several views stacked into the same space. It has two modes: it can either switch the view that is visible, hiding the others, or it can keep all of them visible, switching the one that is on top.
The second mode is useful for example for overlaying a view with a [UserView](../Classes/UserView.md), on which you can then draw additional information. If you still want to be able to interact with the view below using the mouse, you can make the one above ignore the mouse using [View#-acceptsMouse](../Classes/View.md#-acceptsmouse). See the [example](#examples) below.
Views can be added to the layout immediately at [construction](#*new), or you can [add](#-add) or [insert](#-insert) them after. To remove a view, you simply call [View#-remove](../Classes/View.md#-remove).
You can change the current view (the one visible / on top) using [#-index](#-index), while [#-count](#-count) tells you how many views are managed by the layout.
To switch between the two modes use [#-mode](#-mode).

> **Note:** Unlike other layouts, StackLayout can not contain another layout, but only subclasses of View.




## Class Methods




### `new`
 Creates a StackLayout and fills it with the items given as arguments. The first view becomes the current one, i.e. visible and on top of others.**Arguments:**

| Argument | Description |
|----------|-------------|
| `... views` | A sequence of **views**. Unlike other layouts, StackLayout can not contain another layout. |  
In the example below, the button will switch between the three text editing areas:
```
(
var stack;
w = Window().layout_(VLayout(
    Button().states_([["One"], ["Two"], ["Three"]]).action_({ |b| stack.index = b.value }),
    stack = StackLayout(
        TextView().string_("This is a chunk of text..."),
        TextView().string_("...and this is another..."),
        TextView().string_("...and another.")
    );
)).front;
)
```



## Instance Methods


### `add`
 Adds a view at the last index. This does not affect the current [#-index](#-index).**Arguments:**

| Argument | Description |
|----------|-------------|
| `view` | A View. |  

### `insert`
 Inserts a view at the specific index. This does not affect the current [#-index](#-index).**Arguments:**

| Argument | Description |
|----------|-------------|
| `view` | A View. |  
| `index` | An integer. If it is less than 0 or more than [#-count](#-count), the view will always be inserted as last. |  

### `count`
 The number of views managed by the layout.
### `index`
 Sets or gets the index of the current view. The current view is placed on top of others, and if [#-mode](#-mode) is 0, all the others are hidden.
### `mode`
 Sets or gets the current mode: in mode 0, the layout only displays the current view; in mode 1, the layout displays all the views. In both modes, the current view will be placed on top of others. See also: [#-index](#-index).**Arguments:**

| Argument | Description |
|----------|-------------|
| `value` | 0 or 1. Instead of an integer you can also use symbols \stackOne or \stackAll. |  
**Returns:** 0 or 1.
## Examples

Overlaying a TextView with a UserView to do additional drawing on top, while still allowing the interaction with the text:

```
(
var text, canvas;
text = TextView().string_("Hello world!").keyDownAction_({ canvas.refresh });
canvas = UserView().acceptsMouse_(false).drawFunc_({
    var b = canvas.bounds();
    var str = text.string;
    Pen.translate(b.center.x, b.center.y);
    Pen.fillColor = text.palette.baseText.alpha_(0.1);
    str.do { |c|
        var x = 40.0.rand + 10.0;
        var r = c.asString.bounds.center_(0@0);
        Pen.push;
        Pen.rotate(1.0.rand);
        Pen.translate(rand2(-0.3, 0.3) * b.width, rand2(-0.3, 0.3) * b.width);
        Pen.scale(x, x);
        Pen.stringCenteredIn(c.asString, r);
        Pen.pop;
    }
}).refresh;
w = Window().layout_(StackLayout(canvas, text).mode_(\stackAll)).front;
)
```




