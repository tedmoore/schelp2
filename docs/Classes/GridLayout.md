# GridLayout

*A layout that organizes views in a grid*

**Categories:** GUI>Layout

**Related:** [HLayout](../Classes/HLayout.md), [VLayout](../Classes/VLayout.md), [StackLayout](../Classes/StackLayout.md), [GUI-Layout-Management](../Guides/GUI-Layout-Management.md)

## Description

GridLayout distributes its space into a **grid of rows and columns**, where each item can occupy **one or more cells**.
You can construct the layout in two ways using [#*rows](#*rows) and [#*columns](#*columns). In the former constructor you pass arrays of items by rows, and in the latter by columns. Items can also be added later using [#-add](#-add) and [#-addSpanning](#-addspanning). To remove an item, simply use [View#-remove](../Classes/View.md#-remove) for views, or [QObject#-destroy](../Classes/QObject.md#-destroy) for views or layouts.
It is possible to add more than one view into the same cell. The last added view will be the top-most. However, it is most probably more convenient to use a [StackLayout](../Classes/StackLayout.md) for that purpose.
The layout manages the grid size automatically: you can add an item at any row and cell number. When items are added or removed, the grid will re-adjust according to the last occupied row and column.

### Fine tuning
Each item can be assigned an **alignment** either at layout [construction](#*rows) or later using [#-setAlignment](#-setalignment). An item will then get at most its default size, if available (see: [View#-sizeHint](../Classes/View.md#-sizehint)), and will be aligned within its cell according to the specified alignment.

Each row or column can be assigned a **stretch factor** using [#-setRowStretch](#-setrowstretch) and [#-setColumnStretch](#-setcolumnstretch). Rows or columns that would otherwise get equal space are then distributed according to the relative proportions of their stretch factors.

Each row or column can also be assigned a **minimum** size using [#-setMinRowHeight](#-setminrowheight) and [#-setMinColumnWidth](#-setmincolumnwidth), to override the size constraints imposed by the contained views.

In addition to adjusting the spacing between cells using [Layout#-spacing](../Classes/Layout.md#-spacing) you can control the spacing between rows and between columns separately using [#-hSpacing](#-hspacing) and [#-vSpacing](#-vspacing).



### Leaving empty space
You can leave any cell empty by not placing any item into it, or at [construction](#*rows) using `nil` instead of a view or another layout. Note though that the empty cells will always be regarded as freely stretchable and will not impose any constraints on space distribution.




## Class Methods




### `rows`
 Creates a GridLayout and fills each row with an array of items given as arguments.**Arguments:**

| Argument | Description |
|----------|-------------|
| `... rows` | Each argument is an Array of items to form a consecutive row. An item can be a **view**, another **layout**, or **nil** for an empty cell. |  
You can make an item span more than one cell by wrapping it into an Array, followed by pairs of (\rows, number) and/or (\columns, number). You can also assign an alignment to an item by following it with a pair of (\align, alignment). \rows, \columns, and \align can be abbreviated with \r, \c, and \a, respectively. For possible alignment values see [gui_alignments](../Reference/gui_alignments.md). The simplified syntax for placing key-value pairs into an array comes handy (see [Syntax-Shortcuts#Creating Arrays with key-value pairs](../Reference/Syntax-Shortcuts.md#creating-arrays-with-key-value-pairs), and the example below). Example:
```
(
w = Window().layout_(GridLayout.rows(
    [Slider2D(), Slider2D(), [Slider(), rows: 2]],
    [Slider2D(), Slider2D()],
    [[Slider().orientation_(\horizontal), columns: 2]]
)).front;
)
```



### `columns`
 Creates a GridLayout and fills each column with an array of items given as arguments.**Arguments:**

| Argument | Description |
|----------|-------------|
| `... cols` | Each argument is an Array of items to form a consecutive column. An item can be a **view**, another **layout**, or **nil** for an empty cell. |  
To make an item span several cells, or assign an alignment to it, the same instructions as for [#*rows](#*rows) apply.

## Instance Methods


### `add`
 Adds an item into the cell at specified row and column.**Arguments:**

| Argument | Description |
|----------|-------------|
| `item` | The item can be a **view** or another **layout**. |  
| `row` | The row index. |  
| `column` | The column index. |  
| `align` | A symbol denoting the alignment, or nil. See [gui_alignments](../Reference/gui_alignments.md) for possible values. |  

### `addSpanning`
 Adds an item into the grid so as to occupy several cells.**Arguments:**

| Argument | Description |
|----------|-------------|
| `item` | The item can be a **view** or another **layout**. |  
| `row` | The row index. |  
| `column` | The column index. |  
| `rowSpan` | The amount of cells to occupy in vertical direction. |  
| `columnSpan` | The amount of cells to occupy in horizontal direction. |  
| `align` | A symbol denoting the alignment, or nil. See [gui_alignments](../Reference/gui_alignments.md) for possible values. |  

### `hSpacing`
 The spacing between columns, in Integer amount of pixels.
### `vSpacing`
 The spacing between rows, in Integer amount of pixels.
### `setRowStretch`
 Sets the stretch factor of a row. By default rows have a stretch factor of 0. If a larger factor is assigned to a row, rows will get their space redistributed according to the relative proportions of their factors.**Arguments:**

| Argument | Description |
|----------|-------------|
| `row` | The index of a row. |  
| `factor` | An Integer. |  

### `setColumnStretch`
 Sets the stretch factor of a column. By default columns have a stretch factor of 0. If a larger factor is assigned to a column, columns will get their space redistributed according to the relative proportions of their factors.**Arguments:**

| Argument | Description |
|----------|-------------|
| `column` | The index of a column. |  
| `factor` | An Integer. |  

### `setAlignment`
 Sets the alignment of an item managed by the layout.**Arguments:**

| Argument | Description |
|----------|-------------|
| `item` | A view or a layout managed by this layout, or a Point of which x denotes the column index and y the row index of an item. |  
| `align` | A symbol denoting the alignment. See [gui_alignments](../Reference/gui_alignments.md) for possible values. |  

### `minRowHeight`
 Gets the minimum height assigned to a row.**Arguments:**

| Argument | Description |
|----------|-------------|
| `row` | The index of a row. |  

### `setMinRowHeight`
 Sets the minimum height of row.**Arguments:**

| Argument | Description |
|----------|-------------|
| `row` | The index of a row. |  
| `height` | An Integer amount of pixels. |  

### `minColumnWidth`
 Gets the minimum width assigned to a column.**Arguments:**

| Argument | Description |
|----------|-------------|
| `column` | The index of a column. |  

### `setMinColumnWidth`
 Sets the minimum width of a column.**Arguments:**

| Argument | Description |
|----------|-------------|
| `column` | The index of a column. |  
| `width` | An Integer amount of pixels. |  


