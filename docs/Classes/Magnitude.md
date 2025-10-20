# Magnitude

*Comparable value in a linear continuum*

**Categories:** Math

## Description

Magnitudes represent values along a linear continuum which can be compared against each other.


## Instance Methods


### `<`
**Returns:** a [Boolean](../Classes/Boolean.md) whether the receiver is less than **aMagnitude**.
### `<=`
**Returns:** a [Boolean](../Classes/Boolean.md) whether the receiver is less than or equal to **aMagnitude**.
### `>`
**Returns:** a [Boolean](../Classes/Boolean.md) whether the receiver is greater than **aMagnitude**.
### `>=`
**Returns:** a [Boolean](../Classes/Boolean.md) whether the receiver is greater than or equal to **aMagnitude**.
### `min`
**Returns:** the minimum of the receiver and aMagnitude.
### `max`
**Returns:** the maximum of the receiver and aMagnitude.
### `clip`
If the receiver is less than minVal then answer minVal, else if the receiver is greater than maxVal then answer maxVal, else answer the receiver.
### `inclusivelyBetween`
**Returns:** whether the receiver is greater than or equal to minVal and less than or equal to maxVal.
### `exclusivelyBetween`
**Returns:** whether the receiver is greater than minVal and less than maxVal.

