# Int32Array

*an array whose indexed slots are all of the same type*

**Related:** [FloatArray](../Classes/FloatArray.md), [Int8Array](../Classes/Int8Array.md), [Int16Array](../Classes/Int16Array.md), [DoubleArray](../Classes/DoubleArray.md), [SymbolArray](../Classes/SymbolArray.md)

**Categories:** Collections>Ordered

## Description

These classes implement arrays whose indexed slots are all of the same type.
- Int8Array - 8 bit integer
- Int16Array - 16 bit integer
- Int32Array - 32 bit integer
- FloatArray - 32 bit floating point
- DoubleArray - 64 bit floating point
- SymbolArray - symbols


> **Note:** The overflow behavior of an element in an Int32Array is undefined. This occurs whenever the result of an operation does not fit in the range of values supported by the return type, in this case, a 32-bit signed integer.Elements in Int32Array are not guaranteed to behave like [Integer](../Classes/Integer.md)s.




## Instance Methods

### `readFromStream`


