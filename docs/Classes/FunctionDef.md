# FunctionDef

*FunctionDefs contain code which can be executed from a Function.*

**Categories:** Core>Kernel

**Related:** [Function](../Classes/Function.md)

## Description


### Related Keywords
### `thisFunctionDef`
The global pseudo-variable `thisFunctionDef` always evaluates to the current enclosing FunctionDef.See also: [thisFunction](../Classes/Function.md#.thisfunction)



## Instance Methods


### Accessing
Even though it is possible to change the values in the various arrays that define the FunctionDef, you should not do it, unless you like to crash.

### `code`
Get the byte code array.
```supercollider
{ |a = 9, b = 10, c| a + b }.def.code;
```


### `sourceCode`
Get the source code string.
```supercollider
{ |a = 9, b = 10, c| a + b }.def.sourceCode.postcs;
```


### `numArgs`
Return the number of arguments (the arity) of the function.
```supercollider
{ |a = 9, b = 10, c| a + b }.def.numArgs; // 3
```


### `numVars`
Return the number of variables in the function body.
```supercollider
(
{ |x|
    var y, z;
    x + y + z
}.def.numVars; // 2
)
```


### `varArgs`
Return whether function has ellipsis argument.
```supercollider
{ |a, b ... c| a + b * c }.def.varArgs; // true
{ |a, b, c| a + b * c }.def.varArgs; // false
```


### `hasKwArgs`
Returns whether the function has variable keyword arguments
```supercollider
{ |a, b, c| a + b * c }.def.hasKwArgs; // false
{ |a, b ... c| a + b * c }.def.hasKwArgs; // false
{ |a ... b, c| a * b }.def.hasVarArgs; // true
```


### `varArgsValue`
Returns how many sets of variable arguments the function has. 0 for none, 1 for ellipsis arguments, 2 for keyword arguments.
```supercollider
{ |a, b, c| a + b * c }.def.varArgsValue; // 0
{ |a, b ... c| a + b * c }.def.varArgsValue; // 1
{ |a ... b, c| a * b }.def.varArgsValue; // 1
```


### `hasVarArgs`
Returns whether the function has variable args of any kind
```supercollider
{ |a, b, c| a + b * c }.def.hasVarArgs; // false
{ |a, b ... c| a + b * c }.def.hasVarArgs; // true
{ |a ... b, c| a * b }.def.hasVarArgs; // true
```


### `context`
Get the enclosing FunctionDef or Method.
### `findReferences`
return a list of all references to a given symbol.
### `argNames`
Get the Array of Symbols of the argument names.
```supercollider
{ |a = 9, b = 10, c| a + b }.def.argNames;
```


### `prototypeFrame`
Get the array of default values for argument and temporary variables.
```supercollider
{ |a = 9, b = 10, c| a + b }.def.prototypeFrame;
```


### `varNames`
Get the Array of Symbols of the local variable names.
```supercollider
{ |a = 9, b = 10, c| var x = 9; a + b + x }.def.varNames;
```


### `argumentString`
Return a string that contains all argument names and their default values for embedding in a string. If there are no arguments, it returns nil.
```supercollider
{ |a = 9, b = 10, c| a + b }.def.argumentString; // "a = 9, b = 10, c"
{ "nothing to see here" }.def.argumentString; // nil
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `withDefaultValues` | If set to false, no default values are appended
```supercollider
 // "a, b, c"
{ |a = 9, b = 10, c| a + b }.def.argumentString(withDefaultValues: false);
``` |  
| `withEllipsis` | If set to true, ellipsis characters (`" ... "`) are appended
```supercollider
// "a = 9, b = 10 ... c"
{ |a = 9, b = 10 ... c| a + b }.def.argumentString(withEllipsis: true);
// "a = 9, b = 10, c"
{ |a = 9, b = 10 ... c| a + b }.def.argumentString(withEllipsis: false);
``` |  
| `asArray` | If set to true, return the string for an array that represents all arguments. The other arguments are set to false.
```supercollider
// "[a, b] ++ c"
{ |a = 9, b = 10 ... c| a + b }.def.argumentString(asArray: true);
``` |  

### `makeEnvirFromArgs`
Get the Array of Symbols of the local variable names.
```supercollider
{ |a = 9, b = 10, c| a + b }.def.makeEnvirFromArgs;
```



### Generating Strings
### `makeFuncModifierString`
Return a string that can be interpreted as code for a new function which extracts the arguments from the receiver. This can be used to build a hygienic macro which returns a function with valid keyword arguments, instead of just anonymously forwarding the arguments, like in `{ |...args| func.valueArray(args) }`.For an implementation example [Function / flop ](../Classes/Function.md#flop) (as below).**Arguments:**

| Argument | Description |
|----------|-------------|
| `modifier` | A function to which a string is passed that represents the array of all arguments. It should return a string that can be interpreted.
```supercollider
// basic usage
f = { |x, y| x.squared + y.squared }; // a function
a = f.def.makeFuncModifierString({ |argString| "%.scramble".format(argString) });
a.interpret.value(4, 5)

// use as a macro: multichannel expansion like in flop
f = { |x, y = 1| if(x > 0) { 1 } { 0 } * y }; // some function
// generate the body of a function that has a free and yet undefined variable "func"
// -> "{ |x, y = 1| ([x, y]).flop.collect { |x| func.valueArray(x) } }"
a = f.def.makeFuncModifierString({ |str| str ++ ".flop.collect { |x| func.valueArray(x) }" });
// wrap that body into a function that takes "func" as argument and returns the function above
// now we have a valid code for a function:
// -> "{ |func| { |x, y = 1| [x, y].flop.collect { |x| func.valueArray(x) } } }"
b = "{ |func| % }".format(a);
// interpret the code to a function
g = b.interpret;
// pass the function f to g, which returns a function from a where "func" is bound to f
h = g.value(f);
// we can now use h in place of f, but all arguments are multichannel expanded:
f.([1, 0], [6, 7]); // does not work
h.([1, 0], [6, 7]); // [6, 0]
// and the new function supports the same keywords arguments:
h.(x: (-2..2), y: (-2..2));

// this functionality is implemented for function in the method "flop"
h = f.flop;
h.([1, 0], [6, 7]); // [6, 0]
``` |  


### Utilities
### `dumpByteCodes`
"Disassemble" and post the FunctionDef's byte code instructions to the text window.


