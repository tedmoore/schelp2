# EZRanger

*A wrapper class for a label, a rangeslider, and numberboxes*

**Categories:** GUI>EZ-GUI

**Related:** [EZGui](../Classes/EZGui.md), [StaticText](../Classes/StaticText.md), [RangeSlider](../Classes/RangeSlider.md), [NumberBox](../Classes/NumberBox.md)

## Description

EZRanger is wrapper class which creates an (optional) [StaticText](../Classes/StaticText.md), and a [RangeSlider](../Classes/RangeSlider.md) plus a [NumberBox](../Classes/NumberBox.md). If the parent is `nil`, then EZRanger will create its own window. See [EZGui](../Classes/EZGui.md) more options.

### Scrolling and Arrow Keys
EZRanger's number boxes scroll by default, using the step size of the [ControlSpec](../Classes/ControlSpec.md). If the ControlSpec's step is set to 0, or is not set, then the stepping and scrolling will be guessed according to the `minval` and `maxval` values of the spec on creation of the view. Unlike the step variable of a regular [NumberBox](../Classes/NumberBox.md), `controlSpec.step` is also the smallest possible increment for the number boxes. By default, the shift-key modifier will allow you to step by 100x `controlSpec.step`, while the ctrl-key will give you 10x `controlSpec.step`. Since the alt-key would give you 0.1 of the minimum step, it is disabled by default, but you can change that by setting `numberView.alt_step` to any value you like. Accordingly, you can customize the other modifier keys to fit your needs. This also affects the arrow keys for the slider.




## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `parent` | The parent view or window. If the parent is nil, then EZRanger will create its own [Window](../Classes/Window.md), and place it conveniently on the screen if the bounds are a [Point](../Classes/Point.md). If the bounds are a [Rect](../Classes/Rect.md), then the [Rect](../Classes/Rect.md) determines the window bounds. |  
| `bounds` | An instance of [Rect](../Classes/Rect.md) or [Point](../Classes/Point.md). Default value is `160@20`. |  
| `label` | The label. Default value is `nil`. If `nil`, then no [StaticText](../Classes/StaticText.md) is created. |  
| `controlSpec` | The [ControlSpec](../Classes/ControlSpec.md) for scaling the value. |  
| `action` | A [Function](../Classes/Function.md) called when the value changes. The function is passed the EZRanger instance as its argument. |  
| `initVal` | An instance of [Array](../Classes/Array.md) `[lo, hi]`. If `nil`, then it uses the [ControlSpec](../Classes/ControlSpec.md)'s default value. |  
| `initAction` | A [Boolean](../Classes/Boolean.md) indicating whether the action function should be called when setting the initial value. The default is `false`. |  
| `labelWidth` | Number of pixels width for the label. default is 60. |  
| `numberWidth` | Number of pixels width for the number box. default is 45. |  
| `unitWidth` | Number of pixels width for the unit label. The default is 0. If 0, then no `unitLabel` is created. |  
| `labelHeight` | The default is 20; |  
| `layout` | `\vert`, `\line2`, or `\horz`. The default is `\horz`. |  
| `gap` | A [Point](../Classes/Point.md). By default, the view tries to get its parent's gap, otherwise it defaults to `2@2`. Setting it overrides these. |  
| `margin` | A [Point](../Classes/Point.md). This will inset the bounds occupied by the subviews of view. |  

```supercollider
(
w = Window.new.front;
g = EZRanger(w, 400@16, " test  ", \freq, { |v| v.value.postln }, [50, 2000], unitWidth: 30)
)

// Simplest version, no parent view, so a window is created
(
EZRanger(nil, 400@16, " test  ", \freq, { |v| v.value.postln }, [50, 2000])
)
```

The contained views can be accessed via the EZRanger instance variables: `rangeSlider`, `hiBox`, `loBox`, `unitView`, `labelView`.

## Instance Methods


