# QtGUI

*Top-level controls for Qt GUI*

**Categories:** GUI

## Description

QtGUI provides top-level control for the Qt GUI bindings and some platform-level functionality.


## Class Methods









### `availableStyles`
Returns an array of all available styles on this platform. For use with [#-style](#-style).

### `cursorPosition`
Gets the current position of the cursor as a [Point](../Classes/Point.md).

### `debugLevel`
Gets or sets the verbosity level for debug output from "QtCollider" code. SuperCollider must have been built in debug mode for messages to appear. Valid values are -1 (none), 0 (warnings only, default), 1 (most messages), and 2 (verbose). Values outside this range are effectively clipped.

### `focusView`
Gets the currently focused view.

### `palette`
Gets or sets the [QPalette](../Classes/QPalette.md) used for GUI display.

### `selectedText`
Gets the selected text in the currently focused view. If there is no such string then return empty string.Internally, first calls `selectedText` if that method is available; otherwise, calls `selectedString` if that method is available. Otherwise, returns empty string.

### `stringBounds`
Returns a [Rect](../Classes/Rect.md) representing the size of the smallest rectangle that could contain a given string rendered with the given font.
```
QtGUI.stringBounds("hellooo", Font(Font.defaultSansFace, 100))
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `aString` | A [String](../Classes/String.md) to render. |  
| `aFont` | An instance of [Font](../Classes/Font.md). |  


### `style`
Gets or sets the current GUI style. The given style must be a [String](../Classes/String.md) or [Symbol](../Classes/Symbol.md) that names one of the styles returned by [#-availableStyles](#-availablestyles).

