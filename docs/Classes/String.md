# String

*array of Chars*

**Related:** [Char](../Classes/Char.md)

**Categories:** Collections>Ordered

## Description

String represents an array of [Chars](../Classes/Char.md).
Strings can be written literally using double quotes:

```supercollider
"my string".class
```


A sequence of string literals will be concatenated together:

```supercollider
x = "hel" "lo";
y = "this is a\n"
    "multiline\n"
    "string";
```


Backslash is the escape character. See [Literals / Characters ](../Reference/Literals.md#characters).

### Character encodings
Note that, while Char does not support encodings aside from ASCII—such as multi-byte encodings like UTF-8 and UTF-16, or the full Latin-1 (ISO 8859-1) character set—Chars with negative values are perfectly legal, and may be strung together in strings that use these encodings.

The SuperCollider IDE uses UTF-8 (a superset of ASCII) to decode and display strings, which means that the string `"🎹🙄🎻😂🎚️🎛️🎤😍"` can be written in the editor, posted in the post window, and treated for the most part like any other string. However, because non-ASCII UTF-8 characters consist of two or more bytes, and a SuperCollider String's members are one-bit Chars, concepts of size and indexing may not behave intuitively. For instance, the "`size`" of the string above is 38, not 8, and the value of its first index is `-16`, which is not a valid ASCII value at all but rather the signed 8-bit representation of the first byte of the UTF-8 value of the piano keyboard emoji (🎹), `0xF09F8EB9`.




## Class Methods




### `readNew`
Read the entire contents of a [File](../Classes/File.md) and return them as a new String.
### `scDir`
Deprecated alias for `Platform.resourceDir`. Please use [Platform#*resourceDir](../Classes/Platform.md#*resourcedir) instead.

## Instance Methods


### Accessing characters
### `@`, `at`
Strings respond to .at in a manner similar to other indexed collections. Each element is a [Char](../Classes/Char.md).
```supercollider
"ABCDEFG".at(2)
```


### `ascii`
Returns an Array of ASCII values of the Strings's characters.
```supercollider
"wertvoll".ascii // [119, 101, 114, 116, 118, 111, 108, 108]
```

Note that if a string contains multi-byte UTF-8 characters, this array will not be of the same length as the number of visible characters, nor will it necessarily be an array of valid 7-bit ASCII values.
```supercollider
// "face with tears of joy" is Unicode codepoint U+1F602, which is encoded in UTF-8 as hex value 0xF09F9882
a = "😂";

// although this is one UTF-8 character, it must be stored as 4 Chars because Chars can only hold 1 byte each
a.size // 4 (!)
a.ascii // [-16, -97, -104, -126]

// "wrap(0, 255)" converts these numbers to their unsigned 8-bit values
b = a.ascii.wrap(0, 255) // [240, 159, 152, 130]

// if we represent these values in hexidecmial, it's the same as the UTF-8 above: 0xF09F9882
b.collect(_.asHexString(2)) // [F0, 9F, 98, 82]
```



### Comparing strings
### `compare`
Returns an integer less than, equal to or greater than zero, depending on whether the receiver should be sorted before the argument, is equal to the argument or should be sorted after the argument. This is a case sensitive compare.
### `<`
Returns a [Boolean](../Classes/Boolean.md) whether the receiver should be sorted before the argument.
```supercollider
"same" < "samf"
```


### `>`
Returns a [Boolean](../Classes/Boolean.md) whether the receiver should be sorted after the argument.
```supercollider
"same" > "samf"
```


### `<=`
Returns a [Boolean](../Classes/Boolean.md) whether the receiver should be sorted before the argument, including the same string.
```supercollider
"same" <= "same"
"same" <= "samf"
```


### `>=`
Returns a [Boolean](../Classes/Boolean.md) whether the receiver should be sorted after the argument, including the same string.
```supercollider
"same" >= "same"
"same" >= "samf"
```


### `==`
Returns a [Boolean](../Classes/Boolean.md) whether the two Strings are equal.
> **Note:** This method is (now) case sensitive!


```supercollider
"same" == "same"
"same" == "Same"; // false
```


### `!=`
Returns a [Boolean](../Classes/Boolean.md) whether the two Strings are not equal.
```supercollider
"same" != "same"; // false
"same" != "Same";
```



### Fuzzy string comparison
With fuzzy comparison, the strings don't need to match exactly - we can work out how similar they are, and make decisions based on that. This behaviour is inherited from the [SequenceableCollection#-editDistance](../Classes/SequenceableCollection.md#-editdistance), and is documented fully there, but to provide an example:


```supercollider
"hello".editDistance("hallo"); // 1 (substitution)
"hello".editDistance("hell"); // 1 (deletion)
"hello".editDistance("helloo"); // 1 (addition)
"hello".editDistance("hllo"); // 1 (removal)
"hello".editDistance("haldo"); // 2 (substitutions)
```



### Posting strings
### `post`
Prints the string to the current post window.
```supercollider
"One".post; "Two".post; "";
```


### `postln`
Prints the string and a carriage return to the current post window.
```supercollider
"One".postln; "Two".postln; "";
```


### `postc`, `postcln`
As [post](#post) and [postln](#postln), but formatted as a comment.
```supercollider
"This is a comment.".postcln;
```


### `postf`
Prints a formatted string with arguments to the current post window. The % character in the format string is replaced by a string representation of an argument. To print a % character use \\% .
```supercollider
postf("this % a %. pi = %, list = %\n", "is", "test", pi.round(1e-4), (1..4))

this is a test. pi = 3.1416, list = [1, 2, 3, 4]
```


### `postcs`
As [postln](#postln), but posts the [compileString](#ascompilestring) of the receiver.
```supercollider
List[1, 2, ["comment", [3, 2]], { 1.0.rand }].postcs;
```


### `error`
Prepends an error banner and posts the string.
```supercollider
"Do not press this button again".error;
```


### `warn`
Prepends a warning banner and posts the string.
```supercollider
"Do not press this button again".warn;
```


### `inform`
Legacy method (although due to widespread use, it will not be removed). This is identical to `postln`.

### Interpreting strings as code
### `compile`
Compiles a String containing legal SuperCollider code and returns a Function.
```supercollider
(
var f;
f = "2 + 1".compile.postln;
f.value.postln;
)
```


### `interpret`
Compile and execute a String containing legal SuperCollider code, returning the result.
```supercollider
"2 + 1".interpret.postln;
```


### `interpretPrint`
Compile, execute and print the result of a String containing legal SuperCollider code.
```supercollider
"2 + 1".interpretPrint;
```



### Converting strings
### `asCompileString`
Returns a String formatted for compiling.
```supercollider
(
var f;
f = "myString";
f.postln;
f.asCompileString.postln;
)
```


### `asSymbol`
Return a [Symbol](../Classes/Symbol.md) derived from the String.
```supercollider
(
var z;
z = "myString".asSymbol.postln;
z.class.postln;
)
```


### `asInteger`
Returns an [Integer](../Classes/Integer.md) derived from the String. Strings beginning with non-numeric characters return 0. 
```supercollider
"4".asInteger
```

  The method `.asInteger` does not understand scientific notation (e.g., `2e3` for `2000`),  and simply ignores all characters in the string after its first nonnumeric character  (excepting signs `+,-` at the beginning of the string).  If you use scientific notation, use [asFloat](#asfloat) instead.
```supercollider
"2e3".asInteger // -> 2
```


### `asFloat`
Returns a [Float](../Classes/Float.md) derived from the String. Strings beginning with non-numeric characters return 0. 
```supercollider
"4.3".asFloat
```

  The method `.asFloat` understands scientific notation (e.g., `2e3` for `2000`, `2e-3` for `0.002`), and accepts uppercase `E` and lowercase `e`. By contrast, the method [asInteger](#asinteger) does *not* accept scientific notation.
```supercollider
"2e3".asFloat // -> 2000.0
```


### `asSecs`
Return a [Float](../Classes/Float.md) based on converting a time string in format `(ddd:)hh:mm:ss(.z)`, where `z` is any sequence of digits. This is the inverse method to [SimpleNumber#-asTimeString](../Classes/SimpleNumber.md#-astimestring).
```supercollider
"00:00:59.900".asSecs; // hh:mm:ss.zzz
"1:1:1.1".asSecs; // h:m:s.z
"001:00:00:00.001".asSecs; // ddd:hh:mm:ss.zzz
"32.1".asSecs;
"32.".asSecs; // trailing period
"32.12345678".asSecs; // any number of decimal places
"62.1".asSecs; // warns
"-1".asSecs; // neg sign supported
"-12:34:56".asSecs; // neg sign always at the beginning
"-23:12.346".asSecs;
"-1:00:00:00".asSecs; // neg with days
"12:-34:56".asSecs; // warns
(45296.789.asTimeString).asSecs; // inverse of aNumber.asTimeString
```



### Concatenate strings
### `++`
Return a concatenation of the two strings.
```supercollider
"hello" ++ "word"
```


### `+`
Return a concatenation of the two strings with a space between them.
```supercollider
"hello" + "word"
```


### `+/+`
Concatenates `this` and `path`, as components of a filesystem path on the host operating system. The strings are joined to avoid duplicate path separators.If `this` ends with a path separator and `path` begins with one, then the separator in `path` is dropped. If there is a path separator on either side, this has the same effect as using `++`. If neither side has a path separator, the platform's preferred separator ('\' on Windows, '/' otherwise) is added.Returns `this` and `path` concatenated. If `path` was a PathName, the result is a PathName; otherwise, it is a String.
> **Note:** Do not use `+/+` in URLs or in other situations where forward slash is expected. `+/+` should only be used with filesystem paths, where it will resolve to either forward or backward slash, depending on the operating system's requirements.

**Arguments:**

| Argument | Description |
|----------|-------------|
| `path` | Any object that can be converted to a string. Typically, either a String, [Symbol](../Classes/Symbol.md), or [PathName](../Classes/PathName.md).
```supercollider
// On Windows, this produces "foo\\bar"; on other platforms, "foo/bar"
"foo" +/+ "bar"

// On all platforms, this produces "foo/bar": +/+ prefers using an existing separator
"foo/" +/+ "bar"
"foo" +/+ "/bar"
"foo/" +/+ "/bar"

// On Windows, this produces "foo\\bar"; on other platforms, "foo/\\bar"
"foo" +/+ "\\bar"

// Concatenating a symbol is also OK
"foo" +/+ 'bar'
``` |  

### `catArgs`
Concatenate this string with the following args.
```supercollider
"These are some args: ".catArgs(\fish, SinOsc.ar, { 4 + 3 }).postln;
```


### `scatArgs`
Same as [catArgs](#catargs), but with spaces in between.
```supercollider
"These are some args: ".scatArgs(\fish, SinOsc.ar, { 4 + 3 }).postln;
```


### `ccatArgs`
Same as [catArgs](#catargs), but with commas in between.
```supercollider
"a String".ccatArgs(\fish, SinOsc.ar, { 4 + 3 }).postln;
```


### `catList`, `scatList`, `ccatList`
As [catArgs](#catargs), [scatArgs](#scatargs) and [ccatArgs](#ccatargs) above, but takes a Collection (usually a [List](../Classes/List.md) or an [Array](../Classes/Array.md)) as an argument.
```supercollider
"a String".ccatList([\fish, SinOsc.ar, { 4 + 3 }]).postln;
```



### Regular expressions
The String class provides access to the boost library's regular expression functions. Boost's default uses Perl settings. (Currently, there is no hook to override the regex style.) Syntax details may be found at [https://www.boost.org/doc/libs/1_69_0/libs/regex/doc/html/boost_regex/syntax/perl_syntax.html](https://www.boost.org/doc/libs/1_69_0/libs/regex/doc/html/boost_regex/syntax/perl_syntax.html).

Note carefully the argument order:

- `regexp.matchRegexp(stringToSearch)`
- `stringToSearch.findRegexp(regexp)` (and similar for `findAllRegexp` and `findRegexpAt`).


`findRegexp` follows the pattern established by [String#-find](../Classes/String.md#-find), where the receiver is the string to be searched. `matchRegexp` follows the pattern of [matchItem](../Reference/matchItem.md), where the receiver is the pattern to match and the first argument is the object to be tested. This is a common source of confusion, but it is based on this precedent.

### `matchRegexp`
Perl regular expression matching (see [String / Regular expressions ](../Classes/String.md#regular-expressions)). Returns true if the receiver (a regular expression pattern) matches the string passed to it. The **start** is an offset where to start searching in the string (default: 0), **end** where to stop.
> **Note:** This is `regexp.matchRegexp(stringToSearch)` and not the other way around! See above: [String / Regular expressions ](../Classes/String.md#regular-expressions).


```supercollider
"c".matchRegexp("abcdefg", 2, 5); // true: substring exists
"c".matchRegexp("abcdefg", 4, 5); // false: substring doesn't exist

"behaviou?r".matchRegexp("behavior"); // true: character may or may not exist
"behaviou?r".matchRegexp("behaviour"); // true: character may or may not exist
"behaviou?r".matchRegexp("behavir"); // false: but the rest does not match
"behavi(ou)?r".matchRegexp("behavir"); // true: the substring in parens may or may not exist
"b.h.v.r".matchRegexp("behavor"); // true
"b.h.v.r".matchRegexp("behaviiiiir"); // false: dot stands for exactly one char
"b.h.vi*r".matchRegexp("behaviiiiir"); // true: (kleene) star stands for any number of chars preceding, or none
"b.h.vi*r".matchRegexp("behavuuuur"); // false
"(a|u)nd".matchRegexp("und"); // true
"(a|u)nd".matchRegexp("and"); // true
"[a-c]nd".matchRegexp("ind"); // false
"[a-c]nd".matchRegexp("bnd"); // true: anything between a and c
"[a-c]*nd".matchRegexp("accacaccacand"); //  true: any combination of a, b, c, or none.
"[xtz]+nd".matchRegexp("xnd"); // true: any combination of x, t, z
```


### `replaceRegexp`
This method is used to replace parts of text.**Arguments:**

| Argument | Description |
|----------|-------------|
| `regex` | A perl regular expression (see [String / Regular expressions ](../Classes/String.md#regular-expressions)) with which to match the caller. |  
| `with` | The [String](../Classes/String.md) to replace the found regex with. |  
**Returns:** A [String](../Classes/String.md).
```supercollider
// remove numbers
"g8et t8ho9se 3num5b89ers ou06t o8f h12er56e!".replaceRegexp("[0-9]", "")
-> get those numbers out of here!

// remove capital letters
"HelLO WoRlD".replaceRegexp("(\\\w)", "\\\L$1")
-> hello world

// remove all capital letter unless at the start of a word
"HelLO worLD! I weNT tO Paris yeSTErDay.".replaceRegexp("(\\\S)(\\\S*)", "$1\\\L$2")
-> Hello world! I went to Paris yesterday.
```


### `findRegexp`
Perl regular expression search (see [String / Regular expressions ](../Classes/String.md#regular-expressions)). This method searches exhaustively for matches and collects them into an array of pairs, in the format `[character index, matching string]`."Leftmost largest match": As in most flavors of regular expressions, `*` and `+` are greedy; if it is possible to have more than one overlapping match for a part of the regular expression, the match list will include only the leftmost and largest of them. In `"foobar".findRegexp("o+")`, `"o+"` may potentially have three matches: `"o"` at index 1 (second character), `"o"` at index 2, and `"oo"` at index 1. `findRegexp` will return only the last of these (`"oo"`), because it begins in the leftmost-possible matching position, and it is the longest possible match at that position.Note, though, that parentheses for grouping (a "marked sub-expression" or "capturing group") will produce a separate result: `"aaa".findRegexp("(a+)");` appears to produce duplicated results `[[0, aaa], [0, aaa]]`, but this is because the first match is for the parentheses and the second is for `a+`.To see the marked sub-expression results more clearly, consider:
```supercollider
"foobar".findRegexp("(o*)(bar)");
-> [[1, oobar], [1, oo], [3, bar]]
```

`"oobar"` matches the entire regular expression. `"oo"` and `"bar"` match the first and second parenthesized sub-expressions, respectively.
```supercollider
"foobar".findRegexp("o*bar");
"32424 334 /**aaaaaa*/".findRegexp("/\\*\\*a*\\*/");
"aaaabaaa".findRegexp("a+");
```

**Returns:** A nested array, where each sub-array is a pair, `[character index, matching string]`. If there are no matches, an empty array.
### `findAllRegexp`
Like [findAll](#findall), but use regular expressions (see [String / Regular expressions ](../Classes/String.md#regular-expressions)). Unlike findRegexp, it returns only the indices of the matches: `string.findAllRegexp(regexp)` returns the same as `string.findRegexp(regexp).flop.at(0)`.
```supercollider
"foobar".findAllRegexp("o*bar");
"32424 334 /**aaaaaa*/".findAllRegexp("/\\*\\*a*\\*/");
"foobar".findAllRegexp("(o*)(bar)");
"aaaabaaa".findAllRegexp("a+");
```

**Returns:** An array of integer character indices pointing to all the possible matches.
### `findRegexpAt`
Match a regular expression (see [String / Regular expressions ](../Classes/String.md#regular-expressions)) at the given offset, returning the match and the length of the match in an Array, or nil if it doesn't match. The match must begin right at the offset.
```supercollider
"foobaroob".findRegexpAt("o*b+", 0); // nil
"foobaroob".findRegexpAt("o*b+", 1); // [oob, 3]
"foobaroob".findRegexpAt("o*b+", 2); // [ob,  2]
"foobaroob".findRegexpAt("o*b+", 3); // [b,   1]
"foobaroob".findRegexpAt("o*b+", 4); // nil
"foobaroob".findRegexpAt("o*b+", 5); // nil
"foobaroob".findRegexpAt("o*b+", 6); // [oob, 3]
"foobaroob".findRegexpAt("o*b+", 7); // [ob,  2]
```

**Returns:** An array `[matching string, length]` if a match is found at the specified offset; `nil` if the offset doesn't match.

### Searching strings
### `find`
Returns the index of the string in the receiver, or nil if not found. If **ignoreCase** is true, find makes no difference between uppercase and lowercase letters. The **offset** is the point in the string where the search begins. string may be a String or a [Char](../Classes/Char.md).
```supercollider
"These are several words".find("are").postln;
"These are several words".find("fish").postln;
```


### `findBackwards`
Same like [find](#find), but starts at the end of the string.
```supercollider
// compare:
"These words are several words".find("words"); // 6
"These words are several words".findBackwards("words"); // 24
```


### `findAll`
Returns the indices of the string in the receiver, or nil if not found.
```supercollider
"These are several words which are fish".findAll("are").postln;
"These are several words which are fish".findAll("fish").postln;
```


### `findSimilarIn`
From a list of strings, find similar strings, sorted by edit distance and limited by similarity.
```supercollider
"hi".findSimilarIn(["ho", "hu?", "hugs", "Hola", "else"], 2); // [ho, hu?]
"hi".findSimilarIn(["ho", "hu?", "hugs", "Hola", "else"], 3); // [ho, hu?, hugs, Hola]
"hi".findSimilarIn(["ho", "Hi", "hugs", "Hola", "else"], 3, prioritizeCapitalization: false); // [ho, Hi, hugs]
"hi".findSimilarIn(["ho", "Hi", "hugs", "Hola", "else"], 3, prioritizeCapitalization: true); // [Hi, ho, hugs, Hola]
"hi".findSimilarIn(["ho", "Hi", "hugs", "Hola", "else"], 4, minSimilarity: nil); // [Hi, ho, hugs, Hola, else]
"hi".findSimilarIn(["ho", "Hi", "hugs", "Hola", "else"], 4, minSimilarity: 0.01); // [Hi, ho, hugs, Hola]
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `array` | An array of strings to find similar strings in. |  
| `maxEditDistance` | The largest [edit distance](../Classes/SequenceableCollection.md#editdistance) that is accepted as a match. |  
| `minSimilarity` | Keep only results whose [similarity](../Classes/SequenceableCollection.md#similarity) is larger than this value. If set to `nil`, all values are accepted. |  
| `prioritizeCapitalization` | If true, calculated the edit distances on lower case versions. |  

### `contains`
Returns a [Boolean](../Classes/Boolean.md) indicating if the String contains string.
```supercollider
"These are several words".contains("are").postln;
"These are several words".contains("fish").postln;
```


### `containsi`
Same as [contains](#contains), but case insensitive.
```supercollider
"These are several words".containsi("ArE").postln;
```


### `containsStringAt`
Returns a [Boolean](../Classes/Boolean.md) indicating if the String contains string beginning at the specified index.
```supercollider
"These are several words".containsStringAt(6, "are").postln;
```


### `icontainsStringAt`
Same as [containsStringAt](#containsstringat), but case insensitive.
### `beginsWith`

### `endsWith`
Returns true if this string begins/ends with the specified other string.**Arguments:**

| Argument | Description |
|----------|-------------|
| `string` | The other string |  
**Returns:** A [Boolean](../Classes/Boolean.md)

### Manipulating strings
### `rotate`
Rotate the string by n steps.
```supercollider
"hello word".rotate(1)
```


### `scramble`
Randomize the order of characters in the string.
```supercollider
"hello word".scramble
```


### `replace`
Like [tr](#tr), but with Strings as well as Chars as arguments.
```supercollider
"Here are several words which are fish".replace("are", "were");
```


### `format`
Returns a formatted string with arguments. The % character in the format string is replaced by a string representation of an argument. To print a % character use \\% .
```supercollider
format("this % a %. pi = %, list = %\n", "is", "test", pi.round(1e-4), (1..4))

this is a test. pi = 3.1416, list = [1, 2, 3, 4]
```


### `escapeChar`
Add the escape character (\) before any character of your choice.
```supercollider
// escape spaces:
"This will become a Unix friendly string".escapeChar($ ).postln;
```


### `quote`
Return this string enclosed in double-quote (`"`) characters.
```supercollider
"tell your" + "friends".quote + "not to tread onto the lawn"
```


### `zeroPad`
Return this string enclosed in space characters.
```supercollider
"spaces".zeroPad.postcs;
```


### `underlined`
Return this string followed by dashes in the next line (`-`).
```supercollider
"underlined".underlined;
"underlined".underlined($~);
```


### `tr`
Transliteration. Replace all instances of **from** with **to**.
```supercollider
":-(:-(:-(".tr($(, $)); // turn the frowns upside down
```


### `padLeft`

### `padRight`
Pad this string with **string** so it fills **size** character.**Arguments:**

| Argument | Description |
|----------|-------------|
| `size` | Number of characters to fill |  
| `string` | Padding string
```supercollider
"this sentence has thirty-nine letters".padRight(39, "-+");
"this sentence has thirty-nine letters".padLeft(39, "-+");
"this sentence more than thirteen letters".padRight(13, "-+"); // nothing to pad.
``` |  

### `toUpper`
Return this string with uppercase letters.
```supercollider
"Please, don't be impolite".toUpper;
```


### `toLower`
Return this string with lowercase letters.
```supercollider
"SINOSC".toLower;
```


### `stripRTF`
Returns a new String with all RTF formatting removed.
```supercollider
(
// same as File-readAllStringRTF
g = File("/code/SuperCollider3/build/Help/UGens/Chaos/HenonC.help.rtf", "r");
g.readAllString.stripRTF.postln;
g.close;
)
```


### `split`
Returns an Array of Strings split at the separator. The separator is a [Char](../Classes/Char.md), and is **not** included in the output array.
```supercollider
"These are several words".split($ );

// The default separator $/ is handy for Unix paths.
"This/could/be/a/Unix/path".split;
```



### Stream support
### `printOn`
Print the String on stream.
```supercollider
"Print this on Post".printOn(Post);

// equivalent to:
Post << "Print this on Post";
```


### `storeOn`
Same as [printOn](#printon), but formatted [asCompileString](#ascompilestring).
```supercollider
"Store this on Post".storeOn(Post);

// equivalent to:
Post <<< "Store this on Post";
```



### Unix Support
Where relevant, the current working directory is the same as the location of the SuperCollider app and the shell is the Bourne shell (sh). Note that the cwd, and indeed the shell itself, does not persist:


```supercollider
"echo $0".unixCmd; // print the shell (sh)
"pwd".unixCmd;
"cd Help/".unixCmd;
"pwd".unixCmd;

"export FISH=mackerel".unixCmd;
"echo $FISH".unixCmd;
```


It is however possible to execute complex commands:


```supercollider
"pwd; cd Help/; pwd".unixCmd;
"export FISH=mackerel; echo $FISH".unixCmd;
```


Also on os x applescript can be called via osascript:


```supercollider
"osascript -e 'tell application \"Safari\" to activate'".unixCmd;
```


Should you need an environment variable to persist you can use [setenv](#setenv).


> **Note:** Despite the fact that the method is called 'unixCmd', **it does work in Windows**. The string must be a DOS command, however: "dir" rather than "ls" for instance.


### `unixCmd`
Executes an operating system command **asynchronously** using the standard shell (`sh` on *nix, `cmd` on Windows).If you want to run a command without a shell, please use [SequenceableCollection#-unixCmd](../Classes/SequenceableCollection.md#-unixcmd).**Arguments:**

| Argument | Description |
|----------|-------------|
| `action` | A [Function](../Classes/Function.md) that is called when the process has exited. It is passed two arguments: the exit code and pid of the exited process. |  
| `postOutput` | A [Boolean](../Classes/Boolean.md) that controls whether or not the output of the process is displayed in the post window. |  
**Returns:** An [Integer](../Classes/Integer.md) - the pid of the **shell** running the command, not of the command itself (see note below for exceptions).To get the actual pid of the command, use [SequenceableCollection#-unixCmd](../Classes/SequenceableCollection.md#-unixcmd), which does not use a shell and returns the actual pid of the command.Use [Integer#-pidRunning](../Classes/Integer.md#-pidrunning) to test if a process is alive.
> **Note:** While the underlying system call will obtaing the pid of the shell, we may get an actual pid of the command in the following situations:- On *nix systems, if the command is run with `exec`, e.g. `"exec scsynth -u 57110".unixCmd;`, which causes the calling process (the shell) to be replaced with the new command;
- On macOS specifically, if the command consists of a single executable, where macOS seems the optimize the call by not spawining a new shell.
Past documentation incorrectly stated that this method always returned the pid of the actual command.Note that `exec` is not available on Windows.

Example:
```supercollider
"ls Help".unixCmd;
"echo one; sleep 1; echo two; sleep 1".unixCmd { |res, pid| [\done, res, pid].postln };
```


### `unixCmdGetStdOut`
Similar to [unixCmd](#unixcmd) except that the stdout of the process is returned (**synchronously**) rather than sent to the post window.
```supercollider
~listing = "ls Help".unixCmdGetStdOut; // Grab
~listing.reverse.as(Array).dupEach.join.postln; // Mangle
```


### `systemCmd`
Executes an operating system command **synchronously** using the standard shell (`sh` on *nix, `cmd` on Windows).**Returns:** Error code of the system command
### `runInTerminal`
Execute the String in a new terminal window (**asynchronously**).**Arguments:**

| Argument | Description |
|----------|-------------|
| `shell` | The shell used to execute the string. |  

> **Note:** On macOS and Linux, the string is incorporated into a temporary script file and executed using the shell.


> **Note:** On Linux, it is possible to choose a specific terminal emulator to be used, otherwise sclang tries to find one by itself. See [LinuxPlatform#*runInTerminalCmd](../Classes/LinuxPlatform.md#*runinterminalcmd).

Example:
```supercollider
"echo ---------Hello delightful SuperCollider user----------".runInTerminal;
```


### `setenv`
Set the environment variable indicated in the string to equal the String **value**. This value will persist until it is changed or SC is quit. Note that if **value** is a path you may need to call [standardizePath](#standardizepath) on it.
```supercollider
// all defs in this directory will be loaded when a local server boots
"SC_SYNTHDEF_PATH".setenv("~/scwork/".standardizePath);
"echo $SC_SYNTHDEF_PATH".unixCmd;
```


### `getenv`
Returns the value contained in the environment variable indicated by the String.
```supercollider
"USER".getenv;
```


### `unsetenv`
Set the environment variable to nil.
### `mkdir`
Make a directory from the given path location.
### `pathMatch`
Returns an [Array](../Classes/Array.md) containing all paths matching this String. Wildcards apply, non-recursive.
```supercollider
Post << "Help/*".pathMatch;
```


### `load`
Load and execute the file at the path represented by the receiver.
### `loadPaths`
Perform [pathMatch](#pathmatch) on this String, then load and execute all paths in the resultant [Array](../Classes/Array.md).
```supercollider
// first prepare a file with some code...
(
File.use(Platform.defaultTempDir +/+ "loadPaths_example.scd", "w", { |file|
    file << "\"This text is the result of a postln command which was loaded and executed by loadPaths\".postln;";
    file <<    "\"I will now throw a dice for you: \".post; 7.rand;"
})
)

// then load the file...
// ... it posts some text, and the return value of loadPaths is an array of the return values of each file
(Platform.defaultTempDir +/+ "loadPaths_example.scd").loadPaths;
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `warn` | Post a warning if path doesn't point to any file. |  
| `action` | If a function is passed, it is called with each path as argument. |  

### `loadRelative`
Load and execute the file at the path represented by the receiver, interpreting the path as relative to the current document or text file. Requires that the file has been saved. This can be used e.g. to load initialization code from files in the same folder.**Arguments:**

| Argument | Description |
|----------|-------------|
| `warn` | Warn if a file is not found. |  
| `action` | A function that is called for each file path that is found. |  

### `resolveRelative`
Convert the receiver from a relative path to an absolute path, relative to the current document or text file. Requires that the current text file has been saved. Absolute paths are left untransformed.
### `standardizePath`
Expand ~ to your home directory, and resolve aliases on macOS. See [PathName](../Classes/PathName.md) for more complex needs. See [File#*realpath](../Classes/File.md#*realpath) if you want to resolve symlinks.
```supercollider
"~/".standardizePath; // This will print your home directory
```


### `openOS`
Open file, directory or URL via the operating system. On macOS this is implemented via `open`, on Linux via `xdg-open` and on Windows via `start`.
```supercollider
Platform.userConfigDir.openOS;
"http://supercollider.sf.net".openOS;
```



### Pathname Support
Also see [#-+/+](#-+/+) for path concatenation.

The term "path separator" is a platform-independent term for the character(s) that can be used to separate components of a path. On Windows, both forward slash "/" and backward slash "\\" are path separators. On POSIX-based systems like macOS and Linux, only forward slash is allowed.

### `shellQuote`
Return a new string suitable for use as a filename in a shell command, by enclosing it in single quotes (`'`). If the string contains any single quotes they will be escaped.You should use this method on a path before embedding it in a string executed by [unixCmd](#unixcmd) or [systemCmd](#systemcmd).
```supercollider
unixCmd("ls " + Platform.userExtensionDir.shellQuote)
```


> **Note:** This works well with shells such as **bash**, other shells might need different quotation/escaping. Apart from usage in the construction of shell commands, **escaping is not needed** for paths passed to methods like pathMatch(path) or File.open(path).


### `absolutePath`

### `asAbsolutePath`
Return this path as an absolute path by prefixing it with [File#*getcwd](../Classes/File.md#*getcwd) if necessary.
### `asRelativePath`
Return this path as relative to the specified path.**Arguments:**

| Argument | Description |
|----------|-------------|
| `relativeTo` | The path to make this path relative to. |  

### `withTrailingSlash`
Appends a path separator if one is not already present.
### `withoutTrailingSlash`
Removes a trailing path separator if one is present.
### `basename`
Return the filename from a filesystem path.
```supercollider
"Imaginary/Directory/fish.rtf".basename;
```


### `dirname`
Return the directory name from a filesystem path.
```supercollider
"Imaginary/Directory/fish.rtf".dirname;
```


### `splitext`
Split off the extension from a filename or path and return both in an [Array](../Classes/Array.md) as [path or filename, extension].
```supercollider
"fish.rtf".splitext;
"Imaginary/Directory/fish.rtf".splitext;
```



### YAML and JSON parsing
### `parseYAML`
Parse this string as YAML/JSON.**Returns:** A nested structure of [Array](../Classes/Array.md)s (for sequences), [Dictionaries](../Classes/Dictionary.md) (for maps) and [String](../Classes/String.md)s (for scalars).
### `parseYAMLFile`
Same as `parseYAML` but parse a file directly instead of a string. This is faster than reading a file into a string and then parse it.
### `parseJSON`
This method is currently just an alias for [parseYAML](#parseyaml), in the future it will only accept valid JSON.**Returns:** A nested structure of [Array](../Classes/Array.md)s (for sequences), [Dictionaries](../Classes/Dictionary.md) (for maps) and [String](../Classes/String.md)s (for scalars).
```supercollider
"{ \"a\": 1 }".parseYAML;
"{ \"a\": 1 }".parseJSON;
```


### `parseJSONFile`
This method is currently just an alias for [parseYAMLFile](#parseyamlfile), in the future it will only accept valid JSON files.

### Document Support
### `newTextWindow`
Create a new [Document](../Classes/Document.md) with this.
```supercollider
"Here is a new Document".newTextWindow;
```


### `openDocument`
Create a new [Document](../Classes/Document.md) from the path corresponding to this. The selection arguments will preselect the indicated range in the new window. Returns this.
```supercollider
(
String.filenameSymbol.asString.openDocument(10, 20)
)
```


### `findHelpFile`
Returns the path for the helpfile named this, if it exists, else returns nil.
```supercollider
"Document".findHelpFile;
"foobar".findHelpFile;
```


### `help`
Performs [findHelpFile](#findhelpfile) on this, and opens the file it if it exists, otherwise opens the main helpfile.
```supercollider
"Document".help;
"foobar".help;
```



### Misc methods
### `inspectorClass`
Returns class [StringInspector](../Classes/StringInspector.md).

### Drawing Support
The following methods must be called within an Window-drawFunc or a SCUserView-drawFunc function, and will only be visible once the window or the view is refreshed. Each call to Window-refresh SCUserView-refresh will 'overwrite' all previous drawing by executing the currently defined function.

See also: [Window](../Classes/Window.md), [UserView](../Classes/UserView.md), [Color](../Classes/Color.md), and [Pen](../Classes/Pen.md).


> **Note:** for cross-platform GUIs, use `Pen.stringAtPoint, Pen.stringInRect, Pen.stringCenteredIn, Pen.stringLeftJustIn, Pen.stringRightJustIn` instead.


### `draw`
Draws the String at the current 0@0 [Point](../Classes/Point.md). If not transformations of the graphics state have taken place this will be the upper left corner of the window. See also [Pen](../Classes/Pen.md).
```supercollider
(
w = Window.new.front;
w.view.background_(Color.white);
w.drawFunc = {
    "abababababa\n\n\n".scramble.draw
};
w.refresh
)
```


### `drawAtPoint`
Draws the String at the given [Point](../Classes/Point.md) using the [Font](../Classes/Font.md) and [Color](../Classes/Color.md) specified.
```supercollider
(
w = Window.new.front;
w.view.background_(Color.white);
w.drawFunc = {
    "abababababa\n\n\n".scramble.drawAtPoint(
        100@100,
        Font("Courier", 30),
        Color.blue(0.3, 0.5))
};
w.refresh;
)
```


### `drawInRect`
Draws the String into the given [Rect](../Classes/Rect.md) using the [Font](../Classes/Font.md) and [Color](../Classes/Color.md) specified.
```supercollider
(
w = Window.new.front;
r = Rect(100, 100, 100, 100);
w.view.background_(Color.white);
w.drawFunc = {
    "abababababa\n\n\n".scramble.drawInRect(r, Font("Courier", 12), Color.blue(0.3, 0.5));
    Pen.strokeRect(r);
};
w.refresh;
)
```


### `drawCenteredIn`
Draws the String into the given Rect using the Font and Color specified.
```supercollider
(
w = Window.new.front;
w.view.background_(Color.white);
r = Rect(100, 100, 100, 100);
w.drawFunc = {
    "abababababa\n\n\n".scramble.drawCenteredIn(
        r,
        Font("Courier", 12),
        Color.blue(0.3, 0.5)
    );
    Pen.strokeRect(r);
};
w.refresh;
)
```


### `drawLeftJustIn`
Draws the String into the given Rect using the Font and Color specified.
```supercollider
(
w = Window.new.front;
w.view.background_(Color.white);
r = Rect(100, 100, 100, 100);
w.drawFunc = {
    "abababababa\n\n\n".scramble.drawLeftJustIn(
        r,
        Font("Courier", 12),
        Color.blue(0.3, 0.5)
    );
    Pen.strokeRect(r);
};
w.refresh;
)
```


### `drawRightJustIn`
Draws the String into the given [Rect](../Classes/Rect.md) using the [Font](../Classes/Font.md) and [Color](../Classes/Color.md) specified.
```supercollider
(
w = Window.new.front;
w.view.background_(Color.white);
r = Rect(100, 100, 100, 100);
w.drawFunc = {
    "abababababa\n\n\n".scramble.drawRightJustIn(
        r,
        Font("Courier", 12),
        Color.blue(0.3, 0.5)
    );
    Pen.strokeRect(r);
};
w.refresh;
)
```


### `bounds`
Tries to return a [Rect](../Classes/Rect.md) with the size needed to fit this string if drawn with given font.**Arguments:**

| Argument | Description |
|----------|-------------|
| `font` | A [Font](../Classes/Font.md) |  



