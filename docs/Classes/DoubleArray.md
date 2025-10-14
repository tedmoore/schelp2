# DoubleArray

*an array of 64-bit double precision floating-point numbers*

**Related:** [FloatArray](../Classes/FloatArray.md), [Signal](../Classes/Signal.md)

**Categories:** Collections>Ordered

## Description

An array of 64-bit double precision floating point numbers.
Note that despite not having "Float" in its name, DoubleArray does in fact hold a sequence of SuperCollider double precision [floats](../Classes/Float.md). For a raw array of 32-bit floats, use [FloatArray](../Classes/FloatArray.md).
FloatArray and its subclass [Signal](../Classes/Signal.md) are commonly used to hold audio data in SuperCollider. Since almost all audio has 16-bit or 24-bit precision, using double precision floats for this purpose would be a waste of space. In other words, use FloatArray for audio, and DoubleArray for precise math operations.
The complete list of RawArray types in SuperCollider is:
- [Int8Array](../Classes/Int8Array.md) - 8 bit integer
- [Int16Array](../Classes/Int16Array.md) - 16 bit integer
- [Int32Array](../Classes/Int32Array.md) - 32 bit integer
- FloatArray - 32 bit floating point
- DoubleArray - 64 bit floating point
- [SymbolArray](../Classes/SymbolArray.md) - symbols


> **Note:** The overflow/underflow behavior of an element in a DoubleArray is undefined but usually `inf`/`-inf`, respectively. This occurs whenever the result of an operation does not fit in the range of values supported by the return type, in this case, a 64-bit floating point number.  See the note in [Float](../Classes/Float.md).




## Instance Methods

### `readFromStream`


