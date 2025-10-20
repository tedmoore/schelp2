# GUI: Composing views with basic components

*General examples about composing views with basic GUI components.*

**Categories:** Tutorials>GUI

**Related:** [GUI/create_window](../../Tutorials/GUI/create_window.md), [GUI/create_simple_instrument_view](../../Tutorials/GUI/create_simple_instrument_view.md)


## GUI Tutorial
This helpfile is part of a [GUI tutorial](../../Tutorials/GUI/tutorial_intro.md).

It is the third part of a beginner's introduction to SuperCollider's GUI system. First part covers  [creating a window](../../Tutorials/GUI/create_window.md), while second part talks about [interfacing a synth with a GUI interface](../../Tutorials/GUI/create_simple_instrument_view.md).



## What is this tutorial about?
This tutorial presents **different interfaces you might need to construct** when working with SuperCollider's system, **and discuss their particularities**. If you need a more detailed tutorial about the basics of view composition, you should read [GUI/create_simple_instrument_view](../../Tutorials/GUI/create_simple_instrument_view.md) first.

**SuperCollider implements different GUI components that allow you to compose complex softwares interfaces.**

The list of those components is available in the documentation, by selecting **Browse > GUI > Views**.

You can see those components as some base building blocks allowing you to construct a greater structure.



## Composing a Slider with a title and an editable text field
This is the simplest example about view composition: a [Slider](../../Classes/Slider.md), a [TextField](../../Classes/TextField.md) and a [StaticText](../../Classes/StaticText.md). Not much to say here, the code mostly speaks for itself. The only thing to remember is to have the [Slider](../../Classes/Slider.md) and the [TextField](../../Classes/TextField.md) update each other accordingly when edited.

**Please note that this example is 'unsafe'**: there is no mechanism preventing to enter high values inside the [TextField](../../Classes/TextField.md): any float number is valid. You are still responsible to clip values to the correct range when using a [TextField](../../Classes/TextField.md). Entering a non-valid number in the [TextField](../../Classes/TextField.md) will set the value to 0.0 (because converting a non-float [String](../../Classes/String.md) with `.asFloat` returns 0.0).


```
(
var value = 1;
var displayValue = { |value|
    value.postln;
};

var sliderView = UserView()
.bounds_(Rect(0, 0, 400, 64));
var slider;
var text = StaticText()
.align_(\center)
.string_("Slider Name");
var field;

slider = Slider()
.orientation_(\horizontal)
.action_({
    value = slider.value;
    field.string_(
        value.trunc(0.01).asString);
    displayValue.value(value);
});

field = TextField()
.align_(\center)
.string_(value.asString)
.maxWidth_(64)
.action_({
    value = field.string.asFloat;
    slider.value_(value);
    displayValue.value(value);
});

sliderView.layout_(
    HLayout()
    .add(
        VLayout()
        .add(text)
        .add(slider),
    )
    .add(field)
);

sliderView.front;
)
```




## Centralizing Views actions with a single Function
This example is the continuation of the previous one, and explains why **UI components shouldn't be directly responsible for the action they ultimately perform**. It also talks briefly about focus and keyboard input response.

One of the **common mistake when starting using SuperCollider's GUI system is to use a View's action function as if it was effectively the function responsible for modifying the software**. Even if it works reliably if there is only one View associated with the algorithm, this tends to decrease code readability. When several Views are tied to the same algorithm, this almost always introduces issues, as one can see in the previous example.

The next example shows **how to centralize the algorithm in a single** [Function](../../Classes/Function.md), which is responsible for applying the modification to the software, then update the Views accordingly. In this context, **View's action functions are only responsible to convert the data they provide to the right format, then to call the centralizing function**.

Here, several views are using the `updateValue` function to modify the value. This function also updates every views at once. What's interesting is that the function clips the value if it was out of bounds: this is preventing users to specify a wrong value when using the [TextField](../../Classes/TextField.md). This will clip any wrong value, regardless of its origin.

Both the [Slider](../../Classes/Slider.md) and the [TextField](../../Classes/TextField.md) have really small action functions: they only convert the value to the right format, then call `updateValue`. Beside readability, we only need to modify `updateValue` if we have to change the algorithm. View's `action` functions aren't concerned by any changes once set.

