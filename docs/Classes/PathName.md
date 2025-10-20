# PathName

*file and directory path utilities*

**Related:** [File](../Classes/File.md), [String](../Classes/String.md)

**Categories:** Files

## Description

PathName is a utility class for manipulating file names and paths. It expects a path to a file, and lets you access parts of that file path.

> **Note:** Most classes in SC that operate on files generally expect paths to be [String](../Classes/String.md)s, not an instance of [PathName](../Classes/PathName.md). Use `.fullPath` to convert [PathName](../Classes/PathName.md) to a [String](../Classes/String.md) expected in most cases.




## Class Methods



### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` | a [String](../Classes/String.md) which likely contains one or more / as typical for folder separation. ~ will be converted to your fully addressed home directory, as per [String#-standardizePath](../Classes/String.md#-standardizepath).
```
PathName.new("MyDisk/SC 2.2.8 f/Sounds/FunkyChicken");
``` |  


### `tmp`
Get or set the global temp directory as a [String](../Classes/String.md). This is used by [Buffer](../Classes/Buffer.md), etc. By default this is `Platform.defaultTempDir`.

## Instance Methods


### `fileName`
returns just the name of the file itself; i.e. everything after the last slash in the full path.
```
(
var myPath;
myPath = PathName.new("MyDisk/SC 2.2.8 f/Sounds/FunkyChicken");
myPath.fileName.postln;
)
```


### `fileNameWithoutExtension`
returns the name of the file itself without the file extension.
### `extension`
returns the file extension, i.e. everything after the last full-stop in the [#-fileName](#-filename).
### `pathOnly`
returns the full path up to the file name itself; i.e. everything up to and including the last slash. This is handy e.g. for storing several files in the same folder.
```
(
var myPath;
myPath = PathName.new("MyDisk/SC 2.2.8 f/Sounds/FunkyChicken");
myPath.pathOnly.postln;
)
```


### `isAbsolutePath`, `asAbsolutePath`, `isRelativePath`, `asRelativePath`
you MUST have correctly initialized the scroot classvar for this to know what it is relative to !
### `folderName`
returns only the name of the folder that the file is in; i.e. everything in between the last but one and the last slash.
```
(
var myPath;
myPath = PathName.new("MyDisk/SC 2.2.8 f/Sounds/FunkyChicken");
myPath.folderName.postln;
)
```


### `fullPath`
returns the full path name that PathName contains.
```
(
var myPath;
myPath = PathName.new("MyDisk/SC 2.2.8 f/Sounds/FunkyChicken");
myPath.fullPath.postln;
)
```


### `entries`
returns a list of all the files+folders inside the folder represented by this path.
```
(
var myPath;
myPath = PathName.new("./");
myPath.entries.postln;
)
```


### `files`
returns a list of all the files in the folder represented by this path.
```
(
var myPath;
myPath = PathName.new("./");
myPath.files.postln;
)
```


### `folders`
returns a list of all the subfolders of the folder represented by this path.
```
(
var myPath;
myPath = PathName.new("./");
myPath.folders.postln;
)
```


### `isFile`
returns a [Boolean](../Classes/Boolean.md) indicating whether or not the path represents a file (not a folder).
```
(
var myPath;
myPath = PathName.new("./");
myPath.isFile.postln;
)
```


### `isFolder`
returns a [Boolean](../Classes/Boolean.md) indicating whether or not the path represents a folder (not a file).
```
(
var myPath;
myPath = PathName.new("./");
myPath.isFolder.postln;
)
```


### `filesDo`
Iterates over all files found in the pathname, including ones in subfolders.
```
(
var myPath;
myPath = PathName.new("./");
myPath.filesDo{ |afile| afile.postln };
)
```


### `allFolders`
returns a list of all the folder names contained in the pathname itself.
```
(
var myPath;
myPath = PathName.new("MyDisk/SC 2.2.8 f/Sounds/FunkyChicken");
myPath.allFolders.postln;
)
```


### `diskName`
if path is an absolute path, returns the disk name; else a blank string.
```
(
var myPath;
myPath = PathName.new("MyDisk/SC 2.2.8 f/Sounds/FunkyChicken");
myPath.diskName.postln;
)

( // note the / at the start
var myPath;
myPath = PathName.new("/MyDisk/SC 2.2.8 f/Sounds/FunkyChicken");
myPath.diskName.postln;
)
```


### `+/+`
Path concatenation operator - useful for avoiding doubling-up slashes unnecessarily.
```
(PathName("/somewhere") +/+ PathName("over/the/rainbow")).postln;
(PathName("/somewhere") +/+ PathName("/over/the/rainbow")).postln;
```


### `endNumber`
returns a number at the end of PathName. Returns zero if there is no number.
```
PathName("floating1").endNumber.postln;
PathName("floating").endNumber.postln;
```


### `noEndNumbers`
returns [#-fullPath](#-fullpath) without any numbers at the end.
```
PathName("floating1").noEndNumbers.postln;
PathName("floating").noEndNumbers.postln;
```


### `nextName`
generates a sensible next name for a file by incrementing a number at the end of PathName, or by adding one if there is none. This is useful for recording files with consecutive names, and e.g. to generate a new filename when you don't want to overwrite an existing file with the current name.
```
PathName("floating34").nextName.postln;
PathName("floating").nextName.postln;
PathName("floating12_3A4X_56.7").nextName.postln;
```


## Examples

Here is an example that uses many instance methods. Just pick any file to see all the parts of its path.

```
(
FileDialog.new(
    { |ok, path|
    var myPathName;
    if (ok,
        {
            myPathName = PathName.new(path);

            "New PathName object:  ".postc;
            myPathName.postln;

            "fileName only:        ".postc;
            myPathName.fileName.postln;

            "path up to file only: ".postc;
            myPathName.pathOnly.postln;

            "folder Name:          ".postc;
            myPathName.folderName.postln;
        }
    )
    }
)
)
```


Choose a soundfile to put into the library, using its foldername and filename.

```
(
FileDialog.new(
    { |ok, path|
    var myPathName, myFile;
    if (ok,
        {
            myPathName = PathName.new(path);

            // read your file from disk, e.g. a soundFile/

            myFile = SoundFile.new;
            if (myFile.openRead(path),
                {
                    Library.put(
                        [myPathName.folderName.asSymbol, myPathName.fileName.asSymbol],
                        myFile);
                    ("Check Library.global" + myPathName.folderName + "please.").postln;
                },
                { ("Could not read soundfile" + path ++ ".").postln }
            );
            myFile.close;
        }
    )
    }
)
)
```


Save three tables in the same folder. Note: The file name chosen in the dialog is ignored! The files are always named table1, table2, table3.

```
(
var table1, table2, table3;

table1 = Wavetable.sineFill(1024, [1, 2, 3]);
table2 = Signal.newClear.asWavetable;
table3 = Wavetable.sineFill(1024, Array.rand(64, 0.0, 1.0));

FileDialog.new(
    { |ok, path|
    var myPathName, myPathOnly;
    if (ok,
        {
            myPathName = PathName.new(path);
            myPathOnly = myPathName.pathOnly;
            ("writing files tables1-3 to"+myPathOnly).postln;
            table1.write(myPathOnly ++ "table1");
            table2.write(myPathOnly ++ "table2");
            table3.write(myPathOnly ++ "table3");
        }
    )
    }
)
)
```




