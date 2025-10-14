# SCImage

*image component*

**Categories:** GUI>Views

**Related:** [SCImageFilter](../Classes/SCImageFilter.md), [SCImageKernel](../Classes/SCImageKernel.md)

## Description

SCImage is an image component for the macOS SuperCollider client. SCImage is currently a wrapper around different models : you can use it for bitmap operations, image embedding for custom UI and for more advanced image processing as applying filters and kernels, both provided with the CoreImage framework.
SCImage currently supports most formats including tiff, bmp, gif, jpeg, png, tga...ect.. for reading. But for for writing it supports only those in `SCImage.formats`.

> **Note:** [GUI](../Classes/GUI.md) Issue : since it is macOS only, be sure to call `GUI.cocoa` before any SCImage.call




## Class Methods


### `new`
Creates a new SCImage instance. multiple stands here for multiple arguments.**Arguments:**

| Argument | Description |
|----------|-------------|
| `multiple` | May be a...- [Number](../Classes/Number.md) to create an **empty** image of size multiple as width and height
```supercollider
i = SCImage.new(400);        // Create a 400x400 pixels SCimage.
i.dump;
i.free;

i = SCImage.new(400, 200);    // Create a 400x200 pixels SCimage.
i.dump;
i.free;
```


- [Point](../Classes/Point.md) to create an **empty** image of size multiple.x as width and multiple.y as height
```supercollider
i = SCImage.new(400@200);    // Create a 400x200 pixels SCimage.
i.dump;
i.free;
```


