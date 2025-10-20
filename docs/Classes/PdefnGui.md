# PdefnGui

*a simple gui for Pdefns*

**Categories:** JITLib>GUI, Live Coding

**Related:** [Pdefn](../Classes/Pdefn.md), [PdefnAllGui](../Classes/PdefnAllGui.md), [TdefAllGui](../Classes/TdefAllGui.md)

## Description

PdefnGui displays a PdefnGui, and allows editing and evaluating its code.


## Class Methods


### `observedClass`
Pdefn

## Instance Methods

**JITGui methods:**
### `accepts`
test whether object can be displayed
### `getState`, `checkUpdate`

## Examples


```
g = PdefnGui();
Pdefn(\abc, [1, 2, 3]);
g.object_(Pdefn(\abc));
Pdefn(\abc, 345);

// Note: When editing code in the csView and evaluating,
// there is a short delay before displaying. this is intended.
```




