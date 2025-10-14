# GUI: Create a Window

*How to create a window, insert widgets and map keyboard inputs to it with SuperCollider.*

**Categories:** Tutorials>GUI

**Related:** [GUI/create_simple_instrument_view](../../Tutorials/GUI/create_simple_instrument_view.md), [GUI/compose_complex_view](../../Tutorials/GUI/compose_complex_view.md)


## GUI Tutorial
This helpfile is part of a [GUI tutorial](../../Tutorials/GUI/tutorial_intro.md).

It is the first part of a beginner's introduction to SuperCollider's GUI system. Second part covers  [interfacing a synth with a GUI interface](../../Tutorials/GUI/create_simple_instrument_view.md), while third part talks about [composing views with basic GUI components](../../Tutorials/GUI/compose_complex_view.md).



## Creating and manipulating a Window
To **create** a [Window](../../Classes/Window.md) in SuperCollider, simply execute the following code:


```supercollider
(
var win = Window();
win.front;
)
```


The first command creates the window, and the second tells your graphical system to display it.

You can customize its name, position and size directly when creating it:


```supercollider
(
var window = Window("My window", Rect(100, 100, 600, 200));

window.front;
)
```


You can also toggle its **fullscreen** mode:


```supercollider
(
var window = Window();
window.fullScreen;
window.front;
)
```


If you executed the previous example, you might have noticed that closing it can be difficult, because it doesn't show its top menu, and doesn't respond to keyboard inputs. To **close every window** that SuperCollider created using code, simply execute the following command:


```supercollider
Window.closeAll;
```


If you stored your window in a global variable, you can also **close it directly**:


```supercollider
~window.close;
```


Once closed, you need to recreate it, because it has been completely deleted.


> **Note:** The following code can be useful when developing graphical interfaces:
```supercollider
(
var window = Window();
CmdPeriod.doOnce({ window.close; });
window.front;
)
```

Every time you hit **ctrl + shift + .**, this will close the window you're currently creating, if it is still open, preventing the accumulation of windows during development process.




## Inserting and positioning views
Once you've created the window, you can **add** a [View](../../Classes/View.md) **directly** into it, by passing the window as parent argument when creating the [View](../../Classes/View.md):


```supercollider
(
var window = Window();
var button = Button(window);
button.string_("Click me!");
window.front;
)
```


When doing so, **you are responsible for** setting your [View](../../Classes/View.md) at **the right position and size**:


```supercollider
(
var window = Window();
var button = Button(
    window,
    Rect(100, 100, 200, 200)
);
button.string_("Click me!");
window.front;
)
```


If you'd rather use **automatic positioning** and **automatic resizing** when the window is re-sized, you should use a [Layout](../../Classes/Layout.md):


```supercollider
(
var window = Window();

var layout = HLayout();

var button = Button(window);
button.string_("Click me!");

// Assign the layout to the window
window.layout_(layout);
// Then add the View to the layout
layout.add(button);

window.front;
)
```


See [Layout](../../Classes/Layout.md) for more information about this organisation method. The layout system is also discussed in the next tutorial of this series.


> **Note:** Adding a [StackLayout](../../Classes/StackLayout.md) as primary Layout for a Window allows to easily switch between different Views, in other words, different interfaces.




## Keyboard input
[Window](../../Classes/Window.md) 'inherits' from the [UserView](../../Classes/UserView.md) **action** system. It can respond to mouse and keyboard events. See the [UserView](../../Classes/UserView.md) help file for more information about this.

Another way to interact with the window using the keyboard, which might be preferable, is to assign a function to `View.globalKeyDownAction`.

`View.globalKeyDownAction` **will be executed whenever a keyboard input is received** (regardless of current focus), and **allows an action to take place in response** to the keyboard event, for example closing the window:


```supercollider
(
var window = Window();
var fullScreenActive = false;

View.globalKeyDownAction = { |view, char, mod, unicode, keycode, key|

    switch(keycode)

    // if the keycode is 65307 (ESC): close the window
    { 65307 } { window.close; }

    // if the keycode is 102 (f): toggle full screen ON / OFF
    { 102 } {
        fullScreenActive = fullScreenActive.not;
        if(fullScreenActive)
        { window.fullScreen; }
        { window.endFullScreen; };
    };
};

window.front;
)
```



> **Note:** Using a [FunctionList](../../Classes/FunctionList.md) with `View.globalKeyDownAction` allows to incrementally build up keyboard input response:
```supercollider
(
var window = Window();

View.globalKeyDownAction = FunctionList();

View.globalKeyDownAction.addFunc({ |view, char, mod, unicode, keycode, key|

    switch(keycode)
    // if the keycode is 65307, i.e. ESC, close the window
    { 65307 } { window.close; };
});

window.front;
)
```




## And that's it!
With the ability to **create a window**, **insert views inside** and make it **respond to keyboard inputs**, you're well set to go forward in your SuperCollider graphical experiments.

The next section of this tutorial is: [GUI/create_simple_instrument_view](../../Tutorials/GUI/create_simple_instrument_view.md). It starts from the previous examples and talks about connecting a button and a slider to a synth, and about the layout system.



