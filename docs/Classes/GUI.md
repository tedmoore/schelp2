# GUI

*Factory abstraction for all GUI related core classes*

**Categories:** GUI>Kits

**Related:** [Overviews/GUI-Classes](../Overviews/GUI-Classes.md), [GUI-Introduction](../Guides/GUI-Introduction.md)

## Description

SuperCollider currently supports three operating system platforms: macOS, UNIX (Linux and FreeBSD) and Windows (with some limitations).
> **⚠️ Warning:** The redirect system has been deprecated, please use the view classes directly. If you find old code that uses prefixes for the old GUI Kits (e.g. SCWindow for CocoaGUI), try dropping the prefixes to Window, Button etc. The Qt prefix Q, as e.g. in QWindow, is converted to Window automatically; still it is better style to simply write Window.
Switching between GUI schemes is not needed anymore, as Qt runs well on all platforms. Still, you can get the available schemes with:

```
GUI.schemes;
```


For a complete list of historical gui classes and their redirects, see [GUI-Classes](../Overviews/GUI-Classes.md).


## Class Methods


### `new`


### `makeGUI`


### `initClass`
Sets the `skin` to default values on compile.
```
fontSpecs: ["Helvetica", 10],
fontColor: Color.black,
background: Color(0.8, 0.85, 0.7, 0.5),
foreground: Color.grey(0.95),
onColor: Color(0.5, 1, 0.5),
offColor: Color.clear,
gap: 0@0,
margin: 2@2,
buttonHeight: 16
```



### `add`


### `qt`
Makes QtGUI the current scheme and returns it. Subsequent GUI object calls to GUI are delegated to Qt. Returns the current (Qt) scheme.

### `fromID`
Changes the current scheme and returns the new scheme.**Arguments:**

| Argument | Description |
|----------|-------------|
| `id` | A [Symbol](../Classes/Symbol.md). The identifier of the scheme to use. |  


### `current`
Returns the current scheme. This is useful for objects that, upon instantiation, wish to store the then-current scheme, so as to be able to consistently use the same scheme in future method calls.
> **Note:** the caller shouldn't make any assumptions about the nature (the class) of the returned object, so that the actual implementation (an Event) may change in the future.



### `get`
Returns the scheme for a given identifier. Does not switch the current scheme.**Arguments:**

| Argument | Description |
|----------|-------------|
| `id` | A [Symbol](../Classes/Symbol.md). The identifier of the scheme to retrieve, such as returned by calling `aScheme.id`. |  


### `set`
Changes the current scheme.**Arguments:**

| Argument | Description |
|----------|-------------|
| `aScheme` | An instance of [Symbol](../Classes/Symbol.md). The scheme to use as current scheme. |  


### `use`
Executes a function body, temporarily setting the current GUI scheme. This is useful inside view's action functions in order to make this function use the GUI scheme that was originally used for the view of the action, even if the scheme has been switched meanwhile.**Arguments:**

| Argument | Description |
|----------|-------------|
| `aScheme` | The scheme to use during the function execution. |  
| `func` | An Instance of [Function](../Classes/Function.md). |  


### `useID`
Same as `use` but using a scheme's id as first argument.**Arguments:**

| Argument | Description |
|----------|-------------|
| `id` | The id of the scheme to use during the function execution. |  
| `func` | A body to execute. |  


### `add`
Registers a new scheme. This is typically called by external libraries in their startup procedure. If a scheme with the same identifier (`scheme.id`) exists, it is overwritten.**Arguments:**

| Argument | Description |
|----------|-------------|
| `aScheme` | The scheme to add. |  


### `doesNotUnderstand`
All method calls are mapped to the current scheme, so that for example `GUI.button` can be used and is delegated to the button association of the current scheme.**Arguments:**

| Argument | Description |
|----------|-------------|
| `selector` |  |  
| `... args` |  |  


### `setSkin`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `skinName` |  |  


### `scheme`
A class variable. Returns the current scheme.

### `schemes`
A class variable. Returns an [IdentityDictionary](../Classes/IdentityDictionary.md) of registered schemes.

### `skin`
A class variable. Returns the current skin.

### `skins`
A class variable. Returns an [IdentityDictionary](../Classes/IdentityDictionary.md) of registered skins.

