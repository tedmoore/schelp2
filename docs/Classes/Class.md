# Class

*A Class describes the structure and implementation of a set of objects which are its instances.*

**Categories:** Core>Kernel, Language>OOP

**Related:** [WritingClasses](../Guides/WritingClasses.md), [Classes](../Reference/Classes.md)


## Class Methods

### `allClasses`
**Returns:** an [Array](../Classes/Array.md) of all Classes
### `initClass`
When SuperCollider starts up, just after it has compiled the library, it initializes all the classes from Object down, a depth first traversal of subclasses.This method can be overloaded in any class that requires initialization of classvars or other resources.
> **Note:** Each class will be initialized once, thus each class' `initClass` is called exactly once during the initialization phase.


### `initClassTree`
used in [#*initClass](#*initclass) to assure the initialisation of `aClass` before using it. Wherever necessary, it recursively initializes all classes required by `aClass`.In some cases it is required that another class and its resources are initialized before you initialize your own. This can be accomplished by
```supercollider
YourClass {
    *initClass {
        // initialize OtherClass before continuing
        Class.initClassTree(OtherClass);

        ..

        // use OtherClass

        ..
    }

    ..

}
```

Pre-initialized data such as [SynthDef](../Classes/SynthDef.md)s should be deferred to [StartUp](../Classes/StartUp.md)
```supercollider
YourClass {
    *initClass {
        StartUp.add {
            ..
        }
    }

    ..

}
```



## Instance Methods

### `browse`
Open a graphical browser for this Class. Shows methods, arguments, variables, subclasses, and has buttons for navigating to the superclass, source, helpfile, etc.
```supercollider
Dictionary.browse;
```

### `findMethod`
Find the Method referred to by name. If not found, return nil.
```supercollider
Integer.findMethod('>'); // nil
Integer.findMethod('*'); // Integer:*
```

### `findRespondingMethodFor`
As above, but climb the class tree to see if the method is inherited from a superclass. If not found, return nil.
```supercollider
Integer.findRespondingMethodFor('>'); // SimpleNumber:>
Integer.findRespondingMethodFor('+'); // Integer:*
```

### `respondingMethods`
Return a list of methods for the selectors that an object of this class responds to.
```supercollider
Integer.respondingMethods.do { |item| item.postln };
```

### `instancesRespondTo`
Return true if the message selector or array of message selectors are understood by objects of this class.
```supercollider
Collection.instancesRespondTo(\flop); // false
Set.instancesRespondTo(\clear); // true
Set.instancesRespondTo([\flop, \clear]) // false: not both
```

### `findRespondingSubclasses`
Return a list of all subclasses whose instances respond to the message selector or all message selector in an array.
```supercollider
Collection.findRespondingSubclasses(\flop); // a long list
Set.findRespondingSubclasses(\clear);
Set.findRespondingSubclasses([\flop, \clear]); // not both
```

### `findRespondingUpperSubclasses`
Return a list of all classes down the class tree starting from the receiver, whose instances respond to the message selector or all message selector in an array.
```supercollider
Collection.findRespondingUpperSubclasses(\flop);
Set.findRespondingUpperSubclasses(\clear);
Set.findRespondingUpperSubclasses([\flop, \clear]); // not both
```

### `findSimilarSelectors`
Returns a list of selectors similar to the argument passed. For other arguments and sorting, see [String#-findSimilarIn](../Classes/String.md#-findsimilarin).
```supercollider
Array.findSimilarSelectors(\skramle);
Array.findSimilarSelectors(\flip);
Array.findSimilarSelectors(\flip, maxEditDistance: 7);
```

### `dumpAllMethods`
Post all instance methods which instances of this class responds too, including inherited ones. `this.class.dumpAllMethods` will post all class methods which this class responds to.
```supercollider
Integer.dumpAllMethods
```

### `dumpByteCodes`
Dump the byte codes of the named method.
```supercollider
Integer.findMethod(\do).dumpByteCodes
```

### `dumpClassSubtree`
Post the tree of all Classes that inherit from this class.
```supercollider
Collection.dumpClassSubtree
```

### `dumpInterface`
Post all the methods defined in this Class and their arguments.
```supercollider
Array.dumpInterface
Array.class.dumpInterface
```

### `dumpFullInterface`
Post all the class and instance methods that this class responds to.
```supercollider
Array.dumpFullInterface
```

### `help`
Opens the help file for this Class if it exists. It may take a little while until the help window responds.
```supercollider
Array.help
```

### `helpFilePath`
Returns the path of this Class's helpfile as a String.
```supercollider
Array.helpFilePath
```

### `helpFileForMethod`
Opens the helpfile for the class in which the responding method is implemented.
```supercollider
Array.helpFileForMethod('select'); // This will open the Collection helpfile
```

### `asClass`
Return this.### `asString`
Return the name of the class as a String.
### Accessing
### `name`
A Symbol that is the name of the class.
### `nextclass`
The next class in a linked list of all classes.
```supercollider
Set.nextclass
```


### `superclass`
The Class from which this class directly inherits.
```supercollider
Set.superclass // Collection
```


### `superclasses`
An Array of this class's superclasses, going back to Object.
```supercollider
Set.superclasses // [class Collection, class Object]
```


### `subclasses`
An Array of the direct subclasses of this.
```supercollider
Set.subclasses // [class Dictionary, class IdentitySet]
```


### `allSubclasses`
An Array of all subclasses of this.
```supercollider
Set.allSubclasses
```


### `superclassesDo`
Call a function passing each superclass of the receiver.
```supercollider
List.superclassesDo { |x| x.postln };
```


### `methods`
An Array of the methods of this class.
```supercollider
Set.methods.do { |item| item.name.postln }
```


### `instVarNames`
An Array of the names of the instance variables for this class.
### `classVarNames`
An Array of the names of the class variables for this class.
### `iprototype`
An Array of the initial values of instance variables.
### `cprototype`
An Array of the initial values of class variables.
### `filenameSymbol`
A Symbol which is a path to the file which defines the Class.
```supercollider
Set.filenameSymbol
```




