# Pget

*Retrieve a value within the scope (namespace) of a Plambda*

**Categories:** Streams-Patterns-Events>Patterns>Data Sharing

**Related:** [Plambda](../Classes/Plambda.md), [Plet](../Classes/Plet.md)

## Description

[Pget](../Classes/Pget.md) retrieves the value of a [Plet](../Classes/Plet.md).  [Plet](../Classes/Plet.md)/[Pget](../Classes/Pget.md) are used to share data between patterns inside of a [Plambda](../Classes/Plambda.md)


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `key` | The name of the variable |  
| `default` | default value if none is defined by a paired [Plet](../Classes/Plet.md) |  
| `repeats` |  |  


## Instance Methods


### `default`

### `storeArgs`

### `key`

### `repeats`

### `embedInStream`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `inval` |  |  

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




