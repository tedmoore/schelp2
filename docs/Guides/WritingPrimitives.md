# Writing Primitives

*Writing Primitives*

**Categories:** Internals

Although much of SuperCollider's functionality is implemented in the SuperCollider language itself, for reasons of efficiency, some functionality is implemented in 'back end' C++ functions called 'primitives'. This document provides guidance to members of the SC development community on writing primitives.

## Example

### SuperCollider code
Primitive calls are preceded with an underscore, so for example `_myPrimitiveName`. Here is an example call to a primitive in an SC class:


```supercollider
Cocoa {
    prGetPathsDialog { arg returnSlot;
        _Cocoa_GetPathsDialog
        ^this.primitiveFailed
    }
}
```


In the example above the primitive is dispatched at `_Cocoa_GetPathsDialog`. If it is successful, it will return without executing the code below that. Primitive functions (see below) return an integer, which should be one of the values defined in the file *PyrErrors.h*:


If your primitive can return any value besides `errNone` then you will need to provide handling code after the primitive call. In most cases this will be `^this.primitiveFailed`. This will throw an `Error` giving the user information about what went wrong.

In some cases, you may wish to execute fallback SC code instead of throwing an `Error`. This can be useful in cases where for example a primitive provides an optimised version of a method which is not usable in all instances. Here is an example of how this can be done:


```supercollider
flop {
    _ArrayMultiChannelExpand
    ^super.flop // this gets executed if the primitive fails
}
```


Note that returning anything besides `errNone` will result in executing the SC method *ignoring* the primitive call. For this reason, if you need to do some preparatory work in SC before calling the primitive, it is best practice to do this in a separate method to avoid duplication. For example:


```supercollider
// do initial work here
openUDPPort {|portNum|
    var result;
    if(openPorts.includes(portNum), {^true});
    result = this.prOpenUDPPort(portNum);
    if(result, { openPorts = openPorts.add(portNum); });
    ^result;
}

// this method only calls the primitive, and throws any primitive errors
prOpenUDPPort {|portNum|
    _OpenUDPPort
    ^this.primitiveFailed;
}
```





### Define your primitive
In your primitive source code define the primitive:


Here is the prototype for `definePrimitive`:


The `numArgs` is the number of arguments that were passed into the SuperCollider method that calls the primitive, plus one to include the receiver which is passed in as the first argument.

(TODO varArgs ...)




### Write your primitive
`g->sp` is the top of the stack and is the last argument pushed. `g->sp - inNumArgsPushed + 1` is the receiver and where the result goes.

In this example, the `numArgsPushed` will be 2 (as specified in `definePrimitive`)


This example does not set the receiver, so the primitive returns the original receiver unchanged (still an instance of `Cocoa`). Or set the object at `receiver` which again is at `(g->sp - numArgsPushed + 1)`.





## Guidelines

### Creating objects in primitives, and GC safety
SuperCollider uses a garbage collector to manage memory allocation and collection where needed.> *Some SC language objects, such as numbers, boolean types, chars, and symbols are stored directly within a PyrSlot, and do not require allocation. (Symbols are a special case: A reference to a location in the global symbol table is stored, where each defined symbol is permanently stored.)* In order to meet the requirements of good real time performance, a small and bounded amount of garbage collection may be triggered each time an object is created. This consists of incrementally examining all objects and determining if they are reachable (see below) or not. Unreachable objects may have their memory reallocated to new objects.

The following points are important to understanding how the GC works, and how to avoid bugs:

- An object is *reachable* if it has- been stored on the stack, or
- been stored in an sclang variable, or a class variable, or
- been stored in another object that fulfills one of the above criteria

- The GC marks objects as one of the following:- **White** - To be examined
- **Grey** - Reachable, but containing objects which themselves have not been fully inspected and marked grey or black
- **Black** - Reachable, with any contained objects all fully inspected
- **Free** - Unreachable; memory is available for reuse

- If triggered, garbage collection will happen *before* allocating the new object.
- The newly created object will be marked as **white** (to be examined).


SC provides a number of functions which create new objects. These include `instantiateObject`, `newPyrObject`, `newPyrString`, and `newPyrArray`. Before any calls to such functions it is crucial that all previously created objects have been made reachable. If this is not done, it is possible that such objects will be marked as **free**. Since a freed object's memory may not be immediately reused, problems may not arise at the time your primitive is called, leading to extremely hard to find bugs.

