# Image

*image component*

**Categories:** GUI>Views

**Related:** [View](../Classes/View.md)

## Description

Image enables the drawing of images in the SuperCollider GUI.


## Class Methods


### `new`
Creates a new Image instance. "multiple" here stands for multiple arguments.**Arguments:**

| Argument | Description |
|----------|-------------|
| `multiple` | Any of the following:- [Number](../Classes/Number.md) to create an **empty** image of size multiple as width and height
```supercollider
i = Image.new(400);        // Create a 400x400 pixel Image.
i.bounds;
i.free;

i = Image.new(400, 200);    // Create a 400x200 pixel Image.
i.bounds;
i.free;
```


- [Point](../Classes/Point.md) to create an **empty** image of size multiple.x as width and multiple.y as height
```supercollider
i = Image.new(400@200);    // Create a 400x200 pixel Image.
i.bounds;
i.free;
```


- [String](../Classes/String.md) to create an image from a **local file**
```supercollider
//    Path string
i = Image.new(SCDoc.helpSourceDir +/+ "images/Swamp.png"); // add a path to your image
[i.width, i.height].postln;
i.bounds;
i.plot;
i.free;
``` |  
| `height` | If **multiple** is a number, then this argument indicates the height of the new image. |  

### `color`
Creates a new Image instance filled with the specified color.
```supercollider
i = Image.color(400, 200, Color.blue(0.9, 0.1));
i.plot(freeOnClose: true);
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `... args` | Multiple arguments. the last argument should be a valid [Color](../Classes/Color.md) |  

### `open`
Creates a new Image instance from the local file at **path**.
```supercollider
(
i = Image.open(SCDoc.helpSourceDir +/+ "images/Swamp.png");
i.plot(freeOnClose: true);
i.url.postln;
)
```


### `openSVG`
Creates a new Image instance from the local SVG file at **path**.
```supercollider
(
i = Image.openSVG(SCDoc.helpSourceDir +/+ "images/plugin.svg", 200@200);
i.plot(freeOnClose: true);
i.url.postln;
)
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` | A String containing the SVG file's path. |  
| `size` | A [Size](../Classes/Size.md). SVG contents will be drawn into an image of this size. If not provided, suggested size provided by SVG will be used. |  

### `openURL`

> **Note:** Not implemented yet.

Creates a new Image instance from a valid image at the specified URL **path**.
```supercollider
i = Image.openURL(SCDoc.helpSourceDir +/+ "images/Swamp.png");
i.url;
w = i.plot(freeOnClose: true);
```


### `fromImage`
Creates a new Image instance from another Image.
```supercollider
i = Image.new(SCDoc.helpSourceDir +/+ "images/Swamp.png");
j = Image.fromImage(i);
i.dump;
j.dump;
[i, j].do(_.plot);
[i, j].do(_.free);
```


### `fromWindow`
Creates a new Image from a portion of a Window. this can be used to capture either a window or a specific View.
```supercollider
// WINDOW Example:
// First create a window and draw inside of it
(
    w = Window.new;
    w.front; // comment this to copy offscreen window
    w.view.background_(Color.white);
    w.drawHook = {
        Pen.translate(100, 100);
        10.do{
            // set the Color
            Pen.color = Color.blue(rrand(0.0, 1), rrand(0.0, 0.5));
            Pen.addWedge((100.rand)@(100.rand), rrand(10, 100), 2pi.rand, 2pi.rand);
            Pen.perform([\stroke, \fill].choose);
        }
    };
    w.refresh;
)

// then grab the window
(
    i = Image.fromWindow(w);
    w.close;
    i.plot(freeOnClose: true);
)

// VIEW Capture Example:
// First create a window and add some views inside of it
(
    w = Window.new.front;
    b = [10, 80].asSpec;
    c = NumberBox(w, Rect(20, 20, 60, 40));
    a = Slider(w, Rect(20, 80, 100, 40))
        .focusColor_(Color.red(alpha: 0.2))
        .action_({
            c.value_(b.map(a.value).round(0.01))
    // round the float so it will fit in the NumberBox
            });
)

