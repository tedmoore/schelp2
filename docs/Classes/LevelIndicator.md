# LevelIndicator

*a level indicator GUI widget*

**Categories:** GUI>Views

**Related:** [RangeSlider](../Classes/RangeSlider.md)

## Description

A level indicator view, suitable for use as a level or peak meter, etc.


## Class Methods



## Instance Methods

### `value`
Get or set the current level of the view.**Arguments:**

| Argument | Description |
|----------|-------------|
| `val` | A [Float](../Classes/Float.md) between 0 and 1. |  
**Returns:** A [Float](../Classes/Float.md)### `warning`
### `critical`
Set the warning and critical thresholds. If meter value is above either threshold, [#-warningColor](#-warningcolor) or [#-criticalColor](#-criticalcolor) will be shown, respectively (by default, yellow and red). If [#-drawsPeak](#-drawspeak) is true warning color will be displayed based on [#-peakLevel](#-peaklevel) rather than value.**Arguments:**

| Argument | Description |
|----------|-------------|
| `val` | A [Float](../Classes/Float.md).
```supercollider
a = LevelIndicator(bounds: Rect(10, 10, 20, 160)).front;
a.value = 0.5;
a.warning = 0.6; a.critical = 0.9;
a.value = 0.7;
a.value = 0.9;
``` |  
### `style`
Sets the style of the view.**Arguments:**

| Argument | Description |
|----------|-------------|
| `val` | An [QLevelIndicatorStyle](../Classes/QLevelIndicatorStyle.md) \continuous or \led (see [#-stepWidth](#-stepwidth))
```supercollider
(
w = Window().front.layout_(
    HLayout(
        LevelIndicator().style_(\continuous).value_(1/3),
        LevelIndicator().style_(\led).value_(2/3),
)
)
)
``` |  
### `stepWidth`
The width of each led light, for \led.**Arguments:**

| Argument | Description |
|----------|-------------|
| `val` | An positive [Integer](../Classes/Integer.md).
```supercollider
(
w = Window().front.layout_(HLayout(
    LevelIndicator().style_(\led).value_(0.8).stepWidth_(1),
    LevelIndicator().style_(\led).value_(0.8).stepWidth_(3),
    LevelIndicator().style_(\led).value_(0.8).stepWidth_(10),
    LevelIndicator().style_(\led).value_(0.8).stepWidth_(50),
));
)
``` |  
### `numSteps`
The number of steps used in \led style.**Arguments:**

| Argument | Description |
|----------|-------------|
| `val` | An positive [Integer](../Classes/Integer.md).
```supercollider
(
a = LevelIndicator(bounds: Rect(10, 10, 80, 400)).front();
a.value = 1;
a.style = \led;
a.numSteps = 4;
)
``` |  
### `image`

> **Note:** Not yet implemented in Qt GUI

**Arguments:**

| Argument | Description |
|----------|-------------|
| `image` | An [Image](../Classes/Image.md). The default image is the SC cube. |  
### `numTicks`
The number of ticks to display in the view's scale.**Arguments:**

| Argument | Description |
|----------|-------------|
| `number` | An [Integer](../Classes/Integer.md) >= 0.
```supercollider
(
w = Window(bounds: 100@400).front().background_(Color.black);
w.layout_(HLayout(
    LevelIndicator()
        .numTicks_(16)
        .value_(0.75)
))
)
``` |  
### `numMajorTicks`
The number of ticks in the view's scale which will be large sized.**Arguments:**

| Argument | Description |
|----------|-------------|
| `number` | An [Integer](../Classes/Integer.md) >= 0.
```supercollider
(
w = Window(bounds: 100@400).front().background_(Color.black);
w.layout_(HLayout(
    LevelIndicator()
        .numMajorTicks_(16)
        .numTicks_(16)
        .value_(0.75)
))
)
``` |  
### `drawsPeak`
Determines whether the view draws a separate peak display. This can be useful for displaying both peak and RMS values. If drawsPeak is true [#-warning](#-warning) and [#-critical](#-critical) will be displayed based on [#-peakLevel](#-peaklevel) rather than value.**Arguments:**

| Argument | Description |
|----------|-------------|
| `bool` | A [Boolean](../Classes/Boolean.md). By default the peak is not drawn.
```supercollider
(
w = Window().front().layout_(HLayout(
    LevelIndicator().style_(\continuous).value_(0.75).drawsPeak_(true).peakLevel_(0.9),
    LevelIndicator().style_(\led).value_(0.75).drawsPeak_(true).peakLevel_(0.9)
))
)
``` |  
### `peakLevel`
Sets the level of the peak display. (See [#-drawsPeak](#-drawspeak).)**Arguments:**

| Argument | Description |
|----------|-------------|
| `val` | A [Float](../Classes/Float.md).
```supercollider
(
w = Window().front().layout_(HLayout(
    LevelIndicator().style_(\continuous).value_(0.1).drawsPeak_(true).peakLevel_(0.3),
    LevelIndicator().style_(\continuous).value_(0.1).drawsPeak_(true).peakLevel_(0.5),
    LevelIndicator().style_(\continuous).value_(0.1).drawsPeak_(true).peakLevel_(0.7),
    LevelIndicator().style_(\continuous).value_(0.1).drawsPeak_(true).peakLevel_(0.9),
))
)
``` |  
### `meterColor`
### `warningColor`
### `criticalColor`
Sets the color of the meter, as well as the warning and critical colors.**Arguments:**

| Argument | Description |
|----------|-------------|
| `color` | A [Color](../Classes/Color.md).
```supercollider
(
l = LevelIndicator(bounds: Rect(100, 100, 100, 400)).front().value_(1).style_(\led);
l.meterColor = Color.blue(0.9);
l.warningColor = Color.blue(0.7);
l.criticalColor = Color.blue(0.5);
)
```


```supercollider
(
// inverse
l.background = Color.blue;
l.meterColor = Color.black.alpha_(1);
l.warningColor = Color.black.alpha_(1);
l.criticalColor = Color.black.alpha_(0.3);
)
``` |  

## Examples


```supercollider
(
// something to meter
s.waitForBoot({
b = Buffer.read(s, ExampleFiles.child);

    x = {
        var colum, noise, imp, delimp, mul = 1;
    imp = Impulse.kr(10);
    delimp = Delay1.kr(imp);
    colum = PlayBuf.ar(1, b, BufRateScale.kr(b), loop: 1) * mul;
    // measure rms and Peak
    SendReply.kr(imp, '/levels', [Amplitude.kr(colum), K2A.ar(Peak.ar(colum, delimp).lag(0, 3))]);
    colum;
}.play;

    a = LevelIndicator(bounds: Rect(100, 100, 100, 400)).front;
    a.onClose_({ x.free; o.free });
o = OSCFunc({ |msg|
    {
        a.value = msg[3].ampdb.linlin(-40, 0, 0, 1);
        a.peakLevel = msg[4].ampdb.linlin(-40, 0, 0, 1);
    }.defer;
}, '/levels', s.addr);
})
)

(
a.warning = -6.dbamp;
a.critical = -3.dbamp;
)
// optionally show peak level
a.drawsPeak = true;

(
a.style = \led;
a.stepWidth = 3;
)

// different colors
(
a.meterColor = Color.blue(0.9);
a.warningColor = Color.blue(0.8);
a.criticalColor = Color.blue(0.6);
)
// all styles can have ticks
(
a.background = Color.clear;
a.numTicks = 11; // includes 0;
)

// Single blinking square level indicator
(
a.style = \led;
a.numTicks = 0;
a.drawsPeak = false;
a.bounds = a.bounds.resizeTo(90, 90);
a.numSteps = 1;
)
```




