# Stethoscope

*An oscilloscope*

**Categories:** GUI>Interfaces

**Related:** [ScopeView](../Classes/ScopeView.md), [FreqScope](../Classes/FreqScope.md)

## Description

Stethoscope provides a complete oscilloscope GUI. It displays a window containing a bus-plotting [ScopeView](../Classes/ScopeView.md) and an interface to configure the plotting and choose among the buses.

### Creation by message .scope
Several classes provide a convenient 'scope' method that creates a Stethoscope to display their data. See for example: [Server#-scope](../Classes/Server.md#-scope), [Bus#-scope](../Classes/Bus.md#-scope), [Function#-scope](../Classes/Function.md#-scope).



### Keyboard shortcuts
The following keyboard shortcuts may be used when focused on the Stethoscope display:

| **Shortcut** | **Action** | 
| --- | --- || J | one channel back | | K | switch rate (audio vs. control) | | L | one channel forward | | O | jump to first hardware output channel and adjust numChannels to hardware | | I | jump to first hardware input channel and adjust numChannels to hardware | | space | run, if not running already | | . (period) | stop | | M | toggle screen size | | + / - | zoom horizontally | | * / _ | zoom vertically | | S | change style between parallel and overlay | | Shift+S | change style to lissajou | | Shift+A | allocate buffer size so it fills the screen (to next power of two) (this can be dangerous, might crash) | 



## Class Methods


### `new`
 Create a Stethoscope, either as a window, or placed on a given parent view.**Arguments:**

| Argument | Description |
|----------|-------------|
| `server` | A valid Server (either a local or the internal server), or `nil`, in which case the `Server.default` is used. |  
| `numChannels` | An integer. Default value is 2. |  
| `index` | The offset index. An Integer. Default is nil. |  
| `bufsize` | The size of the analysis buffer. Default is 4096. See also [#-bufsize](#-bufsize). |  
| `zoom` | Horizontal magnification of the displayed wave. Default is 1. See also [#-xZoom](#-xzoom). |  
| `rate` | \audio or \control. Default is \audio. |  
| `view` | The optional parent view. Default is nil. If nil, then it will open in its own Window. |  
| `bufnum` | The id number of the Buffer to analyze. Default value is nil. If nil, then a Buffer of size bufSize is allocated. discussion:  Example:
```supercollider
s.boot
{ SinOsc.ar([330, 440], 0, 0.4) }.play;
Stethoscope(s, 2);
``` |  

### `isValidServer`
 Tests whether Stethoscope can operate on the given server (any local server. See [Server#-isLocal](../Classes/Server.md#-islocal)).**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A [Server](../Classes/Server.md). |  
**Returns:** A Boolean.
### `ugenScopes`
 Returns an array of the running ugen scopes.
```supercollider
s.boot
{ [SinOsc.ar.scope, WhiteNoise.ar(0.5).scope]*0.1 }.scope(2);
Stethoscope.ugenScopes; // returns the ugen scopes
```


### `tileBounds`
 A utility method used by [UGen#-scope](../Classes/UGen.md#-scope) to tile scope windows.**Returns:** A Rect.

## Instance Methods


### Data
### `server`
 The server on which the scope operates.
### `rate`
 Whether to operate on audio or control busses.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | One of the two symbols: `\audio` or `\control`. |  

### `index`
 The starting index of the busses to scope.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Integer. |  

### `numChannels`
 The amount of adjacent busses to scope (from [#-index](#-index) on).**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Integer. |  

### `bufsize`
 Defines the maximum allowed [#-cycle](#-cycle).
### `cycle`

> **Note:** Only available in Qt GUI

 The exact scoping period, in signal frames. Reciprocal to what is also known as *sweep speed* in analog oscilloscopes. It is dynamically adjustable while the scope is running. Data from scoped signals will be accumulated into a buffer until it reaches `cycle` amount frames, at which point the buffering will immediately restart. The view will repeatedly display the entire buffer; it may skip a cycle if the drawing is too slow to keep up with the speed of incoming data, but the cycle boundaries will never shift with respect to signals. If you are scoping a periodic signal, setting `cycle` to match the signal's period will keep the waveform locked in place.

### Display
### `window`
 The (parent) Window of the scope.
### `bounds`
 The position and size of the window. The position is relative to the bottom-left corner of the screen.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A [Rect](../Classes/Rect.md), or any object responding to the [.asRect](../Search.md#asrect) method. The width less than 264 will be changed to 264, the minimum width. |  
**Returns:** A Rect.
```supercollider
s.scope.bounds_(Rect(100, 200, 500, 600));
s.scope.bounds_([100, 200, 500, 600]);
s.scope.bounds_(Size(500, 600));
```


```supercollider
s.scope.bounds_(Rect(0, 0, 500, 600));
s.scope.bounds_(500@600);
```


### `size`
 Sets the width and the height of the scope window.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Integer (the window is square). |  

### `toggleSize`
 Toggle between small and large size.
### `zoom`
 A synonym for [#-xZoom](#-xzoom).
### `xZoom`
 Magnifies the displayed wave horizontally to the given factor. This sets [#-cycle](#-cycle) to `1024 * xZoom.reciprocal`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `yZoom`
 Magnifies the displayed wave vertically to the given factor.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `style`
 The plotting style:- 0 = the channels are vertically spaced
- 1 = the channels are overlaid
- 2 = lissajou; each pair of channels is used for 2D plotting (as streams of x and y coordinates).
**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | One of the above Integers. |  


### Operation
### `run`
 Starts the scope, if not already running.
### `quit`
 Closes the window, and cleans up any used synths and buffers.

### Convenience
### `setProperties`
 Sets several properties at once: [#-numChannels](#-numchannels), [#-index](#-index), [#-bufsize](#-bufsize), [#-zoom](#-zoom), and [#-rate](#-rate).

## Examples


### A step-by-step example

```supercollider
s.boot;
(
{
    SinOsc.ar([225, 450, 900], 0, 0.2)
    + LPF.ar(
        LFPulse.ar(226 * [1, 2, 5], [0, 0.1, 0.1], 0.2, 0.2),
        MouseX.kr(20, 10000, 1)
        )
}.scope;
)

// server.scope only changes the properies explicitly given:

s.scope(numChannels: 5);
s.scope(index: 12);
s.scope(zoom: 4);
s.scope(index: 0);

s.scopeWindow.size = 600;
s.scopeWindow.size = 222;

// scoping buses:

a = Bus.audio(s, 4);
{ WhiteNoise.ar(0.2.dup(4)) }.play(s, a);

a.scope;

c = Bus.control(s, 3);
{ WhiteNoise.kr(1.dup(4) * MouseX.kr) }.play(s, c);

c.scope;

// note that scoping control rate buses shows block size interpolation (this is due to the
// fact that ScopeOut.kr doesn't work yet.)
```




### Multi-channel Lissajou plots

```supercollider
(
{ 
    var f = { |l,h| SinOsc.kr(0.1, {pi.rand}).range(l, h) } ;
    Pulse.ar({ f.(20, 1000) }!6, { f.(0.0, 1) }!6, { f.(0.0, 1.0) }!6) 
}.play;
)

c = s.scope;
c.numChannels = 6;
c.scopeView.waveColors = [Color.red, Color.red, Color.cyan, Color.cyan, Color.white, Color.white];
c.style = 2;
```




### Embedded use
You can pass your own view in to add a stethoscope to it:


```supercollider
w = Window.new("my own scope", Rect(20, 20, 400, 500));
w.view.decorator = FlowLayout(w.view.bounds);
c = Stethoscope.new(s, view: w.view);
w.onClose = { c.free }; // don't forget this
w.front;
```






