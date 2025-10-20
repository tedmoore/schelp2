# LanguageConfig

*Access and modify interpreter configuration*

**Categories:** Language

## Description

The LanguageConfig class provides access to the interpreter configuration.


## Configuration File Format
The configuration file is stored in YAML format, which contains one dictionary. The semantics of the dictionary is listed in the following table:


**`includePaths`**
: List of class library paths.

**`excludePaths`**
: List of paths to exclude from the class library files (overrides `includePaths`).

**`postInlineWarnings`**
: Boolean flag to post warnings about missing inline opportunities.





## Class Methods


### `store`
Store the current configuration to file. Throws an error if the config file cannot be opened or if writing fails.**Arguments:**

| Argument | Description |
|----------|-------------|
| `file` | Path to the configuration file to store. If the value is `nil` it defaults to currently used configuration file, as specified in the IDE preferences, or by the `sclang -l "/path/to/sclang_conf.yaml"` argument. By default this is `Platform.userConfigDir +/+ "sclang_conf.yaml"` |  


### Library Path Handling
The language configuration mechanism provides a way to add or exclude specific paths for the class library.


> **Note:** Changes to the class library paths won't have any effect before the configuration file is stored and the class library is recompiled.



### `includePaths`
Return the class library include paths.

### `addIncludePath`
Add new class library include path.

### `removeIncludePath`
Remove path from class library include paths.

### `excludePaths`
Return the class library exclude paths.

### `addExcludePath`
Add new class library exclude path.

### `removeExcludePath`
Remove path from class library exclude paths.

### `currentPath`
Return the current config file path.

### `excludeDefaultPaths`
Get or set whether default class library paths are included.
> **Note:** If sclang is started with -a the class library paths are excluded and this value is ignored. The default class library paths are Platform.classLibraryDir, and the system and user extensions directories.




### Compiler Warnings

### `postInlineWarnings`
Get or set the compiler flag, whether warnings should be posted if a FunctionDef cannot be inlined.
```
LanguageConfig.postInlineWarnings_(true) // warn
if(0.5.coin) { var x; x = 10.rand; x + 1 } { 10 };
LanguageConfig.postInlineWarnings_(false) // ignore it.
if(0.5.coin) { var x; x = 10.rand; x + 1 } { 10 };
```




