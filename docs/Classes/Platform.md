# Platform

*handle cross-platform differencies*

**Categories:** Platform

## Description

The Platform class (along with its subclasses) handles things which differ between operating systems (mac/linux/windows/...), to simplify cross-platform aspects of SuperCollider.
Platform is an abstract class encapsulating various platform dependent constants and properties, such as directories, primitive features and startup files. The platform object is accessible through the `platform` method of the main process instance:

```
thisProcess.platform
```


Currently implemented platforms include: OSXPlatform, LinuxPlatform, WindowsPlatform, UnixPlatform.


## Class Methods

Most of Platforms class methods are simply wrappers to `thisProcess.platform.method`.

### Platform name and platform dependent actions

### `case`
Perform actions depending on the current platform (name), just like Object:switch:
```
Platform.case(
    \osx,       { "OSX".postln },
    \linux,     { "Linux".postln },
    \windows,   { "Windows".postln }
);
```



### `ideName`
returns a String indicating which IDE the language believes it is running in. (Often this is determined via the "-i" option to the sclang executable.) This is determined when sclang starts and cannot be changed dynamically.The main purpose of this is to include/exclude folders from the class search patch depending on which IDE is in use: for example, if the value of ideName is "scapp" then folders named "scide_scapp" are included and all other folders beginning with "scide_" are excluded. The default value of this is "none".Known IDE names in use are "scapp" (SuperCollider.app on Mac), "scvim" (vim), "scel" (emacs). Others may be used.


### Directories and filesystem stuff

### `classLibraryDir`
location of the bundled class library

### `helpDir`
location of the bundled help files

### `systemAppSupportDir`
system application support directory

### `systemExtensionDir`
system extension directory (see [UsingExtensions](../Guides/UsingExtensions.md))

### `userHomeDir`
user home directory

### `userAppSupportDir`
user application support directory

### `userConfigDir`
directory for configuration files

### `userExtensionDir`
user extension directory (see [UsingExtensions](../Guides/UsingExtensions.md))

### `platformDir`
platform specific directory for class files (see [UsingExtensions](../Guides/UsingExtensions.md))

### `pathSeparator`
platform specific path separator

### `resourceDir`
platform specific resource directory

### `recordingsDir`
platform recordings directory

### `defaultTempDir`
default directory for temporary files

### `hasQt`
true if the Qt library is available, false otherwise

### `hasQtWebEngine`
true if the QtWebEngine library is available, false otherwise

### `architecture`
A [Symbol](../Classes/Symbol.md) naming the architecture for which this version of SuperCollider was built. Returns one of 'AArch32' (32-bit ARM), 'AArch64' (64-bit ARM, introduced in ARMv8), 'Itanium64', 'i386', 'x86_64', 'PowerPC', or 'unknown' if the architecture is unidentifiable.

### `systemInformation`
Return a dictionary with system/context information like SuperCollider, QT, and OS versions.

### `postBugReportInfo`
Post system information that is useful to attach to bug reports.

### `exampleDir`
**Returns:** The full path of the `sclang/scd examples` folder as a [String](../Classes/String.md)


### Features

### `when`
Evaluate ifFunction if all features are present, otherwise evaluate elseFunction.
```
Platform.when(#[\Document, \Window], { "yeehah!".postln });
```




## Instance Methods


### `name`
returns the platform name
### `recompile`
recompile class library
### Directories and filesystem stuff

### `classLibraryDir`
location of the bundled class library

### `helpDir`
location of the bundled help files

### `systemAppSupportDir`
system application support directory

### `systemExtensionDir`
system extension directory (see [UsingExtensions](../Guides/UsingExtensions.md))

### `userHomeDir`
user home directory

### `userAppSupportDir`
user application support directory

### `userConfigDir`
directory for configuration files

### `userExtensionDir`
user extension directory (see [UsingExtensions](../Guides/UsingExtensions.md))

### `platformDir`
platform specific directory for class files (see [UsingExtensions](../Guides/UsingExtensions.md))

### `pathSeparator`
platform specific path separator

### `pathDelimiter`
platform specific path delimiter

### `recordingsDir`
platform recordings directory

### `resourceDir`
platform specific resource directory

### `defaultTempDir`
default directory for temporary files

### `formatPathForCmdLine`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` | A path string. |  
**Returns:** The input string formatted as a command-line argument. On Windows this method quotes the string. On Unix-based systems this method escapes space characters with a backslash.

### Startup files

### `startupFiles`
files to be loaded on startup

### `loadStartupFiles`
(re)load startup files

### System commands

### `killAll`
kill all processes as defined by cmdLineArgs.**Arguments:**

| Argument | Description |
|----------|-------------|
| `cmdLineArgs` | a string containing one or several process names. |  
| `force` | if true (default), the process will be closed forcefully, using `killall -KILL` on *nix and `taskkill /f` on Windows.
```
// e.g. kill all possibly running servers (scsynth or supernova)
thisProcess.platform.killAll("scsynth supernova");
``` |  


### `killProcessByID`
kill a single process as identified by its process ID.**Arguments:**

| Argument | Description |
|----------|-------------|
| `pid` | an Integer which is the pid of the process to kill. |  
| `force` | if true (default), the process will be closed forcefully, using `kill -KILL` on *nix and `taskkill /f` on Windows. |  
| `subprocesses` | if true (default), the subprocesses (children) of the process will be closed as well; this is useful if the process is a shell that started a subprocess, e.g. when using `String -unixCmd`
```
// start a server program from the cmdLine for testing
~pid = unixCmd(Server.program + s.options.asOptionsString(57100));
// kill just that server program by its pid:
thisProcess.platform.killProcessByID(~pid);
``` |  


### Features
Features are abstract symbols that can be declared by extension authors and be checked during runtime in user code. Apart from explicitly declared features, class and primitive names are implicitly declared.


### `declareFeature`
Declare aSymbol to be a feature present in the runtime. Class names and primitive names cannot be declared as features.

### `hasFeature`
Return true if the feature aSymbol is present in the runtime system. aSymbol can refer to explicitly declared features as well as class and primitive names.
```
thisProcess.platform.hasFeature(\Object);
thisProcess.platform.hasFeature('_myFuncyPrimitive');

thisProcess.platform.declareFeature('superCrazyCompositionSystem');
thisProcess.platform.hasFeature('superCrazyCompositionSystem');
```



### `when`
Evaluate ifFunction if all features are present, otherwise evaluate elseFunction.
```
thisProcess.platform.when(#[\Document, \Window], { "yeehah!".postln });
```




