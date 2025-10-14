# ServerMeter

*Graphical feedback window showing input/output levels*

**Categories:** GUI>Interfaces

**Related:** [Stethoscope](../Classes/Stethoscope.md), [FreqScope](../Classes/FreqScope.md), [ServerMeterView](../Classes/ServerMeterView.md)

## Description

A ServerMeter is a simple graphical display showing the volume levels of inputs and outputs on the server.
Also see: [Server#-meter](../Classes/Server.md#-meter)


## Class Methods

### `new`
Create a new ServerMeter.**Arguments:**

| Argument | Description |
|----------|-------------|
| `server` | The [Server](../Classes/Server.md) whose inputs and outputs you wish to visualize. |  
| `numIns` | The number of inputs you want to display (starts counting at the first input bus, similar to [SoundIn](../Classes/SoundIn.md)) |  
| `numOuts` | The number of outputs you want to display (starts counting at bus 0) |  
**Returns:** A reference to the newly created ServerMeter

## Instance Methods

### `window`
Get a reference to the [Window](../Classes/Window.md) of this ServerView**Returns:** a [Window](../Classes/Window.md) reference### `meterView`
Get a reference to the [ServerMeterView](../Classes/ServerMeterView.md) of this ServerView**Returns:** a [ServerMeterView](../Classes/ServerMeterView.md) reference
> **Note:** A ServerMeter encapsulates both a [Window](../Classes/Window.md) and a [ServerMeterView](../Classes/ServerMeterView.md) within that Window. For more information about Windows and views see [GUI-Introduction#Basic elements: Windows, views and containers](../Guides/GUI-Introduction.md#basic-elements:-windows,-views-and-containers)

### `position`
the position of the [ServerMeter](../Classes/ServerMeter.md) window. The value should be a [Point](../Classes/Point.md), e.g. `x@y`, or respond to `.asPoint`. E.g.: setting the position to `150@50` places the bottom left corner of the meter window 150 pixels from the left and 50 pixels up from the bottom of the screen.
## Examples


```supercollider
s = Server.internal; // use the internal server
s.boot;

// display 4 input channels & main stereo output
m = ServerMeter.new(s, 4, 2);

// Query the current window position
m.position  // -> Point(5.0, 277.0)

// Query the current window bounds
m.window.bounds

// Set/Get the ServerMeter's screen position by the bottom left corner of its window
m.position_(0@100);
m.position // -> Point(0.0, 100.0)

// Retrieve the moved new window bounds
m.window.bounds
```




