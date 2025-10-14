# HLayout

*A layout that distributes views in a horizontal line*

**Categories:** GUI>Layout

**Related:** [LineLayout](../Classes/LineLayout.md), [VLayout](../Classes/VLayout.md), [GridLayout](../Classes/GridLayout.md), [StackLayout](../Classes/StackLayout.md), [GUI-Layout-Management](../Guides/GUI-Layout-Management.md)

## Description

See documentation of superclass [LineLayout](../Classes/LineLayout.md) for details.

## Examples


```supercollider
// simple example
(
w = Window().front;
a = { Button(w) } ! 10;
w.layout = HLayout(*a);
);

// for a scroll view we need to set its canvas to a View with the desired layout
(
var view = ScrollView();
view.canvas = View().layout_(HLayout(
    *(
        100.collect {
            Slider().orientation_(\vertical).background_(Color.rand)
        }
    )
));
view.front;
)

// combining HLayout and VLayout

(
w = Window().front;
a = { { Button(w) } ! 10 } ! 10;
w.layout = HLayout(*a.collect { |x| VLayout(*x) });
)

(
w = Window().front;
a = { { PopUpMenu(w, Rect(0, 0, 50, 20)).items_({ "abcdefghijklmno".scramble.keep(3) } ! 7) } ! 10 } ! 10;
w.layout = HLayout(*a.collect { |x| VLayout(*x) });
)

(
w = Window().front;
a = { HLayout(Slider(w, Rect(0, 0, 130, 20)), Button(w)) } ! 12;
b = { Slider2D(w) } ! 3;
w.layout = HLayout(VLayout(*a), VLayout(*b));
)

(
w = Window().front;
f = { SoundFileView(w).load(ExampleFiles.child, 1e5.rand, 1e4) };
a = { HLayout(VLayout(*{ Slider(w, Rect(0, 0, 230, 20)).minSize_(Size(130, 20)) } ! 3), f.value) } ! 4;
w.layout = HLayout(VLayout(*a));
)
```



## Class Methods




## Instance Methods



