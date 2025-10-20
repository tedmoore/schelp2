# HelpBrowser

**Categories:** HelpSystem, GUI>Interfaces

**Related:** [SCDoc](../Classes/SCDoc.md)

*Browse the SuperCollider help documentation*

## Description

HelpBrowser is a GUI help browser that lets you browse the documentation of SuperCollider. It is coupled with SCDoc to allow on-the-fly rendering of HTML help files.
There are two different help browsers in SuperCollider: the help browser built into SCIDE, and this HelpBrowser class implemented with sclang's GUI features. Both are implemented with the same underlying Qt WebEngine browser.
Since the Qt WebEngine dependency is hefty and difficult to install on some systems, it is possible for sclang to have been built without WebView support (using the CMake flag `-DSC_USE_QTWEBENGINE=OFF` at compile). If so, attempting to invoke this class will throw an error.

### Keyboard shortcuts
Unlike the help browser built into SCIDE, the HelpBrowser offers vim-like keyboard shortcuts for navigation, along with several additional features that enhance workflow efficiency for those who prefer keyboard-based interaction.

| **Shortcut** | **Functionality** | 
| --- | --- || j | scroll down | | k | scroll up | | ctrl + d | scroll more lines down | | ctrl + u | scroll more lines up | | h or alt + left arrow | go back | | l or alt + right arrow | go forward | | G | go to bottom  | | g | go to top | | shift + j or ctrl + minus | zoom out | | shift + k or ctrl + plus | zoom in | | / or ctrl + f | search in page | | F3 | open Search page | | F5 | reload page | | t | toggle TOC | | ctrl+{j,k} | scroll in TOC | | ESC | close TOC | 



## Class Methods



### `instance`
The singleton HelpBrowser instance.

### `new`
Create a new HelpBrowser instance with given home URL.

### `defaultHomeUrl`
Get or set the default home URL.

### `openNewWindows`
Get or set the default for "open in new windows" toggle.

### `goTo`
Go to url with singleton instance or a new window, depending on the `openNewWindows` setting.

### `openHelpFor`
Open the relevant help page for given text in the singleton HelpBrowser instance.

### `openSearchPage`
Open the help search page with given text in the singleton HelpBrowser instance.

### `openBrowsePage`
Open the category browser page in the singleton HelpBrowser instance.**Arguments:**

| Argument | Description |
|----------|-------------|
| `category` | An optional String to start at specified category, like "UGens>Filters" |  


### `openHelpForMethod`
Open help for specified method.**Arguments:**

| Argument | Description |
|----------|-------------|
| `method` | a [Method](../Classes/Method.md) |  


## Instance Methods


### `homeUrl`
Get or set the home URL.
### `window`
The GUI window for this HelpBrowser.Mainly useful for when you need to show the browser:
```
HelpBrowser.instance.window.front;
```


### `goTo`
Go to specific URL. If the URL points to a file under [SCDoc#*helpTargetDir](../Classes/SCDoc.md#*helptargetdir) it will be rendered on demand if needed.
### `goHome`
Go to the home URL.
### `goBack`
Go back.
### `goForward`
Go forward.

