# LineLayout

*Superclass of layouts that distribute views in a line*

**Categories:** GUI>Layout

**Related:** [HLayout](../Classes/HLayout.md), [VLayout](../Classes/VLayout.md), [GridLayout](../Classes/GridLayout.md), [StackLayout](../Classes/StackLayout.md), [GUI-Layout-Management](../Guides/GUI-Layout-Management.md)

## Description

This is an abstract superclass of [HLayout](../Classes/HLayout.md) and [VLayout](../Classes/VLayout.md) which distribute views in a horizontal or vertical line, respectively.

### Fine tuning
Each item can be assigned a **stretch factor** and an **alignment** flag to fine tune how its size and position are managed. This can be done at layout [construction](#*new), when an item is [added](#-add) or [inserted](#-insert) or for an already present item with [#-setStretch](#-setstretch) and [#-setAlignment](#-setalignment) methods.

The **stretch factor** only affects distribution in the direction of the layout (vertical or horizontal). All items have a stretch factor of 0 by default, so only their own preferences will determine space distribution. As soon as an item is assigned a stretch factor higher than 0, the space will be redistributed according to proportions of stretch factors.



### Leaving empty space
An empty space with an arbitrary stretch factor may be inserted using nil in place of an item in combination with the stretch factor. Similarly, an empty space of fixed size may be inserted using an integer in place of an item. See [constructor](#*new) and [#-add](#-add) for details.




## Class Methods




### `new`
Create a [HLayout](../Classes/HLayout.md) or a [VLayout](../Classes/VLayout.md) and immediately fill it with items given as arguments. (Note that LineLayout is an abstract class and can not be instantiated, but HLayout and VLayout inherit this constructor).**Arguments:**

| Argument | Description |
|----------|-------------|
| `... items` | Each item can be a **view**, a **layout**, **nil** (for stretchable empty space) or an **Integer** (for fixed-size empty space). |  
You can assign a **stretch factor** and/or **alignment** to an item by wrapping it into an array, followed by pairs of ('stretch', factor) and/or ('align', alignment). 'stretch' and 'align' may be abbreviated with 's' and 'a'. Simplified syntax for placing key-value pairs into an array comes handy (see [Syntax-Shortcuts#Creating arrays with key-value pairs](../Reference/Syntax-Shortcuts.md#creating-arrays-with-key-value-pairs), and the example below). For possible alignment values see [gui_alignments](../Reference/gui_alignments.md).If the item is a stretchable empty space (nil) alignment will have no effect; if the item is a fixed-size empty space (an Integer), it is unaffected by both the stretch factor and alignment.Example:
```
(
w = Window.new;
w.layout = VLayout(
    [Button().states_([["Foo"]]), stretch: 1, align: \bottomLeft],
    20,
    [TextView().string_("Bar\nBar\nBar\n"), s: 3],
    [nil, s: 1]
);
w.front;
)
```



## Instance Methods


### `add`
Add an item to the right or the bottom end of the line, for HLayout and VLayout respectively.**Arguments:**

| Argument | Description |
|----------|-------------|
| `item` | The item can be a **view**, a **layout**, an **Integer** (specifying amount in pixels of empty space) or **nil** (for stretchable empty space). |  
| `stretch` | An integer stretch factor. |  
| `align` | A symbol expressing the alignment. See [gui_alignments](../Reference/gui_alignments.md) for possible values. |  
If the item is a stretchable empty space (nil) the align argument will have no effect; if the item is a fixed-size empty space (an Integer) both stretch and align arguments will have no effect.
### `insert`
Insert an item at a specific position.**Arguments:**

| Argument | Description |
|----------|-------------|
| `item` | The item can be a **view**, a **layout**, an **Integer** (specifying amount in pixels of empty space) or **nil** (for stretchable empty space). |  
| `index` | The integer position among current items at which to insert the new item. If index is smaller than 0 or larger than the current amount of items, the new item will always be added to the end of the line. |  
| `stretch` | An integer stretch factor. |  
| `align` | A symbol expressing the alignment. See [gui_alignments](../Reference/gui_alignments.md) for possible values. |  
If the item is a stretchable empty space (nil) the align argument will have no effect; if the item is a fixed-size empty space (an Integer) both stretch and align arguments will have no effect.
### `setStretch`
Set stretch factor of an item contained in the layout.**Arguments:**

| Argument | Description |
|----------|-------------|
| `item` | A view or layout managed by this layout, or an Integer index of an item. |  
| `stretch` | An integer stretch factor. |  

### `setAlignment`
Set alignment of an item contained in the layout.**Arguments:**

| Argument | Description |
|----------|-------------|
| `item` | A view or a layout managed by this layout, or an Integer index of an item. |  
| `align` | A symbol expressing the alignment. See [gui_alignments](../Reference/gui_alignments.md) for possible values. |  

## Examples

Try resizing the window created by the following code.

```
(
w = Window.new;
w.layout = VLayout(
    TextView().string_("Foo\nBar\nFoo\nBar\nFoo"),
    HLayout(
        Button().states_([["Foo"]]),
        [TextField().string_("Bar"), stretch: 1],
        [TextField().string_("BarBarBar"), stretch: 4]
    )
);
w.front;
)
```


For a scroll view we need to set its canvas to a View with the desired layout.

```
(
var view = ScrollView();
view.canvas = View().layout_(VLayout(
    *(
        100.collect {
            Slider().orientation_(\horizontal).background_(Color.rand)
        }
    )
));
view.front;
)
```




