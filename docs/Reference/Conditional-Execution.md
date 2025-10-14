# Conditional Execution

*conditional expressions in SuperCollider*

**Categories:** Language

**Related:** [Boolean](../Classes/Boolean.md), [Function](../Classes/Function.md), [Exception](../Classes/Exception.md), [Syntax-Shortcuts](../Reference/Syntax-Shortcuts.md), [loop](../Reference/loop.md)

This page gives an overview of the conditional expressions in SuperCollider and the many ways to write them.

## Quick Overview

### Recommended syntax
| [#if](#if) | `if(expr) { trueFuncBody } { falseFuncBody }` | 
| --- | --- || [#case](#case) | `case { testFuncBody1 } { trueFuncBody1 } ... { testFuncBodyN } { trueFuncBodyN }` | | [#switch](#switch) | `switch(value) { testValue1 } { trueFuncBody1 } ... { testValueN } { trueFuncBodyN }` | | [#while](#while) | `while { testFuncBody } { loopFuncBody }` | 
More syntax variants exist, see [below](#syntax-of-conditional-expressions).


> **Note:** Throughout this file, the placeholder `someFuncBody` is distinct from `someFunc`  (e.g., `trueFunc` vs. `trueFuncBody`, `testFunc` vs. `testFuncBody`, etc.). In distinction from `someFunc`, `someFuncBody` does *not* stand for an already instantiated Function object (a lambda function), but rather for an expression that can serve as a Function definition. In other words, if `{ "doThis".postln }` is your `someFunc`, then `"doThis".postln;`---without the curly Brackets---is your `someFuncBody`.Consequently, **do not** write `if([false,true].choose) { { "doThis".postln; } }`, but **do** write `if([false,true].choose) { "doThis".postln; }`.





### Examples
|  |  | 
| --- | --- ||  |  | 
Quick links to sections:

1. [#if](#if),  [#case](#case), [#switch](#switch), [#while](#while) (specifics),
2. [optimization/inlining](#optimization-through-inline-expansion), 
3. [if-statements in Synths](#audio-control-structures:-do-not-use-.if-etc.-in-synths!) (strongly discouraged).
4. [#Syntax of conditional expressions](#syntax-of-conditional-expressions),


For other control structures, see [loop](../Reference/loop.md) and [Exception](../Classes/Exception.md).





## Overview of Basic Conditional Expressions

> **Note:** Reminder: `falseFunc == { falseFuncBody }`. For instance, when `falseFunc == { "aaa" }`,  then `falseFuncBody == "aaa".`


 


### if
The `.if` method is called on a receiver `expr` which must return a [Boolean](../Classes/Boolean.md) value. (In other words, `if` is a method of Boolean.)

In addition the method call takes two arguments:  a [Function](../Classes/Function.md) `trueFunc` to execute (call .value on) if the expression is true,  and another optional Function `falseFunc` to execute (call .value on) if `expr` is false. 

The `.if` method returns the value of the function which is executed (i.e., `trueFunc.value` if receiver is `true`,  `falseFunc.value` if receiver is `false`).

If `falseFunc` is not present and `expr` is false, then the `.if` method returns `nil`.


#### Syntax

```supercollider
// function call notation
if(expr, trueFunc, falseFunc);
if(0 < 3, {"aha"} {"brb"}); 

// function call notation with trailing argument block
// looks almost like C (without the "else").
if(expr) { trueFuncBody } { falseFuncBody };
if(0 < 3) {"aha"} {"brb"}; 

// not recommended: receiver notation, 
// reflects the fact that .if is a method like any other;
// but is hard to read and rarely used in practice 
expr.if(trueFunc, falseFunc);
```





#### Examples

```supercollider
// function call notation with trailing argument block
// note the indentation and linebreaks,
// which are recommended, but not mandatory.
(
if([false, true].choose) {
    "expr was true".postln  // trueFuncBody
} {
    "expr was false".postln  // falseFuncBody
};
)

// assignment of value according to condition
(
var a = 1, z;
z = if(a < 5) { 100 } { 200 };
z.postln;
)

// same as
(
var a = 1, z;
if(a < 5) { z = 100 } { z = 200 };
z.postln;
)

// no falseFunc, expr is true
(
var x = 1;
if(x > 0) { 90 + x }; // returns { 90 + x }.value
) // -> 91

// no falseFunc, expr is false
(
var x = 1;
if(x < 0) { 90 + x}; 
) // -> nil
```







### case
Function also implements a `case` method which allows for conditional evaluation with multiple cases.  The receiver here but can be thought of as simply the zeroth argument, representing the first of multiple "cases". Thus, the arguments including the receiver can be written as pairs of `testFunc`s and corresponding `trueFunc`s.  if a `testFunc` returns true, its corresponding `trueFunc` is evaluated and its `.value` returned. If no `testFunc` returns true, either `nil` is returned, or the `.value` of a `defaultFunc` supplied as the final argument. Case is inlined (under the conditions outlined [below](#optimization-through-inline-expansion)), and is therefore just as efficient as nested if statements.


#### Syntax

```supercollider
// { testFuncBody1 } is technically the receiver.
// trailing receiver and argument block notation
// (possible because receiver and all arguments are Functions):
case
    { testFuncBody1 } { trueFuncBody1 }
    { testFuncBody2 } { trueFuncBody2 }
    ...
    { testFuncBodyN } { trueFuncBodyN }
    { defaultFuncBody }; // defaultFunc can be omitted.

// function call notation:
case(   
        testFunc1, trueFunc1,
        testFunc2, trueFunc2,
        ...,
        testFuncN, trueFuncN,
        defaultFunc // defaultFunc can be omitted.
    ); 
// in some cases the function call notation will appear to work even if 
// arguments are not Function objects, as long as they respond to .value;
// however, no inlining will take place then.
```





#### Example

```supercollider
(
var i, x;
i = [0, 7, 2, 329, 4, 5000].choose;
x = case
    { i == 0 }     { \no }   
    { i == 7 }     { \wrong }
    { i == 2 }     { \worng }
    { i == 329 }   { \wrnog }
    { i == 4 }     { \wnorg }
    { i == 5000 }  { \true };
x.postln;
)
```


or


```supercollider
(
case(
    {[true,false].choose}, {"first test was true"},
    {[true,false].choose}, {"second test was true"},
    {[true,false].choose}, {"third test was true"},
    { "no test was true" }
);
)
```







### switch
Object implements a switch method which allows for conditional evaluation with multiple cases.  Each case is represented by a pair of two arguments: a `testValue` followed by a `trueFunc`. In distinction to [#case](#case), the receiver is *not* the first test function, but rather an object that other `testValues` are all compared to.  The receiver is compared against the `testValue`s, and if the comparison returns true, the corresponding `trueFunc` will be evaluated and its value returned. If it is false, the next `testValue` is compared, and so on.  The return value of `switch` in case of *no* matching `testValue` is dependent on whether the number of arguments passed to it is even or odd.  If the number of arguments is even, `switch` will return `nil` in such cases, whereas if it is odd, the last argument should be a `defaultFunction` whose `.value` will be returned.

The **comparison function** used is equality, i.e., `==`,  unless the switch statement is inlined (see also [below](#optimization-through-inline-expansion)),  in which case switch compares by identity, i.e., `===`. (See [EqualityIdentity](../Guides/EqualityIdentity.md))

The switch statement will automatically be inlined if two conditions are met: 

**First**, the test objects are all values with unique representations (Floats, Integers, Symbols, Chars, nil, false, true) and  **second**, functions used in the switch statement have no variable or argument declarations.  The inlined switch uses a hash lookup (which is faster than nested if statements), so it should be very fast and scale to any number of clauses. 


> **Note:** **Avoid using String or Float as test objects for switch.**  The former is simply less efficient than Symbol, as it will not inline;  the latter will inline, but may yield unexpected results due to floating-pointing representation, e.g., `(2/3) == (1 - (1/3))` returns `false`.



#### Syntax

```supercollider
// function call syntax with trailing argument blocks
// linebreaks are optional but recommended
switch(value)
    { testValue1 } { trueFuncBody1 }
    { testValue2 } { trueFuncBody2 }
    { testValue3 } { trueFuncBody3 }
    ...
    { testValueN } { trueFunchBodyN }
    { defaultBody }; // defaultbody can be omitted.

//function call syntax without trailing arguments 
switch(value,
    testValue1, trueFunc1,
    testValue2, trueFunc2,
    ...
    testValueN, trueFuncN,
    defaultFunc // defaultFunc can be omitted
);
```





#### Examples

```supercollider
//function call syntax without trailing arguments 
(
var x = 0; //also try 1
switch(x, 
    0, { "hello" }, 
    1, { "goodbye" }
    )
)


// function call syntax with trailing argument blocks
(
var x = 0; //also try 1
switch(x) 
    { 0 } { "hello" } 
    { 1 } { "goodbye" };
)

(
var x, z;
z = [0, 7, 2, 329, 4, 5000].choose;
switch (z.postln,
    7,    { \no },
    2,    { \wrong },
    329,  { \worng },
    4,    { \wrnog },
    5000, { \wnorg },
    0,    { \true }
).postln;
)
```


or:


```supercollider
(
var x, z;
z = [0, 7, 2, 329, 4, 5000].choose;
x = switch(z)
    {7}    { \no }
    {2}    { \wrong }
    {329}  { \worng }
    {4}    { \wrnog }
    {5000} { \wnorg }
    {0}    { \true };
x.postln;
)
```





#### Inlined vs non-inlined comparison
The following code will inline, but will compare by identity:


```supercollider
(
switch(1)
    { 1.0 } { "yes" }
    { "no" }
) // -> no
```


The identity comparison `1 === 1.0` returns false.  While 1.0 and 1 represent the same numeric value, one is a Float and the other is an Integer, so they cannot be identical. On the other hand, if we prevent inlining by declaring a variable within one of the functions, the code will compare by equality: `1 == 1.0` returns true. 


```supercollider
(
// 'var x' prevents inlining
switch(1)
    { 1.0 } { var x; "yes" }
    { "no" }
)  // -> yes
```







### while
The `while` method implements conditional execution of a loop;  it is a method of [Function](../Classes/Function.md). If the `testFunc` answers true when evaluated,  then the `loopFunc` is evaluated and the process is repeated.  Once the `testFunc` returns false, the loop terminates.

Note the distinction to `if`:  `testFunc` is a Function (which returns itself), e.g., `{x < 0}`,  whereas `expr` above was an expression, e.g., `x < 0`, which returned a Boolean.


#### Syntax

```supercollider
// function call with receiver and argument as trailing function block
// this is _different_ from C!
while { testFuncBody } { loopFuncBody };
// abbreviation of:
while ({testFuncBody}) { loopFuncBody };
// but the following (C syntax) will not work in SuperCollider:
while (testFuncBody) { loopFuncBody } ; // Syntax Error

// function call without trailing argument.
while({ testFuncBody }, { loopFuncBody });

// receiver notation 
// hard to read and rarely used in practice 
{ testFuncBody }.while({ loopFuncBody });
```





#### Example

```supercollider
(
i = 0;
while { i < 5 } { i = i + 1; "boing".postln };
)
```


`while` expressions are also optimized by the compiler if they do not contain variable declarations in the `testFunc` and the `loopFunc`.







## Other Control Structures
Conditional expressions are a type of control structures; another useful type are iterations such as `.do` and `.for`.  These are discussed separately in the page on [iteration](../Reference/loop.md) (also see [Collection / Iteration ](../Classes/Collection.md#iteration)). Finally, the methods [Function#-try](../Classes/Function.md#-try) and [Function#-protect](../Classes/Function.md#-protect) are technically conditional expressions,  but their intended use is in the handling of exceptions, which is why their are discussed in [Exception](../Classes/Exception.md) rather than here.



## Optimization through inline expansion
`if`, `while`, `switch`, and `case` expressions are optimized (i.e., inlined) by the compiler if they do not contain variable declarations in the functions.  We can see this if we dump the bytecodes of the receiver function definition.  (Bytecodes are a lower-level representation of the code sent to the interpreter.)  The optimization does not use function calls within the bytecodes and instead uses a jump statement, which is faster.


### Failure to inline: Functions include variable declaration.

```supercollider
(
{
    if(6 == 9) {
        var notHere; // variable declaration 
        "hello".postln;
    } {
        "world".postln;
    }
}.def.dumpByteCodes
)
```


This returns the following warning,> *You can switch on and off the above warning (see: [LanguageConfig#*postInlineWarnings](../Classes/LanguageConfig.md#*postinlinewarnings)):
```supercollider
LanguageConfig.postInlineWarnings_(true) // warn
LanguageConfig.postInlineWarnings_(false) // ignore it.
```

*and below it we can see what the bytecodes look like without inlining:


That is, entries 5 and 7 are proper function calls, which are costly (i.e., slow/inefficient).




### Successful inlining: Functions do not include variable declarations.
Here is the opposite example, where inlining has taken place:


```supercollider
(
{
    if(6 == 9) {
        "hello".postln;
    } {
        "world".postln;
    }
}.def.dumpByteCodes
)
```


The bytecodes read as follows:


Entries 5 and 12 are jump statements, instructing to jump to entries 15 and 19 respectively.  In between those lines, we can recognize the contents of the two Functions,  but they are now no longer implemented as function calls, but as direct instructions, which saves resources.





## Audio Control Structures: Do not use .if etc. in Synths!
The control structures discussed here is intended for use in sclang (i.e., language/client), not in scsynth (i.e., server).  Use of .if in signal processing contexts may appear to work in simple cases but is **not advised**.  Intead, use [Select](../Classes/Select.md) or [SelectX](../Classes/SelectX.md) and related classes. Also see [UserFAQ / SynthDef Issues ](../Guides/UserFAQ.md#synthdef-issues) for more details.

The following code runs (does not produce an error), but is **not good usage**, because it is not very obvious what is going on: 


```supercollider
(
    var freq = 100;
    {
        if(LFTri.kr(0.1).unipolar, //receiver is a UGen. 
            SinOsc.ar(freq), //as are arguments
            Saw.ar(freq)
        ) * 0.2;
    }.scope(bufsize: s.sampleRate/freq; //bufsize to match the period of the oscillators
)
```


Here, the receiver LFTri is a UGen.  The UGen class in turn implements an [UGen#-if](../Classes/UGen.md#-if) method by translating it into a linear crossfade using binary operators:


```supercollider
    if { arg trueUGen, falseUGen;
        ^(this * (trueUGen - falseUGen)) + falseUGen;
    }
```


The regular [Boolean#-if](../Classes/Boolean.md#-if) discussed above does *not* crossfade.  Hence, if the crossfade is desired, it is better practice to make this explicit by using [LinSelectX](../Classes/LinSelectX.md): 


```supercollider
(
    var freq = 100;
    {
        LinSelectX.ar(
            LFTri.kr(0.1).unipolar, 
            [SinOsc.ar(freq), Saw.ar(freq)]
        ) * 0.2;
    }.scope(bufsize: s.sampleRate/freq); 
)
```


On the other hand, in the case where not a crossfade but a simple either/or analogous to language-side `Boolean.if` is desired, [Select](../Classes/Select.md) is preferable:


```supercollider
(
    var freq = 100;
    { Select.ar(
        LFPulse.ar(1), 
        [SinOsc.ar(freq), Saw.ar(freq)]
        ) * 0.2;
    }.scope(bufsize: s.sampleRate/freq);
)
```


 



## Syntax of conditional expressions
In SuperCollider, control structures implemented as **methods to be called on a receiver and which return a value**. This is distinct from many other languages where, e.g., `if` is a reserved identifier (keyword) independent of a particular receiver, and does not return a value.  For instance, in C or in python, you cannot create a variable called `if`, whereas in SuperCollider, you can (which does not mean that you should...). In SuperCollider, it is also possible to implement an `.if` method for a particular class that does something rather different (see [below](#audio-control-structures:-do-not-use-.if-etc.-in-synths!)); despite these differences, SuperCollider's flexible syntax can make it *look* as if `if` were just such a reserved identifier,  whereas it is in fact a method of [Boolean](../Classes/Boolean.md).

Thus, SuperCollider's [flexibility with respect to syntax](../Reference/Syntax-Shortcuts.md) is a potentially confusing factor when it comes to conditional expressions.  For instance, there are four equivalent ways to write a simple if-expression:

|  | Receiver notation | Function call notation | 
| --- | --- | --- || Regular argument notation | `condition.if(trueFunc, falseFunc)` | `if(condition, trueFunc, falseFunc)` | | Argument(s) as trailing blocks | `condition.if { trueFuncBody } { falseFuncBody }` | `if(condition) { trueFuncBody } { falseFuncBody }` | 
While the receiver notation reflects the implementation in SuperCollider most closely, it is hard to read and rarely used in practice.  The two function call notations are the most commonly used.  The version with trailing argument blocks superficially resembles conditional syntax familiar from C or javascript:



```supercollider
//if-statement in SuperCollider, function call notation with trailing argument block 
if (condition) { 
    trueFuncBody
} {  //no "else" in SuperCollider!
    falseFuncBody
}
```



### Trailing argument blocks
The above C-like syntax is enabled in SuperCollider by a syntactic mechanism called "trailing argument blocks".  A **block** is any expression enclosed in curly brackets, e.g. `{ trueFuncBody }`.  The syntax `receiver.method { expr1 } { expr2 }` is equivalent to `receiver.method({ expr1 }, { expr2 })`.  That is, the round brackets and comma are omitted.  This can be combined with the function call syntax such that we can write `method(receiver) { expr1 } { expr2 }`;  this in turn gives the above form of the if-statement in function call notation with trailing argument block. 

However, even if the curly brackets now indicate where one argument ends and where the next one starts,  they also retain their usual role of showing that the enclosed expression should serve as the definition of a [Function](../Classes/Function.md) instance. 

This means, **first**, that the use of trailing argument syntax implies that `expr1` and `expr2` *define* Functions; **second**, that `expr1` and `expr2` should not already *be* Functions in their own right (unless you intend them to be). 

In examples:


```supercollider
::

subsubsection:: Receiver blocks (.case, .while)

If the receiver is itself an expression surrounded by curly brackets, a special version of the trailing argument block syntax can be used:
Here, not only the arguments can be written as trailing {}-enclosed blocks, but also the receiver itself.
For instance, code::{ funcBody }.fork:: is often written as code::fork { funcBody }::.

When the method takes arguments, these arguments must also be written as {}-enclosed blocks, and follow the receiver:

code:: method { receiverFuncBody } { arg1FuncBody }  { arg2FuncBody }::

Among the conditional expressions discussed here, this applies to .while and .case (because they are methods of link::Classes/Function::.)

Example:
code::
//function call notation with receiver block and trailing argument block
while { testFuncBody } { loopFuncBody }; 
// abbreviation of  function call notation with trailing argument block
while ({ testFuncBody }) { loopFuncBody };
// in receiver notation
{ testFuncBody }.while({ loopFuncBody })
// distinct from C-style while, which will not work in SuperCollider:
while (testFuncBody) { loopFuncBody }; // -> Syntax Error
```



#### Return values (.if, .case, .switch)
Unlike other common programming languages, conditional expressions (`.if`, `.case`, and `.switch`) in SuperCollider have return values by default; these in turn can be assigned to variables.  For instance, in python, the following will produce an error:


  and for conditional assignment, one has to write


Whereas in SuperCollider, both analogous cases work:


```supercollider
(
var a = "oink"
a = if([true,false].choose, {"gobbledeegook"});
a.postln;
)

( 
var a = "oink";
    if([true,false].choose, {a = "gobbledeegook"});
a.postln;
)
```


However, this does not change the syntactic requirement that the assignment statement, when it is an argument to a conditional expression, must be a Function. In other words, the following is wrong:


```supercollider
 ( 
var a = "oink";
    if([true,false].choose, a = "gobbledeegook"); //syntax error
a.postln;
)
```


This is because a Function is expected after the comma in `if(expr, arg)`.







