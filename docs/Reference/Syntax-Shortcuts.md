# Syntax Shortcuts

*syntactic sugar*

**Categories:** Language

**Related:** [Overviews/SymbolicNotations](../Overviews/SymbolicNotations.md)


## Introduction
This file shows a number of syntax equivalences in the compiler.

Because of the multiple syntax equivalences, some expressions can be written in many different ways. All of the following do the same thing and compile to the same code.


```
// new argument syntax

(1..10).collect({ |n| n.squared });  // receiver syntax
collect((1..10), { |n| n.squared }); // function call syntax
(1..10).collect { |n| n.squared };   // receiver syntax with trailing-block argument
collect ((1..10)) { |n| n.squared }; // function call syntax with trailing-block argument
(1..10) collect: { |n| n.squared };  // binary operator syntax


// old argument syntax

(1..10).collect({ arg n; n.squared });  // receiver syntax
collect((1..10), { arg n; n.squared }); // function call syntax
(1..10).collect { arg n; n.squared };   // receiver syntax with trailing-block argument
collect ((1..10)) { arg n; n.squared }; // function call syntax with trailing-block argument
(1..10) collect: { arg n; n.squared };  // binary operator syntax


// partial application syntax

(1..10).collect(_.squared);   // receiver syntax
collect((1..10), _.squared);  // function call syntax
(1..10) collect: _.squared;   // binary operator syntax
```


You could even start expanding out the equivalent of (1..10) which is really a shortcut for `series(1, nil, 10)`. This could also be written `1.series(nil,10)`. This adds another 26 variations to the 13 variations above.



## Defining functions and classes

### shorter argument lists in definitions
| instead of writing: | you can write: | 
| --- | --- || `{ arg x; x < 2 }` | `{ |x| x < 2 }` | | `{ arg x = 123; x < 2 }` | `{ |x = 123| x < 2 }` | | `{ arg x = 10.rand; x < 2 }` | `{ |x = (10.rand)| x < 2 }` or `{|x(10.rand)| x < 2 }` | 



> **Note:** When using the new `||` syntax, the default value needs to be enclosed in parenthesis if it's not a literal.





### partial application
| instead of writing: | you can write: | 
| --- | --- || `{ |x| object.msg(a, x, b) }` | `object.msg(a, _, b)` | | `{ |x,y| object.msg(a, x, y) }` | `object.msg(a, _, _)` | | `{ |x| a + x }` | `a + _` | | `{ |x| [a, b, x] }` | `[a, b, _]` | | `{ |x| (a: x) }` | `(a: _)` | 



> **Note:** There are some limitations to the extent of the surrounding expression that `_` can capture. See [Partial-Application](../Reference/Partial-Application.md) for details.





### defining instance variable accessor methods
| instead of writing: | you can write: | 
| --- | --- ||  |  | 




## Sending messages, calling functions, and instantiating objects

### function-call and receiver notations
| instead of writing: | you can write: | 
| --- | --- || `f(x, y)` | `x.f(y)` | | `f(g(x))` | `x.g.f` | 



### calling the 'value' method
| instead of writing: | you can write: | 
| --- | --- || `f.value(x)` | `f.(x)` | 



### instantiate object
| instead of writing: | you can write: | 
| --- | --- || `Point.new(3, 4)` | `Point(3, 4)` | 



### calling an instance variable setter method
| instead of writing: | you can write: | 
| --- | --- || `p.x_(y)` | `p.x = y` or `x(p) = y` | 



### calling performList
| instead of writing: | you can write: | 
| --- | --- || `object.performList(\method, a, b, array)` | `object.method(a, b, *array)` | 



### moving blocks out of argument lists (trailing-block arguments)
| instead of writing: | you can write: | 
| --- | --- || `if (x < 3, { \abc }, { \def })` | `if (x < 3) { \abc } { \def }` | | `z.do({ |x| x.play })` | `z.do { |x| x.play }` | | `while({ a < b }, { a = a * 2 })` | `while { a < b } { a = a * 2 }` | | `Pfunc({ rrand(3, 6) })` | `Pfunc { rrand(3, 6) }` | 

> **Note:** Trailing arguments must be literal blocks. No other expression may be used as a trailing argument, even if it evaluates to a Function. For example, you cannot use a variable name as a trailing argument, even if this variable was assigned a Function.Using a selector as an infix binary operator (discussed in the next section) enables a visually similar construct that does allow arbitrary expressions as operands, but these binary-operator constructs technically do not have trailing arguments.
```
(
var f = { |n| (2**n) + (3**n) };
collect((1..5), f); // valid
(1..5).collect(f);  // valid
(1..5) collect: f;  // valid (selector as binary operator)
)
(1..5).collect f;   // syntax error (non-block as a trailing argument)
collect((1..5)) f;  // syntax error (ibid.)
```

