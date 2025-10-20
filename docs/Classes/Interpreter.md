# Interpreter

*The interpreter defines a context in which interactive commands are compiled and executed.*

**Categories:** Core>Kernel

**Related:** [How-to-Use-the-Interpreter](../Guides/How-to-Use-the-Interpreter.md)

## Description

The interpreter is an object that handles the translation and execution of code at runtime. It is that what runs any program code and defines a context for it.

```
(
a = 5 + 7;
this.cmdLine.postln;
)
```




## Class Methods



## Instance Methods


### Accessing
In the interpreter, `this` refers to the interpreter itself, e.g.: `this.postln`

The interpreter defines global variables (`a` … `z`), that can be used for interactive programming. Except these single letter variables ("interpreter variables"), all variables have to be defined by the keyword `var` (see: [Assignment](../Reference/Assignment.md), and [Scope](../Reference/Scope.md)).


```
// typical usage
a = 4;
b = 3;
b = b + a;

// some sound
a = Synth(\default);
g = fork { loop { 0.1.wait; a.set(\freq, 200 + 20.0.rand2.postln) } };
g.stop; a.free;

// an overview of all the variables
this.inspect;
```



> **Note:** Use these variables with a bit of extra care – as they are global, they remain in memory and one piece of code may happen to interfere with another one. The variable `s` is by convention bound to the default server ([Server](../Classes/Server.md)) and should not be changed.



### `clearAll`
set the values of the variables `a` through `z` to nil.
```
x = 123;
x.postln;
this.clearAll;
x.postln;
```



### Compile & Interpret

### `interpret`
Compile and execute a [String](../Classes/String.md).
```
this.interpret("(123 + 4000).postln");
```



### `interpretPrint`
Compile and execute a [String](../Classes/String.md), printing the result.
```
this.interpretPrint("123 + 4000");
```



### `compile`
Compile a String and return a [Function](../Classes/Function.md).
```
(
z = this.compile("(123 + 4000).postln");
z.postln;
z.value;
)
```



### `compileFile`
Reads the file at pathName, compiles it and returns a Function. The file must contain a valid SuperCollider expression, naturally. This will not compile class definitions, only expressions.

### `executeFile`
Reads the file at pathName, compiles it and executes it, returning the result. The file must contain a valid SuperCollider expression, naturally. This will not compile class definitions, only expressions.

### `cmdLine`
Returns the previously interpreted code.
```
1 + 2;
this.cmdLine
```



### `codeDump`
this interpreter variable can be set to evaluate a function with any successfully compiled code. see e.g. the class History.
```
a = []; // store all the code evaluated in a
this.codeDump = { |code| a = a.add(code) };
1 + 3;
f = { "hallo" };
a.postcs;
codeDump = nil; // reset to nil.
```



### `preProcessor`
If this is set to a function, all interactively executed code is piped through it before parsing and interpreting. This is mostly used for developing domain-specific live coding languages that piggyback off the SuperCollider editing environment.This function is called by [Interpreter#-interpretPrintCmdLine](../Classes/Interpreter.md#-interpretprintcmdline) with two arguments: the code string and the interpreter itself.
```
// silly but simple: understand a Saw for every SinOsc
this.preProcessor = { |code| code.replace("SinOsc", "Saw") };

{ SinOsc.ar(200) * 0.1 }.play;

preProcessor = nil; // reset to nil.
```



### `a`, `b`, `c`, `d`, `e`, `f`, `g`, `h`, `i`, `j`, `k`, `l`, `m`, `n`, `o`, `p`, `q`, `r`, `s`, `t`, `u`, `v`, `w`, `x`, `y`, `z`
Global variables ("interpreter variables") for interactive programming (see [#Accessing](#accessing)).

### `functionCompileContext`
The compiler uses this method as a virtual context in which to compile code.


