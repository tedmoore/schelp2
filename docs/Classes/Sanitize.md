# Sanitize

*Remove infinity, NaN, and denormals*

**Categories:** UGens>Info

## Description

Replaces infinities, NaNs, and subnormal numbers (denormals) with a given signal, zero by default. The method [UGen#-sanitize](../Classes/UGen.md#-sanitize) provides a shorthand for this.
See also [CheckBadValues](../Classes/CheckBadValues.md), which allows you to discriminate specific kinds of bad values and print information about them to the post window.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | Input signal to sanitize. |  
| `replace` | The signal that replaces bad values. |  


