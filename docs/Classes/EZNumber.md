# EZNumber

*Wrapper class for label and number box*

**Categories:** GUI>EZ-GUI

**Related:** [NumberBox](../Classes/NumberBox.md)

## Description

EZNumber is wrapper class which creates an (optional) [StaticText](../Classes/StaticText.md), and a [NumberBox](../Classes/NumberBox.md).

### Some Important Issues Regarding NumberBox
If the parent is `nil`, then EZNumber will create its own window. See [EZGui](../Classes/EZGui.md) more options.



### Scrolling and Arrow Keys
EZNumber scrolls by default, using the step size of the [ControlSpec](../Classes/ControlSpec.md). If the controlSpec's step is set to 0, or is not set, then the stepping and scrolling will be guessed according to the `minval` and `maxval` values of the spec on creation of the view. Unlike the step variable of a regular [NumberBox](../Classes/NumberBox.md), `controlSpec.step` is also the smallest possible increment for the EZNumber. By default, the shift-key modifier will allow you to step by 100 x `controlSpec.step`, while the ctrl-key will give you 10x `controlSpec.step`. Since the alt-key would give you 0.1 of the minimum step, it is disabled by default, but you can change that by setting `numberView.alt_step` to any value you like. Accordingly you can customize the other modifiers to fit your needs. See [NumberBox](../Classes/NumberBox.md).




## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `parent` | The parent view or window. If the parent is nil, then EZNumber will create its own [Window](../Classes/Window.md), and place it conveniently on the screen if the bounds are a [Point](../Classes/Point.md). If the bounds are a [Rect](../Classes/Rect.md), then the [Rect](../Classes/Rect.md) determines the window bounds. |  
| `bounds` | An instance of [Rect](../Classes/Rect.md) or [Point](../Classes/Point.md). Default value is `160@20`. |  
| `label` | The label. Default value is `nil`. If `nil`, then no [StaticText](../Classes/StaticText.md) is created. |  
| `controlSpec` | The [ControlSpec](../Classes/ControlSpec.md) for scaling the value. |  
| `action` | A [Function](../Classes/Function.md) called when the value changes. The function is passed the EZNumber instance as its argument. |  
| `initVal` | The value to initialize the slider and number box with. If `nil`, then it uses the [ControlSpec](../Classes/ControlSpec.md)'s default value. |  
| `initAction` | A [Boolean](../Classes/Boolean.md) indicating whether the action function should be called when setting the initial value. The default is `false`. |  
| `labelWidth` | Number of pixels width for the label. The default is 60. In the `\horz` layout, if you specify the `numberWidth`, then the `labelWidth` is ignored and is set to the `bounds.width - unitWidth - numberWidth`. |  
| `numberWidth` | Number of pixels width for the number box. The default is 45. In \line2 layout, numberWidth defaults to the bounds.width minus the unitWidth. |  
| `unitWidth` | Number of pixels width for the unit label. The default is 0. If `unitWidth` is 0, then no `unitLabel` is created. In the `\line2` layout, if you specify the `numberWidth`, then the `unitWidth` is ignored and is set to the `bounds.width - unitWidth - numberWidth`. |  
| `labelHeight` | Default is 20; |  
| `layout` | `\line2`, or `\horz`. The default is `\horz`; `\line2` is a two line version. |  
| `gap` | A [Point](../Classes/Point.md). By default, the view tries to get its parent's gap, otherwise it defaults to `2@2`. Setting it overrides these. |  
| `margin` | A [Point](../Classes/Point.md). This will inset the bounds occupied by the subviews of view. |  

```supercollider
(
w = Window.new.front;
g = EZNumber(w,        // parent
             150@20,   // bounds
             " test ", // label
             \freq,    // controlSpec
             { |ez| (ez.value.asString ++" is the value of " ++ ez).postln }, // action
             330,      // initValue
             true      // initAction
);
g.setColors(Color.grey, Color.white);
);


// Simplest version, no parent view, so a window is created
(
    g = EZNumber(label:" test ", controlSpec: \amp.asSpec.step_(0.01));
    g.action_({ |ez| (ez.value.asString ++" is the value of " ++ ez).postln });
);
```

The contained views can be accessed via the EZNumber instance variables: `labelView`, `numberView`.

## Instance Methods

### `numberView`
Returns the numberView### `action`
A function to be evaluated when the value changes. Te first argument will be the EZNumber.**Arguments:**

| Argument | Description |
|----------|-------------|
| `arg1` | An instance of [Function](../Classes/Function.md) or [FunctionList](../Classes/FunctionList.md). Default value is nil. |  
### `value`
The value of the slider### `round`
Rounds the values in the number box.### `controlSpec`
An instance of [ControlSpec](../Classes/ControlSpec.md) for scaling the values.### `value`
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
Performs the action at the current index and the global action.### `set`
Set the args after creation.### `enabled`
Sets/gets if the list is enabled.**Arguments:**

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
| `numBackground` | An instance of [Color](../Classes/Color.md). The `background` of the number view. |  
| `numStringColor` | An instance of [Color](../Classes/Color.md). The `stringColor` of the number view. |  
| `numNormalColor` | An instance of [Color](../Classes/Color.md). The `normalColor` of the number view. |  
| `numTypingColor` | An instance of [Color](../Classes/Color.md). The `typingColor` of the number view. |  
| `background` | An instance of [Color](../Classes/Color.md). The `background` of the enclosing view. |  

