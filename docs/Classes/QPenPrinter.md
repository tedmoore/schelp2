# QPenPrinter

*QPen PDF export and printing of vector graphics*

**Categories:** GUI>Accessories

**Related:** [Pen](../Classes/Pen.md)

## Description

QPenPrinter allows Pen to operate on a printer device. The graphics can be exported to PDF by using "print to file" as printer device.


## Class Methods


### `new`
Create a new QPenPrinter object.**Returns:** an instance of QPenPrinter
### `print`
Convenience function to show a print dialog and print.**Arguments:**

| Argument | Description |
|----------|-------------|
| `printFunc` | A [Function](../Classes/Function.md) to be evaluated when the user presses "Print", with the printer object as Pen painter target. See **aPrintFunc** in [#-print](#-print) below. |  
| `cancelFunc` | An optional [Function](../Classes/Function.md) to be evaluated if the user presses "Cancel". |  


## Instance Methods


### Printing
### `showDialog`
Shows a Print Dialog to allow the user to configure the printer object. This is asynchronous and the method will return immediately. When the user presses the "Print" button, **aOkFunc** is called with this QPenPrinter object as argument.**Arguments:**

| Argument | Description |
|----------|-------------|
| `aOkFunc` | A [Function](../Classes/Function.md) to be evaluated when the user presses "Print". |  
| `aCancelFunc` | An optional [Function](../Classes/Function.md) to be evaluated if the user presses "Cancel". |  

### `print`
This method does the actual printing or PDF export. It evaluates **aPrintFunc** with the printer object as Pen painter target. This QPenPrinter object is passed as the argument.All the ordinary [Pen](../Classes/Pen.md) commands can be used inside the function.**Arguments:**

| Argument | Description |
|----------|-------------|
| `aPrintFunc` | A [Function](../Classes/Function.md) to be evaluated to draw the graphics. |  
If this method is called without configuring the printer object first, it will print on the default printer with default settings.This method is typically called from within the **aOkFunc** of [#-showDialog](#-showdialog) above. After showDialog has configured the printer once, this method can be called multiple times to reuse the last printer configuration.The point at (0@0) will coincide with the origin of [#-pageRect](#-pagerect), which is offset by the page margins. So you don't need to translate the Pen.
### `newPage`
Starts a new page. Typically called within the **aPrintFunc** of [#-print](#-print).

### Properties
### `paperRect`
Get the paper bounds.**Returns:** a [Rect](../Classes/Rect.md)
### `pageRect`
Get the page bounds, which is the printable area and usually smaller than [#-paperRect](#-paperrect) due to margins.**Returns:** a [Rect](../Classes/Rect.md)The **origin** of the Rect is relative to the paper, and will be non-zero due to margins.
### `pageSize`
Get the page size as a Size.**Returns:** a [Size](../Classes/Size.md)This can be used to scale the graphics to fit the page if the bounds of the graphics is known:
```supercollider
x = penPrinter.pageSize.width / bounds.width;
Pen.scale(x, x);
// ... draw stuff here ...
```



### Page range
The methods below returns the page range selected by the user. Page number starts at 1. When both methods returns 0 it means "print all pages".

### `fromPage`
Get the start page.**Returns:** an [Integer](../Classes/Integer.md)
### `toPage`
Get the end page.**Returns:** an [Integer](../Classes/Integer.md)

## Examples

Simple usage:

```supercollider
QPenPrinter.print {
    // first page
    Pen.moveTo(100@100);
    Pen.lineTo(300@300);
    Pen.stroke;

    // second page
    p.newPage;
    Pen.addRect(p.pageSize.asRect);
    Pen.stroke;
}
```


Keep the QPenPrinter object to save configuration state:

```supercollider
p = QPenPrinter();
```


The code below can then be called multiple times:

```supercollider
p.showDialog {
    p.print {
        // first page
        Pen.moveTo(100@100);
        Pen.lineTo(300@300);
        Pen.stroke;

        // second page
        p.newPage;
        Pen.addRect(p.pageSize.asRect);
        Pen.stroke;
    }
} {
    "Printing cancelled!".postln;
};
```




