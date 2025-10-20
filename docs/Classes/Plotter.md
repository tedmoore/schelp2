# Plotter

*Plot numerical data on a window or view*

**Categories:** GUI>Accessories

**Related:** [plot](../Reference/plot.md)

## Description

Plot data of up to three dimensions on a [Window](../Classes/Window.md) or [UserView](../Classes/UserView.md).

### Keyboard shortcuts
When the plotter window has focus, the following keyboard shortcuts can be used to change the display:

| + / - | vertical zoom | 
| --- | --- || = | compare plot channels | | n | toggle normalize display (0..1) / (-1..1), or fit range | | s | toggle superposition (see: superpose) | | m | switch plot mode (see: [Plotter#-plotMode](../Classes/Plotter.md#-plotmode)) | | e | toggle editing (see: [Plotter#-editMode](../Classes/Plotter.md#-editmode)) | | g | toggle horizontal (domain) grid | | G | toggle vertical (codomain) grid | | p | print curve | | ctrl-+ / - | zoom font | | alt-click | post value | 


### Method extensions
Plotter extends other classes with methods. To see what classes implements plot, see [Methods#plot](../Overviews/Methods.md#plot)


### `plot`

```
// plot array
[1, 6, 2, -5, 2].plot;
(0..100).normalize(0, 8pi).sin.plot;

// nested arrays
{ (0..100).normalize(0, 15.0.rand).sin }.dup(3).plot;
{ { (0..17).normalize(0, 15.0.rand).sin }.dup(4) }.dup(3).plot;

// UGen functions
{ SinOsc.ar([700, 357]) * SinOsc.ar([400, 476]) * 0.2 }.plot;

// Buffer
{ var b = Buffer.read(s, ExampleFiles.sinedPink); s.sync; b.plot }.fork(AppClock);

// Env
Env.perc(0.4, 0.6).plot;
```



### `plotGraph`

```
{ |x| sin(x) }.plotGraph(300, 0, 2*pi);
{ |x| sin(1/x) * x }.plotGraph(from: 0.0001, to: 0.2);
```





## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` | Plot window title. |  
| `bounds` | The window bounds (a [Rect](../Classes/Rect.md)). |  
| `parent` | Either a [Window](../Classes/Window.md) / [View](../Classes/View.md) may be passed in - then the plot is embedded. Otherwise a new [Window](../Classes/Window.md) is created. |  

```
(
a = Plotter("the plot", Rect(600, 30, 800, 250));
a.value = (0..1000).normalize(0, 14pi).curdle(0.01).scramble.flat.sin;
)
```



## Instance Methods


### Embedding in another view

### `makeWindow`
Open given plotter in a new window or within a given composite view.See the [#Embedding in another View or GUI](#embedding-in-another-view-or-gui) example.**Arguments:**

| Argument | Description |
|----------|-------------|
| `argParent` | Either a [Window](../Classes/Window.md) or [View](../Classes/View.md) may be passed in - then the plot is embedded. Otherwise a new [Window](../Classes/Window.md) is created. |  
| `argBounds` | The window bounds (a [Rect](../Classes/Rect.md)). |  


### Plot properties

### `plotMode`
Get/Set the style of data display. This can be an array of different modes for multi-channel data. Available modes:| `\points` | draw data points as circles with a dot in the middle | 
| --- | --- || `\dots` | draw data points as filled circles | | `\lines, \linear` | lines connect data points | | `\plines` | lines connect data points, marked also by `\points` | | `\dlines` | lines connect data points, marked also by `\dots` | | `\stems` | PCM-style vertical lines from zero to the data point | | `\pstems` | vertical lines from zero to the data points, marked also by `\points` | | `\dstems` | vertical lines from zero to the data points, marked also by `\dots` | | `\filled` | fills the area under a waveform, and assumes a bipolar signal (filled to the zero-crossing) | | `\pfilled` | `\filled`, marked also by `\points` | | `\dfilled` | `\filled`, marked also by `\dots` | | `\levels` | sample-and-hold style horizontal lines from the data point extending over the sample interval | | `\steps` | "step interpolation": `\levels` connected by vertical lines | | `\bars` | bar graph with filled bars | **Arguments:**

| Argument | Description |
|----------|-------------|
| `modes` | A [Symbol](../Classes/Symbol.md) or an [Array](../Classes/Array.md) of [Symbol](../Classes/Symbol.md)s.If `modes.size < numChannels`, the plots will *wrap* around the array of modes. |  
**Returns:** An [Array](../Classes/Array.md) of [Symbol](../Classes/Symbol.md)s, unless there is only one mode specified or if all modes of a multi-channel plot are the same, in which case a single [Symbol](../Classes/Symbol.md) is returned.
```
p = (0..20).scramble.plot;
p.plotMode = \points;
p.plotMode = \plines;
p.plotMode = \steps;

/* Preview the available modes */
(
s.waitForBoot{
    var modeList = [
        \points, \dots, \levels, \steps,
        \lines, \plines, \dlines,
        \stems, \pstems, \dstems,
        \filled, \dfilled, \pfilled, \bars,
    ];
    modeList.clump((modeList.size/2).ceil).do{ |modes, i|
        var frq = 1000, w = 600, h = 800;
        p = {
            LFSaw.ar(frq) ! modes.size
        }.plot(2.25 * frq.reciprocal);

        0.25.wait; // let Plotter update with data
        p.plotMode_(modes);
        p.axisLabelX_(modes.collect(_.asString));
        p.setProperties(\labelFont, (Font().size_(15)));
        p.parent.bounds_(Rect(0, 0, w, h).left_(w*i));
    };
}
)

/* Mixed modes */
(
d = 4.collect({ |i| 100.collect({ |j| sinPi(1+i.squared*j * 50.reciprocal) }) });
p = d.plot;
p.plotColor_([Color.red, Color.cyan, Color.green, Color.blue]);
p.plotMode_([\steps, \linear, \plines, \points]);
p.superpose_(true);
)
```



### `plotColor`
Set or get the colors of your data plot.**Arguments:**

| Argument | Description |
|----------|-------------|
| `colors` | This can be an [Array](../Classes/Array.md) of [Color](../Classes/Color.md)s for multichannel data, or a single [Color](../Classes/Color.md) to map to all channels.If `colors.size < numChannels`, the plots will *wrap* around the array of colors. |  
**Returns:** An [Array](../Classes/Array.md) of [Color](../Classes/Color.md)s, unless there is only one color specified or if all colors of a multi-channel plot are the same, in which case a [Color](../Classes/Color.md) is returned.
```
// Colorize channels
(
d = 4.collect({ |i|
    100.collect({ |j|
        sinPi(1+i.squared*j * 50.reciprocal)
    })
});
d.plot.plotColor_([Color.red, Color.cyan, Color.green, Color.blue]);
)

// Use 'filled' plotMode to show phase relationships
(
var freq = 100;
{ LFPar.ar(freq * [1, 1.5, 2.25]) }.plot
.plotMode_(\filled)
.plotColor_(
    [\red, \green, \blue].collect{ |col|
        Color.perform(col).alpha_(0.2)
    }
).superpose_(true);
)
```



### `superpose`
If `true`, plotter displays channels overlaid on a single plot. (keyboard shortcut: s)
```
a = { (0..30).scramble }.dup(2).plot;
a.superpose = true;
```



### `axisLabelX`
Get/set the label for the x-axes. Can be a [String](../Classes/String.md) or an [Array](../Classes/Array.md) of [String](../Classes/String.md)s, or `nil` to remove the label. See [#Axis labels](#axis-labels) example below.

### `axisLabelY`
Get/set the label for the y-axes. Can be a [String](../Classes/String.md) or an [Array](../Classes/Array.md) of [String](../Classes/String.md)s, or `nil` to remove the label. See [#Axis labels](#axis-labels) example below.

### `showUnits`
Get/set whether the corresponding [ControlSpec#-units](../Classes/ControlSpec.md#-units) are displayed as labels. The state of [#-unitLocation](#-unitlocation) determines whether the units are shown as axis labels or appended to the tick labels.**Arguments:**

| Argument | Description |
|----------|-------------|
| `bool` | A `Boolean`. |  
When enabling `showUnits`, axis or tick labels will only be updated to show the units when the `axisLabelX/Y` or grid `labelAppendString` properties are `nil`, empty, or were previously set to show the spec units — i.e. `showUnits` won't overwrite a label that has been explicitly set.See [#Unit labels](#unit-labels) example below.

### `unitLocation`
Get/set the label type on which the `Spec` [ControlSpec#-units](../Classes/ControlSpec.md#-units) are shown.See the Discussion in [#-showUnits](#-showunits) about the interraction with pre-existing labels at the **location**, and [#Unit labels](#unit-labels) example below.**Arguments:**

| Argument | Description |
|----------|-------------|
| `location` | A `Symbol`, `\axis` or `\ticks`, to show the units as the axis label or appended to each of the tick labels, respectively. |  


### `setProperties`
Set properties of all plot views. Defaults are taken from `GUI.skins.at(\plot);`> **⚠️ Warning:** It's preferrable to use Plotter's instance methods when possible to set Plot properties to ensure proper behavior when using [#-superpose](#-superpose).**Arguments:**

| Argument | Description |
|----------|-------------|
| `... pairs` | A list of symbol, value pairs. Supported properties:- font
- fontColor
- gridColorX
- gridColorY
- plotColor (an [Array](../Classes/Array.md))
- backgroundColor
- gridLinePattern
- gridLineSmoothing ([Boolean](../Classes/Boolean.md))
- labelX
- labelY
- gridOnX ([Boolean](../Classes/Boolean.md))
- gridOnY ([Boolean](../Classes/Boolean.md)) |  
Example:
```
(
a = { (0..30).scramble }.dup(2).plot;
a.setProperties(
  \fontColor, Color.yellow,
  \plotColor, Color.magenta,
  \backgroundColor, Color.black,
  \gridColorX, Color.green,
  \gridColorY, Color.green,
  \labelX, "Frames",
  \labelFontColor, Color.magenta
);
);

GUI.skins.at(\plot); // defaults
```



### `plots`
**Returns:** An [Array](../Classes/Array.md) of [Plot](../Classes/Plot.md)s.

### Grid properties

### `setGridProperties`
Set one or more properties of the `DrawGridX` or `DrawGridY` used by all `Plots`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `axis` | A `Symbol` denoting the axis whose grid you're modifying: `\x` or `\y`. |  
| `... propertyPairs` | Key value pairs, listed as successive arguments, of the properties to change and their new values. The property key is a `Symbol`.Any of setters of `DrawGridX` or `DrawGridY` can be used. Here is a subset of useful properties:| `\labelAnchor` | A `Symbol` denoting the point on the label's bounding [Rect](../Classes/Rect.md) that anchors to the point where the grid line meets the base of the axis. `\center, \top, \bottom, \left, \right, \topLeft, \topRight, \bottomLeft, \bottomRight, \leftTop, \rightTop, \leftBottom, \rightBottom`. | 
| --- | --- || `\labelOffset` | A [Point](../Classes/Point.md) describing the offset of the `\labelAnchor` from the point where the grid line meets the base of the axis. The positive direction for the `x` and `y` dimensions is right and down, respectively. | | `\labelAlign` | Alignment of the text within its bounding `Rect`: `\left`, `\center`, or `\right`. | | `\constrainLabelExtents` | A `Boolean` specifying whether the tick labels at either end of the axis are constrained by, or can extend beyond, the grid bounds. | | `\drawBaseLine` | A `Boolean` whether a line is drawn at the minimum extent of this **axis**. | | `\drawBoundingLines` | A `Boolean` whether a line is drawn at both ends of the extent of this **axis**. | | `\drawBoundingRect` | A `Boolean` whether a `Rect` is drawn around the bounds of the grid area. | | `\labelAppendString` | A string to append to all of the axis's tick labels. | | `\tickSpacing` | Set the *minimum* spacing between grid lines ("ticks") for each axis. See [DrawGrid#-tickSpacing](../Classes/DrawGrid.md#-tickspacing) for details. | | `\numTicks` | Set the *approximate* number of grid lines ("ticks") for each axis. See [DrawGrid#-numTicks](../Classes/DrawGrid.md#-numticks) for details. | | `\font` | A [Font](../Classes/Font.md) (including size) to be used for the tick labels. | | `\fontColor` | The [Color](../Classes/Color.md) of the tick labels. | | `\gridColor` | The [Color](../Classes/Color.md) of the axis grid lines. | The properties `\drawBaseLine`, `\drawBoundingLines`, or `\drawBoundingRect` are mutually exlusive — setting any of them to true will set the others two to `false`. In the context of `Plotter`, setting `\drawBoundingRect` on one axis to `true` has the same appearance of setting `\drawBoundingLines` on *both* axes to `true`. |  
This is a convenience method to set the grid properties for *all* `Plot`s to the same values. An Example:
```
(
var plotter = [10, 34, 167].collect({ |freq|
    101.collect{ |i| sin((i/1000) * 2pi * freq) }
}).plot;
plotter.setGridProperties(\x,
    \labelAnchor, \topLeft,
    \labelAlign, \left,
    \labelOffset, 1 @ 5,
    \labelAppendString, " samp"
).setGridProperties(\y,
    \labelAnchor, \right,
    \labelAlign, \right,
    \labelOffset, -5 @ 0,
    \constrainLabelExtents, false
)
)
```

To set the properties of grids on each `Plot` separately, iterate over the plots:
```
(
var plotter, labelAnchors;
plotter = [10, 34, 167].collect({ |freq|
    101.collect{ |i| sin((i/1000) * 2pi * freq) }
}).plot;

labelAnchors = [\topLeft, \top, \bottomLeft];

plotter.plots.do{ |plot, i|
    plot.drawGrid.x
    .labelAnchor_(labelAnchors[i])
    .constrainLabelExtents_(true);
};
plotter.updatePlotBounds;
)
```



### `getGridProperty`
Get the value of a grid property. See [#-setGridProperties](#-setgridproperties) for a list of available properties.**Arguments:**

| Argument | Description |
|----------|-------------|
| `axis` | A `Symbol` denoting the axis whose grid you're modifying: `\x` or `\y`. |  
| `property` | The property name as a `Symbol`. |  
As a convenience method, `getGridProperty` assumes that properties across all `Plot`s are the same (as would be the case if set by [#-setGridProperties](#-setgridproperties)) so returns a single value. Alternatively, properties from individual plot grids can be collected by iterating over the plots:
```
( // inspect the \labelAnchor of each DrawGridX
var plotter  = [10, 34, 167].collect({ |freq|
    101.collect{ |i| sin((i/1000) * 2pi * freq) }
}).plot;

plotter.plots.collect({ |plot|
    plot.drawGrid.x.labelAnchor
}).postln;
)
```



### `drawGridBoundingRect`
Set whether a [Rect](../Classes/Rect.md) is drawn around the boundary of the grid. Setting to `false` disables any bounding grid lines (including "base" lines).**Arguments:**

| Argument | Description |
|----------|-------------|
| `bool` | A `Boolean`. |  
In some cases, the [GridLines](../Classes/GridLines.md) of the grid will not fall on the minimum or maximum of it's spec's range. Using [#-drawGridBaseLines](#-drawgridbaselines) or [#-drawGridBoundingRect](#-drawgridboundingrect) will give the appearance of grid lines at the lower end ("base") of the grid, or at both ends of the grid, respectively.

### `drawGridBaseLines`
Set whether a line is drawn at the lower extent of the grid axes. Setting to `false` disables any bounding grid lines (including a bounding `Rect`). See also the Discussion in [#-drawGridBoundingRect](#-drawgridboundingrect).**Arguments:**

| Argument | Description |
|----------|-------------|
| `bool` | A `Boolean`. |  


### Data display properties

### `specs`
Set or get the [spec](../Classes/ControlSpec.md) for the y-axis (codomain).
```
a = { (40..3000).scramble }.dup(2).plot;
a.specs = \freq.asSpec;
```

See also the [#Explicit domain and axis specs](#explicit-domain-and-axis-specs) example below.

### `domainSpecs`
Set or get the [spec](../Classes/ControlSpec.md) for the x-axis (domain).
```
a = { (40..300).scramble }.dup(2).plot;
a.domainSpecs = \freq.asSpec;
```

See also the [#Explicit domain and axis specs](#explicit-domain-and-axis-specs) example below.When setting your `Plotter` [#-value](#-value), the default **domainSpecs** is a linear spec in the range `[0, value.size-1]` (i.e. the indices of the values). Therefore, your values are displayed as evenly sampled between the `minval` and `maxval`, unless you have explicitly set the [#-domain](#-domain) values.If a new [#-value](#-value) is set, you will need to update your domainSpecs.

### `domain`
Set/get the x-axis positions of your data points. The size of the `domainArray` must equal the size of your [#-value](#-value) array, i.e. a domain value specified for each data point.
```
(
var data, domain, plot;
domain = 25.collect({ rrand(0, 50) }).sort;
data = domain.linlin(0, 50, 0, 1);

plot = data.plot.plotMode_(\points);
plot.domainSpecs_([0, 50].asSpec);
plot.domain_(domain);
)
```

See also the [#Explicit domain and axis specs](#explicit-domain-and-axis-specs) example below.Domain values are mapped into the range of the [#-domainSpecs](#-domainspecs), so need not be evenly distributed. If [#-domain](#-domain) is set to `nil`, your values are displayed as evenly sampled between the `minval` and `maxval` of the [#-domainSpecs](#-domainspecs).Currently, for multichannel data plots, it's assumed that all channels of data share a single [#-domain](#-domain). I.e. `domainArray` must be an [Array](../Classes/Array.md) of rank 1.If a new [#-value](#-value) is set, you will need to update your [#-domain](#-domain).

### `resolution`
Set the minimum number of pixels between data points (default: 1)
```
// Changing plot resolution (x-axis)
p = 5000.collect({ |i| sinPi(i * 0.0025) }).plot;
p.resolution_(5).refresh;  // 5px
p.resolution_(10).refresh;
p.resolution_(50).refresh; // undersampled
p.resolution_(1).refresh;  // default
```



### Plot data

### `value`
Return or set the data values. Data may be numerical arrays of up to 3 dimensions.
```
a = [1, 4, 2, 7, 4].dup(2).plot;
a.value;
```



### `setValue`
Set the data values, with additional arguments determining how the plot is updated.**Arguments:**

| Argument | Description |
|----------|-------------|
| `arrays` | Arrays of data to plot. Data may be numerical arrays of up to 3 dimensions. |  
| `findSpecs` | A `Boolean`. If `true` (default), bounds of the plot(s) are determined automatically. If `false`, previous bounds will persist. |  
| `refresh` | A `Boolean`. If `true` (default), refresh the view immediately. |  
| `separately` | A `Boolean`. If `true` (default), min and max of each set of data will be calculated and displayed separately for each plot. If `false`, each plot's range on the y-axis will be the same. |  
| `minval` | (Optional) The minimum value displayed on the y-axis. |  
| `maxval` | (Optional) The maximum value displayed on the y-axis. |  
| `defaultRange` | (Optional) A default range for the y-axis in the case that the max and min values of the data are identical. |  


### `findSpecs`
If `true`, specs are derived from new data (using min and max values) automatically. Default: `true`.

### `data`
Reference to the current internal data (with shape up to depth of 3).

### Edit mode

### `editMode`
If the edit mode is set to true, the data may be edited via cursor.
```
a = (0..20).plot;
a.editMode = true; // now edit the data by clicking into the plot..
a.value; // the updated values
```



### `editFunc`
Supply a function which is evaluated when editing data. The function is called with the arguments: `plotter`, `plotIndex`, `index`, `val`, `x`, `y`.Example:
```
(
a = { (0..10).scramble.normalize }.dup(2).plot;
a.editMode = true;
a.editFunc = { |...args| args.postln };
)

// using plotter as a control interface
(
a = { (0..10).scramble.normalize(300, 400) }.dup.plot;
a.specs = \freq; a.plotMode = \bars;
a.editMode = true;
x = {
    var phase = SinOsc.ar(\rate.kr(a.value[1]));
    SinOsc.ar(\freq.kr(a.value[0]), phase).mean * 0.1
}.play;
a.editFunc = { |plotter, plotIndex, i, val|
    x.setn(\freq, a.value[0]);
    x.setn(\rate, a.value[1]);
};
a.parent.onClose = { x.release };
)
```



### `cursorPos`
**Returns:** The last cursorPos (a [Point](../Classes/Point.md)).


## Examples


```
(
a = Plotter("the plot", Rect(600, 30, 600, 400));
a.value = (0..100).normalize(0, 8pi).sin;
)

a.value = { |i| (0..90) % (i + 12) + ((0..90) % (i + 2 * 1)) }.dup(3);
a.value = (0..12).squared;
a.plotMode = \points;
a.plotMode = \levels;
a.plotMode = \plines;

a.domainSpecs = [[0, 115, \lin, 1]];

a.parent.close; // close window
a.makeWindow; a.updatePlotBounds; // open it again

a.value = { (0..70).scramble }.dup(3);
a.plotMode = \linear;
a.value = { |i| (0..2000).normalize(0, 4pi + i).sin } ! 4; // lots of values, test efficiency
a.value = { |i| (0..10000).normalize(0, 8pi + i).sin } ! 3; // lots of values, test efficiency
a.value = { (0..140).scramble } ! 7;

a.value = { |i| (0..90).normalize(0, 8pi + (i*2pi)).sin } ! 2 * [400, 560] + 700;
a.value = { |i| (_ + 2.0.rand).dup(100).normalize(0, 8pi + i).sin } ! 2 * 400 + 700;


// Multi channel expansion of single values
a.value = { |i| (_ + 2.0.rand).dup(100).normalize(0, 8pi + i).sin *.t [1, 2, 3] } ! 2 * 400 + 700;
a.value = { |i| (0..10) **.t [1, 1.2, 1.3, 1.5] * (3.5 ** i) }.dup(3);

a.parent.bounds = Rect(400, 100, 500, 700);
a.parent.bounds = Rect(600, 30, 500, 300);

a.superpose = true;
a.value = { |i| (0..20) * (3.5 ** i) }.dup(5);
a.superpose = false;
```



### Object .plot methods

```
// Array:plot
(
a = (4 ** (-5..0)).postln.plot;
a.specs = \delay;
a.domainSpecs = [0, 10, \lin, 0, 0, " Kg"].asSpec;
);

a.domainSpecs = [0.1, 10, \exponential, 0, 0, " Kg"].asSpec;
a.domainSpecs = [-10, 10, \lin, 0, 0, " Kg"].asSpec;

a = [(0..100) * 9, (200..1300) * 2, (200..1000)/ 5].plot;
a.superpose = true;

a = [[0, 1.2, 1.5], [0, 1.3, 1.5, 1.6], [0, 1.5, 1.8, 2, 6]].midiratio.plot;
a.plotMode = \levels;
a.superpose = false;

// Function:plot
a = { SinOsc.ar([700, 357]) * SinOsc.ar([400, 476]) * 0.2 }.plot;
a = { SinOsc.ar([700, 357] *0.02) * SinOsc.ar([400, 476]) * 0.3 }.plot(0.2, minval: -1);

// Env:plot
Env.perc(0.4, 0.6).plot;
Env.new({ 1.0.rand2 }! 8, { 1.0.rand } ! 7, \sin).plot;

// Buffer:plot
(
s.waitForBoot({
    var b = Buffer.read(s,
        ExampleFiles.sinedPink
    );
    s.sync;
    b.plot;
    b.free;
});
)
```




### Explicit domain and axis specs

```
// data
a = (50..90).midicps.scramble.plot;
// specs (y-axis)
a.specs = ControlSpec(100, 2000, units: "Hz");

a.value = 50.collect{ exprand(1e4, 1e7) };
a.specs = [1e4, 1e7, \exp].asSpec;

// domainSpecs (x-axis)
// If domain is unassigned, values are
// distributed evenly within the spec range
a.domainSpecs = [-10, 70].asSpec;


// Setting the domain, run the full block:
(
var ys, xs; // ys: data, xs: domain positions
var rs = 0, plt2;

// xs are the sample points over a 2pi range

// sample locations, normalized
xs = 50.collect({ rrand(0.05, 1) }).normalizeSum;
xs.do{ |me, i| xs[i] = me + rs; rs = rs + me };

// force beginning/end to land on 0/2pi
xs[0] = 0;
xs[xs.size-1] = 1;

// scale these points to a 2pi range
xs = xs * 2pi;

// ys are the values of the sinusoid at the sampled points
ys = sin(xs);

// the uneven sampling is apparent when
// displayed as uniformly sampled
ys.plot("original data plot, uniform domain", [100, 100, 385, 285].asRect);

// generate a second plot whose domainSpec is specified:
// we see a smooth sinusoid cycle beginning
// at 0 and ending at 2pi
plt2 = ys.plot("resampled domain", [100+400, 100, 385, 285].asRect);

// domain values place plotted points where they
// actually sampled the sinusoid, thus visually
// reconstructing it.
plt2.domain = xs;

// these values are placed within the domainSpec
// so we can pad the plot on either side.
plt2.domainSpecs_(([-0.5pi, 2.5pi]).asSpec);
)

// Non-linear scaling of axes.
// plot 1000 values, linearly distributed on X and Y
p = (1, 2 .. 1000).plot.domainSpecs_([1, 1000, \lin].asSpec);
// scale y axis exponentially
p.specs_([[1, 1000, \exp].asSpec]);
// then scale x axis exponentially
p.domainSpecs_([1, 1000, \exp].asSpec);
```




### Axis labels

```
(
p = 4.collect({
    100.collect({ rrand(0, 1.0) })
}).plot(bounds: Rect(50, 50, 500, 650));
p.plotColor_([Color.red, Color.blue, Color.green, Color.cyan]);
)

// a single label propagates through all Plots
p.axisLabelX_("one");
// set each individually
p.axisLabelX_(["one", "two", "three", "four"]);
// superposed plots default to the first label
p.superpose_(true);
p.superpose_(false); // labels are restored
// nil element removes a label
p.axisLabelX_(["one", "two", nil, "four"]);
// assigning nil removes all labels
p.axisLabelX_(nil);
// ... axisLabelY behaves the same way
```




### Unit labels
The units of the grid specs are shown as labels, either axis labels or appended to tick labels. Unit labels won't overwrite preexisting labels, and can be disabled altogether.


```
( // units displayed in the axis labels by default
p = (4 ** (-1.5, -1.25 .. 0)).plot;
p.specs = \delay.asSpec.minval_(0.1);
p.domainSpecs = [0, 10, \lin, 0, 0, "xUnits"].asSpec;
p.setGridProperties(\y, \constrainLabelExtents, false);
p.setGridProperties(\x, \constrainLabelExtents, true);
)

p.showUnits = false;      // hide units
p.unitLocation = \ticks;  // move units to tick labels
p.showUnits = true;       // show units
p.axisLabelX = "X LABEL"; // set an axis label
p.unitLocation = \axis;   // move units to axes
// ... x-axis label isn't overwritten
p.axisLabelX = nil        // remove x-axis label
p.unitLocation = \axis;   // set units to axes again
// ... units now appear on the x-axis

// customize the Y labels
p.setGridProperties(\y, \labelAppendString, " y");
// move units to tick labels
p.unitLocation = \ticks;
// ... y-axis tick labels aren't overwritten
// now remove y-tick label string
p.setGridProperties(\y, \labelAppendString, nil);
// set units to tick labels again
p.unitLocation = \ticks;
// ... units now appear on the y-tick labels
```




### Embedding in another View or GUI

```
(
var w, z, p, d, func;
w = Window("plot panel", Rect(20, 30, 520, 450));
z = CompositeView(
    w, Rect(10, 35, 490, 400)
).background_(Color.rand(0.7)).resize_(5);
p = Plotter("plot", parent: z);
d = Array.rand(32, 0, 20);
func = { |v|
    var offset = v.value.linlin(0, 1, 0, d.size.neg).asInteger;
    p.value = d.rotate(offset).keep(8);
    w.refresh;
};
Slider.new(w, Rect(10, 10, 490, 20)).resize_(2).action_({ |v| func.(v.value) });
func.value(0);
w.front;
)
```




### Changing global defaults
The default styles are kept (and may be overridden) in `GUI.skins.at(\plot)`. See also [GUI](../Classes/GUI.md) help.


```
// specify plot layout
(
GUI.skins.plot.gridLinePattern = FloatArray[1, 0];
GUI.skins.plot.fontColor = Color(0.5, 1, 0);
GUI.skins.plot.gridColorX = Color.yellow(0.5);
GUI.skins.plot.gridColorY = Color.yellow(0.5);
GUI.skins.plot.background = Color.black;
GUI.skins.plot.plotColor = Color.red;
GUI.skins.plot.labelX = "X";
GUI.skins.plot.labelY = "Y";
)

(
x = { |i| (0..60).scramble * (3.5 ** i) }.dup(3);
x.plot("ARRAY:PLOT", Rect(200, 300, 600, 500));
)

GUI.skins.plot.put(\plotColor, { Color.rand(0.0, 0.8) } ! 8);
[(0..100), (20..120), (40..140)].squared.flop.bubble.plot;

// reset the defaults:
Plot.initClass;
```






