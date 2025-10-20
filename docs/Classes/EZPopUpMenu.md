# EZPopUpMenu

*A wrapper class for a label plus a popUpMenu with per item actions*

**Categories:** GUI>EZ-GUI

**Related:** [PopUpMenu](../Classes/PopUpMenu.md)

## Description

EZPopUpMenu is wrapper class which creates an (optional) label and a popUpMenu. It includes per item actions as well as a global action which are both evaluated upon selection of an item. Convenience methods for inserting and deleting menu items are also included . If the parent is nil, then EZPopUpMenu will create its own window.See [EZGui](../Classes/EZGui.md) and [EZLists](../Classes/EZLists.md) for all of the options.

### Some Important Issues Regarding EZPopUpMenu
The convenience methods for EZPopUpMenu require that the items array is an array of associations of labels and functions, not like in [PopUpMenu](../Classes/PopUpMenu.md), where items is simply an array of strings. If `label` is `nil`, then no staticText is created.




## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `parentView` | The parent view or window. If the parent is nil, then EZPopUpMenu will create its own [Window](../Classes/Window.md), and place it conveniently on the screen if the bounds are a [Point](../Classes/Point.md). If the bounds are a [Rect](../Classes/Rect.md), then the [Rect](../Classes/Rect.md) determines the window bounds. |  
| `bounds` | An instance of [Rect](../Classes/Rect.md) or [Point](../Classes/Point.md). Default value is `160@22`. |  
| `label` | The label. Default value is `nil`. If `nil`, then no [StaticText](../Classes/StaticText.md) is created. |  
| `items` | Default value is `nil`. An [Array](../Classes/Array.md) of [Association](../Classes/Association.md)s `['label' -> { |menuObj| value }, ]`. Or and [Array](../Classes/Array.md) [Symbol](../Classes/Symbol.md)s (if you are only using `globalAction`). |  
| `globalAction` | A global function to be performed in addition to the item functions `{ |menuObj| value }`. |  
| `initVal` | Initial value of the menu, i.e. the index selected. Default value is 0. |  
| `initAction` | An instance of [Boolean](../Classes/Boolean.md). Performs the action at `initVal` on creation of the menu, plus the `globalAction`. Default value is `false`. |  
| `labelWidth` | Default value is 80. |  
| `labelHeight` | Default value is 20. Not used if layout is `\horz`. |  
| `layout` | `\vert` or `\horz`. default is `\horz`. |  
| `gap` | A [Point](../Classes/Point.md). By default, the view tries to get its parent's `gap`, otherwise it defaults to `2@2`. Setting it overrides these. |  
| `margin` | A [Point](../Classes/Point.md). This will inset the bounds occupied by the subviews of view. |  

```
(
w = Window.new.front;
w.view.decorator = FlowLayout(w.view.bounds);
g = EZPopUpMenu.new(
    w,
    230@22,
    "A PopUpMenu: ",
    [
        \item0 ->{ |a| ("this is item 0 of " ++ a).postln },
        \item1 ->{ |a| ("this is item 1 of " ++ a).postln },
        \item2 ->{ |a| ("this is item 2 of " ++ a).postln },
    ],
    globalAction: { |a| ("this is a global action of "++a.asString).postln },
    initVal: 1,
    initAction: true,
    labelWidth: 120,
    labelHeight: 20,
    layout: \horz,
    gap: 2@2
);
)

// or a more simple syntax:
(
w = Window.new.front;
w.view.decorator = FlowLayout(w.view.bounds);
g = EZPopUpMenu.new(w, 200@22, "Menu: ");
g.addItem(\item0, { |a| ("this is item 0 of " ++ a).postln });
g.addItem(\item1, { |a| ("this is item 1 of " ++ a).postln });
g.addItem(\item2, { |a| ("this is item 2 of " ++ a).postln });
g.value = 0;
)
```



## Instance Methods


### Changing Appearance

