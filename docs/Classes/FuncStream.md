# FuncStream

*Stream of a function*

**Categories:** Streams-Patterns-Events

**Related:** [Pfunc](../Classes/Pfunc.md)

## Description

FuncStream is one of the most basic ways to describe a stream: it has a function that is called for each next stream value.

```supercollider
// make a stream that returns a random number
a = FuncStream({ 1.0.rand });
a.next;
```


It uses [Function#-inEnvir](../Classes/Function.md#-inenvir) to statically bind the function call to the environment in which the `FuncStream` was created.

```supercollider
a = Environment.use { ~x = 100; FuncStream({ ~x + 8 }) };
~x = 0;
a.next; // returns 108, not 8.
```




## Class Methods

### `new`
Return a new stream object.
```supercollider
(
var func, reset, count = 0;
func = { count = count + 2.rand };
reset = { count = 0 };
a = FuncStream(func, reset);
)

a.next;
a.nextN(80).plot;
a.reset;
a.next; // starts again.
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `nextFunc` | The function that is called on each next |  
| `resetFunc` | The function that is called on reset |  


## Instance Methods

### `next`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `inval` | Return the next value by calling the function. `inval` is passed as an argument to the function. |  
### `reset`
Call the reset function, if defined.### `envir`
Get or set the environment to which the function has been bound.### `nextFunc`
Get or set the function which is called on [#-next](#-next).### `resetFunc`
Get or set the function which is called on [#-reset](#-reset).
## Examples


```supercollider
(
// create 16 different series
a = {
    var diff = [2, 4, 5].choose * [1, -1].choose;
    var val = 0;
    var stream = FuncStream({
        // next function
        val = val + diff;
        if(abs(val) > 30) { stream.reset };
        val
    }, {
        // reset function
        val = 0
    });
    stream
}.dup(16);

// play them as parallel notes
fork {
    loop {
        (
            note: a.collect { |f| f.next.postln },
            sustain: 0.1
        ).play;

        // reset a randomly chosen FuncStream
        a.choose.reset;
        0.16.wait;
    }
}
)
```




