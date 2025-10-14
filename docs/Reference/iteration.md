# Iteration

*for, do, loop, repeat*

**Categories:** Core, Common methods

**Related:** [Object](../Classes/Object.md), [Function](../Classes/Function.md), [Routine](../Classes/Routine.md), [Stream](../Classes/Stream.md), [Pattern](../Classes/Pattern.md)

(This page combines material formerly in the Control Structures and loop/repeat helpfiles.)
There are a number of ways to implement iteration in SuperCollider. The most familiar ones will be the [Number#-for](../Classes/Number.md#-for) and [Collection#-do](../Classes/Collection.md#-do) methods. The [Function#-while](../Classes/Function.md#-while) method is discussed [here](../Reference/Conditional-Execution.md#while).
For Routines (Streams) and Patterns, special methods exist: [.repeat and .loop](#patterns-and-routines:-repeat-and-loop)
| **Thing you want to do** | **method to use** | **returns** | 
| --- | --- | --- || iterate over a numeric range | [#for](#for), [#forBy](#forby) | `loopFunc.value(n)` for each number `n` in range | | iterate over integers from $0$ to $n-1$ | [n.do](#do) | `loopFunc.value(i)` for each integer `i` between $0$ and $n-1$ inclusive. | | iterate over a collection | [collection.do](#do) | `loopFunc.value(x)` for each element `x` of collection | | iterate while some condition is true | [Conditional-Execution#while](../Reference/Conditional-Execution.md#while) | `loopFunc.value` for each iteration. | | embed in a stream n times | [#.repeat](#.repeat)(n) (with argument) | [Routine](../Classes/Routine.md) or [Pn](../Classes/Pn.md) | | embed in a stream an infinite number of times | [.loop](#apart-from-function.loop,-the-.loop-method-is-an-alias-for-.repeat(inf)) | a [Routine](../Classes/Routine.md) or [Pn](../Classes/Pn.md) | | [break from a loop](#breaking-from-a-loop) | [Function#-block](../Classes/Function.md#-block) | `nil` unless specified; see [below](#breaking-from-a-loop) | 
## for, forBy, do

### for
The for message implements iteration over an integer series from a starting value to an end value stepping by one each time. A function is evaluated each iteration and is passed the iterated numeric value as an argument.

Syntax


```supercollider
for(startValue, endValue) { loopFuncBody }

// alternate
for(startValue, endValue, loopFunc)

Example
code::
for(3, 7) { arg i; i.postln };  // prints values 3 through 7
```





### forBy
The forBy selector implements iteration over an integer series with a variable step size. A function is evaluated each iteration and is passed the iterated numeric value as an argument.

Syntax


```supercollider
forBy(startValue, endValue, stepValue) { loopFuncBody };

forBy(startValue, endValue, stepValue, loopFunc);
```


Example


```supercollider
forBy(0, 8, 2) { arg i; i.postln };  // prints values 0 through 8 by 2's
```





### do
Do is used to iterate over a [Collection](../Classes/Collection.md). Positive Integers also respond to `do` by iterating from zero up to their value (excluding that value). Collections iterate, calling the function for each object they contain. Other kinds of Objects respond to do by passing themselves to the function one time. The function is called with two arguments, the item, and an iteration counter.

Syntax


```supercollider
collection.do { loopFuncBody };

// alternate
collection.do(loopFunc)

// alternates, rarely seen
do(collection, loopFunc)
do(collection) { loopFuncBody };
```


Example


```supercollider
[ 1, 2, "abc", (3@4) ].do { arg item, i; [i, item].postln; };

5.do { arg item; item.postln }; // iterates from zero to four

"you".do { arg item; item.postln }; // a String is a collection of characters

'they'.do { arg item; item.postln }; // a Symbol is a singular item

(8..20).do { arg item; item.postln }; // iterates from eight to twenty

(8,10..20).do { arg item; item.postln }; // iterates from eight to twenty, with stepsize two

Routine {
    var i = 10;
    while { i > 0 } {
        i.yield;
        i = i - 5.0.rand
    }
}.do { arg item; item.postln };  // 'do' applies to the Routine
```



> **Note:** The syntax `(8..20).do` uses an optimization to avoid generating an array that is used only for iteration (but which would be discarded thereafter). The return value of `(8..20).do { |item| item.postln }` is 8, the starting value.However, if `do` is written as an infix binary operator, as in `(8..20) do: { |item| item.postln }`, then it will generate the series as an array first, before calling Array:do. One side effect of this is that it is valid to `do` over an infinite series within a routine only if `do` is written as a method call. If it is written as a binary operator, you will get a "wrong type" error because the array must be finite.
```supercollider
// OK: 'do' is a method call
r = Routine {
    (8 .. ).do { |i|
        i.yield;
    };
};

r.next;
-> 8
-> 9 etc.

// ERROR: 'do' is an operator
r = Routine {
    (8 .. ) do: { |i|
        i.yield;
    };
};

r.next;

ERROR: Primitive '_SimpleNumberSeries' failed.
Wrong type.
```






## Breaking from a loop
To break from a loop, use the [Function#-block](../Classes/Function.md#-block) method.

The syntax is somewhat unusual. Consider the following loop:


```supercollider
100.do { |i| i.postln; }
```


Suppose we want the loop to stop after `i == 7`. Other languages (e.g. javascript or python) would allow us to write expressions analogous to the following:


```supercollider
// this won't work in SC
100.do { |i| if(i == 7) {break}; i.postln; } // syntax error;
```


However, there is no break keyword in sclang; instead, we have to do three things (not in order, but simultaneously):

1. enclose the looping expression (`100.do { ... }` here) in another Function block that takes an argument (which we call `break` here, but which can be called anything);
```supercollider
{ |break|   
    100.do { |i|  // the original expression
    i.postln;     // from which we 
    }             // want to break.
}
```


2. inside the looped Function, call `.value` on that argument when the relevant condition is true;
```supercollider
{ |break|  
    100.do { |i| 
    i.postln; 
    if (i == 7) {   // added lines
        break.value // ...
        }           // ...
    } 
}
```


3. on the enclosing Function, call `.block.`
```supercollider
block { |break| // block goes at the beginning of this line
        100.do { |i| 
                i.postln; 
                if (i == 7) {
                    break.value
                    } 
        } 
} 
// this is the complete expression, at last
```




This will return nil once the break condition is reached, but if a specific return value is desired, this can be provided to the `.value` call:


```supercollider
block { |break| 
        100.do { |i| 
                i.postln; 
                if (i == 7) {
                    break.value("return this")
                    } 
        } 
} 
//phew
```




## There is no continue keyword in SuperCollider
Some languages permit "skipping" individual iterations of a loop by means of a "continue" keyword. For instance, in python, the following will print `0,1,2,  4,5,6,7,8,9`, skipping over the `3`:


Note that the remainder of the body of the loop, `print(i)`, is fully skipped over when the continue keyword is reached. For the same result in sclang, the body of the loop must be moved *inside* the conditional statement:


```supercollider
10.do { |i|
    if (i == 3) {
        //no code here.
    } {
        i.postln; // the equivalent to print(i) above
    }
}
// the above code is awkward, it merely serves an explanatory purpose.
// more elegant in pratice is to negate the continue condition:
10.do { |i|
    if (i != 3) {
        i.postln;
    }
}
```




## Patterns and Routines: repeat and loop
The method `.repeat(n)` can be used to create a Routine or a Pattern which repeats values for a specific number of times. To repeat indefinitely, use either `.loop`, or use `.repeat` without supplying an argument.

Roughly, if `pat` is some Pattern, then `pat.repeat(n)` will return `Pn(pat, n)`. For most other classes, `object.repeat(n)` will return a Routine equivalent to `Pn(object, n).asStream`.

Regarding `Function.loop`, which should only be used **inside** a Routine,  see [below](#apart-from-function.loop,-the-.loop-method-is-an-alias-for-.repeat(inf)).


### .repeat

**[Object#-repeat](../Classes/Object.md#-repeat)(n)**
: Returns a Routine. Embeds the receiver n times by wrapping it in a [Pn](../Classes/Pn.md) and calling [Pattern#-.asStream](../Classes/Pattern.md#-.asstream) on it.  If no argument is provided, the stream will repeat indefinitely. Implementation:  `repeat { arg n = inf; ^Pn(this, n).asStream }` Example:
```supercollider
    x = [0,1,2]; // an Array
    y = x.repeat(4); // a Routine that repeats the array 4 times
    y.nextN(15); // -> [[0,1,2],[0,1,2],[0,1,2],[0,1,2],nil,nil,nil,nil,nil,nil,nil]
```

**[Pattern#-repeat](../Classes/Pattern.md#-repeat)(n)**
: Returns a [Pn](../Classes/Pn.md). Embeds the receiver n times by wrapping it in a [Pn](../Classes/Pn.md), but doesn't call `.asStream` on it.  [pattern.repeat(n)](../Classes/Pattern.md#-repeat) is thus effectively a synonym for [Pn(pattern, n)](../Classes/Pn.md).  If no argument is provided, the Pattern will repeat indefinitely.Example:
```supercollider
    // x is a pattern that counts from 0 to 2
    x = Pseq([0,1,2]); // -> a Pseq
    // y is a pattern that does this 4 times in a row
    y = x.repeat(4); // -> a Pn
    y.asStream.nextN(15); // -> [0,1,2,0,1,2,0,1,2,0,1,2,nil,nil,nil]
```

**[Routine#-repeat](../Classes/Routine.md#-repeat)(n)**
: Embeds the receiver in another Routine that repeats it n times, and returns that.  For instance:
```supercollider
    // x is a a Routine that counts from 0 to 2
    x = Routine({ 3.do({ arg i; i.yield }) }); // -> a Routine
    // y is a Routine that does x four times
    y = x.repeat(4); // -> a Routine
    y.nextN(15); // -> [0,1,2,0,1,2,0,1,2,0,1,2,nil,nil,nil]
```






### Apart from Function.loop, the .loop method is an alias for .repeat(inf)
`.loop` is simply an alias for `.repeat(inf)`. An important exception to this is [Function#-.loop](../Classes/Function.md#-.loop), which should be treated with care:


**[Function#-loop](../Classes/Function.md#-loop)**
: Used on a function *inside* a [Routine](../Classes/Routine.md),  it will result in a Routine that repeats the receiver function an infinite number of times.  Used on a Function *outside* a Routine, it will crash the interpreter. Example:
```supercollider
    f = { 3.yield; }; // -> a Function
    x = Routine({ f.loop }); // -> a Routine
    10.do({ x.next.postln }); // -> [3,3,3,3,3,3,3,3,3,3]
    // Similar outcome:
    x = Routine(f).loop; // -> a Routine
    10.do({ x.next.postln }); // -> [3,3,3,3,3,3,3,3,3,3]
```









