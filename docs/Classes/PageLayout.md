# PageLayout

*a Window with a FlowView on it for use in ObjectGui's MVC model*

**Categories:** GUI

**Related:** [ObjectGui](../Classes/ObjectGui.md), [FlowView](../Classes/FlowView.md), [Window](../Classes/Window.md), [NotificationCenter](../Classes/NotificationCenter.md)

## Description

This class encapsulates the common task of creating a Window, adding a FlowView (CompositeView with a FlowLayout on it). It also supports the MVC model by registering controllers that are then removed (sent the .remove message) when the Window closes. Additionally it can resize itself to fit the contents.


## Class Methods

### `new`
Create a Window with a FlowView on it. The PageLayout object can be treated like a Window or like a View.**Arguments:**

| Argument | Description |
|----------|-------------|
| `title` | Window title |  
| `bounds` | Bounds or nil. Default of nil will size the window to the entire screen size. Use .resizeToFit to shrink the window to the content size. |  
| `margin` | FlowLayout margin. |  
| `background` | Background color |  
| `scroll` | boolean: add scroll bars or not. |  
| `front` | boolean: whether to immediately display the window, bringing it to the front. default is true. You may choose to first add your views to the window and then front it which is useful for large slow GUIs |  
**Returns:** a PageLayout

## Instance Methods

### `window`
the Window object**Returns:** a Window### `view`
the top most view on the Window**Returns:** a View### `isClosed`
boolean: has the window been closed ?**Returns:** boolean### `onClose`
Just as for Window, this method is called when the PageLayout's window is closed. The actual Window's onClose method is used to trigger clean up operations, releasing dependencies and will also call this onClose function.**Returns:** get/set onClose handler### `asView`
returns the top view**Returns:** a View### `asFlowView`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bounds` | if bounds are nil then it returns self, as a PageLayout is compatible with FlowView. If bounds are supplied then a child FlowView is placed and returned |  
**Returns:** self or a new FlowView### `bounds`
inner bounds of the top level view.**Returns:** a Rect### `asPageLayout`
Similar to asFlowView, this message converts nil and various other objects to a PageLayout. This is already a PageLayout, so it returns self.**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` | Ignored. If the receiver had been nil then the name would be the Window name. |  
| `bounds` | Ignored. Would have been used to size the PageLayout |  
**Returns:** self### `startRow`
compatible with FlowView**Returns:** self### `indentedRemaining`
compatible with FlowView**Returns:** self### `checkNotClosed`
isClosed.not**Returns:** boolean### `front`
bring Window to the front**Returns:** self### `hide`
Hide window**Returns:** self### `show`
Show the window if it was previously hidden.**Returns:** self### `close`
Close the window, releasing any dependencies and calling the onClose handler.**Returns:** self### `refresh`
Refresh the top level view**Returns:** self### `background`
set background color of top level view**Arguments:**

| Argument | Description |
|----------|-------------|
| `c` | color |  
**Returns:** self### `removeOnClose`
Register an object, usually a ObjectGui subclass or an Updater so that when the Window closes the .remove message will be sent to it. This will cause the object to release its dependencies on its Model. This means the ObjectGui (or other controller object) will stop getting update messages and will stop trying to update the View which has just been closed along with the Window. It also means that if there is no link to the Model and no longer any Views that held links to the controller object, that the controller is now unreferenced and will be garbage collected.**Arguments:**

| Argument | Description |
|----------|-------------|
| `dependant` | the object that wishes to be sent .remove on closing the window |  
**Returns:** self### `resizeToFit`
Resize the top FlowView to fit its contents and then resize the Window to fit that.**Arguments:**

| Argument | Description |
|----------|-------------|
| `reflow` | boolean: FlowView can relay all of its child views in cases where the bounds have changed or views have been removed. This puts them all back in place one by one for the updated bounds. So this may result in smaller over all bounds, after which the window is shrunk. |  
| `center` | boolean: after resizing, re-center the window in the screen. |  
**Returns:** self### `reflowAll`
see FlowView reflowAll**Returns:** self### `fullScreen`
go Full screen**Returns:** self### `endFullScreen`
end full screen**Returns:** self
### FlowView extensions
### `flow`
Place a new FlowView on the window**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | A handler that recieves the new FlowView as argument |  
| `bounds` | Bounds of the FlowView |  
**Returns:** (returnvalue)
### `vert`
(describe method here)**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | (describe argument here) |  
| `bounds` | (describe argument here) |  
| `spacing` | (describe argument here) |  
**Returns:** (returnvalue)
### `horz`
(describe method here)**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | (describe argument here) |  
| `bounds` | (describe argument here) |  
| `spacing` | (describe argument here) |  
**Returns:** (returnvalue)
### `comp`
(describe method here)**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | (describe argument here) |  
| `bounds` | (describe argument here) |  
**Returns:** (returnvalue)
### `scroll`
(describe method here)**Arguments:**

| Argument | Description |
|----------|-------------|
| `... args` | (describe argument here) |  
**Returns:** (returnvalue)

## Examples


```supercollider
PageLayout.new
```




