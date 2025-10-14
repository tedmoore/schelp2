# SoundFileView

*Sound file display*

**Categories:** GUI>Views

**Related:** [SoundFile](../Classes/SoundFile.md)

## Description

A sound file viewer with numerous options.
Zoom in and out using Shift + right-click + mouse-up/down;
Scroll using right-click + mouse-left/right.


## Class Methods



## Instance Methods


### Data
### `soundfile`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Instance of SoundFile to display. |  

### `read`
 Reads a section of the [soundfile](#soundfile) and displays it in the view. For large files, you may want to use readWithTask instead. The 'block' argument has no effect; the display resolution is infinite.**Arguments:**

| Argument | Description |
|----------|-------------|
| `startFrame` | The beginning of the section, in frames. |  
| `frames` | The size of the section, in frames. |  
| `block` | The block size - visual resolution of the display. An Integer of the form 2**n. |  
| `closeFile` | If true, closes the SoundFile after reading. |  
| `doneAction` | A Function called when the file reading has completed. |  

### `readFile`
 Reads a section of an open instance of SoundFile, and displays it in the view. For large files, you may want to use the method readWithTask instead. The 'block' argument has no effect; the display resolution is infinite.**Arguments:**

| Argument | Description |
|----------|-------------|
| `aSoundFile` | An open instance of SoundFile. |  
| `startFrame` | The beginning of the section, in frames. |  
| `frames` | The size of the section, in frames. |  
| `block` | The block size - visual resolution of the display. An Integer of the form 2**n. |  
| `closeFile` | If true, closes the SoundFile after reading. |  
| `doneAction` | A Function called when the file reading has completed. |  

### `readWithTask`
 Reads a section of the [soundfile](#soundfile) asynchronously (in the background), updating the [readProgress](#readprogress) along the way. If the `showProgress` argument is `true`, a SoundFileViewProgressWindow opens to show the progress. The 'block' argument has no effect; the display resolution is infinite. The 'showProgress' argument has no effect; the view always displays reading progress within itself.**Arguments:**

| Argument | Description |
|----------|-------------|
| `startFrame` | The beginning of the section, in frames. |  
| `frames` | The size of the section, in frames. |  
| `block` | The block size - visual resolution of the display. An Integer of the form 2**n. |  
| `doneAction` | An optional function to be evaluated on completion. |  
| `showProgress` | Whether to open a progress window. Defaults to `true`. |  

### `readFileWithTask`
 Reads a section of an open instance of SoundFile asynchronously (in the background), updating the [readProgress](#readprogress) along the way. If the `showProgress` argument is `true`, a SoundFileViewProgressWindow opens to show the progress. The 'block' argument has no effect; the display resolution is infinite.  The 'showProgress' argument has no effect; the view always displays reading progress within itself.**Arguments:**

| Argument | Description |
|----------|-------------|
| `soundFile` | An open instance of SoundFile. |  
| `startFrame` | The beginning of the section, in frames. |  
| `frames` | The size of the section, in frames. |  
| `block` | The block size - visual resolution of the display. An Integer of the form 2**n. |  
| `doneAction` | An optional function to be evaluated on completion. |  
| `showProgress` | Whether to open a progress window. Defaults to `true`. |  

### `data`
 Sets custom data instead of a sound file. This is a setter only; it is not possible to get the data. If you need access to the data, you must keep it in your own variable. Setting this property assumes 1 channel and sample rate of 44100 Hz. Use [setData](#setdata) instead if you want more control.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Array of Floats; multiple channel data should be interleaved. |  

### `setData`
 Sets custom display data instead of a sound file, interpreting it using specified number of channels and sample rate.**Arguments:**

| Argument | Description |
|----------|-------------|
| `data` | An Array of Floats; multiple channel data should be interleaved. |  
| `block` | The block size - visual resolution of the display. An Integer of the form 2**n. (since the port to QT, the 'block' argument has no effect; the display resolution is infinite). |  
| `startFrame` | An integer. |  
| `channels` | An integer. |  
| `samplerate` | An integer. |  

### `alloc`
Allocates a desired amount of display channels and frames; all frames have initial value of 0.**Arguments:**

| Argument | Description |
|----------|-------------|
| `frames` | An Integer. |  
| `channels` | An Integer. |  
| `samplerate` | An Integer. |  

### `set`
Overwrites a range of display data with another data. This method can be used after [alloc](#alloc) or [setData](#setdata) has been called, but not while the view is displaying a sound file.**Arguments:**

| Argument | Description |
|----------|-------------|
| `offset` | The frame at which to start overwriting; an Integer. |  
| `data` | The new data; an Array of Floats; multiple channel data should be interleaved. |  

### `startFrame`
 The beginning of the read section of the soundfile, or 0 if [alloc](#alloc) or [setData](#setdata) has been used.
### `numFrames`
 The total amount of frames in the view; this is unrelated to [zooming](#zoom) and [scrolling](#scroll).
### `readProgress`
 The reading progress, updated periodically when reading a soundfile using [readWithTask](#readwithtask) or [readFileWithTask](#readfilewithtask).

### Navigation
### `viewFrames`
 The amount of currently visible frames in the view.
### `zoom`
 Zooms by a factor relative to current zoom.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `zoomToFrac`
 Zooms to a specific scale.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `zoomAllOut`
 Zooms to the [current selection](#currentselection).
### `zoomSelection`
 Zooms to a specific selection.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | The index of the selection; an Integer between 0 an 63. |  

### `xZoom`
 The number of seconds of audio to display in the view. E.g., to zoom out by a factor of 2, `view.xZoom = dataDuration / 2`. (You are responsible for keeping track of the data duration.)**Returns:** A Float, in seconds of audio displayed.
### `yZoom`
 Vertical scaling. The default `yZoom = 1` sets ±1.0 to the top and bottom of the view. If `yZoom = 2`, the view covers ±0.5 of the value range.**Returns:** A Float scaling factor.
### `yOffset`
 Vertical offset. The default `yOffset = 0` sets value of 0.0 in the middle of the channel's view, while `yOffset = 1`, sets 0.0 at the top and `yOffset = -1` sets 0.0 at the bottom of the view. This is performed after (and thus is not scaled by) the [yZoom](#yzoom) factor.**Returns:** A Float offset.
### `spacing`
 A ratio between vertical space outside of the ±1.0 value range and channel's full height. The default `spacing = 0.1` makes top and bottom spaces add up to `0.1 * height` (each of them occupying half of that), while ±1.0 value range occupies `0.9 * height`. The value is clipped in the range from `0.0` to `1.0`.**Returns:** A Float scaling factor.
### `scrollPos`
 The scrolling position of the view, as a fraction of the total scrolling range. The total scrolling range is `totalDuration - xZoom`.**Returns:** A Float in the range of 0.0 to 1.0.
### `scrollTo`
 Scrolls to a fraction of the total scrolling range. The total scrolling range is `totalDuration - xZoom`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float in the range of 0.0 to 1.0. |  

### `scroll`
 Scrolls by a fraction of the visible range.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  

### `scrollToStart`
 Scrolls to the beginning.
### `scrollToEnd`
 Scrolls to the end.

### Selection
### `selections`
 All the selections.**Returns:** An array of 64 arrays of start frames and sizes: [[start0, size0], [start1, size1], ...].
### `selection`
 The selection at index.**Returns:** An Array of the form `[start, size]`, where start and size denote frames.
### `setSelection`
 Sets the selection at index.**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | An Integer between 0 an 63. |  
| `selection` | An Array of the form `[start, size]`, where start and size are Integers and denote frames. |  

### `currentSelection`
 The index of the current selection**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An integer between 0 an 63. |  

### `selectionStart`
 The start frame of a selection.**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | The index of the selection; an Integer between 0 an 63. |  
**Returns:** An Integer.
### `setSelectionStart`
 Sets the start frame of a selection.**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | The index of the selection; an Integer between 0 an 63. |  
| `frame` | The starting frame of the selection, an Integer. |  

### `selectionSize`
 The size of a selection.**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | The index of the selection; an Integer between 0 an 63. |  
**Returns:** An Integer.
### `setSelectionSize`
 Sets the size of a selection.**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | The index of the selection; an Integer between 0 an 63. |  
| `frames` | The size in frames of the selection, an Integer. |  

### `selectionStartTime`
 The start of a selection in seconds.**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | The index of the selection; an Integer between 0 an 63. |  
**Returns:** A Float.
### `selectionDuration`
 The size of a selection in seconds.**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | The index of the selection; an Integer between 0 an 63. |  
**Returns:** A Float.
### `selectAll`
 Sets a selection to span the whole data range.**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | The index of the selection; an Integer between 0 an 63. |  

### `selectNone`
 Sets the size of a selection to 0.**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | The index of the selection; an Integer between 0 an 63. |  

### `setSelectionColor`
 Sets the color of a selection.**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | The index of the selection; an Integer between 0 an 63. |  
| `color` | A Color. |  

### `setEditableSelectionStart`
 Sets whether the start point of a selection can be edited.**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | The index of the selection; an Integer between 0 an 63. |  
| `editable` | A Boolean. |  

### `setEditableSelectionSize`
 Whether the end point of a selection can be edited.**Arguments:**

| Argument | Description |
|----------|-------------|
| `index` | The index of the selection; an Integer between 0 an 63. |  
| `editable` | A Boolean. |  

### `readSelection`

> **Note:** Not implemented

 Read the data within a selection.**Arguments:**

| Argument | Description |
|----------|-------------|
| `block` | The block size - visual resolution of the display. An Integer of the form 2**n. |  
| `closeFile` | If true, closes the SoundFile after reading. |  

### `readSelectionWithTask`

> **Note:** Not implemented

 Read the data within the current selection asynchronously (in the background), showing the progress in a separate window.

### Display
### `peakColor`
 The color of the peak-to-peak data. This can be overridden by [waveColors](#wavecolors). Defaults to `Color(0.95, 0.7)`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A `Color`. |  

### `rmsColor`
 The color of the RMS data. Defaults to `Color(1.0, 1.0)`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A `Color`. |  

### `waveColors`
 An array of colors for the peak-to-peak data for each channel, allowing each channel to be represented by a different color. Defaults to `[]`. Once set, it overrides [peakColor](#peakcolor). In order to revert to using `.peakColor`, set `.waveColors` back to an empty array: `.waveColors_([])`.
> **Note:** [rmsColor](#rmscolor) stays the same for all channels. However, using alpha blending, it is possible to display RMS data using either a lighter (e.g. `.rmsColor_(Color.grey(1, 0.3))`) or a darker (e.g. `.rmsColor_(Color.grey(0, 0.3))`) shade of the peak-to-peak color.

**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | And array of `[Color]`. |  

### `gridOn`
 Whether the grid is displayed. Defaults to `true`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `gridResolution`
 The resolution of the grid.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An instance of Float. |  

### `gridOffset`
 Sets the grid offset.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | Grid blocks are offset by this value (in seconds). |  

### `gridColor`
 The color of the grid.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  

### `drawsWaveForm`
 Whether the data is displayed. Defaults to `true`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `drawsRMS`
 Whether the RMS data for the waveform is displayed. Defaults to `true`.
### `drawsCenterLine`
 Whether the center line (at value 0.0) is displayed. Defaults to `true`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `drawsBoundingLines`
 Whether the bounding lines (at values ±1.0) are displayed. Defaults to `true`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `timeCursorOn`
 Whether the time cursor is displayed. Defaults to `false`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `timeCursorPosition`
 The position of the time cursor in frames.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Integer. |  

### `timeCursorColor`
 The color of the time cursor.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  

### `elasticMode`
 Not operational, for compatibility only.

### Actions
### `action`
 The object to be evaluated whenever the user interacts with the view.
### `metaAction`
 The object to be evaluated on Ctrl + click.

## Examples


### Basic example

```supercollider
// To zoom in/out: Shift + right-click + mouse-up/down
// To scroll: right-click + mouse-left/right
(
w = Window.new("soundfile test", Rect(200, 300, 740, 100));
a = SoundFileView.new(w, Rect(20, 20, 700, 60));

f = SoundFile.new;
// ExampleFiles helps locate audio files used in examples
p = ExampleFiles.child;
// peek at the path to see location and the format of a path
p.postln;
f.openRead(p);
f.inspect;

a.soundfile = f;
a.read(0, f.numFrames);

a.timeCursorOn = true;
a.timeCursorColor = Color.red;
a.timeCursorPosition = 2050;
a.drawsWaveForm = true;
a.gridOn = true;
a.gridResolution = 0.2;

w.front;
)
```




### Step by step examples

```supercollider
( // make a simple SoundFileView
y = Window.screenBounds.height - 120;
w = Window.new("soundfile test", Rect(200, y, 740, 100)).alwaysOnTop_(true);
w.front;
a = SoundFileView.new(w, Rect(20, 20, 700, 60));

f = SoundFile.new;
f.openRead(ExampleFiles.child);
// f.inspect;

a.soundfile = f;            // set soundfile
a.read(0, f.numFrames);     // read in the entire file.
a.refresh;                  // refresh to display the file.
)

// To zoom in/out: Shift + right-click + mouse-up/down
// To scroll: right-click + mouse-left/right

// reading file
a.read(0, f.numFrames / 2).refresh; // read first half
a.read.refresh;                     // read entire file by default
a.read(f.numFrames / 2).refresh;    // read second half
a.read(0, -1).refresh;              // -1 also reads entire file, like buffer.

// the resolution of the view is always infinite;
// you can always zoom in until you see a single sample.

a.read(0, -1).refresh;

// for longer files, you can use:
a.readWithTask;

// zoom is relative
a.zoom(0.2).refresh;
a.zoom(2).refresh;
a.zoom(2).refresh;
a.zoomToFrac(0.5); // zoom to half file size
a.zoomAllOut;

a.gridOn = true;            // time grid, 1 second by default,
a.gridResolution = 0.2;     // or set resolution in seconds
a.gridColor = Color.cyan;   // color is changeable.
a.gridOffset_(0.1);         // not sure if this is working?

a.timeCursorOn = true;          // a settable cursor
a.timeCursorPosition = 2050;    // position is in frames.
a.timeCursorColor = Color.white;

// toggle drawing on/off
a.drawsWaveForm = false;
a.drawsWaveForm = true;

// these methods should return view properties:
a.gridOn
a.gridResolution
a.gridColor
a.timeCursorOn
a.timeCursorPosition
a.timeCursorColor

// Selections: multiple selections are supported.
// e.g. use selection 0:
a.setSelectionColor(0, Color.red);  // set...(index, value)
a.selectionStart(0);                // at index
a.setSelectionStart(0, 12345);
a.setSelectionSize(0, 12345);

a.setSelectionStart(0, 1234);
a.selectionStart(0);

// now selection 1
a.setSelectionColor(1, Color.white);
a.setSelectionStart(1, 1234).setSelectionSize(1, 1234 * 2);
a.selectionStart(1);
a.setSelectionStart(0, 12345);

// the current selection gets changed when click/dragging in view.
a.currentSelection;     // index of current selection;
a.currentSelection_(1); // switch current selection - try click/drag white now.
a.currentSelection;

a.selections.size;      // 64 selections
a.selections[0];
a.selections[1];
a.selections;

// setSelection (index, selection);
a.setSelection(0, [234, 2345]);
a.selection(1); // returns [start, size].

(       // mouseUpAction
a.mouseUpAction = {
    ("mouseUp, current selection is now:"
        + a.selections[a.currentSelection]).postln;
};
)
// lock selection 0:
a.currentSelection_(0);
a.setEditableSelectionStart(0, false);
a.setEditableSelectionSize(0, false);


// unlock selection 0:
a.setEditableSelectionStart(0, true);
a.setEditableSelectionSize(0, true);

a.selectionStartTime(0);
a.selectionDuration(0);


a.setSelectionStart(0, 12345);
a.setSelectionSize(0, 12345);
a.readSelection.refresh;
a.readSelection(16).refresh;    // in higher resolution
a.read.refresh;                 // go back to entire file.


a.dataNumSamples;   // visual data have this many points
a.data.plot;
a.setData(a.data.reverse);


a.zoom(0.25);       // scrolling is normalized
a.scrollTo(0.5);    //
a.scrollTo(0.6);    //
a.scroll(12);       // scroll is in viewFrames.

a.zoom(4);

w.close;
```




### Adding a scroll bar
Zooming and scrolling by mouse, directly in a SoundFileView, may not be immediately intuitive. (Most users wouldn't guess to shift-right-click!) You can add a [RangeSlider](../Classes/RangeSlider.md) to act as a scrollbar.

Notes:

- If the user shift-right-clicks, the only way to track the SoundFileView's display changes is by using mouse actions: [View#-mouseDownAction](../Classes/View.md#-mousedownaction) and [View#-mouseUpAction](../Classes/View.md#-mouseupaction) to know which button is pressed, and [View#-mouseMoveAction](../Classes/View.md#-mousemoveaction) to read the new scrolling and zooming values.
- [SoundFileView#-xZoom](../Classes/SoundFileView.md#-xzoom) is in seconds, while the range slider is normalized to a 0-1 range. So `xZoom == slider.range * duration`, and `slider.range == xZoom / duration`.
- [SoundFileView#-scrollPos](../Classes/SoundFileView.md#-scrollpos) is normalized to the "total scrolling range," where 1.0 is scrolled fully to the right. We have to subtract the displayed area: `slider.lo = sfv.scrollPos / (1 - slider.size)`, with some refinements to avoid division by 0.



```supercollider
p = ExampleFiles.child;
f = SoundFile.openRead(p);
f.readData(d = Signal.newClear(f.numFrames * f.numChannels));
f.close;

(
var w = Window("test", Rect(700, 200, 600, 300)),
sfv, sfZoom, mouseButton,
dur = d.size / f.sampleRate / f.numChannels;

w.layout = VLayout(
    sfv = SoundFileView(),
    sfZoom = RangeSlider().orientation_(\horizontal)
);

sfZoom.lo_(0).range_(1)
.action_({ |view|
    var divisor, rangeStart;
    rangeStart = view.lo;
    divisor = 1 - sfZoom.range;
    if(divisor < 0.0001) {
        rangeStart = 0;
        divisor = 1;
    };
    sfv.xZoom_(sfZoom.range * dur)
    .scrollTo(rangeStart / divisor)
});

sfv.setData(d, startFrame: 0, channels: f.numChannels, samplerate: f.sampleRate);

sfv.mouseDownAction_({ |view, x, y, mod, buttonNumber|
    mouseButton = buttonNumber;
})
.mouseUpAction_({ |view, x, y, mod|
    mouseButton = nil;
})
.mouseMoveAction_({ |view, x, y, mod|
    var rangeSize, rangeStart;
    if(mouseButton == 1) {
        rangeSize = view.xZoom / dur;
        rangeStart = view.scrollPos * (1 - rangeSize);
        sfZoom.lo_(rangeStart).range_(rangeSize);
    };
});

w.front;
)
```






