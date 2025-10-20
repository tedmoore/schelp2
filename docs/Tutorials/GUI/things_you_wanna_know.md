# GUI: Things you probably want to know

*Miscellaneous things you probably want to know about SuperCollider's GUI system.*

**Categories:** Tutorials>GUI


## GUI Tutorial
This helpfile is part of a [GUI tutorial](../../Tutorials/GUI/tutorial_intro.md).



## Rendering isn't always available
SuperCollider provides some useful classes to automate processes. Some of them are associated to a [Clock](../../Classes/Clock.md): mainly [Routine](../../Classes/Routine.md) and [Task](../../Classes/Task.md).

**Qt rendering system is unavailable within the context of clock associated threads**. In other words, you cannot 'directly' modify a widget within a [Routine](../../Classes/Routine.md) or a [Task](../../Classes/Task.md).

Instead, you need to defer the modification by **encapsulating it in a deferred function**, that will be executed once SuperCollider resume its main context, see [Function#-defer](../../Classes/Function.md#-defer). Doing otherwise will crash the program:


```
(
var win = Window();
var slider= Slider();
var value = 0;

var routine = Routine({
    loop {
        value = 101.rand / 100;
        // Interacting with a widget from within a routine:
        // instructions must be nested in a function, and deferred
        { slider.value_(value); }.defer;
        0.5.wait;
    };
}).play;

win.layout_(
    VLayout()
    .add(slider)
);

CmdPeriod.doOnce({
    routine.stop;
    win.close;
});

win.front;
)
```




## Qt limitations
This remark mostly concerns debugging and understanding issues. Since **Qt is a third-party library integrated within SuperCollider**, some of its limitations are unrelated to SuperCollider itself.

As an example, at the time of writing this, Qt [QImage](../../Classes/QImage.md) has a strict pixel limit and cannot exceed 32767x32767 pixels. This 'issue' being only related to Qt, it is documented on Qt sources/forums, but not on SuperCollider sources/forums. In other words, working with Qt within the context of SuperCollider might also include using Qts documentation directly.



## Pen usage and resource management
The [Pen](../../Classes/Pen.md) class allows the user to define a custom `drawFunc` to a [View](../../Classes/View.md).

[Pen](../../Classes/Pen.md) usage is a **two-steps process**: the user **first 'describes' the shape** they want to draw (using methods such as `fillRect` or `lineTo`), **then renders the shape**, using either `fill`, `stroke`, or `fillStroke`.

Depending on the hardware, **when drawing very complex shapes** (for a example a million lines), **some issues might arise**:

Drawing instructions are cached until they are drawn. This means that calling `lineTo` a million times before calling `stroke` might saturate the computers RAM before the `stroke` instruction effectively takes place and frees the cached instructions.

On the other hand, calling successively `lineTo` then `stroke` a million time might be time inefficient as several `lineTo` could have been grouped together before being drawn on screen.

The best solution in this case would be to test several configurations to balance RAM/CPU usage in the most efficient way.