- [String](../Classes/String.md) to create an image from a **local file** or from an **URL** (http://, ftp://, [file:///)](../file:///).md)
```supercollider
//    Path string
i = SCImage.new("/Library/Desktop Pictures/Ripples Blue.jpg");
[i.width, i.height].postln;
i.plot;
i.free;
//    URL string - http:// or ftp:// - blocks until image is downloaded
i = SCImage.new("http://www.google.com/intl/en_ALL/images/logo.gif");
i.plot;
i.url;
i.free;
``` |  

### `color`
Creates a new SCImage instance filled with the specified color.
```supercollider
i = SCImage.color(400, 200, Color.blue(0.9, 0.1));
i.plot(freeOnClose: true);
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `args` | multiple arguments. the last argument should be a valid [Color](../Classes/Color.md) |  

### `open`
Creates a new SCImage instance from the local file at **path**.
```supercollider
(
i = SCImage.open("/Library/Desktop Pictures/Ripples Blue.jpg");
i.plot(freeOnClose: true);
i.url.postln;
)
```


### `openURL`
Creates a new SCImage instance from a valid image at the specified URL **path**.
```supercollider
i = SCImage.openURL("file:///Library/Desktop%20Pictures/Ripples%20Blue.jpg");
i.url;
w = i.plot(freeOnClose: true);
```


### `fromImage`
Creates a new SCImage instance from another SCImage.
```supercollider
i = SCImage.new(SCDoc.helpSourceDir +/+ "images/vduck2.jpg");
j = SCImage.fromImage(i);
i.dump;
j.dump;
[i, j].do(_.plot);
[i, j].do(_.free);
```


### `fromWindow`
Creates a new SCImage from a portion of a SCWindow. this can be used to capture either a window or a specific SCView.
```supercollider
// WINDOW Example:
// First create a window and draw inside of it
(
    w = SCWindow.new;
    w.front; // comment this to copy offscreen window
    w.view.background_(Color.white);
    w.drawFunc = {
        SCPen.translate(100, 100);
        10.do{
            // set the Color
            SCPen.color = Color.blue(rrand(0.0, 1), rrand(0.0, 0.5));
            SCPen.addWedge((100.rand)@(100.rand), rrand(10, 100), 2pi.rand, 2pi.rand);
            SCPen.perform([\stroke, \fill].choose);
        }
    };
    w.refresh;
)

// then grab the window
(
    i = SCImage.fromWindow(w);
    w.close;
    i.plot(freeOnClose: true);
)

// VIEW Capture Example:
// First create a window and add some views inside of it
(
    w = SCWindow.new.front;
    b = [10, 80].asSpec;
    c = SCNumberBox(w, Rect(20, 20, 60, 40));
    a = SCSlider(w, Rect(20, 80, 100, 40))
        .focusColor_(Color.red(alpha: 0.2))
        .action_({
            c.value_(b.map(a.value).round(0.01))
    // round the float so it will fit in the SCNumberBox
            });
)

// then grab the window
(
    i = SCImage.fromWindow(w, a.bounds);
    w.close;
    i.plot(freeOnClose: true);
)
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `window` | the SCWindow object. |  
| `rect` | optional. the constrained rect to capture inside the SCWindow. By default, it is the window size. |  


### Class variables and attributes
### `formats`
returns all the valid image formats as an [Array](../Classes/Array.md)
```supercollider
SCImage.formats;
```


### `compositingOperations`
returns all the valid compositing operations you can use when drawing an SCImage as an [Array](../Classes/Array.md)
```supercollider
SCImage.compositingOperations;
```


### `interpolations`
returns an [Array](../Classes/Array.md) of the different levels of interpolation you can specify when drawing an SCImage.
```supercollider
SCImage.interpolations;
```


### `closeAllPlotWindows`
close all the SCImage plot windows currently opened.


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
```supercollider
i = SCImage.new("/Library/Desktop Pictures/Ripples Blue.jpg");
SCImage.all;
i.free;
SCImage.all;
```


### `scalesWhenResized`
flag to tell or set if the receiver should update its bitmap representation to scale when a resize operation if performed
```supercollider
(
    i = SCImage.new("/Library/Desktop Pictures/Ripples Blue.jpg");
    i.bounds.postln; // getting the dimensions
    w = i.plot;
)

// changing the size of an image
(
    i.scalesWhenResized_(true);
    i.setSize(400, 400 / (i.width / i.height));
    a = i.plot;
)
(
a.close; w.close; i.free;
)
```


### `url`
returns or set the url of the receiver. Returning only if any where supplied at creation, otherwise returns nil. Setting may be used for different purpose but try to supply a valid one since it is used for archiving the image as an object.
```supercollider
i = SCImage.new("http://www.google.com/intl/en_ALL/images/logo.gif");
i.url;
i.plot;
i.free;
```


### `accelerated`
if true, the receiver currently use the CoreImage model, possibly caching its data on GPU, if not the bitmap model. Set it to switch representation.> **⚠️ Warning:** this method should never be used directly unless you know perfectly what you are doing. Since the SCImage will switch internally and manage itself the syncronization between representations.
### `interpolation`
get or set the level of interpolation used when rendering the image - it has not effect when the SCImage is accelerated. see [#*interpolations](#*interpolations) for a valid range of values.
```supercollider
(
i = SCImage.new(SCDoc.helpSourceDir +/+ "images/vduck2.jpg");
w = i.plot;
i.interpolation;            // get the image current interpolation mode
)

(
i.interpolation = 'none';        // experiment with interpolation modes
w.refresh;
)

(
i.interpolation = 'low';
w.refresh;
)

(
i.interpolation = 1;            // same as 'low'
w.refresh;
)

(
i.interpolation = 'high';
w.refresh;
)

(
i.interpolation = 'default';
w.refresh;
)

(
i.accelerated_(true);
i.interpolation = 'none'; // does not work on coreimage accelerated image
w.refresh;
)

i.free;
```



### saving and archiving
### `write`
write the SCImage to a file.
```supercollider
i = SCImage.new("/Library/Desktop Pictures/Ripples Blue.jpg");
i.dump
i.write("~/Desktop/my_image.png");
i.free;

//    storeOn / asCompileString
i = SCImage.new("/Library/Desktop Pictures/Ripples Blue.jpg");
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
| `format` | (optional) format to use. see SCImage.formats for supported formats. If nil, it will get the format depending on the path extension. |  


### rendering
### `plot`
plots the image in a SCWindow.
```supercollider
i = SCImage.new("/Library/Desktop Pictures/Ripples Blue.jpg");
w = i.plot;
w.close;

w = i.plot(showInfo: false);
w.close;
i.free;

// other option - image will be automatically freed when closed
SCImage.new("/Library/Desktop Pictures/Ripples Blue.jpg").plot("Hello", freeOnClose: true);
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` | the title of the SCWindow. may be nil. |  
| `bounds` | the bounds of the SCWindow. may be nil. |  
| `freeOnClose` | flag to tell if the SCWindow should free the SCImage when closed. |  
| `background` | additional background to apply to the SCWindow. may be useful for artifacts due to alpha / compositing... |  
| `showInfo` | shows pixel coordinates while the mouse is over the image's plot window. |  

### `lockFocus`
sets the receiver as the current graphic context. So you can use SCPen to draw inside of it.
### `unlockFocus`
restore the graphic context state. the receiver is not anymore the current graphic context.
```supercollider
(
    j = SCImage.new(400, 300);

    j.lockFocus;

        SCPen.translate(100, 100);
        1000.do{
            // set the Color
            SCPen.color = Color.green(rrand(0.0, 1), rrand(0.0, 0.5));
            SCPen.addAnnularWedge(
                (100.rand)@(100.rand),
                rrand(10, 50),
                rrand(51, 100),
                2pi.rand,
                2pi.rand
            );
            SCPen.perform([\stroke, \fill].choose);
        };

    j.unlockFocus;
)

j.plot;
j.write("~/Desktop/my_drawing.png"); // write the image
j.free;
```


### `draw`
shortcut for drawing inside an image. equivalent to :- receiver.lockFocus
- aFunction
- receiver.unlockFocus

```supercollider
(
    j = SCImage.new(400, 300);
    j.draw({ |image|

        SCPen.translate(100, 100);
        1000.do {
            // set the Color
            SCPen.color = Color.green(rrand(0.0, 1), rrand(0.0, 0.5));
            SCPen.addAnnularWedge(
                (100.rand)@(100.rand),
                rrand(10, 50),
                rrand(51, 100),
                2pi.rand,
                2pi.rand
            );
            SCPen.perform([\stroke, \fill].choose);
        };
    }).plot(freeOnClose: true);
)

//    String drawing support on the image
//    drawStringAtPoint(string, point, font, color);
(
    j = SCImage.new(150, 50);
    j.draw({ |bounds|
        j.drawStringAtPoint("Hello, world!", 10@10, Font("Lucida Grande", 24), Color.black);
    });
)

j.plot;
j.write("~/Desktop/hello.png");
j.free;
```


### `drawStringAtPoint`
renders *correctly* a String inside an SCImage :) `// to fix to have a compliant interface`
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
    i = SCImage(width@(height));
    i.draw({ |bb|
        SCPen.smoothing_(false);
        i.drawStringAtPoint(str, 0@0, font, color);
    });
    i.interpolation_(\none);
    tgHeight = targetWidth * ratio;
    w = SCWindow.new("", Rect(400, 400, 450, 150)).drawFunc_({
        SCPen.setShadow(2@2, 0.4, color: Color.red);
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

    i = SCImage.new(
    //    "http://supercollider.sourceforge.net/theme/sc01/icon.supercollider.gif"
    //    SCDoc.helpSourceDir +/+ "images/duck_alpha.png"
        SCDoc.helpSourceDir +/+ "images/Swamp.png"
    );

    w = SCWindow.new("SCImage", Rect(120, 400, 360, 180)).front;

    SCSlider.new(w, Rect(10, 150, 150, 16))
        .value_(1.0)
        .action_({ |sl|
            fraction = sl.value;
            w.refresh;
        });

    SCPopUpMenu.new(w, Rect(170, 150, 100, 16))
        .items_(SCImage.compositingOperations.collect({ |i| i.asString }))
        .value_(2)
        .action_({ |pm|
            operation = SCImage.compositingOperations.at(pm.value);
            w.refresh;
        });

    w.onClose_({ i.free }); // free the image when the window is closed

    w.drawFunc_({

        i.drawAtPoint(10@10, nil, operation, fraction);

    });
)
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `point` | the [Point](../Classes/Point.md) where to draw it |  
| `fromRect` | the portion of the SCImage to use |  
| `operation` | the compositing operation to use. `'sourceOver'` is the default. |  
| `fraction` | the opacity to use, ranging from 0.0 (fully transparent) to 1.0 (fully opaque) |  

### `drawInRect`
render the image or a portion of it in a specified rectangle of the current graphic context. This may stretch the image depending on the destination rect.
```supercollider
(
    i = SCImage.new(
        // "http://supercollider.sourceforge.net/theme/sc01/icon.supercollider.gif"
        SCDoc.helpSourceDir +/+ "images/icon.supercollider.png"
    );

    w = SCWindow.new("SCImage", Rect(120, 400, 360, 180)).front;
    w.onClose_({ i.free }); // free the image when the window is closed
    w.drawFunc_({
        i.drawInRect(Rect(10, 10, 50, 50), Rect(10, 10, 50, 50), 2, 1.0); // only a section
    });
)
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `rect` | the [Rect](../Classes/Rect.md) where to draw it |  
| `fromRect` | the portion of the SCImage to use |  
| `operation` | the compositing operation to use. `'sourceOver'` is the default. |  
| `fraction` | the opacity to use, ranging from 0.0 (fully transparent) to 1.0 (fully opaque) |  

### `tileInRect`
tile the image or a portion of it in a specified rectangle of the current graphic context. This may stretch the image depending on the destination rect.
```supercollider
(
    i = SCImage.new(
        // "http://supercollider.sourceforge.net/theme/sc01/icon.supercollider.gif"
        SCDoc.helpSourceDir +/+ "images/icon.supercollider.png"
    );

    w = SCWindow.new("SCImage", Rect(120, 400, 360, 180)).front;
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
| `fromRect` | the portion of the SCImage to use |  
| `operation` | the compositing operation to use. `'sourceOver'` is the default.
> **Note:** Compositing operations are currently disabled for tileInRect |  
| `fraction` | the opacity to use, ranging from 0.0 (fully transparent) to 1.0 (fully opaque) |  


### Instance Methods / accessing and setting pixels
### `setPixel`
fill a pixel located at x @ y.
```supercollider
i = SCImage.color(60, 60, Color.blue(0.1, 0.1));
w = i.plot;
i.setPixel([255, 0, 0, 255].asRGBA, 0, 0); // setting red
w.refresh;
("pixel at 0 @ 0:"+i.getPixel(0, 0).rgbaArray).postln;
i.free;
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `rgbaInteger` | an 32 bit [Integer](../Classes/Integer.md) containing color information packed as 8bit RGBA |  

### `getPixel`
retrieve the pixel value at x @ y as a RGBA integer
```supercollider
// A simple example on how to manipulate pixels with SCImage
b = Int32Array[
    Integer.fromRGBA(255, 0, 0, 255), // red
    Integer.fromRGBA(0, 255, 0, 255), // green
    Integer.fromRGBA(0, 0, 255, 255), // blue
    Integer.fromRGBA(255, 0, 255, 255) // purple
];

b[0].red; // 255 see Integer.red
b[0].green; // 0 see Integer.green
b[0].blue; // 0 see Integer.blue
b[0].alpha; // 255 see Integer.alpha

a = SCImage.new(b.size@1).pixels_(b).interpolation_(\none);
a.plot;


// Set + Get
a.setPixel([255, 0, 255, 128].asRGBA /* create an Integer from 0-255 integer rgba value */, 0, 0).plot;
p = a.getPixel(0, 0);

p.red; // 255
p.green; // 0
p.blue; // 255
p.alpha; // 128

// now another important example
a.setPixel([255, 0, 255, 0].asRGBA, 1, 0).plot; // clear color -> alpha is 0
p = a.getPixel(1, 0);

p.red; // you expect 255 but you get 0 ??? Why = because SCImage uses premultiplied color component value internally
// meaning all Red, Green, and Blue component are premultiplied by the alpha
// if alpha is 0 you get 0 back for all components.

p.green; // 0
p.blue; // 0
p.alpha; // 0

p = a.getColor(1, 0); // more explicit - but same here
```


### `setColor`
fill the pixel located at x @ y with the specified **color**.
### `getColor`
retrieve the pixel value at x @ y as a [Color](../Classes/Color.md).
### `pixels`
retrieve or set all the pixels of the receiver.
> **Note:** Carefull: the returned Array is a [Int32Array](../Classes/Int32Array.md) of size receiver.width * receiver.height containing all pixel values as 32bit Integer

**Arguments:**

| Argument | Description |
|----------|-------------|
| `array` | an [Int32Array](../Classes/Int32Array.md) of size receiver.width * receiver.height containing all pixel values as 32bit Integer |  

### `loadPixels`
load all the pixels of the receiver in an array. it is better and faster to call this function instead of [#-pixels](#-pixels) if you plan to retrieve frequently the pixel data (since it won't allocate a new array everytime !)
```supercollider
// exec one line at a time
i = SCImage.new(
    // "http://supercollider.sourceforge.net/theme/sc01/icon.supercollider.gif"
    SCDoc.helpSourceDir +/+ "images/icon.supercollider.png"
);

// first grab the pixels
p = i.pixels;

// do some mods - here invert
i.invert;

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
    i = SCImage.new(20@20);
    i.pixels_(
        Int32Array.fill(i.width * i.height, {
            Integer.fromRGBA(255.rand, 127.rand, 255.rand, 255)
        })
    );
    // i.interpolation_(\none); // uncomment to see the difference
    w = i.plot(freeOnClose: true);
    i.pixels.postln;
)

(
    i = SCImage.color(50@50, Color.white);
    i.setPixels(
        Int32Array.fill(20*20, { Integer.fromRGBA(255.rand, 127.rand, 255.rand, 255) }),
        Rect(10, 10, 20, 20)
    );
    i.interpolation_(\none); // uncomment to see the difference
    w = i.plot(freeOnClose: true);
    i.pixels.postln;
)
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `array` | an [Int32Array](../Classes/Int32Array.md) of size **rect**.width * **rect**.height containing all pixel values as 32bit Integer |  
| `rect` | a rectangle defining the portion to update in the receiver. By default **rect** is nil, meaning full image size. |  
| `start` | the array start index. |  


### Instance Methods / Attributes for SCImageFilter support
see [SCImageFilter](../Classes/SCImageFilter.md) for more info

### `applyFilters`
apply an array of [SCImageFilter](../Classes/SCImageFilter.md) to the image. this should be considered as an in place operation, meaning the SCImage is altered after it.
```supercollider
// ******** Built In CoreImage Generators ********
// Generators are not filters, they actually create an image but do not need an input image
// you just have to create an image of a new size
// ** The Simple Random Filter **
(
f = SCImageFilter.new(\CIRandomGenerator);
a = SCImage.new(500@500);
a.applyFilters(f);
w = a.plot(freeOnClose: true, background: Color.black);
a.bounds.postln;
)

// ** The StarShine example **
(
var width = 500, height = 500, centerVector;

centerVector = [width*0.5, height*0.5];
a = SCImage.new(500@500);
f = SCImageFilter.new(\CIStarShineGenerator);

f.center_(centerVector);
f.radius_(width*0.05);
f.color_(Color.blue);
f.crossWidth_(2.0);
f.crossAngle_(0.0);
f.crossOpacity_(-4.0);

a.applyFilters(f);
w = a.plot(freeOnClose: true, background: Color.gray); // change background to see
)


// ** Starshine + Pixellate + ZoomBlur **
(
var width = 500, height = 500, centerVector;

centerVector = [width*0.5, height*0.5];
a = SCImage.new(500@500);

f = SCImageFilter.new(\CIStarShineGenerator);
g = SCImageFilter.new(\CIPixellate);
h = SCImageFilter.new(\CIZoomBlur);

f.center_(centerVector);
f.radius_(width*0.05);
f.color_(Color.blue);
f.crossWidth_(2.0);
f.crossAngle_(0.0);
f.crossOpacity_(-4.0);
g.center_(centerVector);
h.center_(centerVector);
h.amount_(50);

a.applyFilters([f, g, h]);
w = a.plot(freeOnClose: true, background: Color.black);
)
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `filters` | a SCImageFilter or an array of [SCImageFilter](../Classes/SCImageFilter.md) to be applied |  
| `crop` | the crop region to finally use. This may be required for extending bounds since some SCImageFilter / CoreImageFilters require to set a wider region (to be applied correctly) or may create a huge image. Setting crop to nil sets no crop region. In case the current maximum size of a filtered SCImage is 4096 / 4096. Any larger size will be clipped. by default crop is constrained to the receiver bounds. |  
| `region` | option to constrain the filter to a specific region IN the SCImage. |  

### `filteredWith`
returns a new SCImage, copy of the receiver filtered with an array of SCImageFilter. arguments are the same as [#-applyFilters](#-applyfilters) (except for **region**).
> **Note:** Beware: you are responsible for freeing the newly created SCImage !!!


### `filters`
filters is the instance variable that holds the array of SCImageFilter attached to the receiver. This is a convenient for applying filters out place and changing the SCImageFilter's attributes. see [#-addFilter](#-addfilter), [#-removeFilter](#-removefilter)see [SCImageFilter](../Classes/SCImageFilter.md) for an example on how to use the **filters** array.
### `addFilter`
you can also attach filters to the receiver for real-time changing operations. In this case the receiver will create a cache before each rendering to maintain its previous state, and allowing you to use filters without applying them in place. The cache is managed directly by the receiver. you can add several filters to the receiver, the first filter in the array is the first applied in the rendering chain.see [SCImageFilter](../Classes/SCImageFilter.md) for an example on how to use **addFilter**.**Arguments:**

| Argument | Description |
|----------|-------------|
| `filter` | a SCImageFilter to apply before rendering of the image |  

### `removeFilter`
see [SCImageFilter](../Classes/SCImageFilter.md) for an example on how to use **removeFilter**.**Arguments:**

| Argument | Description |
|----------|-------------|
| `filter` | the SCImageFilter to remove from the rendering chain. |  

### `flatten`
if [#-filters](#-filters) is not zero sized, this method will apply all those filters in place. if the image is accelerated this method force a bitmap representation of the receiver.
### `invert`
invert the receiver
```supercollider
(
i = SCImage.new("/Library/Desktop Pictures/Ripples Blue.jpg");
i.invert;
i.plot(freeOnClose: true);
)
```


### `crop`
crop the receiver
```supercollider
(
i = SCImage.new("/Library/Desktop Pictures/Ripples Blue.jpg");
i.crop(Rect(10, 10, 120, 100));
i.plot(freeOnClose: true);
)
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `aRect` | the cropping region |  


### Instance Methods / Attributes for SCImageKernel support
see [SCImageKernel](../Classes/SCImageKernel.md) for examples and more info.

### `applyKernel`
apply a Kernel in place. the receiver is modified after this call.**Arguments:**

| Argument | Description |
|----------|-------------|
| `kernel` | a [SCImageKernel](../Classes/SCImageKernel.md) |  


## Examples


### Views addition
you can now use a SCImage as a valid view background. 16 drawing modes are defined to behave differently.


**tileMode values:**
: | 1 | fixed to left, fixed to top | 
| --- | --- || 2 | horizontally tile, fixed to top | | 3 | fixed to right, fixed to top | | 4 | fixed to left, vertically tile | | 5 | horizontally tile, vertically tile | | 6 | fixed to right, vertically tile | | 7 | fixed to left, fixed to bottom | | 8 | horizontally tile, fixed to bottom | | 9 | fixed to right, fixed to bottom | | 10 | fit | | 11 | center, center (scale) | | 12 | center, fixed to top | | 13 | center, fixed to bottom | | 14 | fixed to left, center | | 15 | fixed to right, center | | 16 | center, center (no scale) |

**SCView: backgroundImage_**
: **image** - the SCImage to use**tileMode** - the mode to use. by default fixed to left, fixed to top**alpha** - opacity 0 < x < 1**fromRect** - the portion of the image to use. by default use the full image.






```supercollider
(
    b = 1.0;
    a = SCImage.new(SCDoc.helpSourceDir +/+ "images/vduck2.jpg");
    r = Rect(20, 3, 40, 40);
    w = SCWindow.new("SCImage background" /*, textured: false*/);
    w.view.background_(Color.gray);
    w.view.backgroundImage_(a, 5, b, r);
    w.front;
)

// monte carlo :) exec every line to test
// r = nil; // uncomment for full image
w.view.backgroundImage_(a, 1, b, r);
w.view.backgroundImage_(a, 2, b, r);
w.view.backgroundImage_(a, 3, b, r);
w.view.backgroundImage_(a, 4, b, r);
w.view.backgroundImage_(a, 5, b, r);
w.view.backgroundImage_(a, 6, b, r);
w.view.backgroundImage_(a, 7, b, r);
w.view.backgroundImage_(a, 8, b, r);
w.view.backgroundImage_(a, 9, b, r);
w.view.backgroundImage_(a, 10, b, r);
w.view.backgroundImage_(a, 11, b, r); // find best ratio - move to see
w.view.backgroundImage_(a, 12, b, r);
w.view.backgroundImage_(a, 13, b, r);
w.view.backgroundImage_(a, 14, b, r);
w.view.backgroundImage_(a, 15, b, r);
w.view.backgroundImage_(a, 16, b, r);

// this is safe even if window is still open because Background object holds the SCImage
a.free;

w.close;

(
    a = SCImage.new("/Library/Desktop Pictures/Ripples Blue.jpg");
    w = SCWindow.new("SCImage background");
    l = SC2DSlider.new(w, Rect(10, 10, 200, 200))
        .backgroundImage_(a, 5, 1, Rect(0, 0, 10, 10));
    w.front;
    a.free; // safe
)

(
    var bounds = Rect(10, 10, 150, 18);
    a = SCImage.new("/Library/Desktop Pictures/Ripples Blue.jpg");
    w = SCWindow.new("SCImage background");
    l = SCSlider.new(w, bounds)
        .backgroundImage_(a);
    w.front;
    a.free; // safe
)
```






