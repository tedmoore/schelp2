# CmdPeriod

*register objects to be cleared when Cmd-. is pressed*

**Related:** [ShutDown](../Classes/ShutDown.md), [ServerQuit](../Classes/ServerQuit.md)

**Categories:** Control

## Description

CmdPeriod allows you to register objects to perform an action when the user presses Cmd-. These objects must implement a method called **-cmdPeriod** which performs the necessary tasks. (You can add such a method in your custom classes.) Note that since [Function](../Classes/Function.md) implements **-cmdPeriod** as a synonym for **-value**, it is possible to register any function (and thus any arbitrary code) for evaluation when Cmd-. is pressed.


## Class Methods


### `add`
Registers an object to be cleared when Cmd-. is pressed. This object will stay registered until it is explicitly removed, and will thus respond to additional presses of Cmd-.

### `remove`
Removes an object that was previously registered.

### `removeAll`
Removes all objects that have been registered.

### `doOnce`
Registers an object to be evaluated once, and then unregistered.

### `objects`
Get or set the list of objects that are called when CmdPeriod is evaluated.

### `era`
The number of times CmdPeriod has been called since startup.
## Examples


```
(
f = { "foo".postln };
g = { "bar".postln };
CmdPeriod.add(f);
CmdPeriod.add(g);
)

// Now press Cmd-.

CmdPeriod.remove(g);

// Now press Cmd-. Only f executes

CmdPeriod.remove(f); // must explicitly cleanup


// Now press Cmd-.

CmdPeriod.add(g); // one object is added only once.
CmdPeriod.add(g); // one object is added only once.


// Now press Cmd-.

// remove it again.
CmdPeriod.remove(g);


// note that often you want to automatically remove the function once it is evaluated
// instead of

f = { "foo".postln; CmdPeriod.remove(f) };
CmdPeriod.add(f);

// you can write:

CmdPeriod.doOnce { "foo".postln }

// a typical example:
(
w = Window.new("close on cmd-.").front;
CmdPeriod.doOnce { w.close };
)


// in some cases you might need to defer the function by a short amount of time
a = { Synth(\default) };
a.value;
CmdPeriod.add({ { a.value }.defer(0.01) });

// remove all
CmdPeriod.removeAll
```




