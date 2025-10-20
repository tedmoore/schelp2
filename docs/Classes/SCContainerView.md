# SCContainerView

*An abstract superclass for container views*

**Categories:** GUI>Kits>Cocoa

**Related:** [CompositeView](../Classes/CompositeView.md), [HLayoutView](../Classes/HLayoutView.md), [VLayoutView](../Classes/VLayoutView.md), [ScrollView](../Classes/ScrollView.md)

## Description

Users will not normally directly create instances of ContainerView, but only use it through its subclasses. It provides the basic mechanisms for container views of various kinds, which are used for placing and grouping widgets in a window.

### Some Important Issues Regarding ContainerView
Container views are meant for placing and grouping child views and widgets. While they accept key actions, many do not accept mouse clicks or drags. The exception is SCTopView and its subclasses.




## Class Methods


## Instance Methods


### Accessing Instance and Class Variables

### `decorator`
An automatic layout management for a container. Currently the only one existing is [FlowLayout](../Classes/FlowLayout.md).
> **Note:** Crucial Library also has a useful layout tool called GridLayout.

**Arguments:**

| Argument | Description |
|----------|-------------|
| `arg1` |  |  


### `addFlowLayout`
A convenience utility which sets decorator to [FlowLayout](../Classes/FlowLayout.md) and returns the decorator. See [FlowLayout](../Classes/FlowLayout.md) for examples.**Arguments:**

| Argument | Description |
|----------|-------------|
| `margin` | An instance of [Point](../Classes/Point.md). |  
| `gap` | An instance of [Point](../Classes/Point.md). |  


### `children`
An array containing all the views (children) contained in the container.

### Adding and Removing Subviews

### `add`
Adds a view to children. The placement of the child view will depend on the decorator, and the child's bounds. Normally you don't need to call this directly, since subviews call it automatically when you create them.**Arguments:**

| Argument | Description |
|----------|-------------|
| `child` |  |  


### `removeAll`
Removes all children from the view.

### Subclassing and Internal Methods
The following methods are usually not used directly or are called by a primitive. Programmers can still call or override these as needed.


### `init`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `argParent` |  |  
| `argBounds` |  |  


### `prRemoveChild`
Private method.**Arguments:**

| Argument | Description |
|----------|-------------|
| `child` |  |  


### `prClose`
Private method.


