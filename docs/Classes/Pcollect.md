# Pcollect

*Apply a function to a pattern*

**Categories:** Streams-Patterns-Events>Patterns>Filter

**Related:** [Pselect](../Classes/Pselect.md), [Preject](../Classes/Preject.md)

## Description

Modifies each value by passing it to the function. This is the pattern library's equivalent of [Collection#-collect](../Classes/Collection.md#-collect).


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | A [Function](../Classes/Function.md). Receives values from `pattern`. |  
| `pattern` | A [Pattern](../Classes/Pattern.md). |  

## Examples


```
(
a = Pcollect({ |item| item * 3 }, Pseq(#[1, 2, 3], inf));
x = a.asStream;
9.do({ x.next.postln });
)
```


The message `collect` returns a Pcollect when passed to a pattern. Note that because the pattern is converted to a [Stream](../Classes/Stream.md) (more precisely a [FuncStream](../Classes/FuncStream.md)) the collect function is evaluated for one item each time the message `next` is passed.

```
(
a = Pseq(#[1, 2, 3], inf).collect({ |item| item * 3 });
a.postln;

x = a.asStream;
9.do({ x.next.postln });
)
```