// then grab the window
(
    i = Image.fromWindow(w, a.bounds);
    w.close;
    i.plot(freeOnClose: true);
)
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `window` | the Window object. |  
| `rect` | optional. the constrained rect to capture inside the Window. By default, it is the window size. |  

### `closeAllPlotWindows`
Close all the Image plot windows currently opened.
### `colorToPixel`
Convert a [Color](../Classes/Color.md) into a pixel datatype suitable for setting pixel data in the Image class.**Returns:** A 32bit packed Integer in the RGBA format.
### `pixelToColor`
Convert a 32bit packed Integer in the RGBA format into a [Color](../Classes/Color.md)**Returns:** A [Color](../Classes/Color.md)


### Class variables and attributes
### `formats`
returns all the valid image formats as an [Array](../Classes/Array.md)
```supercollider
Image.formats;
```


### `compositingOperations`
returns all the valid compositing operations you can use when drawing an Image as an [Array](../Classes/Array.md)
```supercollider
Image.compositingOperations;
```


### `interpolations`
returns an [Array](../Classes/Array.md) of the different levels of interpolation you can specify when drawing an Image.
```supercollider
Image.interpolations;
```


### `resizeModes`
returns an [Array](../Classes/Array.md) of the different resize modes you can specify when changing the size of an Image.
```supercollider
Image.resizeModes;
```


### `allPlotWindows`
Returns an array of all the Image plot windows currently opened.
```supercollider
Image.allPlotWindows
```




## Instance Methods


### commons / general attributes
### `width`
returns or set the width of the receiver
### `height`
returns or set the height of the receiver
### `setSize`
set the size of the receiver
### `bounds`
returns the bounds of the receiver.
### `free`
deallocate the receiver. this method is useful if you want to manage and reclaim yourself resources. otherwise you do not need to call this method since each object is automatically garbage collected.
### `scalesWhenResized`
flag to tell or set if the receiver should update its bitmap representation to scale when a resize operation is performed
```supercollider
(
i = Image.new(SCDoc.helpSourceDir +/+ "images/Swamp.png");
i.bounds.postln; // getting the dimensions
w = i.plot;
)

// changing the size of an image
(
i.scalesWhenResized_(true);
i.setSize(400, (400 / (i.width / i.height)).asInteger);
a = i.plot;
)

(
a.close; w.close; i.free;
)
```


### `url`
returns or set the url of the receiver. Returning only if any where supplied at creation, otherwise returns nil. Setting may be used for different purpose but try to supply a valid one since it is used for archiving the image as an object.
```supercollider
i = Image.new("http://www.google.com/intl/en_ALL/images/logo.gif");
i.url;
i.plot;
i.free;
```


