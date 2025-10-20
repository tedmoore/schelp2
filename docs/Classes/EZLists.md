# EZLists

*An abstract superclass for EZListView and EZPopUpMenu*

**Categories:** GUI>EZ-GUI

**Related:** [EZListView](../Classes/EZListView.md), [EZPopUpMenu](../Classes/EZPopUpMenu.md)

## Description

Users will not normally directly create instances of EZLists, but only use it through its subclasses. It provides the basic mechanisms for [EZListView](../Classes/EZListView.md) and [EZPopUpMenu](../Classes/EZPopUpMenu.md).


## Class Methods


### `new`


## Instance Methods


### Building and Changing the List

### `globalAction`
Set/get the global function to be performed in addition to the item functions: `{ |listObj| value }`.

### `items`
Set/get an [Array](../Classes/Array.md) of Associations including the labels and the item functions: `['label' -> { |listObj| value }, ]`.In menus, the macOS graphics system gives special meanings to some characters. See [PopUpMenu](../Classes/PopUpMenu.md) ; Or and [Array](../Classes/Array.md) [Symbol](../Classes/Symbol.md)s (if you are only using `globalAction`). [Array](../Classes/Array.md)s of [Symbol](../Classes/Symbol.md)s will get converted into and array of [Association](../Classes/Association.md)s with and empty [Function](../Classes/Function.md) `['label' -> { }, ]`.

### `item`
**Returns:** the item label of the current selection.

### `itemFunc`
**Returns:** the item function of the current selection.

### `addItem`
Adds an item.**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` | An instance of [String](../Classes/String.md) or [Symbol](../Classes/Symbol.md). The name of the list/menu item. |  
| `action` | An instance of [Function](../Classes/Function.md). |  


### `insertItem`
Inserts a list/menu item at index position.**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | An [Integer](../Classes/Integer.md). The index where to insert an item. |  
| `name` | An instance of [String](../Classes/String.md) or [Symbol](../Classes/Symbol.md). The name of the list/menu item. |  
| `action` | An instance of [Function](../Classes/Function.md). |  


### `replaceItemAt`
Replace a list/menu item at index position.**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | An [Integer](../Classes/Integer.md). The index where to insert an item. |  
| `name` | An instance of [String](../Classes/String.md) or [Symbol](../Classes/Symbol.md). The name of the list/menu item. Default is the current item label. |  
| `action` | An instance of [Function](../Classes/Function.md). Default is the current item action. |  


### `removeItemAt`
Removes a list/menu item at index position.**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | An [Integer](../Classes/Integer.md). The index where to remove an item. |  


### `remove`
Removes both the view, label and the list/menu from the parent view.

### Accessing Values

### `value`
Gets/sets the list/menu to the index at value. Does not perform the action.**Arguments:**

| Argument | Description |
|----------|-------------|
| `val` | An [Integer](../Classes/Integer.md). |  


### `valueAction`
Sets the value and performs the action at the index value and the global action.**Arguments:**

| Argument | Description |
|----------|-------------|
| `val` | An [Integer](../Classes/Integer.md). |  


### `doAction`
Performs the action at the current index and the global action.

### `initViews`
Called by init and overridden by all subclasses. This is where the class specific views are built.


