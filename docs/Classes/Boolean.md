# Boolean

*abstract class whose instances represent a logical value*

**Categories:** Core

**Related:** [Conditional-Execution](../Reference/Conditional-Execution.md)

## Description

Boolean is the superclass of [True](../Classes/True.md) and [False](../Classes/False.md) which are the concrete realizations. In code True and False are represented by the literal values `true` and `false`.


## Instance Methods

### `xor`
**Returns:** the exclusive or of the receiver and another Boolean.### `and`
If the receiver is true then answer the evaluation of function. If the receiver is false then function is not evaluated and the message answers false.### `or`
If the receiver is false then answer the evaluation of function. If the receiver is true then function is not evaluated and the message answers true.### `&&`
**Returns:** true if the receiver is true and aBoolean is true.### `||`
**Returns:** true if either the receiver is true or aBoolean is true.### `nand`
**Returns:** true unless both the operands are true (Sheffer stroke)### `not`
**Returns:** true if the receiver is false, and false if the receiver is true.### `if`
If the receiver is true, answer the evaluation of the trueFunc. If the receiver is false, answer the evaluation of the falseFunc.### `asInteger`
### `binaryValue`
**Returns:** 1 if the receiver is true, and 0 if the receiver is false.### `asBoolean`
### `booleanValue`
**Returns:** The receiver. The same message is understood by [SimpleNumber](../Classes/SimpleNumber.md) and can be used to convert it to boolean.### `keywordWarnings`
turn on/off warnings if a keyword argument is not found

