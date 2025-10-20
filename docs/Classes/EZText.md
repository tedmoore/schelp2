# EZText

*Wrapper class for a label, a text field and a value*

**Categories:** GUI>EZ-GUI

**Related:** [StaticText](../Classes/StaticText.md), [TextField](../Classes/TextField.md)

## Description

EZText is a wrapper class which creates an (optional) [StaticText](../Classes/StaticText.md), and a [TextField](../Classes/TextField.md). The value is displayed as a compileString in the text field for editing.

### Some Important Issues Regarding EZText
If the parent is `nil`, then EZText will create its own [Window](../Classes/Window.md). See [EZGui](../Classes/EZGui.md) for more options.




## Class Methods


### Creation / Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `parent` | The parent view or window. If the parent is nil, then EZText will create its own [Window](../Classes/Window.md), and place it conveniently on the screen if the bounds are a [Point](../Classes/Point.md). If the bounds are a [Rect](../Classes/Rect.md), then the [Rect](../Classes/Rect.md) determines the window bounds. |  
| `bounds` | An instance of [Rect](../Classes/Rect.md) or [Point](../Classes/Point.md). Default value is `160@20`. |  
| `label` | The label. Default value is `nil`. If `nil`, then no [StaticText](../Classes/StaticText.md) is created. |  
| `action` | A [Function](../Classes/Function.md) called when the value changes. The function is passed the EZText instance as its argument. |  
| `initVal` | The value to initialize the EZText with. |  
| `initAction` | A [Boolean](../Classes/Boolean.md) indicating whether the action function should be called when setting the initial value. The default is false. |  
| `labelWidth` | Number of pixels width for the label. The default is 60. In the `\horz` layout, if you specify the `textWidth`, then the `labelWidth` is ignored and is set to the `bounds.width - textWidth`. |  
| `textWidth` | Number of pixels width for the number box. The default is 45. In `\vert` layout, `textWidth` defaults to the `bounds.width`. |  
| `labelHeight` | Default is 20. |  
| `layout` | `\vert`, or `\horz`. The default is `\horz`; `\vert` is a two line version. |  
| `gap` | A [Point](../Classes/Point.md). By default, the view tries to get its parent's gap, otherwise it defaults to `2@2`. Setting it overrides these. |  
| `margin` | A [Point](../Classes/Point.md). This will inset the bounds occupied by the subviews of view. |  
Example:
```
(
w = Window("EZText", Rect(300, 300, 260, 60)).front;
g = EZText(w,          // parent
            250@50,     // bounds
            "testing",  // label
            { |ez| (ez.value.asString ++" is the value of " ++ ez).postln }, // action
            [1, 2, 3],  // initValue
            true        // initAction
);
g.setColors(Color.grey, Color.white);
);

// Simplest version, no parent view, so a window is created
(
    g = EZText(label:" test ");
    g.action_({ |ez| (ez.value.asString ++" is the value of " ++ ez).postln });
);

(
    g = EZText(bounds: Rect(100, 200, 150, 50), label:" test ", layout: \vert);
    g.action_({ |ez| (ez.value.asString ++" is the value of " ++ ez).postln });
);
```

The contained views can be accessed via the EZText instance variables: `labelView`, `textField`.


## Instance Methods


### `textField`
Returns the textField.
### `action`
A [Function](../Classes/Function.md) to be evaluated when the value changes. Typical use is to type in a new value, and interpret it by hitting the evaluation shortcut. The first argument to the function will be the EZText.
### `value`
Gets/sets the value of the ezText. Does not perform the action.**Arguments:**

| Argument | Description |
|----------|-------------|
| `inval` | Any object. |  

### `valueAction`
Sets the value and performs the action.**Arguments:**

| Argument | Description |
|----------|-------------|
| `val` | Any object. |  

### `doAction`
Performs the action.
### `enabled`
Sets/gets whether the textfield is enabled.**Arguments:**

| Argument | Description |
|----------|-------------|
| `bool` | An instance of [Boolean](../Classes/Boolean.md). Default is `true`. |  

### Changing Appearance

### `setColors`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `stringBackground` | An instance of [Color](../Classes/Color.md). The `background` of the label and unit views. |  
| `stringColor` | An instance of [Color](../Classes/Color.md). The `stringColor` of the label and unit views. |  
| `textBackground` | An instance of [Color](../Classes/Color.md). The `background` of the textField. |  
| `textStringColor` | An instance of [Color](../Classes/Color.md). The `stringColor` of the textField. |  
| `textNormalColor` | An instance of [Color](../Classes/Color.md). The `normalColor` of the textField. |  
| `textTypingColor` | An instance of [Color](../Classes/Color.md). The `typingColor` of the textField. |  
| `background` | An instance of [Color](../Classes/Color.md). The `background` of the enclosing view. |  


### `font`
Set the Font used by all the views.**Arguments:**

| Argument | Description |
|----------|-------------|
| `font` | An instance of [Font](../Classes/Font.md). |  


## Examples


```
// Simplest version
(        // basic use
        w = Window("ez", Rect(300, 300, 300, 50)).front;
        g = EZText(w, 290@40, " test  ", textWidth: 220, layout: \horz);
        g.setColors(Color.grey, Color.white);
);


// lots of textFields on one window
(
w = Window.new.front;
w.view.decorator = FlowLayout(w.view.bounds);
w.view.decorator.gap = 2@2;

40.do{
        g = EZText(w, 170@16, " test  ", textWidth: 120, layout: \horz);
        g.setColors(Color.grey, Color.white, Color.grey(0.8));
};
);


// click these parentheses to see three variants
(

m = nil;
m = 2@2;        // comment for no margin

/////////////////
/// Layout \horz

(        // with label
        g = EZText(nil, 170@20, " freq  ", textWidth: 120, layout: \horz, margin: m);
        g.setColors(Color.grey, Color.white, background: Color.grey(0.7));
        g.window.bounds = g.window.bounds.moveBy(-180, 50);
);

(        // no label. use window name as label
        g = EZText(nil, 120@20, layout: \horz, margin: m);
        g.setColors(Color.grey, Color.white, background: Color.grey(0.7));
        g.window.bounds = g.window.bounds.moveBy(-180, -90);
        g.window.name = "Freq";
);

/////////////////
/// Layout \vert

(        // all features
        g = EZText(nil, 120@60, " freq  ", textWidth: 120, layout: \vert, margin: m);
        g.setColors(Color.grey, Color.white, background: Color.grey(0.7));
        g.window.bounds = g.window.bounds.moveBy(100, 50);
);

)



// Simplest sound example
(
Tdef(\text).set(\note, [0, 2, 7], \dur, { [0.1, 0.2].choose });

w = Window("EZTexts", Rect(200, 400, 304, 120)).front;
w.addFlowLayout;

TdefGui(Tdef(\text), 0, w);
Tdef(\text).envir.keysValuesDo { |k, v|
    EZText(w, Rect(0, 0, 300, 40), k, { |ez|
        Tdef(\text).envir.put(*[k, ez.value].postcs);
    }, v);
};

Tdef(\text, { |ev|
    var mydur;
    loop {
        mydur = ev.dur;
        (note: ev.note, dur: mydur).postln.play;
        mydur.wait;
    }
}).play;
)

// type these or similar functions into dur and note fields and evaluate:

{ [0.1, 0.2, 0.3].choose }
{ [0, 2, 7, 10].scramble.keep(rrand(0, 4)) }
```