### `interpolation`
get or set the level of interpolation used when rendering the image - it has not effect when the Image is accelerated. see [#*interpolations](#*interpolations) for a valid range of values.
```supercollider
(
i = Image.new(SCDoc.helpSourceDir +/+ "images/Swamp.png");
w = i.plot;
i.interpolation;            // get the image currrent interpolation mode
)

(
i.interpolation = 'fast';        // experiment with interpolation modes
w.refresh;
)

(
i.interpolation = 'smooth';
w.refresh;
)

i.free;
```



### saving and archiving
### `write`
write the Image to a file.
```supercollider
i = Image.new(SCDoc.helpSourceDir +/+ "images/Swamp.png");
i.dump
i.write("~/Desktop/my_image.png".standardizePath);
i.free;

//    storeOn / asCompileString
i = Image.new(SCDoc.helpSourceDir +/+ "images/Swamp.png");

i.url;
i.asCompileString;
i.writeArchive("~/Desktop/my_image.scd".standardizePath);

i.free;
i = nil;

Document.open("~/Desktop/my_image.scd".standardizePath);

i = Object.readArchive("~/Desktop/my_image.scd".standardizePath);
i.plot;
i.free;
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` | the location where to save it |  
| `format` | (optional) format to use. see Image.formats for supported formats. If nil, it will get the format depending on the path extension. |  
| `quality` | The quality factor must be in the range 0 to 100 or -1. Specify 0 to obtain small compressed files, 100 for large uncompressed files, and -1 (the default) to use the default settings. |  


### rendering
### `plot`
plots the image in a Window.
```supercollider
i = Image.new(SCDoc.helpSourceDir +/+ "images/Swamp.png");
w = i.plot;
w.close;

w = i.plot(showInfo: false);
w.close;
i.free;

// other option - image will be automatically freed when closed
Image.new(SCDoc.helpSourceDir +/+ "images/Swamp.png").plot("Hello", freeOnClose: true);
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` | the title of the Window. may be nil. |  
| `bounds` | the bounds of the Window. may be nil. |  
| `freeOnClose` | flag to tell if the Window should free the Image when closed. |  
| `background` | additional background to apply to the Window. may be useful for artifacts due to alpha / compositing... |  
| `showInfo` | shows pixel coordinates while the mouse is over the image's plot window. |  

### `draw`
shortcut for drawing inside an image. equivalent to :- receiver.lockFocus
- aFunction
- receiver.unlockFocus

```supercollider
(
    j = Image.new(400, 300);
    j.draw({ |image|

        Pen.translate(100, 100);
        1000.do {
            // set the Color
            Pen.color = Color.green(rrand(0.0, 1), rrand(0.0, 0.5));
            Pen.addAnnularWedge(
                (100.rand)@(100.rand),
                rrand(10, 50),
                rrand(51, 100),
                2pi.rand,
                2pi.rand
            );
            Pen.perform([\stroke, \fill].choose);
        };
    }).plot(freeOnClose: true);
)

//    String drawing support on the image
//    drawStringAtPoint(string, point, font, color);
(
    j = Image.new(150, 50);
    j.draw({ |bounds|
        j.drawStringAtPoint("Hello, world!", 10@10, Font("Lucida Grande", 24), Color.black);
    });
)

j.plot;
j.write("~/Desktop/hello.png");
j.free;
```


### `drawStringAtPoint`
renders *correctly* a String inside an Image :) `// to fix to have a compliant interface`
```supercollider
(
    var width, height, tgHeight, ratio, str, font, color, strb, targetWidth = 400, shadowColor, run = true;
    shadowColor = Color.black;

    color = Color.gray(0.8);
    str = "I Love Pixels";
    font = Font("Monaco", 10);
    strb = str.bounds(font);
    width = strb.width;
    height = strb.height;
    ratio = height / width;
    i = Image(width@(height));
    i.draw({ |bb|
        Pen.smoothing_(false);
        i.drawStringAtPoint(str, 0@0, font, color);
    });
    i.interpolation_(\none);
    tgHeight = targetWidth * ratio;
    w = Window.new("", Rect(400, 400, 450, 150)).drawHook_({
        Pen.setShadow(2@2, 0.4, color: Color.red);
        i.drawInRect(Rect(5, 5, targetWidth, tgHeight));
    });

    w.view.background_(Color.white);
    w.onClose_({ run = false; i.free });
    w.front;
)
```


### `drawAtPoint`
render the image or a portion of it in the current graphic context.
```supercollider
(
    var operation = 'sourceOver', fraction = 1.0, i, w;

    i = Image.new(
    //    "http://supercollider.sourceforge.net/theme/sc01/icon.supercollider.gif"
    //    SCDoc.helpSourceDir +/+ "images/duck_alpha.png"
        SCDoc.helpSourceDir +/+ "images/Swamp.png"
    );

    w = Window.new("Image", Rect(120, 400, 360, 180)).front;

    Slider.new(w, Rect(10, 150, 150, 16))
        .value_(1.0)
        .action_({ |sl|
            fraction = sl.value;
            w.refresh;
        });

    PopUpMenu.new(w, Rect(170, 150, 100, 16))
        .items_(Image.compositingOperations.collect({ |i| i.asString }))
        .value_(2)
        .action_({ |pm|
            operation = Image.compositingOperations.at(pm.value);
            w.refresh;
        });

    w.onClose_({ i.free }); // free the image when the window is closed

    w.drawHook_({

        i.drawAtPoint(10@10, nil, operation, fraction);

    });
)
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `point` | the [Point](../Classes/Point.md) where to draw it |  
| `fromRect` | the portion of the Image to use |  
| `operation` | the compositing operation to use. `'sourceOver'` is the default. |  
| `fraction` | the opacity to use, ranging from 0.0 (fully transparent) to 1.0 (fully opaque) |  

### `drawInRect`
render the image or a portion of it in a specified rectangle of the current graphic context. This may stretch the image depending on the destination rect.
```supercollider
(
    i = Image.new(
        // "http://supercollider.sourceforge.net/theme/sc01/icon.supercollider.gif"
        SCDoc.helpSourceDir +/+ "images/icon.supercollider.png"
    );

    w = Window.new("Image", Rect(120, 400, 360, 180)).front;
    w.onClose_({ i.free }); // free the image when the window is closed
    w.drawHook_({
        i.drawInRect(Rect(10, 10, 50, 50), Rect(10, 10, 50, 50), 2, 1.0); // only a section
    });
)
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `rect` | the [Rect](../Classes/Rect.md) where to draw it |  
| `fromRect` | the portion of the Image to use |  
| `operation` | the compositing operation to use. `'sourceOver'` is the default. |  
| `fraction` | the opacity to use, ranging from 0.0 (fully transparent) to 1.0 (fully opaque) |  