### Accessing Instance and Class Variables
### `unitView`
The units label. Only appears if `unitWidth` was set to > 0.
### `controlSpec`
An instance of ControlSpec for scaling the values.
### `loBox`
The `lo` value [NumberBox](../Classes/NumberBox.md).
### `action`
Set/get a [Function](../Classes/Function.md) or [FunctionList](../Classes/FunctionList.md) to be evaluated when the value changes. The first argument will be the EZRanger.
### `rangeSlider`
The [RangeSlider](../Classes/RangeSlider.md) [View](../Classes/View.md)
### `lo`
Set/get the low value.
### `hi`
Set/get the high value
### `hiBox`
The hi value [NumberBox](../Classes/NumberBox.md).
### `round`
Rounds the values in the number boxes.

### Doing Some Task (optional)
### `doAction`
Performs the action at the current index and the global action.
### `value`
Gets/sets the `lo` and `hi` values.**Arguments:**

| Argument | Description |
|----------|-------------|
| `vals` | An instance of [Array](../Classes/Array.md) `[lo, hi]`. |  

### `valueAction`
Sets the value and performs the action at the index value and the global action.**Arguments:**

| Argument | Description |
|----------|-------------|
| `vals` | An instance of [Array](../Classes/Array.md) `[lo, hi]`. |  


### Changing Appearance
### `setColors`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `stringBackground` | An instance of [Color](../Classes/Color.md). The `background` of the label and unit views. |  
| `stringColor` | An instance of [Color](../Classes/Color.md). The `stringColor` of the label and unit views. |  
| `sliderColor` | An instance of [Color](../Classes/Color.md). The slider `background`. |  
| `numBackground` | An instance of [Color](../Classes/Color.md). The `background` of the number view. |  
| `numStringColor` | An instance of [Color](../Classes/Color.md). The `stringColor` of the number view. |  
| `numNormalColor` | An instance of [Color](../Classes/Color.md). The `normalColor` of the number view. |  
| `numTypingColor` | An instance of [Color](../Classes/Color.md). The `typingColor` of the number view. |  
| `knobColor` | An instance of [Color](../Classes/Color.md). The `knobColor` of the slider view. |  
| `background` | An instance of [Color](../Classes/Color.md). The `background` of the enclosing view. |  

### `font`
Set the Font used by all the views.**Arguments:**

| Argument | Description |
|----------|-------------|
| `font` | An instance of [Font](../Classes/Font.md). |  


## Examples


