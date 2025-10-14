# MainMenu

*A manager for sclang's application-level menu*

**Categories:** GUI

**Related:** [MenuAction](../Classes/MenuAction.md), [ToolBar](../Classes/ToolBar.md), [MainMenu](../Classes/MainMenu.md)

## Description

This class allows control over items displayed in the sclang application-level menu. Application-level menus may not exist depending on platform — in particular, macOS and some Linux window managers have it, but Windows does not. On platforms without this feature, the methods in this class simply don't do anything.

> **Note:** This is the menu for the sclang application, not the IDE.


> **⚠️ Warning:** The behavior of this class changed in version 3.10.2. Menu items for controlling the process and servers will not be added and updated by default, as in versions 3.10.0 and 3.10.1. Those items can still be created by calling `initBuiltInMenus`. This behavior may change again in a future version.

```supercollider
(
~testTone = MenuAction("Test Tone", {
    { SinOsc.ar(400) * 0.1 }.play;
});

MainMenu.register(~testTone, "Tests");
)

MainMenu.unregister(~testTone); // to remove
```




## Class Methods


### `initBuiltInMenus`
 Initialize menu items under the main "SuperCollider" menu that enable process and server monitoring and control:- Stop - same as Cmd/Ctrl-Period
- Servers - a submenu listing available servers, with items for controlling each. The default server will be noted, and selecting the name of a server in this menu will set it as the default.
- Quit - quit sclang process

### `register`
 Register a MenuAction to a main application menu. This menu item will exist for the duration of the app, or until .unregister is called for the action.**Arguments:**

| Argument | Description |
|----------|-------------|
| `action` | A [MenuAction](../Classes/MenuAction.md). |  
| `menu` | A String, representing the name of the top-level menu to contain the action. |  
| `group` | An optional string. Action will be placed in a section of the menu with other members of the same group, with a separator between items of other groups. |  
MainMenu.register provides an easy way to register global menu items, in a way that helps avoid disrupting menus registered by other SuperCollider components. If you want to register menus for personal use, add the registration calls to your startup.scd file. This will ensure the menus are created automatically on launch. If you're registering menu actions for a Quark or other component intended for distribution, be sure to be polite and thoughtful about where you're registering actions. Avoid creating new top-level menus if possible - instead, try to use one of the following canonical menus to register your actions. Add your actions to a group to ensure you don't collide with actions from another component:- File
- Edit
- Server
- Quarks
- Help
 If registering menu items for a Quark, consider registering as a sub-menu of the Quarks menu. This can easily be done using the [#*registerQuarkMenu](#*registerquarkmenu) method.
### `registerQuarkMenu`
 Convenience method for registering a menu of functionality related to a Quark.  It will appear as a sub-menu under the main Quarks menu.**Arguments:**

| Argument | Description |
|----------|-------------|
| `quarkName` | A String, the name of the quark |  
| `menu` | A [Menu](../Classes/Menu.md), a menu. |  

### `unregister`
 Remove a MenuAction that has been registered previously.
> **Note:** It is usually disruptive and confusing to add and remove menu items dynamically.  If you're registering a menu item that should only sometimes be available, consider disabling it using `menuAction.enabled = false;` rather than removing it.

**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A MenuAction. |  

### `otherMenus`
 A list of menus to append to the set of main application menus.> **⚠️ Warning:** This is intended for standalone SuperCollider applications, and should not be used to register menus during normal SC usage.
### `add`
 Adds a menu to `otherMenus`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `menu` | A [Menu](../Classes/Menu.md). |  

### `remove`
 Removes a menu to `otherMenus`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `menu` | A [Menu](../Classes/Menu.md). |  

### `insert`
 Inserts a menu in `otherMenus` at the given index.**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | Index. An [Integer](../Classes/Integer.md). |  
| `menu` | A [Menu](../Classes/Menu.md). |  

### `clear`
 Clears `otherMenus`. The main application menus are unaffected.**Arguments:**

| Argument | Description |
|----------|-------------|
| `menu` | A [Menu](../Classes/Menu.md). |  

### `applicationMenu`
 The main SuperCollider application menu.> **⚠️ Warning:** This is intended for standalone SuperCollider applications, and should not be used to register menus during normal SC usage.
## Examples


```supercollider
(
~show = MenuAction("Show Window", {
    ~window ?? {
        ~window = TextView().string_("Here it goes!").minSize_(300@200);
        ~window.onClose = { ~window = nil };
        ~window.front;
    }
});
~hide = MenuAction("Hide Window", {
    ~window !? {
        ~window.close();
        ~window = nil;
    }
});

MainMenu.register(Menu(~show, ~hide).title_("My Quark"), "Quarks", "My Quark")
)
```




