# Char

*ASCII character*

**Related:** [String](../Classes/String.md)

**Categories:** Core

## Description

An ASCII character represented as a signed 8-bit integer (-128 to 127). Valid ASCII values are in the range 0-127. Chars may be written as literals using the $ sign. For example: $a, $b, $c. Some special characters can be expressed as literals using escape sequences (for example, `$\n` for newline). See [Literals#Characters](../Reference/Literals.md#characters) for more information.
Chars may be created from [Integers](../Classes/Integer.md) using the methods [Integer#-asAscii](../Classes/Integer.md#-asascii) and [Integer#-asDigit](../Classes/Integer.md#-asdigit).
Note that, while Char does not support encodings aside from ASCII—such as multi-byte encodings like UTF-8 and UTF-16, or the full Latin-1 (ISO 8859-1) character set—Chars with negative values are perfectly legal, and may be strung together in strings that use these encodings.
The SuperCollider IDE uses UTF-8 to decode and display strings. See [String](../Classes/String.md) for more information.


## Class Methods

### `nl`
Newline `($\n)`.
### `ret`
Carriage return `($\r)`.
### `tab`
Horizontal tab `($\t)`.
### `ff`
Form feed `($\f)`.
### `vtab`
Vertical tab `($\v)`.
### `space`
Single space `($ )`.
### `comma`
Comma `($,)`.
### `bullet`
Asterisk `($*)`.
### `binaryOpCharacters`
A string containing all characters allowed in a binary operator: `"!@%&*-+=|<>?/"`.

## Instance Methods


### conversion
### `hash`
**Returns:** the hash value of the receiver.
### `ascii`
**Returns:** the integer ASCII value of a Char.
### `digit`
**Returns:** an integer value from 0 to 9 for chars $0 to $9, and values 10 to 35 for chars $a to $z or $A to $Z.
### `asAscii`
**Returns:** the object itself.
### `asUnicode`
**Returns:** the object itself.
### `toUpper`
**Returns:** the upper case version of a char. Nonalphabetic chars return themselves.
### `toLower`
**Returns:** a lower case version of a char. Nonalphabetic chars return themselves.

### Testing
### `isAlpha`
**Returns:** whether the char is an alphabetic character.
### `isAlphaNum`
**Returns:** whether the char is an alphabetic or numeric character.
### `isPrint`
**Returns:** whether the char is printable.
### `isPunct`
**Returns:** whether the char is a punctuation character.
### `isControl`
**Returns:** true if the char is a control character.
### `isSpace`
**Returns:** true if the char is white space: any of `[$ , $\f, $\n, $\r, $\t, $\v]`.
### `isDecDigit`
**Returns:** true if the char is a decimal digit $0 to $9.
### `isFileSafe`
**Returns:** true if the char is safe for use in a filename. Excludes the path separators / and :
```supercollider
 for(0, 255, { |i|
    var a;
    [i, a = i.asAscii, a.isAlphaNum, a.isPrint, a.isPunct, a.isControl].postln;
});
```


### `isLower`
**Returns:** true if the char is a lowercase letter.
### `isUpper`
**Returns:** true if the char is a uppercase letter.
### `isPathSeparator`
**Returns:** true if the char is one of the platform specific path separators.
### `isVowel`
**Returns:** true if the char is a vowel.
### `++`
**Returns:** `this.asString ++ that`
### `<`
**Returns:** `this.ascii < aChar.ascii`
### `==`
**Returns:** True if the receiver equals the argument.