```supercollider
(    // basic use
    w = Window.new.front;
    g = EZRanger(w, 400@16, " test  ", \freq, { |v| v.value.postln }, [50, 2000], unitWidth: 30);
    g.setColors(Color.grey, Color.white, Color.grey(0.7), Color.grey, Color.white, Color.yellow);
);

// lots of range sliders on a view
(
w = Window.new.front;
w.view.decorator = FlowLayout(w.view.bounds);
w.view.decorator.gap = 1@1;

20.do{
    g = EZRanger(w, 400@16, " test  ", \freq, { |v| v.value.postln }, [50.rand, 50+20000.rand], unitWidth: 30)
    .setColors(Color.grey, Color.white, Color.grey(0.7), Color.grey, Color.white, Color.white, Color.yellow)
    .font_(Font("Helvetica", 11));

};
);

Window.closeAll

/////////////////////////////////////////////////////////////////
////////// click these parentheses to see all features and layouts
(

m = nil;
m = 2@2; // comment for no margin


/////////////////
/// Layout \horz

(        // all features, small font
        g = EZRanger(nil, 400@16, " freq  ", \freq,
            initVal: [100.rand, 200+2000.rand], unitWidth: 30, numberWidth: 60, layout: \horz, margin: 2@2);
        g.setColors(Color.grey, Color.white, Color.grey(0.7),
            Color.grey, Color.white, Color.yellow, background: Color.grey(0.7),
                knobColor: HiliteGradient(Color.grey, Color.white));
        g.window.bounds = g.window.bounds.moveBy(-180, 50);
        g.font_(Font("Helvetica", 10));
);

(        // no unitView
        g = EZRanger(nil, 400@16, " freq  ", \freq, initVal: [100.rand, 200+2000.rand],
            unitWidth: 0, numberWidth: 60, layout: \horz, margin: 2@2);
        g.setColors(Color.grey, Color.white, Color.grey(0.7),
            Color.grey, Color.white, Color.yellow, background: Color.grey(0.7),
                knobColor: HiliteGradient(Color.grey, Color.white));
        g.window.bounds = g.window.bounds.moveBy(-180, -20);
        g.font_(Font("Helvetica", 10));
);
(        // no label, so use window name as label
        g = EZRanger(nil, 400@16, nil, \freq, initVal: [100.rand, 200+2000.rand],
            unitWidth: 0, numberWidth: 60, layout: \horz, margin: 2@2);
        g.setColors(Color.grey, Color.white, Color.grey(0.7),
            Color.grey, Color.white, Color.yellow, background: Color.grey(0.7),
                knobColor: HiliteGradient(Color.grey, Color.white));
        g.window.bounds = g.window.bounds.moveBy(-180, -90);
        g.window.name = "Freq";
        g.font_(Font("Helvetica", 10));
);

/////////////////
/// Layout \line2

(        // all features
        g = EZRanger(nil, 300@42, " freq  ", \freq, initVal: [100.rand, 200+2000.rand],
            unitWidth: 30, numberWidth: 60, layout: \line2, margin: 2@2);
        g.setColors(Color.grey, Color.white, Color.grey(0.7),
            Color.grey, Color.white, Color.yellow, background: Color.grey(0.7),
                knobColor: HiliteGradient(Color.grey, Color.white));
        g.window.bounds = g.window.bounds.moveBy(-180, -160);
);

(        // no unitView, with label
        g = EZRanger(nil, 300@42, " freq  ", \freq, initVal: [100.rand, 200+2000.rand],
            unitWidth: 0, numberWidth: 60, layout: \line2, margin: 2@2);
        g.setColors(Color.grey, Color.white, Color.grey(0.7),
            Color.grey, Color.white, Color.yellow, background: Color.grey(0.7),
                knobColor: HiliteGradient(Color.grey, Color.white));
        g.window.bounds = g.window.bounds.moveBy(-180, -260);
);

(        // no label
        g = EZRanger(nil, 300@42, nil, \freq, initVal: [100.rand, 200+2000.rand],
            unitWidth: 30, numberWidth: 60, layout: \line2, margin: 2@2);
        g.setColors(Color.grey, Color.white, Color.grey(0.7),
            Color.grey, Color.white, Color.yellow, background: Color.grey(0.7),
                knobColor: HiliteGradient(Color.grey, Color.white));
        g.window.bounds = g.window.bounds.moveBy(-180, -360);
        g.window.name = "Freq";
);

(        // no label, so use window name as label
        g = EZRanger(nil, 150@42, nil, \freq, initVal: [100.rand, 200+2000.rand],
            unitWidth: 0, numberWidth: 60, layout: \line2, margin: 2@2);
        g.setColors(Color.grey, Color.white, Color.grey(0.7),
            Color.grey, Color.white, Color.yellow, background: Color.grey(0.7),
                knobColor: HiliteGradient(Color.grey, Color.white));
        g.window.bounds = g.window.bounds.moveBy(-180, -460);
        g.window.name = "Freq";
);

/////////////////
/// Layout \vert

(        // all features, small font
        g = EZRanger(nil, 45@300, " Vol  ", \db.asSpec.step_(0.01), initVal: [-3-15.rand, -2.rand],
            unitWidth: 30, numberWidth: 60, layout: \vert, margin: 2@2);
        g.setColors(Color.grey, Color.white, Color.grey(0.7),
            Color.grey, Color.white, Color.yellow, background: Color.grey(0.7),
                knobColor: HiliteGradient(Color.grey, Color.white, \h));
        g.window.bounds = g.window.bounds.moveBy(250, 50);
        g.font_(Font("Helvetica", 9));
);
(        // no label, small font
        g = EZRanger(nil, 45@300, nil, \db.asSpec.step_(0.01), initVal: [-3-15.rand, -2.rand],
            unitWidth: 30, numberWidth: 60, layout: \vert, margin: 2@2);
        g.setColors(Color.grey, Color.white, Color.grey(0.7),
            Color.grey, Color.white, Color.yellow, background: Color.grey(0.7),
                knobColor: HiliteGradient(Color.grey, Color.white, \h));
        g.window.bounds = g.window.bounds.moveBy(310, 50);
        g.font_(Font("Helvetica", 9));
);
(        // no Units small font
        g = EZRanger(nil, 45@300, " Vol", \db.asSpec.step_(0.01), initVal: [-3-15.rand, -2.rand],
            unitWidth: 0, numberWidth: 60, layout: \vert, margin: 2@2);
        g.setColors(Color.grey, Color.white, Color.grey(0.7),
            Color.grey, Color.white, Color.yellow, background: Color.grey(0.7),
                knobColor: HiliteGradient(Color.grey, Color.white, \h));
        g.window.bounds = g.window.bounds.moveBy(370, 50);
        g.font_(Font("Helvetica", 9));
);
(        // no unitView, no units small font
        g = EZRanger(nil, 45@300, nil, \db.asSpec.step_(0.01), initVal: [-3-15.rand, -2.rand],
            unitWidth: 0, numberWidth: 60, layout: \vert, margin: 2@2);
        g.setColors(Color.grey, Color.white, Color.grey(0.7),
            Color.grey, Color.white, Color.yellow, background: Color.grey(0.7),
                knobColor: HiliteGradient(Color.grey, Color.white, \h));
        g.window.bounds = g.window.bounds.moveBy(430, 50);
        g.font_(Font("Helvetica", 9));
);

)

/////////////////

////Sound Example


(    // example to explore a synthesis idea:
p = ProxySpace.push(s.boot);

q = q ? ();
q.freqRange = [200, 2000];
q.ampRange = [0.1, 1];
q.ringRange = [0.1, 10];
q.numRange = [3, 30];

q.soundfunc = { |dens = 5|
    Splay.ar(
        Array.fill(exprand(q.numRange[0], q.numRange[1]).asInteger, {
            Ringz.ar(
                Dust.ar(dens),
                exprand(q.freqRange[0], q.freqRange[1]),
                exprand(q.ringRange[0], q.ringRange[1]),
                exprand(q.ampRange[0], q.ampRange[1])
            )
        })
    ).distort
};
)
~plong.play;

~plong.fadeTime = 3;
~plong = q[\soundfunc];

(
w = Window("cow herd").front;
w.view.decorator_(FlowLayout(w.bounds.copy.moveTo(0, 0)));

Spec.add(\ring, [0.03, 30, \exp]);
Spec.add(\num, [3, 30, \exp, 1]);

EZRanger(w, 390@20, "numRange", \num, { |sl| q.numRange = sl.value }, labelWidth: 65)
    .round_(1);

EZRanger(w, 390@20, "freqRange", \freq, { |sl| q.freqRange = sl.value }, q.freqRange, labelWidth: 65)
    .round_(0.1);
EZRanger(w, 390@20, "ringRange", \ring, { |sl| q.ringRange = sl.value }, q.ringRange, labelWidth: 65)
    .round_(0.0001);
EZRanger(w, 390@20, "ampRange", \amp, { |sl| q.ampRange = sl.value }, q.ampRange, labelWidth: 65)
    .round_(0.0001);
Button(w, 190@20).states_([[\newSound]]).action_({ ~plong = q[\soundfunc] });
)
```




