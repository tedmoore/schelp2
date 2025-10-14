# DragBoth

*A simple drag-and-drop source and receiver*

**Categories:** GUI>Views

**Related:** [DragSink](../Classes/DragSink.md), [DragSource](../Classes/DragSource.md)

## Description

[DragSource](../Classes/DragSource.md), [DragSink](../Classes/DragSink.md) and [DragBoth](../Classes/DragBoth.md) are a set of view classes intended as simple-to-use drag-and-drop sources and destinations. They are graphically represented as a simple rectangle, and their specialty is that they *do not require the Cmd/Ctrl key to be held down to initiate dragging*.
Akin to [StaticText](../Classes/StaticText.md) they can store arbitrary content in the [-object](../Classes/StaticText.md#-object) variable, and display it using [Object#-asString](../Classes/Object.md#-asstring). You can set the displayed text separately using [-string](../Classes/StaticText.md#-string), and keep it independent of the content if you set [-setBoth](../Classes/StaticText.md#-setboth) to `false`.
**DragBoth**, specifically, **accepts any** dropped data and stores it into the **-object** variable, as well as gives that variable as data **for dragging**.
See: [View#Drag and drop](../Classes/View.md#drag-and-drop) for a general description of the drag and drop mechanism.


## Class Methods



## Instance Methods

### `defaultGetDrag`
**Returns:** The [-object](../Classes/StaticText.md#-object).### `defaultCanReceiveDrag`
**Returns:** Always True.### `defaultReceiveDrag`
 Sets the [-object](../Classes/StaticText.md#-object) to the current drag data.
## Examples


```supercollider
(
w = Window.new.front;
w.addFlowLayout;
// store various kinds of objects in the drag source

// a string source
a = DragBoth(w, Rect(10, 10, 150, 20)).align_(\center).background_(Color.rand);
a.object = "drag us around";

a = DragBoth(w, Rect(10, 10, 150, 20)).align_(\center).background_(Color.rand);
a.object = "SUPERCOLLIDER";

8.do{
a = DragBoth(w, Rect(10, 10, 150, 20)).align_(\center).background_(Color.rand);
a.receiveDragHandler = { |obj| obj.object = View.currentDrag.scramble };
}
)
```




