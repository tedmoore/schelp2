# ServerMeterView

*A GUI widget that displays input/output levels*

**Categories:** GUI>Views

**Related:** [ScopeView](../Classes/ScopeView.md), [FreqScopeView](../Classes/FreqScopeView.md), [ServerMeter](../Classes/ServerMeter.md)

## Description

A [ServerMeterView](../Classes/ServerMeterView.md) is a modular widget for showing the volume levels of inputs/outputs on the server. [ServerMeterView](../Classes/ServerMeterView.md) can be embedded inside of your custom graphical user interfaces just like a button or slider.

> **Note:** If you are looking for a quick input/output levels display without having to build your own GUI from scratch, see [ServerMeter](../Classes/ServerMeter.md) and [Server#-meter](../Classes/Server.md#-meter)




## Class Methods

### `height`
Get the height in pixels of the standard [ServerMeterView](../Classes/ServerMeterView.md) widget**Returns:** an [Integer](../Classes/Integer.md)
### `getWidth`
Get the width in pixels of a [ServerMeterView](../Classes/ServerMeterView.md) widget with the given number of inputs and outputs**Arguments:**

| Argument | Description |
|----------|-------------|
| `numIns` | number of inputs used to calculate the width |  
| `numOuts` | number of outputs used to calculate the width |  
| `server` | the server |  
**Returns:** an [Integer](../Classes/Integer.md)
### `new`
Create a new [ServerMeterView](../Classes/ServerMeterView.md) instance**Arguments:**

| Argument | Description |
|----------|-------------|
| `aserver` | The [Server](../Classes/Server.md) whose inputs/outputs will be monitored |  
| `parent` | The parent [View](../Classes/View.md) or [Window](../Classes/Window.md) where the new [ServerMeterView](../Classes/ServerMeterView.md) will be embedded. |  
| `leftUp` | Where to position the new [ServerMeterView](../Classes/ServerMeterView.md) inside the parent. **leftUp** must be a [Point](../Classes/Point.md), describing where to place the upper left corner of the new [ServerMeterView](../Classes/ServerMeterView.md). |  
| `numIns` | The number of inputs to monitor |  
| `numOuts` | The number of outputs to monitor |  
**Returns:** A new [ServerMeterView](../Classes/ServerMeterView.md)

## Instance Methods

### `view`
get the [CompositeView](../Classes/CompositeView.md) used to construct the various elements of the [ServerMeterView](../Classes/ServerMeterView.md) widget**Returns:** a [CompositeView](../Classes/CompositeView.md)### `remove`
Removes this [ServerMeterView](../Classes/ServerMeterView.md) from its parent view (if any) and then destroys it. Once this method is called you can no longer use this [ServerMeterView](../Classes/ServerMeterView.md).### `start`
Enable the monitoring of input/outputs**Returns:** this [ServerMeterView](../Classes/ServerMeterView.md)### `stop`
Disable the monitoring of input/outputs**Returns:** this [ServerMeterView](../Classes/ServerMeterView.md)
## Examples


### Simple Usage

```supercollider
// make a window and embed a ServerMeterView inside of it.
w = Window.new("Server Levels");
ServerMeterView.new(s, w, 0@0, 2, 2);
w.front; // show the window
```




### A More Complex Example

```supercollider
// make a GUI to monitor two servers running simultaneously
s = Server.local;
q = Server.internal;
s.boot; q.boot; // wait a moment for the servers to boot

// make a window big enough to hold 2 ServerMeterViews
r = Rect(0, 0, ServerMeterView.getWidth(2, 2) * 2, ServerMeterView.height)
w = Window.new("Local | Internal", r);

// make one ServerMeterView to monitor the input/output of each server
ServerMeterView.new(s, w, Point(0, 0), 2, 2);
ServerMeterView.new(q, w, Point(ServerMeterView.getWidth(2, 2), 0), 2, 2);
w.front; // show the window
```






