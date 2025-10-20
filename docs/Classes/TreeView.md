# TreeView

*A view displaying a tree of items with columns*

**Categories:** GUI>Views

## Description

A view that displays a hierarchy of items. It is divided into rows and column: each row represents an item, and each column represents a different data field of the items.
The items are represented in code by instances of [TreeViewItem](../Classes/TreeViewItem.md), returned by the various TreeView methods. Top level items are added via the TreeView interface, while child items are added via the TreeViewItem interface, which also allows to manipulate items in more detail after their creation.
Items can be visually sorted with [#-sort](#-sort), or by clicking on one of the column headers, if [#-canSort](#-cansort) is enabled.
Each item can hold other views in each of its data fields, which allows for rich graphical interaction. See [TreeViewItem#-setView](../Classes/TreeViewItem.md#-setview).


## Class Methods



## Instance Methods


### Data

### `columns`
 Gets or sets the number of columns (data fields) and their names. When setting a smaller number of columns than the current the extra columns will be removed, and hence all the data stored stored in those columns.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An array of Strings for column names. |  


### `numColumns`
 The total number of columns (data fields).

### `addItem`
 Append a new top-level item.**Arguments:**

| Argument | Description |
|----------|-------------|
| `strings` | An array of Strings (or nil), each for the text of one data field. |  
**Returns:** An instance of TreeViewItem representing the new item.

### `insertItem`
 Insert a new top-level item at `index`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | The position at which to insert the item. |  
| `strings` | An array of Strings (or nil), each for the text of one data field. |  
**Returns:** An instance of TreeViewItem representing the new item.

### `removeItem`
 Remove the given `item`. After the item is removed, any usage of the related TreeViewItems will have no effect.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An instance of TreeViewItem. |  


### `numItems`
 The total number of items.

### `clear`
 Removes all items.

### `currentItem`
 Gets or sets the currently selected item.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An instance of TreeViewItem. |  
**Returns:** An instance of TreeViewItem or nil, if no current item.

### `itemAt`
 The item at `index`.

### `childAt`
 Alias for [#-itemAt](#-itemat), provided for compatibility with TreeViewItem.

### `addChild`
 Alias for [#-addItem](#-additem), provided for compatibility with TreeViewItem.

### `insertChild`
 Alias for [#-addChild](#-addchild), provided for compatibility with TreeViewItem.

### Appearance

### `sort`
 Sort items by data in `column`. This works regardless of [#-canSort](#-cansort).
> **Note:** Sorting has no effect on the logical order of the items, it only affects how they are displayed.

**Arguments:**

| Argument | Description |
|----------|-------------|
| `column` | The integer column index to sort by. |  
| `descending` | Whether to sort in descending or ascending fashion. The default is ascending. |  


### `columnWidth`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `column` | The integer index of a column |  
**Returns:** Integer width of column in pixels. If `column` is not in the range  `0..(numColumns-1)`, returns `-1`.

### `setColumnWidth`
Sets the width of a column. The rightmost column must extend at least to the right bound of the TreeView.**Arguments:**

| Argument | Description |
|----------|-------------|
| `column` | The integer index of the column to modify |  
| `width` | Integer width in pixels |  



### Interaction

### `canSort`
 Whether the user can sort the items by clicking on a column header. When setting to `true`, the items will be sorted immediately according to the current sorting column. While `true`, the view will also automatically sort new items. The default is `false`. See also: [#-sort](#-sort).

### Actions

### `itemPressedAction`
 The object to be evaluated when a mouse button is pressed on an item, passing this view as the argument.

### `onItemChanged`
 The object to be evaluated whenever the current item changes, passing this view as the argument.

## Examples


```
(
var t = TreeView().front;
t.columns_(["a", "b", "c", "d"]);
t.addItem(["A1", "B1", "C1", "D1"]);
t.addItem(["A2", "B2", "C2"]);
t.addItem(["A3", "B3"]);
t.addItem(["A4"]);
)


// sorting example
(
var names = ["black", "white", "red", "green", "blue", "cyan", "magenta", "yellow"];
var colors = names.collect{ |str| Color.perform(str.asSymbol) };
var window, tree, popup;
window = Window.new("TreeView example - RGBA colors").front;
window.view.layout_(VLayout(
    tree = TreeView()
));
tree.columns_(["Index", "Name", "Int", "Hex"]);
tree.font = Font.defaultMonoFace;
tree.setColumnWidth(0, 60);
tree.setColumnWidth(2, 130);
names.do{ |str, i|
    var intString = "% % % %".format(*(colors[i].asArray*255).asInteger);
    tree.addItem([i, str, intString, colors[i].hexString]);
};
tree.numItems.do{ |i|
    var c = [Color.clear, colors[i], Color.clear, Color.clear];
    tree.itemAt(i).colors_(c).textColors_(Color.grey);
};
tree.onItemChanged_({ |view|
    view.currentItem.strings.postln;
});
tree.canSort = true;
)
```




