# Pprotect

*evaluate a function when an error occured in the thread*

**Related:** [Ptrace](../Classes/Ptrace.md)

**Categories:** Streams-Patterns-Events>Patterns>Language Control


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `pattern` | any pattern |  
| `func` | a [Function](../Classes/Function.md) to be evaluated when an error occurs. The error and the thread are passed as arguments to the function. |  

## Examples


```
(
var x;
var func = { "an error happened".postln };
a = Pprotect(Pseq([1, 3, 3, Pfuncn({ Error.new.throw }), 2]), func);
x = Pbind(\degree, a, \dur, 0.5).play;
)
```




