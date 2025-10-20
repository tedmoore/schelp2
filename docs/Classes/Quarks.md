# Quarks

*Package manager*

**Categories:** Quarks

**Related:** [UsingQuarks](../Guides/UsingQuarks.md), [Quark](../Classes/Quark.md)

## Description

See [UsingQuarks](../Guides/UsingQuarks.md) for an introduction to the Quarks package system.


## Class Methods


### `gui`
Show the interface for managing quarks**Returns:** QuarksGui

### `install`
Will execute the [hooks](../Guides/UsingQuarks.md#hooks) `\preInstall` and `\postInstall` if defined.**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` | Name of a quark that is listed in the directory, or the url of a git repository or the path (absolute or relative to current working directory) of a folder to install. |  
| `refspec` | Optional git refspec. By default it will install the latest version. Optionally you can specify a tag: "tags/1.0.0" A sha commit: "15e6ea822a18d06b286c3f10918f83b8d797d939" "HEAD" nil (default) |  
**Returns:** this

### `installQuark`
Install a quark Usually you use *install with a name, url or path.**Arguments:**

| Argument | Description |
|----------|-------------|
| `quark` |  |  
**Returns:** this

### `uninstall`
Will execute the [hooks](../Guides/UsingQuarks.md#hooks) `\preUninstall` and `\postUninstall` if defined.**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` | Name (String) of a quark that is listed in the directory, or url of a git repository or the path (absolute or relative to current working directory) of a folder to uninstall. |  
**Returns:** this

### `clear`
Uninstall all Quarks, by setting LanguageConfig.installedPaths to empty.**Returns:** this

### `addFolder`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` | In addition to the default downloaded-quarks add folders that contain quarks to offer on the menu for installation. These may be private quarks, cloned working copies or folders where you have manually downloaded quarks.
> **Note:** The argument should be a path to a directory *containing quark directories*. It should *not* be an isolated quark directory by itself. Users are discouraged from scattering quark directories in isolated locations. |  
**Returns:** this

### `all`
All Quarks whether downloaded or installed or not. Includes any Quarks that were installed by path.**Returns:** Array of Quarks

### `installed`
All currently installed Quarks**Returns:** Array of Quarks

### `isInstalled`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` | Name, url or path |  
**Returns:** Boolean

### `save`
Saves the currently installed quarks to a file as a list of urls and refspecs.**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` | path of file to save to |  
**Returns:** this

### `load`
Clear all installed quarks and load a list from a file. Relative paths in the file are resolved relative to the file itself. eg. ./classes/my-quark Unix style tildes (~/supercollider/quarks/my-quark) resolve to the user's home directory, even on Windows. By convention the file is called quarks.txt**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` | path of file to load. May contain ~ or relative paths (root is current working directory) |  
| `done` | function to be evaluated when loading is done |  
**Returns:** this

### `update`
Runs 'git pull' on the checked out copy of the quark. The gui provides a more robust way to do updates. Will execute the [hooks](../Guides/UsingQuarks.md#hooks) `\preUpdate` and `\postUpdate` if defined.**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` | name of quark |  
**Returns:** this

### `openFolder`
Open the downloaded-quarks folder**Returns:** this

### `folder`
Path of the downloaded-quarks folder where Quarks are cloned to before installing.**Returns:** path

### `checkForUpdates`
Scan through all downloaded, git-repository quarks and download any updates. This uses `git fetch`; updates will be retrieved but not applied to the working copy (i.e., no visible change to the environment). After this, repositories will be aware of new branches and version tags.This will take several seconds per quark. The SC interpreter will be unresponsive during each individual quark update.**Arguments:**

| Argument | Description |
|----------|-------------|
| `done` | (Optional) A function to evaluate after all quarks have been checked. |  
| `quarkAction` | (Optional) A function to evaluate *before* checking each individual quark. This function receives the Quark object as an argument, so you can use it, for instance, to print the quark name and have a running status update in the post window: `Quarks.checkForUpdates(quarkAction: { |quark| "Updating %\n".postf(quark.name) });`. |  


### `fetchDirectory`
Private. Fetches the directory listing into downloaded-quarks/quarks If a local copy already exists and it is not a git repo then this is used instead.**Arguments:**

| Argument | Description |
|----------|-------------|
| `force` | (Boolean) Force fetch. By default it is fetched once per session. Recompile the class library to fetch it again, or call Quarks.fetchDirectory(true) to force it. |  
**Returns:** this

### `classesInPackage`
Returns the Classes that are defined in the Quark or package.**Arguments:**

| Argument | Description |
|----------|-------------|
| `packageName` | name of quark or any folder in Extensions or Common. "Common" is a package that refers to the standard library. |  
**Returns:** Array of Classes

### `link`
Adds the path to LanguageConfig.installedPaths. private**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` |  |  
**Returns:** this

### `unlink`
Removes a path from LanguageConfig.installedPaths. private**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` |  |  
**Returns:** this

### `initClass`
private**Returns:** this

### `findQuarkURL`
private**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` |  |  
**Returns:** this

### `directoryUrl`
The URL of the directory.txt file**Returns:** this

### `directory`
The community contributed Quarks directory. Fetched from the directoryUrl and parsed.**Returns:** Dictionary[name->url@refspec]

### `asAbsolutePath`
Helper method to resolve paths to absolute paths.**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` |  |  
| `relativeTo` | optional root for resolving relative paths |  
**Returns:** absolute path

### `quarkNameAsLocalPath`
private**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` | quark name, path or git url. |  
**Returns:** absolute path where the Quark is

### `at`
private. gets or creates a Quark by name, storing it in a central cache.**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` |  |  
**Returns:** Quark


## Instance Methods



