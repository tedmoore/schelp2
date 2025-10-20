# EZKnob

*Wrapper class for label, knob, number box*

**Categories:** GUI>EZ-GUI

**Related:** [Knob](../Classes/Knob.md), [NumberBox](../Classes/NumberBox.md), [StaticText](../Classes/StaticText.md), [CompositeView](../Classes/CompositeView.md), [EZGui](../Classes/EZGui.md)

## Description

EZKnob is wrapper class which creates an (optional) [StaticText](../Classes/StaticText.md), and a [Knob](../Classes/Knob.md) plus a [NumberBox](../Classes/NumberBox.md). If the parent is nil, then EZKnob will create its own window. See [EZGui](../Classes/EZGui.md) more options.

### Some Important Issues Regarding NumberBox
> **⚠️ Warning:** EZKnob replaces the EZKnob Quark, which is now called EZKnobOld. It is encouraged to update your code. The two classes have different creation methods and approaches, particularly concerning the **dimensions** (now **bounds**). To make the conversion process easier, EZKnobOld has an instance method called convert which will post the equivalent creation code for the new EZKnob.

> **Note:** Bounds: Make certain to choose bounds that are large enough to encompass the knob, the number box, and the label (if you use one), otherwise you may get confusing results. See the examples below.





## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `parent` | The parent view or window. If the parent is nil, then EZKnob will create its own [Window](../Classes/Window.md), and place it conveniently on the screen if the bounds are a [Point](../Classes/Point.md). If the bounds are a [Rect](../Classes/Rect.md), then the [Rect](../Classes/Rect.md) determines the window bounds. |  
| `bounds` | An instance of [Rect](../Classes/Rect.md) or [Point](../Classes/Point.md). Default value is `160@20`. Make certain to choose bounds that are large enough to encompass the knob, the number box, and the label (if you use one), otherwise you may get confusing results. See the examples below. |  
| `label` | The label. Default value is nil. If nil, then no [StaticText](../Classes/StaticText.md) is created. |  
| `controlSpec` | The [ControlSpec](../Classes/ControlSpec.md) for scaling the value. If the `minVal + maxVal` of the spec is 0, then `centered` will be set to true automatically. |  
| `action` | A [Function](../Classes/Function.md) called when the value changes. The function is passed the EZKnob instance as its argument. |  
| `initVal` | The value to initialize the knob and number box with. If nil, then it uses the [ControlSpec](../Classes/ControlSpec.md)'s default value. |  
| `initAction` | A [Boolean](../Classes/Boolean.md) indicating whether the action function should be called when setting the initial value. The default is false. |  
| `labelWidth` | Number of pixels width for the label. default is 60. This is only valid for the `\horz` layout. |  
| `knobSize` | An instance of [Point](../Classes/Point.md). It will adjust itself to maximize the space use of `width/height`. By default, it uses the maximum available height, and adjusts the width accordingly. |  
| `unitWidth` | Number of pixels width for the unit label. Default is 0. If 0, then no unitLabel is created. |  
| `labelHeight` | Default is 20. |  
| `layout` | `\vert`, `vert2`, `\line2`, or `\horz`. default is `\vert`. |  
| `gap` | A [Point](../Classes/Point.md). By default, the view tries to get its parent's gap, otherwise it defaults to `2@2`. Setting it overrides these. |  
| `margin` | A [Point](../Classes/Point.md). This will inset the bounds occupied by the subviews of view. |  

```
(
w = Window.new.front;
g = EZKnob(w,        // parent
            50@90,    // bounds
            " test ", // label
            \freq,    // controlSpec
            { |ez| (ez.value.asString ++" is the value of " ++ ez).postln } // action
);
g.setColors(Color.grey, Color.white)
);

// Simplest version, no parent view, so a window is created
(
    g = EZKnob(label:" test ");
    g.action_({ |ez| (ez.value.asString ++" is the value of " ++ ez).postln });
);
```

The contained views can be accessed via the EZKnob instance variables: `labelView`, `knobView`, `numberView`.

## Instance Methods


### Accessing Instance Variables

### `numberView`
**Returns:** the `numberView`

### `knobView`
**Returns:** the `knobView`

### `labelView`
Set/get the `labelView`

### `action`
A function to be evaluated when the value changes. Te first argument will be the EZKnob.**Arguments:**

| Argument | Description |
|----------|-------------|
| `arg1` | An instance of [Function](../Classes/Function.md) or [FunctionList](../Classes/FunctionList.md). Default value is `nil`. |  


