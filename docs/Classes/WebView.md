# WebView

*Web page display and browser*

**Categories:** GUI>Views

## Description

WebView displays web pages and provides all the standard browsing functionality.
Since the Qt WebEngine dependency is hefty and difficult to install on some systems, it is possible for sclang to have been built without WebView support (using the CMake flag `-DSC_USE_QTWEBENGINE=OFF` at compile). If so, attempting to invoke this class will throw an error.


## Class Methods


### `clearCache`
 Clears the cache for all browser instances.
### `setUrlHandler`
 Set or clear a function to handle a specific URL prefix (e.g. [mail://)](../mail://).md)**Arguments:**

| Argument | Description |
|----------|-------------|
| `prefix` | URL prefix. For [mail:///](../mail:///.md), use the string "mail" (do not append "://") |  
| `function` | Function to execute when any WebView loads a URL with this prefix. First argument is the URL. |  


## Instance Methods


### Navigation
### `url`
 Gets the current URL, or navigates to a new one. This is equivalent to entering a URL in a browser's URL box.
### `navigate`
 Navigate to a url. This is equivalent to clicking a link on a page - after a navigate call, back will return you to the previous page.
### `back`
 Navigates to the previous page in history.
### `forward`
 Navigates to the next page in history.
### `findText`
 Finds and selects the next instance of given text on the current page. When the given text changes, the search starts anew.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | The text to find; a String. |  
| `` | Whether to search in reverse direction; a Boolean. |  
| `` | A function, called when the operation is finished. If the text was found this function is passed `true`, otherwise `false`. |  

### `triggerPageAction`
 Trigger an action on the current page. Possible actions include: reload, select all, copy, undo, redo (see [QWebPageAction](../Classes/QWebPageAction.md))**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A QWebPageAction. |  
| `` | A Boolean to enable or disable the action (applies to only some actions). |  


### Data
### `setHtml`
 Set the HTML displayed in the view.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A String. |  
| `` | A url. The browser will interpret this to be the current page location. |  

### `setContent`
 Set the raw content of a web view. This can be used to display binary data such as image / movie files.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | An Int8Array containing data. |  
| `` | A mime type, of the form e.g. "image/jpeg" |  
| `` | A url. The browser will interpret this to be the current page location. |  

### `setAttribute`
 Set a QWebAttribute for the view. Attributes can affect behavior such as caching, auto-loading images, file url access, etc.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A QWebAttribute. |  
| `` | A Boolean. |  

### `testAttribute`
 Check the enablement state of a QWebAttribute.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A QWebAttribute. |  
**Returns:** A Boolean.
### `resetAttribute`
 Reset the enablement state of a QWebAttribute.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A QWebAttribute. |  

### `toPlainText`
 Convert the page to plain text.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A callback function. Called with the resulting plain text string when the operation is finished. |  

### `toHtml`
 Fetch the HTML of the current page.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A callback function. Called with the resulting HTML string when the operation is finished. |  

### `title`
 The title of the current page.**Returns:** A String.
### `requestedUrl`
 The requested url for the current page.**Returns:** A String.
### `selectedText`
 The currently selected text.**Returns:** A String.

### Behavior and appearance
### `audioMuted`
 Get or set audio mute setting for the view;**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `contentsSize`
 Get the size of the current content.**Returns:** A Point
### `scrollPosition`
 Get or sets the scroll position of the current page.**Returns:** A Point
### `hasSelection`
 Returns whether the page has a text selection.**Returns:** A Boolean.
### `enterInterpretsSelection`
 Whether pressing Ctrl+Return or Ctrl+Enter while some text is selected should evaluate the selection as SuperCollider code.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `setFontFamily`
 Sets a specific font family to be used in place of a CSS-specified generic font family.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | The CSS generic font family to assign a font to; one of [QWebFontFamily](../Classes/QWebFontFamily.md) |  
| `` | A font family name to be assigned to the generic family; a String. |  

### `zoom`
 Gets or sets the zoom level on a page.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Number, where 1.0 is the default zoom. |  

### `editable`
 Get or set whether the entire web page is editable.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  

### `pageBackgroundColor`
 Get or set the default background color of web pages.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  


### Actions
### `onAudioMutedChanged`
 Sets the object to be evaluated when the mute setting of the view has changed.
### `onRecentlyAudibleChanged`
 Sets the object to be evaluated when the page has started or stopped playing audio.
### `onContentsSizeChanged`
 Sets the object to be evaluated when the contents size of the view has changed
### `onScrollPositionChanged`
 Sets the object to be evaluated when the scroll position on a page has changed.
### `onSelectionChanged`
 Sets the object to be evaluated when the text selection on a page has changed.
### `onJavaScriptMsg`
 Sets the object to be evaluated when a javascript console message is posted.
### `onLinkHovered`
 Sets the object to be evaluated when a the mouse rolls over a link.
### `onTitleChanged`
 Sets the object to be evaluated when the title of the displayed page changes.
### `onUrlChanged`
 Sets the object to be evaluated when the url of the displayed page changes.
### `onLoadProgress`
 Sets the object to be evaluated with load progress updates.
### `onLoadStarted`
 Sets the object to be evaluated when a page load begins.
### `onLoadFinished`
 Sets the object to be evaluated when a page has loaded successfully, passing the view as the argument.
### `onLoadFailed`
 Sets the object to be evaluated when a page has failed to load, passing the view as the argument.
### `overrideNavigation`
 When true, page navigation requests will not be handled. Use in combination with onLinkActivated to provide custom navigation behavior.
### `onLinkActivated`
 Sets the object to be evaluated when the user triggers a link. Arguments are: a URL, a QWebPageNavigationType, a bool (page is opening in current view). When this is set to other than nil, WebView will stop handling clicked links altogether. Setting this to nil will restore WebView link handling again.  Note: for specialty behavior when clicking on links, it is much better to use setUrlHandler in most cases.
### `onReloadTriggered`
 Sets the object to be evaluated whenever a page reload is requested, passing the view and the URL to be reloaded (as String) as the arguments.

### JavaScript
### `runJavaScript`
 Evaluates the given JavaScript code in the context of the current page.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A String. |  
| `` | A function to be called when execution is complete, with the result as first argument.
> **Note:** javascript code can correctly return Numbers, Strings and Arrays, but it can't currently pass javascript Objects to sclang. It is possible however to use JSON serialization to acheive this:


```supercollider
// passing a nested object from javascript to sclang:
WebView().runJavaScript("JSON.stringify({ a: [1,2,3], b: { ba: 1, bb: 'yeah' } })"){ |res| res.parseJSON.postln }
``` |  


## Examples


```supercollider
// A simple web browser
(
var browser, webview, reloadStop, prev, next, urlBox, go;

webview = WebView()
    .minSize_(300@200);
reloadStop = Button()
    .states_([["※"], ["◙"]])
    .fixedSize_(36@28);
prev = Button()
    .states_([["⇦"]])
    .fixedSize_(36@28);
next = Button()
    .states_([["⇨"]])
    .fixedSize_(36@28);
urlBox = TextField()
    .minWidth_(100);
go = Button()
    .states_([["⌘"]])
    .fixedSize_(36@28);

reloadStop.action = {
    |v|
    if (v.value == 1) {
        webview.reload(true);
    } {
        webview.stop;
    }
};

prev.action = { webview.back };
next.action = { webview.forward };
urlBox.action = { webview.url = urlBox.string };
go.action = { webview.url = urlBox.string };

webview.onUrlChanged = {
    |view, url|
    urlBox.string = url;
};

webview.onLoadStarted = {
    reloadStop.value = 1;
    urlBox.background = Color.grey(0.4);
};

webview.onLoadFinished = {
    reloadStop.value = 0;
    urlBox.background = Color.grey(0.2);
};

webview.onLoadFailed = {
    reloadStop.value = 0;
    urlBox.background = Color.red(1, 0.2);
};

browser = View(bounds: 900@700).layout_(VLayout(
    HLayout(
        prev, reloadStop, next,
        urlBox,
        go
    ),
    webview
));

browser.front;

urlBox.valueAction = "http://supercollider.github.io/"
)
```




