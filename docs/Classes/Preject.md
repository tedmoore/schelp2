# Preject

*Filters a source pattern by rejecting particular values.*

**Categories:** Streams-Patterns-Events>Patterns>Filter

**Related:** [Pselect](../Classes/Pselect.md), [Pcollect](../Classes/Pcollect.md), [Collection#-reject](../Classes/Collection#-reject.md)

## Description

Preject filters the source **pattern** using **func**. Values for which **func** returns true will not be returned by Preject.
This is the pattern library's equivalent of [Collection#-reject](../Classes/Collection.md#-reject).


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | A [Function](../Classes/Function.md). The function used to reject values. It should take a single parameter (the next value from `pattern`), and return a boolean. |  
| `pattern` | The [Pattern](../Classes/Pattern.md) to be filtered. |  

## Examples


```
(
var a, b;
a = Preject({ |item| item == 1 }, Pseq(#[1, 2, 3], inf));
x = a.asStream;
9.do({ x.next.postln });
)
```


The message reject returns a Preject when passed to a pattern

```
(
var a, b;
a = Pseq(#[1, 2, 3], inf).reject({ |item| item == 1 });
a.postln;
x = a.asStream;
9.do({ x.next.postln });
)
```