### `tileInRect`
tile the image or a portion of it in a specified rectangle of the current graphic context. This may stretch the image depending on the destination rect.
```supercollider
(
i = Image.new(
    // "http://supercollider.sourceforge.net/theme/sc01/icon.supercollider.gif"
    SCDoc.helpSourceDir +/+ "images/icon.supercollider.png"
);

w = Window.new("Image", Rect(120, 400, 360, 180)).front;
w.onClose_({ i.free }); // free the image when the window is closed
w.drawFunc_({
    i.tileInRect(w.view.bounds, nil, 2, 1.0); // all image contents
});
)
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `rect` | the [Rect](../Classes/Rect.md) where to draw it |  
| `fromRect` | the portion of the Image to use |  
| `operation` | the compositing operation to use. `'sourceOver'` is the default.
> **Note:** Compositing operations are currently disabled for tileInRect |  
| `opacity` | the opacity to use, ranging from 0.0 (fully transparent) to 1.0 (fully opaque) |  


### Instance Methods / accessing and setting pixels
### `setPixel`
fill a pixel located at x @ y.
```supercollider
i = Image.color(60, 60, Color.blue(0.1, 0.1));
w = i.plot;
i.setPixel(Image.colorToPixel(Color.new(1, 0, 0, 1)), 0, 0); // setting red
w.refresh;
("pixel at 0 @ 0:"+Image.pixelToColor(i.getPixel(0, 0)).asArray).postln;
i.free;
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `rgbaInteger` | an 32 bit [Integer](../Classes/Integer.md) containing color information packed as 8bit RGBA |  
| `x` | the x position of the pixel in the image |  
| `y` | the y position of the pixel in the image |  

### `getPixel`
retrieve the pixel value at x @ y as a RGBA integer
```supercollider
// A simple example on how to manipulate pixels with Image
(
b = Int32Array[
    Image.colorToPixel(Color.new255(255, 0, 0, 255)), // red
    Image.colorToPixel(Color.new255(0, 255, 0, 255)), // green
    Image.colorToPixel(Color.new255(0, 0, 255, 255)), // blue
    Image.colorToPixel(Color.new255(255, 0, 255, 255)) // purple
];
)

Image.pixelToColor(b[0]).red; // 1.0 see Color -red
Image.pixelToColor(b[0]).green; // 0.0 see Color -green
Image.pixelToColor(b[0]).blue; // 0.0 see Color -blue
Image.pixelToColor(b[0]).alpha; // 1.0 see Color -alpha

a = Image.new(b.size@1).pixels_(b).interpolation_(\fast);
a.plot;


// Set + Get
a.setPixel(Image.colorToPixel(Color.new255(255, 0, 255, 128)) /* create an Integer from 0-255 integer rgba value */, 0, 0).plot;
p = a.getPixel(0, 0);

Image.pixelToColor(p).red; // 1.0
Image.pixelToColor(p).green; // 0.0
Image.pixelToColor(p).blue; // 1.0
Image.pixelToColor(p).alpha; // ~0.5

// now another important example
a.setPixel(Image.colorToPixel(Color.new255(255, 0, 255, 0)), 1, 0).plot; // clear color -> alpha is 0
p = a.getPixel(1, 0);

Image.pixelToColor(p).red; // you expect 1.0 but you get 0.0 ??? Why = because Image uses premultiplied color component value internally
// meaning all Red, Green, and Blue component are premultiplied by the alpha
// if alpha is 0 you get 0 back for all components.

Image.pixelToColor(p).green; // 0
Image.pixelToColor(p).blue; // 0
Image.pixelToColor(p).alpha; // 0

p = a.getColor(1, 0); // more explicit - but same here
```