In this particular example, I also implement a switch statement which **allows the window to respond to keyboard inputs**. Since both [Slider](../../Classes/Slider.md) and [TextField](../../Classes/TextField.md) natively respond to keyboard inputs events, we have to manipulate Views focus to specify the context of the events.


```
(
// Specifying default value, and its range
var valueDefault = 440;
var valueMin = 440;
var valueMax = 880;
// Referencing value
// for keyboard events
var currentValue = valueDefault;

var window = Window("", Rect(100, 100, 400, 400));

var slider = Slider()
.orientation_(\horizontal)
.maxHeight_(64)
.value_(
    valueDefault.linlin(valueMin, valueMax, 0, 1)
);

var textField = TextField()
.string_(valueDefault.asString)
.align_(\center);

// The centralizing function:
var updateValue = { |value|
    // Clip the value to the correct range
    currentValue = value.clip(valueMin, valueMax);

    // This is where you'd implement actual controls
    // e.g.
    // synth.set(\freq, value);

    // Now we can update our interface

    // Adapt the value back to the slider's range
    slider.value_(
        currentValue.linlin(valueMin, valueMax, 0, 1
    ));

    // Convert the value to string format for the textField
    textField.string_(currentValue.trunc(0.01).asString);
};

// The slider needs to map its value to the correct
// range before calling the function
slider.action_({
    updateValue.value(
        slider.value.linlin(0, 1, valueMin, valueMax)
    );
});

// The textField needs to convert its value
// to float format before calling the function
textField.action_({
    updateValue.value(textField.string.asFloat);
});

// Clicking the background removes
// slider and textField focus,
// allowing to use arrow keys
// to control the value directly
window.view.mouseDownAction_({
    slider.focus(false);
    textField.focus(false);
});

// Setup the windows view
// so it responds to arrow
// keys events
window.view.keyDownAction_({ |view, char, mod, unicode, keycode|
    switch(keycode)
    // Arrow LEFT detection
    { 65361 } { updateValue.value(currentValue * 0.99); }
    // Arrow RIGHT detection
    { 65363 } { updateValue.value(currentValue * 1.01); }
    // Arrow UP detection
    { 65362 } { updateValue.value(currentValue * 1.1); }
    // Arrow DOWN detection
    { 65364 } { updateValue.value(currentValue * 0.9); };
});

window.layout_(
    VLayout()
    .add(slider)
    .add(textField)
);

// Unfocus the slider,
// which has focus by default
window.view.focus(true);

window.front;
)
```



> **Note:** There are several other ways to interface algorithms with graphical user interfaces. One of the most widely spread is the [Model-View-Controller design pattern](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller). For SuperCollider implementation of the Model-View-Controller paradigm, see [SimpleController](../../Classes/SimpleController.md).




## Creating a Tab View
An interface that provides a simple tab system, like one would find in a web browser, allowing to switch between several web pages.

To do this, we can **combine two simple building blocks**: some [Button](../../Classes/Button.md)s, and a [StackLayout](../../Classes/StackLayout.md).

A [StackLayout](../../Classes/StackLayout.md) allows to **insert several graphical contexts on top of each other**, as you would pile some drawings on top of each other. You can chose to only display one of them, or all of them, in which case you can see a view under another view. This is similar to the layer system you can find in drawing softwares.


```
(
var tabView = UserView();
var stackLayout = StackLayout();
var buttonLayout = HLayout();

var tabNames = [
    "Tab One",
    "Tab Two",
    "Tab Three"
];
var tabs = List(0);

tabNames.do({ |tabName, tabIndex|
    var button = Button()
    .string_(tabName)
    // Map the button to the stackLayout index:
    .action_({ stackLayout.index_(tabIndex); });

    // Tabs are created here
    // because it is only an example.
    // In real code,
    // your views have likely
    // been created before.
    var tab = UserView()
    .background_(Color.rand);

    buttonLayout.add(button);
    stackLayout.add(tab);
});

// Allows to specify the starting tab
stackLayout.index_(0);

tabView.layout_(
    VLayout()
    .add(buttonLayout, 1)
    .add(stackLayout, 9)
);

tabView.front;
)
```




## Implementing a view minimizer
This example demonstrate how to **toggle a views visibility as one would use a window minimize function**.

