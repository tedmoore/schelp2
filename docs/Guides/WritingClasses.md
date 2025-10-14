# Writing Classes

*Writing SuperCollider Classes*

**Categories:** Language>OOP

**Related:** [Classes](../Reference/Classes.md), [Class](../Classes/Class.md), [Object](../Classes/Object.md)

SuperCollider follows a pure object-oriented paradigm. It is not built on data types, but on objects, which respond to messages. A class is an object that holds information about how its objects (instances) respond to such messages. Writing a class gives a definition of this behavior.
This is an overview of idioms used in writing classes. It is not a tutorial on writing a system of interrelated classes. It gives an overview of some typical expressions. See also: [Intro-to-Objects](../Guides/Intro-to-Objects.md), [Messages](../Reference/Messages.md), and [Classes](../Reference/Classes.md).
There is also an overview of the current full [ClassTree](../Overviews/ClassTree.md).

> **Note:** Class definitions are statically compiled when you launch SuperCollider or "recompile the library." This means that class definitions must be saved into a file with the extension .sc, in a disk location where SuperCollider looks for classes. Saving into the main class library (SCClassLibrary) is generally not recommended. It's preferable to use either the user or system extension directories.
```supercollider
Platform.userExtensionDir;   // Extensions available only to your user account
Platform.systemExtensionDir; // Extensions available to all users on the machine
```

It is not possible to enter a class definition into an interpreter window and execute it.



## Inheriting
To avoid having to write the same code several times, classes can **inherit** implementations from their **superclasses**.


```supercollider
MyClass : SomeSuperclass {

}
```


Without specifying a superclass, [Object](../Classes/Object.md) is assumed as the default superclass.


```supercollider
MyClass { // : Object is implied

}
```


This is why in the above example, the message `new` can be called without being explicitly defined in the class.



## Methods

### Instance Methods
Each object instance responds to its **instance methods**. Instance methods are called in the local context of the object. Within instance methods, the keyword `this` refers to the instance itself.


```supercollider
MyClass {

    instanceMethod { | argument |
        this.anotherInstanceMethod(argument)
    }

    anotherInstanceMethod { | argument |
        "hello instance".postln
    }
}
```


This could then be used as follows:


```supercollider
a = MyClass.new // returns a new instance
a.instanceMethod // posts "hello instance"
```


To return from the method use `^` (caret). Multiple exit points also possible. If no `^` is specified, the method will return the instance (and in the case of Class methods, will return the class). There is no such thing as returning void in SuperCollider.


```supercollider
MyClass {
    someMethod {
        ^returnObject
    }

    someOtherMethod { | aBoolean |
        if(aBoolean) {
            ^someObject
        } {
            ^someOtherObject
        }
    }

}
```





### Class Methods
An object's **class methods** are defined alongside its instance methods. They are specified with an asterisk (`*`) before the method name.

A [Class](../Classes/Class.md) is itself an object. It is what all instances of it have in common. Class methods are the instance methods of the object's class. That's why within class methods, the keyword `this` refers to the class.


```supercollider
MyClass {
    *classMethod { | argument |
        this.anotherClassMethod(argument)
    }

    *anotherClassMethod { | argument |
        "hello class".postln
    }

}
```


This could then be used as follows:


```supercollider
MyClass.classMethod // posts "hello class"
```





### Overriding methods (overloading)
To change the behaviour inherited from the superclass, methods can be overridden. Note that an object looks always for the method it has defined first and then looks in the superclass. Here `MyClass.value(2)` will return 6, not 4:


```supercollider
SomeSuperclass {
    calculate { |in| ^in * 2 }
    value { |in| ^this.calculate(in) }
}

MyClass : SomeSuperclass {
    calculate { |in| ^in * 3 }
}
```


The keyword `super` can be used to call methods on the superclass


```supercollider
SomeSuperclass {

    value {
        ^100.rand
    }
}

MyClass : SomeSuperclass {

    value {
        ^super.value * 2
    }
}
```






## Instances
`Object.new` will return a new object. When overriding the class method `.new` you must call the superclass, which in turn calls its superclass, up until `Object.new` is called and an object is actually created and its memory allocated.


