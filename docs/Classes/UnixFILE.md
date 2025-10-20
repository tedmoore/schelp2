# UnixFILE

*An abstract class*

**Related:** [File](../Classes/File.md), [Pipe](../Classes/Pipe.md)

**Categories:** Files


## Instance Methods


### `isOpen`
Returns whether the file is open. An open request can fail if a file cannot be found for example. This method lets you test that the open call succeeded.
### `pos`
Answer the current file position**Arguments:**

| Argument | Description |
|----------|-------------|
| `offset` | an offset in bytes. |  
| `origin` | one of the following [Integer](../Classes/Integer.md)s:
**0**
: seek from beginning of file.

**1**
: seek from current position in file.

**2**
: seek from end of file. |  

### `write`
Writes an item to the file.**Arguments:**

| Argument | Description |
|----------|-------------|
| `item` | one of the following:
**[Float](../Classes/Float.md)**
: 

**[Integer](../Classes/Integer.md)**
: 

**[Char](../Classes/Char.md)**
: 

**[Color](../Classes/Color.md)**
: 

**[Symbol](../Classes/Symbol.md)**
: writes the name of the Symbol as a C string.

**[RawArray](../Classes/RawArray.md)**
: write the bytes from any RawArray in big endian. |  

### `getLine`
reads and returns a [String](../Classes/String.md) up to lesser of next newline or 1023 chars.
### `getChar`
read one byte and return as a [Char](../Classes/Char.md).
### `getInt8`
read one byte and return as a [Integer](../Classes/Integer.md).
### `getInt16`
read two bytes and return as an [Integer](../Classes/Integer.md).
### `getInt32`
read four bytes and return as an [Integer](../Classes/Integer.md).
### `getFloat`
read four bytes and return as a [Float](../Classes/Float.md).
### `getDouble`
read eight bytes and return as a [Float](../Classes/Float.md).
### `getPascalString`
Reads the next byte as an unsigned integer N, then reads the following N bytes and returns them as a [String](../Classes/String.md).
### `putChar`
write a [Char](../Classes/Char.md) as one byte.
### `putInt8`
write an [Integer](../Classes/Integer.md) as one byte. That is a signed [Integer](../Classes/Integer.md) value between -128 and 127.
### `putInt16`
write an [Integer](../Classes/Integer.md) as two bytes.
### `putInt32`
write an [Integer](../Classes/Integer.md) as four bytes.
### `putFloat`
write a [Float](../Classes/Float.md) as four bytes.
### `putDouble`
write a [Float](../Classes/Float.md) as eight bytes.
### `putString`
write a null terminated [String](../Classes/String.md).
### `putPascalString`
Writes `aString` preceded by its length represented as a single byte. Throws an error if `aString` is longer than 255 characters.
### `putString0`
Writes `aString` followed by a zero byte, like a null-terminated C string.

