# Menu

*Context and application-level menus*

**Categories:** GUI

**Related:** [MenuAction](../Classes/MenuAction.md), [CustomViewAction](../Classes/CustomViewAction.md), [ToolBar](../Classes/ToolBar.md), [MainMenu](../Classes/MainMenu.md)

## Description

The Menu class allows the creation and control of context menus and application-level menus.

```
(
~menu = Menu(
    MenuAction("A", { "A selected".postln }),
    MenuAction("B", { "B selected".postln }),
    MenuAction("C", { "C selected".postln }),
).front;
)
```




## Class Methods


### `new`
 Create a new menu. A menu is populated with [MenuAction](../Classes/MenuAction.md)s**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | One or more [MenuActions](../Classes/MenuAction.md) or Menus to be displayed in the menu. Menu arguments will create sub-menus. |  

```
(
    Menu(
        MenuAction("main"),
        MenuAction("menu"),
        Menu(
            MenuAction("sub"),
            MenuAction("menu"),
        ).title_("submenu")
    ).front;
)
```



## Instance Methods


### Control

### `front`
 Show the menu if it is not already shown. Note that unlike most Views, Menus are not destroyed when they are closed - front can be used to re-generate a single menu again and again.**Arguments:**

| Argument | Description |
|----------|-------------|
| `point` | A [Point](../Classes/Point.md) at which to show the menu. Default to the current mouse cursor position. |  
| `action` | The action that should appear at the specified point coordinates. Should be an action contained in the menu. |  


### `title`
 The title of the menu.**Arguments:**

| Argument | Description |
|----------|-------------|
| `title` | A [String](../Classes/String.md). |  


### `tearOff`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | If true, menu is / will be torn off from its parent and become a free-floating menu. |  


### `copy`
 Create an identical copy of the menu. The new menu will not be shown until `.front` is called.

### Events
 Menus broadcast several kinds of events that can be registered for with the standard [Object#-addDependant](../Classes/Object.md#-adddependant) calls.  Events broadcast by menu:

- `\aboutToShow`
- `\aboutToHide`
- `\triggered` (with the MenuAction that was triggered)
- `\hovered` (with action that was hovered over)


 **Events example**


```
(
m = Menu(MenuAction("Option A"), MenuAction("Option B")).title_("Event Example");

f = {
    |menu, what, value|
    "Menu '%' sent event %, value = %".format(menu.title, "\\" ++ what, value).postln;
    if (what == \hovered) { "Hovering over: %".format(value).postln };
    if (what == \triggered) { "Action triggered: %".format(value).postln; menu.destroy };
};

m.addDependant(f);
m.onClose_({ m.removeDependant(f) }).front;
)
```



### Context Menus
 One or more MenuActions can be attached to any View object. The shortcut key combinations for these actions will become available, and the actions will appear in the context menu for that view.

 See [View#-setContextMenuActions](../Classes/View.md#-setcontextmenuactions), [View#-addMenuAction](../Classes/View.md#-addmenuaction), [View#-removeMenuAction](../Classes/View.md#-removemenuaction) for more information.


```
(
~view = View().layout_(HLayout(
    ~button = Button().states_([["Button"]]),
    ~number = NumberBox().minWidth_(100).value_(100)
)).front;

~button.setContextMenuActions(
    MenuAction("Red", { ~button.states = [["Red", Color.red]] }),
    MenuAction("Green", { ~button.states = [["Green", Color.green]] }),
    MenuAction("Blue", { ~button.states = [["Blue", Color.blue]] })
);

~number.setContextMenuActions(
    MenuAction("100", { ~number.value = 100 }),
    MenuAction("200", { ~number.value = 200 }),
    MenuAction("300", { ~number.value = 300 })
);

)
```



## Examples

**A more complex menu.**

```
(
~image = Image(64, 64).draw({
    Pen.fillColor = Color.blue;
    Pen.fillOval(Rect(0, 0, 64, 64));
});

~menu = Menu(
    MenuAction("checked", { "checked".postln })
        .checked_(true),

    MenuAction("disabled", { "disabled".postln })
        .enabled_(false),

    MenuAction("keyboard short", { "keyboard short".postln })
        .shortcut_("Ctrl+Shift+N"),

    MenuAction("icon", { "icon".postln })
        .icon_(~image),

    MenuAction("font", { "font".postln })
        .font_(Font("Helvetica", 20, italic: true)),

    MenuAction.separator.string_("other stuff"),

    CustomViewAction(Slider().orientation_(\horizontal)).action_({ |v| v.value.postln }),

    Menu(
        "string.toAction",
        { "function.toAction".postln }
    ).title_("submenu")
).front;
)
```