```supercollider
MyClass {
    // This is a normal constructor method.
    *new { ^super.new }
}
```


In this case note that `super.new` calls the method `new` on the superclass and returns a new object.


### Instance Variables and Initialisation Logic
Instance can have variables associated with them — known as members is other languages.


```supercollider
Foo {
    var a, b, c; // Instance variables.
}
```


These can be assigned in two ways. Through `newCopyArgs` or through an `init` method. The former is recommend and discussed first.

Rather than calling the method `new` a call to [Object#*newCopyArgs](../Classes/Object.md#*newcopyargs) can be used to initialise members.

The code below allows the call–site to decide the initial value of `c` and defaults `a` to 10 and `b` to 20.


```supercollider
Foo {
    var a, b, c;
    *new { |myC| ^super.newCopyArgs(a: 10, b: 20, c: myC) }
}
```


If initialisation logic that prepares the arguments before assignment is required, ideally, it should go before the call to `super.newCopyArgs`. This way the final object never exists in an invalid state — an alternative is the use of an `init` method and shall be shown shortly.

However, when there is a hierarchy of classes, `newCopyArgs` requires that all the base class arguments be passed in the order they are defined.  This makes changing the base class difficult. Here is one way to mitigate this issue using variable keyword arguments [Functions#Variable Arguments](../Reference/Functions.md#variable-arguments) and [Object#-superPerformArgs](../Classes/Object.md#-superperformargs).


```supercollider
Base {
    var <>a, <>b;
    *new { |a, b ...args, kwargs|
        ^super.superPerformArgs(\newCopyArgs, [a, b] ++ args, kwargs);
    }
}

Derived : Base {
    var <>c;
    *new { |a, b, c ...args, kwargs|
        ^super.superPerformArgs(\new, [a, b, c] ++ args, kwargs)
    }
}
```


Calling `Derived(1, 2, 3)` will set `a` to `1`, `b` to `2`, and `c` to 3. Here are some more examples:


```supercollider
Derived(c: 10) // a: nil, b: nil, c: 10
Derived(1, 2, c: 10) // a: 1, b: 2, c: 10
Derived(d: 10) // If 'd' existed somewhere in the hierarchy, it would be assigned the value 10.
```


Although this approach might seem complex, the benefit is that the new instance variables can be added to either class and it will always be clear which one you meant to assign to.

Should it be desirable to remove instance variables of the base class in the future, it is good to require that only keyword arguments be used. This can be achieved by removing the named arguments and throwing an error if `args` is not empty. One disadvantage here is that autocomplete in the IDE will not work.


```supercollider
Foo {
    *new { |... args, kwargs| 
        if(args.empty.not) { Error().throw };
        ^super.superPerformArgs(\newCopyArgs, #[], kwargs);
    }
}
```


Another benefit is that the instance is never in an incomplete state: either all the instance members have been assigned to, or the object does not exist.

The disadvantages come when you have complex initialisation logic where the arguments in `Derived` require knowledge of the arguments in `Base`. Traditionally in SuperCollider this has been solved with an `init` method as seen below, although a 'builder' pattern might be considered for complex cases.


```supercollider
Base {
    var a, b;
    *new {|a, b| ^super.new.init(a, b) }
    init {|newA, newB|
        // Initialization logic goes here.
        a = newA;
        b = newB;
    }
}
```


This works but becomes more complex in inheritance chains.


```supercollider
Base {
    var a, b;
    *new {|a, b| ^super.new.init(a, b) }
    init {|newA, newB|
        // Initialization logic goes here.
        a = newA;
        b = newB;
    }
}

Derived : Base {
    var c;
    *new { |a, b, c| ^super.new.derivedInit(a, b, c) }
    derivedInit { |newA, newB, newC|
        // do initialisation with all the arguments
        this.init(newA, newB) // call Base.init
        c = newC; // assign to Derived's c
    }
}
```


> **⚠️ Warning:** If both the `Base` and `Derived` class define an `init` method, the `Derived` class will override the `Base`'s implementation,  meaning it will no longer be possible to call that implementation. In such cases, a unique method name like `myclassInit` should be used, or better yet, a specialised name that indicates what kind of initialization is performed.
While the `init` pattern is the most flexible, care must be taken as inside the `init` functions, the instance is in an incomplete state and other methods might not work as expected; for example, this may become confusing when combined with threads and asynchronous execution, for example, when interacting with the server.





## Class instances
Class variables are accessible within class methods and in any instance methods.


```supercollider
MyClass {
    classvar myClassvar;

    instanceMethod {
        ^myClassvar
    }
}
```


Initializations on class level (e.g. to set up `classvar`s) can be implemented by overloading the [Class#*initClass](../Classes/Class.md#*initclass) method.


```supercollider
MyClass {
    classvar myClassvar;

    *initClass {
        myClassvar = IdentityDictionary.new;
    }
}
```




## Alternatives to inheritance
Overreliance on inheritance is usually a design flaw. Inheritance is mainly a way to organise code, and shouldn't be mistaken for a categorisation of objects. Two objects may respond to a message in different ways (polymorphism), and objects delegate control to ther objects they hold in their instance variables (object composition).


### Polymorphism
See also: [Polymorphism](../Guides/Polymorphism.md)

Two completely unrelated objects can respond to the same messages and therefore be used together in the same code. For example, [Function](../Classes/Function.md) and [Event](../Classes/Event.md) have no common superclass apart from the general class [Object](../Classes/Object.md). But both respond to the message `play`. Instead of inheriting all methods, you can simply implement some of the same methods in your class.


```supercollider
MyClass {
    var count = 0;
    value {
        ^count = count + 1
    }
}
// objects of this class will respond to the message "value", just like a function.
a = MyClass.new;
a.value; // returns 1
```





### Object Composition
Often, an object passes control to one of the objects it has in its instance variables. Because these objects can be of any kind, this is a very flexible way to achieve a wide range of functionalities. For example, a [Button](../Classes/Button.md) has an `action` instance variable, which may hold anything that responds to the message `value`.


```supercollider
MyClass {
    var action;
    *new { |action|
        ^super.newCopyArgs(action)
    }
    value { |x|
        action.value(x);
    }
}

// depending on what "action" is, objects of this class will behave differently
a = MyClass({ "hello." });
b = MyClass({ |i| log2(i) * sin(i * pi) });
a.value(8);
b.value(8);
```


Often, variables like `action` above are filled with custom objects that belong to `MyClass`. Thus, one will write many small classes that can be well combined in such a way. This is called "pluggable behavior".





## Variables

### Initializing variables directly
In a variable declaration, variables can be directly initialized. Only [Literals](../Reference/Literals.md) may be used to initialize variables this way. This means that it is not possible to chain assignments (e.g. `var x = 9; var y = x + 1`).


```supercollider
MyClass {
    classvar all = #[];
    var x = 8;
    var y = #[1, 2, 3];
}
```





### Variable Scope
An instance variable is accessible **from all instance methods** of this class and its subclasses. A class variable, by contrast, is accessible **from all class and instance methods** of this class and its subclasses. Instance variables will shadow class variables of the same name.


```supercollider
MyClass {
    classvar x = 0, y = 1;
    var x = 1;

    *returnX { ^x } // returns 0
    returnX { ^x } // returns 1
    returnXY { ^x + y } // returns 2
}
```


Subclasses can override class variable declarations (but not instance variables). Then the class variables of the superclass are not accessible in the subclass anymore.


```supercollider
SomeSuperclass {
    classvar x = 0;

    returnX { ^x }
    returnXHere { ^x }
}

MyClass : SomeSuperclass {
    classvar x = 1;

    returnXHere { ^x }
}

// SomeSuperclass.returnXHere returns 0
// MyClass.returnXHere returns 1
// MyClass.returnX returns 0
```





### Getters and Setters
SuperCollider demands that variables are not accessible outside of the class or instance. A method must be added to explicitly give access:


```supercollider
MyClass : SomeSuperclass {
    var myVariable;

    variable {
        ^myVariable
    }

    variable_ { | newValue |
        myVariable = newValue;
    }
}
```


These are referred to as getter and setter methods. SuperCollider allows these methods to be easily added by adding `<` or `>`.


```supercollider
MyClass {
    var <getMe, >setMe, <>getMeOrSetMe;
}
```


This provides the following methods:


```supercollider
someObject.getMe;
someObject.setMe_(value);
```


And it also allows us to say:


```supercollider
someObject.setMe = value;

someObject.getMeOrSetMe_(5);
someObject.getMeOrSetMe;
```


A getter or setter method created in this fashion may be overridden in a subclass by explicitly defining the method. Setter methods should take only one argument to support both ways of expression consistently. eg.


```supercollider
MyClass {

    variable_ { | newValue |
        variable = newValue.clip(minval,maxval);
    }

}
```


A setter method should always return the receiver. This allows us to be sure that several setters can chained up.




### Constants
Constants are variables, that, well, don't vary. They can only be assigned initially.


```supercollider
MyClass {
    const <zero = 0;
}

MyClass.zero // returns 0
```






## External method files
Methods may be added to Classes in separate files. This is equivalent to Categories in Objective-C. By convention, the file name starts with a lower case letter: the name of the method or feature that the methods are supporting.


```supercollider
+ Class {

    newMethod {

    }

    *newClassMethod {

    }

}
```




## Slotted classes
Classes defined with `[slot]` can use the syntax `myClass[...]` which will call `myClass.new` and then `this.add(each)` for each item in the square brackets.


```supercollider
MyClass[] {
    var <allOfThem;
    add { |item|
        allOfThem = allOfThem.add(item)
    }
}

a = MyClass[1, 2, 3];
a.allOfThem; // [1, 2, 3]
```




## Printing to string

### Printing custom messages to post window
By default when postln is called on an class instance the name of the class is printed in a post window. When `postln` or `asString` is called on a class instance, the class then calls `printOn` which by default returns just the object's class name. This should be overridden to obtain more useful information.


```supercollider
MyTestPoint {
    var <x, <y;

    *new { |x, y|
        ^super.newCopyArgs(x, y)
    }

    printOn { | stream |
        stream << "MyTestPoint( " << x << ", " << y << " )";
    }
}
```



```supercollider
a = MyTestPoint(2, 3)
```





### Defining custom asCompileString behaviour
A call to `asCompileString` should return a string which when evaluated creates the exact same instance of the class. To define a custom behaviour one should either override `storeOn` or `storeArgs`. The method `storeOn` should return the string that evaluated creates the instance of the current object. The method `storeArgs` should return an array with the arguments to be passed to `TheClass.new`. In most cases this method can be used instead of `storeOn`.


```supercollider
// either
MyTestPoint {
    var <x, <y;

    *new { |x, y|
        ^super.newCopyArgs(x,y)
    }

    storeOn { | stream |
        // note that <<< stands for storeOn, and << for printOn.
        // we want x and y to be completely represented
        stream << "MyTestPoint.new(" <<< x << ", " <<< y << ")"
    }
}

// or
MyTestPoint {
    var <x, <y;

    *new { |x, y|
        ^super.newCopyArgs(x,y)
    }

    storeArgs { | stream |
        ^[x, y]
    }
}
```



```supercollider
MyTestPoint(2, 3).asCompileString;
```






## Private Methods
Private methods are marked by a prefix `pr`, e.g. `prBundleSize`. This is just a **naming convention**; the message can still be called from anywhere. It is recommended to stick to convention and only call private methods from within the class that defines them.



## Catching undefined method calls
When a message is received that is undefined, the receiver calls the method `doesNotUnderstand`. Normally this throws an error. By overriding `doesNotUnderstand`, it is possible to catch those calls and use them. For an example, see the class definition of `IdentityDictionary`.


```supercollider
MyClass {

    doesNotUnderstand { | selector... args, kwargs |
        (this.class ++ " does not understand method " ++ selector);

        if(UGen.findRespondingMethodFor(selector).notNil) {
            "But UGen understands this method".postln
        };
    }
}
```



```supercollider
a = MyClass();
a.someMethodThatDoesNotExist
```






