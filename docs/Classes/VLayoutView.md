# VLayoutView

*A container view that arranges its children vertically*

**Categories:** GUI>Views

**Related:** [HLayoutView](../Classes/HLayoutView.md), [CompositeView](../Classes/CompositeView.md)

## Description


> **Note:** In Qt GUI, this class has been rendered **obsolete** by a special set of layout classes; they are easier to use and more flexible. See [VLayout](../Classes/VLayout.md) for an equivalent to this class, and [GUI-Layout-Management](../Guides/GUI-Layout-Management.md) for a general description of the Qt layout system.


VLayoutView can be a parent to other views, and it automatically arranges its child views in vertical order, expanding their width to its own bounds. Only the height of the children is relevant.
When arranging its children, VLayoutView takes the values of their 'minHeight' and 'maxHeight' properties into account. This is useful when a child's [resize](../Classes/View.md#-resize) mode is set to 4, 5, or 6. See [#examples](#examples) below.
VLayoutView inherits some useful formatting methods from its superclasses.

> **Note:** VLayoutView is designed mainly for grouping and placing widgets. While you can set it to accept key presses, it does not accept mouse clicks or drags.




## Class Methods


## Examples


```supercollider
(
q = 10;
w = Window.new;

v = VLayoutView(w, Rect(10, 10, 300, 300));

Array.fill(q, { |i|
    Slider(v, Rect(0, 0, 75, 20)).value_(i / q)
});

w.front
)

// show the area of the view.
v.background_(Color.rand) // The sliders automatically expand to the optimal width
```


Stretching the layout view; Slider height is fixed:

```supercollider
(
q = 10;
w = Window.new;

v = VLayoutView(w, Rect(10, 10, 300, 300));
v.background_(Color.rand);
v.resize = 5; // elastic
Array.fill(q, { |i|
    var s;
    s = Slider(v, Rect(0, 0, 55, 20)); // The bounds.width are irrelevant here. They expand to the optimal width
    s.value = i / q;
    s
});
StaticText(v, Rect(0, 0, 55, 20)).background_(Color.rand).string_("Some Example Text").align_(\center);
w.front
)
```


Stretching the layout view and the contents; if all the contents are elastic, the heights of the contents are perfectly divided up. In this example, the StaticText is not elastic in order to preserve its height.

```supercollider
(
q = 10;
w = Window.new;

v = VLayoutView(w, Rect(10, 10, 300, 300));
v.background_(Color.rand);
v.resize = 5; // elastic
Array.fill(q, { |i|
    var s;
    s = Slider(v, Rect(0, 0, 75, 20));
    s.resize = 5; // elastic
    s.value = i / q;
    s
});
StaticText(v, Rect(0, 0, 55, 40))
    .background_(Color.rand).string_("Some Example Text")
    .align_(\center);

w.front
)
```


Mixed stretching modes:

```supercollider
(
q = 5;
w = Window.new;

v = VLayoutView(w, Rect(10, 10, 300, 300));
v.resize = 5; // elastic
v.background_(Color.grey);
Array.fill(q, { |i|
    var s;
    s = Slider(v, Rect(0, 0, 75, 20)).background_(Color.rand);
    s.value = i / 5;
    if(i < 2, {
        s.resize = 5; // some elastic
        s.setProperty(\minHeight, 20);
    }, {
        s.resize = 1; // some not elastic
    });
    s
});
StaticText(v, Rect(0, 0, 55, 20)).background_(Color.rand).string_("Some Example Text").align_(\center);

w.front
)
```


Set minimum heights; beware that if the layout view height is smaller than the combined height of all the contents, things might disappear when you try to handle them with the mouse:

```supercollider
(
q = 5;
w = Window.new;

v = VLayoutView(w, Rect(10, 10, 300, 300));
v.resize = 5; // elastic
v.background_(Color.grey);
Array.fill(q, { |i|
    var s;
    s = Slider(v, Rect(0, 0, 75, 20)).background_(Color.blue.alpha_(0.2));
    s.value = i / 5;
    s.resize = 5;
    s.setProperty(\minHeight, 20);
    s.setProperty(\maxHeight, 40);
    s
});
w.front
)
```


Spacing:

```supercollider
(
q = 10;
w = Window.new;

v = VLayoutView(w, Rect(10, 10, 300, 300));
v.setProperty(\spacing, 0);

Array.fill(q, {
    Slider(v, Rect(0, 0, 75, 20))
});

w.front
)
```


Nesting: use VLayoutView and HLayoutView in combination:

```supercollider
(
q = 10;
w = Window.new("nesting", Rect(30, 30, 400, 700));

v = VLayoutView(w, Rect(10, 10, 300, 600));

v.background = Color.rand;

Array.fill(q, { |i|
    Slider(v, Rect(0, 0, 75, 20)).value_(i / q)
});

StaticText(v, Rect(0, 0, 55, 20)).background_(Color.rand).string_("Some Example Text").align_(\center);

h = HLayoutView(v, Rect(10, 10, 300, 300));

Array.fill(q, { |i|
    Slider(h, Rect(0, 0, 20, 70)).value_(i / q)
});
h.background = Color.rand;

w.front
)
```




