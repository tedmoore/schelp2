# Functions

*lambda expressions*

**Categories:** Language

**Related:** [Function](../Classes/Function.md), [AbstractFunction](../Classes/AbstractFunction.md), [FunctionDef](../Classes/FunctionDef.md)


## Introduction
A [Function](../Classes/Function.md) is an expression which defines operations to be performed when it is sent the `value` message. In functional languages, a function would be known as a lambda expression. Function definitions are enclosed in curly brackets `{}`. Argument declarations, if any, follow the open bracket. Variable declarations follow argument declarations. An expression follows the declarations.


```supercollider
{ |a, b, c|
    var d;
    d = a * b;
    c + d
}
```


Functions are not evaluated immediately when they occur in code, but are themselves objects that can be passed around.

A function object may be evaluated by passing it the `value` message, or its shorthand `.()`, and a list of arguments.

When evaluated, the function object returns the final value of its expression.


```supercollider
f = { |a, b| a + b };
f.value(4, 5).postln;
f.(4, 5).postln; // same as above
f.(10, 200).postln;
```


An empty function object returns the value nil when evaluated.


```supercollider
{}.value.postln;
```


Arguments can also be provided by name.


```supercollider
f = { |a, b| a + b };
f.(a: 10, b: 2) // 12

f.(b: 3, a: 10) // 13, order does not matter for keywords
f.(3, b: 4) // 7, 'a' is always first argument

f.(3, a: 4) // Error: Duplicate keyword 'a' at position 0.

f.(a: 3) // Error: binary operator '+' failed, b is 'nil' and you cannot add a number and 'nil'
```


A function can be thought as a machine able to perform a task on demand, e.g. a calculator. The calculator can receive input (args) and can output a value, the result of the performed operations. The function definition can then be thought as the building of the calculator: once built, the calculator does nothing until it is requested to work (by passing the value method to a function). The following figure depicts an empty function, input without output, output without input, and the general case with input and output.

![functions.png / Functions ](functions.png#Functions)


## Arguments
An argument list immediately follows the open curly bracket of a function definition. An argument list either begins with the reserved word `arg`, or is contained between two vertical bars. If a function takes no arguments, then the argument list may be omitted.

Names of arguments in the list may be initialized to a default value using the following syntax forms. Arguments which are not explicitly initialized will be set to nil if no value is passed for them.

"arg" style, default value is a literal: `{ arg x = 1; .... }` [#[1]](#[1])

"arg" style, default value is an expression: `{ arg x = 10.rand; ... }` [#[2]](#[2])

"arg" style, default value is a literal but you want to treat it like an expression: `{ arg x = (2); ... }` [#[2]](#[2])

Pipe style, default value is a literal: `{ |x = 1| ... }` [#[1]](#[1])

Pipe style, default value is an expression: `{ |x = (10.rand)| ... }` [#[2]](#[2])

In general arguments may be initialized to literals or expressions, but in the case of [Function#-play](../Classes/Function.md#-play) or [SynthDef#-play](../Classes/SynthDef.md#-play), they may only be initialized to literals.


```supercollider
// this is okay:

{ arg a = Array.geom(4, 100, 3); a * 4 }.value;

// this is not:

{ arg freq = Array.geom(4, 100, 3); Mix(SinOsc.ar(freq, 0, 0.1)) }.play; // silence

// but this is:
{ arg freq =  #[ 100, 300, 900, 2700 ]; Mix(SinOsc.ar(freq, 0, 0.1)) }.play; // produces sound!
```


See [Literals](../Reference/Literals.md) for more information.



## Variable Arguments
Variable arguments are how functions catch an unknown number of arguments or keyword arguments.  There are two possible variable arguments, the first for positional arguments, and second for keyword arguments. They are marked by an ellipsis after any normal arguments and separated by a comma.

The first variable argument (positional) catches all remaining arguments in an [Array](../Classes/Array.md)


```supercollider
f = { |a ... args| "a: %, args: %".format(a, args) };

f.(1, 2, 3) // a: 1, args: [2, 3]
f.(1) // a: 1, args: []
f.(a: 1) // a: 1, args: []

// catches all arguments
g = { |...args| "args: %".format(args) };

g.(1, 2, 3) // args: [1, 2, 3]
g.() // args: []
```


The second variable argument catches all keyword arguments. It puts them in an [Array](../Classes/Array.md) of key-value pairs.


```supercollider
f = { |...args, kwargs| "args: %, kwargs: %".format(args, kwargs) };

f.(1, 2, 3) // args: [1, 2, 3], kwargs: []

f.(a: 10) // args: [], kwargs: [a, 10]

f.(1, 2, 3, meow: 10, woof: 20) // args: [1, 2, 3], kwargs: [meow, 10, woof, 20]
```


The use of variable keyword arguments is often paired with [Object#-performArgs](../Classes/Object.md#-performargs).

While you can pick any name for the variable arguments, they always refer to the unmatched positional and keyword arguments, so it is often best to name them `args` and `kwargs`.

You cannot reassign the value of the variable arguments at the call–site even if they share the same name (see below for example).


```supercollider
f = { |...args, kwargs| "args: %, kwargs: %".format(args, kwargs) };
f.(args: 10, kwargs: 20) // args: [], kwargs: [args: 10, kwargs: 20]

f = { |...a, b| "a: %, b: %".format(a, b) };
f.(a: 10, b: 20) // a: [], b: [a: 10, b: 20]
```


<a id="[1]"></a>


### [1] Literal argument defaults
Argument defaults that are literals are stored as part of the [FunctionDef](../Classes/FunctionDef.md). Arguments passed at runtime — including nil — always override the defaults:


```supercollider
f = { |x = 1| x };
f.(2);  // prints 2

f.();   // prints 1

f.(nil);  // prints nil
```


<a id="[2]"></a>




### [2] Expression argument defaults
Since expressions are evaluated when the function is called, they cannot be stored in the [FunctionDef](../Classes/FunctionDef.md). They are executed only if the passed-in value is nil.


```supercollider
f = { |x = (10.rand)| x };
f.value(100);  // prints 100

f.value;   // prints a number 0-9

f.(nil);   // prints a number 0-9!
```


This means you can use expression-style to define a default that cannot be overridden by nil.


```supercollider
f = { |x = (3)| x };
f.(nil);   // prints 3
```


Note: Parentheses are required when initializing an argument to an expression, if the argument list is written inside `||` pipes.


```supercollider
(
var abc = 2;
{ arg x = abc+1; x }   // OK
)

(
var abc = 2;
{ |x = abc+1| x }
)
ERROR: Parse error
   in file 'selected text'
   line 1 char 10:
  { |x = abc•+1| x }
-----------------------------------
ERROR: Command line parse failed

(
var abc = 2;
{ |x = (abc+1)| x }   // OK
)

(
var abc = 2;
{ |x (abc+1)| x }   // In ||, the = may be omitted if () are there
)
```


This is because the pipe character also serves as a binary operator. Without parentheses, expressions such as the following are ambiguous:


```supercollider
{ |a, b, c = a | b | c }
```


The following produce identical function definitions. Expression-style defaults are simply a shortcut syntax for the latter.


```supercollider
{ arg x = 10.rand; x };

{    arg x;
    x ?? { x = 10.rand };
    x
};
```






## Variables
Following the argument declarations are the variable declarations. These may be declared in any order. Variable lists are preceded by the reserved word `var`. There can be multiple var declaration lists if necessary. Variables may be initialized to default values in the same way as arguments. Variable declarations lists may not contain an ellipsis.


```supercollider
var level=0, slope=1, curve=1;
```






