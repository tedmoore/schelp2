# ScrollView

*A container view that can scroll its contents*

**Categories:** GUI>Views

**Related:** [CompositeView](../Classes/CompositeView.md)

## Description

A container view which allows the user to scroll across contents when they exceed the view's bounds.

### The canvas
The view places the children onto a *canvas*, which may then be scrolled. The child views' position is always relative to the canvas, and thus not affected by scrolling.

The size of the canvas is always equal to the collective bounds of the children, and automatically adjusts when they are added, moved, resized and removed. If you wish to set it to a particular size, you could do so by first placing e.g. a [CompositeView](../Classes/CompositeView.md) (or another container) of desired size, and then placing all the other views into that container.

Exceptionally though, you can **replace the canvas** with any other view (e.g. simply with [View](../Classes/View.md)), which allows you to install a [layout](../Classes/Layout.md) on it. In that case, the canvas will fill the whole visible area of the ScrollView, if the layout contents allow so, or a larger area, if the layout contents demand so. Effectively, the **contents will resize** together with the ScrollView, unless their size constraints prevent that, and if [#-autohidesScrollers](#-autohidesscrollers) is `true`, a scrollbar will only be shown if the contents can not be resized small enough in the scrollbar's direction. See [#-canvas](#-canvas) for further explanation.



### Restrictions

> **Note:** - The [View#-resize](../Classes/View.md#-resize) mode of the children is ignored.
- One should not use a decorator such as FlowLayout directly on a ScrollView, only on a container view placed within it.





## Class Methods



## Instance Methods


### Geometry

### `canvas`
Returns the current canvas that carries the child views, or replaces it with another.By default, the canvas is a subclass of QObject, and hence does not allow the type of manipulations that views do. However, it can only be replaced with a subclass of View, which greatly extends the possibilities, including the use of layouts on the canvas.The new canvas will always resize with the ScrollView, as far its size constraints allow. A plain [View](../Classes/View.md) which completely disregards its children will be freely resizable, and hence the scrolling will never be possible, since the scrollbars are activated according to the size of the canvas. To prevent this, you can either place explicit size constraints on it using [View#-minSize](../Classes/View.md#-minsize) and similar, or you can install a layout on it, which will forward to it the size constraints of the children.See the [example](#examples) below.Once the canvas is replaced, new views constructed with the ScrollView as the parent will end up as children of the canvas view, equivalent to constructing them with the canvas as the parent, or inserting them into the layout installed on the canvas.> **⚠️ Warning:** Replacing the canvas will remove and destroy all the views placed on the previous one!

### `innerBounds`
Returns either the rectangle corresponding to the size of the canvas, or the visible area of the ScrollView's background, whichever is larger. The position of the rectangle is always 0@0.See the [discussion](#description) above regarding the size of the canvas.**Returns:** A Rect.

### `visibleOrigin`
Gets the position on the canvas corresponding to its upper-left-most visible point, or moves the canvas so as to leave the given point on it at the top-left corner of the visible bounds, if possible.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Point. |  


### Behavior

### `autohidesScrollers`
Sets or gets whether the view hides one or another scrollbar if the contents do not exceed the view's bounds in the scrollbar's direction.If [#-hasHorizontalScroller](#-hashorizontalscroller) or [#-hasVerticalScroller](#-hasverticalscroller) is set to `false`, the respective scrollbar will always be hidden, regardless of this policy.Defaults to **true**.

### `hasHorizontalScroller`
Sets or gets whether the view has the horizontal scrollbar. If this is `true`, the scrollbar may still be hidden if [#-autohidesScrollers](#-autohidesscrollers) allows so; however, if this is `false` the scrollbar will never be shown.Defaults to **true**.

### `hasVerticalScroller`
Sets or gets whether the view has the vertical scrollbar. If this is `true`, the scrollbar may still be hidden if [#-autohidesScrollers](#-autohidesscrollers) allows so; however, if this it `false` the scrollbar will never be shown.Defaults to **true**.

### Appearance

### `hasBorder`
Sets or gets whether the view draws its border.Defaults to **true**.

### Actions

### `action`
Sets or gets the object to be evaluated when the user moves the scrollbars, or when [#-visibleOrigin](#-visibleorigin) is set.

## Examples


### Layout management on the canvas
By replacing the canvas of the ScrollView with a View, and installing a layout on it, the contents will expand to the edge of the ScrollView, and only exceed the edge if necessary.


```
(
var scroll = ScrollView(bounds: Rect(0, 0, 300, 300).center_(Window.availableBounds.center));
var canvas = View();
var layout;
var i = 0;

var makeEntry = {
    var view = View().background_(Color.rand).layout_(
        HLayout(
            TextField().string_(("This is entry number " + i.asString)),
            Button().states_([["Delete"]]).action_({ view.remove; i = i - 1 })
        )
    );
    i = i + 1;
    view;
};

layout = VLayout();
layout.add (View().background_(Color.black).layout_(
    HLayout(
        Button().states_([["Add"]]).action_({ layout.insert(makeEntry.(), i) }),
        nil // stretch remaining empty space
    )
));

canvas.layout = layout;
10.do { canvas.layout.add(makeEntry.()) };
canvas.layout.add(nil); // stretch remaining empty space

scroll.canvas = canvas;
scroll.front;
)
```




### Force a canvas size

```
(
w = Window.new;

b = ScrollView(w, Rect(0, 0, 300, 300)).hasBorder_(true);
c = CompositeView(b, Rect(0, 0, 500, 500)); // 'canvas' is this big
c.decorator = FlowLayout(c.bounds); // now we can use a decorator

Slider2D(c, Rect(0, 0, 240, 240));
Slider2D(c, Rect(0, 0, 240, 240));
Slider2D(c, Rect(0, 0, 240, 240));

c.decorator.nextLine;
w.front;
)
```




### "Rulers", using an action function

```
(
var drawFunc;
w = Window.new;

a = ScrollView(w, Rect(40, 40, 300, 300));
b = ScrollView(w, Rect(0, 40, 40, 300)).hasHorizontalScroller_(false).hasVerticalScroller_(false);
c = ScrollView(w, Rect(40, 0, 300, 40)).hasHorizontalScroller_(false).hasVerticalScroller_(false);
b.background = Color.grey;
c.background = Color.grey;

d = UserView(a, Rect(0, 0, 620, 620));
e = UserView(b, Rect(0, 0, 40, 630));
f = UserView(c, Rect(0, 0, 630, 40));

a.action = { var origin;
    origin = a.visibleOrigin;
    b.visibleOrigin = 0@(origin.y);
    c.visibleOrigin = (origin.x)@0;
};

drawFunc = {
    30.do({ |i|
        (i+1).asString.drawAtPoint((i+1 * 20)@0, Font("Courier", 9), Color.black);
    });
};

d.drawFunc = {
    Pen.use({
        Pen.translate(0, 5);
        drawFunc.value;
    });
    Pen.translate(15, 0).rotate(0.5pi);
    drawFunc.value;
};

e.drawFunc = {
    Pen.translate(40, 0).rotate(0.5pi);
    drawFunc.value;
};

f.drawFunc = {
    Pen.translate(0, 25);
    drawFunc.value;
};

w.front;
)
```





> **Note:** Apparently a method 'autoScrolls' was planned but not implemented yet; its doc said that it sets or gets whether the view scrolls automatically when you drag on a child view past the edge of visible bounds.