Alternatively, most object creation functions include a `bool runGC` argument. If set to false, this will guarantee that the garbage collector does not run on this allocation. While not ideal, as it is best that GC activity is amortised to the extent possible, this option is safe, since the status of any previously created objects will not be changed.

The following two examples are both safe:


**Make the newly created object reachable:**
: 

**Set `runGC` to false:**
: 



One caveat: When making a new object reachable by storing it on the stack, you must ensure that you are not overwriting objects that will be needed later in the primitive. If this is done the receiver may be collected on any future allocations. One solution is to **push** the object onto the stack, and then pop it when finished, e.g.:


`prArrayMultiChanExpand` in *lang/LangPrimSource/PyrListPrim.cpp* gives an example of this approach. Setting `runGC` to `false` is another possible solution.

Similarly, care must be taken when writing utility functions which themselves create new objects, since this may happen somewhat opaquely and the calling context may not be known. Functions which may call themselves recursively also need special attention. In such cases setting `runGC` to `false` may be the safest option, or including a `runGC` arg so that GC behaviour is explicit. `MsgToInt8Array` is one example of such a function.


Setting an object into another object's internal slot (e.g. with `SetObject` or `slotCopy`) also requires care. If the parent object is *black* (reachable and examined), the GC needs to be notified of the change. For this reason, you must usually call `g->gc->GCWrite(parentObject, childObject)` after using one of these methods. The *only* exceptions to this rule are cases in which the parent object is known to be white (unexamined). This will be true if:

- It is the last created object, or
- Any subsequently created objects were allocated with `runGC = false` (i.e. the GC cannot have run in the interim), *and*
- It has not had `GCWrite` called upon it


The following two examples are both safe:


**Run `GCWrite` as parent may not be white:**
: 

**We know that parent *is* white:**
: 



If you *know* that the child object is still white, then you can use `GCWriteNew` instead of `GCWrite`. The child object will still be white if the GC has not been triggered since it was created, and you have not previously called `GCWrite` on it.

If placing an object inside another has modified its size (e.g. adding an object to an array), you must correctly adjust its size by `parent->size = newSize`. Both this and calling `GCWrite` (if necessary) should be done before any further object allocations. It is best practice to do them immediately if possible.


**This is safe:**
: 

**This is *not* safe:**
: 



It is good practice to avoid creating objects in a primitive at all where possible. Primitives are much simpler to write and debug if you pass in an object that you create in SC code and fill in its slots in the primitive.


> **Note:** To summarize, before calling any function that might allocate (like `newPyr*`) you **must** make sure these criteria are fulfilled:1. All objects previously created must be reachable, which means they must exist- on the `g->sp` stack (taking care not to overwrite any objects which will be needed later)
- or, in a lang-side variable or class variable.
- or, in a slot of another object that fulfils these criteria.

2. If any object ( `child` ) was put inside a slot of another object ( `parent` ), you must have- called `g->gc->GCWrite(parent, child)` afterwards unless you **know** that the parent is still white (unexamined), or `GCWriteNew` if you also **know** that the child is white
- and, set `parent->size` to the correct value


Here's an example of how a complete primitive might look:


If we would have put `SetObject(arg, array);` at the end of this function, `array` would **not** have been reachable at the call to `newPyrString`, and thus may have been marked `free`, resulting in a hard to track down bug.

> **⚠️ Warning:** Do not store pointers to `PyrObject`s in C/C++ variables unless you can absolutely guarantee that they cannot be garbage collected. For example the `File` and `SCWindow` classes do this by storing the objects in an array in a `classvar`. The object has to stay in that array until no C object refers to it. **Failing to observe the above two points can result in very hard to find bugs.**



### Type safety
Since SC is dynamically typed, you cannot rely on any of the arguments being of the class you expect. You should check every argument to make sure it is the correct type.

One way to do this is by using `isKindOfSlot`. If you just want a numeric value, you can use `slotIntVal`, `slotFloatVal`, or `slotDoubleVal` which will return an error if the value is not a numeric type. Similarly there is `slotStringVal`.

It is safe to assume that the receiver will be of the correct type because this is ensured by the method dispatch mechanism.





## FAQ

**Now where do I put the thing to return it?**
: Store your return value at `g->sp - inNumArgsPushed + 1`. (In most primitives this is referred to by the variable `a`.)







