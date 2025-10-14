# Document


*Editor-specific text document editing*

**Categories:** Frontends

**Related:** [EmacsDocument](../Classes/EmacsDocument.md), [ScelDocument](../Classes/ScelDocument.md)

## Description

The Document class represents a text document within the context of your text editing environment. You can use the class to programmatically create, modify, and query these documents.
Document used to be an abstract class, meaning it didn't provide all the functionality itself, but instead relied on subclasses to complete the functionality. One such subclass was CocoaDocument. Although CocoaDocument was available only to macOS and had an ad hoc interface, it possessed many additional features like code animation and rich text.
In SuperCollider 3.6, Document changed a bit and now the "abstract class" descriptor is only partially true. The SuperCollider IDE provides its own version of the Document class. The Emacs editor still supplies [ScelDocument](../Classes/ScelDocument.md) (which links to [EmacsDocument](../Classes/EmacsDocument.md)) as a subclass of Document. As an unfortunate byproduct of the history of Document, there are inconsistencies in the APIs of SCIDE's Document and Emacs' ScelDocument. This help file describes that of SCIDE.
Future versions of SuperCollider will aim to fix these API inconsistencies and restore the functionality of CocoaDocument.

### Setting the Environment
By default `envir` it is set to the current [Environment](../Classes/Environment.md). However, you can make it use its own [Environment](../Classes/Environment.md) also. Thus, e.g., if you were to set the [Environment](../Classes/Environment.md) variable `~myVar = 12` in the current [Environment](../Classes/Environment.md), you can create a new Document window in which that [Environment](../Classes/Environment.md) variable is not set.




## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `title` | An instance of [String](../Classes/String.md) or [Symbol](../Classes/Symbol.md). |  
| `string` | An instance of [String](../Classes/String.md). The contents of the document. |  
| `envir` | An instance of [Environment](../Classes/Environment.md). The [Environment](../Classes/Environment.md) to be used by the interpreter of the document window. By default, it is set to the current [Environment](../Classes/Environment.md). |  

```supercollider
Document.new("this is the title", "this is the text");
```


### `open`
Open a document from a path.**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` | The file system path to the document. An instance of [String](../Classes/String.md). |  
| `selectionStart` | The beginning of the cursor selection of the file content. |  
| `selectionLength` | The length of the cursor selection of the file content. |  
| `envir` | An instance of [Environment](../Classes/Environment.md). The Environment to be used by the interpreter of the document window. By default, it is set to the current [Environment](../Classes/Environment.md). |  
See also [Document#save](../Classes/Document.md#save) below.
```supercollider
Document.open("README", 292, 253); // notice the selected text in the open document
```


### `openDocuments`
Returns an Array of all open documents.
```supercollider
d = Document.openDocuments.do{ |doc| doc.name.postln };
```


### `hasEditedDocuments`
Returns true if there are edited Documents.
### `closeAll`
> **⚠️ Warning:** Closes all open Documents, whether edited or not.**Arguments:**

| Argument | Description |
|----------|-------------|
| `leavePostWindowOpen` | An instance of [Boolean](../Classes/Boolean.md). |  

### `closeAllUnedited`
Closes all unedited Documents.**Arguments:**

| Argument | Description |
|----------|-------------|
| `leavePostWindowOpen` | An instance of [Boolean](../Classes/Boolean.md). |  

### `current`
Gets/sets the current Document.**Arguments:**

| Argument | Description |
|----------|-------------|
| `value` | A Document. |  

```supercollider
Document.current.name.postln; // Prints "Document.html"
```


### `allDocuments`
Returns all documents.
### `globalKeyDownAction`
Get/set A global action to be performed when a key is pressed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `action` | An instance of [Function](../Classes/Function.md) or [FunctionList](../Classes/FunctionList.md). |  

### `globalKeyUpAction`
Get/set A global action to be performed when a key is released.**Arguments:**

| Argument | Description |
|----------|-------------|
| `action` | An instance of [Function](../Classes/Function.md) or [FunctionList](../Classes/FunctionList.md). |  

### `initAction`
Get/set A an action to be performed up opening or creating a Document.**Arguments:**

| Argument | Description |
|----------|-------------|
| `action` | An instance of [Function](../Classes/Function.md) or [FunctionList](../Classes/FunctionList.md). |  

### `autoRun`
If autoRun is set to true, documents beginning with the comment `/*RUN*/` will be executed immediately after being opened, and also when the class library is recompiled with the document already open in the IDE.**Arguments:**

| Argument | Description |
|----------|-------------|
| `value` | An instance of [Boolean](../Classes/Boolean.md). Default value is `true`. |  

### `implementationClass`
The editor implementation specific class which will handle Documents.**Arguments:**

| Argument | Description |
|----------|-------------|
| `value` | A class for implementing Document. |  


### Path Utilities
Utilities and settings for dealing with documents such as SuperCollider code files. By default the document directory is SuperCollider's application directory.

### `dir`
Get/set the default document directory. The default is dependent on [#*implementationClass](#*implementationclass).**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` | The file system path to the directory. An instance of [String](../Classes/String.md). |  
In Main-startUp you can set this to a more practical directory:
```supercollider
Document.dir = "~/Documents/SuperCollider";
```


