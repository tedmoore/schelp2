# SCViewHolder

*Instead of subclassing a (Q/SC)View, this is a proxy/adapter object that holds the View*

**Categories:** GUI

**Related:** [View](../Classes/View.md)

## Description

When writing gui widgets it is sometimes not desirable to subclass a view class. Its preferable to write a class that acts like a View and is used where Views normally are used but isn't a direct subclass of a View class.
In the View hierarchy it is not possible to subclass an View class because under the hood there is always a strict relationship between the View subclass and its paired C++ class. The C++ class makes the actual view, the SC class is an interface to that C++ object.
In Qt there is a bit more flexibility.
But there are other reasons to not inherit from a specific view: your widget may not be a single view, in which case you would want to place a CompositeView and then place subviews inside of that. Altogether these views are what your widget manages. SCViewHolder can be used in this situation and it would set the top level CompositeView as its primary view.
Although it is still called "SC"ViewHolder it is in fact cross platform since it doesn't draw the view(s), it simply holds them.
Another possible name might be ViewAdapter or PseudoView. It was originally called SCViewAdapter.
Most of the standard view methods here simply defer to the proxied view. This makes the ViewHolder act and quack like a View.
Messages that are not understood by the view holder are forwarded to the proxied view.
Historical note: this class was originally in the cruciallib. ObjectGui is a subclass of this.


## Class Methods


### `consumeKeyDowns`
global preference variable: if true then subclasses that do not set a keyDownAction do NOT bubble up keyDown events by default.**Returns:** The result of calling the method on the proxied view

## Instance Methods


### `view`
get or set the view for which this object is a proxy/adapter.**Arguments:**

| Argument | Description |
|----------|-------------|
| `v` | the view: a [View](../Classes/View.md) |  
**Returns:** The result of calling the method on the proxied view
### `doesNotUnderstand`
Messages that are not understood by the view holder are forwarded to the proxied view. So when the interpreter is told to send a message to a view holder object and that message is not understood, it calls doesNotUnderstand**Arguments:**

| Argument | Description |
|----------|-------------|
| `selector` | The message that was not understood |  
| `... args` | The arguments that were supplied |  
**Returns:** the result of calling the method on the proxied view
### `viewDidClose`
Unsets the view variable. After the view is closed (removed from the window) then all calls to the view holder will fail, and should fail as there is no view anymore. You can check viewHolder.isClosed if you are unsure**Returns:** this
### `remove`
Removes the view from the window if it has not already been removed.**Returns:** this
### `action`
This method is forwarded to the view**Arguments:**

| Argument | Description |
|----------|-------------|
| `f` |  |  
**Returns:** The result of calling the method on the proxied view
### `doAction`
This method is forwarded to the view**Returns:** The result of calling the method on the proxied view
### `keyDownAction`
This method is forwarded to the view**Arguments:**

| Argument | Description |
|----------|-------------|
| `f` |  |  
**Returns:** The result of calling the method on the proxied view
### `keyDownResponder`
This method is forwarded to the view. Note: this is a cruciallib convention and will be deprecated here.**Returns:** The result of calling the method on the proxied view
### `enableKeyDowns`
This method is forwarded to the view. Note: this is a cruciallib convention and will be deprecated here.**Returns:** The result of calling the method on the proxied view
### `asView`
returns the view**Returns:** the view
### `bounds`
This method is forwarded to the view**Arguments:**

| Argument | Description |
|----------|-------------|
| `b` |  |  
**Returns:** The result of calling the method on the proxied view
### `resize`
This method is forwarded to the view**Arguments:**

| Argument | Description |
|----------|-------------|
| `r` |  |  
**Returns:** The result of calling the method on the proxied view
### `enabled`
This method is forwarded to the view**Arguments:**

| Argument | Description |
|----------|-------------|
| `b` |  |  
**Returns:** The result of calling the method on the proxied view
### `refresh`
This method is forwarded to the view**Returns:** The result of calling the method on the proxied view
### `background`
This method is forwarded to the view**Arguments:**

| Argument | Description |
|----------|-------------|
| `b` |  |  
**Returns:** The result of calling the method on the proxied view
### `focus`
This method is forwarded to the view**Arguments:**

| Argument | Description |
|----------|-------------|
| `flag` |  |  
**Returns:** The result of calling the method on the proxied view
### `visible`
This method is forwarded to the view**Arguments:**

| Argument | Description |
|----------|-------------|
| `boo` |  |  
**Returns:** The result of calling the method on the proxied view
### `isClosed`
This method is forwarded to the view**Returns:** The result of calling the method on the proxied view
### `font`
This method is forwarded to the view**Arguments:**

| Argument | Description |
|----------|-------------|
| `f` |  |  
**Returns:** The result of calling the method on the proxied view