### `setColor`
fill the pixel located at x @ y with the specified **color**.
### `getColor`
retrieve the pixel value at x @ y as a [Color](../Classes/Color.md).
### `pixels`
retrieve or set all the pixels of the receiver.
> **Note:** Careful: the returned Array is a [Int32Array](../Classes/Int32Array.md) of size receiver.width * receiver.height containing all pixel values as 32bit Integer. See [#*colorToPixel](#*colortopixel) and [#*pixelToColor](#*pixeltocolor).

**Arguments:**

| Argument | Description |
|----------|-------------|
| `array` | an [Int32Array](../Classes/Int32Array.md) of size receiver.width * receiver.height containing all pixel values as 32bit Integer |  

### `loadPixels`
load all the pixels of the receiver in an array. it is better and faster to call this function instead of [pixels](#pixels) if you plan to retrieve frequently the pixel data (since it won't allocate a new array everytime !)
```supercollider
// exec one line at a time
(
i = Image.new(
    // "http://supercollider.sourceforge.net/theme/sc01/icon.supercollider.gif"
    SCDoc.helpSourceDir +/+ "images/icon.supercollider.png"
);
)

// first grab the pixels
p = i.pixels;

// do some mods - here invert
// i.invert; // not implemented yet

// reload directly in my array - do not need to call i.pixels again
i.loadPixels(p);
i.free;
p;
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `array` | the array that will be filled. Should be an [Int32Array](../Classes/Int32Array.md) of size receiver.width * receiver.height. |  
| `region` | the targeted rectangular region. (nil by default, meaning full size) |  
| `start` | the start index of the array. |  

### `setPixels`
set the pixels in a specific portion of the receiver.
```supercollider
(
i = Image.new(20@20);
i.pixels_(
    Int32Array.fill(i.width * i.height, {
        Image.colorToPixel(Color.new255(255.rand, 127.rand, 255.rand, 255))
    })
);
// i.interpolation_(\fast); // uncomment to see the difference
w = i.plot(freeOnClose: true);
i.pixels.postln;
)

(
i = Image.color(50@50, Color.white);
i.setPixels(
    Int32Array.fill(20*20, { Image.colorToPixel(Color.new255(255.rand, 127.rand, 255.rand, 255)) }),
    Rect(10, 10, 20, 20)
);
i.interpolation_(\fast); // uncomment to see the difference
w = i.plot(freeOnClose: true);
i.pixels.postln;
)
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `array` | an [Int32Array](../Classes/Int32Array.md) of size **rect**.width * **rect**.height containing all pixel values as 32bit Integer |  
| `region` | a rectangle defining the portion to update in the receiver. By default **rect** is nil, meaning full image size. |  
| `start` | the array start index. |  

### `pixelRatio`
Get/set pixel ratio of the image.This does NOT affect the content of the image, only how it is interpreted when it is drawn onto a View or another Image. For example, in a high DPI context, the pixel ratio of a View might be 2. When drawing an image with a pixelRatio of 1, each pixel of the image will fill a 2x2 area of the View. If both the Image and the View had a pixel ratio of 2, each pixel would be 1:1 with pixels in the View.By default, the pixelRatio of all Images is 1 - *this ensures that an image will look the same when drawn on a normal or a high DPI view*. Setting a custom (!= 1) pixelRatio should generally only be done to draw specially rendered high DPI images to a View that is known to be high DPI.Note that when drawing to an Image using [Pen](../Classes/Pen.md), pixelRatio is accounted for - so, a line of width 1 will have a true width of 1px for an image where `image.pixelRatio==1`, and a true width of 2px where `image.pixelRatio==2`.


