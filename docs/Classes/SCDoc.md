# SCDoc

*Help system main class*

**Categories:** HelpSystem

**Related:** [SCDocSyntax](../Reference/SCDocSyntax.md), [WritingHelp](../Guides/WritingHelp.md), [SCDocHTMLRenderer](../Classes/SCDocHTMLRenderer.md), [SCDocNode](../Classes/SCDocNode.md), [SCDocEntry](../Classes/SCDocEntry.md)

## Description

SCDoc manages the SuperCollider documentation system.
It uses parses help files written in [SCDoc markup language](../Reference/SCDocSyntax.md) and renders them as human-readable documents.
A guide to writing help can be found here: [WritingHelp](../Guides/WritingHelp.md).


## Class Methods


### Document index
### `indexAllDocuments`
Index all documents and undocumented classes on the system, putting them in the `SCDoc.documents` dictionary. If run inside a Routine, this method will yield occasionally.Run this method if you added a new document and want to see the changes without restarting SuperCollider.**Arguments:**

| Argument | Description |
|----------|-------------|
| `clearCache` | If true, force re-render of files even if the schelp source file is not newer than the destination. This will also refresh all static files via [SCDoc#*refreshStaticFiles](../Classes/SCDoc.md#*refreshstaticfiles). |  
This will take a couple of seconds, and will be done automatically once before any help can be viewed. You might consider putting this in your startup.scd file to avoid getting this delay later when you decide to view a helpfile.
### `documents`
The dictionary of indexed documents. They keys are the path relative to the Help folder and without extension, like `Classes/SinOsc` or `Reference/SCDocSyntax`. The values are instances of [SCDocEntry](../Classes/SCDocEntry.md)
### `didIndexDocuments`
A Boolean indicating if `SCDoc.indexAllDocuments` was called in this session yet.
### `helpSourceDir`
get/set the system-wide directory of help sourcefiles. Defaults to `Platform.classLibraryDir.dirname +/+ "HelpSource"` and should typically not be changed by the user.
### `helpSourceDirs`
get the list of HelpSource folders, including extensions and quarks (unless they are excluded from library compilation, e.g. by [LanguageConfig#*excludeDefaultPaths](../Classes/LanguageConfig.md#*excludedefaultpaths))This searches recursively for all folders named "HelpSource" under [LanguageConfig#*includePaths](../Classes/LanguageConfig.md#*includepaths), as well as including the system-wide `helpSourceDir`. Unless [LanguageConfig#*excludeDefaultPaths](../Classes/LanguageConfig.md#*excludedefaultpaths) is on, `Platform.userExtensionDir` and `Platform.systemExtensionDir` are searched too.
### `findHelpFile`
Find help for a given string. Tries to be smart.**Returns:** the URL for help on given string
### `verbosity`
Verbosity level. 0 is silent.


### Parsing and Rendering

### `renderer`
The default renderer, defaults to [SCDocHTMLRenderer](../Classes/SCDocHTMLRenderer.md)
### `helpTargetDir`
get/set the user help target directory. Defaults to `Platform.userAppSupportDir +/+ "Help"` and should typically not be changed by the user.
### `parseFileFull`
Parse file.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | Full path to .schelp file |  
**Returns:** An [SCDocNode](../Classes/SCDocNode.md) tree
### `parseFileMetaData`
Parse only the stuff needed for metadata.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | Base HelpSource directory. |  
| `` | Path relative above dir. |  
**Returns:** An [SCDocNode](../Classes/SCDocNode.md) tree
### `parseFilePartial`
Parse a file without header, for merging of document additions**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | Full path to .ext.schelp file |  
**Returns:** An [SCDocNode](../Classes/SCDocNode.md) tree
### `parseDoc`
Parse the files associated with an [SCDocEntry](../Classes/SCDocEntry.md), including any document additions (`*.ext.schelp`)**Arguments:**

| Argument | Description |
|----------|-------------|
| `doc` | The [SCDocEntry](../Classes/SCDocEntry.md) to parse. |  
**Returns:** An [SCDocNode](../Classes/SCDocNode.md) tree
### `parseAndRender`
Parse and render a specific document.**Arguments:**

| Argument | Description |
|----------|-------------|
| `doc` | The [SCDocEntry](../Classes/SCDocEntry.md) to parse and render. |  

### `renderAll`
Render all help-files. Useful mainly if you want to render all help to put online or similar.**Arguments:**

| Argument | Description |
|----------|-------------|
| `includeExtensions` | If false, skip quarks, plugins and other extensions. |  

### `refreshStaticFiles`
Copy (and replace) all non-schelp files within [SCDoc#*helpSourceDirs](../Classes/SCDoc.md#*helpsourcedirs) to [SCDoc#*helpTargetDir](../Classes/SCDoc.md#*helptargetdir). This should only be called by the user for development or debugging purposes.This will be invoked by- [SCDoc#*indexAllDocuments](../Classes/SCDoc.md#*indexalldocuments) if invoked with `clearCache=true` or if [SCDoc#*checkVersion](../Classes/SCDoc.md#*checkversion) detects a version bump of [SCDoc#*version](../Classes/SCDoc.md#*version)
- [SCDoc#*renderAll](../Classes/SCDoc.md#*renderall)

### `prepareHelpForURL`
Prepare help for the given URL by checking if the file needs rendering from schelp source, or some other action needs to be done. Used as a wrapper to get on-the-fly rendering and processing of help files.**Arguments:**

| Argument | Description |
|----------|-------------|
| `url` | The url to prepare. If this is not a local file inside [#*helpTargetDir](#*helptargetdir) then it will just pass through the url directly. |  
**Returns:** the URL or nil if file not found.


### Utilities
### `getMethodDoc`
Extract the [SCDocNode](../Classes/SCDocNode.md) tree for the specified method documentation.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | Name of class |  
| `` | Name of method, prefixed with `*` for classmethods and `-` for instancemethods. |  
**Returns:** An [SCDocNode](../Classes/SCDocNode.md) tree
### `makeClassTemplate`
Create a schelp template for specified class.**Arguments:**

| Argument | Description |
|----------|-------------|
| `doc` | The [SCDocEntry](../Classes/SCDocEntry.md) for the undocumented class. |  
**Returns:** Returns the template string.
### `classHasArKrIr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `c` | The [Class](../Classes/Class.md) to check. |  
**Returns:** `true` if the class responds to ar, kr or ir classmethods.


## Parser node tree output
The SCDoc parser outputs a tree of [SCDocNode](../Classes/SCDocNode.md)s

The nodes reflects the tags in the input, but it's not a one-to-one correspondence. A more detailed structure is added in the node tree, for easier rendering.

Example:

DOCUMENT

HEADERTITLE `"SinOsc"`SUMMARY `"Interpolating sine wavetable oscillator"`RELATEDSTRING `"Classes/FSinOsc"`STRING `"Classes/SinOscFB"`CATEGORIESSTRING `"UGens>Generators>Deterministic"`STRING `"UGens>Oscillators"`BODYDESCRIPTIONPROSETEXT `"A paragraph with "`LINK `"Classes/Osc##a link"`TEXT `" to another document."`PROSETEXT `"Another paragraph with "`STRONG `"strong words"`TEXT `" in it."`CLASSMETHODSPROSETEXT `"Some text..."`CMETHODMETHODNAMESSTRING `"ar"`STRING `"kr"`METHODBODYPROSETEXT `"Some text..."`ARGUMENTSARGUMENT `"freq"`PROSETEXT `"Frequency in hertz"`ARGUMENT `"phase"`PROSETEXT `"Phase modulation"`EXAMPLESPROSETEXT `"Here are some examples:"`CODEBLOCKSECTION `"Another section"`PROSETEXT `"Some text..."`




