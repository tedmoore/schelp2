# Pselect

*Filters values returned by a source pattern.*

**Categories:** Streams-Patterns-Events>Patterns>Filter

**Related:** [Pcollect](../Classes/Pcollect.md), [Preject](../Classes/Preject.md), [Collection#-select](../Classes/Collection#-select.md)

## Description

This pattern will filter the source pattern using the supplied function **func**.
Values from the source pattern will be passed to **func**. Pselect will only return that value if the **func** returns true.
This is the pattern library's equivalent of [select](../Classes/Collection.md#-select).


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | A [Function](../Classes/Function.md) that takes one parameter (the next value from **pattern**) and returns a boolean. |  
| `pattern` | The source [Pattern](../Classes/Pattern.md). |  

## Examples


```supercollider
(
var a, b;
a = Pselect({ |item| item != 2 }, Pseq(#[1, 2, 3], inf));
x = a.asStream;
9.do({ x.next.postln });
)
```


The message `select` returns a Pselect when passed to a pattern.

```supercollider
(
var a, b;
a = Pseq(#[1, 2, 3], inf).select({ |item| item != 2 });
a.postln;
x = a.asStream;
9.do({ x.next.postln });
)
```




