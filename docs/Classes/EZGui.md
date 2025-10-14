# EZGui

*An abstract superclass for EZ widget wrappers*

**Categories:** GUI>EZ-GUI

**Related:** [EZListView](../Classes/EZListView.md), [EZPopUpMenu](../Classes/EZPopUpMenu.md), [EZSlider](../Classes/EZSlider.md), [EZNumber](../Classes/EZNumber.md), [EZRanger](../Classes/EZRanger.md), [EZKnob](../Classes/EZKnob.md)

## Description

Users will not normally directly create instances of EZGui, but only use it through its subclasses. It provides the basic mechanisms for various EZ widget wrappers. It also provides a standard for EZ GUI Classes, and new EZ Classes should subclass EZGUI to help keep a consistent user interface.


## Instance Methods


### Accessing Instance Variables
### `view`
Returns the enclosing [CompositeView](../Classes/CompositeView.md).
### `bounds`
Returns the bounds of the enclosing [CompositeView](../Classes/CompositeView.md).
### `label`
Sets/gets it the label. Will add the label view if none was initially created.**Arguments:**

| Argument | Description |
|----------|-------------|
| `string` | An Instance of [String](../Classes/String.md). |  

### `window`
Returns the window if you used the popUp window function.

### Accessing GUI options
### `alwaysOnTop`
Makes the popup window always on top, if there is one.**Arguments:**

| Argument | Description |
|----------|-------------|
| `bool` | An Instance of [Boolean](../Classes/Boolean.md). Default is false. |  

### `visible`
Sets/gets it the component views are visible.**Arguments:**

| Argument | Description |
|----------|-------------|
| `bool` | An Instance of [Boolean](../Classes/Boolean.md). Default is true. |  

### `enabled`
Sets/gets if the list is enabled.**Arguments:**

| Argument | Description |
|----------|-------------|
| `bool` | An Instance of [Boolean](../Classes/Boolean.md). Default is true. |  

### `onClose`
Sets/gets the onClose function of either `view` or `window`, depending on whether the EZ view used a popup window.**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | An Instance of [Function](../Classes/Function.md) or [FunctionList](../Classes/FunctionList.md). |  

### `font`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `font` | An instance of [Font](../Classes/Font.md). |  


### Subclassing
EZGui provides a standard and basic tools for most EZ classes. If you make a new EZ class, then subclass EZGui, and override the necessary methods. If your class only has a label and a widget, chances are, you need to override nothing, but only need to write the new and init class methods. See existing subclasses of EZGui for examples of this. You may also want to override the following:

### `widget`
Returns the active widget. Subclasses will typically refer to it or ignore it, e.g.:
```supercollider
MyEZClass{
    myOtherMethods{ }
    ....
    listView{ ^widget }
}
```


### `action`
Gets/sets the action of the EZ class instance.**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | An Instance of [Function](../Classes/Function.md) or [FunctionList](../Classes/FunctionList.md). |  

### `value`
Gets/sets the value of the `widget`. Does not perform the action.**Arguments:**

| Argument | Description |
|----------|-------------|
| `val` | An integer. |  

### `valueAction`
Gets/sets the value of the widget. Performs do action.**Arguments:**

| Argument | Description |
|----------|-------------|
| `val` | An integer. |  

### `doAction`
Performs `this.action.value(this)`.

### Internal Utilities
### `prSubViewBounds`
This calculates the bounds of the subviews and the gaps. It returns an array of Rects, which depends on how many subview there are. Subclasses override this if they have more than one widget.
### `prMakeView`
Called by init. Returns `[view, bounds]`. The container is either the enclosing Container, or a pop up window with a container.
### `prSetViewParams`
Only defined by some subclasses. Sets the `resize` and `align` of all the views, according to the state of `layout`.
### `prMakeMarginGap`
Called in the init method of all subclasses. Sets the margin and gap of `view`. By default, it tries to get its parent's gap, otherwise it defaults to `2@2`. Setting `argGap` overrides these.