A fairly common case when this syntactic restriction matters: a partial application using the `_` syntax is an expression evaluating to a Function, but it is not a literal block. Therefore:
```
do(6) _.postln  // syntax error
6.do _.postln   // syntax error
do(6, _.postln) // valid
6.do(_.postln)  // valid
6 do: _.postln  // valid
```





### use a selector (method name) as a binary operator
| instead of writing: | you can write: | 
| --- | --- || `div(x, y)` | `x div: y` | 
> **⚠️ Warning:** When switching between various forms of call syntax, one has to be mindful that a selector as a binary operator has equal precedence with most other binary operators, but has lower precedence than the receiver dot notation (`.`). Therefore, replacing a receiver syntax (dot) with a selector written as a binary operator can change the result of some expressions, as illustrated below:
```
4 + 5.div(2) // -> 6
4 + 5 div: 2 // -> 4

// This is a left-to-right application of two dots,
// the first of which has a trailing block argument.
(1..3).collect { |x| x + 1 }.bubble
// -> [ [ 2, 3, 4 ] ]

// This is a selector binary operator ("collect:") applied
// to two arguments, the second of which is the result
// of applying "bubble" (via dot syntax) to a function.
(1..3) collect: { |x| x + 1 }.bubble
// -> [ [ a Function ], [ a Function ], [ a Function ] ]

// Changing precedence in the above with explicit parentheses
((1..3) collect: { |x| x + 1 }).bubble
// -> [ [ 2, 3, 4 ] ]

// Or by uniform use of selectors as binary operators
(1..3) collect: { |x| x + 1 } bubble: 0
```
Native infix operators like `+` can also be written in (longer) function-call form, e.g.:

| infix: | function call: | 
| --- | --- || `1 + 2` | `(+)(1, 2)` | 
The latter form is usually not a shortcut, except when one wants to dynamically change the adverb of an operator, for instance that of `+++`, because adverbs in the infix notation are interpreted as literals.


```
(
var a = (_+_) ! [3, 3]; // -> [ [ 0, 1, 2 ], [ 1, 2, 3 ], [ 2, 3, 4 ] ]
(0..2) collect: (+++)(a, 99, _) flatten: 3; // iterated adverb
)
(0..2) collect: (a +++._ 99) flatten: 3;    // syntax error
(
var a = (_+_) ! [3, 3];
(0..2) collect: {|v| a +++.v 99} flatten: 3 // the literal adverb \v is used
)
```






## Collections

### create a collection
| instead of writing: | you can write: | 
| --- | --- || `Set.new.add(3).add(4).add(5)` | `Set[3, 4, 5]` | | `Array[3, 4, 5]` | `[3, 4, 5]` | 



### indexing elements
| instead of writing: | you can write: | 
| --- | --- || `z.at(i)` | `z[i]` | | `z.put(i, y)` | `z[i] = y` | 



### accessing subranges of Arrays
| instead of writing: | you can write: | 
| --- | --- || `a.copyRange(4, 8)` | `a[4..8]` | | `a.copyToEnd(4)` | `a[4..]` | | `a.copyFromStart(4)` | `a[..4]` | 



### creating arithmetic series
| instead of writing: | you can write: | 
| --- | --- || `Array.series(16, 1, 1)` or `series(1, nil, 16)` | `(1..16)` | | `Array.series(6, 1, 2)` or `series(1, 3, 11)` | `(1, 3..11)` | 
There is also the similar syntax for creating an iterating [Routine](../Classes/Routine.md):

| instead of writing: | you can write: | 
| --- | --- || `seriesIter(1, 3, 11)` | `(:1, 3..11)` | 



> **Note:** SuperCollider also supports [ListComprehensions](../Guides/ListComprehensions.md).


As a simple (non-combinatorial) example, the following are equivalent ways of listing the first 10 primes:


```
(:1..) select: _.isPrime nextN: 10;
{: x, x <- (1..), x.isPrime }.nextN(10);
```





### creating Events
| instead of writing: | you can write: | 
| --- | --- || `Event[\a -> 1, \b -> 2]` | `(a: 1, b: 2)` | 



### creating Arrays with key-value pairs
| instead of writing: | you can write: | 
| --- | --- || `[\a, 1, \b, 2]` | `[a: 1, b: 2]` | 




## Other shortcuts

### multiple assignment
| instead of writing: | you can write: | 
| --- | --- || `x = z.at(0); y = z.at(1);` | `# x, y = z;` | 



### accessing environment variables
| instead of writing: | you can write: | 
| --- | --- || `'myName'.envirGet` | `~myName` | | `'myName'.envirPut(9)` | `~myName = 9` | 



### shorthand for Symbols
| instead of writing: | you can write: | 
| --- | --- || `'mySymbol'` | `\mySymbol` | 



> **Note:** The shorthand only admits a subset of the symbols that may be enclosed in single quotes. See [Literals#Symbols](../Reference/Literals.md#symbols) for details.





### creating a Ref
| instead of writing: | you can write: | 
| --- | --- || `Ref.new(thing)` | ``thing` | 






