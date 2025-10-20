# QPalette

*Set of colors used by the GUI*

**Categories:** GUI>Accessories

## Description

QPalette is a **set of colors** that the GUI system uses to draw the views. The colors are organized into three **color groups** (active, inactive and disabled) used according to the state of the views drawn, and each group containing one color assigned to each of the various **color roles** (window, windowText, button, buttonText, etc.), used to draw distinct elements of the views. See [palette_color_roles](../Reference/palette_color_roles.md) and [palette_color_groups](../Reference/palette_color_groups.md) for details.
A palette can be assigned to the whole GUI using [QtGUI#*palette](../Classes/QtGUI.md#*palette), or to a particular view using [View#-palette](../Classes/View.md#-palette). Views will inherit a palette from their parent, and ultimately QtGUI, unless a palette is explicitly assigned to them. Moreover, when setting a palette on a view, it will be combined with the inherited one, overriding only those colors that have been explicitly set on the palette (see [#-hasColor](#-hascolor)). Hence, assigning a new and unmodified palette will reset all the colors to the inherited ones.
There are also two predefined palettes accessible using [#*light](#*light) and [#*dark](#*dark). The light palette is assigned to QtGUI by default on startup. Should you wish to use a palette that matches the color scheme used natively on your platform, you can access such palette using [#*system](#*system).
If you wish to design your own palette, it is most convenient to use [#*auto](#*auto), which will automatically derive a palette from only two colors, and then modify the details as you see fit.
Note that in Qt GUI most color-related methods of views (like [Window#-background](../Classes/Window.md#-background), [Slider#-knobColor](../Classes/Slider.md#-knobcolor), etc.) actually modify the view's palette.


## Class Methods


### `new`
 Instantiates a new palette, equivalent to the global palette assigned to QtGUI. All colors are considered to not be set (see [#-hasColor](#-hascolor)).

### `auto`
 Instantiates a new palette, with colors automatically derived from the given colors for 'button' and 'window' color roles. All colors are considered to be set (see [#-hasColor](#-hascolor)).**Arguments:**

| Argument | Description |
|----------|-------------|
| `buttonColor` | The Color assigned to the button role. |  
| `windowColor` | The Color assigned to the window role. |  


### `light`
 A predefined palette using light colors. All colors are considered to be set (see [#-hasColor](#-hascolor)).

### `dark`
 A predefined palette using dark colors. All colors are considered to be set (see [#-hasColor](#-hascolor)).

### `system`
 The native system palette. All colors are considered to be set (see [#-hasColor](#-hascolor)).

## Instance Methods


### `color`
 Returns the color assigned to a color role within a color group.**Arguments:**

| Argument | Description |
|----------|-------------|
| `role` | A symbol among [palette_color_roles](../Reference/palette_color_roles.md). |  
| `group` | A symbol among [palette_color_groups](../Reference/palette_color_groups.md), or nil, in which case the current color group is used. |  

### `setColor`
 Assigns a color to a color role within a color group.**Arguments:**

| Argument | Description |
|----------|-------------|
| `color` | A Color. |  
| `role` | A symbol among [palette_color_roles](../Reference/palette_color_roles.md). |  
| `group` | A symbol among [palette_color_groups](../Reference/palette_color_groups.md), or nil, in which case the color will be assigned to all groups. |  

### `hasColor`
 Whether the color belonging to a color role and group has been set on this QPalette instance. When setting a palette on a view, only colors for which this methods returns true will be changed, others will be inherited from the parent view (or QtGUI if this view has no parent).**Arguments:**

| Argument | Description |
|----------|-------------|
| `role` | A symbol among [palette_color_roles](../Reference/palette_color_roles.md). |  
| `group` | A symbol among [palette_color_groups](../Reference/palette_color_groups.md). |  

### `window`
 Convenience method to get or set the color for the 'window' role.
### `windowText`
 Convenience method to get or set the color for the 'windowText' role.
### `button`
 Convenience method to get or set the color for the 'button' role.
### `buttonText`
 Convenience method to get or set the color for the 'buttonText' role.
### `base`
 Convenience method to get or set the color for the 'base' role.
### `baseText`
 Convenience method to get or set the color for the 'baseText' role.
### `highlight`
 Convenience method to get or set the color for the 'highlight' role.
### `highlightText`
 Convenience method to get or set the color for the 'highlightText' role.

