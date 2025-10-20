# TreeViewItem

*An item in TreeView*

**Categories:** GUI>Views

## Description

An instance of TreeViewItem represents an item in TreeView. There may be multiple instances representing the same item, e.g. after calling [TreeView#-currentItem](../Classes/TreeView.md#-currentitem) multiple times.


## Instance Methods


### `index`
**Returns:** An integer position of this item among its siblings.
### `parent`
**Returns:** An new instance of TreeViewItem representing the parent item.
### `childAt`
**Returns:** A new instance of TreeViewItem representing the child item at `index`.
### `addChild`
 Appends a new child to this item.**Arguments:**

| Argument | Description |
|----------|-------------|
| `strings` | An array of Strings (or nil), each for the text of one data field. |  
**Returns:** An instance of TreeViewItem representing the new item.
### `insertChild`
 Inserts a new child to this item at `index`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | The position at which to insert the child. |  
| `strings` | An array of Strings (or nil), each for the text of one data field. |  
**Returns:** An instance of TreeViewItem representing the new item.
### `strings`
 The text in the data fields.**Arguments:**

| Argument | Description |
|----------|-------------|
| `strings` | An array of Strings (or nil), each for the text of one data field. |  

### `setString`
 Sets the text in the given data field.**Arguments:**

| Argument | Description |
|----------|-------------|
| `column` | An integer index of a data field. |  
| `string` | A String or nil. |  

### `colors`
 The background colors of the data fields.**Arguments:**

| Argument | Description |
|----------|-------------|
| `colors` | An array of Colors, each for the color of one data field. |  

### `setColor`
 Sets the background color of the given data field.**Arguments:**

| Argument | Description |
|----------|-------------|
| `column` | An integer index of a data field. |  
| `color` | A Color. |  

### `textColors`
 The text colors of the data fields.**Arguments:**

| Argument | Description |
|----------|-------------|
| `textColors` | An array of Colors, each for the color of one data field. |  

### `setTextColor`
 Sets the text color of the given data field.**Arguments:**

| Argument | Description |
|----------|-------------|
| `column` | An integer index of a data field. |  
| `color` | A Color. |  

### `setView`
 Places another view into the given data field. Only one view can be placed into a data field at once. If a view is already present, it will be removed and destroyed. If the number of data fields decreases due to a call to [TreeView#-columns](../Classes/TreeView.md#-columns), the views contained in removed data fields will also be removed and destroyed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `column` | An integer index of a data field. |  
| `view` | A View. |  

### `removeView`
 Removes the view from the given data field, if any.**Arguments:**

| Argument | Description |
|----------|-------------|
| `column` | An integer index of a data field. |  

### `view`
 The view in the given data field.**Arguments:**

| Argument | Description |
|----------|-------------|
| `column` | An integer index of a data field. |  

### `==`
 Implements equality comparison between two TreeViewItem instances. Two instances are equal if they represent the same item in TreeView.**Returns:** A Boolean.
### `isNull`
 Whether the item is invalid. After an item is removed, all related TreeViewItem instances become invalid.**Returns:** A Boolean.
## Examples


```
(
t = TreeView().front;
t.columns_(["one", "two", "three"]);
t.addItem(["Alice", "Anna", "Anders"]);
t.addItem(["Bob", "Beatrice", "Benny"]);
t.addItem(["Cleo", "Conrad", "Cecilia"]);
)

i = t.itemAt(1);  // get an item

i.setString(1, "Hans");
i.setColor(1, Color.red);
i.setTextColor(1, Color.white);

i.addChild(["Bengt", "Bodil", "Ben"]);
i.strings;
i.childAt(0).strings;
```