### `value`
The value of the knob

### `centered`
Sets/gets whether the knob is in centered mode. See [Knob](../Classes/Knob.md).

### `round`
Rounds the values in the number box.

### `controlSpec`
An instance of [ControlSpec](../Classes/ControlSpec.md) for scaling the values.

### `value`
Gets/sets the list/menu to the index at value. Does not perform the action.**Arguments:**

| Argument | Description |
|----------|-------------|
| `val` | An [Integer](../Classes/Integer.md). |  


### `doAction`
Performs the action at the current index and the global action.

### `set`
Set the args after creation. You can only set the label if it was not nil from the beginning.

### `visible`
Sets/gets if the component views are visible.**Arguments:**

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
| `numBackground` | An instance of [Color](../Classes/Color.md). The `numColor` of the number view. |  
| `numStringColor` | An instance of [Color](../Classes/Color.md). The `stringColor` of the number view. |  
| `numNormalColor` | An instance of [Color](../Classes/Color.md). The `normalColor` of the number view. |  
| `numTypingColor` | An instance of [Color](../Classes/Color.md). The `typingColor` of the number view. |  
| `knobColors` | An instance of [Color](../Classes/Color.md). The `knobColors` of the knob view. |  
| `background` | An instance of [Color](../Classes/Color.md). The `background` of the enclosing view. |  


### `font`
Set the Font used by all the views.**Arguments:**

| Argument | Description |
|----------|-------------|
| `font` | An instance of [Font](../Classes/Font.md). |  


## Examples