### `standardizePath`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `p` | The file system path to the directory. An instance of [String](../Classes/String.md). |  
If it is a relative path, expand it to an absolute path relative to your document directory. Expand tildes in path (your home directory), resolve symbolic links (but not aliases). Also converts from Mac OS 9 path format. See PathName for more complex needs.
```supercollider
Document.standardizePath("~/"); // This will print your home directory

Document.standardizePath(":Patches:newfoots:fastRuckAndTuck");
// Returns: /Volumes/Macintosh HD/Users/cruxxial/Documents/SC3docs/Patches/newfoots/fastRuckAndTuck

Document.standardizePath("~/Documents/SC3docs/Patches/newfoots/fastRuckAndTuck");
// Returns: Patches/newfoots/fastRuckAndTuck

Document.standardizePath("Patches/newfoots/fastRuckAndTuck")
// Returns: Patches/newfoots/fastRuckAndTuck
```


### `abrevPath`
Returns a path relative to Document.dir, if the path is inside Document.dir.**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` | The file system path to the directory. An instance of [String](../Classes/String.md). |  



## Instance Methods


### General Document Properties
### `path`
Get / set the Document's path.**Arguments:**

| Argument | Description |
|----------|-------------|
| `apath` | An instance of [String](../Classes/String.md). A files system path. |  

```supercollider
Document.current.path.postln;
```


### `dir`
Returns the directory of a Document.
```supercollider
Document.current.dir.postln;
```


### `==`
A binary operator.**Arguments:**

| Argument | Description |
|----------|-------------|
| `that` | An instance of Document. |  

```supercollider
Document.current == Document.listener; // presumably returns false
```


### `editable`
Get / set the document is editable.**Arguments:**

| Argument | Description |
|----------|-------------|
| `bool` | An instance of [Boolean](../Classes/Boolean.md). |  

### `name`
Get / set the title (same as [#-title](#-title)).**Arguments:**

| Argument | Description |
|----------|-------------|
| `aname` | An instance of [String](../Classes/String.md). |  

```supercollider
Document.current.name.postln;
```


### `title`
Get / set the title (same as [#-name](#-name)).**Arguments:**

| Argument | Description |
|----------|-------------|
| `newTitle` | An instance of [String](../Classes/String.md). |  

### `promptToSave`
Get/set whether a document is prompts to save if it has been changed. Use this with caution.**Arguments:**

| Argument | Description |
|----------|-------------|
| `bool` | An instance of [Boolean](../Classes/Boolean.md). |  

### `closed`
Returns `true` if the document has been closed.
### `isEdited`
Returns `true` if the document has been edited.
```supercollider
Document.current.isEdited.postln;
```


### `isFront`
Returns `true` if the document is in front.
### `didBecomeKey`
Saves the current [Environment](../Classes/Environment.md), makes the document current, and performs its [#-toFrontAction](#-tofrontaction).
### `didResignKey`
Performs the Document's [#-endFrontAction](#-endfrontaction) and restores the current [Environment](../Classes/Environment.md).

### Controlling Document
### `close`
Close a document.
```supercollider
(
Task({
    var doc;
    doc = Document("background", "closing in 2 seconds");
    2.wait;
    doc.close;
}).play(AppClock);
)
```


### `save`
Save this Document.**Arguments:**

| Argument | Description |
|----------|-------------|
| `docPath` | An optional instance of [String](../Classes/String.md) indicating the path to save the Document. If a path is not provided, the current path (if it has been previously saved or read) is used. After a successful save, this Document's path will be updated if needed. See also [Document#*open](../Classes/Document.md#*open) above.
```supercollider
d = Document.new("testSave", "foo");
d.save(Platform.defaultTempDir ++ "foo.scd"); // saved in the temp dir
d.string_("foobar", 0, 3);
d.save; // save at previous path
d.string_("save as now", 0, 6);
d.save(Platform.defaultTempDir ++ "savedAs.scd");
d.path;
``` |  

### `front`
Bring a document to the front.
```supercollider
Document.listener.front;
```


### `onClose`
Get/set the action to be performed on closing the document.**Arguments:**

| Argument | Description |
|----------|-------------|
| `value` | An instance of [Function](../Classes/Function.md) or [FunctionList](../Classes/FunctionList.md). |  

### `endFrontAction`
Get/set the action to be performed when the document becomes no longer the front document.**Arguments:**

| Argument | Description |
|----------|-------------|
| `value` | An instance of [Function](../Classes/Function.md) or [FunctionList](../Classes/FunctionList.md). |  

### `toFrontAction`
Get / set the action to be performed when the document become the front document.**Arguments:**

| Argument | Description |
|----------|-------------|
| `value` | An instance of [Function](../Classes/Function.md) or [FunctionList](../Classes/FunctionList.md). |  

### `mouseDownAction`
Get/set the action to be performed on [#-mouseDown](#-mousedown).**Arguments:**

| Argument | Description |
|----------|-------------|
| `action` | An instance of [Function](../Classes/Function.md) or [FunctionList](../Classes/FunctionList.md). The arguments passed to the function are: `document`, `x`, `y`, `modifiers`, `buttonNumber`, `clickCount`. |  

### `mouseUpAction`
Get/set the action to be performed on [#-mouseUp](#-mouseup).**Arguments:**

| Argument | Description |
|----------|-------------|
| `action` | An instance of [Function](../Classes/Function.md) or [FunctionList](../Classes/FunctionList.md). The arguments passed to the function are: `document`, `x`, `y`, `modifiers`, `buttonNumber`. |  

```supercollider
(

// add a mouse action to this document:
// example: easy button:
// when you click in front of a 17 a SinOsc will start up;
s.waitForBoot({
    Document.current.mouseUpAction_({ |doc|
        var char;
        char = doc.rangeText(doc.selectionStart, 2);
        if(char == "17", {
            { EnvGen.kr(Env.perc, doneAction: Done.freeSelf) * SinOsc.ar([600, 720, 300].choose, 0, 0.5) }.play;
        });
        if(char == "23", {
            { EnvGen.kr(Env.perc, doneAction: Done.freeSelf) * PinkNoise.ar(0.2) }.play;
        });
    })
});
)
```

Test here and click in front of the numbers: 17 and 23.
```supercollider
Document.current.mouseUpAction = nil; // clear mouseUpAction
```


### `keyDownAction`
Get/set the action to be performed on [#-keyDown](#-keydown).**Arguments:**

| Argument | Description |
|----------|-------------|
| `action` | An instance of [Function](../Classes/Function.md) or [FunctionList](../Classes/FunctionList.md). The arguments passed to the function are: `document`, `char`, `modifiers`, `unicode`, `keycode`. See [View#Key actions](../Classes/View.md#key-actions) for details on these arguments. |  

```supercollider
Document.current.keyDownAction = { |...args| args.postln };
// now type some text
Document.current.keyDownAction = nil;
```


### `keyUpAction`
Get/set the action to be performed on [#-keyUp](#-keyup).**Arguments:**

| Argument | Description |
|----------|-------------|
| `action` | An instance of [Function](../Classes/Function.md) or [FunctionList](../Classes/FunctionList.md). The arguments passed to the function are: `document`, `char`, `modifiers`, `unicode`, `keycode`. See [View#Key actions](../Classes/View.md#key-actions) for details on these arguments. |  

```supercollider
Document.current.keyUpAction = { |...args| args.postln };
// now type some text
Document.current.keyUpAction = nil;
```



### Accessing and Editing Content
### `selectLine`
Select a line of the document by number.**Arguments:**

| Argument | Description |
|----------|-------------|
| `line` | An [Integer](../Classes/Integer.md). |  

```supercollider
Document.current.selectLine(343);
```


### `selectRange`
Select a text range in the string of the document.**Arguments:**

| Argument | Description |
|----------|-------------|
| `start` | The start index. |  
| `length` | The length of the selection. |  

```supercollider
(
Document.current.selectRange(Document.current.selectLine(355), 150);
)
```


### `selectionStart`
Returns the start of a current selection.
```supercollider
Document.current.selectionStart.postln;
```


### `selectionSize`
Returns the size of a current selection.
```supercollider
(
var doc;
doc = Document.current;
doc.selectRange(doc.selectionStart - 40, 10);
doc.selectionSize.postln;
)
```


### `selectedString`
Gets/sets the selected string.**Arguments:**

| Argument | Description |
|----------|-------------|
| `txt` | An instance of [String](../Classes/String.md). |  

```supercollider
(
var doc;
doc = Document.current;
doc.selectRange(doc.selectionStart - 40, 10);
doc.selectedString.postln;
)
```


### `currentLine`
Returns the current line as a [String](../Classes/String.md).
```supercollider
(
var doc;
doc = Document.current;
doc.selectRange(doc.selectionStart - 40, 10);
doc.currentLine.postln;
)
```


### `getSelectedLines`
Returns all full lines from before `rangestart` to after `rangestart + rangesize` as a [String](../Classes/String.md).
```supercollider
(
var doc;
doc = Document.current;
doc.selectRange(doc.selectionStart - 40, 10);
doc.getSelectedLines(doc.selectionStart - 40, 130).postln;
)
```


### `string`
Gets or sets the string within a certain range.**Arguments:**

| Argument | Description |
|----------|-------------|
| `string` | A [String](../Classes/String.md). |  
| `rangestart` | An [Integer](../Classes/Integer.md). |  
| `rangesize` | An [Integer](../Classes/Integer.md). |  

```supercollider
// Select the following code in parentheses and execute it
(
Document.current.string_(": test test test test test ",
    Document.current.selectionStart,
    18);
)
// Watch me change content
```


### `getText`
Get a range of text from the document. Synchronous. The text is directly returned.**Arguments:**

| Argument | Description |
|----------|-------------|
| `start` | An [Integer](../Classes/Integer.md) for the starting position to access. |  
| `range` | An [Integer](../Classes/Integer.md) for the number of characters to retrieve. -1 retrieves to the end of the document. |  

### `getTextAsync`
Get a range of text from the document. Asynchronous. The text is passed to the `action` function as an argument.
> **Note:** Currently, in Windows, [#-getText](#-gettext) and [#-string](#-string) may be unreliable. Windows users are recommended to use [#-getTextAsync](#-gettextasync) for the time being.

**Arguments:**

| Argument | Description |
|----------|-------------|
| `action` | A function to evaluate after the request is complete. It is passed one argument, a [String](../Classes/String.md), for the retrieved contents. |  
| `start` | An [Integer](../Classes/Integer.md) for the starting position to access. |  
| `range` | An [Integer](../Classes/Integer.md) for the number of characters to retrieve. -1 retrieves to the end of the document. |  


### Subclassing and Internal Methods
The following methods are usually not used directly or are called by a primitive. Programmers can still call or override these as needed.


```supercollider
    *startup
    *numberOfOpen
    mouseUp (x, y, modifiers, buttonNumber, clickCount, clickPos)
    keyDown (character, modifiers, unicode, keycode)
    keyUp (character, modifiers, unicode, keycode)
    getIdentifierCoordFromEnd (endPos)
    dataptr

    Private. Used only internally:
    *newFromIndex (idx)
    *prnumberOfOpen
    *prGetLast
    *prGetIndexOfListener
    *prBasicNew
    prAdd
    prGetLastIndex
    setFont (font, rangeStart, rangeSize)
    setTextColor (color, rangeStart, rangeSize)
    propen (path, selectionStart, selectionLength)
    rangeText (rangestart, rangesize)
    insertTextRange (string, rangestart, rangesize)
    prinitByString (title, str, makeListener)
    prSetBackgroundColor (color)
    prGetBackgroundColor (color)
    prSelectLine (line)
    prIsEditable_ (editable)
    prSetTitle (argName)
    prGetTitle
    prGetFileName
    prSetFileName (apath)
    prGetBounds (argBounds)
    prSetBounds (argBounds)
    prclose
    prinsertText (dataPtr, txt)
    prinitByIndex (idx)
    envir
    envir_ (ev)
    text
    removeUndo
    selectedText
    selectUnderlinedText (clickPos)
    linkAtClickPos (clickPos)
    selectedRangeSize
    restoreCurrentEnvironment
    saveCurrentEnvironment
    initByIndex (idx)
    initLast
    initFromPath (path, selectionStart, selectionLength)
    initByString (argTitle, str, makeListener)
