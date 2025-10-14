# TextView

*A view displaying editable formatted text*

**Categories:** GUI>Views

## Description

TextView consists of an area where **multi-line text** can be typed in and edited.
Using the view's methods, the text can be formatted: different **font** and **text color** can be applied to parts of the text. Text can also be inserted, removed, and selected programmatically.
The view can **open text documents** and load from them both **plain text**, as well as formatted text in **HTML**, although it can not save the text back to files. However, you can get the contents of the view using the [string](#string) method and then implement saving on your own, but the -string method will only return plain text, regardless of how the contents of the view are formatted.


## Class Methods



## Instance Methods


### Text and Formatting
### `open`
 Opens a file at `path` and loads text from it. The file can be in plain text or HTML (or RTF, in Cocoa GUI) format. Note however that saving formatted text in the view is not supported. If loading the text from the file succeeds, it will replace any current contents of the view.**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` | A String. |  

### `string`
 The entire displayed contents of the view, as plain text. Setting this variable will replace any current contents of the view.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A String. |  

### `setString`
 Inserts the `string` at `start` position, replacing `size` amount of following characters. If `size` is 0, the text will be inserted without any characters being removed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `string` | A String - the text to insert. |  
| `start` | An Integer position within the text, in characters. |  
| `size` | An Integer amount of characters to be replaced. |  

### `currentLine`
 The plain text of the line at text cursor.

### Formatting
TextView supports text font and color, and can syntax colorize sclang code.


> **Note:** The formatting is reset when the string changes.



```supercollider
(
var text = "Tous ces nombres paraissent bien concrets";
t = TextView(bounds: Rect(300, 400));
t.string = text;
t.front;
fork {
    loop {
        2.0.rand.wait;
        defer {
            t.setFont(Font("Times", rrand(12, 48)), rand(text.size - 1), rrand(3, 17));
            t.setStringColor(Color.rand, rand(text.size - 1), rrand(3, 17));

        }
    }
};
)
```


### `setFont`
 Applies the `font` to `size` amount of characters following the `start` position.**Arguments:**

| Argument | Description |
|----------|-------------|
| `font` | A Font to apply to the desired range of text. |  
| `start` | An Integer position within the text, in characters. |  
| `size` | An Integer amount of characters. |  

### `setStringColor`
 Applies the `color` to `size` amount of characters following the `start` position.**Arguments:**

| Argument | Description |
|----------|-------------|
| `color` | A Color to apply to the desired range of text. |  
| `start` | An Integer position within the text, in characters. |  
| `size` | An Integer amount of characters. |  

### `syntaxColorize`
 Applies colors to text throughout the entire contents of the view, according to the SuperCollider language syntax highlighting scheme.
```supercollider
(
t = TextView(bounds: Rect(300, 400));
t.string = this.cmdLine;
t.syntaxColorize;
t.front;
)
```



### Text Selection
### `selectedString`
 The plain text contained in the current selection. When getting this variable and there is no selection, the entire line at text cursor is returned (equivalent to [currentLine](#currentline)). Setting this variable will replace text in the selection with the argument, or do nothing if there is no selection.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A String. |  
**Returns:** A String.
### `selectionStart`
 The starting position of the selection. If no text is selected this variable represents the cursor position.**Returns:** An Integer position within the text, in characters.
### `selectionSize`
 The size of the current selection.**Returns:** An Integer amount of characters - 0 if no text is selected.
### `select`

> **Note:** Not available in **Cocoa GUI**.

 Selects `size` amount of characters following the `start` position. The cursor will remain at the end of the new selection.**Arguments:**

| Argument | Description |
|----------|-------------|
| `start` | An Integer position within the text, in characters. |  
| `size` | An Integer amount of characters. |  


### Appearance
### `font`
 The default font of the entire text. This font applies to any text to which a font has not been applied using [setFont](#setfont).**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Font. |  

### `stringColor`
 The default color of the entire text. This color applies to any text to which a color has not been applied using [setStringColor](#setstringcolor).
> **Note:** Calling `stringColor_` does *not* affect the cursor's color. Setting a dark background, using `background_`, and a light text color will leave the cursor as a dark color. It is recommended to set the background and string colors by setting the TextView's palette to an instance of [QPalette](../Classes/QPalette.md).
```supercollider
(
t = TextView(nil, Rect(800, 50, 500, 400))
.string_("Some text")
.palette_(QPalette.dark)  // set all colors here
.front;
)
```


### `tabWidth`
 The width of tab characters as they are displayed.

### Interaction
### `editable`
 Whether the contents of the view are editable, i.e. the text can be typed in and deleted by the user.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `enterInterpretsSelection`
 Whether the selection will be interpreted and invoked as SuperCollider code when Ctrl/Cmd/Shift + Enter key combination is pressed. Defaults to `false`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `usesTabToFocusNextView`
 Whether the tab key will - instead of inserting a tab character into the text - switch focus to the next view (as usual for other views). Defaults to `false`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `hasHorizontalScroller`
 Whether the horizontal scroller is shown. Note that if [autohidesScrollers](#autohidesscrollers) is `true` the scroller may be hidden despite this variable being set to `true`. Since the TextView typically wraps text into the next line when a line reaches the edge of the view, the horizontal scroller may never be shown, unless [autohidesScrollers](#autohidesscrollers) is `false`. Defaults to `true`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `hasVerticalScroller`
 Whether the vertical scroller is shown. Note that if [autohidesScrollers](#autohidesscrollers) is `true` the scroller may be hidden despite this variable being set to `true`. Defaults to `true`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `autohidesScrollers`
 Whether each of the scrollers will be automatically hidden if there is no use for it, i.e. the content is not scrollable in the direction of the scroller. If [hasHorizontalScroller](#hashorizontalscroller) or [hasVerticalScroller](#hasverticalscroller) is `false`, the respective scroller will always be hidden, regardless of this variable. Defaults to `true`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  


### Drag and Drop

> **Note:** Default drag-and-drop behavior of TextView is not defined in standard SC methods, but in the view implementation instead (except for [defaultGetDrag](#defaultgetdrag)). It may or may not be overridable by adding your own handlers (see [View / Drag and drop ](../Classes/View.md#drag-and-drop)), depending on the GUI kit in use.


Dragging from TextView will give the selected text in a String as drag data, while dropping will accept any object and insert it [as String](../Classes/Object.md#-asstring) at the drop location.

You can also drag files from outside SuperCollider onto a TextView, and it will insert their URLs at the drop location.

### `defaultGetDrag`
**Returns:** The [selectedString](#selectedstring).

## Examples


```supercollider
(
w = Window.new("Text View Example", Rect(100, Window.screenBounds.height-400, 520, 300)).front;
t = TextView(w.asView, Rect(10, 10, 500, 200))
    .focus(true);
)

// Using the Window you just created, try these in succession, and test how the text view responds
t.mouseUpAction_{ |it, x, y, modifiers, buttonNumber| [x, y].postln };
t.autohidesScrollers_(false);
t.hasVerticalScroller_(false);
t.hasVerticalScroller_(true);
t.hasHorizontalScroller_(false);
t.hasHorizontalScroller_(true);
t.autohidesScrollers_(true);

t.open("Help/GUI/Main-GUI/Button.html"); // load an html file

// selective editing and formatting
t.setStringColor (Color.red, 5, 5);
t.setFont (Font("Courier", 12), 5, 10);
t.setString ("\nA replacement String\n", 12, 6);

// compare with these methods, which change everything
t.font_(Font("Courier", 14));
t.stringColor_(Color.blue);
```




