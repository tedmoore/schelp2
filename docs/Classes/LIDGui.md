# LIDGui

*A GUI for an LID*

**Categories:** Platform>Linux, External Control>HID

**Related:** [LID](../Classes/LID.md)

## Description

This class creates a simple GUI for an LID device.


## Class Methods

### `new`
Create a new GUI.**Arguments:**

| Argument | Description |
|----------|-------------|
| `device` | An instance of LID, for which to create the GUI. |  


## Instance Methods

### `win`
The window that the LIDGui is in.### `device`
The device for which this GUI is.
## Examples


```supercollider
LID.findAvailable;
LID.postAvailable; // pick one that you want to open, and fill in the vendor and product id in the next line:
d = LID.open(2, 10); // trackpoint

g = LIDGui.new(d);

// or the shortcut method:
g = d.makeGui;
```