```
(    // basic use
    w = Window.new.front;
    g = EZKnob(w, 50@90, " test  ", \freq, { |a| a.value.postln });
    g.setColors(Color.grey, Color.white);
);


// lots of knobs on on view
(
w = Window.new.front;
w.view.decorator = FlowLayout(w.view.bounds);
w.view.decorator.gap = 2@2;

20.do{
    EZKnob(w, 180@24, " Freq ", \freq, unitWidth: 30, initVal: 6000.rand, layout: \horz)
    .setColors(Color.grey, Color.white)
    .font_(Font("Helvetica", 11));

};
);

Window.closeAll  // use this to close all the windows

/////////////////////////////////////////////////////////////////
////////// click these parentheses to see all features and layouts

(
m = nil;
m = 2@2;        // comment this for no margin

/////////////////
/// Layout \line2

(        // all features, small font
        g = EZKnob(nil, 128@40, " freq  ", \freq, unitWidth: 20, layout: \line2, margin: m);
        g.setColors(Color.grey, Color.white, Color.grey,
            Color.white, Color.yellow, nil, nil, Color.grey(0.7));
        g.window.bounds = g.window.bounds.moveBy(-180, 50);
        g.font_(Font("Helvetica", 10));
);

(        // no unitView
        g = EZKnob(nil, 118@40, " freq  ", \freq, unitWidth: 0, layout: \line2, margin: m);
        g.setColors(Color.grey, Color.white, Color.grey,
            Color.white, Color.yellow, nil, nil, Color.grey(0.7));
        g.window.bounds = g.window.bounds.moveBy(-180, -40);
);
(        // no label, so use window name as label
        g = EZKnob(nil, 118@30, nil, \freq, labelWidth: 100, unitWidth: 20, layout: \line2, margin: m);
        g.setColors(Color.grey, Color.white, Color.grey,
            Color.white, Color.yellow, nil, nil, Color.grey(0.7));
        g.window.bounds = g.window.bounds.moveBy(-180, -130);
        g.window.name = "Freq";
);

/////////////////
/// Layout \horz


(        // all features
        g = EZKnob(nil, 200@28, " freq  ", \freq, unitWidth: 30, layout: \horz, margin: m);
        g.setColors(Color.grey, Color.white, Color.grey,
            Color.white, Color.yellow, nil, nil, Color.grey(0.7));
        g.window.bounds = g.window.bounds.moveBy(0, 50);
);

(        // no unitView
        g = EZKnob(nil, 160@28, " freq  ", \freq, layout: \horz, margin: m);
        g.setColors(Color.grey, Color.white, Color.grey,
            Color.white, Color.yellow, nil, nil, Color.grey(0.7));
        g.window.bounds = g.window.bounds.moveBy(0, -30);
);
(        // no label, so use window name as label
        g = EZKnob(nil, 120@28, nil, \freq, layout: \horz, margin: m);
        g.setColors(Color.grey, Color.white, Color.grey,
            Color.white, Color.yellow, nil, nil, Color.grey(0.7));
        g.window.bounds = g.window.bounds.moveBy(0, -110);
        g.window.name = "Freq";
);



/////////////////
/// Layout \vert

(        // all features
        g = EZKnob(nil, 82@82, " freq  ", \freq, unitWidth: 18, layout: \vert, margin: m);
        g.setColors(Color.grey, Color.white, Color.grey,
            Color.white, Color.yellow, nil, nil, Color.grey(0.7));
        g.font_(Font("Helvetica", 10));
        g.window.bounds = g.window.bounds.moveBy(220, 50);
);

(        // no unitView, with label
        g = EZKnob(nil, 70@90, " freq  ", \freq, unitWidth: 0, layout: \vert, margin: m);
        g.setColors(Color.grey, Color.white, Color.grey,
            Color.white, Color.yellow, nil, nil, Color.grey(0.7));
        g.window.bounds = g.window.bounds.moveBy(220, -90);
);

(        // no label
        g = EZKnob(nil, 120@60, nil, \freq, unitWidth: 30, layout: \vert, margin: m);
        g.setColors(Color.grey, Color.white, Color.grey,
            Color.white, Color.yellow, nil, nil, Color.grey(0.7));
        g.window.bounds = g.window.bounds.moveBy(220, -230);
        g.window.name = "Freq";
);

(        // no lablel, so use window name as label
        g = EZKnob(nil, 120@60, nil, \freq, unitWidth: 0, layout: \vert, margin: m);
        g.setColors(Color.grey, Color.white, Color.grey,
            Color.white, Color.yellow, nil, nil, Color.grey(0.7));
        g.window.bounds = g.window.bounds.moveBy(220, -340);
        g.window.name = "Freq";
);


/////////////////
/// Layout \vert2

(        // all features
        g = EZKnob(nil, 82@82, " freq  ", \freq, unitWidth: 18, layout: \vert2, margin: m);
        g.setColors(Color.grey, Color.white, Color.grey,
            Color.white, Color.yellow, nil, nil, Color.grey(0.7));
        g.font_(Font("Helvetica", 10));
        g.window.bounds = g.window.bounds.moveBy(350, 50);
);

(        // no unitView, with label
        g = EZKnob(nil, 70@90, " freq  ", \freq, unitWidth: 0, layout: \vert2, margin: m);
        g.setColors(Color.grey, Color.white, Color.grey,
            Color.white, Color.yellow, nil, nil, Color.grey(0.7));
        g.window.bounds = g.window.bounds.moveBy(350, -90);
);

(        // no label
        g = EZKnob(nil, 120@60, nil, \freq, unitWidth: 30, layout: \vert2, margin: m);
        g.setColors(Color.grey, Color.white, Color.grey,
            Color.white, Color.yellow, nil, nil, Color.grey(0.7));
        g.window.bounds = g.window.bounds.moveBy(350, -230);
        g.window.name = "Freq";
);

(        // no lablel, so use window name as label
        g = EZKnob(nil, 120@60, nil, \freq, unitWidth: 0, layout: \vert2, margin: m);
        g.setColors(Color.grey, Color.white, Color.grey,
            Color.white, Color.yellow, nil, nil, Color.grey(0.7));
        g.window.bounds = g.window.bounds.moveBy(350, -340);
        g.window.name = "Freq";
);


)




///////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////


// Sound example
(
// start server
s.waitForBoot({

var w, startButton, noteControl, cutoffControl, resonControl;
var balanceControl, ampControl;
var node, cmdPeriodFunc;

// define a synth
SynthDef("window-test", { |out, note = 36, fc = 1000, rq = 0.25, bal = 0, amp = 0.4, gate = 1|
        var x;
        x = Mix.fill(4, {
            LFSaw.ar((note + { 0.1.rand2 }.dup).midicps, 0, 0.02)
        });
        x = RLPF.ar(x, fc, rq).softclip;
        x = RLPF.ar(x, fc, rq, amp).softclip;
        x = Balance2.ar(x[0], x[1], bal);
        x = x * EnvGen.kr(Env.cutoff, gate, doneAction: Done.freeSelf);
        Out.ar(out, x);
    }, [0.1, 0.1, 0.1, 0.1, 0.1, 0]
).add;




// make the window
w = Window("another control panel", Rect(20, 400, 230, 250));
w.front; // make window visible and front window.
w.view.decorator = FlowLayout(w.view.bounds);
w.view.decorator.gap = 2@2;

// add a button to start and stop the sound.
startButton = Button(w, 75 @ 20);
startButton.states = [
    ["Start", Color.black, Color.green(0.7)],
    ["Stop", Color.white, Color.red(0.7)]
];
startButton.action = { |view|
        if (view.value == 1) {
            // start sound
            node = Synth("window-test", [
                "note", noteControl.value,
                "fc", cutoffControl.value,
                "rq", resonControl.value,
                "bal", balanceControl.value,
                "amp", ampControl.value.dbamp]);
        } {
            // set gate to zero to cause envelope to release
            node.release; node = nil;
        };
};

// create controls for all parameters
w.view.decorator.nextLine;
noteControl = EZKnob(w, 220 @ 32, "Note ", ControlSpec(24, 60, \lin, 1, 36, \note),
    { |ez| node.set("note", ez.value) }, unitWidth: 30, layout: \horz)
        .setColors(Color.grey, Color.white, Color.grey(0.7), Color.grey, Color.white, Color.yellow);

w.view.decorator.nextLine;
cutoffControl = EZKnob(w, 220 @ 32, "Cutoff ", ControlSpec(200, 5000, \exp, 0.01, 1000, \Hz),
    { |ez| node.set("fc", ez.value) }, unitWidth: 30, layout: \horz)
        .setColors(Color.grey, Color.white, Color.grey(0.7), Color.grey, Color.white, Color.yellow);

w.view.decorator.nextLine;
resonControl = EZKnob(w, 220 @ 32, "Reson ", ControlSpec(0.1, 0.7, \lin, 0.001, 0.2, \rq),
    { |ez| node.set("rq", ez.value) }, unitWidth: 30, layout: \horz)
        .setColors(Color.grey, Color.white, Color.grey(0.7), Color.grey, Color.white, Color.yellow);

w.view.decorator.nextLine;
balanceControl = EZKnob(w, 220 @ 32, "Balance ", \bipolar,
    { |ez| node.set("bal", ez.value) }, unitWidth: 30, layout: \horz)
        .setColors(Color.grey, Color.white, Color.grey(0.7), Color.grey, Color.white, Color.yellow);

w.view.decorator.nextLine;
ampControl = EZKnob(w, 220 @ 32, "Amp ", \db,
    { |ez| node.set("amp", ez.value.dbamp) }, -6, unitWidth: 30, layout: \horz)
        .setColors(Color.grey, Color.white, Color.grey(0.7), Color.grey, Color.white, Color.yellow);


// set start button to zero upon a cmd-period
cmdPeriodFunc = { startButton.value = 0 };
CmdPeriod.add(cmdPeriodFunc);

// stop the sound when window closes and remove cmdPeriodFunc.
w.onClose = {
    node.free; node = nil;
    CmdPeriod.remove(cmdPeriodFunc);
};
});
)


//////////////////////////////
// more examples
// these mimick the original  EZKnob layout and colors

(
w = Window("EZKnob", Rect(380, 400, 300, 180)).front;
w.view.decorator = FlowLayout(w.view.bounds);
k = EZKnob(w, 42 @ 74, "Knob", action: { |knb| knb.value.postln }, margin: 2@2, labelHeight: 16);
k.view.background_(Color.grey.alpha_(0.4));
)
k.centered_(true)
k.value = 0.5;
k.visible_(false)
k.visible_(true)

k.enabled_(false)
k.value = 0.1
k.enabled
k.enabled_(true)
k.value = 0.25

(
w = Window("EZKnob", Rect(380, 400, 300, 180)).front;
w.view.decorator = FlowLayout(w.view.bounds, gap: 1@1);
StaticText(w, (42 * 4 + 3) @ 16).string_("EZKnob Cluster").background_(Color.blue(0.1, 0.1));
w.view.decorator.nextLine;
a = [
        EZKnob(w, 42 @ 74, "knob 1", margin: 2@2, labelHeight: 16),
        EZKnob(w, 42 @ 74, "knob 2", controlSpec: \freq, margin: 2@2, labelHeight: 16),
        EZKnob(w, 42 @ 74, "knob 3", controlSpec: \pan, margin: 2@2, labelHeight: 16).round_(0.001),
        EZKnob(w, 42 @ 74, "knob 4", controlSpec: \rq, margin: 2@2, labelHeight: 16)
    ];
a.do{ |a|a.view.background_(Color.grey.alpha_(0.4)) };
)
// a now holds the array of knobs
a
a[0].value
a[3].value_(0.5)
a.collect(_.value);
```