```



## Examples


```supercollider
(
var doc;
doc = Document("", "||");

Task({
    1000.do({
        0.08.wait;
    })
}).play(AppClock);

Task({
    100.do({
        1.01.wait
    })
}).play(AppClock);

Task({
    100.do({
        1.01.wait;
        doc.selectedString_(["\"\n#", "||", "-", "--"].choose);
    })
}).play(AppClock);

Task({
    var co, mul;
    co = 0.1;
    mul = 1.02;
    100.do({
        0.16.wait;
        co = co * mul;
        if(co > 0.99, { co = 0.1 });
    });
    doc.close;
}).play(AppClock)
)
```


A simple implementation of TBT (time based text) [http://tbt.dyne.org/?info=download](http://tbt.dyne.org/?info=download)

```supercollider
// record: type some text
(
var time = Main.elapsedTime;
a = List.new;
r = Routine { |char|
loop {
    a = a.add([char, Main.elapsedTime - time]);
    char = 0.yield;
}
};

Document.new("type some text")
    .keyDownAction = { |doc, key| r.value(key) ; time = Main.elapsedTime };
)

// play back text in time
(
d = Document.new("type some text");
fork({
    a.do { |pair|
        d.string = d.string ++ pair[0];
        pair[1].wait;
    }
}, AppClock)
)
```




