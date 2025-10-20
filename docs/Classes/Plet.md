# Plet

*Define a value within the scope (namespace) of a Plambda*

**Categories:** Streams-Patterns-Events>Patterns>Data Sharing

**Related:** [Plambda](../Classes/Plambda.md), [Pget](../Classes/Pget.md)

## Description

[Plet](../Classes/Plet.md)/[Pget](../Classes/Pget.md) are used to share data between patterns inside of a [Plambda](../Classes/Plambda.md)
Plet defines a variable containing a pattern or data for sharing within the scope of a [Plambda](../Classes/Plambda.md). 
Using the [Pget](../Classes/Pget.md) class, the contents of this variable can then be accessed by key in other patterns within the [Plambda](../Classes/Plambda.md).


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `key` | The name of the variable |  
| `pattern` | The contents of the variable |  
| `return` | If return is nil, the pattern will be returned. If not nil, the contents of the return argument will be returned while the variable defined by the Plet will be set to the value of pattern |  


## Instance Methods


### `storeArgs`

### `embedInStream`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `inval` |  |  

### `pattern`

### `silent`

### `key`

### `return`

## Examples


```
(
    /*

    Two patterns playing in parallel, 
    sharing data between eachother

    */

    // a melody playing random scale degrees
    a = Pbind(
        \dur, 0.125, 
        \octave, 4,
        \degree, Plet(\melody, pattern: Pwhite(0, 7))
    );

    // the bass, scale degrees sampled from the \melody variable defined above 
    b = Pbind(
        \dur, 0.5, 
        \octave, 3,
        \degree, Pget(\melody, default: 1, repeats: inf).trace
    );

    // Play the patterns in parallel
    Plambda(
        Ppar([a, b], inf)
    ).play;
)
```




