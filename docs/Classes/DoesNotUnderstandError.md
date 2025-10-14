# DoesNotUnderstandError

*Error thrown when calling an unknown method name*

**Categories:** Core

**Related:** [Error](../Classes/Error.md)

## Description

This error is typically generated when a method that doesn't exist on the receiver is called. Users typically do not construct this object themselves. The object has a few getters to learn more about the call that caused the error.
This method reports a backtrace as well as a best-guess suggested replacement based on edit distance.


## Class Methods

### `new`
Construct a new DoesNotUnderstandError, and choose a possible suggested replacement based on the class of the receiver and contents of the selector.**Arguments:**

| Argument | Description |
|----------|-------------|
| `receiver` | The object on which the method was called. |  
| `selector` | The method name that was not understood. |  
| `args` | Arguments passed to the unknown method. |  
| `keywordArgumentPairs` | The keyword arguments that were passed to the [DoesNotUnderstandError](../Classes/DoesNotUnderstandError.md). |  


## Instance Methods

### `selector`
**Returns:** The selector passed to new. Typically, the method name that was not understood.### `args`
**Returns:** The args passed to new. Typically, an array of arguments passed to the unknown method.### `suggestedCorrection`
**Returns:** If there is a method that the receiver would understand that looks similar to the unknown method name, the the [Method](../Classes/Method.md) object that corresponds to it. Otherwise, `nil`.### `errorString`
**Returns:** Short-form representation of the error as a [String](../Classes/String.md), with a suggested replacement if one was found.### `reportError`
Print a long-form explanation of the error including backtrace and suggested replacement if one was found.

