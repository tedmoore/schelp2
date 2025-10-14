# Pwhile

*While a condition holds, repeatedly embed stream*

**Categories:** Streams-Patterns-Events>Patterns>Language Control

## Description

Repeatedly **embed** a [Stream](../Classes/Stream.md) while the result of `func` is `true`.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | Stream function. In an event stream receives the current [Event](../Classes/Event.md) as argument. |  
| `pattern` | A [Pattern](../Classes/Pattern.md). |  

## Examples


```supercollider
(
z = true;
a = Pwhile({ z }, Pseq(#[1, 2, 3]));
x = a.asStream;
);

7.do({ x.next.postln }); // while z == true, the values are embedded
z = false; // set z to false
x.next; // the rest of the stream is still embedded
x.next;
x.next; // but then it is not continued.
x.next;
x.next;
x.next;
```




