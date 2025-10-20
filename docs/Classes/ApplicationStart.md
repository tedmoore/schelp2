# ApplicationStart

*register functions to be evaluated on Application start*

**Related:** [StartUp](../Classes/StartUp.md), [ServerBoot](../Classes/ServerBoot.md)

**Categories:** Control, Platform>macOS

## Description

Available in macOS SuperCollider.app only.
ApplicationStart allows you to register functions or objects to perform an action only on application start. The functions will be evaluated last; After the library has been compiled, the startup file has run and StartUp actions have been evaluated.
See also [StartUp](../Classes/StartUp.md) for functions that are evaluated *every* time the ClassLibrary is recompiled.


## Class Methods


### `add`
Registers an object or function. Objects will be receive a **doOnApplcationStart** message on application start. Functions will be evaluated.

### `remove`
Removes a function that was previously registered.

### `run`
Evaluates the functions or objects in order.
## Examples


```
SomeStartClass {
    *initClass {
        ApplicationStart.add {
            // something to do when the app has been launched...
        }
    }
}

// or...
SomeStartClass {
    *initClass {
        ApplicationStart.add(this);
    }
    *doOnApplicationStart { "something started".postln }
}
```




