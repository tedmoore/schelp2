# Symbolic Notations

*Catalog of symbolic notations in SuperCollider*

**Categories:** Language

**Related:** [Overviews/Operators](../Overviews/Operators.md), [Syntax-Shortcuts](../Reference/Syntax-Shortcuts.md)


## Arithmetic operators
Math operators apply to many classes, including arrays and other collections.

Using a basic math operator on a Symbol swallows the operation (returns the symbol)


```supercollider
\symbol * 5
symbol
```



**`number + number`**
: addition

**`number - number`**
: subtraction

**`number * number`**
: multiplication

**`number / number`**
: division

**`number % number`**
: modulo

**`number ** number`**
: exponentiation





## Bitwise arithmetic

**`number & number`**
: bitwise and

**`number | number`**
: bitwise or

**`number << number`**
: bitwise left shift

**`number >> number`**
: bitwise right shift

**`number +>> number`**
: unsigned bitwise right shift





## Logical operators

**`object == object`**
: equivalence

**`object === object`**
: identity

**`object != object`**
: not equal to

**`object !== object`**
: not identical to



Objects may be equivalent but not identical.


```supercollider
[1, 2, 3] == [1, 2, 3]
true
[1, 2, 3] === [1, 2, 3]
false       // a and b are two different array instances with the same contents

a = b = [1, 2, 3];
a === b;
true        // a and b are the same array instance
```



**`number < number`**
: comparison (less than)

**`number <= number`**
: comparison (less than or equal to)

**`number > number`**
: comparison (greater than)

**`number >= number`**
: comparison (greater than or equal to)






**`boolean && boolean`**
: logical And

**`boolean || boolean`**
: logical Or



When a function is the second operand, these operators perform short-circuiting (i.e., the function is executed only when its result would influence the result of the operation). This is recommended for speed.

With `and:` and `or:` second-argument functions will be inlined. If you use `&&` or `||`, no inlining will be done and performance will be slower.


```supercollider
a = 1;

a == 1 and: { "second condition".postln; [true, false].choose }
second condition
true

a == 1 or: { "second condition".postln; [true, false].choose }
true

a != 1 and: { "second condition".postln; [true, false].choose }
false

a != 1 or: { "second condition".postln; [true, false].choose }
second condition
true
```


In this case, the second condition will cause an error if a is nil, because nil does not understand addition. a.notNil is a safeguard to ensure the second condition makes sense.


```supercollider
a = nil;
a.notNil and: { "second condition".postln; (a = a+1) < 5 }
false

a = 10;
a.notNil and: { "second condition".postln; (a = a+1) < 5 }
second condition
false
```




## SequenceableCollection operators
Operators oftwn used with [Array](../Classes/Array.md), [Collection](../Classes/Collection.md), [List](../Classes/List.md) and so on. Due to [Polymorphism](../Guides/Polymorphism.md), the calculation result may vary depending on the class.


**`object ++ object`**
: concatenation

**`collection +++ collection`**
: lamination (see [J-concepts-in-SC](../Guides/J-concepts-in-SC.md))

**`collection @ index`**
: collection/array indexing: .at(index) or [index]

**`collection @@ integer`**
: collection/array indexing: .wrapAt(int)

**`collection @|@ integer`**
: collection/array indexing: .foldAt(int)

**`collection |@| integer`**
: collection/array indexing: .clipAt(int)





## Set operators

**`set & set`**
: intersection of two sets

**`set | set`**
: union of two sets

**`setA - setB`**
: difference of sets (elements of setA not found in setB)

**`set -- set`**
: symmetric difference:
```supercollider
(setA -- setB) == ((setA - setB) | (setB - setA))
```




```supercollider
a = Set[2, 3, 4, 5, 6, 7];
b = Set[5, 6, 7, 8, 9];

a - b
Set[ 2, 4, 3 ]

b - a
Set[ 8, 9 ]

((a-b) | (b-a))
Set[ 2, 9, 3, 4, 8 ]

a -- b
Set[ 2, 9, 3, 4, 8 ]
```




## Geometry operators

**`number @ number`**
: make a [Point](../Classes/Point.md) of two numbers
```supercollider
x @ y
// returns:
Point(x, y)
```

**`point @ point`**
: make a [Rect](../Classes/Rect.md) of two [Point](../Classes/Point.md)s
```supercollider
Point(left, top) @ Point(right, bottom)
// returns:
Rect(left, top, right-left, bottom-top)
```

