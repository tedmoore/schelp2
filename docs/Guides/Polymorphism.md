# Polymorphism

*the ability of different classes to respond to a message in different ways*

**Categories:** Language>OOP

**Related:** [Messages](../Reference/Messages.md), [Classes](../Reference/Classes.md), [Intro-to-Objects](../Guides/Intro-to-Objects.md)


## Introduction
Polymorphism is the ability of different classes to respond to a message in different ways. A message generally has some underlying meaning and it is the responsibility of each class to respond in a way appropriate to that meaning.

For example, the `value` message means "give me the effective value of this object".

The value method is implemented by these classes (among others):


**Function :**
: this.value(args)

**Object :**
: this.value()

**Ref :**
: this.value



Let's look at how these classes implement the value message.


### Object
Here's the value method in class [Object](../Classes/Object.md) :


```supercollider
value { ^this }
```


It simply returns itself. Since all classes inherit from class Object this means that unless a class overrides `value`, the object will respond to `value` by returning itself.


```supercollider
5.postln;            // posts itself
5.value.postln;        // value returns itself
'a symbol'.postln;
'a symbol'.value.postln;
[1,2,3].value.postln;
//etc...
```





### Function
In class [Function](../Classes/Function.md) the value method is a primitive:


```supercollider
value { arg ... args;
    _FunctionValue
    // evaluate a function with args
    ^this.primitiveFailed
}
```


`_FunctionValue` is a C code primitive, so it is not possible to know just by looking at it what it does. However what it does is to evaluate the function and return the result.


```supercollider
{ 5.squared }.postln;            // posts Instance of Function
{ 5.squared }.value.postln;        // posts 25
```





### Ref
The [Ref](../Classes/Ref.md) class provides a way to create an indirect reference to an object. It can be used to pass a value by reference. Ref objects have a single instance variable called `value`. The `value` method returns the value of the instance variable `value`. Here is a part of the class definition for Ref:


```supercollider
Ref : AbstractFunction
{
    var <>value;

    *new { arg thing; ^super.new.value_(thing) }
    set { arg thing; value = thing }
    get { ^value }
    dereference { ^value }
    asRef { ^this }

    // behave like a stream
    next { ^value }

    printOn { arg stream;
        stream << "`(" << value << ")";
    }
    storeOn { arg stream;
        stream << "`(" <<< value << ")";
    }
}
```


Here is how it responds :


```supercollider
Ref.new(123).postln;
Ref.new(123).value.postln;
```


Ref also implements a message called `dereference` which is another good example of polymorphism. As implemented in Ref, dereference just returns the value instance variable which is no different than what the value method does. So what is the need for it? That is explained by how other classes respond to dereference. The dereference message means "remove any Ref that contains you". In class Object dereference returns the object itself, again just like the value message. The difference is that no other classes override this method. So that dereference of a Function is still the Function.


**Object :**
: this.dereference()

**Ref :**
: this.dereference()






```supercollider
5.value.postln;
{ 5.squared }.value.postln;
Ref.new(123).value.postln;

5.dereference.postln;
{ 5.squared }.dereference.postln;
Ref.new(123).dereference.postln;
```






## Play
Yet another example of polymorphism is play. Many different kinds of objects know how to play themselves.


### Function

```supercollider
{ PinkNoise.ar(0.1) }.play;
```





### AppClock

```supercollider
(
var w, r;
w = Window.new("trem", Rect(512, 256, 360, 130));
w.front;
r = Routine({ arg appClockTime;
    ["AppClock has been playing for secs:",appClockTime].postln;
    60.do({ arg i;
        0.05.yield;
        w.bounds = w.bounds.moveBy(10.rand2, 10.rand2);
        w.alpha = cos(i*0.1pi)*0.5+0.5;
    });
    1.yield;
    w.close;
});
AppClock.play(r);
)
```





### SynthDef

```supercollider
(
x = SynthDef("Help-SynthDef", { arg out=0;
    Out.ar(out, PinkNoise.ar(0.1))
}).play;
)
```





### Pattern

```supercollider
Pbind(\degree, Pseq([0, 1, 2, 3],inf)).play;
```






## Conclusion
Polymorphism allows you to write code that does not assume anything about the implementation of an object, but rather asks the object to "do what I mean" and have the object respond appropriately.