### `setColors`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `stringBackground` | An instance of [Color](../Classes/Color.md). The `background` of the label and unit views. |  
| `stringColor` | An instance of [Color](../Classes/Color.md). The `stringColor` of the label and unit views. |  
| `menuBackground` | An instance of [Color](../Classes/Color.md). The `background` of the menu. |  
| `menuStringColor` | An instance of [Color](../Classes/Color.md). The `stringColor` of the menu. |  
| `background` | An instance of [Color](../Classes/Color.md). The `background` of the list view. |  


### `font`
Set the [Font](../Classes/Font.md) used by all the views.**Arguments:**

| Argument | Description |
|----------|-------------|
| `font` | An instance of [Font](../Classes/Font.md). |  


## Examples


```
// try several examples together
(

// many menus
// inherits the parent's decorator gap

(
w = Window.new("oscillators", Rect(200, 500, 200, 160)).front;
w.view.decorator = FlowLayout(w.view.bounds).gap_(2@2);
5.do{ |i|
    g = EZPopUpMenu.new(w, 190@22, "Oscillator % : ".format(i+1));
    g.addItem(\off, { "off".postln });
    g.addItem(\sine, { "sine".postln });
    g.addItem(\saw, { "saw".postln });
    g.addItem(\pulse, { "pulse".postln });
    g.setColors(Color.grey, Color.white);
    g.value = 0;
};
w.bounds = w.bounds.moveBy(300, 60);
);


// Creates its own window if parentView is nil:
(
g = EZPopUpMenu.new(nil, 250@22, " Select : ");
g.addItem(\item0, { "this is item 0".postln });
g.addItem(\item1, { "this is item 1".postln });
g.addItem(\item2, { "this is item 2".postln });
g.setColors(Color.grey, Color.white);
g.value = 0;

);

// layout vertical:
(
g = EZPopUpMenu.new(nil, 200@42, " Choose", layout: \vert);
g.addItem(\item0, { "this is item 0".postln });
g.addItem(\item1, { "this is item 1".postln });
g.addItem(\item2, { "this is item 2".postln });
g.setColors(Color.grey, Color.white);
g.window.bounds = g.window.bounds.moveBy(300, -200);
g.value = 0;
);

// No labelView created, so set the window title;
(
g = EZPopUpMenu.new(bounds: 180@22); // no label
g.addItem(\item0, { "this is item 0".postln });
g.addItem(\item1, { "this is item 1".postln });
g.addItem(\item2, { "this is item 2".postln });
g.value = 0;
g.window.name = " choose item";
g.window.bounds = g.window.bounds.moveBy(0, -200);
);
)
// insertItem;

(
g = EZPopUpMenu.new(nil, 200@22, "Menu:");
g.addItem(\item0, { "this is item 0".postln });
g.addItem(\item1, { "this is item 1".postln });
g.addItem(\item2, { "this is item 2".postln });
g.addItem(\item4, { "this is item 4".postln });
g.value = 0;
);

g.insertItem(3, \item3, { "this is item 3".postln });


// remove Item ;

(
w = Window.new.front;
w.view.decorator = FlowLayout(w.view.bounds);
g = EZPopUpMenu.new(w, 200@22, "Menu:");
g.addItem(\item0, { "this is item 0".postln });
g.addItem(\item1, { "this is item 1".postln });
g.addItem(\item2, { "this is item 2".postln });
g.addItem(\item4, { "this is item 4".postln });
g.insertItem(3, \item3, { "this is item 3".postln });
g.value = 0;
)

g. removeItemAt(0);



// replace item;
(
g = EZPopUpMenu.new(nil, 200@22, "List:");
g.addItem(\item0, { "this is item 0".postln });
g.addItem(\item1, { "this is item 1".postln });
g.addItem(\item2, { "this is item 2".postln });
g.addItem(\item3, { "this is item 3".postln });
)

g.replaceItemAt(2, \item2_replaced, { "this is item 2 replaced".postln });
```