This is possible because **a layout redraws its children when their visibility is modified**.

The window is first split vertically in two: a main view, and a small menu that 'contains' hidden views. This menu is only visible when it is non-empty.

For each of our subviews (in our example, a [MultiSliderView](../../Classes/MultiSliderView.md) and a [StaticText](../../Classes/StaticText.md)), we are creating two [Button](../../Classes/Button.md)s: one that hides the view, and is situated in the same layout as the view it is hiding, and one inside the menu, that displays it back. They control the views visibility, and they also control the visibility of the menu.


```
(
var window = Window(
    "Visibility Toggle",
    Rect(100, 100, 600, 400)
);

// Our main display
var mainView = UserView()
.layout_(HLayout());

// Restricting max height
// because it is only a menu
var visibilityView = UserView()
.maxHeight_(64)
.layout_(HLayout());

// We reference the
// number of hidden views
// to hide the 'visibility menu'
// when no views are hidden
var numberOfHiddenView = 0;

// A multiSlider example
var multiSliderView;
var multiSliderHideButton;
var multiSliderShowButton;
var multiSlider;

// A text example
var textView;
var textHideButton;
var textShowButton;
var text;

// Setup the multiSlider view
multiSliderView = UserView()
.layout_(VLayout());

multiSlider = MultiSliderView()
.value_([1, 2, 3, 4, 5, 6, 7, 8].reciprocal)
.drawLines_(true)
.elasticMode_(1);

multiSliderHideButton = Button()
.string_("Hide MultiSlider")
.maxHeight_(64);

// Show button is not visible on startup
multiSliderShowButton = Button()
.visible_(false)
.string_("Show MultiSlider")
.maxHeight_(64);

multiSliderView.layout.add(
    multiSliderHideButton, 1);
multiSliderView.layout.add(
    multiSlider, 9);

// Insert the subview into the main view
mainView.layout.add(multiSliderView, 1);
// Add the 'show' button to the visibility view
visibilityView.layout.add(multiSliderShowButton);

// Setup the text view
textView = UserView()
.layout_(VLayout());

text = StaticText()
.string_("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam.")
.align_(\center);

textHideButton = Button()
.string_("Hide Text")
.maxHeight_(64);

// Show button is not visible on startup
textShowButton = Button()
.visible_(false)
.string_("Show Text")
.maxHeight_(64);

textView.layout.add(
    textHideButton, 1);
textView.layout.add(
    text, 9);

// Insert the subview into the main view
mainView.layout.add(textView, 1);
// Add the 'show' button to the visibility view
visibilityView.layout.add(textShowButton);

// Constructing the top level
window.layout_(
    VLayout()
    .add(mainView)
    .add(visibilityView)
);

// Hide the visibility view,
// because everything is visible at start
visibilityView.visible_(false);


// --- Here's the visibility logic: ---
// When the hide button is pressed
multiSliderHideButton.action_({
    // Hide the view
    multiSliderView.visible_(false);
    // Set the show button visible
    multiSliderShowButton.visible_(true);
    // Increment the number of hidden views
    numberOfHiddenView = numberOfHiddenView + 1;
    // If exactly one item is hidden,
    // this means we have to show the visibility view
    // which was previously hidden
    if(numberOfHiddenView == 1)
    { visibilityView.visible_(true); };
});

// Now the inverse for the show button:
// When the show button is pressed
multiSliderShowButton.action_({
    // Show the view
    multiSliderView.visible_(true);
    // Hide the show button
    multiSliderShowButton.visible_(false);
    // Decrement the number of hidden views
    numberOfHiddenView = numberOfHiddenView - 1;
    // If there is no hidden item,
    // hide the visibility view
    if(numberOfHiddenView == 0)
    { visibilityView.visible_(false); };
});

// Same for the text view:
textHideButton.action_({
    textView.visible_(false);
    textShowButton.visible_(true);
    numberOfHiddenView = numberOfHiddenView + 1;
    if(numberOfHiddenView == 1)
    { visibilityView.visible_(true); };
});

textShowButton.action_({
    textView.visible_(true);
    textShowButton.visible_(false);
    numberOfHiddenView = numberOfHiddenView - 1;
    if(numberOfHiddenView == 0)
    { visibilityView.visible_(false); };
});

// Done
window.front;
)
```






