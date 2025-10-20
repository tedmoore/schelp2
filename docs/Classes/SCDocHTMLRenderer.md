# SCDocHTMLRenderer

*Render SCDoc markup text to HTML*

**Categories:** HelpSystem

**Related:** [SCDoc](../Classes/SCDoc.md), [WritingHelp](../Guides/WritingHelp.md), [SCDocSyntax](../Reference/SCDocSyntax.md), [SCDocStyling](../Reference/SCDocStyling.md)

## Description

This class is part of the SCDoc help system, and handles the rendering of the parsed document tree into HTML output.
In normal cases you won't need to use this class directly, [SCDoc](../Classes/SCDoc.md) uses this class by default to render help files.
For CSS styling, see [SCDocStyling](../Reference/SCDocStyling.md).


## Class Methods


### `renderOnStream`
Renders a parsed document as HTML onto given stream.**Arguments:**

| Argument | Description |
|----------|-------------|
| `stream` | A stream, for example a [File](../Classes/File.md) instance. |  
| `doc` | An instance of [SCDocEntry](../Classes/SCDocEntry.md) |  
| `root` | An instance of [SCDocNode](../Classes/SCDocNode.md) |  


### `renderToFile`
Opens a file and passes it to [#*renderOnStream](#*renderonstream)

### `htmlForLink`
Create a html string for the given scdoc link.**Arguments:**

| Argument | Description |
|----------|-------------|
| `link` | An scdoc link, such as a document key like "Classes/SinOsc", or an URL, or link to other file installed with the help. |  
| `escape` | a boolean to set whether to escape special characters. |  
**Returns:** A String

### `makeArgString`
Used internally.**Returns:** A [String](../Classes/String.md) representing the arguments (with defaults) for a [Method](../Classes/Method.md).

## CSS styling
The rendered HTML reads the global style from `scdoc.css`, but also reads `frontend.css` and `custom.css` (in that order) if available, to enable specific frontends and users to override the CSS.

So to customise the CSS, the user can create a `custom.css` in their [SCDoc#*helpTargetDir](../Classes/SCDoc.md#*helptargetdir) or at the root of any HelpSource directory (for example in `YourExtension/HelpSource/custom.css`).



