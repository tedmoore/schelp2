# What's new in Qt GUI

*A summary of new features and differences in Qt GUI*

**Categories:** GUI, News

This document is intended for those already familiar with graphical user interface programming in SuperCollider. If you are new to this topic, you are suggested to first read the [GUI-Introduction](../Guides/GUI-Introduction.md).
For the purpose of this guide, let's switch to the Qt GUI:

```
GUI.qt
```


## View hierarchy

### Every view can be a window
Every view can be displayed as a window on its own, without the use of the Window class. Hence, most methods that are present in Window, are also present in View.

For example, you can display any view without embedding it in a Window or another container view using the [View#-front](../Classes/View.md#-front) method. For this reason, it is valid to omit the 'parent' argument at view construction - any view without a parent can be shown as a window:


```
(
x = SoundFileView().front;
x.load(ExampleFiles.child);
)
```





### Every view can be a container
Every view can contain other views (i.e. act as their parent). For this reason, if you want to group several views together, you can simply use a View as the container:


```
(
v=View(bounds:300@300);
5.do { |i|
    Slider(v).moveTo(i * 25 + 10, 10);
};
v.front;
)
```






## Layout management
The Qt layout system allows you to forget about pixels - it manages the size and position of child views in a parent automatically.


### Intrinsic view sizes
You may have noticed in the examples above that, besides omitting the `parent` argument, we sometimes omitted the `bounds` argument as well, at view construction. This is possible because views have intrinsically defined preferred and minimum sizes. See [GUI-Layout-Management#Intrinsic view sizes](../Guides/GUI-Layout-Management.md#intrinsic-view-sizes) for further explanation.




### Layout classes
A collection of layout classes allows you to associate one of them with a parent view and several child views, and it will manage positions and sizes of the children automatically according to their size preferences and constraints. It will also do that dynamically, as you resize the window:


```
(
w = Window.new(bounds:Rect(100,100,300,80)).layout_(
    VLayout (
        HLayout(
            Button().states_([["Super"]]),
            TextField().string_("Collider")
        ),
        Button().states_([["SuperCollider"]])
    )
).front;
)
```


See the [GUI-Layout-Management](../Guides/GUI-Layout-Management.md) guide for detailed explanation.





## Color management

### The palette
Qt has the notion of the color palette - a collection of colors from which the views pick when drawing themselves. It is represented by the [QPalette](../Classes/QPalette.md) class, and can be set on a view using [View#-palette](../Classes/View.md#-palette).

By default, a window will get the global palette ( [QtGUI#*palette](../Classes/QtGUI.md#*palette) ), and the palette is inherited by child views from their parent. Thus, changing the parent's palette will also affect its children, unless the palette has been overridden on a particular child. You can easily change the appearance of the whole GUI by changing the global palette.




### Predefined palettes
There are two predefined palettes ( [QPalette#*light](../Classes/QPalette.md#*light) and [QPalette#*dark](../Classes/QPalette.md#*dark) ), and you can also access the native palette of your operating system ( [QPalette#*system](../Classes/QPalette.md#*system) ):

Try changing the global palette with the code below; if you have the Qt GUI active, this will affect this window as well:


```
QtGUI.palette = QPalette.dark;

QtGUI.palette = QPalette.light;

QtGUI.palette = QPalette.system;
```






## View actions and hooks

### Mouse and key event propagation
In addition to key events, mouse events can also propagate to parent views.

Also, the control over event propagation works differently in Qt. See [View#Key and mouse event processing](../Classes/View.md#key-and-mouse-event-processing) for detailed explanation.

Moreover, you can make a view transparent for mouse events using [View#-acceptsMouse](../Classes/View.md#-acceptsmouse), which will forward all mouse events to the view under, regardless of whether they are in a parent-child relationship.


```
(
var win, parent, child, sibling1, sibling2;
win = Window(bounds:Rect(30,30,300,300));
parent = Slider2D(win, win.bounds.moveTo(0,0).insetBy(50,50));

// A StaticText will propagate mouse clicks to parent by default:
child = StaticText(parent, Rect(100,-50,150,150))
    .align_(\bottomLeft)
    .string_("\npropagate\nto\nSlider2D")
    .background_(Color.red.alpha_(0.4));

// This StaticText is not a child of Slider2D so will propagate mouse
// clicks to the window instead:
sibling1 = StaticText(win, Rect(0,0,150,150))
    .align_(\topLeft)
    .string_("propagate\nto\nWindow")
    .background_(Color.cyan.alpha_(0.4));

// This StaticText is not a child of Slider2D, but is made transparent for mouse events:
sibling2 = StaticText(win, Rect(150,150,150,150))
    .align_(\bottomRight)
    .string_("ignore")
    .background_(Color.green.alpha_(0.4))
    .acceptsMouse_(false);
win.view.mouseDownAction = { win.background = Color.red(0.6) };
win.view.mouseUpAction = { win.view.palette = QPalette() };
win.front;
)
```





### Extended mouse interaction
Many Qt views already implement some kind of **mouse wheel** interaction. For example, you can scroll a ScrollView, ListView and TreeView using the mouse wheel. You can also change the value of a Slider or a Knob using the mouse wheel. In addition, you can assign an action of your own to the mouse wheel event using [View#-mouseWheelAction](../Classes/View.md#-mousewheelaction):

There's another two handy new mouse actions triggered when the **mouse enters or leaves** the view: [View#-mouseEnterAction](../Classes/View.md#-mouseenteraction) and [View#-mouseLeaveAction](../Classes/View.md#-mouseleaveaction):.


```
(
var val = 1.0;
t=StaticText(bounds:Rect(30,30,100,100))
    .font_(Font(size:25))
    .align_(\center)
    .string_(val.asString)
    .stringColor_(Color.red)
    .background_(Color.black)
    .front;
t.mouseEnterAction = { t.background = Color.white };
t.mouseLeaveAction = { t.background = Color.black };
t.mouseWheelAction = { |v,x,y,mod,dx,dy|
    if(dy > 0) { val = val + 0.05 } { val = val - 0.05 };
    val = val.clip(0,2).round(0.01);
    t.string = val.asString;
    t.stringColor = Color.red(val);
};
)
```





### Hooks for position and size change
Since views can be automatically repositioned and resized by [layouts](#layout-management), or by the user (if they are windows), it may come handy to make your view respond to these changes using [View#-onMove](../Classes/View.md#-onmove) and [View#-onResize](../Classes/View.md#-onresize).


```
(
var view, update;
update = { |v|
    var bounds = v.bounds;
    v.string = "%@%\n%x%".format(
        bounds.left,
        bounds.top,
        bounds.height,
        bounds.width
    );
};

x = StaticText(bounds:Rect(100,100,200,200)).align_(\center).font_(Font(size:25));
x.onMove = update;
x.onResize = update;
update.(x);

x.front;
)
```






## Enhancements

### Stethoscope
Qt brings a new implementation of [Stethoscope](../Classes/Stethoscope.md) that uses *shared memory* to allow highly efficient monitoring of buses on any **local server**.

All the 'scope' methods of various classes (like Server, Bus, Function, etc.) are wired to this new implementation, so you don't need to worry about instantiating a Stethoscope yourself.


```
Server.local.scope;
```





### SoundFileView
[SoundFileView](../Classes/SoundFileView.md) has **infinite display resolution**. This means you can always zoom into the waveform until you see a single sound frame.

It also offers convenient **mouse interaction** for zooming in and scrolling:

- shift + right-click + mouse-up/down = **zoom**
- right-click + mouse-left/right = **scroll**



```
(
var x = SoundFileView().front;
x.load(ExampleFiles.child);
)
```


Alternatively to displaying a soundfile, you can allocate an empty amount of display frames, and fill it **part by part** with data to display (see documentation of [SoundFileView#-alloc](../Classes/SoundFileView.md#-alloc) and [SoundFileView#-set](../Classes/SoundFileView.md#-set)). This allows, for example, to implement efficient monitoring of recording into a Buffer.


```
(
var v, s;
v = SoundFileView().front;
s = Signal.sineFill(1000, 1.0/[1,2,3,4]);
v.alloc(5000, samplerate: 500);
3.do { |i| v.set( i * 2000, s * (1/(i+1)) ) };
)
```





### EnvelopeView
[EnvelopeView](../Classes/EnvelopeView.md) offers two different **display styles**: in addition to traditional style where nodes are drawn as rectangles with labels inside, it can draw nodes as small dots, with labels next to them. See [EnvelopeView#-style](../Classes/EnvelopeView.md#-style).


```
(
var w, e, m;
e = EnvelopeView()
    .value_([[0,0.4,0.6,1.0],[0,0.7,0.5,0.56]])
    .strings_(["alpha", "beta", "gamma", "delta"])
    .thumbWidth_(60)
    .style_(\dots);
m = PopUpMenu()
    .items_(["Dot Style", "Rect Style"])
    .action_({e.style = m.value});
w = Window()
    .layout_(VLayout(m,e))
    .front;
)
```


You can enforce a **strict order of nodes** on the time axis. In this case, a node can not move to position before the previous node, or after the next node. See [EnvelopeView#-keepHorizontalOrder](../Classes/EnvelopeView.md#-keephorizontalorder) and the example below.

You can also control how a **selection of nodes** behaves when it is **moved**: it can either keep its form rigidly and block all movement when meeting view edges or other nodes, or it can adjust its form to the obstacles, allowing the movement of those nodes that are not blocked individually. See [EnvelopeView#-elasticSelection](../Classes/EnvelopeView.md#-elasticselection) and the following example.

Example: try selecting several nodes (by clicking on them with Shift key pressed) and moving them around, then use the menu to switch the way selection behaves, and repeat:


```
(
var w, e, m;
e = EnvelopeView()
    .value_([
        [0, 0.1, 0.3, 0.4, 0.55, 0.7, 1.0],
        [0, 1.0, 0.7, 0.3, 0.5, 0.2, 0]
    ])
    .keepHorizontalOrder_(true)
    .elasticSelection_(true)
    .front;
m = PopUpMenu()
    .items_(["Elastic Selection", "Rigid Selection"])
    .action_({e.elasticSelection = m.value == 0});
w = Window()
    .layout_(VLayout(m,e))
    .front;
)
```





### ScrollView
[ScrollView](../Classes/ScrollView.md) allows to **replace the canvas** that holds its child views with an arbitrary view. This allows great flexibility, including using a [layout](#layout-management) to manage the child views. See [ScrollView#-canvas](../Classes/ScrollView.md#-canvas) for explanation, and this [example](../Classes/ScrollView.md#examples).





## New views

### TreeView
[TreeView](../Classes/TreeView.md) is a powerful addition to the group of views that display a **set of items** (including ListView and PopUpMenu). It displays items organized in a **hierarchical** manner, akin to filesystem browsers.

Unlike ListView, where items are only arranged in one column, TreeView may consist of **several columns**: each item occupies a row, and may contain one text value for each column. Columns also have **labeled headers**.

Moreover, each data field of an item may also **contain another view**, giving you a great potential for interactivity with items.




### WebView
[WebView](../Classes/WebView.md) is the core component for **web page browsing**. It is also implemented in the Cocoa GUI, but we list it here nonetheless.

It is a view that displays web pages, with web technology support comparable to widespread desktop web browsers.


> **Note:** There may currently be some issues with displaying multimedia content.



```
(
w = WebView(bounds: Window.screenBounds.insetBy(100,40))
    .url_("http://supercollider.sourceforge.net/")
    .front;
)
```








