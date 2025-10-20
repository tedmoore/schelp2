# Penvir

*use an environment when embedding the pattern in a stream*

**Related:** [Pkey](../Classes/Pkey.md)

**Categories:** Streams-Patterns-Events>Patterns>Data Sharing


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `envir` | an environment with objects to embed. |  
| `pattern` | pattern or stream, usually a [Pfunc](../Classes/Pfunc.md), [Prout](../Classes/Prout.md). |  
| `independent` | if true streams can write to the environment without influencing other streams created from this pattern. if false, the streams write to a common namespace. |  

## Examples


```
(
x = (a: 8);
y = Penvir(
    x,
    Pfunc { ~a * 2 }
);

t = y.asStream;
)

t.next;



(
x = (a: 8);
y = Penvir(
    x,
    Pfunc { ~a = ~a * 2 }
);

t = y.asStream;
z = y.asStream;
)

t.next;
t.next;
x.postln;    // x stays unchanged
```




