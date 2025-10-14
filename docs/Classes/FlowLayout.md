# FlowLayout

*A view decorator which autowraps the view contents*

**Categories:** GUI>Layout

**Related:** [SCContainerView](../Classes/SCContainerView.md), [CompositeView](../Classes/CompositeView.md)

## Description

FlowLayout is a decorator which automatically arranges views inside a container view in a row, and starts a new row if there is not enough space left for the next view. [Window](../Classes/Window.md) and [CompositeView](../Classes/CompositeView.md) both have `addFlowLayout` methods which assign FlowLayout to their view decorators and return the decorator.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bounds` | An instance of [Rect](../Classes/Rect.md). Normally set to the `parent.bounds`. |  
| `margin` | An instance of [Point](../Classes/Point.md). The horizontal and vertical inner margins, within which the parent's subviews are placed. |  
| `gap` | An instance of [Point](../Classes/Point.md). The horizontal and vertical layout gap between the subviews. |  
Example:
```supercollider
(
w = Window.new.front;
// change the gaps and margins to see how they work
w.view.decorator = FlowLayout(w.view.bounds, 10@10, 20@5);
16.do{ Slider2D(w.view, 80@80).background_(Color.rand) };
)
```

You can also write:
```supercollider
(
w = Window.new.front;
w.addFlowLayout(10@10, 20@5); // a shortcut method, see SCContainerView
16.do{ Slider2D(w.view, 80@80).background_(Color.rand) };
)
```



## Instance Methods


### Accessing Instance Variables
### `nextLine`
Forces the decorator to start a new line:
```supercollider
(
w = Window.new;
q = w.addFlowLayout(10@10, 20@5);
Slider2D(w.view, 140@140).background_(Color.rand);
q.nextLine;
Slider2D(w.view, 140@140).background_(Color.rand);
w.front;
)
```


### `indentedRemaining`
Returns and instance of [Rect](../Classes/Rect.md). This is a very useful method which tells you how much space is left in a row, before the next row starts. The height of `indentedRemaining`, is the full height remaining in the FlowLayout.
```supercollider
(
// normally you will only use the width of indentedRemaining
w = Window.new;
w.view.decorator = d = FlowLayout.new(w.view.bounds, 10@10, 20@5);
Slider2D(w.view, 150@150).background_(Color.rand);
Slider2D(w.view, 150@150).background_(Color.rand);
Slider(w.view, d.indentedRemaining.width@150) // fits this view perfectly to the right innerBounds
    .background_(Color.rand);
w.front;
)
```

Compare this with:
```supercollider
( // here the third view is fit to both the right and bottom innerBounds
w = Window.new;
w.view.decorator = d = FlowLayout.new(w.view.bounds, 10@10, 20@5);
Slider2D(w.view, 140@140).background_(Color.rand);
Slider2D(w.view, 140@140).background_(Color.rand);
d.nextLine;
Slider2D(w.view, d.indentedRemaining).background_(Color.rand);
w.front;
)
```


### `bounds`
The outer bounds in which the decorator places the subviews in the parent view.**Arguments:**

| Argument | Description |
|----------|-------------|
| `b` | An instance of [Rect](../Classes/Rect.md). |  

### `innerBounds`
Returns the bounds inset by margin.
### `gap`
The horizontal and vertical layout gap between the subviews.**Arguments:**

| Argument | Description |
|----------|-------------|
| `arg1` | An instance of [Point](../Classes/Point.md). |  

### `margin`
The horizontal and vertical inner margins, within which the parent's subviews are placed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `arg1` | An instance of [Point](../Classes/Point.md). |  


### Subclassing and Internal Methods
The following methods are usually not used directly or are called by a primitive. Programmers can still call or override these as needed.

### `left`
Get the current left indentation or manually set it.**Arguments:**

| Argument | Description |
|----------|-------------|
| `arg1` | A number. |  

```supercollider
(
w = Window.new;
w.view.decorator = d = FlowLayout.new(w.view.bounds, 10@10, 20@5);
Slider2D(w.view, 150@150).background_(Color.rand);
d.left_(220); // manually set the new indentation
Slider2D(w.view, 150@150).background_(Color.rand);
w.front;
)
```


### `top`
Get the current top indentation or manually set it.**Arguments:**

| Argument | Description |
|----------|-------------|
| `arg1` | A number. |  

```supercollider
(
w = Window.new;
w.view.decorator = d = FlowLayout.new(w.view.bounds, 10@10, 20@5);
Slider2D(w.view, 150@150).background_(Color.rand);
d.top_(50); // manually set the new indentation
Slider2D(w.view, 150@150).background_(Color.rand);
Slider2D(w.view, 150@150).background_(Color.rand);
w.front;
)
```


### `shift`
Set the current left and top indentation (see above).
### `maxHeight`
Get/set maximium height of the subviews in the current position.**Arguments:**

| Argument | Description |
|----------|-------------|
| `arg1` | A number. |  

```supercollider
(
w = Window.new;
w.view.decorator = d = FlowLayout.new(w.view.bounds, 10@10, 20@5);
Slider2D(w.view, 100@160).background_(Color.rand);
Slider2D(w.view, 150@150).background_(Color.rand);
"first row maxHeight: " ++ d.maxHeight.postln;
Slider2D(w.view, 150@150).background_(Color.rand);
"second row maxHeight: " ++ d.maxHeight.postln;
w.front;
)
```


### `maxRight`
Get/set maximium right of the subviews in the current position.**Arguments:**

| Argument | Description |
|----------|-------------|
| `arg1` | A number. |  

```supercollider
(
w = Window.new;
w.view.decorator = d = FlowLayout.new(w.view.bounds, 10@10, 20@5);
Slider2D(w.view, 100@160).background_(Color.rand);
"first row maxRight: " ++ d.maxRight.postln;
Slider2D(w.view, 150@150).background_(Color.rand);
Slider2D(w.view, 150@150).background_(Color.rand);
"second row maxRight: " ++ d.maxRight.postln;
w.front;
)
```


### `currentBounds`
Gets a [Rect](../Classes/Rect.md) with `bounds.width` and `height = top + maxHeight`.
```supercollider
(
w = Window.new;
w.view.decorator = d = FlowLayout.new(w.view.bounds, 10@10, 10@5);
Slider2D(w.view, 100@160).background_(Color.rand);
d.currentBounds.postln;
Slider2D(w.view, 150@150).background_(Color.rand);
d.currentBounds.postln;
Slider2D(w.view, 150@150).background_(Color.rand);
d.currentBounds.postln;
w.front;
)
```


### `used`
Gets a [Rect](../Classes/Rect.md) with the space actually used.
```supercollider
(
w = Window.new;
w.view.decorator = d = FlowLayout.new(w.view.bounds, 10@10, 20@5);
Slider2D(w.view, 100@160).background_(Color.rand);
d.used.postln;
Slider2D(w.view, 150@150).background_(Color.rand);
d.used.postln;
Slider2D(w.view, 150@150).background_(Color.rand);
d.used.postln;
w.front;
)
```


### `reset`
Resets the layout mechanism to 0,0.


