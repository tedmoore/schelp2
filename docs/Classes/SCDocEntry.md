# SCDocEntry

*An SCDoc document index entry*

**Related:** [SCDoc](../Classes/SCDoc.md)

**Categories:** HelpSystem

## Description

This class is used by [SCDoc](../Classes/SCDoc.md) to represent a document in the help file index.
The document represented can be either a real .schelp file, or an auto-generated stub for undocumented classes.


## Class Methods

### `new`
Create and initialize a new instance.**Arguments:**

| Argument | Description |
|----------|-------------|
| `node` | An [SCDocNode](../Classes/SCDocNode.md) instance. Does not have to be a fully parsed document, since only the header tags, methods and keywords are used. (See [SCDoc#*parseFileMetaData](../Classes/SCDoc.md#*parsefilemetadata)). |  
| `path` | A [String](../Classes/String.md) for the document key, like "Classes/SinOsc". |  

### `newUndocClass`
Create and initialize a new instance for an undocumented class.**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` | Name of undocumented class |  


## Instance Methods


### Document properties
### `path`
A [String](../Classes/String.md) for the document key, like "Reference/SCDocSyntax".
### `title`
Document title. Should equal the classname for class reference docs.
### `summary`
Document summary.
### `categories`
Document categories. An [Array](../Classes/Array.md) of Strings.
### `related`
Related document links. An [Array](../Classes/Array.md) of Strings.
### `keywords`
Keywords listed in the document. An [Array](../Classes/Array.md) of Strings.
### `fullPath`
The full path to this documents .schelp file, if any.
### `mtime`
The modification time of the .schelp file, if any.
### `destPath`
The render destination path.
### `docmethods`
Documented methods which are not class or instance methods. An [Array](../Classes/Array.md) of Strings.
### `additions`
A list of document additions (*.ext.schelp) for this document. An [Array](../Classes/Array.md) of Strings.
### `isExtension`
True if this document is an extension (not part of the main library). A [Boolean](../Classes/Boolean.md)
### `isClassDoc`
True if this document is a class doc. A [Boolean](../Classes/Boolean.md)

### Class docs
These methods and properties are only used for class docs.

### `klass`
The [Class](../Classes/Class.md) documented.
### `isUndocumentedClass`
True if this class is undocumented (which means there are no .schelp file). A [Boolean](../Classes/Boolean.md)
### `doccmethods`
A list of documented class methods.
### `docimethods`
A list of documented instance methods.
### `privcmethods`
A list of private class methods.
### `privimethods`
A list of private instance methods.
### `undoccmethods`
A list of undocumented class methods.
### `undocimethods`
A list of undocumented instance methods.
### `makeMethodList`
Return a list of strings for all non-private methods, prefixed with `xy` where x is `_` for documented methods and `?` for undocumented methods, and y is `*` for class methods, `-` for instance methods and `.` for other/generic methods.
### `redirect`
The name of the class variable holding the implementing class. Used by GUI redirection system, for example.
### `implKlass`
The implementing [Class](../Classes/Class.md), if `redirect` was set.
### `implements`
The [Class](../Classes/Class.md) being implemented. For example, the entry for [QButton](../Classes/QButton.md) has this set to [Button](../Classes/Button.md)
### `toJSON`
Write a representation of this document entry as JSON to Stream. Used to export the document entries to the javascript used in the [HTML help browser](../Classes/HelpBrowser.md).**Arguments:**

| Argument | Description |
|----------|-------------|
| `stream` | A Stream. |  



