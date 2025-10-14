# Window

*Top-level container of views*

**Categories:** GUI>Views

## Description

The Window is the most fundamental element of the GUI. It occupies a rectangular space on the screen within which other GUI elements (Views) are displayed.
A child view is added into a window by passing the window to the view's constructor. See [View#*new](../Classes/View.md#*new).

> **Note:** There is no distinction between windows, views, and containers; a View can be displayed directly on screen, and can contain other views. Therefore, visual descriptions of Window and most of the methods that are specific to Window in other GUI kits, also apply to and make part of View in Qt, and are thus shared by all its subclasses.The Window class is provided in Qt GUI for compatibility as well as convenience: e.g. unlike View, Window will be created by default in the center of the screen, and various aspects can be conveniently controlled using its constructor arguments.


The Window is usually drawn with a bar on its top edge that displays the window's title which you can set in the [constructor](#*new), or using [name](#name).


## Class Methods


### `new`
 Creates a new Window instance. You will need to call [front](#front) on it to become visible.**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` | A String for the text that will be displayed in the title bar. The default is 'panel'. |  
| `bounds` | A [Rect](../Classes/Rect.md) specifying the position and size of the window in screen coordinates.  The size does **not** include the window's border and title bar. Position is measured from the **bottom-left** corner of the screen (This differs from [View#-bounds](../Classes/View.md#-bounds), which uses the top-left corner).  This coordinate convention originates from SuperCollider’s original Cocoa GUI implementation on macOS, which uses a bottom-left origin. The default size is 400x400.  If no position is specified, the window is centered on the screen by default.
> **Note:** The default position may vary depending on screen resolution, platform, and operating system settings. |  
| `resizable` | A Boolean indicating whether the window is resizable by the user.  The default is `true`. |  
| `border` | A Boolean indicating whether this window has a border. Borderless windows have no title bar and thus can only be closed in code. The default is `true`. |  
| `scroll` | A Boolean indicating whether this window will add scrollbars if its contents exceed its bounds. If this is set to `true`, then [View#-resize](../Classes/View.md#-resize) settings will be ignored for contained views. The default is false. |  

### `allWindows`
 An array of all existing Window instances.
### `closeAll`
 Calls [close](#close) an all existing Window instances.
### `initAction`
 The default action object to be evaluated whenever a new Window is instantiated.
### `screenBounds`
 Returns a Rect with the size of the screen in pixels
### `availableBounds`
 Returns a Rect describing the area of the screen that windows can actually occupy (i.e. excluding the Mac dock, the task bar, or similar).
### `lowestPosition`
 Returns a floating-point value representing the lowest reasonable vertical position for a window on the screen.  This value is calculated to avoid overlap with system-reserved interface elements, such as the Windows taskbar, the macOS Dock, or the Linux dock (e.g. GNOME, KDE, etc.).  The result is not the absolute bottom edge of the screen, but rather the lowest position a window can occupy without interfering with areas reserved by the operating system.

## Instance Methods


### View hierarchy
### `view`
 When a Window is created, it creates a container view, accessible using this method, that occupies the whole area of the window, and which will be used as the actual parent of the child widgets.**Returns:** A View.
### `asView`
 Equivalent to [view](#view)
### `currentSheet`

> **Note:** Only in Cocoa GUI

 returns: The current modal sheet attached to this window, if it exists. See `"SCModalSheet".help`.

### Visibility
### `front`
 Displays the window on the screen (This has the same effect as setting [visible](#visible) to true).
### `minimize`
 Hides the window, only keeping its representation in the dock, taskbar, etc..
### `unminimize`
 Restores the window's previous state after being minimized.
### `fullScreen`
 Displays the window full-screen.
### `endFullScreen`
 Restores the window's previous state after being displayed full-screen.
### `alwaysOnTop`
 Whether the window should always stay on top of other windows, even when it is not the active one.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `visible`
 Whether the window is visible. Setting this to `true` has the same effect as [front](#front), and setting it to false closes the window without destroying it.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `close`
 Closes and destroys the window.
### `isClosed`
**Returns:** A Boolean stating whether the view has been closed.

### Geometry
### `bounds`
 The position and size of the window. The position is relative to the bottom-left corner of the screen.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Rect or a Point interpreted [as Rect](../Classes/Point.md#-asrect). |  
**Returns:** A Rect.
### `setTopLeftBounds`
 A convenience method that, unlike [bounds](#bounds), sets the bounds by measuring position from the top-left corner of the screen, and vertically offset by `menuSpacer`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `rect` | A Rect. |  
| `menuSpacer` | An Integer amount of pixels. |  

### `setInnerExtent`
 Resizes the window, keeping its position intact. This is equivalent to [View#-resizeTo](../Classes/View.md#-resizeto) called on the [view](#view).**Arguments:**

| Argument | Description |
|----------|-------------|
| `w` | An Integer width in pixels. |  
| `h` | An Integer height in pixels. |  

### `sizeHint`
 Redirects to [View#-sizeHint](../Classes/View.md#-sizehint) of the [view](#view).
### `minSizeHint`
 Redirects to [View#-minSizeHint](../Classes/View.md#-minsizehint) of the [view](#view).
### `addFlowLayout`
 A convenience method which sets `decorator` of the [view](#view) to a new instance of FlowLayout. See [FlowLayout](../Classes/FlowLayout.md) for examples.**Arguments:**

| Argument | Description |
|----------|-------------|
| `margin` | A Point describing the [margin](../Classes/FlowLayout.md#-margin) of the FlowLayout. |  
| `gap` | A Point describing the [gap](../Classes/FlowLayout.md#-gap) of the FlowLayout. |  
**Returns:** The new FlowLayout instance.
### `layout`
 Redirects to [View#-layout](../Classes/View.md#-layout) of the [view](#view).
### `moveToBottom`
 Moves the window to the lowest usable screen position without overlapping system-reserved areas (e.g., taskbars, docks).**Arguments:**

| Argument | Description |
|----------|-------------|
| `margin` | Adds vertical offset from the bottom. |  


### Appearance
### `name`
 The title of the window.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A String. |  

### `background`
 The background color of the window.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  

### `alpha`
 The transparency of the window.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float between 0.0 (invisible) and 1.0 (opaque). |  

### `refresh`
 Redraws the window and all its children.

### Interaction
### `userCanClose`
 Whether the user can close the window. The default is `true`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `acceptsClickThrough`
 Whether the window receives clicks when it is not front-most. The default is `true`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `acceptsMouseOver`
 Whether the window and all its children receive mouse-over events. The default is `false`. See also: [View#-acceptsMouseOver](../Classes/View.md#-acceptsmouseover) and [View#-mouseOverAction](../Classes/View.md#-mouseoveraction).**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  


### Actions and hooks
### `drawFunc`
 Just like the [UserView](../Classes/UserView.md), the window can be given a Function to evaluate whenever it is asked to redraw itself, so you can use the [Pen](../Classes/Pen.md) class to draw on the window. See [UserView#-drawFunc](../Classes/UserView.md#-drawfunc) for explanation.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Function. |  

### `toFrontAction`
 The action object to be evaluated whenever the window becomes the active one.
### `endFrontAction`
 The action object to be evaluated whenever the window ceases to be the active one.
### `onClose`
 The action object to be evaluated when the window is closed.
### `addToOnClose`
 Adds an object to [onClose](#onclose), wrapping the current value into an Array, if it is not yet.
### `removeFromOnClose`
 Removes an object from [onClose](#onclose), if the latter is an Array.

## Examples


### Adding Views

```supercollider
(
var w;
w = Window("my name is... panel", Rect(128, 64, 340, 360));

32.do({ |i|
    b = Button(w, Rect(rrand(20, 300), rrand(20, 300), 75, 24));
    b.states = [["Start "++i, Color.black, Color.rand],
        ["Stop "++i, Color.white, Color.red]];
});
w.front;
)
```




### Using Decorator

```supercollider
(
var w;
w = Window("my name is... panel", Rect(128, 64, 340, 360));

w.view.decorator = FlowLayout(w.view.bounds);
// w.addFlowLayout; // you can als write this instead of the line above

w.view.background = Color(0.6, 0.8, 0.8);
32.do({ |i|
    b = Button(w, Rect(rrand(20, 300), rrand(20, 300), 75, 24));
    b.states = [["Start "++i, Color.black, Color.rand],
        ["Stop "++i, Color.white, Color.red]];
});

w.front;
)
```




### Setting Bounds

```supercollider
// use screenbounds for precise placement from the top
(
x = Window.new("test", Rect(100, Window.screenBounds.height-180, 300, 100)); x.front;
)

// bounds.top refers to the bottom edge of the window,
// measured from the bottom of the screen. Different than in View.
x.bounds_(Rect(100, 400, 300, 300));
```




### Borderless Window

```supercollider
w = Window.new(border: false).front; // can't be manually closed
w.close; // so close it in code
```




### Window with Scrollers

```supercollider
(
w = Window(scroll: true); // you must set this when the window is created
c = Slider2D(w, Rect(0, 0, 1500, 300));
d = Slider(w, Rect(0, 310, 20, 300));
c.background = Color.grey.alpha = 0.6;
d.background = Color.grey.alpha = 0.6;
w.front;
)
```




### onClose

```supercollider
(
x = Window.new.front;
x.alpha = 0.8;
x.onClose_({ y = Synth.new(\default) }); // close the window and the synth plays
)
x.close;
y.free;
```




### Using Layouts
Layouts are used to organize view sizes automatically. See: [GUI-Layout-Management](../Guides/GUI-Layout-Management.md).


> **Note:** Only in Cocoa GUI



```supercollider
// make a window and a layout
(
w = Window(bounds: Rect(700, 200, 200, 200));
h = HLayout();
v = VLayout(h);
w.layout =  v;
w.front;
w.alwaysOnTop = true;
)

// add views step by step

v.add(k = Slider());
h.add(Slider());
h.add(Slider());
k.orientation = \horizontal;


h.add(g = VLayout(), 2, \left);
g.add(TextView());
g.add(TextView().string_("sand and hand"));

v.add(Button());
v.add(Button());
v.add(Button());
g.add(Button());

g.margins = [1, 1, 1, 1];
h.margins = [1, 1, 1, 1] * 23;
v.margins = [1, 1, 1, 1] * 5;

h.add(g = VLayout(), 1, \left);
g.add(g = HLayout(), 1, \left);
5.do { g.add(Slider().orientation_(\vertical)) };
```




### Drawing on Window with Pen

```supercollider
(
var w, much = 0.02, string, synth;

w = Window.new("gui", Rect(100, 100, 300, 500)).front;
w.view.background_(Color.new255(153, 255, 102).vary);

string = "gui ".dup(24).join;

w.drawFunc = Routine {
    var i = 0;
    var size = 40;
    var func = { |i, j| sin(i * 0.07 + (j * 0.0023) + 1.5pi) * much + 1 };
    var scale;
    var font = Font("Helvetica", 40).boldVariant;
    loop {
        i = i + 1;
        Pen.font = font;
        string.do { |char, j|

            scale = func.value(i, j).dup(6);

            Pen.fillColor = Color.new255(0, 120, 120).vary;
            Pen.matrix = scale * #[1, 0, 0, 1, 1, 0];
            Pen.stringAtPoint(char.asString,
                ((size * (j % 9)) - 10) @ (size * (j div: 9))
            );
        };
        0.yield // stop here, return something unimportant
   }
};

{ while { w.isClosed.not } { w.refresh; 0.04.wait } }.fork(AppClock);

w.front;

)
```