**`ugen @ ugen`**
: create a Point with two [UGen](../Classes/UGen.md)s

**`rect & rect`**
: intersection of two rectangles

**`rect | rect`**
: union of two rectangles (returns a Rect whose boundaries exactly encompass both Rects)





## IOStream operators

**`stream << object`**
: represent the object as a string and add to the stream. A common usage is with the Post class, to write output to the post window.
```supercollider
Post << "Here is a random number: " << 20.rand << ".\n";
Here is a random number: 13.
```

**`stream <<* collection`**
: add each item of the collection to the stream.
```supercollider
Post << [0, 1, 2, 3]
[ 0, 1, 2, 3 ]

Post <<* [0, 1, 2, 3]
0, 1, 2, 3
```

**`stream <<< object`**
: add the object's compile string to the stream.
```supercollider
Post <<< "a string"
"a string"
```

**`stream <<<* collection`**
: add each item's compile string to the stream.





## Conditional execution operators

**`object ? object`**
: nil check (no .value)

**`object ?? function`**
: nil check (.value, function is inlined) If the object is nil, the second expression's value will be used; otherwise, it will be the first object.
```supercollider
a = [nil, 5];

10.do({ (a.choose ? 20.rand).postln });
10.do({ (a.choose ?? { 20.rand }).postln });
```

`?? { }` is generally recommended. `?` always evaluates the second expression, even if its value will not be used. `??` evaluates the function conditionally (only when needed). If the function defines no variables, the function will be inlined for speed.Especially useful when the absence of an object requires a new object to be created. In this example, it's critical that a new Slider not be created if the object was already passed in.
```supercollider
f = { |slider, parent|
    slider = slider ?? { Slider.new(parent, Rect(0, 0, 100, 20)) };
    slider.value_(0);
};
```

If the first line inside the function instead read
```supercollider
slider = slider ? Slider.new(parent, Rect(0, 0, 100, 20));
```

, a new slider would be created even if it is not needed, or used.

**`object !? function`**
: execute function if object is not nil.
```supercollider
a = [10, nil].choose;
a !? { "ran func".postln };
// equivalent of:
if (a.notNil) { "ran func".postln };
```

Used when an operation requires a variable not to be empty.
```supercollider
f = { |a| a + 5 };
f.value
// error: nil does not understand +

f = { |a| a !? { a+5 } };
f.value
nil // no error
f.value(2)
7
```





## Miscellaneous operators

**`object ! number`**
: same as `object.dup(number)`
```supercollider
15 ! 5
[ 15, 15, 15, 15, 15 ]
```

If the object is a function, it behaves like Array.fill(number, function).
```supercollider
{ 10.rand } ! 5
[ 8, 9, 3, 8, 0 ]
```

**`object -> object`**
: creates an [Association](../Classes/Association.md), used in dictionaries.

**`expression <! expression`**
: bypass value of second expression. This operator evaluates both expressions, and returns the value of the first.
```supercollider
a = 0;
0

// a is incremented twice, but the return value (1)
// comes from the first increment (0 + 1)
(a = a + 1) <! (a = a + 1)
1

a    // a's value reflects both increments
2
```

**`function <> function`**
: function composition operator. This operator returns a new function, which evaluates the second function and passes the result to the first function.
```supercollider
f = { |a| a * 5 } <> {|a| a + 2 };
f.(10);
60                  // == (10+2) * 5
```

An array as argument is passed through the chain:
```supercollider
f.([10, 75, 512]);
[ 60, 385, 2570 ]   // == ([10, 75, 512]+2) * 5
```





## Symbolic notations to define literals/other objects

**`$`**
: character prefix: `"ABC".at(0) == $A`

**`''` or `\`**
: define a literal [Symbol](../Classes/Symbol.md) : `'abc' === \abc`

**`""`**
: define a literal [String](../Classes/String.md) : `"SuperCollider is the best"`

**`[item, item...]`**
: define an [Array](../Classes/Array.md) containing given items

**`Set[item, item...]`**
: define a [Set](../Classes/Set.md) -- any [Collection](../Classes/Collection.md) class name can be used other than Set

**`#[item, item...]`**
: define a literal [Array](../Classes/Array.md)

**`(a:1, b:2)`**
: define an [Event](../Classes/Event.md) (same as `Event[\a -> 1, \b -> 2]`)

