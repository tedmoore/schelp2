# FunctionList

*A function that composes multiple functions into one*

**Categories:** Core>Kernel

## Description

A FunctionList is a function that composes multiple functions into one. This allows allow to deal transparently with several functions as if they were one and to append new functions at a later point. The functions are evaluated in the order they have in the FunctionList's array, which is by default the order in which they have been added to it.
See the [Functions](../Reference/Functions.md) help file for a basic introduction.

```
a = FunctionList.new;
fork { loop { 0.7.wait; a.value.postln } };
a.addFunc({ 800.rand });
a.addFunc({ "another".scramble });
```




## Class Methods


### `new`
create a new instance.**Arguments:**

| Argument | Description |
|----------|-------------|
| `functions` | An array of functions or objects |  


## Instance Methods


### `array`
Set/get the FunctionList's array. New functions can be added to the array directly, e.g.
```
x = FunctionList(...some functions);
x.array = x.array.insert(2, aFunction);
```


### `addFunc`
This message is used to be able to add to an Object, to a Function, or to a FunctionList. `nil.addFunc` returns a function, if only one function is passed in the argument. `function.addFunc` then returns a FunctionList.
### `removeFunc`
remove a function from the list.**Returns:** the last function when only one function is left, or `nil` when the last function was removed.`addFunc` and `removeFunc` are implemented for [Nil](../Classes/Nil.md), [Object](../Classes/Object.md) and [FunctionList](../Classes/FunctionList.md)
```
nil.addFunc(f) // returns f
obj.addFunc(f) // returns FunctionList([obj, f])
nil.removeFunc(f) // returns nil
obj.removeFunc(f) // returns nil, if f === obj, else obj is returned
```


## Examples


```
// example

a = nil;
a = a.addFunc { |x = "", y = ""| "this % is an % example\n".postf(x, y); 1 };
a.postln;
a = a.addFunc { |x = "", y = ""| "there is no % that is %\n".postf(x, y); 2 };
a.value;
a.value("text", "extraordinary well written")
a.valueArray(["x", "y"]);
```



```
// Function:do vs FunctionList:do (same)
a.do { |x| x.value };
{ 4 }.do { |x| x.value.postln }

(
().use {
    ~x = "array";
    ~y = "ominous";
    a.valueEnvir;
    a.valueEnvir("list");
}
)
```



```
// removing a function
x = { "removal test".postln };
a.addFunc(x);
a.value;
a = a.removeFunc(x);
a.value;

// mathematics
a = nil;
a = a.addFunc({ 1.0.rand }).addFunc({ [0, 1].choose });
a = a.squared.linexp(0, 1, 1.0, 500);

a.value;
```



```
// compatibility with function multichannel expansion
a = nil;
a = a.addFunc { |x = 0| if(x > 0) { 7 } { 1000.rand } };
a = a.addFunc { |x = 0| if(x < 0) { 17 } { -1000.rand } };
a.value

a = a.flop;
a.value
a.value([-1, 1])
a.value(x:[-1, 1]); // kwargs
```



```
// typical usage in a Document action
// see also SCView: addAction example.

d = Document.current;
d.keyDownAction = { "You touched the keyboard.".postln };

d.keyDownAction = d.keyDownAction.addFunc { :x, x<-(1..), :: "already % times\n\n".postf(x) };


d.keyDownAction = nil;

// even if you don't know if there is already an action defined
// one can add one.

(
d.keyDownAction = nil;
d.keyDownAction = d.keyDownAction.addFunc { :x, x<-(1..), :: "already % times\n\n".postf(x) };

);

d.keyDownAction = nil;
```




