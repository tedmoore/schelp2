# Classes

**Categories:** Language>OOP

*explaining classes*

**Related:** [Class](../Classes/Class.md), [Assignment](../Reference/Assignment.md), [Intro-to-Objects](../Guides/Intro-to-Objects.md), [Messages](../Reference/Messages.md), [Polymorphism](../Guides/Polymorphism.md), [WritingClasses](../Guides/WritingClasses.md)

All objects in SuperCollider are members of a class that describes the objects' data and interface. The name of a class must begin with a capital letter. Class names are the only global values in the SC language. Since classes are themselves objects, the value of a class name identifier is the object representing that class.
See [Intro-to-Objects](../Guides/Intro-to-Objects.md) for an introduction to the concepts of classes, objects and messages.

## Instance Variables
The data of an object is contained in its instance variables. Instance variables are of two kinds, named and indexed. Each object contains a separate copy of its instance variables.

Some classes' instances have no instance variables at all but instead have an atomic value. Classes whose instances consist of an atomic value are [Integer](../Classes/Integer.md), [Float](../Classes/Float.md), [Symbol](../Classes/Symbol.md), [True](../Classes/True.md), [False](../Classes/False.md), [Nil](../Classes/Nil.md), [Char](../Classes/Char.md), [Color](../Classes/Color.md).

Instance variables declaration lists occur after the open curly bracket of the class definition and are preceded by the reserved word `var`. Instance variables names in the list may be initialized to a default literal value by using an equals sign. Instance variables which are not explicitly initialized will be set to nil. Instance variables that are immutable are defined by the reserved word `const`.

Instance variables may only be directly accessed and changed from within the class' own methods. Instance variables may be exposed to clients by adding getter and setter messages to the class. A getter message is a message with the same name as the variable which returns the value of that variable when sent to the receiver. A setter message is a message with the name of the variable with an underscore appended which sets the value of the instance variable to the value of the argument to the message.

Getter and setter methods may be defined in the declaration of the instance variable. A getter message for an instance variable is created by typing a less than sign `<` before the variable name. A setter message is created by typing a greater than `>` sign before the variable name. If both occur then they must occur in the order `<>`.


```
var a, <b, >c, <>d;
```





**a**
: has no getter or setter.

**b**
: has a getter but not a setter.

**c**
: has only a setter.

**d**
: has both a getter and setter.






```
Point {
    // x and y are instance variables which have both getter and setter methods
    // and default to zero.
    var <>x = 0, <>y = 0;
    ...
}

p = Point.new;
p.x_(5);        // send setter message to set x to 5
p.y_(7);        // send setter message to set y to 7
p.x = 5;        // send setter message using setter assignment
p.y = 7;        // send setter message using setter assignment
a = p.x;        // send getter message for x
b = p.y;        // send getter message for y
```




## Class Variables
Class variables are values that are shared by all objects in the class. Class variable declaration lists are preceded by the reserved word `classvar` and may be interspersed with instance variable declaration lists. Class variables like instance variables may only be directly accessed by methods of the class. Class variables may also have getter and setter methods created for them using the less than `<` and greater than `>` symbols.



## Instance Methods
The messages of a class' interface are implemented in the methods of the class. When an object is sent a message the method whose name matches the message selector in the receiver's class is executed.

Method definitions follow the class variable and instance variable declarations in the class.

Method definitions are similar to FunctionDefs in syntax. Method definitions begin with the message selector. The message selector must be an identifier or a binary operator. Methods have arguments and variable declarations with the same syntax as in FunctionDefs. Methods however have an implicit first argument named this which is the receiver of the message. The variable `this` may be referred to just like any of the other arguments and variables in the method. You may not assign a value to `this`.



## Class Methods
Class Methods are methods that implement messages sent to the class object. A common example is the message new which is sent to the class object to create a new instance of the class. Class method names have an asterisk `*` preceding the message selector.



## Determine the class of an object
[Object](../Classes/Object.md) defines the method `isKindOf`:


```
anObject.isKindOf(aClass)
```


It returns true if the object is of the class or one of its subclasses.

To determine if an object is specifically of type aClass, but not one of its subclasses, use the `class` instance variable and the identity equals sign:


```
anObject.class === aClass
```






