# ParamView

*show a parameter of a JITLib process*

**Categories:** JITLib

**Related:** [JITGui](../Classes/JITGui.md), [Overviews/JITLib](../Overviews/JITLib.md)

## Description

ParamView displays a parameter value, and switches representation as appropriate for value: A single number is shown by an EZSlider, a pair of numbers by an EZRanger, and anything else as code on an EZText.
First examples:

```
w = Window("test", Rect(20, 820, 400, 100)).front;
w.addFlowLayout;
~pv = ParamView(w, Rect(20, 20, 360, 20));
~pv2 = ParamView(w, Rect(20, 20, 360, 40));

// not working properly yet
~pv.bounds_(Rect(4, 4, 300, 40));

~pv.dump
~pv.viewType_(0); // EZNumber
~pv.viewType_(1); // EZRanger
~pv.viewType_(2); // EZText

~pv.label_(\freq);
~pv.spec_(\freq);  // needs spec for EZSlider


~pv.value_(200);
~pv.value_(2000);
// switches to EZRanger
~pv.value_([200, 2000]);
// 3 numbers -> switches to EZText
~pv.value_([20, 200, 2000]);
// anything else -> EZText
~pv.value_(\blonk);
~pv.action = { |pv| pv.value.postcs };
```




## Class Methods


### `new`
create a new ParamView with**Arguments:**

| Argument | Description |
|----------|-------------|
| `parent` | the parent window or view |  
| `bounds` | the bounds of the view |  
| `label` | a label to display |  
| `spec` | a controlspec for the value |  
| `action` | an action to do when the value changes |  
| `initVal` | an initial value |  
| `initAction` | a boolean whether to perform the action on init. |  


## Instance Methods


### `label`
get and set the view's label
### `spec`
get and set the view's control spec
### `action`
get and set the paramview's action
### `ezviews`, `slider`, `ranger`, `textview`
the 3 ezviews between which the ParamView switches
### `currview`
the currently shown view of these
### `value`
get and set value
### `valueAction`
get and set value and do action
### `doAction`
do the view's action
### `viewType`
get and set the view's type: 0 is single number -> EZSlider, 1 is pair of numbers -> EZRanger, 2 is anything else
### `valueType`
determine viewType for a given value
### `background`
get and set background color

