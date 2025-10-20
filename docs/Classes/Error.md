# Error

**Categories:** Core

*superclass of all Errors*

## Description

Error and its subclasses separate different types of error is that can occur in the SuperCollider program into distinct classes, so that they can be reported differently to the user.
Anywhere that an error must be reported to the user and execution must stop, an error object must be created and thrown.

```
(
var file, path = "betcha-this-file-doesnt-exist.txt";
if((file = File(path, "r")).isOpen) {
    "File is % bytes long.\n".postf(file.length);
    file.close;
} {
    Error("File % could not be opened.".format(path)).throw;
};
)
```


For backward compatibility, `.die()` creates the error for you.

```
"Keyboard not found. Press F1 to Resume.".die;
```


Throwing an error object gives the caller the opportunity to catch, and possibly recover from, the error. See the Exception help file for more information about this.

### Error hierarchy
The following error classes exist in the main library.

- [Error](../Classes/Error.md)
- [DeprecatedError](../Classes/DeprecatedError.md) : this method is no longer supported.
- [MethodError](../Classes/MethodError.md) : generic error occurring within a method.
- [DoesNotUnderstandError](../Classes/DoesNotUnderstandError.md) : the receiver does not understand the method name.
- [BinaryOpFailureError](../Classes/BinaryOpFailureError.md) : a binary operator cannot work with the operand classes.
- [ImmutableError](../Classes/ImmutableError.md) : attempted to modify an immutable object.
- [MustBeBooleanError](../Classes/MustBeBooleanError.md) : a test (in if or while) returned a non-Boolean value.
- [NotYetImplementedError](../Classes/NotYetImplementedError.md) : the method name exists, but isn't implemented yet.
- [OutOfContextReturnError](../Classes/OutOfContextReturnError.md) : a method return by ^ took place outside of a method.
- [PrimitiveFailedError](../Classes/PrimitiveFailedError.md) : an error occurred inside a primitive.
- [ShouldNotImplementError](../Classes/ShouldNotImplementError.md) : you called a method on a class that has no business implementing it.
- [SubclassResponsibilityError](../Classes/SubclassResponsibilityError.md) : you called a method on an abstract class.


The exact inheritance tree looks like this:





