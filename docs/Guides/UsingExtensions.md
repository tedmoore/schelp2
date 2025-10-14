# Using Extensions

*Using Extensions*

**Categories:** Internals

**Related:** [WritingUGens](../Guides/WritingUGens.md), [UsingQuarks](../Guides/UsingQuarks.md), [WritingClasses](../Guides/WritingClasses.md)

SC supports extensions to its class library, documentation, and server UGen plugins. Extensions should be packaged as a single folder containing all three (for convenient addition or removal), or any combination, which can then be placed in platform-specific extension directories in order to be included.

## Platform Specific Directories
You can install extensions simply by copying the extensions to the following location. There are different directories for per-user and system-wide extensions that apply to all users.. The locations can be obtained by running `Platform.userExtensionDir` and `Platform.systemExtensionDir`.

Typical user-specific extensions directories:

| macOS | ~/Library/Application Support/SuperCollider/Extensions/ | 
| --- | --- || Linux | ~/.local/share/SuperCollider/Extensions/ | | Windows | %LOCALAPPDATA%/SuperCollider/Extensions/ | 
Typical system-wide extension directories:

| macOS | /Library/Application Support/SuperCollider/Extensions/ | 
| --- | --- || Linux | /usr/share/SuperCollider/Extensions/ | | Windows | %PROGRAMDATA%/SuperCollider/Extensions/ | 


## How Extensions Folders Should be Organised
Class files and UGen plugins are recognised by their file extensions. Anything placed within a folder named  `ignore/` (case insensitive) will be ignored when compiling the class library or loading plugins.

Here is an example folder layout:

`MyExtension`

`classes``myClass.sc``myUGens.sc``plugins``myUGenPlugins.scx``HelpSource``Classes``MyClass.schelp``MyUGen1.schelp``MyUGen2.schelp``Guides``MyExtensionGuide.schelp`




