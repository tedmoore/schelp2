# EnvelopeView

*A configurable view with nodes and connections*

**Categories:** GUI>Views

**Related:** [MultiSliderView](../Classes/MultiSliderView.md), [SCEnvelopeEdit](../Classes/SCEnvelopeEdit.md)

## Description

A view which can graphically display nodes at x/y coordinates, connection lines, cross-connections, node markers, and labels. All of the values for these are stored in arrays. While this view is typically used to make editable envelopes interfaces, it can be used to draw very complex interconnection graphs as well.
You can make the view display an [Env](../Classes/Env.md) using [setEnv](#setenv). Note however that the view will work on a copy of the data of the Env object, therefore moving the nodes through the view will have no effect on the Env.
You can also define nodes with arrays of x and y values using [value](#value), and the connections using [connect](#connect).

### Appearance
The view supports two **display styles**: the default one draws nodes as small dots, with labels next to them, while another style draws nodes as rounded rectangles with labels drawn inside. See [style](#style).

A **label** for each of the nodes can be set using [strings](#strings) and [setString](#setstring).



### Interaction
Nodes can be selected and moved using mouse. Shift-clicking a node will add it to the selection.

You can also move selected nodes and change selection using keyboard. Pressing the arrow keys will move selected nodes (as long as [step](#step) is larger than 0). Pressing the left or right arrow keys while holding down Alt will select previous or next node, and holding down Shift will extend selection to the left or to the right. Other GUI kits may differ.

[keepHorizontalOrder](#keephorizontalorder) allows you to enforce the order of nodes in horizontal direction to match their index order. In that case, node movement to the left and to the right will be restricted by the positions of their immediate neighbours. This is especially useful when EnvelopeView is used to display an [Env](../Classes/Env.md).

[elasticSelection](#elasticselection) determines whether moving multiple nodes will be blocked altogether if any of the nodes meet an obstacle (the view bounds or a neighbour node), or only those individual nodes will be blocked.

Node selection can also be changed programmatically using [index](#index), [selectIndex](#selectindex), and [deselectIndex](#deselectindex). The [current](#index) node can be moved programmatically using [x](#x) and [y](#y).




## Instance Methods


### Data
### `setEnv`
 Sets an [Env](../Classes/Env.md) to be displayed by the view. The view will extract data from the Env object to display (times, values and curve types). Any nodes existent prior to calling this method will be removed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Env. |  

### `value`
 `value` retrieves the node positions, returning an array in the format of the Argument below. `value_(anArray)` Sets the positions of the nodes, creating them if not existent. If there were already existent nodes and their amount is different than the amount of x/y pairs in the argument, nodes will be added or removed (in order of creation reversed) until the amounts match, and then the new values will be applied.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Array containing two other Arrays, of which one contains the horizontal and the other the vertical position of the new nodes. The values must be between 0 and 1. For example: `[[x1, x2, x3, ...], [y1, y2, y3, ...]]` |  

### `valueAction`
 Sets [value](#value) to the argument and triggers the [action](#action).
### `x`
 The horizontal position of the *current* node.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float between 0 and 1. |  

### `y`
 The vertical position of the *current* node.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float between 0 and 1. |  

### `currentvalue`
 Synonym for [y](#y).
### `curves`
 The shapes of connections between nodes. See below for the valid objects that describe a shape. If a single shape is given, it will be applied to all the existing nodes. If an Array of shapes is given, each of its elements will be applied to an existing node, in order of index. A connection curve shape applied to a node will determine the shape of the connections originating at that node. If no connections have been created using [connect](#connect), the origin node of a connection is the one with lower index. If there are such connections however, their origin is the node that was passed as the first argument to [connect](#connect).**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | The valid objects to describe a shape are listed in [Env#*new](../Classes/Env.md#*new). The argument can be either a single, or an Array of those values. |  

### `strings`
 The labels of the nodes.
> **Note:** In order for the labels to be visible, you might need to ensure that the [strokeColor](#strokecolor) contrasts the [fillColor](#fillcolor) (depending on how the view draws the nodes and the labels).

**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Array of Strings. |  

### `setString`
 Sets the label of the node at the given index.
> **Note:** In order for the label to be visible, you might need to ensure that the [strokeColor](#strokecolor) contrasts the [fillColor](#fillcolor) (depending on how the view draws the nodes and the labels).

**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | the index of the node. |  
| `string` | A String. |  

### `setFillColor`
 Sets the color used to draw the inside of the node at the given index.**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | An Integer. |  
| `color` | A Color. |  

### `setThumbWidth`
 Sets the width of the node at the given index.
> **Note:** For compatibility with existing code, this will set the [style](#style) to **'rects'**.

**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | An Integer. |  
| `width` | An Integer. |  

### `setThumbHeight`
 Sets the height of the node at the given index.
> **Note:** For compatibility with existing code, this will set the [style](#style) to **'rects'**.

**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | An Integer. |  
| `height` | An Integer. |  

### `setThumbSize`
 Sets both width and height of the node at the given index to `size`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | An Integer. |  
| `size` | An Integer. |  

### `connect`
 Removes any connections created when the [value](#value) was set, and then creates new ones from the node at index given in the first argument to each of the nodes at indexes given in the second argument.**Arguments:**

| Argument | Description |
|----------|-------------|
| `source` | An Integer - the index of the node to become one end of all the new connections. |  
| `targets` | An Array of Integers - indexes of nodes, each to become the second end to a new connection created. |  

### `selection`
 Returns an array of indexes of all selected nodes.

### Appearance
### `style`
 One of the following drawing styles:- **'dots'** - nodes are drawn as small dots within a larger circle indicating the area of mouse sensitivity. Labels are drawn next to the dots (see [setString](#setstring)). This style always draws nodes with *equal width and height*, and will use the smaller of the node's sizes, if different (it never draws ellipses).
- **'rects'** - nodes are drawn as rounded rectangles. Labels are drawn within the bounds of the rectangles.

> **Note:** For compatibility with existing code, calling any of [thumbWidth](#thumbwidth), [thumbHeight](#thumbheight), [setThumbWidth](#setthumbwidth), or [setThumbHeight](#setthumbheight) will automatically switch style to **'rects'**. You can still set a different style afterwards.

**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | One of the symbols: `\dots` or `\rects`. Alternatively, an integer 0 or 1, for each style respectively. |  
**Returns:** An integer 0 or 1.
### `drawLines`
 Whether to draw the connections between the nodes.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `drawRects`
 Whether to draw the nodes**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `gridOn`
 Whether to draw the grid.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `grid`
 The resolution of the grid.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Point of which x and y correspond to grid spacing on the horizontal and the vertical axis, respectively. If one of the two is 0, the grid on that axis will not be drawn. |  

### `thumbWidth`
 Sets the width of all nodes.
> **Note:** For compatibility with existing code, this will set the [style](#style) to **'rects'**.

**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Integer. |  

### `thumbHeight`
 Sets the height of all nodes.
> **Note:** For compatibility with existing code, this will set the [style](#style) to **'rects'**.

**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Integer. |  

### `thumbSize`
 Sets both [thumbWidth](#thumbwidth) and [thumbHeight](#thumbheight) to the argument.
### `strokeColor`
 The color used to draw the connections and the node labels.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  

### `fillColor`
 The default color used to draw the nodes. If the color of a specific node has been set using [setFillColor](#setfillcolor), it will take precedence.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  

### `selectionColor`
 The color of a node when it is selected.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  

### `gridColor`
 The color of the grid.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  

### `colors`
 Sets the [strokeColor](#strokecolor) and the [fillColor](#fillcolor) to the arguments, respectively.

### Interaction
### `index`
 The index of the *current* node, i.e. the node affected by [x](#x) and [y](#y) methods. This is the selected node with lowest index, or -1 if no selection.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Integer. |  

### `lastIndex`
 The last node selected, regardless of the current state of selection, or -1 if no node has yet been selected.
### `selectIndex`
 Selects the node at given index and makes it the current one, i.e. [currentvalue](#currentvalue) will relate to that node. As a special case, if the argument is -1 all nodes will be deselected.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Integer. |  

### `deselectIndex`
 Deselects the node at given index.
> **Note:** Not available in **Cocoa GUI**.

**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Integer. |  

### `editable`
 Whether any node is editable.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `setEditable`
 Sets whether the node at given index is editable. Regardless of this, no node will be editable unless [editable](#editable) is `true`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | An Integer. |  
| `flag` | A Boolean. |  

### `step`
 Makes the nodes snap (i.e. quantized) to the nearest multiple of the argument. Unless this is larger than 0, nodes will not be movable using keyboard.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `keepHorizontalOrder`
 Whether the position of nodes on the horizontal axis shall be restricted by their immediate neighbours (in order of their index). Setting this to `true` will immediately modify the positions of existing nodes to match the order.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `elasticSelection`
 Whether the relative positions of nodes within the selection can change when the selection is moved using mouse or keyboard, in order to adapt to obstacles (the view bounds or, in case [keepHorizontalOrder](#keephorizontalorder) is `true`, a neighbour node). If this is `false`, movement of multiple nodes will be blocked altogether when an obstacles is met, otherwise only the individual nodes will be blocked at their obstacles.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  


### Actions
### `action`
 The action object evaluated whenever the user moves a node.
### `metaAction`
 The action object evaluated whenever the user moves a node while the Ctrl key is pressed.
### `defaultKeyDownAction`
 Implements the default behavior on key presses. The default behavior is defined in the C++ implementation of the view instead of this method. See [View#Key and mouse event processing](../Classes/View.md#key-and-mouse-event-processing) for explanation of how to override the behavior.

### Drag and drop
### `defaultGetDrag`
**Returns:** The [value](#value).
### `defaultCanReceiveDrag`
**Returns:** True for any drag data, but the data should be in the same format as [value](#value).
### `defaultReceiveDrag`
 If the drag data is of the acceptable form (see [defaultCanReceiveDrag](#defaultcanreceivedrag) above), sets [value](#value) using that data.

## Examples

Use as envelope view

```supercollider
(
// use shift-click to keep a node selected
w = Window("envelope", Rect(150, Window.screenBounds.height - 250, 250, 100)).front;
w.view.decorator = FlowLayout(w.view.bounds);

b = EnvelopeView(w, Rect(0, 0, 230, 80))
    .drawLines_(true)
    .selectionColor_(Color.red)
    .drawRects_(true)
    .resize_(5)
    .step_(0.05)
    .action_({ |b| [b.index, b.value].postln })
    .thumbSize_(5)
    .value_([[0.0, 0.1, 0.5, 1.0], [0.1, 1.0, 0.8, 0.0]]);
w.front;
)

// show grid
b.grid = Point(0.2, 0.2);
b.gridOn_(true);

// show Env
b.setEnv(Env.asr(0.5, 1, 0.2));

// make the first point unmoveable
(
b.setEditable(0, false);
)
```


Use shift click to select/unselect the points

```supercollider
(
w = Window("envelope", Rect(150, Window.screenBounds.height - 250, 400, 150)).front;
w.view.decorator = FlowLayout(w.view.bounds);

b = EnvelopeView(w, Rect(0, 0, 350, 100))
    .thumbSize_(5)
    .drawLines_(true)
    .fillColor_(Color.green)
    .selectionColor_(Color.red)
    .drawRects_(true)
    .value_([(0.0, 0.1 .. 1.0), (0.0, 0.1 .. 1.0)])
    .setEditable(0, false);
)

(
r = Routine({
    var j = 0;
    20.do({ |i|
        b.selectIndex((b.size - 1).rand.abs);
        0.1.wait;
        b.x_(1.0.rand.abs);
        b.y_(1.0.rand.abs);
    });
    b.selectIndex(-1);
});
AppClock.play(r);
)
```


Show boxes with a string in it:

```supercollider
(
a = Window("text-boxes", Rect(200, 450, 450, 450));
a.view.decorator = FlowLayout(a.view.bounds);

b = EnvelopeView(a, Rect(0, 0, 440, 440))
    .thumbWidth_(60.0)
    .thumbHeight_(15.0)
    .drawLines_(true)
    .drawRects_(true)
    .selectionColor_(Color.red)
    .value_([[0.1, 0.4, 0.5, 0.3], [0.1, 0.2, 0.9, 0.7]]);
4.do({ |i|
    b.setString(i, ["this", "is", "so much", "fun"].at(i));
    b.setFillColor(i, [Color.yellow, Color.white, Color.green].choose);
});
a.front;
)

(
b.connect(3, [2.0, 0.0, 1.0]); // the text objects can be connected
b.connect(0, [2.0, 3.0, 1.0]);
)
```




