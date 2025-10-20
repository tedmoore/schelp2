# Int16Array

*an array whose indexed slots are all of the same type*

**Related:** [FloatArray](../Classes/FloatArray.md), [Int8Array](../Classes/Int8Array.md), [Int32Array](../Classes/Int32Array.md), [DoubleArray](../Classes/DoubleArray.md), [SymbolArray](../Classes/SymbolArray.md)

**Categories:** Collections>Ordered

## Description

These classes implement arrays whose indexed slots are all of the same type.
- Int8Array - 8 bit integer
- Int16Array - 16 bit integer
- Int32Array - 32 bit integer
- FloatArray - 32 bit floating point
- DoubleArray - 64 bit floating point
- SymbolArray - symbols


> **Note:** The overflow behavior of an element in an Int16Array is undefined. This occurs whenever the result of an operation does not fit in the range of values supported by the return type, in this case, a 16-bit signed integer.




## Instance Methods


### `readFromStream`


