# Pkey

*access a key in an event stream*

**Related:** [Penvir](../Classes/Penvir.md)

**Categories:** Streams-Patterns-Events>Patterns>Data Sharing

## Description

Pkey simplifies backward access to values in an event being processed by [Pbind](../Classes/Pbind.md) or another event pattern.


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `key` | The name of the event variable to read from. |  
| `repeats` | The number of items returned before finishing. Using `nil`, the default value, makes the stream infinite. |  

## Examples


```
// \b should thus take twice the value of \a in each event:
p = Pbind(\a, Pwhite(1, 10, inf), \b, Pkey(\a) * 2).asStream;


p.next(())    // for Pbind, must pass in a default event even if empty

('a': 10, 'b': 20)
('a': 2, 'b': 4)
('a': 5, 'b': 10)
('a': 4, 'b': 8)
('a': 2, 'b': 4)

// note: to check if a Pkey's result /equals/ another value,
// be sure to use |==|
p = Pbind(
    \a, Pseries(1, 1, inf),
    \b, Pif(
        Pkey(\a) == 2,
        "equals 2",
        "nope"
    )
).asStream;

p.next(());  // 'b' is always "nope"

p = Pbind(
    \a, Pseries(1, 1, inf),
    \b, Pif(
        Pkey(\a) |==| 2,
        "equals 2",
        "nope"
    )
).asStream;

p.next(());  // 'b' is as expected
```




