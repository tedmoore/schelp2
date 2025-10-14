# Font

*A font object*

**Categories:** GUI>Accessories

## Description

This is the object you pass to other gui objects to set their font name or size.


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` | An instance of [String](../Classes/String.md). Must coincide with the name of a font on the system. See [#*availableFonts](#*availablefonts). |  
| `size` | An instance of [Float](../Classes/Float.md). |  
| `bold` | A Boolean. |  
| `italic` | A Boolean. |  
| `usePointSize` | A Boolean. Whether to regard the **size** argument as point-size - adapting to the screen resolution. |  
Example:
```supercollider
g = Font("Helvetica", 12);
```


### `availableFonts`
**Returns:** [Array](../Classes/Array.md) of the available fonts.
### `antiAliasing`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `flag` | An instance of [Boolean](../Classes/Boolean.md). Default value is `false`. |  

### `smoothing`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `flag` | An instance of [Boolean](../Classes/Boolean.md). Default value is `false`. |  

### `defaultSansFace`
**Returns:** The default sans serif face Font.
### `defaultSerifFace`
**Returns:** The default serif face Font.
### `defaultMonoFace`
**Returns:** The default monospace face Font.
### `default`
The global default Font.Setting this property is equivalent to `Font.setDefault(font)`. See [#*setDefault](#*setdefault) for details.
### `setDefault`
Sets the global default font. Properties of the `font` argument will be combined with properties of the default system font, and those of individual views.Optionally, a class can be given, so only views of that class will be affected.Note that this will immediately affect any existing views.**Arguments:**

| Argument | Description |
|----------|-------------|
| `font` | An instance of Font. |  
| `class` | A Class (either View or one of its subclasses), or `nil`. |  

### `sansSerif`
Create a new sans serif face Font.
### `monospace`
Create a new monospace face Font.
### `serif`
Create a new serif face Font.

## Instance Methods

### `name`
Gets/sets the name of the font.**Arguments:**

| Argument | Description |
|----------|-------------|
| `value` | An instance of [String](../Classes/String.md). |  
### `size`
Gets/sets the size of the font. Setting this variable is always considered as setting the [#-pixelSize](#-pixelsize), while getting it will return any size set. See [#-hasPointSize](#-haspointsize) for distinction.**Arguments:**

| Argument | Description |
|----------|-------------|
| `pixelSize` | A Float. |  
### `hasPointSize`
A Boolean variable indicating whether the [#-size](#-size) is regarded as pixel-size (precise amount of pixels), or point-size (adapting to screen resolution). To change this, you need to set the size via [#-pixelSize](#-pixelsize) or [#-pointSize](#-pointsize).### `pixelSize`
Gets or sets the pixel-size of the font. When getting, returns nil if the font has point-size instead. See [#-hasPointSize](#-haspointsize) for distinction.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | Any number, but note that floats will be rounded to integer values when setting pixel-size. |  
### `pointSize`
Gets or sets the point-size of the font. When getting, returns nil if the font has pixel-size instead. See [#-hasPointSize](#-haspointsize) for distinction.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Float. |  
### `setDefault`
Makes this instance of Font the default.This is equivalent to calling [#*setDefault](#*setdefault) with this Font and the given class as arguments.### `storeArgs`
(?)**Returns:** an [Array](../Classes/Array.md), `[name, size]`.### `boldVariant`

> **Note:** On the Cocoa GUI it appends `"-Bold"` to the name. This is only useful for fonts that have bold variants.

**Returns:** Bold variant of the Font.
## Examples


```supercollider
(
w = Window.new.front;
t = StaticText(w, w.view.bounds).align_(\center);
t.string = " SUPERCOLLIDER";
)
t.font = Font("Monaco", 24);


(
var updateFont, w, m, y, t, a, b, c;
w = Window("Fonts", Rect(150, Window.screenBounds.height - 500, 400, 400)).front;
w.view.decorator = FlowLayout(w.view.bounds);
StaticText.new(w, Rect(5, 0, 30, 20)).string_("Font").align_(\right);
m = PopUpMenu(w, Rect(40, 0, 250, 20));
m.items = Font.availableFonts;

StaticText.new(w, Rect(290, 0, 28, 20)).string_("Size").align_(\right);
y = PopUpMenu(w, Rect(322, 0, 50, 20));
y.items = ["6","7","8","9","10","12","13","14","18","24","36","48","60","72","96"];

t = TextView(w, Rect(10, 40, 380, 150));
t.string = "\nThe quick drowned fox jumped over the lazy blog. \n\n 0 1 2 3 4 5 6 7 8 9 ";

a = StaticText(w, 200@20).string_("The quick drowned fox").background_(Color.rand).align_(\center);
b = Button(w, 200@20).states_([["The quick drowned fox"]]).background_(Color.rand);
c = PopUpMenu(w, 200@20).items_(["The quick drowned fox"]).background_(Color.rand);

y.action = {
    var font;
    font = Font(m.items[m.value], y.items[y.value].asInteger);
    a.font_(font).refresh;
    b.font_(font).refresh;
    c.font_(font).refresh;
    t.font_(font).refresh;
};

m.action = y.action;

m.valueAction = 3;
y.valueAction = 5;
)


(
var w, f;

w = Window("Fonts", Rect(128, 64, 340, 360));
w.view.decorator = f = FlowLayout(w.view.bounds, Point(4, 4), Point(4, 2));

[
"Helvetica-Bold",
"Helvetica",
"Monaco",
"Arial",
"Gadget",
"MarkerFelt-Thin"
].do({ |name|
    var v, s, n, height = 16;

        v = StaticText(w, Rect(0, 0, 110, height + 20));
        v.font = Font(name, 13);
        v.string = name;

        s = Button(w, Rect(0, 0, 140, height + 20));
        s.font = Font(name, 13);
        s.states = [[name]];

        n = NumberBox(w, Rect(0, 0, 56, height + 20));
        n.font = Font(name, 13);
        n.object = pi;

    f.nextLine;
});

w.front;
)


(
var w, b, f, i = 0;

w = Window("Fonts", Rect(128, 64, 1024, 768));
b = ScrollView(w, w.view.bounds);

b.decorator = f = FlowLayout(b.bounds, Point(4, 4), Point(4, 2));

Font.availableFonts.do({ |name|
    var v, s, n, height = 16, font;
    font = Font(name, 13);

        v = StaticText(b, Rect(0, 0, 120, height + 20));
        v.font = font;
        v.string = name;

        s = Button(b, Rect(0, 0, 140, height + 20));
        s.font = font;
        s.states = [[name]];
        s.action = { font.asCompileString.postln };

        n = NumberBox(b, Rect(0, 0, 56, height + 20));
        n.font = font;
        n.object = pi;
    if((i = i + 1) % 3 == 0, {
        f.nextLine;
    });
});

w.front;
)
```




