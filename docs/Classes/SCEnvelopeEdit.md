# SCEnvelopeEdit

*An envelope editor view*

**Categories:** GUI>Kits>Cocoa

**Related:** [EnvelopeView](../Classes/EnvelopeView.md)

## Description

An editable Envelope view.

### Some Important Issues Regarding SCEnvelopeEdit
The breakpoints are color coded as follows:

| blue | normal | 
| --- | --- || red | sustain node | | green | loop node | 



## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `parent` | The parent view. |  
| `bounds` | An instance of [Rect](../Classes/Rect.md), or a [Point](../Classes/Point.md) indicating `width@height`. |  
| `env` | The envelope. An instance of [Env](../Classes/Env.md). |  
| `pointsPerSegment` | The resolution in points per segment. Default value is 10. |  

### `paletteExample`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `parent` |  |  
| `bounds` |  |  


### Subclassing and Internal Methods
The following methods are usually not used directly or are called by a primitive. Programmers can still call or override these as needed.

### `viewClass`



## Instance Methods

### `refresh`
If the [Env](../Classes/Env.md) object is modified directly, this needs to be called to update the GUI.method: maxLevel Changes maximum level shown in editor.**Arguments:**

| Argument | Description |
|----------|-------------|
| `level` | An instance of [Float](../Classes/Float.md). |  
### `minLevel`
Changes minimum level shown in editor.**Arguments:**

| Argument | Description |
|----------|-------------|
| `level` | An instance of [Float](../Classes/Float.md). |  
### `minTime`
Changes minimum time (sec) shown in editor. Negative times are okay because [Env](../Classes/Env.md) uses inter-node durations.**Arguments:**

| Argument | Description |
|----------|-------------|
| `sec` | An instance of [Float](../Classes/Float.md). Seconds. |  
### `maxTime`
Changes maximum time (sec) shown in editor.**Arguments:**

| Argument | Description |
|----------|-------------|
| `sec` | An instance of [Float](../Classes/Float.md). Seconds. |  

### Subclassing and Internal Methods
The following methods are usually not used directly or are called by a primitive. Programmers can still call or override these as needed.

### `defaultMouseDownAction`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `x` |  |  
| `y` |  |  
| `modifiers` |  |  
| `buttonNumber` |  |  
| `clickCount` |  |  

### `env`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `e` |  |  

### `addBreakPoint`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `level` |  |  

### `insertAtTime`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `time` |  |  
| `level` |  |  

### `pointsPerSegment`

### `initSCEnvelopeEdit`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `argEnv` |  |  
| `argPPS` |  |  
| `setMinMax` |  |  

### `redraw`

### `updateAll`

### `updateSegment`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `segNum` |  |  

### `clear`


## Examples

Make a basic editor:

```supercollider
(
e = Env([1, 2], [10]);
w = Window("Env Editor", Rect(200, 200, 300, 200));
v = SCEnvelopeEdit(w, w.view.bounds.moveBy(20, 20).resizeBy(-40, -40), e, 20).resize_(5);
w.front;
)

v.addBreakPoint;

(
v.clear;
v.redraw;
v;
)

v.maxLevel_(2); // to give more headroom
v.maxTime_(2); // to increase release point
v.minTime_(-1); // to increase attack time

e.curves_('sin'); // env object is changed
v.refresh; // must refresh editor
```


Controlling a Synth

```supercollider
s.boot;

(
e = Env([0, 1, 0.7, 0.9, 0], [0.03, 0.03, 0.03, 0.03], 'sin');
f = Env([0, 1, 0.7, 0.9, 0], [0.03, 0.03, 0.03, 0.03], 'sin');
w = Window("Shards", Rect(100, 100, 500, 400));
v = SCEnvelopeEdit(w, w.view.bounds.resizeBy(-20, -200), e, 10).resize_(2);
StaticText(w, v.bounds).string_(" amplitude").resize_(2);
x = SCEnvelopeEdit(w, v.bounds.moveBy(0, 200), f, 10).resize_(2);
StaticText(w, x.bounds).string_(" frequency").resize_(2);
w.front;
)

(
SynthDef("sineBlip", {
    arg freq = 440, vol = 0.1, la0, la1, la2, la3, la4, ta0, ta1, ta2, ta3, crva,
        lf0, lf1, lf2, lf3, lf4, tf0, tf1, tf2, tf3, crvf;
    var signal, fenv, aenv;
    fenv = EnvGen.ar(Env([lf0, lf1, lf2, lf3, lf4], [tf0, tf1, tf2, tf3], crvf));
    aenv = EnvGen.ar(Env([la0, la1, la2, la3, la4], [ta0, ta1, ta2, ta3], crva), doneAction: Done.freeSelf);
    signal = SinOsc.ar([freq, freq*2] * fenv) * aenv * vol;
    Out.ar(0, signal.dup);
}).add;
)

(
Routine({
    var par, indices;
    indices = (2..21);
    loop({
        par = (indices +++ (
            v.env.levels ++
            v.env.times ++
            v.env.curves ++
            x.env.levels ++
            x.env.times ++
            x.env.curves)).flatten;
        s.sendBundle(s.latency, [\s_new, "sineBlip", -1, 1, 1, \freq, exprand(4e3, 11e3)] ++ par);
        0.04.wait;
    });
}).play;
)
```