### `font`
Set the [Font](../Classes/Font.md) used by all the views.**Arguments:**

| Argument | Description |
|----------|-------------|
| `font` | An instance of [Font](../Classes/Font.md). |  


## Examples


```supercollider
// Simplest version
(        // basic use
        w = Window.new.front;
        g = EZNumber(w, 170@16, " test  ", \freq, unitWidth: 30, numberWidth: 60, layout: \horz);
        g.setColors(Color.grey, Color.white);
);


// lots of numberviews on on view
(
w = Window.new.front;
w.view.decorator = FlowLayout(w.view.bounds);
w.view.decorator.gap = 2@2;

40.do{
        g = EZNumber(w, 170@16, " test  ", \freq, unitWidth: 30, numberWidth: 60, layout: \horz);
        g.setColors(Color.grey, Color.white, Color.grey(0.8));
};
);


// click these parentheses to see all features and layouts
(

m = nil;
m = 2@2;        // comment for no margin

/////////////////
/// Layout \horz

(        // all features
        g = EZNumber(nil, 170@20, " freq  ", \freq, unitWidth: 30, numberWidth: 60, layout: \horz, margin: m);
        g.setColors(Color.grey, Color.white, background: Color.grey(0.7));
        g.window.bounds = g.window.bounds.moveBy(-180, 50);
);

(        // no unitView
        g = EZNumber(nil, 170@20, " freq  ", \freq, unitWidth: 0, numberWidth: 60, layout: \horz, margin: m);
        g.setColors(Color.grey, Color.white, background: Color.grey(0.7));
        g.window.bounds = g.window.bounds.moveBy(-180, -20);
);

(        // no label, with unit. use window name as label
        g = EZNumber(nil, 120@20, nil, \freq, unitWidth: 30, numberWidth: 60, layout: \horz, margin: m);
        g.setColors(Color.grey, Color.white, background: Color.grey(0.7));
        g.window.bounds = g.window.bounds.moveBy(-180, -90);
        g.window.name = "Freq";
);


(        // no units, no label; use window name as label;
        g = EZNumber(nil, 120@20, nil, \freq, unitWidth: 0, numberWidth: 60, layout: \horz, margin: m);
        g.setColors(Color.grey, Color.white, background: Color.grey(0.7));
        g.window.bounds = g.window.bounds.moveBy(-180, -160);
        g.window.name = "Freq";
);

/////////////////
/// Layout \line2

(        // all features
        g = EZNumber(nil, 120@42, " freq  ", \freq, unitWidth: 30, numberWidth: 60, layout: \line2, margin: m);
        g.setColors(Color.grey, Color.white, background: Color.grey(0.7));
        g.window.bounds = g.window.bounds.moveBy(100, 50);
);

(        // no unitView, with label
        g = EZNumber(nil, 170@42, " freq  ", \freq, unitWidth: 0, numberWidth: 60, layout: \line2, margin: m);
        g.setColors(Color.grey, Color.white, background: Color.grey(0.7));
        g.window.bounds = g.window.bounds.moveBy(100, -50);
);
(        // no unitView, no label; use window name as label
        g = EZNumber(nil, 170@20, nil, \freq, unitWidth: 0, numberWidth: 60, layout: \line2, margin: m);
        g.setColors(Color.grey, Color.white, background: Color.grey(0.7));
        g.window.bounds = g.window.bounds.moveBy(100, -150);
        g.window.name = "Freq";
);


)



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
    w = Window("another control panel", Rect(200, 400, 300, 180));
    w.front; // make window visible and front window.
    w.view.decorator = FlowLayout(w.view.bounds);

    w.view.background = Color.rand;

    // add a button to start and stop the sound.
    startButton = Button(w, 75 @ 20);
    startButton.states = [
        ["Start", Color.black, Color.green],
        ["Stop", Color.white, Color.red]
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
    noteControl = EZNumber(w, 160 @ 20, "Note ", ControlSpec(24, 60, \lin, 1),
        { |ez| node.set("note", ez.value) }, 36);

    w.view.decorator.nextLine;
    cutoffControl = EZNumber(w, 160 @ 20, "Cutoff ", ControlSpec(200, 5000, \exp),
        { |ez| node.set("fc", ez.value) }, 1000);

    w.view.decorator.nextLine;
    resonControl = EZNumber(w, 160 @ 20, "Reson", ControlSpec(0.1, 0.7),
        { |ez| node.set("rq", ez.value) }, 0.2);

    w.view.decorator.nextLine;
    balanceControl = EZNumber(w, 160 @ 20, "Balance ", \bipolar,
        { |ez| node.set("bal", ez.value) }, 0);

    w.view.decorator.nextLine;
    ampControl = EZNumber(w, 160 @ 20, "Amp ", \db,
        { |ez| node.set("amp", ez.value.dbamp) }, -6);


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
```




