# Dialog

*Shows various system dialogs*

**Categories:** GUI>Accessories

**Related:** [FileDialog](../Classes/FileDialog.md), [File](../Classes/File.md)

## Description

This class allows to show various system dialogs. [#*openPanel](#*openpanel) will show a dialog for selecting a file to open, and [#*savePanel](#*savepanel) will show a dialog for selecting or creating a file to save to.
The methods here are convenience functions built on top of [FileDialog](../Classes/FileDialog.md).


## Class Methods


### `openPanel`
 Shows a dialog for selection of an existing file (or multiple files) to open. It does not do anything with the file, instead it just passes the chosen filenames to the given result handler.**Arguments:**

| Argument | Description |
|----------|-------------|
| `okFunc` | An object to be evaluated when OK is pressed. As argument, either a single filename is passed as a String, or an Array of Strings for multiple selected items is passed, depending on the **multipleSelection** argument. The paths will always be absolute paths. |  
| `cancelFunc` | An object to be evaluated when Cancel is pressed. |  
| `multipleSelection` | A Boolean indicating whether multiple files can be selected. |  
| `path` | A string. The dialog will initially display the contents of this path. The default is the current  user's home directory. |  
Example:
```supercollider
(
Dialog.openPanel({ |path|
    path.postln;
}, {
    "cancelled".postln;
});
)
```


### `savePanel`
 Shows a dialog for selecting or creating a file to save to. It does not do anything with the selected file, and does not create any file; instead it just passes the chosen filename to the given result handler.**Arguments:**

| Argument | Description |
|----------|-------------|
| `okFunc` | An object to be evaluated when OK is pressed. The chosen filename (as an absolute path) is passed as a String as argument. If the file already exists, the user will be asked to confirm. |  
| `cancelFunc` | An object to be evaluated when Cancel is pressed. |  
| `path` | A string. The dialog will initially display the contents of this path. The default is the current  user's home directory. |  
Example:
```supercollider
(
Dialog.savePanel({ |path|
    path.postln;
}, {
    "cancelled".postln;
});
)
```


### `getPaths`

> **Note:** Deprecated. Use [#*openPanel](#*openpanel) instead.

 Implements the same functionality as *openPanel, only the last argument is named differently and defaults to true.

