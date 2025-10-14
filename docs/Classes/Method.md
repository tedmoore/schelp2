# Method

**Categories:** Core>Kernel

*Code that implements an operation upon instances of a Class.*

**Related:** [Class](../Classes/Class.md)

## Description

A Method is code that is a part of the set of operations upon instances of a [Class](../Classes/Class.md).

### Related Keywords
### `thisMethod`
The global pseudo-variable `thisMethod` always evaluates to the enclosing Method in a class definition, much like `thisFunction`. When executed outside that context, it returns [Interpreter#-functionCompileContext](../Classes/Interpreter.md#-functioncompilecontext), the method within which all interpreted code executes.
```supercollider
// if the following code were compiled as part of the class library:
SomeClass {
    methodThatPostsItself {
        thisMethod.postln;
    }
}

// then running this would post
// "SomeClass:methodThatPostsItself"
a = SomeClass.new;
a.methodThatPostsItself;
```

`thisMethod` is frequently used to pass information to error-throwing methods. For example, the implementation of `Nil.new` is:
```supercollider
*new { ^this.shouldNotImplement(thisMethod) }
```

See also: [thisFunction](../Classes/Function.md#.thisfunction).



## Instance Methods

### `ownerClass`
**Returns:** The [Class](../Classes/Class.md) for which the method is part of the implementation.### `name`
**Returns:** A [Symbol](../Classes/Symbol.md) which is the name of the Method.### `primitiveName`
**Returns:** A [Symbol](../Classes/Symbol.md) which contains the name of the primitive function that implements the Method, if there is one.### `filenameSymbol`
**Returns:** A [Symbol](../Classes/Symbol.md) which is the full path of the source file that this method is defined in.

