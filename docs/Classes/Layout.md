# Layout

*Superclass of all GUI layouts*

**Categories:** GUI>Layout

**Related:** [HLayout](../Classes/HLayout.md), [VLayout](../Classes/VLayout.md), [GridLayout](../Classes/GridLayout.md), [StackLayout](../Classes/StackLayout.md), [GUI-Layout-Management](../Guides/GUI-Layout-Management.md)

## Description

Layout is the abstract superclass of all layouts. Any layout can be installed on a view with the view's ['layout'](../Classes/View.md#-layout) setter method. See [GUI-Layout-Management](../Guides/GUI-Layout-Management.md) for details of operation common to all layouts.


## Instance Methods

### `spacing`
The amount of empty pixels left between the managed views.**Arguments:**

| Argument | Description |
|----------|-------------|
| `spacing` | An integer representing the spacing in pixels. |  
### `margins`
The amount of empty pixels left between the edges of the parent view and the managed children.**Arguments:**

| Argument | Description |
|----------|-------------|
| `margins` | An array of four integers defining margins in the following order: left margin, top margin, right margin, bottom margin; or an array of two integers applied to left/right margin and top/bottom margin respectively; or a single integer applied to all margins. |  

## Examples


```supercollider
w = Window.new;
w.layout = HLayout(TextView().string_("One"), TextView().string_("Two"));
w.layout.spacing = 20;
w.layout.margins = [10, 30, 10, 30];
w.front;
```




