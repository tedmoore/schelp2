# Quark

*Object for managing a Quark - a package of source code*

**Categories:** Quarks

**Related:** [UsingQuarks](../Guides/UsingQuarks.md), [Quarks](../Classes/Quarks.md)

## Description

A Quark is a folder of source code, a package. It may be cloned from a git repository, or maybe not. This class is used by the Quarks class and you will not usually want to use it directly.


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` | Quark name, git url or local path (absolute or relative) |  
| `refspec` |  |  
| `url` |  |  
| `localPath` |  |  
**Returns:** this

### `fromLocalPath`
alternate constructor**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` |  |  
**Returns:** this

### `fromDirectoryEntry`
alternate constructor**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` |  |  
| `directoryEntry` |  |  
**Returns:** this

### `parseQuarkName`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `name` |  |  
| `refspec` |  |  
| `url` |  |  
| `localPath` |  |  
**Returns:** this

### `parseDependency`
private**Arguments:**

| Argument | Description |
|----------|-------------|
| `dep` |  |  
| `forQuark` |  |  
**Returns:** this


## Instance Methods


### `name`
**Returns:** String
### `dependencies`
Based on the dependencies list in the quark file, returns an array of Quarks.**Returns:** Array of Quark
### `deepDependencies`
Declared dependencies of this Quark and those of each dependency. This will check out all dependencies.**Returns:** Array of Quarks
### `data`
Lazily parses the quark file (if found) and caches it**Returns:** Dictionary - the contents of the quark file
### `refspec`
Git refspec (tag or sha hash)**Returns:** this
### `localPath`
Absolute path where the Quark is located**Returns:** this
### `summary`
Summary text from the quark file**Returns:** this
### `url`
Git repository url. If not declared when creating, it will examine the checked out git source and get the origin.**Returns:** this
### `isDownloaded`
**Returns:** Boolean
### `isInstalled`
**Returns:** Boolean
### `git`
Quarks that have git repos have a Git object that can be used for checking out, listing tags etc.**Returns:** a Git object
### `init`
private**Arguments:**

| Argument | Description |
|----------|-------------|
| `argName` |  |  
| `argUrl` |  |  
| `argRefspec` |  |  
| `argLocalPath` |  |  
**Returns:** this
### `install`
**Returns:** this
### `uninstall`
**Returns:** this
### `checkout`
Clone and checkout the url and refspec. Used by install and for switching versions.**Returns:** this
### `version`
**Returns:** String
### `branch`
returns the current branch name.**Returns:** String or nil, if failed
### `tags`
**Returns:** Array of Strings
### `isCompatible`
Evaluates the 'isCompatible' function in the quarkfile, if there is one. This allows a quarkfile to check its environment and raise an alarm before it gets installed and breaks something.**Returns:** Boolean
### `definesClasses`
Classes that are defined by this Quark**Returns:** Array of Classes
### `definesExtensionMethods`
Methods that this Quark defines that overwrite implementations in other packages including in Common.**Returns:** Array of Methods
### `help`
Open the help file. Either as specified in the quark file as 'schelp' or searches by the name of the quark.**Returns:** this
### `changed`
After un/installing or checking out, state is set to changed. code smell: this is for the gui**Returns:** Boolean
### `runHook`
Runs the function `hook` which is defined in the `.quark` file. This can be used for running a function before or after installation, see [UsingQuarks#Hooks](../Guides/UsingQuarks.md#hooks) for more information. In case the function can not be executed properly a warning will be printed and the update or installation process will be stopped.**Arguments:**

| Argument | Description |
|----------|-------------|
| `hook` | Name of function to run. |  
**Returns:** this
### `printOn`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `stream` |  |  
**Returns:** this
### `parseQuarkFile`
private**Returns:** this

