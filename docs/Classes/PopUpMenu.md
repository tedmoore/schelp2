# PopUpMenu

*A view displaying a text item selectable from a drop-down menu.*

**Categories:** GUI>Views

## Description

When clicked, this view opens a menu containing several text items, then closes the menu and displays one of the items after it is selected.


## Class Methods



## Instance Methods


### Data
### `items`
 The list of items displayed in a menu when the view is clicked.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Array of Strings or Symbols. |  

### `clear`
 Removes all items.
### `item`
 The currently selected item.**Returns:** A String.
### `value`
 The index of the currently selected item.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An integer, or nil meaning no selected item. |  

### `valueAction`
 Sets [value](#value) and triggers [action](#action).**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An integer, or nil meaning no selected item. |  


### Appearance
### `stringColor`
 The color used to display text.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  

### `background`
 Setting this variable colors the area of the view under the text with the given color.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  


### Interaction
### `allowsReselection`
 Determines whether the action is triggered when selecting already selected item. Defaults to false.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  


### Actions
### `action`
 The action object evaluated whenever the user changes the selected item from the menu. See [allowsReselection](#allowsreselection) for customization.

### Drag and drop
### `defaultGetDrag`
**Returns:** The [value](#value).
### `defaultCanReceiveDrag`
**Returns:** True if the current drag data is a number.
### `defaultReceiveDrag`
 Sets [valueAction](#valueaction) to the current drag data.

## Examples


### Basic Example

```supercollider
(
w = Window.new("The Eightfold Path").front;
m = PopUpMenu(w, Rect(10, 10, 180, 20));

m.items = [
 "right view", "right thinking", "right mindfulness", "right speech",
 "right action", "right diligence", "right concentration", "right livelihood"
];

m.background_(Color.green(0.7));  // only changes the look of displayed item
m.stringColor_(Color.white);   // only changes the look of displayed item
m.font_(Font("Courier", 13));   // only changes the look of displayed item
m.action = { |menu|
 [menu.value, menu.item].postln;
};
)

m.value;   // returns the index of the current item;
m.item;    // returns the String or Symbol of the current item

m.value_(2);  // changes the displayed item, but does not evaluate the action
m.valueAction_(3); // evaluates the action.
```




### Sound Example
Play different functions:


```supercollider
(
s.waitForBoot({
    var w, menu, snd, funcs, b;
    
    w = Window.new.front;
    menu = PopUpMenu(w, Rect(10, 10, 90, 20))
    .items_(["Sine", "Saw", "Noise", "Pulse"]);
    
    funcs = [
        { SinOsc.ar(440, 0, 0.3) },
        { Saw.ar(440, 0.3) },
        { WhiteNoise.ar(0.3) },
        { Pulse.ar(440, 0.2, 0.3) }
    ];
    
    b = Button(w, Rect(110, 10, 180, 20))
    .states_([["play", Color.black, Color.green]])
    .mouseDownAction_({
        snd = funcs.at(menu.value).play;
    })
    .action_({ |butt, mod|
        snd.release;
    });
    
    w.front;
    
    p = CmdPeriod.add({ b.value_(0) }); // set button to 0 on hitting Cmd-period
    w.onClose_{ snd.release; CmdPeriod.removeAll }; // clean up when window is closed
    
})
)
```