**``` (backtick or backquote)**
: define a [Ref](../Classes/Ref.md) : ``1 == Ref(1), `(a+1) == Ref(a+1)`

**`\`**
: inside a string or symbol, escapes the next character
```supercollider
"abc\"def\"ghi"
abc"def"ghi

'abc\'def\'ghi'
abc'def'ghi
```


**`\t`**
: tab character

**`\n`**
: newline character

**`\l`**
: linefeed character

**`\r`**
: carriage return character

**`\\`**
: \ character

**`{ }`**
: define an open function

**`#{ }`**
: define a closed function

**`(_ * 2)`**
: define a function `{ |a| a * 2 }` (see [Partial-Application](../Reference/Partial-Application.md))





## Argument definition

**`|a, b, c|`**
: define function/method arguments

**`|a, b ... c|`**
: define function/method arguments; arguments after a and b will be placed into c as an array

**`#a, b, c = myArray`**
: assign consecutive elements of myArray to multiple variables

**`#a, b ... c = myArray`**
: assign first two elements to a and b; the rest as an array into c





## Where f is a function

**`f.( )`**
: evaluate the function with the arguments in parentheses

**`f.(*argList)`**
: evaluate the function with the arguments in an array

**`f.(anArgName: value)`**
: keyword addressing of function or method arguments
```supercollider
f = { |a, b| a * b };
f.(2, 4);
f.(*[2, 4]);
f.(a: 2, b: 4);
```

**`SomeClass.[index]`**
: Equivalent to SomeClass.at(index) -- Instr.at is a good example

**`myObject.method(*array)`**
: call the method with the arguments in an array

**`obj1 method: obj2`**
: same as `obj1.method(obj2)` or `method(obj1, obj2)`. This works only with single-argument methods like binary operators.





## Class and instance variable access
Inside a class definition (see [WritingClasses](../Guides/WritingClasses.md) ):


```supercollider
{
    classvar <a,    // Define a class variable with a getter method (for outside access)
             >b,    // Define a class variable with a setter method
             <>c;   // Define a class variable with both a getter and setter method

    var      <a,    // Define an instance variable with a getter method (for outside access)
             >b,    // Define an instance variable with a setter method
             <>c;   // Define an instance variable with both a getter and setter method

    // methods go here ...
}
```


These notations do not apply to variables defined within methods.


**`^someExpression`**
: Inside a method definition: return the expression's value to the caller

**`instVar_ { }`**
: define a setter for an instance variable

**`myObject.instVar = x;`**
: invoke the setter: `(myObject.instVar_(x); x)`





## Array series and indexing

**`(a..b)`**
: produces an array consisting of consecutive integers from a to b

**`(a, b..c)`**
: e.g.: (1, 3..9) produces [1, 3, 5, 7, 9]

**`(..b)`**
: produces an array 0 through b

**`(a..)`**
: not legal (no endpoint given)

**`a[i..j]`**
: same as `a.copySeries(i, j)` (see [ArrayedCollection#-copySeries](../Classes/ArrayedCollection.md#-copyseries))

**`a[i, j..k]`**
: e.g.: `a[1, 3..9]` retrieves array elements 1, 3, 5, 7, 9

**`a[..j]`**
: same as `a.copySeries(0, j)`

**`a[j..]`**
: same as `a.copySeries(i, a.size-1)` (this is OK--Array is finite)

**`~`**
: access an environment variable

**`~abc`**
: compiles to `\abc.envirGet`

**`~abc = value`**
: compiles to `\abc.envirPut(value)`





## Adverbs to math operators
(see [Adverbs](../Reference/Adverbs.md) )

e.g.:


```supercollider
[1, 2, 3] * [2, 3, 4]
[ 2, 6, 12 ]

[1, 2, 3] *.t [2, 3, 4]
[ [ 2, 3, 4 ], [ 4, 6, 8 ], [ 6, 9, 12 ] ]
```





**`.s`**
: output length is the shorter of the two arrays

**`.f`**
: use folded indexing instead of wrapped indexing

**`.t`**
: table-style

**`.x`**
: cross (like table, except that the results of each operation are concatenated, not added as another dimension)

**`.0`**
: operator depth (see [J-concepts-in-SC](../Guides/J-concepts-in-SC.md) )

**`.1`**
: etc.







