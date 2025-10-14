# File

*A class for reading and writing files*

**Related:** [FileReader](../Classes/FileReader.md)

**Categories:** Files

## Description

A class for reading and writing files. Not sound files.


## Class Methods


### `new`
Create a File instance and open the file. If the open fails, [isOpen](../Classes/UnixFILE.md#-isopen) will return false.**Arguments:**

| Argument | Description |
|----------|-------------|
| `pathName` | A [String](../Classes/String.md) containing the path name of the file to open. |  
| `mode` | a [String](../Classes/String.md) indicating one of the following modes:
**"r"**
: Opens a file for reading. The file must exist.

**"w"**
: Creates an empty file for writing. If a file with the same name already exists its content is erased and the file is treated as a new empty file.

**"a"**
: Appends to a file. Writing operations append data at the end of the file. The file is created if it does not exist.

**"rb", "wb", "ab"**
: same as above, but data is binary

**"r+"**
: Opens a file for update both reading and writing. The file must exist.

**"w+"**
: Creates an empty file for both reading and writing. If a file with the same name already exists its content is erased and the file is treated as a new empty file.

**"a+"**
: Opens a file for reading and appending. All writing operations are performed at the end of the file, protecting the previous content to be overwritten. You can reposition the internal pointer using the seek method to anywhere in the file for reading, but writing operations will move it back to the end of file. The file is created if it does not exist.

**"rb+", "wb+", "ab+"**
: same as above, but data is binary |  

### `open`
Same as [#*new](#*new), but a more intuitive name.
### `getcwd`
POSIX standard 'get current working directory'.
```supercollider
// example;
File.getcwd;
```


### `use`
Open the file, evaluate the function with the file as argument, and close it again. If the process fails, close the file and throw an error.
### `readAllString`
Open the file at the given path, call [readAllString](#readallstring), and return the string. Whether the process succeeds or fails, the file will always be closed.
```supercollider
// write a file
File.use("~/test.txt".standardizePath, "w", { |f| f.write("The green fox fell into the blue lake") });

// read it again
File.readAllString("~/test.txt".standardizePath);
```


### `readAllSignal`
Open the file at the given path, call [readAllSignal](#readallsignal), and return the signal. Whether the process succeeds or fails, the file will always be closed.
### `readAllStringHTML`
Open the file at the given path, call [readAllStringHTML](#readallstringhtml), and return the string. Whether the process succeeds or fails, the file will always be closed.
### `readAllStringRTF`
Open the file at the given path, call [readAllStringRTF](#readallstringrtf), and return the string. Whether the process succeeds or fails, the file will always be closed.

### Filesystem utilities
### `exists`
Answers if a file exists at that path.
> **Note:** Some filesystems, like the one used by macOS, are case insensitive. On such systems, this method will return true for "fOo" even if the file is actually named "Foo". For a workaround, see [#*existsCaseSensitive](#*existscasesensitive) below.

**Returns:** a [Boolean](../Classes/Boolean.md)
### `existsCaseSensitive`
Like [#*exists](#*exists) but ensure case sensitivity *of the last path component* on case insensitive filesystems. On case sensitive systems, it falls back to using `exists`.
> **Note:** This is slower than the normal `exists` method, so use it only when really needed.


### `systemIsCaseSensitive`
Answers if the filesystem is case sensitive or not.
### `mkdir`
Create directory at path, including any missing parent directories.**Returns:** a [Boolean](../Classes/Boolean.md), as follows:- `true` -- A new directory was created at `path`.
- `false` -- A directory already existed at `path`; a new one was not created.

### `delete`
Deletes the file at that path. Use only for good, never for evil.**Returns:** a [Boolean](../Classes/Boolean.md), as follows:- `true` -- You can assume that the path no longer exists. (Either it existed and was deleted, or it didn't exist and it still doesn't exist.)
- `false` -- The file could not be deleted (probably a permissions error). Your code should assume that the path still exists.

### `deleteAll`
Deletes the file and all children at that path. Use only for good, never for evil.**Returns:** a [Boolean](../Classes/Boolean.md), as follows:- `true` -- At least one file was deleted.
- `false` -- No files were deleted.
If deletion fails, a PrimitiveFailedError object will be thrown.
### `realpath`
Follow symbolic links (and aliases on macOS) and any parent directory references (like "..") and return the true absolute path.**Returns:** a [String](../Classes/String.md) or `nil` if path did not exist.
### `copy`
Copy file, symlink or directory. this method will fail if pathNameTo already exists.Symlinks are copied as symlinks (re-created).
### `type`
Get file type as one of `\error, \not_found, \regular, \directory, \symlink, \block, \character, \fifo, \socket, \unknown`**Returns:** a [Symbol](../Classes/Symbol.md)
### `fileSize`
Get size of file in bytes.**Returns:** an [Integer](../Classes/Integer.md)
### `mtime`
Get last modification time in seconds since the Epoch.**Returns:** an [Integer](../Classes/Integer.md)


### Error handling in filesystem utilities
If one of the above filesystem primitives fails, in most cases, a PrimitiveFailedError object will be thrown:


```supercollider
File.mkdir("/usr/oh-no-you-cant");
```



The methods [Function#-try](../Classes/Function.md#-try) and [Function#-protect](../Classes/Function.md#-protect) can detect and handle these errors. See [Understanding-Errors](../Guides/Understanding-Errors.md) for details.

Currently, [File#*copy](../Classes/File.md#*copy), [File#*fileSize](../Classes/File.md#*filesize), [File#*mkdir](../Classes/File.md#*mkdir), [File#*mtime](../Classes/File.md#*mtime), and [File#*type](../Classes/File.md#*type) throw errors upon failure. ([File#*delete](../Classes/File.md#*delete) does not throw an error, but instead returns a Boolean.)



## Instance Methods

### `open`
Open the file. Files are automatically opened upon creation, so this call is only necessary if you are closing and opening the same file object repeatedly.
> **Note:** it is possible when saving files with a standard file dialog to elect to "hide the extension" and save it as RTF. When opening the file you must specify the real filename: "filename.rtf", even though you can't see in file load dialogs or in the Finder.

### `close`
Close the file.### `readAllString`
Reads the entire file as a [String](../Classes/String.md).### `readAllStringHTML`
Reads the entire file as a [String](../Classes/String.md), stripping HTML tags.### `readAllStringRTF`
Reads the entire file as a [String](../Classes/String.md), stripping RTF formatting.### `readAllSignal`
Reads the entire file as a [Signal](../Classes/Signal.md), where every chunk of four bytes is interpreted as a 32-bit floating point sample.### `seek`
Moves the read/write pointer to a given location in the file, where offset is location given in bytes, and origin is the reference of the offset:
**0**
: offset is from the beginning of the file

**1**
: offset is relative to the current position in the file

**2**
: offset is from the end of the file

### `pos`
Sets or returns the current position in the file (in bytes). when used as a setter, this method is a shortcut for seek(0, value). so setting the pos moves the current file position to a given location from the beginning of the file. the value is clipped so that it lies between 0 inclusively and the file length exclusively.### `length`
Returns the current file size in bytes.
## Examples


```supercollider
// write some string to a file:
(
var f, g;
f = File("~/test.txt".standardizePath, "w");
f.write("Does this work?\n is this thing on ?\n");
f.close;
)

// read it again:
(
g = File("~/test.txt".standardizePath, "r");
g.readAllString.postln;
g.close;
)

// try the above with File.use:

File.use("~/test.txt".standardizePath, "w", { |f| f.write("Doesn't this work?\n is this thing really on ?\n") });
File.use("~/test.txt".standardizePath, "r", { |f| f.readAllString.postln });


// more file writing/reading examples:
(
var h, k;
h = File("~/test.dat".standardizePath, "wb");
h.inspect;
h.write(FloatArray[1.1, 2.2, 3.3, pi, 3.sqrt]);
h.close;

k = File("~/test.dat".standardizePath, "rb");
(k.length div: 4).do({ k.getFloat.postln });
k.close;
)


(
var f, g;
f = File("~/test.txt".standardizePath, "w");
100.do({ f.putChar([$a, $b, $c, $d, $e, $\n].choose) });
f.close;

g = File("~/test.txt".standardizePath, "r");
g.readAllString.postln;
g.close;

g = File("~/test.txt".standardizePath, "r");
g.getLine(1024).postln;
"*".postln;
g.getLine(1024).postln;
"**".postln;
g.getLine(1024).postln;
"***".postln;
g.getLine(1024).postln;
"****".postln;
g.close;
)

(
// var f, g;
f = File("~/test.dat".standardizePath, "wb");
f.inspect;
100.do({ f.putFloat(1.0.rand) });

f.inspect;
f.close;

g = File("~/test.dat".standardizePath, "rb");
100.do({
    g.getFloat.postln;
});
g.inspect;
g.close;
)

(
// var f, g;
f = File("~/test.dat".standardizePath, "r");
f.inspect;
f.close;
)
```




